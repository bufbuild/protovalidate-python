# Copyright 2023-2025 Buf Technologies, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys
import typing

import celpy
from google.protobuf import any_pb2, descriptor, descriptor_pool, message_factory

import protovalidate

# TODO(afuller): Use dynamic descriptor pool based on the FileDescriptorSet
# in the TestConformanceRequest, once the Python protobuf library no longer
# segfaults when using a dynamic descriptor pool.
from buf.validate.conformance.cases import (
    bool_pb2,  # noqa: F401
    bytes_pb2,  # noqa: F401
    enums_pb2,  # noqa: F401
    filename_with_dash_pb2,  # noqa: F401
    ignore_empty_proto2_pb2,  # noqa: F401
    ignore_empty_proto3_pb2,  # noqa: F401
    ignore_empty_proto_editions_pb2,  # noqa: F401
    ignore_proto2_pb2,  # noqa: F401
    ignore_proto3_pb2,  # noqa: F401
    ignore_proto_editions_pb2,  # noqa: F401
    kitchen_sink_pb2,  # noqa: F401
    library_pb2,  # noqa: F401
    maps_pb2,  # noqa: F401
    messages_pb2,  # noqa: F401
    numbers_pb2,  # noqa: F401
    oneofs_pb2,  # noqa: F401
    predefined_rules_proto2_pb2,  # noqa: F401
    predefined_rules_proto3_pb2,  # noqa: F401
    predefined_rules_proto_editions_pb2,  # noqa: F401
    repeated_pb2,  # noqa: F401
    required_field_proto2_pb2,  # noqa: F401
    required_field_proto3_pb2,  # noqa: F401
    required_field_proto_editions_pb2,  # noqa: F401
    strings_pb2,  # noqa: F401
    wkt_any_pb2,  # noqa: F401
    wkt_duration_pb2,  # noqa: F401
    wkt_nested_pb2,  # noqa: F401
    wkt_timestamp_pb2,  # noqa: F401
    wkt_wrappers_pb2,  # noqa: F401
)
from buf.validate.conformance.cases.custom_rules import custom_rules_pb2  # noqa: F401
from buf.validate.conformance.harness import harness_pb2


def run_test_case(tc: typing.Any, result: typing.Optional[harness_pb2.TestResult] = None) -> harness_pb2.TestResult:
    if result is None:
        result = harness_pb2.TestResult()
    # Run the validator
    try:
        violations = protovalidate.collect_violations(tc)
        for violation in violations:
            result.validation_error.violations.append(violation.proto)
        if len(result.validation_error.violations) == 0:
            result.success = True
    except celpy.CELEvalError as e:
        result.runtime_error = str(e)
    except protovalidate.CompilationError as e:
        result.compilation_error = str(e)
    except Exception as e:
        result.unexpected_error = str(e)
    return result


def run_any_test_case(
    pool: descriptor_pool.DescriptorPool,
    tc: any_pb2.Any,
    result: typing.Optional[harness_pb2.TestResult] = None,
) -> harness_pb2.TestResult:
    type_name = tc.type_url.split("/")[-1]
    desc: descriptor.Descriptor = pool.FindMessageTypeByName(type_name)
    # Create a message from the protobuf descriptor
    msg = message_factory.GetMessageClass(desc)()
    tc.Unpack(msg)
    return run_test_case(msg, result)


def run_conformance_test(
    request: harness_pb2.TestConformanceRequest,
) -> harness_pb2.TestConformanceResponse:
    # pool = descriptor_pool.DescriptorPool()
    # for fd in request.fdset.file:
    #     pool.Add(fd)
    pool = descriptor_pool.Default()
    result = harness_pb2.TestConformanceResponse()
    for name, tc in request.cases.items():
        run_any_test_case(pool, tc, result.results[name])
    return result


if __name__ == "__main__":
    # Read a serialized TestConformanceRequest from stdin
    request = harness_pb2.TestConformanceRequest()
    request.ParseFromString(sys.stdin.buffer.read())
    # Run the test
    result = run_conformance_test(request)
    # Write a serialized TestConformanceResponse to stdout
    sys.stdout.buffer.write(result.SerializeToString())
    sys.stdout.flush()
    sys.exit(0)
