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

import pytest
from google.protobuf import message

import protovalidate
from gen.tests.example.v1 import validations_pb2
from protovalidate.internal import rules

validators: list[protovalidate.Validator] = [
    protovalidate,  # global module singleton
    protovalidate.Validator(),  # via constructor
]


@pytest.mark.parametrize("validator", validators)
def test_ninf(validator):
    msg = validations_pb2.DoubleFinite()
    msg.val = float("-inf")

    expected_violation = rules.Violation()
    expected_violation.proto.message = "value must be finite"
    expected_violation.proto.rule_id = "double.finite"
    expected_violation.field_value = msg.val
    expected_violation.rule_value = True

    check_invalid(validator, msg, [expected_violation])


@pytest.mark.parametrize("validator", validators)
def test_map_key(validator):
    msg = validations_pb2.MapKeys()
    msg.val[1] = "a"

    expected_violation = rules.Violation()
    expected_violation.proto.message = "value must be less than 0"
    expected_violation.proto.rule_id = "sint64.lt"
    expected_violation.proto.for_key = True
    expected_violation.field_value = 1
    expected_violation.rule_value = 0

    check_invalid(validator, msg, [expected_violation])


@pytest.mark.parametrize("validator", validators)
def test_sfixed64_valid(validator):
    msg = validations_pb2.SFixed64ExLTGT(val=11)

    check_valid(validator, msg)


@pytest.mark.parametrize("validator", validators)
def test_oneofs(validator):
    msg = validations_pb2.Oneof()
    msg.y = 123

    check_valid(validator, msg)


@pytest.mark.parametrize("validator", validators)
def test_protovalidate_oneof_valid(validator):
    msg = validations_pb2.ProtovalidateOneof()
    msg.a = "A"

    check_valid(validator, msg)


@pytest.mark.parametrize("validator", validators)
def test_protovalidate_oneof_violation(validator):
    msg = validations_pb2.ProtovalidateOneof()
    msg.a = "A"
    msg.b = "B"

    expected_violation = rules.Violation()
    expected_violation.proto.message = "only one of a, b can be set"
    expected_violation.proto.rule_id = "message.oneof"

    check_invalid(validator, msg, [expected_violation])


@pytest.mark.parametrize("validator", validators)
def test_protovalidate_oneof_required_violation(validator):
    msg = validations_pb2.ProtovalidateOneofRequired()

    expected_violation = rules.Violation()
    expected_violation.proto.message = "one of a, b must be set"
    expected_violation.proto.rule_id = "message.oneof"

    check_invalid(validator, msg, [expected_violation])


@pytest.mark.parametrize("validator", validators)
def test_protovalidate_oneof_unknown_field_name(validator):
    """Tests that a compilation error is thrown when specifying a oneof rule with an invalid field name"""
    msg = validations_pb2.ProtovalidateOneofUnknownFieldName()

    check_compilation_errors(
        validator, msg, 'field "xxx" not found in message tests.example.v1.ProtovalidateOneofUnknownFieldName'
    )


@pytest.mark.parametrize("validator", validators)
def test_repeated(validator):
    msg = validations_pb2.RepeatedEmbedSkip()
    msg.val.add(val=-1)

    check_valid(validator, msg)


@pytest.mark.parametrize("validator", validators)
def test_maps(validator):
    msg = validations_pb2.MapMinMax()

    expected_violation = rules.Violation()
    expected_violation.proto.message = "map must be at least 2 entries"
    expected_violation.proto.rule_id = "map.min_pairs"
    expected_violation.field_value = {}
    expected_violation.rule_value = 2

    check_invalid(validator, msg, [expected_violation])


@pytest.mark.parametrize("validator", validators)
def test_timestamp(validator):
    msg = validations_pb2.TimestampGTNow()

    check_valid(validator, msg)


@pytest.mark.parametrize("validator", validators)
def test_multiple_validations(validator):
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

    check_invalid(validator, msg, [expected_violation1, expected_violation2])


@pytest.mark.parametrize("validator", validators)
def test_concatenated_values(validator):
    msg = validations_pb2.ConcatenatedValues(
        bar=["a", "b", "c"],
        baz=["d", "e", "f"],
    )

    check_valid(validator, msg)


@pytest.mark.parametrize("validator", validators)
def test_fail_fast(validator):
    """Test that fail fast correctly fails on first violation"""
    msg = validations_pb2.MultipleValidations()
    msg.title = "bar"
    msg.name = "blah"

    expected_violation = rules.Violation()
    expected_violation.proto.message = "value does not have prefix `foo`"
    expected_violation.proto.rule_id = "string.prefix"
    expected_violation.field_value = msg.title
    expected_violation.rule_value = "foo"

    # Test validate
    with pytest.raises(protovalidate.ValidationError) as cm:
        validator.validate(msg, fail_fast=True)
    e = cm.value
    assert str(e) == f"invalid {msg.DESCRIPTOR.name}"
    _compare_violations(e.violations, [expected_violation])  # ty: ignore

    # Test collect_violations
    violations = validator.collect_violations(msg, fail_fast=True)
    _compare_violations(violations, [expected_violation])


def check_valid(validator: protovalidate.Validator, msg: message.Message):
    # Test validate
    validator.validate(msg)

    # Test collect_violations
    violations = validator.collect_violations(msg)
    assert len(violations) == 0


def check_invalid(validator: protovalidate.Validator, msg: message.Message, expected: list[rules.Violation]):
    # Test validate
    with pytest.raises(protovalidate.ValidationError) as exc_info:
        validator.validate(msg)
    e = exc_info.value
    assert str(e) == f"invalid {msg.DESCRIPTOR.name}"
    _compare_violations(e.violations, expected)  # ty: ignore

    # Test collect_violations
    violations = validator.collect_violations(msg)
    _compare_violations(violations, expected)


def check_compilation_errors(validator: protovalidate.Validator, msg: message.Message, expected: str):
    """A helper function for testing compilation errors when validating.

    The tests are run using validators created via all possible methods and
    validation is done via a call to `validate` as well as a call to `collect_violations`.
    """
    # Test validate
    with pytest.raises(protovalidate.CompilationError) as vce:
        validator.validate(msg)
    assert str(vce.value) == expected

    # Test collect_violations
    with pytest.raises(protovalidate.CompilationError) as cvce:
        validator.collect_violations(msg)
    assert str(cvce.value) == expected


def _compare_violations(actual: list[rules.Violation], expected: list[rules.Violation]):
    """Compares two lists of violations. The violations are expected to be in the expected order also."""
    assert len(actual) == len(expected)
    for a, e in zip(actual, expected):
        assert a.proto.message == e.proto.message
        assert a.proto.rule_id == e.proto.rule_id
        assert a.proto.for_key == e.proto.for_key
        assert a.field_value == e.field_value
        assert a.rule_value == e.rule_value
