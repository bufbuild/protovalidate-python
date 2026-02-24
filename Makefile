# See https://tech.davis-hansson.com/p/make/
SHELL := bash
.DELETE_ON_ERROR:
.SHELLFLAGS := -eu -o pipefail -c
.DEFAULT_GOAL := all
MAKEFLAGS += --warn-undefined-variables
MAKEFLAGS += --no-builtin-rules
MAKEFLAGS += --no-print-directory
BUF_VERSION := 1.62.1
BUF := go run github.com/bufbuild/buf/cmd/buf@v$(BUF_VERSION)
ADD_LICENSE_HEADER := go run github.com/bufbuild/buf/private/pkg/licenseheader/cmd/license-header@v${BUF_VERSION} \
		--license-type apache \
		--copyright-holder "Buf Technologies, Inc." \
		--year-range "2023-2025"
CONFORMANCE_ARGS ?= --strict_message --expected_failures=test/conformance/nonconforming.yaml --timeout 10s
PROTOVALIDATE_VERSION ?= 895eefca6d1346f742fc18b9983d40478820906d
PROTOVALIDATE_CONFORMANCE := go run github.com/bufbuild/protovalidate/tools/protovalidate-conformance@$(PROTOVALIDATE_VERSION)
# Version of the cel-spec that this implementation is conformant with
# This should be kept in sync with the version in test/test_format.py
CEL_SPEC_VERSION ?= v0.25.1
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
	@echo $(CEL_SPEC_VERSION)

.PHONY: generate
generate:  ## Regenerate code and license headers
	rm -rf test/gen
	(cd test && $(BUF) generate)
	uv run -- ruff check --fix test/gen
	uv run -- ruff format test/gen
	$(ADD_LICENSE_HEADER)

.PHONY: format
format:  ## Format code
	$(ADD_LICENSE_HEADER)
	$(BUF) format --write .
	uv run -- ruff check --fix protovalidate test
	uv run -- ruff format protovalidate test

.PHONY: test
test: $(TESTDATA_FILE) ## Run unit tests
	uv run -- pytest

.PHONY: conformance
conformance: generate ## Run conformance tests
	$(PROTOVALIDATE_CONFORMANCE) $(CONFORMANCE_ARGS) uv run test/conformance/runner.py

.PHONY: lint
lint: ## Lint code
	$(BUF) format -d --exit-code
	uv run -- ruff format --check --diff protovalidate test
	uv run -- mypy protovalidate
	uv run -- ruff check protovalidate test
	uv lock --check

.PHONY: checkgenerate
checkgenerate: generate
	@# Used in CI to verify that `make generate` doesn't produce a diff.
	test -z "$$(git status --porcelain | tee /dev/stderr)"

$(TESTDATA_FILE):
	mkdir -p $(dir @)
	curl -fsSL -o $@ https://raw.githubusercontent.com/google/cel-spec/refs/tags/$(CEL_SPEC_VERSION)/tests/simple/testdata/string_ext.textproto
