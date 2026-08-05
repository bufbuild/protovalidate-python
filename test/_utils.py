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
from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

import pytest

from protovalidate import CompilationError, Violation

if TYPE_CHECKING:
    from google.protobuf import message as google_message
    from protobuf import Message


class ValidatorProtocol(Protocol):
    def validate(
        self, message: Message | google_message.Message, *, fail_fast: bool = False
    ) -> None: ...

    def collect_violations(
        self, message: Message | google_message.Message, *, fail_fast: bool = False
    ) -> list[Violation]: ...


def check_valid(
    validator: ValidatorProtocol, msg: Message | google_message.Message
) -> None:
    # Test validate
    validator.validate(msg)

    # Test collect_violations
    violations = validator.collect_violations(msg)
    assert len(violations) == 0


def check_compilation_errors(
    validator: ValidatorProtocol, msg: Message | google_message.Message, expected: str
) -> None:
    """A helper function for testing compilation errors when validating.

    The tests are run using validators created via all possible methods and
    validation is done via a call to `validate` as well as a call to `collect_violations`.
    """
    # Test validate
    with pytest.raises(CompilationError) as vce:
        validator.validate(msg)
    assert str(vce.value) == expected

    # Test collect_violations
    with pytest.raises(CompilationError) as cvce:
        validator.collect_violations(msg)
    assert str(cvce.value) == expected


def compare_violations(actual: list[Violation], expected: list[Violation]) -> None:
    """Compares two lists of violations. The violations are expected to be in the expected order also."""
    assert len(actual) == len(expected)
    for a, e in zip(actual, expected, strict=True):
        assert a.proto.message == e.proto.message
        assert a.proto.rule_id == e.proto.rule_id
        assert a.proto.for_key == e.proto.for_key
        assert a.field_value == e.field_value
        assert a.rule_value == e.rule_value
