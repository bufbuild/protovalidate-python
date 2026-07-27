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

"""The semantic validation library for Protobuf in Python."""

from __future__ import annotations

from typing import TYPE_CHECKING

from protobuf import Message

from protovalidate._core import Violation
from protovalidate._gen.buf.validate.validate_pb import (
    FieldPath as FieldPathPb,
    FieldPathElement as FieldPathElementPb,
    Violation as ViolationPb,
    Violations as ViolationsPb,
)
from protovalidate._validator import CompilationError, ValidationError, Validator

if TYPE_CHECKING:
    from google.protobuf import message as google_message

_default_validator = Validator()


def validate(
    message: Message | google_message.Message, *, fail_fast: bool = False
) -> None:
    """Validates the given message against the static rules defined in the message's descriptor using a shared validator.

    Parameters:
        message: The message to validate.
        fail_fast: If true, validation will stop after the first iteration.

    Raises:
        CompilationError: If the static rules could not be compiled.
        ValidationError: If the message is invalid. The violations raised as part of this error should
            always be equal to the list of violations returned by `collect_violations`.
    """
    return _default_validator.validate(message, fail_fast=fail_fast)


def collect_violations(
    message: Message | google_message.Message, *, fail_fast: bool = False
) -> list[Violation]:
    """Collects the violations for the given message against the static rules defined in the message's descriptor using a shared validator.

    Parameters:
        message: The message to validate.
        fail_fast: If true, validation will stop after the first iteration.

    Returns:
        A list of Violation objects that describe the validation errors.

    Raises:
        CompilationError: If the static rules could not be compiled.
    """
    return _default_validator.collect_violations(message, fail_fast=fail_fast)


__all__ = [
    "CompilationError",
    "FieldPathElementPb",
    "FieldPathPb",
    "ValidationError",
    "Validator",
    "Violation",
    "ViolationPb",
    "ViolationsPb",
    "collect_violations",
    "validate",
]
