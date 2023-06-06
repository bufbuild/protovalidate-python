import celpy

from buf.validate.internal import constraints as _constraints
from buf.validate.internal import extra_func
from buf.validate import expression_pb2
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
