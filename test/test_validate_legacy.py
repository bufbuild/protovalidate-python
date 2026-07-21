# Copyright (c) 2023-2026 Buf Technologies, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import pytest

pytest.importorskip("google.protobuf", reason="optional dependency not installed")

from google.protobuf import message as google_message

import protovalidate
from protovalidate.internal import rules

from ._utils import _compare_violations, check_valid
from .conftest import backend_validators
from .gen.tests.example.v1 import validations_pb2

validators: list[protovalidate.Validator] = [
    protovalidate,  # global module singleton
    *backend_validators(),
]


@pytest.mark.parametrize("validator", validators)
def test_legacy_message_valid(validator):
    """A google.protobuf message validates through the legacy conversion path."""
    msg = validations_pb2.DoubleFinite()
    msg.val = 1.0

    check_valid(validator, msg)


@pytest.mark.parametrize("validator", validators)
def test_legacy_message_invalid(validator):
    msg = validations_pb2.DoubleFinite()
    msg.val = float("-inf")

    expected_violation = rules.Violation(
        message="must be finite",
        rule_id="double.finite",
        field_value=msg.val,
        rule_value=True,
    )

    with pytest.raises(protovalidate.ValidationError) as exc_info:
        validator.validate(msg)
    e = exc_info.value
    assert str(e) == f"invalid {msg.DESCRIPTOR.name}"
    _compare_violations(e.violations, [expected_violation])  # ty: ignore

    violations = validator.collect_violations(msg)
    _compare_violations(violations, [expected_violation])


@pytest.mark.parametrize("validator", validators)
def test_legacy_message_map_key(validator):
    msg = validations_pb2.MapKeys()
    msg.val[1] = "a"

    expected_violation = rules.Violation(
        message="must be less than 0",
        rule_id="sint64.lt",
        for_key=True,
        field_value=1,
        rule_value=0,
    )

    violations = validator.collect_violations(msg)
    _compare_violations(violations, [expected_violation])


def check_invalid(validator: protovalidate.Validator, msg: google_message.Message, expected: list[rules.Violation]):
    # Test validate
    with pytest.raises(protovalidate.ValidationError) as exc_info:
        validator.validate(msg)
    e = exc_info.value
    assert str(e) == f"invalid {msg.DESCRIPTOR.name}"
    _compare_violations(e.violations, expected)  # ty: ignore

    # Test collect_violations
    violations = validator.collect_violations(msg)
    _compare_violations(violations, expected)
