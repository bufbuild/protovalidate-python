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

import protovalidate
from buf.validate.conformance.cases import maps_pb2, numbers_pb2, oneofs_pb2, repeated_pb2, wkt_timestamp_pb2


class TestValidate(unittest.TestCase):
    def test_ninf(self):
        msg = numbers_pb2.DoubleFinite()
        msg.val = float("-inf")
        violations = protovalidate.collect_violations(msg)
        self.assertEqual(len(violations.violations), 1)
        self.assertEqual(violations.violations[0].constraint_id, "double.finite")

    def test_map_key(self):
        msg = maps_pb2.MapKeys()
        msg.val[1] = "a"
        violations = protovalidate.collect_violations(msg)
        self.assertEqual(len(violations.violations), 1)
        self.assertEqual(violations.violations[0].field_path, "val[1]")
        self.assertEqual(violations.violations[0].for_key, True)

    def test_sfixed64(self):
        msg = numbers_pb2.SFixed64ExLTGT(val=11)
        protovalidate.validate(msg)

        violations = protovalidate.collect_violations(msg)
        self.assertEqual(len(violations.violations), 0)

    def test_oneofs(self):
        msg1 = oneofs_pb2.Oneof()
        msg1.y = 123
        protovalidate.validate(msg1)

        msg2 = oneofs_pb2.Oneof()
        msg2.z.val = True
        protovalidate.validate(msg2)

        violations = protovalidate.collect_violations(msg1)
        protovalidate.collect_violations(msg2, into=violations)
        assert len(violations.violations) == 0

    def test_repeated(self):
        msg = repeated_pb2.RepeatedEmbedSkip()
        msg.val.add(val=-1)
        protovalidate.validate(msg)

        violations = protovalidate.collect_violations(msg)
        assert len(violations.violations) == 0

    def test_maps(self):
        msg = maps_pb2.MapMinMax()
        try:
            protovalidate.validate(msg)
        except protovalidate.ValidationError as e:
            assert len(e.errors()) == 1
            assert len(e.violations.violations) == 1
            assert str(e) == "invalid MapMinMax"

        violations = protovalidate.collect_violations(msg)
        assert len(violations.violations) == 1

    def test_timestamp(self):
        msg = wkt_timestamp_pb2.TimestampGTNow()
        protovalidate.validate(msg)

        violations = protovalidate.collect_violations(msg)
        assert len(violations.violations) == 0
