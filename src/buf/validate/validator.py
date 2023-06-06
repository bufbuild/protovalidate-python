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

import celpy

from src.buf.validate.internal import extra_func, constraints as _constraints
from src.buf import expression_pb2
from google.protobuf import descriptor
from google.protobuf import message

Violations = expression_pb2.Violations


class Validator:
    _constraints: dict[descriptor.Descriptor, _constraints.Constraints]
    _env: celpy.Environment

    def __init__(self):
        self._constraints = {}
        self._env = celpy.Environment()

    def validate(
        self,
        message: message.Message,
        fail_fast: bool = False,
        result: Violations = None,
    ) -> Violations:
        constraints = self._constraints.get(message.DESCRIPTOR)
        if constraints is None:
            constraints = _constraints.NewConstraints(
                self._env, extra_func.EXTRA_FUNCS, message.DESCRIPTOR
            )
            self._constraints[message.DESCRIPTOR] = constraints
        ctx = _constraints.ConstraintContext(fail_fast=fail_fast, violations=result)
        constraints.validate(ctx, "", message)
        return ctx.violations


_validator = Validator()
validate = _validator.validate
