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
    expression:

 "this.delivery_date > this.purchase_date"
  };
}
```

### Generating Code

Both `buf` and `protoc` provide valuable utilities for working with protovalidate. While `buf` offers modern features
and easier integration with various platforms, `protoc` remains a versatile tool for direct code generation.
Experimenting with both will help you determine which is best suited to your project.

#### `buf`

The `buf` tool facilitates the process of working with protobuf by providing functionality like initialization,
linting, and code generation. Here are the steps:

1. **Initialize a New Configuration File**: To start a new project, initialize the `buf.yaml` configuration file. This
   file will define the behavior of the `buf` tool for your project.

   ```shell
   buf mod init
   ```

2. **Define the Module Configuration**: The `buf.yaml` file defines a module and is placed at the root of the Protobuf
   source files. This file includes lint rules, breaking change detection rules, module name, and dependencies. Here's
   an example of what a typical `buf.yaml` file might look like:

   ```yaml
   # buf.yaml
   version: v1
   # <snip>
   deps: 
     - buf.build/bufbuild/protovalidate
   # <snip>
   ```

3. **Update Module Dependencies**: You can update a module's dependencies using the `buf.lock` file, which keeps track
   of the specific versions of dependencies used in the project.

   ```shell
   buf mod update
   ```

4. **Define a Local Plugin Template**: The `buf.gen.yaml` file is used to define how code will be generated for specific
   languages. 

   ```yaml
   # buf.gen.yaml
   version: v1
   # <snip>
   plugins:
     - plugin: buf.build/protocolbuffers/python:v23.4
       out: gen
   # <snip>
   ```

5. **Generate Code**: Finally, you can generate code using the defined plugins. This command will generate code for the
   language(s) specified in the `buf.gen.yaml` file.

   ```shell
   buf generate 
   ```

#### `protoc`

`protoc` is an alternative to `buf`. It's a command-line utility that you can use to generate code for various
programming languages from `.proto` files. Here's an example command that generates Python code:

```shell
protoc \
  -I . \
  -I path/to/validate/ \
  --python_out=":./gen" \
  transaction.proto
```

This command tells `protoc` to include the current directory (`-I .`) and the path to validation
rules (`-I path/to/validate/`) while generating code for the `transaction.proto` file. The generated code will be placed
in the `./gen` directory.

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
