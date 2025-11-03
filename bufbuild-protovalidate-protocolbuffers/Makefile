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
CONFORMANCE_ARGS ?= --strict_message --expected_failures=test/conformance/nonconforming.yaml --timeout 10s
ADD_LICENSE_HEADER := $(BIN)/license-header \
		--license-type apache \
		--copyright-holder "Buf Technologies, Inc." \
		--year-range "2023-2025"
PROTOVALIDATE_VERSION ?= v1.0.0

.PHONY: help
help: ## Describe useful make targets
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "%-15s %s\n", $$1, $$2}'

.PHONY: all
all: build

.PHONY: generate
generate: $(BIN)/buf $(BIN)/license-header  ## Regenerate protobuf gencode for the bufbuild-protovalidate-protocolbuffers pypi package
	rm -rf buf/validate/proto5
	rm -rf buf/validate/proto6
	# generate gencode for both proto5 and proto6 for buf.build/bufbuild/protovalidate
	$(BIN)/buf generate buf.build/bufbuild/protovalidate:$(PROTOVALIDATE_VERSION)

	# add license headers to the source files
	$(ADD_LICENSE_HEADER)

	# set the version of bufbuild-protovalidate-protocolbuffers to the used PROTOVALIDATE_VERSION
	uv version $(PROTOVALIDATE_VERSION)

build: generate
	uv build

$(BIN):
	@mkdir -p $(BIN)

$(BIN)/buf: $(BIN) Makefile
	go install github.com/bufbuild/buf/cmd/buf@latest

$(BIN)/license-header: $(BIN) Makefile
	go install github.com/bufbuild/buf/private/pkg/licenseheader/cmd/license-header@latest
