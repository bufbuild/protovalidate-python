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
from celpy import celtypes
import datetime
from google.protobuf import message
from google.protobuf import descriptor
from buf.validate import expression_pb2
from buf.validate import validate_pb2
from buf.validate.priv import private_pb2


class CompilationError(Exception):
    pass


def make_duration(msg: message.Message) -> celtypes.DurationType:
    return celtypes.DurationType(
        seconds=msg.seconds,
        nanos=msg.nanos,
    )


def make_timestamp(msg: message.Message) -> celtypes.TimestampType:
    return make_duration(msg) + celtypes.TimestampType(1970, 1, 1)


def unwrap(msg: message.Message) -> celtypes.Value:
    return _FieldToCel(msg, msg.DESCRIPTOR.fields_by_name["value"])


_MSG_TYPE_URL_TO_CTOR = {
    "google.protobuf.Duration": make_duration,
    "google.protobuf.Timestamp": make_timestamp,
    "google.protobuf.StringValue": unwrap,
    "google.protobuf.BytesValue": unwrap,
    "google.protobuf.Int32Value": unwrap,
    "google.protobuf.Int64Value": unwrap,
    "google.protobuf.UInt32Value": unwrap,
    "google.protobuf.UInt64Value": unwrap,
    "google.protobuf.FloatValue": unwrap,
    "google.protobuf.DoubleValue": unwrap,
    "google.protobuf.BoolValue": unwrap,
}


def _MsgToCel(msg: message.Message) -> dict[str, celtypes.Value]:
    ctor = _MSG_TYPE_URL_TO_CTOR.get(msg.DESCRIPTOR.full_name)
    if ctor is not None:
        return ctor(msg)
    result = celtypes.MapType()
    field: descriptor.FieldDescriptor
    for field in msg.DESCRIPTOR.fields:
        if field.containing_oneof is not None and not msg.HasField(field.name):
            continue
        result[field.name] = _FieldToCel(msg, field)
    return result


_TYPE_TO_CTOR = {
    descriptor.FieldDescriptor.TYPE_MESSAGE: _MsgToCel,
    descriptor.FieldDescriptor.TYPE_ENUM: celtypes.IntType,
    descriptor.FieldDescriptor.TYPE_BOOL: celtypes.BoolType,
    descriptor.FieldDescriptor.TYPE_BYTES: celtypes.BytesType,
    descriptor.FieldDescriptor.TYPE_STRING: celtypes.StringType,
    descriptor.FieldDescriptor.TYPE_FLOAT: celtypes.DoubleType,
    descriptor.FieldDescriptor.TYPE_DOUBLE: celtypes.DoubleType,
    descriptor.FieldDescriptor.TYPE_INT32: celtypes.IntType,
    descriptor.FieldDescriptor.TYPE_INT64: celtypes.IntType,
    descriptor.FieldDescriptor.TYPE_UINT32: celtypes.UintType,
    descriptor.FieldDescriptor.TYPE_UINT64: celtypes.UintType,
    descriptor.FieldDescriptor.TYPE_SINT32: celtypes.IntType,
    descriptor.FieldDescriptor.TYPE_SINT64: celtypes.IntType,
    descriptor.FieldDescriptor.TYPE_FIXED32: celtypes.UintType,
    descriptor.FieldDescriptor.TYPE_FIXED64: celtypes.UintType,
    descriptor.FieldDescriptor.TYPE_SFIXED32: celtypes.IntType,
    descriptor.FieldDescriptor.TYPE_SFIXED64: celtypes.IntType,
}


def _FieldValToCel(val: any, field: descriptor.FieldDescriptor) -> celtypes.Value:
    ctor = _TYPE_TO_CTOR.get(field.type)
    if ctor is None:
        raise CompilationError("unknown field type")
    return ctor(val)


