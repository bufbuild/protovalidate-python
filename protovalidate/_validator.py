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

import typing
from typing import TYPE_CHECKING

from protobuf import Message, Registry

from protovalidate import _backend, _extra_func, _rules
from protovalidate._core import CompilationError, RuleContext, Violation
from protovalidate._gen.buf.validate import validate_pb

if TYPE_CHECKING:
    from google.protobuf import message as google_message


__all__ = [
    "CompilationError",
    "ValidationError",
    "Validator",
    "Violation",
    "Violations",
]
Violations = validate_pb.Violations


class _Engine(typing.Protocol):
    """A CEL backend: turns a protobuf-py message into a list of violations."""

    def collect_violations(
        self, message: Message, *, fail_fast: bool
    ) -> list[Violation]: ...


class _CelpyEngine:
    """The pure-Python celpy engine, evaluating directly over protobuf-py."""

    def __init__(self, registry: Registry | None) -> None:
        self._factory = _rules.RuleFactory(_extra_func.make_extra_funcs(), registry)

    def collect_violations(
        self, message: Message, *, fail_fast: bool
    ) -> list[Violation]:
        ctx = RuleContext(fail_fast=fail_fast)
        for rule in self._factory.get(type(message).desc()):
            rule.validate(ctx, message)
            if ctx.done:
                break
        for violation in ctx.violations:
            violation.finalize_paths()
        return ctx.violations


class _CelExprEngine:
    """The cel-expr-python (cel-cpp) engine.

    Rules are discovered from protobuf-py descriptors, but the CEL runtime only
    ingests google.protobuf, so every validated message is bridged to a google
    dynamic message (a serialize/parse round trip) before evaluation. The user's
    ``registry`` is not needed: custom predefined-rule extensions resolve off the
    global google pool the bridge mirrors into.
    """

    def __init__(self, registry: Registry | None) -> None:  # noqa: ARG002 - accepted for API symmetry
        from protovalidate import _celexpr  # noqa: PLC0415

        self._bridge = _celexpr.GoogleBridge()
        self._factory = _celexpr.RuleFactory(_celexpr.make_extension(), self._bridge)

    def collect_violations(
        self, message: Message, *, fail_fast: bool
    ) -> list[Violation]:
        bridged = self._bridge.to_google(message)
        ctx = RuleContext(fail_fast=fail_fast)
        for rule in self._factory.get(type(message).desc()):
            rule.validate(ctx, bridged)
            if ctx.done:
                break
        for violation in ctx.violations:
            violation.finalize_paths()
        return ctx.violations


class Validator:
    """Validates Protobuf messages against static rules.

    Both protobuf-py messages and legacy google.protobuf messages are
    accepted. A google.protobuf message is validated by copying it into a
    protobuf-py message of the same type; violation field values then refer
    to that copy.

    Each validator instance caches internal state generated from the static
    rules, so reusing the same instance for multiple validations
    significantly improves performance.
    """

    _engine: _Engine

    def __init__(self, registry: Registry | None = None) -> None:
        """Creates a new validator.

        Parameters:
            registry: An optional Registry used to resolve custom
                predefined-rule extensions. If omitted, only standard rules are applied.
        """
        try:
            import google.protobuf.message  # noqa: F401, PLC0415

            from protovalidate._legacy import LegacyMessageConverter  # noqa: PLC0415

            self._legacy = LegacyMessageConverter()
        except ImportError:
            self._legacy = None
        if _backend.CEL_EXPR_AVAILABLE:
            self._engine = _CelExprEngine(registry)
        else:
            self._engine = _CelpyEngine(registry)

    def validate(
        self, message: Message | google_message.Message, *, fail_fast: bool = False
    ) -> None:
        """Validates the given message against the static rules defined in the message's descriptor.

        Parameters:
            message: The message to validate.
            fail_fast: If true, validation will stop after the first iteration.

        Raises:
            CompilationError: If the static rules could not be compiled.
            ValidationError: If the message is invalid. The violations raised as part of this error should
            always be equal to the list of violations returned by `collect_violations`.
        """
        coerced = self._coerce(message)
        violations = self.collect_violations(coerced, fail_fast=fail_fast)
        if len(violations) > 0:
            msg = f"invalid {type(coerced).desc().name}"
            raise ValidationError(msg, violations)

    def collect_violations(
        self, message: Message | google_message.Message, *, fail_fast: bool = False
    ) -> list[Violation]:
        """Validates the given message against the static rules defined in the message's descriptor.

        Compared to `validate`, `collect_violations` simply returns the violations as a list and puts
        the burden of raising an appropriate exception on the caller.

        The violations returned from this method should always be equal to the violations
        raised as part of the ValidationError in the call to `validate`.

        Parameters:
            message: The message to validate.
            fail_fast: If true, validation will stop after the first iteration.

        Raises:
            CompilationError: If the static rules could not be compiled.
        """
        coerced = self._coerce(message)
        return self._engine.collect_violations(coerced, fail_fast=fail_fast)

    def _coerce(self, message: Message | google_message.Message) -> Message:
        if self._legacy:
            return self._legacy.normalize(message)
        assert isinstance(message, Message)  # noqa: S101
        return message


class ValidationError(ValueError):
    """An error raised when a message fails to validate."""

    _violations: list[Violation]

    def __init__(self, msg: str, violations: list[Violation]) -> None:
        super().__init__(msg)
        self._violations = violations

    def to_proto(self) -> validate_pb.Violations:
        """Provides the Protobuf form of the validation errors."""
        return validate_pb.Violations(
            violations=[violation.proto for violation in self._violations]
        )

    @property
    def violations(self) -> list[Violation]:
        """Returns the violation errors."""
        return self._violations
