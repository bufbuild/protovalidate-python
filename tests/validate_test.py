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

from buf.validate import validator
from buf import numbers_pb2
import unittest


# Test basic validation
class TestValidate(unittest.TestCase):
    def test_SFixed64ExLTGT(self):
        msg = numbers_pb2.SFixed64ExLTGT(val=11)
        violations = validator.validate(msg)
        self.assertEqual(len(violations.violations), 0)


if __name__ == "__main__":
    unittest.main()