def _IsEmptyField(msg: message.Message, field: descriptor.FieldDescriptor) -> bool:
    if field.containing_oneof is not None and not msg.HasField(field.name):
        return True
    if field.label == descriptor.FieldDescriptor.LABEL_REPEATED:
        return len(getattr(msg, field.name)) == 0
    if field.type == descriptor.FieldDescriptor.TYPE_MESSAGE:
        return not msg.HasField(field.name)
    if field.type == descriptor.FieldDescriptor.TYPE_BOOL:
        return not getattr(msg, field.name)
    if field.type == descriptor.FieldDescriptor.TYPE_BYTES:
        return len(getattr(msg, field.name)) == 0
    if field.type == descriptor.FieldDescriptor.TYPE_STRING:
        return len(getattr(msg, field.name)) == 0
    if field.type == descriptor.FieldDescriptor.TYPE_FLOAT:
        return getattr(msg, field.name) == 0.0
    if field.type == descriptor.FieldDescriptor.TYPE_DOUBLE:
        return getattr(msg, field.name) == 0.0
    if field.type == descriptor.FieldDescriptor.TYPE_INT32:
        return getattr(msg, field.name) == 0
    if field.type == descriptor.FieldDescriptor.TYPE_INT64:
        return getattr(msg, field.name) == 0
    if field.type == descriptor.FieldDescriptor.TYPE_UINT32:
        return getattr(msg, field.name) == 0
    if field.type == descriptor.FieldDescriptor.TYPE_UINT64:
        return getattr(msg, field.name) == 0
    if field.type == descriptor.FieldDescriptor.TYPE_SINT32:
        return getattr(msg, field.name) == 0
    if field.type == descriptor.FieldDescriptor.TYPE_SINT64:
        return getattr(msg, field.name) == 0
    if field.type == descriptor.FieldDescriptor.TYPE_FIXED32:
        return getattr(msg, field.name) == 0
    if field.type == descriptor.FieldDescriptor.TYPE_FIXED64:
        return getattr(msg, field.name) == 0
    if field.type == descriptor.FieldDescriptor.TYPE_SFIXED32:
        return getattr(msg, field.name) == 0
    if field.type == descriptor.FieldDescriptor.TYPE_SFIXED64:
        return getattr(msg, field.name) == 0
    if field.type == descriptor.FieldDescriptor.TYPE_ENUM:
        return getattr(msg, field.name) == 0
    raise ValueError("unknown field type")


def _RepeatedFieldToCel(
    msg: message.Message, field: descriptor.FieldDescriptor
) -> celtypes.Value:
    result = celtypes.ListType()
    for val in getattr(msg, field.name):
        result.append(_FieldValToCel(val, field))
    return result


def _MapFieldToCel(
    msg: message.Message, field: descriptor.FieldDescriptor
) -> celtypes.Value:
    result = celtypes.MapType()
    key_field = field.message_type.fields[0]
    val_field = field.message_type.fields[1]
    for key, val in getattr(msg, field.name).items():
        result[_FieldValToCel(key, key_field)] = _FieldValToCel(val, val_field)
    return result


def _FieldToCel(
    msg: message.Message, field: descriptor.FieldDescriptor
) -> celtypes.Value:
    if field.message_type is not None and field.message_type.GetOptions().map_entry:
        return _MapFieldToCel(msg, field)
    if field.label == descriptor.FieldDescriptor.LABEL_REPEATED:
        return _RepeatedFieldToCel(msg, field)
    elif field.message_type is not None and not msg.HasField(field.name):
        return None
    else:
        return _FieldValToCel(getattr(msg, field.name), field)


class ConstraintContext:
    """The state associated with a single constraint evaluation."""

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
    """The constrains associated with a single 'rules' message."""

    def validate(
        self, ctx: ConstraintContext, field_path: str, message: message.Message
    ):
        """Validate the message against the rules in this constraint."""
        ctx.add(field_path, "unimplemented", "Unimplemented")


