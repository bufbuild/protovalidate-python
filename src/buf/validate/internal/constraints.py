import celpy

from google.protobuf import message
from google.protobuf import descriptor
from google.protobuf import json_format
from buf.validate import expression_pb2
from buf.validate import validate_pb2
from buf.validate.priv import private_pb2


class ConstraintContext:
    def __init__(
        self, fail_fast: bool = False, violations: expression_pb2.Violations = None
    ):
        self._fail_fast = fail_fast
        if violations is None:
            violations = expression_pb2.Violations()
        self._violations = violations

    @property
    def fail_fast(self) -> bool:
        return self._fail_fast

    @property
    def violations(self) -> expression_pb2.Violations:
        return self._violations

    def add(self, field_path: str, constraint_id: str, message: str):
        self._violations.violations.append(
            expression_pb2.Violation(
                field_path=field_path,
                constraint_id=constraint_id,
                message=message,
            )
        )

    @property
    def done(self) -> bool:
        return self._fail_fast and len(self._violations.violations) > 0


class ConstraintRules:
    def __init__(self, rules: message.Message):
        self._rules = rules

    @property
    def rules(self) -> message.Message:
        return self._rules

    def validate(
        self, ctx: ConstraintContext, field_path: str, message: message.Message
    ):
        ctx.add(field_path, "unimplemented", "Unimplemented")


class Constraints:
    _err: Exception | None = None
    _constraints: list[ConstraintRules]

    def __init__(self):
        self._constraints = []

    def add(self, constraint: ConstraintRules):
        self._constraints.append(constraint)

    def validate(
        self, ctx: ConstraintContext, field_path: str, message: message.Message
    ):
        if self._err is not None:
            raise self._err
        for constraint in self._constraints:
            constraint.validate(ctx, field_path, message)
            if ctx.done:
                return


def _MsgToCel(msg: message.Message) -> dict[str, any]:
    # convert the protobuf rules into json
    json = json_format.MessageToDict(
        msg, preserving_proto_field_name=True, use_integers_for_enums=True
    )
    return celpy.json_to_cel(json)


class CelConstraintRules(ConstraintRules):
    _runners: list[celpy.Runner]

    def __init__(self, rules: message.Message):
        super().__init__(rules)
        self._runners = []
        self._rules_cel = _MsgToCel(rules)

    def validate_cel(
        self, ctx: ConstraintContext, field_path: str, activation: dict[str, any]
    ):
        # convert the protobuf rules into json
        json = json_format.MessageToDict(
            self._rules, preserving_proto_field_name=True, use_integers_for_enums=True
        )
        activation["rules"] = self._rules_cel
        for runner in self._runners:
            result = runner.evaluate(activation)
            # TODO(afuller): Handle result

    def add_rule(
        self,
        env: celpy.Environment,
        rules: expression_pb2.Constraint | private_pb2.Constraint,
    ):
        ast = env.compile(rules.expression)
        prog = env.program(ast)
        self._runners.append(prog)

    def add_rules(
        self,
        env: celpy.Environment,
        rules: message.Message,
    ):
        # For each set field in the message, look for the private constraint extension.
        for field, _ in rules.ListFields():
            if private_pb2.field in field.GetOptions().Extensions:
                for cel in field.GetOptions().Extensions[private_pb2.field].cel:
                    self.add_rule(env, cel)


class MessageConstraintRules(CelConstraintRules):
    def validate(
        self, ctx: ConstraintContext, field_path: str, message: message.Message
    ):
        activation = {}
        # activation["this"] = _MsgToCel(message)
        self.validate_cel(ctx, field_path, activation)


class FieldConstraintRules(CelConstraintRules):
    _ignore_empty = False
    _required = False
    _any_rules = None

    def __init__(
        self,
        field: descriptor.FieldDescriptor,
        fieldLvl: validate_pb2.FieldConstraints,
        rules: message.Message,
        any_rules: ConstraintRules | None = None,
    ):
        super().__init__(rules)
        self._field = field
        if any_rules is not None:
            self._any_rules = any_rules
        if fieldLvl.ignore_empty:
            self._ignore_empty = True
        if fieldLvl.required:
            self._required = True

    def validate(
        self, ctx: ConstraintContext, field_path: str, message: message.Message
    ):
        if not self._has_field(message):
            if self._required:
                ctx.add(
                    self._make_field_path(field_path),
                    "required",
                    "Field is required but not set",
                )
                return
            if self._ignore_empty:
                return

        field_path = self._make_field_path(field_path)
        activation = {}
        value = getattr(message, self._field.name)
        # TODO(afuller): Bind the field to 'this' in the activation.
        self.validate_cel(ctx, field_path, activation)

    def _make_field_path(self, field_path: str) -> str:
        if len(field_path) == 0:
            return self._field.name
        return field_path + "." + self._field.name

    def _has_field(self, message: message.Message) -> bool:
        if self._field.label == descriptor.FieldDescriptor.LABEL_REPEATED:
            return len(getattr(message, self._field.name)) > 0
        elif self._field.cpp_type == descriptor.FieldDescriptor.CPPTYPE_MESSAGE:
            return getattr(message, self._field.name) is not None
        return True


