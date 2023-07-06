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
ARGS ?= --strict --expected_failures=nonconforming.yaml

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
generate: generate-proto generate-license ## Regenerate code and license headers

.PHONY: generate-license
generate-license: $(BIN)/license-header format-black ## Format code and regenerate license headers
	$(BIN)/license-header \
		--license-type apache \
		--copyright-holder "Buf Technologies, Inc." \
		--year-range "$(COPYRIGHT_YEARS)" $(LICENSE_IGNORE)

.PHONY: generate-proto
generate-proto: $(BIN)/buf ## Regenerate code from proto files
	rm -rf gen
	$(BIN)/buf generate buf.build/bufbuild/protovalidate
	$(BIN)/buf generate buf.build/bufbuild/protovalidate-testing

.PHONY: format  ## Format all code
format: generate-license

.PHONY: format-black
format-black: install  ## Format all code according to black
	python3 -m black protovalidate tests

.PHONY: test
test: generate install ## Run all unit tests
	pipenv run pytest

.PHONY: conformance
conformance: $(BIN)/protovalidate-conformance install
	$(BIN)/protovalidate-conformance $(ARGS) pipenv -- run python3 -m tests.conformance.runner

.PHONY: install
install:
	python3 -m pip install --upgrade pip
	pip install pipenv ruff mypy types-protobuf black
	pipenv --python python3 install

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
