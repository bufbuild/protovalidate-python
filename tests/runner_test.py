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

from google.protobuf import descriptor_pool

from buf.validate.conformance.cases import oneofs_pb2  # noqa: F401
from buf.validate.conformance.harness import results_pb2
from tests.conformance import runner


def test_oneof():
    results = results_pb2.ResultSet()
    # load the results from oneof.binpb
    with open("tests/oneof.binpb", "rb") as f:
        results.ParseFromString(f.read())
    for suite in results.suites:
        pool = descriptor_pool.Default()
        for result in suite.cases:
            runner.run_any_test_case(pool, result.input)