class EnumConstraintRules(FieldConstraintRules):
    _defined_only = False

    def __init__(
        self, field: descriptor.FieldDescriptor, fieldLvl: validate_pb2.FieldConstraints
    ):
        super().__init__(field, fieldLvl, fieldLvl.enum)
        if fieldLvl.enum.defined_only:
            self._defined_only = True

    def validate(
        self, ctx: ConstraintContext, field_path: str, message: message.Message
    ):
        super().validate(ctx, field_path, message)
        if ctx.done:
            return
        if self._defined_only:
            value = getattr(message, self._field.name)
            if value not in self._field.enum_type.values_by_number:
                ctx.add(
                    self._make_field_path(field_path),
                    "enum.defined_only",
                    "value is not defined in enum",
                )


class RepeatedConstraintRules(FieldConstraintRules):
    _min_items = 0
    _max_items = 0

    def __init__(
        self, field: descriptor.FieldDescriptor, fieldLvl: validate_pb2.FieldConstraints
    ):
        super().__init__(field, fieldLvl, fieldLvl.repeated)
        if fieldLvl.repeated.min_items > 0:
            self._min_items = fieldLvl.repeated.min_items
        if fieldLvl.repeated.max_items > 0:
            self._max_items = fieldLvl.repeated.max_items

    def validate(
        self, ctx: ConstraintContext, field_path: str, message: message.Message
    ):
        super().validate(ctx, field_path, message)
        if ctx.done:
            return
        value = getattr(message, self._field.name)
        if len(value) < self._min_items:
            ctx.add(
                self._make_field_path(field_path),
                "repeated.min_items",
                "value must have at least {} items".format(self._min_items),
            )
        if self._max_items > 0 and len(value) > self._max_items:
            ctx.add(
                self._make_field_path(field_path),
                "repeated.max_items",
                "value can have at most {} items".format(self._max_items),
            )


class MapConstraintRules(FieldConstraintRules):
    _key_rules = None
    _value_rules = None

    def __init__(
        self,
        field: descriptor.FieldDescriptor,
        fieldLvl: validate_pb2.FieldConstraints,
        key_rules: ConstraintRules | None,
        value_rules: ConstraintRules | None,
    ):
        super().__init__(field, fieldLvl, fieldLvl.map)
        if key_rules is not None:
            self._key_rules = key_rules
        if value_rules is not None:
            self._value_rules = value_rules

    def validate(
        self, ctx: ConstraintContext, field_path: str, message: message.Message
    ):
        super().validate(ctx, field_path, message)
        if ctx.done or (self._key_rules is None and self._value_rules is None):
            return
        value = getattr(message, self._field.name)
        for key, value in value.items():
            key_field_path = field_path + "[{}]".format(key)
            if self._key_rules is not None:
                self._key_rules.validate(ctx, key_field_path, message)
            if self._value_rules is not None:
                self._value_rules.validate(ctx, key_field_path, message)


class OneofConstraintRules(ConstraintRules):
    required = True

    def __init__(
        self, oneof: descriptor.OneofDescriptor, rules: validate_pb2.OneofConstraints
    ):
        super().__init__(rules)
        self._oneof = oneof
        if not rules.required:
            self.required = False

    def validate(
        self, ctx: ConstraintContext, field_path: str, message: message.Message
    ):
        if not message.WhichOneof(self._oneof.name):
            if self.required:
                ctx.add(field_path, "oneof.required", "oneof is required")
            return


def NewMessageConstraint(
    env: celpy.Environment, rules: validate_pb2.message
) -> MessageConstraintRules:
    result = MessageConstraintRules(rules)
    for cel in rules.cel:
        result.add_rule(env, cel)
    return result


