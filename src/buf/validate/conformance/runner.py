# Copyright 2023 Buf Technologies, Inc.
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
import celpy

from buf.validate import validator
from buf.validate.conformance.harness import harness_pb2
from google.protobuf import any_pb2
from google.protobuf import descriptor_pool
from google.protobuf import descriptor
from google.protobuf import message_factory


def run_test_case(
    tc: any, result: harness_pb2.TestResult | None = None
) -> harness_pb2.TestResult:
    if result is None:
        result = harness_pb2.TestResult()
    # Run the validator
    try:
        validator.validate(tc, False, result.validation_error)
        if len(result.validation_error.violations) == 0:
            result.success = True
    except celpy.CELEvalError as e:
        result.unexpected_error = str(e)
    return result


def run_any_test_case(
    pool: descriptor_pool.DescriptorPool,
    tc: any_pb2.Any,
    result: harness_pb2.TestResult | None = None,
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
    pool = descriptor_pool.DescriptorPool()
    for fd in request.fdset.file:
        pool.Add(fd)
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
