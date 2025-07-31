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
PROTOVALIDATE_VERSION ?= v0.14.0
# Version of the cel-spec that this implementation is conformant with
# This should be kept in sync with the version in format_test.py
CEL_SPEC_VERSION ?= v0.24.0
TESTDATA_FILE := test/testdata/string_ext_$(CEL_SPEC_VERSION).textproto

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
generate: $(BIN)/buf $(BIN)/license-header ## Regenerate code and license headers
	rm -rf gen
	$(BIN)/buf generate buf.build/bufbuild/protovalidate:$(PROTOVALIDATE_VERSION)
	$(BIN)/buf generate buf.build/bufbuild/protovalidate-testing:$(PROTOVALIDATE_VERSION)
	$(BIN)/buf generate buf.build/google/cel-spec:$(CEL_SPEC_VERSION) --exclude-path cel/expr/conformance/proto2 --exclude-path cel/expr/conformance/proto3
	$(BIN)/buf generate
	$(ADD_LICENSE_HEADER)

.PHONY: format
format: install $(BIN)/license-header ## Format code
	$(ADD_LICENSE_HEADER)
	uv run -- ruff format protovalidate test
	uv run -- ruff check --fix protovalidate test

.PHONY: test
test: generate install gettestdata ## Run unit tests
	uv run -- python -m unittest
	$(MAKE) testextra

.PHONY: testextra
testextra:
	uv sync --extra re2
	uv run -- python -m unittest

.PHONY: conformance
conformance: $(BIN)/protovalidate-conformance generate install ## Run conformance tests
	protovalidate-conformance $(CONFORMANCE_ARGS) uv -- run python3 -m test.conformance.runner

.PHONY: lint
lint: install ## Lint code
	uv run -- ruff format --check --diff protovalidate test
	uv run -- mypy protovalidate
	uv run -- ruff check protovalidate test
	uv sync --locked

.PHONY: install
install: ## Install dependencies
	uv sync --dev

.PHONY: checkgenerate
checkgenerate: generate
	@# Used in CI to verify that `make generate` doesn't produce a diff.
	test -z "$$(git status --porcelain | tee /dev/stderr)"

.PHONY: gettestdata
gettestdata: $(TESTDATA_FILE)

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