def NewScalarFieldConstraint(
    env: celpy.Environment,
    field: descriptor.FieldDescriptor,
    fieldLvl: validate_pb2.field,
):
    if field.type == descriptor.FieldDescriptor.TYPE_ENUM:
        return EnumConstraintRules(field, fieldLvl)
    elif field.type == descriptor.FieldDescriptor.TYPE_BOOL:
        result = FieldConstraintRules(field, fieldLvl, fieldLvl.bool)
        result.add_rules(env, fieldLvl.bool)
        return result
    elif field.type == descriptor.FieldDescriptor.TYPE_BYTES:
        result = FieldConstraintRules(field, fieldLvl, fieldLvl.bytes)
        result.add_rules(env, fieldLvl.bytes)
        return result
    elif field.type == descriptor.FieldDescriptor.TYPE_FIXED32:
        result = FieldConstraintRules(field, fieldLvl, fieldLvl.fixed32)
        result.add_rules(env, fieldLvl.fixed32)
        return result
    elif field.type == descriptor.FieldDescriptor.TYPE_FIXED64:
        result = FieldConstraintRules(field, fieldLvl, fieldLvl.fixed64)
        result.add_rules(env, fieldLvl.fixed64)
        return result
    elif field.type == descriptor.FieldDescriptor.TYPE_FLOAT:
        result = FieldConstraintRules(field, fieldLvl, fieldLvl.float)
        result.add_rules(env, fieldLvl.float)
        return result
    elif field.type == descriptor.FieldDescriptor.TYPE_INT32:
        result = FieldConstraintRules(field, fieldLvl, fieldLvl.int32)
        result.add_rules(env, fieldLvl.int32)
        return result
    elif field.type == descriptor.FieldDescriptor.TYPE_INT64:
        result = FieldConstraintRules(field, fieldLvl, fieldLvl.int64)
        result.add_rules(env, fieldLvl.int64)
        return result
    elif field.type == descriptor.FieldDescriptor.TYPE_SFIXED32:
        result = FieldConstraintRules(field, fieldLvl, fieldLvl.sfixed32)
        result.add_rules(env, fieldLvl.sfixed32)
        return result
    elif field.type == descriptor.FieldDescriptor.TYPE_SFIXED64:
        result = FieldConstraintRules(field, fieldLvl, fieldLvl.sfixed64)
        result.add_rules(env, fieldLvl.sfixed64)
        return result
    elif field.type == descriptor.FieldDescriptor.TYPE_SINT32:
        result = FieldConstraintRules(field, fieldLvl, fieldLvl.sint32)
        result.add_rules(env, fieldLvl.sint32)
        return result
    elif field.type == descriptor.FieldDescriptor.TYPE_SINT64:
        result = FieldConstraintRules(field, fieldLvl, fieldLvl.sint64)
        result.add_rules(env, fieldLvl.sint64)
        return result
    elif field.type == descriptor.FieldDescriptor.TYPE_UINT32:
        result = FieldConstraintRules(field, fieldLvl, fieldLvl.uint32)
        result.add_rules(env, fieldLvl.uint32)
        return result
    elif field.type == descriptor.FieldDescriptor.TYPE_UINT64:
        result = FieldConstraintRules(field, fieldLvl, fieldLvl.uint64)
        result.add_rules(env, fieldLvl.uint64)
        return result
    elif field.type == descriptor.FieldDescriptor.TYPE_STRING:
        result = FieldConstraintRules(field, fieldLvl, fieldLvl.string)
        result.add_rules(env, fieldLvl.string)
        return result


def NewFieldConstraint(
    env: celpy.Environment, field: descriptor.FieldDescriptor, rules: validate_pb2.field
) -> FieldConstraintRules:
    if field.label == descriptor.FieldDescriptor.LABEL_REPEATED:
        return None
    else:
        return NewScalarFieldConstraint(env, field, rules)


def NewConstraints(
    env: celpy.Environment, descriptor: descriptor.Descriptor
) -> Constraints:
    result = Constraints()
    if validate_pb2.message in descriptor.GetOptions().Extensions:
        if constraint := NewMessageConstraint(
            env, descriptor.GetOptions().Extensions[validate_pb2.message]
        ):
            result.add(constraint)

    for oneof in descriptor.oneofs:
        if validate_pb2.oneof in oneof.GetOptions().Extensions:
            if constraint := OneofConstraintRules(
                oneof, oneof.GetOptions().Extensions[validate_pb2.oneof]
            ):
                result.add(constraint)

    for field in descriptor.fields:
        if validate_pb2.field in field.GetOptions().Extensions:
            if constraint := NewFieldConstraint(
                env, field, field.GetOptions().Extensions[validate_pb2.field]
            ):
                result.add(constraint)

    return result
