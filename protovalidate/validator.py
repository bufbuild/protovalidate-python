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

import typing

from google.protobuf import message

from buf.validate import expression_pb2  # type: ignore
from protovalidate.internal import constraints as _constraints
from protovalidate.internal import extra_func

CompilationError = _constraints.CompilationError
Violations = expression_pb2.Violations


class Validator:
    """
    Validates protobuf messages against static constraints.

    Each validator instance caches internal state generated from the static
    constraints, so reusing the same instance for multiple validations
    significantly improves performance.
    """

    _factory: _constraints.ConstraintFactory

    def __init__(self):
        self._factory = _constraints.ConstraintFactory(extra_func.EXTRA_FUNCS)

    def validate(
        self,
        message: message.Message,
        *,
        fail_fast: bool = False,
    ):
        """
        Validates the given message against the static constraints defined in
        the message's descriptor.

        Parameters:
            message: The message to validate.
            fail_fast: If true, validation will stop after the first violation.
        Raises:
            CompilationError: If the static constraints could not be compiled.
            ValidationError: If the message is invalid.
        """
        violations = self.collect_violations(message, fail_fast=fail_fast)
        if violations.violations:
            msg = f"invalid {message.DESCRIPTOR.name}"
            raise ValidationError(msg, violations)

    def collect_violations(
        self,
        message: message.Message,
        *,
        fail_fast: bool = False,
        into: expression_pb2.Violations = None,
    ) -> expression_pb2.Violations:
        """
        Validates the given message against the static constraints defined in
        the message's descriptor. Compared to validate, collect_violations is
        faster but puts the burden of raising an appropriate exception on the
        caller.

        Parameters:
            message: The message to validate.
            fail_fast: If true, validation will stop after the first violation.
            into: If provided, any violations will be appended to the
                Violations object and the same object will be returned.
        Raises:
            CompilationError: If the static constraints could not be compiled.
        """
        ctx = _constraints.ConstraintContext(fail_fast=fail_fast, violations=into)
        for constraint in self._factory.get(message.DESCRIPTOR):
            constraint.validate(ctx, message)
            if ctx.done:
                break
        return ctx.violations


class ValidationError(ValueError):
    """
    An error raised when a message fails to validate.
    """

    violations: expression_pb2.Violations

    def __init__(self, msg: str, violations: expression_pb2.Violations):
        super().__init__(msg)
        self.violations = violations

    def errors(self) -> typing.List[expression_pb2.Violation]:
        """
        Returns the validation errors as a simple Python list, rather than the
        Protobuf-specific collection type used by Violations.
        """
        return list(self.violations.violations)
