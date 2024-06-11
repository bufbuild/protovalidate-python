# protovalidate-python

[![CI](https://github.com/bufbuild/protovalidate-python/actions/workflows/ci.yaml/badge.svg)](https://github.com/bufbuild/protovalidate-python/actions/workflows/ci.yaml)
[![Conformance](https://github.com/bufbuild/protovalidate-python/actions/workflows/conformance.yaml/badge.svg)](https://github.com/bufbuild/protovalidate-python/actions/workflows/conformance.yaml)
[![PyPI version](https://badge.fury.io/py/protovalidate.svg)](https://badge.fury.io/py/protovalidate)

`protovalidate-python` is the Python implementation of [`protovalidate`](https://github.com/bufbuild/protovalidate),
designed to validate Protobuf messages at runtime based on user-defined validation constraints. Powered by Google's
Common Expression Language ([CEL](https://github.com/google/cel-spec)), it provides a flexible and efficient foundation
for defining and evaluating custom validation rules. The primary goal of `protovalidate` is to help developers ensure
data consistency and integrity across the network without requiring generated code.

## The `protovalidate` project

Head over to the core [`protovalidate`](https://github.com/bufbuild/protovalidate/) repository for:

- [The API definition](https://github.com/bufbuild/protovalidate/tree/main/proto/protovalidate/buf/validate/validate.proto):
  used to describe validation constraints
- [Documentation](https://github.com/bufbuild/protovalidate/tree/main/docs): how to apply `protovalidate` effectively
- [Migration tooling](https://github.com/bufbuild/protovalidate/tree/main/docs/migrate.md): incrementally migrate
  from `protoc-gen-validate`
- [Conformance testing utilities](https://github.com/bufbuild/protovalidate/tree/main/docs/conformance.md): for
  acceptance testing of `protovalidate` implementations

Other `protovalidate` runtime implementations include:

- Go: [`protovalidate-go`](https://github.com/bufbuild/protovalidate-go)
- C++: [`protovalidate-cc`](https://github.com/bufbuild/protovalidate-cc)
- Java: [`protovalidate-java`](https://github.com/bufbuild/protovalidate-java)

And others coming soon:

- TypeScript: `protovalidate-ts`

## Installation

To install the package, use pip:

```shell
pip install protovalidate
```

Make sure you have the latest version of `protovalidate-python` by checking the
project's [PyPI page](https://pypi.org/project/protovalidate/).

## Usage

### Implementing validation constraints

Validation constraints are defined directly within `.proto` files. Documentation for adding constraints can be found in
the `protovalidate` project [README](https://github.com/bufbuild/protovalidate) and
its [comprehensive docs](https://github.com/bufbuild/protovalidate/tree/main/docs).

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
    expression: "this.delivery_date > this.purchase_date"
  };
}
```

### Generating Code with `buf`

When using the runtime library after installing it with `pip`, it's necessary to generate the Python code for the core `buf.protovalidate` Protobuf package. `buf` provides an efficient method for this:

1. **Initialize a New Configuration File**: 
   ```shell
   buf mod init
   ```
   This initializes the `buf.yaml` configuration file at the root of the Protobuf source files.

2. **Module Configuration and Dependencies**:
   ```yaml
   # buf.yaml
   version: v1
   deps: 
     - buf.build/bufbuild/protovalidate
   ```

   Ensure your dependencies are up-to-date with:
   ```shell
   buf mod update
   ```

3. **Setup Code Generation**:
   ```yaml
   # buf.gen.yaml
   version: v1
   plugins:
     - plugin: buf.build/protocolbuffers/python:v23.4
       out: gen
   ```

4. **Generate Code**:
   To generate the required Python code:
   ```shell
   buf generate --include-imports
   ```

5. **Specify import paths**:
   Ensure that the generated code is importable by setting the `PYTHONPATH` environment variable:
   ```shell
   export PYTHONPATH=$PYTHONPATH:gen
   ```

If your goal is to generate code specifically for the `buf.protovalidate` Protobuf package, run:
```shell
buf generate buf.build/bufbuild/protovalidate
```

> **Note:** For users familiar with `protoc`, while it's an alternative to `buf`, it is recommended to use tooling or frameworks like Bazel for direct code generation, as it provides an encapsulated environment for such tasks.

### Example

```python
import protovalidate
from google.protobuf.timestamp_pb2 import Timestamp
from my.package import Transaction

transaction = Transaction()
transaction.id = 1234
transaction.price = "$5.67"
transaction.purchase_date.CopyFrom(Timestamp())
transaction.delivery_date.CopyFrom(Timestamp())

try:
    protovalidate.validate(transaction)
except protovalidate.ValidationError as e:
# Report the violations
```

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