class CelConstraintRules(ConstraintRules):
    """A constraint that has rules written in CEL."""

    _runners: list[celpy.Runner]
    _rules_cel: celtypes.Value = None

    def __init__(self, rules: message.Message | None):
        self._runners = []
        if rules is not None:
            self._rules_cel = _MsgToCel(rules)

    def validate_cel(
        self, ctx: ConstraintContext, field_path: str, activation: dict[str, any]
    ):
        activation["rules"] = self._rules_cel
        activation["now"] = celtypes.TimestampType(
            datetime.datetime.now(tz=datetime.timezone.utc)
        )
        for runner in self._runners:
            result = runner.evaluate(activation)

            if isinstance(result, celtypes.BoolType):
                if not result:
                    ctx.add(field_path, "cel", "CEL constraint failed")
            elif isinstance(result, celtypes.StringType):
                if result:
                    ctx.add(field_path, "cel", result)
            elif isinstance(result, Exception):
                raise result

    def add_rule(
        self,
        env: celpy.Environment,
        funcs: dict[str, celpy.CELFunction],
        rules: expression_pb2.Constraint | private_pb2.Constraint,
    ):
        ast = env.compile(rules.expression)
        prog = env.program(ast, functions=funcs)
        self._runners.append(prog)

    def add_rules(
        self,
        env: celpy.Environment,
        funcs: dict[str, celpy.CELFunction],
        rules: message.Message,
    ):
        # For each set field in the message, look for the private constraint extension.
        for field, _ in rules.ListFields():
            if private_pb2.field in field.GetOptions().Extensions:
                for cel in field.GetOptions().Extensions[private_pb2.field].cel:
                    self.add_rule(env, funcs, cel)


class MessageConstraintRules(CelConstraintRules):
    """Message-level rules."""

    def validate(
        self, ctx: ConstraintContext, field_path: str, message: message.Message
    ):
        activation = {}
        # TODO: Support binding recursive messages.
        # activation["this"] = _MsgToCel(message)
        self.validate_cel(ctx, field_path, activation)


def check_field_type(
    field: descriptor.FieldDescriptor, expected: int, wrapper_name: str | None = None
):
    if field.type != expected and (
        field.type != descriptor.FieldDescriptor.TYPE_MESSAGE
        or field.message_type.full_name != wrapper_name
    ):
        raise CompilationError(
            f"field {field.name} has type {field.type} but expected {expected}"
        )


class FieldConstraintRules(CelConstraintRules):
    """Field-level rules."""

    _ignore_empty = False
    _required = False
    _any_rules = None

    def __init__(
        self,
        field: descriptor.FieldDescriptor,
        fieldLvl: validate_pb2.FieldConstraints,
        any_rules: ConstraintRules | None = None,
    ):
        type_case = fieldLvl.WhichOneof("type")
        super().__init__(None if type_case is None else getattr(fieldLvl, type_case))
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
        if _IsEmptyField(message, self._field):
            if self._required:
                ctx.add(
                    self._make_field_path(field_path),
                    "required",
                    "Field is required but not set",
                )
                return
            if (
                self._ignore_empty
                or self._field.type == descriptor.FieldDescriptor.TYPE_MESSAGE
                or self._field.containing_oneof is not None
            ):
                return

        field_path = self._make_field_path(field_path)
        self.validate_cel(ctx, field_path, {"this": _FieldToCel(message, self._field)})

    def _make_field_path(self, field_path: str) -> str:
        if len(field_path) == 0:
            return self._field.name
        return field_path + "." + self._field.name


