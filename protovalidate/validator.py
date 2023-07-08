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

from google.protobuf import message

from buf.validate import expression_pb2  # type: ignore
from protovalidate.internal import constraints as _constraints
from protovalidate.internal import extra_func

CompilationError = _constraints.CompilationError
Violations = expression_pb2.Violations


class Validator:
    """
    Validates protobuf messages against static constraints.

    Each validator instance is caches internal state generated from the static
    constraints, so it is recommended to reuse the same instance for multiple
    validations.
    """

    _factory: _constraints.ConstraintFactory

    def __init__(self):
        self._factory = _constraints.ConstraintFactory(extra_func.EXTRA_FUNCS)

    def validate(
        self,
        message: message.Message,
        fail_fast: bool = False,
        result: expression_pb2.Violations = None,
    ) -> expression_pb2.Violations:
        """
        Validates the given message against the static constraints defined in
        the message's descriptor.

        Parameters:
            message: The message to validate.
            fail_fast: If true, validation will stop after the first violation.
            result: If provided, violations will be appended to this object, and
                this object will be returned. Otherwise, a new Violations object
                is allocated and returned.
        Returns:
            A Violations object containing any violations found.
        Raises:
            CompilationError: If the static constraints could not be compiled.
        """
        ctx = _constraints.ConstraintContext(fail_fast=fail_fast, violations=result)
        for constraint in self._factory.get(message.DESCRIPTOR):
            constraint.validate(ctx, message)
            if ctx.done:
                break
        return ctx.violations
