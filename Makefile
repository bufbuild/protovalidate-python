# See https://tech.davis-hansson.com/p/make/
SHELL := bash
.DELETE_ON_ERROR:
.SHELLFLAGS := -eu -o pipefail -c
.DEFAULT_GOAL := all
MAKEFLAGS += --warn-undefined-variables
MAKEFLAGS += --no-builtin-rules
MAKEFLAGS += --no-print-directory
BIN := .tmp/bin
export PATH := $(BIN):$(PATH)
export GOBIN := $(abspath $(BIN))
export PYTHONPATH ?= gen
CONFORMANCE_ARGS ?= --strict_message --expected_failures=test/conformance/nonconforming.yaml --timeout 10s
ADD_LICENSE_HEADER := $(BIN)/license-header \
		--license-type apache \
		--copyright-holder "Buf Technologies, Inc." \
		--year-range "2023-2025"
# This version should be kept in sync with the version in buf.yaml
PROTOVALIDATE_VERSION ?= v1.0.0
# Version of the cel-spec that this implementation is conformant with
CEL_SPEC_VERSION ?= v0.24.0
TESTDATA_FILE := test/testdata/string_ext.textproto

.PHONY: help
help: ## Describe useful make targets
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "%-15s %s\n", $$1, $$2}'

.PHONY: all
all: test conformance lint ## Run all tests and lint (default)

.PHONY: clean
clean: ## Delete intermediate build artifacts
	@# -X only removes untracked files, -d recurses into directories, -f actually removes files/dirs
	git clean -Xdf

.PHONY: generate
generate: generate-protovalidate-pypi-package generate-protobuf-tests $(BIN)/license-header  ## Regenerate code and license headers
	$(ADD_LICENSE_HEADER)

.PHONY: generate-protobuf-tests
generate-protobuf-tests: $(BIN)/buf ## Regenerate protobuf gencode used in unit tests
	rm -rf test/gen
	# generate protovalidate-testing into test/gen/buf/validate
	$(BIN)/buf generate buf.build/bufbuild/protovalidate-testing:$(PROTOVALIDATE_VERSION)
	
	# generate cel-spec into test/gen/cel/expr
	$(BIN)/buf generate buf.build/google/cel-spec:$(CEL_SPEC_VERSION) --exclude-path cel/expr/conformance/proto2 --exclude-path cel/expr/conformance/proto3
	# we need to update the `from cel.expr` imports in those generated files to `from test.gen.cel.expr`
	LC_ALL=C find test/gen/cel -type f -exec sed -i "" 's/from cel.expr/from test.gen.cel.expr/g' {} +

	# generate proto/tests/example/v1/validations.proto into test/gen/tests/example/v1
	$(BIN)/buf generate

.PHONY:
generate-protovalidate-pypi-package: $(BIN)/buf  ## Regenerate protobuf gencode for the bufbuild-protovalidate-protocolbuffers pypi package
	rm -rf bufbuild-protovalidate-protocolbuffers/buf/validate/proto5
	rm -rf bufbuild-protovalidate-protocolbuffers/buf/validate/proto6
	# generate gencode for both proto5 and proto6 for buf.build/bufbuild/protovalidate
	cd bufbuild-protovalidate-protocolbuffers && ../$(BIN)/buf generate buf.build/bufbuild/protovalidate:$(PROTOVALIDATE_VERSION)

	# set the version of bufbuild-protovalidate-protocolbuffers to the used PROTOVALIDATE_VERSION
	sed -i '' 's/^version = "[^"]*"/version = "$(PROTOVALIDATE_VERSION)"/' bufbuild-protovalidate-protocolbuffers/pyproject.toml

.PHONY: format
format: install $(BIN)/buf $(BIN)/license-header ## Format code
	$(ADD_LICENSE_HEADER)
	buf format --write .
	uv run -- ruff format protovalidate test
	uv run -- ruff check --fix protovalidate test

.PHONY: test
test: generate install $(TESTDATA_FILE) ## Run unit tests
	uv run -- pytest

.PHONY: conformance
conformance: $(BIN)/protovalidate-conformance generate install ## Run conformance tests
	protovalidate-conformance $(CONFORMANCE_ARGS) uv run test/conformance/runner.py

.PHONY: lint
lint: install $(BIN)/buf ## Lint code
	buf format -d --exit-code
	uv run -- ruff format --check --diff protovalidate test
	uv run -- mypy protovalidate
	uv run -- ruff check protovalidate test
	uv lock --check

.PHONY: install
install: ## Install dependencies
	uv sync --dev

.PHONY: checkgenerate
checkgenerate: generate
	@# Used in CI to verify that `make generate` doesn't produce a diff.
	test -z "$$(git status --porcelain | tee /dev/stderr)"

$(TESTDATA_FILE):
	mkdir -p $(dir @)
	curl -fsSL -o $@ https://raw.githubusercontent.com/google/cel-spec/refs/tags/$(CEL_SPEC_VERSION)/tests/simple/testdata/string_ext.textproto

$(BIN):
	@mkdir -p $(BIN)

$(BIN)/buf: $(BIN) Makefile
	go install github.com/bufbuild/buf/cmd/buf@latest

$(BIN)/license-header: $(BIN) Makefile
	go install github.com/bufbuild/buf/private/pkg/licenseheader/cmd/license-header@latest

$(BIN)/protovalidate-conformance: $(BIN) Makefile
	go install github.com/bufbuild/protovalidate/tools/protovalidate-conformance@$(PROTOVALIDATE_VERSION)