class EnumConstraintRules(FieldConstraintRules):
    """Rules for an enum field."""

    _defined_only = False

    def __init__(
        self, field: descriptor.FieldDescriptor, fieldLvl: validate_pb2.FieldConstraints
    ):
        super().__init__(field, fieldLvl)
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
    """Rules for a repeated field."""

    _min_items = 0
    _max_items = 0
    _item_rules: ConstraintRules | None = None

    def __init__(
        self,
        field: descriptor.FieldDescriptor,
        fieldLvl: validate_pb2.FieldConstraints,
        item_rules: ConstraintRules | None,
    ):
        super().__init__(field, fieldLvl)
        if item_rules is not None:
            self._item_rules = item_rules
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
        sub_path = self._make_field_path(field_path)
        if self._item_rules is not None:
            for i, item in enumerate(value):
                self._item_rules.validate_cel(
                    ctx,
                    "{}[{}]".format(sub_path, i),
                    {"this": _FieldValToCel(item, self._field)},
                )
                if ctx.done:
                    return

        if len(value) < self._min_items:
            ctx.add(
                sub_path,
                "repeated.min_items",
                "value must have at least {} items".format(self._min_items),
            )
        if self._max_items > 0 and len(value) > self._max_items:
            ctx.add(
                sub_path,
                "repeated.max_items",
                "value can have at most {} items".format(self._max_items),
            )


class MapConstraintRules(FieldConstraintRules):
    """Rules for a map field."""

    _min_pairs = 0
    _max_pairs = 0
    _key_rules = None
    _value_rules = None

    def __init__(
        self,
        field: descriptor.FieldDescriptor,
        fieldLvl: validate_pb2.FieldConstraints,
        key_rules: ConstraintRules | None,
        value_rules: ConstraintRules | None,
    ):
        super().__init__(field, fieldLvl)
        if fieldLvl.map.min_pairs > 0:
            self._min_pairs = fieldLvl.map.min_pairs
        if fieldLvl.map.max_pairs > 0:
            self._max_pairs = fieldLvl.map.max_pairs
        if key_rules is not None:
            self._key_rules = key_rules
        if value_rules is not None:
            self._value_rules = value_rules

    def validate(
        self, ctx: ConstraintContext, field_path: str, message: message.Message
    ):
        super().validate(ctx, field_path, message)
        if ctx.done:
            return
        value = getattr(message, self._field.name)
        if self._ignore_empty and len(value) == 0:
            return
        if len(value) < self._min_pairs:
            ctx.add(
                field_path,
                "map.min_pairs",
                "value must have at least {} pairs".format(self._min_pairs),
            )
        if self._max_pairs > 0 and len(value) > self._max_pairs:
            ctx.add(
                field_path,
                "map.max_pairs",
                "value can have at most {} pairs".format(self._max_pairs),
            )
        for key, value in value.items():
            key_field_path = field_path + "[{}]".format(key)
            if self._key_rules is not None:
                key_field = self._field.message_type.fields_by_name["key"]
                self._key_rules.validate_cel(
                    ctx, key_field_path, {"this": _FieldValToCel(key, key_field)}
                )
            if self._value_rules is not None:
                value_field = self._field.message_type.fields_by_name["value"]
                self._value_rules.validate_cel(
                    ctx, key_field_path, {"this": _FieldValToCel(value, value_field)}
                )


class OneofConstraintRules(ConstraintRules):
    """Rules for a oneof definition."""

    required = True

    def __init__(
        self, oneof: descriptor.OneofDescriptor, rules: validate_pb2.OneofConstraints
    ):
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


