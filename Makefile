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

.PHONY: help
help: ## Describe useful make targets
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "%-15s %s\n", $$1, $$2}'

.PHONY: all
all: test conformance

.PHONY: clean
clean: ## Delete intermediate build artifacts
	@# -X only removes untracked files, -d recurses into directories, -f actually removes files/dirs
	git clean -Xdf

.PHONY: generate
generate: $(BIN)/buf ## Regenerate code and license headers
	rm -rf gen
	$(BIN)/buf generate buf.build/bufbuild/protovalidate
	$(BIN)/buf generate buf.build/bufbuild/protovalidate-testing
	$(MAKE) generate-license

.PHONY: format
format: install ## Format code
	$(PYTHON) -m isort protovalidate tests
	$(PYTHON) -m black protovalidate tests
	$(MAKE) generate-license

.PHONY: test
test: generate install ## Run all unit tests
	pipenv run pytest

.PHONY: conformance
conformance: $(BIN)/protovalidate-conformance install
	$(BIN)/protovalidate-conformance $(CONFORMANCE_ARGS) pipenv -- run $(PYTHON) -m tests.conformance.runner

.PHONY: install
install:
	$(PYTHON) -m pip install --upgrade pip
	pip install pipenv ruff mypy types-protobuf black isort
	pipenv --python $(PYTHON) install

.PHONY: checkgenerate
checkgenerate: generate
	@# Used in CI to verify that `make generate` doesn't produce a diff.
	test -z "$$(git status --porcelain | tee /dev/stderr)"

.PHONY: generate-license
generate-license: $(BIN)/license-header
	$(BIN)/license-header \
		--license-type apache \
		--copyright-holder "Buf Technologies, Inc." \
		--year-range "$(COPYRIGHT_YEARS)" $(LICENSE_IGNORE)

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
