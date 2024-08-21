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
# Set to use a different Python interpreter. For example, `PYTHON=python make test`.
PYTHON ?= python3
export PYTHONPATH ?= gen
CONFORMANCE_ARGS ?= --strict --strict_message --expected_failures=tests/conformance/nonconforming.yaml --timeout 10s
ADD_LICENSE_HEADER := $(BIN)/license-header \
		--license-type apache \
		--copyright-holder "Buf Technologies, Inc." \
		--year-range "2023-2025"
PROTOVALIDATE_VERSION ?= v0.10.0

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
	buf generate buf.build/bufbuild/protovalidate:$(PROTOVALIDATE_VERSION)
	buf generate buf.build/bufbuild/protovalidate-testing:$(PROTOVALIDATE_VERSION)
	$(ADD_LICENSE_HEADER)

.PHONY: format
format: install $(BIN)/license-header ## Format code
	$(ADD_LICENSE_HEADER)
	uv run -- ruff format protovalidate tests
	uv run -- ruff check --fix protovalidate tests

.PHONY: test
test: $(BIN)/protovalidate-conformance generate install ## Run unit tests
	uv run -- pytest

.PHONY: conformance
conformance: $(BIN)/protovalidate-conformance generate install ## Run conformance tests
	protovalidate-conformance $(CONFORMANCE_ARGS) uv -- run --python $(PYTHON) python3 -m tests.conformance.runner

.PHONY: lint
lint: install ## Lint code
	uv run -- ruff format --check --diff protovalidate tests
	uv run -- mypy protovalidate
	uv run -- ruff check protovalidate tests
	uv sync --locked

.PHONY: install
install: ## Install dependencies
	uv sync --python $(PYTHON) --dev

.PHONY: checkgenerate
checkgenerate: generate
	@# Used in CI to verify that `make generate` doesn't produce a diff.
	test -z "$$(git status --porcelain | tee /dev/stderr)"

$(BIN):
	@mkdir -p $(BIN)

$(BIN)/buf: $(BIN) Makefile
	go install github.com/bufbuild/buf/cmd/buf@latest

$(BIN)/license-header: $(BIN) Makefile
	go install github.com/bufbuild/buf/private/pkg/licenseheader/cmd/license-header@latest

$(BIN)/protovalidate-conformance: $(BIN) Makefile
	go install github.com/bufbuild/protovalidate/tools/protovalidate-conformance@$(PROTOVALIDATE_VERSION)
