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

import unittest

from buf.validate.conformance.cases import oneofs_pb2  # noqa: F401
from buf.validate.conformance.harness import results_pb2
from google.protobuf import descriptor_pool

from tests.conformance import runner


class RunnerTest(unittest.TestCase):
    def test_oneof(self):
        results = results_pb2.ResultSet()
        # load the results from oneof.binproto
        with open("tests/oneof.binproto", "rb") as f:
            results.ParseFromString(f.read())
        for suite in results.suites:
            pool = descriptor_pool.Default()
            # for fd in suite.fdset.file:
            #     pool.Add(fd)
            for result in suite.cases:
                runner.run_any_test_case(pool, result.input)


if __name__ == "__main__":
    unittest.main()
