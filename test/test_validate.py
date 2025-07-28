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

import unittest

from google.protobuf import message

import protovalidate
from gen.tests.example.v1 import validations_pb2
from protovalidate.config import Config
from protovalidate.internal import rules


def get_default_validator():
    """Returns a default validator created in all available ways

    This allows testing for validators created via:
        - module-level singleton
        - instantiated class with no config
        - instantiated class with config
    """
    return [
        ("module singleton", protovalidate),
        ("no config", protovalidate.Validator()),
        ("with default config", protovalidate.Validator(Config())),
    ]


class TestCollectViolations(unittest.TestCase):
    """Test class for testing message validations.

    A validator can be created via various ways:
    - a module-level singleton, which returns a default validator
    - instantiating the Validator class with no config, which returns a default validator
    - instantiating the Validator class with a config

    In addition, the API for validating a message allows for two approaches:
    - via a call to `validate`, which will raise a ValidationError if validation fails
    - via a call to `collect_violations`, which will not raise an error and instead return a list of violations.

    Unless otherwise noted, each test in this class tests against a validator created via all 3 methods and tests
    validation using both approaches.
    """

    def test_ninf(self):
        msg = validations_pb2.DoubleFinite()
        msg.val = float("-inf")

        expected_violation = rules.Violation()
        expected_violation.proto.message = "value must be finite"
        expected_violation.proto.rule_id = "double.finite"
        expected_violation.field_value = msg.val
        expected_violation.rule_value = True

        self._run_invalid_tests(msg, [expected_violation])

    def test_map_key(self):
        msg = validations_pb2.MapKeys()
        msg.val[1] = "a"

        expected_violation = rules.Violation()
        expected_violation.proto.message = "value must be less than 0"
        expected_violation.proto.rule_id = "sint64.lt"
        expected_violation.proto.for_key = True
        expected_violation.field_value = 1
        expected_violation.rule_value = 0

        self._run_invalid_tests(msg, [expected_violation])

    def test_sfixed64_valid(self):
        msg = validations_pb2.SFixed64ExLTGT(val=11)

        self._run_valid_tests(msg)

    def test_oneofs(self):
        msg = validations_pb2.Oneof()
        msg.y = 123

        self._run_valid_tests(msg)

    def test_collect_violations_into(self):
        msg1 = validations_pb2.Oneof()
        msg1.y = 123

        msg2 = validations_pb2.Oneof()
        msg2.z.val = True

        for label, v in get_default_validator():
            with self.subTest(label=label):
                # Test collect_violations into
                violations = v.collect_violations(msg1)
                v.collect_violations(msg2, into=violations)
                self.assertEqual(len(violations), 0)

    def test_protovalidate_oneof_valid(self):
        msg = validations_pb2.ProtovalidateOneof()
        msg.a = "A"

        self._run_valid_tests(msg)

    def test_protovalidate_oneof_violation(self):
        msg = validations_pb2.ProtovalidateOneof()
        msg.a = "A"
        msg.b = "B"

        expected_violation = rules.Violation()
        expected_violation.proto.message = "only one of a, b can be set"
        expected_violation.proto.rule_id = "message.oneof"

        self._run_invalid_tests(msg, [expected_violation])

    def test_protovalidate_oneof_required_violation(self):
        msg = validations_pb2.ProtovalidateOneofRequired()

        expected_violation = rules.Violation()
        expected_violation.proto.message = "one of a, b must be set"
        expected_violation.proto.rule_id = "message.oneof"

        self._run_invalid_tests(msg, [expected_violation])

    def test_protovalidate_oneof_unknown_field_name(self):
        """Tests that a compilation error is thrown when specifying a oneof rule with an invalid field name"""
        msg = validations_pb2.ProtovalidateOneofUnknownFieldName()

        self._run_compilation_error_tests(
            msg, 'field "xxx" not found in message tests.example.v1.ProtovalidateOneofUnknownFieldName'
        )

    def test_repeated(self):
        msg = validations_pb2.RepeatedEmbedSkip()
        msg.val.add(val=-1)

        self._run_valid_tests(msg)

    def test_maps(self):
        msg = validations_pb2.MapMinMax()

        expected_violation = rules.Violation()
        expected_violation.proto.message = "map must be at least 2 entries"
        expected_violation.proto.rule_id = "map.min_pairs"
        expected_violation.field_value = {}
        expected_violation.rule_value = 2

        self._run_invalid_tests(msg, [expected_violation])

    def test_timestamp(self):
        msg = validations_pb2.TimestampGTNow()

        self._run_valid_tests(msg)

    def test_multiple_validations(self):
        """Test that a message with multiple violations correctly returns all of them."""
        msg = validations_pb2.MultipleValidations()
        msg.title = "bar"
        msg.name = "blah"

        expected_violation1 = rules.Violation()
        expected_violation1.proto.message = "value does not have prefix `foo`"
        expected_violation1.proto.rule_id = "string.prefix"
        expected_violation1.field_value = msg.title
        expected_violation1.rule_value = "foo"

        expected_violation2 = rules.Violation()
        expected_violation2.proto.message = "value length must be at least 5 characters"
        expected_violation2.proto.rule_id = "string.min_len"
        expected_violation2.field_value = msg.name
        expected_violation2.rule_value = 5

        self._run_invalid_tests(msg, [expected_violation1, expected_violation2])

    def test_fail_fast(self):
        """Test that fail fast correctly fails on first violation

        Note this does not use a default validator, but instead uses one with a custom config
        so that fail_fast can be set to True.
        """
        msg = validations_pb2.MultipleValidations()
        msg.title = "bar"
        msg.name = "blah"

        expected_violation = rules.Violation()
        expected_violation.proto.message = "value does not have prefix `foo`"
        expected_violation.proto.rule_id = "string.prefix"
        expected_violation.field_value = msg.title
        expected_violation.rule_value = "foo"

        cfg = Config(fail_fast=True)
        validator = protovalidate.Validator(config=cfg)

        # Test validate
        with self.assertRaises(protovalidate.ValidationError) as cm:
            validator.validate(msg)
            e = cm.exception
            self.assertEqual(str(e), f"invalid {msg.DESCRIPTOR.name}")
            self._compare_violations(e.violations, [expected_violation])

        # Test collect_violations
        violations = validator.collect_violations(msg)
        self._compare_violations(violations, [expected_violation])

    def _run_valid_tests(self, msg: message.Message):
        """A helper function for testing successful validation on a given message

        The tests are run using validators created via all possible methods and
        validation is done via a call to `validate` as well as a call to `collect_violations`.
        """
        for label, v in get_default_validator():
            with self.subTest(label=label):
                # Test validate
                try:
                    v.validate(msg)
                except Exception:
                    self.fail(f"[{label}]: unexpected validation failure")

                # Test collect_violations
                violations = v.collect_violations(msg)
                self.assertEqual(len(violations), 0)

    def _run_invalid_tests(self, msg: message.Message, expected: list[rules.Violation]):
        """A helper function for testing unsuccessful validation on a given message

        The tests are run using validators created via all possible methods and
        validation is done via a call to `validate` as well as a call to `collect_violations`.
        """
        for label, v in get_default_validator():
            with self.subTest(label=label):
                # Test validate
                with self.assertRaises(protovalidate.ValidationError) as cm:
                    v.validate(msg)
                e = cm.exception
                self.assertEqual(str(e), f"invalid {msg.DESCRIPTOR.name}")
                self._compare_violations(e.violations, expected)

                # Test collect_violations
                violations = v.collect_violations(msg)
                self._compare_violations(violations, expected)

    def _run_compilation_error_tests(self, msg: message.Message, expected: str):
        """A helper function for testing compilation errors when validating.

        The tests are run using validators created via all possible methods and
        validation is done via a call to `validate` as well as a call to `collect_violations`.
        """
        for label, v in get_default_validator():
            with self.subTest(label=label):
                # Test validate
                with self.assertRaises(protovalidate.CompilationError) as vce:
                    v.validate(msg)
                self.assertEqual(str(vce.exception), expected)

                # Test collect_violations
                with self.assertRaises(protovalidate.CompilationError) as cvce:
                    v.collect_violations(msg)
                self.assertEqual(str(cvce.exception), expected)

    def _compare_violations(self, actual: list[rules.Violation], expected: list[rules.Violation]) -> None:
        """Compares two lists of violations. The violations are expected to be in the expected order also."""
        self.assertEqual(len(actual), len(expected))
        for a, e in zip(actual, expected):
            self.assertEqual(a.proto.message, e.proto.message)
            self.assertEqual(a.proto.rule_id, e.proto.rule_id)
            self.assertEqual(a.proto.for_key, e.proto.for_key)
            self.assertEqual(a.field_value, e.field_value)
            self.assertEqual(a.rule_value, e.rule_value)