class ConstraintFactory:
    """Factory for creating and caching constraints."""

    _env: celpy.Environment
    _funcs: dict[str, celpy.CELFunction]
    _cache: dict[descriptor.Descriptor, list[ConstraintRules] | Exception]

    def __init__(self, funcs: dict[str, celpy.CELFunction]):
        self._env = celpy.Environment()
        self._funcs = funcs
        self._cache = {}

    def get(self, descriptor: descriptor.Descriptor) -> list[ConstraintRules]:
        if descriptor not in self._cache:
            try:
                self._cache[descriptor] = self._new_constraints(descriptor)
            except Exception as e:
                self._cache[descriptor] = e
        result = self._cache[descriptor]
        if isinstance(result, Exception):
            raise result
        return result

    def _new_message_constraint(
        self, rules: validate_pb2.message
    ) -> MessageConstraintRules:
        result = MessageConstraintRules(rules)
        for cel in rules.cel:
            result.add_rule(self._env, self._funcs, cel)
        return result

    def _new_scalar_field_constraint(
        self,
        field: descriptor.FieldDescriptor,
        fieldLvl: validate_pb2.field,
    ):
        type_case = fieldLvl.WhichOneof("type")
        if type_case is None:
            result = FieldConstraintRules(field, fieldLvl, None)
            return result
        elif type_case == "duration":
            check_field_type(field, 0, "google.protobuf.Duration")
            result = FieldConstraintRules(field, fieldLvl)
            result.add_rules(self._env, self._funcs, fieldLvl.duration)
            return result
        elif type_case == "timestamp":
            check_field_type(field, 0, "google.protobuf.Timestamp")
            result = FieldConstraintRules(field, fieldLvl)
            result.add_rules(self._env, self._funcs, fieldLvl.timestamp)
            return result
        elif type_case == "enum":
            check_field_type(field, descriptor.FieldDescriptor.TYPE_ENUM)
            result = EnumConstraintRules(field, fieldLvl)
            result.add_rules(self._env, self._funcs, fieldLvl.enum)
            return result
        elif type_case == "bool":
            check_field_type(
                field, descriptor.FieldDescriptor.TYPE_BOOL, "google.protobuf.BoolValue"
            )
            result = FieldConstraintRules(field, fieldLvl)
            result.add_rules(self._env, self._funcs, fieldLvl.bool)
            return result
        elif type_case == "bytes":
            check_field_type(
                field,
                descriptor.FieldDescriptor.TYPE_BYTES,
                "google.protobuf.BytesValue",
            )
            result = FieldConstraintRules(field, fieldLvl)
            result.add_rules(self._env, self._funcs, fieldLvl.bytes)
            return result
        elif type_case == "fixed32":
            check_field_type(field, descriptor.FieldDescriptor.TYPE_FIXED32)
            result = FieldConstraintRules(field, fieldLvl)
            result.add_rules(self._env, self._funcs, fieldLvl.fixed32)
            return result
        elif type_case == "fixed64":
            check_field_type(field, descriptor.FieldDescriptor.TYPE_FIXED64)
            result = FieldConstraintRules(field, fieldLvl)
            result.add_rules(self._env, self._funcs, fieldLvl.fixed64)
            return result
        elif type_case == "float":
            check_field_type(
                field,
                descriptor.FieldDescriptor.TYPE_FLOAT,
                "google.protobuf.FloatValue",
            )
            result = FieldConstraintRules(field, fieldLvl)
            result.add_rules(self._env, self._funcs, fieldLvl.float)
            return result
        elif type_case == "double":
            check_field_type(
                field,
                descriptor.FieldDescriptor.TYPE_DOUBLE,
                "google.protobuf.DoubleValue",
            )
            result = FieldConstraintRules(field, fieldLvl)
            result.add_rules(self._env, self._funcs, fieldLvl.double)
            return result
        elif type_case == "int32":
            check_field_type(
                field,
                descriptor.FieldDescriptor.TYPE_INT32,
                "google.protobuf.Int32Value",
            )
            result = FieldConstraintRules(field, fieldLvl)
            result.add_rules(self._env, self._funcs, fieldLvl.int32)
            return result
        elif type_case == "int64":
            check_field_type(
                field,
                descriptor.FieldDescriptor.TYPE_INT64,
                "google.protobuf.Int64Value",
            )
            result = FieldConstraintRules(field, fieldLvl)
            result.add_rules(self._env, self._funcs, fieldLvl.int64)
            return result
        elif type_case == "sfixed32":
            check_field_type(field, descriptor.FieldDescriptor.TYPE_SFIXED32)
            result = FieldConstraintRules(field, fieldLvl)
            result.add_rules(self._env, self._funcs, fieldLvl.sfixed32)
            return result
        elif type_case == "sfixed64":
            check_field_type(field, descriptor.FieldDescriptor.TYPE_SFIXED64)
            result = FieldConstraintRules(field, fieldLvl)
            result.add_rules(self._env, self._funcs, fieldLvl.sfixed64)
            return result
        elif type_case == "sint32":
            check_field_type(field, descriptor.FieldDescriptor.TYPE_SINT32)
            result = FieldConstraintRules(field, fieldLvl)
            result.add_rules(self._env, self._funcs, fieldLvl.sint32)
            return result
        elif type_case == "sint64":
            check_field_type(field, descriptor.FieldDescriptor.TYPE_SINT64)
            result = FieldConstraintRules(field, fieldLvl)
            result.add_rules(self._env, self._funcs, fieldLvl.sint64)
            return result
        elif type_case == "uint32":
            check_field_type(
                field,
                descriptor.FieldDescriptor.TYPE_UINT32,
                "google.protobuf.UInt32Value",
            )
            result = FieldConstraintRules(field, fieldLvl)
            result.add_rules(self._env, self._funcs, fieldLvl.uint32)
            return result
        elif type_case == "uint64":
            check_field_type(
                field,
                descriptor.FieldDescriptor.TYPE_UINT64,
                "google.protobuf.UInt64Value",
            )
            result = FieldConstraintRules(field, fieldLvl)
            result.add_rules(self._env, self._funcs, fieldLvl.uint64)
            return result
        elif type_case == "string":
            check_field_type(
                field,
                descriptor.FieldDescriptor.TYPE_STRING,
                "google.protobuf.StringValue",
            )
            result = FieldConstraintRules(field, fieldLvl)
            result.add_rules(self._env, self._funcs, fieldLvl.string)
            return result

    def _new_field_constraint(
        self,
        field: descriptor.FieldDescriptor,
        rules: validate_pb2.field,
    ) -> FieldConstraintRules:
        if field.label != descriptor.FieldDescriptor.LABEL_REPEATED:
            return self._new_scalar_field_constraint(field, rules)
        if field.message_type is not None and field.message_type.GetOptions().map_entry:
            key_rules = None
            if rules.map.HasField("keys"):
                key_field = field.message_type.fields_by_name["key"]
                key_rules = self._new_scalar_field_constraint(key_field, rules.map.keys)
            value_rules = None
            if rules.map.HasField("values"):
                value_field = field.message_type.fields_by_name["value"]
                value_rules = self._new_scalar_field_constraint(
                    value_field, rules.map.values
                )
            return MapConstraintRules(field, rules, key_rules, value_rules)
        item_rule = None
        if rules.repeated.HasField("items"):
            item_rule = self._new_scalar_field_constraint(field, rules.repeated.items)
        return RepeatedConstraintRules(field, rules, item_rule)

    def _new_constraints(self, desc: descriptor.Descriptor) -> list[ConstraintRules]:
        result = []
        if validate_pb2.message in desc.GetOptions().Extensions:
            if constraint := self._new_message_constraint(
                desc.GetOptions().Extensions[validate_pb2.message]
            ):
                result.append(constraint)

        for oneof in desc.oneofs:
            if validate_pb2.oneof in oneof.GetOptions().Extensions:
                if constraint := OneofConstraintRules(
                    oneof, oneof.GetOptions().Extensions[validate_pb2.oneof]
                ):
                    result.append(constraint)

        for field in desc.fields:
            if validate_pb2.field in field.GetOptions().Extensions:
                fieldLvl = field.GetOptions().Extensions[validate_pb2.field]
                if constraint := self._new_field_constraint(field, fieldLvl):
                    result.append(constraint)

        return result
