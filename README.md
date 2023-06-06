# protovalidate-py

[![CI](https://github.com/bufbuild/protovalidate-py/actions/workflows/ci.yaml/badge.svg)](https://github.com/bufbuild/protovalidate-py/actions/workflows/ci.yaml)
[![Conformance](https://github.com/bufbuild/protovalidate-py/actions/workflows/conformance.yaml/badge.svg)](https://github.com/bufbuild/protovalidate-py/actions/workflows/conformance.yaml)
[![Report Card](https://goreportcard.com/badge/github.com/bufbuild/protovalidate-py)](https://goreportcard.com/report/github.com/bufbuild/protovalidate-py)
[![PyPI version](https://badge.fury.io/py/protovalidate-py.svg)](https://badge.fury.io/py/protovalidate-py)

`protovalidate-py` is the Python implementation of [`protovalidate`](https://github.com/bufbuild/protovalidate), designed to validate Protobuf messages at runtime based on user-defined validation constraints. Powered by Google's Common Expression Language ([CEL](https://github.com/google/cel-spec)), it provides a flexible and efficient foundation for defining and evaluating custom validation rules. The primary goal of `protovalidate` is to help developers ensure data consistency and integrity across the network without requiring generated code.

## The `protovalidate` project

Head over to the core [`protovalidate`](https://github.com/bufbuild/protovalidate/) repository for:

- [The API definition](https://github.com/bufbuild/protovalidate/tree/main/proto/protovalidate/buf/validate/validate.proto): used to describe validation constraints
- [Documentation](https://github.com/bufbuild/protovalidate/tree/main/docs): how to apply `protovalidate` effectively
- [Migration tooling](https://github.com/bufbuild/protovalidate/tree/main/docs/migrate.md): incrementally migrate from `protoc-gen-validate`
- [Conformance testing utilities](https://github.com/bufbuild/protovalidate/tree/main/docs/conformance.md): for acceptance testing of `protovalidate` implementations

Other `protovalidate` runtime implementations include:

- Go: [`protovalidate-go`](https://github.com/bufbuild/protovalidate-go)
- C++: [`protovalidate-cc`](https://github.com/bufbuild/protovalidate-cc)

And others coming soon:

- Java: `protovalidate-java`
- TypeScript: `protovalidate-ts`

## Installation

To install the package, use pip:

```shell
pip install protovalidate
```

Make sure you have the latest version of `protovalidate-py` by checking the project's [PyPI page](#).

## Usage

### Implementing validation constraints

Validation constraints are defined directly within `.proto` files. Documentation for adding constraints can be found in the `protovalidate` project [README](https://github.com/bufbuild/protovalidate) and its [comprehensive docs](https://github.com/bufbuild/protovalidate/tree/main/docs).

```protobuf
syntax = "proto3";

package my.package;

import "google/protobuf/timestamp.proto";
import "buf/validate/validate.proto";

message Transaction {
  uint64 id = 1 [(buf.validate.field).uint64.gt = 999];
  google.protobuf.Timestamp purchase_date = 2;
  google.protobuf.Timestamp delivery_date = 3;
  
  string price = 4 [(buf.validate.field).cel = {
    id: "transaction.price",
    message: "price must be positive and include a valid currency symbol ($ or £)",
    expression: "(this.startswith('$') or this.startswith('£')) and float(this[1:]) > 0"
  }];

  option (buf.validate.message).cel = {
    id: "transaction.delivery_date",
    message: "delivery date must be after purchase date",
    expression:

 "this.delivery_date > this.purchase_date"
  };
}
```

### Example

```python
from google.protobuf.timestamp_pb2 import Timestamp
from protovalidate import Validator

validator = Validator()

transaction = Transaction()
transaction.id = 1234
transaction.price = "$5.67"
transaction.purchase_date.CopyFrom(Timestamp())
transaction.delivery_date.CopyFrom(Timestamp())

try:
    validator.validate(transaction)
    print("Validation succeeded")
except Exception as e:
    print("Validation failed:", str(e))
```

### Support legacy `protoc-gen-validate` constraints

The `protovalidate-py` module provides support for existing `protoc-gen-validate` constraints. You can enable legacy support when initializing the validator:

```python
from protovalidate import Validator, LegacyMode

validator = Validator(legacy_mode=LegacyMode.MERGE)
```

Note that `protoc-gen-validate` code generation is **not** used by `protovalidate-py`. The legacy support assumes the `protoc-gen-validate` extensions are imported into the generated code.

A [migration tool](https://github.com/bufbuild/protovalidate/tree/main/tools/protovalidate-migrate) is also available to incrementally upgrade legacy constraints in `.proto` files.

## Performance

Performance benchmarks are not yet available for `protovalidate-py`.

### Ecosystem

- [`protovalidate`](https://github.com/bufbuild/protovalidate) core repository
- [Buf](https://buf.build)
- [CEL Spec](https://github.com/google/cel-spec)

## Legal

Offered under the [Apache 2 license][license].

[license]: LICENSE
[buf]: https://buf.build
[buf-mod]: https://buf.build/bufbuild/protovalidate
[cel-go]: https://github.com/google/cel-go
[cel-spec]: https://github.com/google/cel-spec