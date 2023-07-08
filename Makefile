# See https://tech.davis-hansson.com/p/make/
SHELL := bash
.DELETE_ON_ERROR:
.SHELLFLAGS := -eu -o pipefail -c
.DEFAULT_GOAL := all
MAKEFLAGS += --warn-undefined-variables
MAKEFLAGS += --no-builtin-rules
MAKEFLAGS += --no-print-directory
BIN := .tmp/bin
COPYRIGHT_YEARS := 2023
LICENSE_IGNORE :=
LICENSE_HEADER_VERSION := 59c69fa4ddbd56c887cb178a03257cd3908ce518
# Set to use a different compiler. For example, `GO=go1.18rc1 make test`.
GO ?= go
# Set to use a different Python interpreter. For example, `PYTHON=python make test`.
PYTHON ?= python3
CONFORMANCE_ARGS ?= --strict --expected_failures=nonconforming.yaml
LICENSE_HEADER := $(BIN)/license-header \
		--license-type apache \
		--copyright-holder "Buf Technologies, Inc." \
		--year-range "$(COPYRIGHT_YEARS)"

.PHONY: help
help: ## Describe useful make targets
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "%-15s %s\n", $$1, $$2}'

.PHONY: all
all: test lint ## Run all tests and lint (default)

.PHONY: clean
clean: ## Delete intermediate build artifacts
	@# -X only removes untracked files, -d recurses into directories, -f actually removes files/dirs
	git clean -Xdf

.PHONY: generate
generate: $(BIN)/buf ## Regenerate code and license headers
	rm -rf gen
	$(BIN)/buf generate buf.build/bufbuild/protovalidate
	$(BIN)/buf generate buf.build/bufbuild/protovalidate-testing
	$(LICENSE_HEADER) --ignore __init__.py

.PHONY: format
format: install ## Format code
	$(LICENSE_HEADER)
	pipenv run black protovalidate tests
	pipenv run ruff --fix protovalidate tests

.PHONY: test
test: $(BIN)/protovalidate-conformance generate install ## Run unit and conformance tests
	pipenv run pytest
	$(BIN)/protovalidate-conformance $(CONFORMANCE_ARGS) pipenv -- run $(PYTHON) -m tests.conformance.runner

.PHONY: lint
lint: install ## Lint code
	pipenv run black --check --diff protovalidate tests
	pipenv run mypy protovalidate
	pipenv run ruff protovalidate tests
	pipenv verify

.PHONY: install
install: ## Install dependencies
	$(PYTHON) -m pip install --upgrade pip pipenv
	pipenv --python $(PYTHON) sync

.PHONY: checkgenerate
checkgenerate: generate
	@# Used in CI to verify that `make generate` doesn't produce a diff.
	test -z "$$(git status --porcelain | tee /dev/stderr)"

$(BIN):
	@mkdir -p $(BIN)

$(BIN)/buf: $(BIN) Makefile
	GOBIN=$(abspath $(@D)) $(GO) install github.com/bufbuild/buf/cmd/buf@latest

$(BIN)/license-header: $(BIN) Makefile
	GOBIN=$(abspath $(@D)) $(GO) install \
		  github.com/bufbuild/buf/private/pkg/licenseheader/cmd/license-header@$(LICENSE_HEADER_VERSION)

$(BIN)/protovalidate-conformance: $(BIN) Makefile
	GOBIN=$(abspath $(BIN)) $(GO) install \
    	github.com/bufbuild/protovalidate/tools/protovalidate-conformance@latest
