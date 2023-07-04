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
from google.protobuf import any_pb2
from google.protobuf import message
from google.protobuf import descriptor
from buf.validate import expression_pb2
from buf.validate import validate_pb2
from buf.validate.priv import private_pb2
from protovalidate.internal import string_format


class CompilationError(Exception):
    pass


def make_key_path(field_name: str, key: celtypes.Value) -> str:
    return f"{field_name}[{string_format.format_value(key)}]"


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


def _ScalarFieldValueToCel(
    val: any, field: descriptor.FieldDescriptor
) -> celtypes.Value:
    ctor = _TYPE_TO_CTOR.get(field.type)
    if ctor is None:
        raise CompilationError("unknown field type")
    return ctor(val)


def _FieldValueToCel(val: any, field: descriptor.FieldDescriptor) -> celtypes.Value:
    if field.label == descriptor.FieldDescriptor.LABEL_REPEATED:
        if field.message_type is not None and field.message_type.GetOptions().map_entry:
            return _MapFieldValueToCel(val, field)
        return _RepeatedFieldValueToCel(val, field)
    return _ScalarFieldValueToCel(val, field)


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
    if field.message_type is not None and field.message_type.GetOptions().map_entry:
        return _MapFieldToCel(msg, field)
    return _RepeatedFieldValueToCel(getattr(msg, field.name), field)


def _RepeatedFieldValueToCel(
    val: any, field: descriptor.FieldDescriptor
) -> celtypes.Value:
    result = celtypes.ListType()
    for item in val:
        result.append(_ScalarFieldValueToCel(item, field))
    return result


def _MapFieldValueToCel(map: any, field: descriptor.FieldDescriptor) -> celtypes.Value:
    result = celtypes.MapType()
    key_field = field.message_type.fields[0]
    val_field = field.message_type.fields[1]
    for key, val in map.items():
        result[_FieldValueToCel(key, key_field)] = _FieldValueToCel(val, val_field)
    return result


def _MapFieldToCel(
    msg: message.Message, field: descriptor.FieldDescriptor
) -> celtypes.Value:
    return _MapFieldValueToCel(getattr(msg, field.name), field)


def _FieldToCel(
    msg: message.Message, field: descriptor.FieldDescriptor
) -> celtypes.Value:
    if field.label == descriptor.FieldDescriptor.LABEL_REPEATED:
        return _RepeatedFieldToCel(msg, field)
    elif field.message_type is not None and not msg.HasField(field.name):
        return None
    else:
        return _ScalarFieldValueToCel(getattr(msg, field.name), field)


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

    def add(self, field_name: str, constraint_id: str, message: str):
        self._violations.violations.append(
            expression_pb2.Violation(
                field_path=field_name,
                constraint_id=constraint_id,
                message=message,
            )
        )

    def add_errors(self, other_ctx):
        self._violations.violations.extend(other_ctx.violations.violations)

    def add_path_prefix(self, prefix: str, delim="."):
        for violation in self._violations.violations:
            if violation.field_path:
                violation.field_path = prefix + delim + violation.field_path
            else:
                violation.field_path = prefix

    @property
    def done(self) -> bool:
        return self._fail_fast and self.has_errors

    def has_errors(self) -> bool:
        return len(self._violations.violations) > 0

    def sub_context(self):
        return ConstraintContext(self._fail_fast)


class ConstraintRules:
    """The constrains associated with a single 'rules' message."""

    def validate(self, ctx: ConstraintContext, message: message.Message):
        """Validate the message against the rules in this constraint."""
        ctx.add("", "unimplemented", "Unimplemented")


class CelConstraintRules(ConstraintRules):
    """A constraint that has rules written in CEL."""

    _runners: list[(celpy.Runner, expression_pb2.Constraint | private_pb2.Constraint)]
    _rules_cel: celtypes.Value = None

    def __init__(self, rules: message.Message | None):
        self._runners = []
        if rules is not None:
            self._rules_cel = _MsgToCel(rules)

    def _validate_cel(
        self, ctx: ConstraintContext, field_name: str, activation: dict[str, any]
    ):
        activation["rules"] = self._rules_cel
        activation["now"] = celtypes.TimestampType(
            datetime.datetime.now(tz=datetime.timezone.utc)
        )
        for runner, constraint in self._runners:
            result = runner.evaluate(activation)
            if isinstance(result, celtypes.BoolType):
                if not result:
                    ctx.add(field_name, constraint.id, constraint.message)
            elif isinstance(result, celtypes.StringType):
                if result:
                    ctx.add(field_name, constraint.id, result)
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
        self._runners.append((prog, rules))


class MessageConstraintRules(CelConstraintRules):
    """Message-level rules."""

    def validate(self, ctx: ConstraintContext, message: message.Message):
        self._validate_cel(ctx, "", {"this": _MsgToCel(message)})


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

    def __init__(
        self,
        env: celpy.Environment,
        funcs: dict[str, celpy.CELFunction],
        field: descriptor.FieldDescriptor,
        fieldLvl: validate_pb2.FieldConstraints,
    ):
        type_case = fieldLvl.WhichOneof("type")
        super().__init__(None if type_case is None else getattr(fieldLvl, type_case))
        self._field = field
        if fieldLvl.ignore_empty:
            self._ignore_empty = True
        if fieldLvl.required:
            self._required = True
        type_case = fieldLvl.WhichOneof("type")
        if type_case is not None:
            rules = getattr(fieldLvl, type_case)
            # For each set field in the message, look for the private constraint extension.
            for field, _ in rules.ListFields():
                if private_pb2.field in field.GetOptions().Extensions:
                    for cel in field.GetOptions().Extensions[private_pb2.field].cel:
                        self.add_rule(env, funcs, cel)
        for cel in fieldLvl.cel:
            self.add_rule(env, funcs, cel)

    def validate(self, ctx: ConstraintContext, message: message.Message):
        if _IsEmptyField(message, self._field):
            if self._required:
                ctx.add(
                    self._field.name,
                    "required",
                    "value is required",
                )
                return
            if (
                self._ignore_empty
                or (
                    self._field.label != descriptor.FieldDescriptor.LABEL_REPEATED
                    and self._field.type == descriptor.FieldDescriptor.TYPE_MESSAGE
                )
                or self._field.containing_oneof is not None
            ):
                return
        val = getattr(message, self._field.name)
        self._validate_value(ctx, self._field.name, val)
        self._validate_cel(
            ctx, self._field.name, {"this": _FieldValueToCel(val, self._field)}
        )

    def validate_item(self, ctx: ConstraintContext, field_path: str, val: any):
        self._validate_value(ctx, field_path, val)
        self._validate_cel(
            ctx, field_path, {"this": _ScalarFieldValueToCel(val, self._field)}
        )

    def _validate_value(self, ctx: ConstraintContext, field_path: str, val: any):
        pass


class AnyConstraintRules(FieldConstraintRules):
    """Rules for an Any field."""

    _in = []
    _not_in = []

    def __init__(
        self,
        env: celpy.Environment,
        funcs: dict[str, celpy.CELFunction],
        field: descriptor.FieldDescriptor,
        fieldLvl: validate_pb2.FieldConstraints,
    ):
        super().__init__(env, funcs, field, fieldLvl)
        if getattr(fieldLvl.any, "in"):
            self._in = getattr(fieldLvl.any, "in")
        if fieldLvl.any.not_in:
            self._not_in = fieldLvl.any.not_in

    def _validate_value(
        self, ctx: ConstraintContext, field_path: str, value: any_pb2.Any
    ):
        if len(self._in) > 0:
            if value.type_url not in self._in:
                ctx.add(
                    field_path,
                    "any.in",
                    f"Type {value.type_url} is not in {self._in}",
                )
        if value.type_url in self._not_in:
            ctx.add(
                field_path,
                "any.not_in",
                f"Type {value.type_url} is in {self._not_in}",
            )


class EnumConstraintRules(FieldConstraintRules):
    """Rules for an enum field."""

    _defined_only = False

    def __init__(
        self,
        env: celpy.Environment,
        funcs: dict[str, celpy.CELFunction],
        field: descriptor.FieldDescriptor,
        fieldLvl: validate_pb2.FieldConstraints,
    ):
        super().__init__(env, funcs, field, fieldLvl)
        if fieldLvl.enum.defined_only:
            self._defined_only = True

    def validate(self, ctx: ConstraintContext, message: message.Message):
        super().validate(ctx, message)
        if ctx.done:
            return
        if self._defined_only:
            value = getattr(message, self._field.name)
            if value not in self._field.enum_type.values_by_number:
                ctx.add(
                    self._field.name,
                    "enum.defined_only",
                    "value must be one of the defined enum values",
                )


class RepeatedConstraintRules(FieldConstraintRules):
    """Rules for a repeated field."""

    _item_rules: ConstraintRules | None = None

    def __init__(
        self,
        env: celpy.Environment,
        funcs: dict[str, celpy.CELFunction],
        field: descriptor.FieldDescriptor,
        fieldLvl: validate_pb2.FieldConstraints,
        item_rules: ConstraintRules | None,
    ):
        super().__init__(env, funcs, field, fieldLvl)
        if item_rules is not None:
            self._item_rules = item_rules

    def validate(self, ctx: ConstraintContext, message: message.Message):
        super().validate(ctx, message)
        if ctx.done:
            return
        value = getattr(message, self._field.name)
        if self._item_rules is not None:
            for i, item in enumerate(value):
                sub_ctx = ctx.sub_context()
                self._item_rules.validate_item(sub_ctx, "", item)
                if sub_ctx.has_errors():
                    sub_ctx.add_path_prefix(f"{self._field.name}[{i}]", "")
                    ctx.add_errors(sub_ctx)
                if ctx.done:
                    return


class MapConstraintRules(FieldConstraintRules):
    """Rules for a map field."""

    _key_rules = None
    _value_rules = None

    def __init__(
        self,
        env: celpy.Environment,
        funcs: dict[str, celpy.CELFunction],
        field: descriptor.FieldDescriptor,
        fieldLvl: validate_pb2.FieldConstraints,
        key_rules: ConstraintRules | None,
        value_rules: ConstraintRules | None,
    ):
        super().__init__(env, funcs, field, fieldLvl)
        if key_rules is not None:
            self._key_rules = key_rules
        if value_rules is not None:
            self._value_rules = value_rules

    def validate(self, ctx: ConstraintContext, message: message.Message):
        super().validate(ctx, message)
        if ctx.done:
            return
        value = getattr(message, self._field.name)
        for key, value in value.items():
            key_field_path = make_key_path(self._field.name, key)
            if self._key_rules is not None:
                self._key_rules.validate_item(ctx, key_field_path, key)
            if self._value_rules is not None:
                self._value_rules.validate_item(ctx, key_field_path, value)


class OneofConstraintRules(ConstraintRules):
    """Rules for a oneof definition."""

    required = True

    def __init__(
        self, oneof: descriptor.OneofDescriptor, rules: validate_pb2.OneofConstraints
    ):
        self._oneof = oneof
        if not rules.required:
            self.required = False

    def validate(self, ctx: ConstraintContext, message: message.Message):
        if not message.WhichOneof(self._oneof.name):
            if self.required:
                ctx.add(
                    self._oneof.name,
                    "required",
                    "exactly one field is required in oneof",
                )
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
        if fieldLvl.skipped:
            return None
        type_case = fieldLvl.WhichOneof("type")
        if type_case is None:
            result = FieldConstraintRules(self._env, self._funcs, field, fieldLvl)
            return result
        elif type_case == "duration":
            check_field_type(field, 0, "google.protobuf.Duration")
            result = FieldConstraintRules(self._env, self._funcs, field, fieldLvl)
            return result
        elif type_case == "timestamp":
            check_field_type(field, 0, "google.protobuf.Timestamp")
            result = FieldConstraintRules(self._env, self._funcs, field, fieldLvl)
            return result
        elif type_case == "enum":
            check_field_type(field, descriptor.FieldDescriptor.TYPE_ENUM)
            result = EnumConstraintRules(self._env, self._funcs, field, fieldLvl)
            return result
        elif type_case == "bool":
            check_field_type(
                field, descriptor.FieldDescriptor.TYPE_BOOL, "google.protobuf.BoolValue"
            )
            result = FieldConstraintRules(self._env, self._funcs, field, fieldLvl)
            return result
        elif type_case == "bytes":
            check_field_type(
                field,
                descriptor.FieldDescriptor.TYPE_BYTES,
                "google.protobuf.BytesValue",
            )
            result = FieldConstraintRules(self._env, self._funcs, field, fieldLvl)
            return result
        elif type_case == "fixed32":
            check_field_type(field, descriptor.FieldDescriptor.TYPE_FIXED32)
            result = FieldConstraintRules(self._env, self._funcs, field, fieldLvl)
            return result
        elif type_case == "fixed64":
            check_field_type(field, descriptor.FieldDescriptor.TYPE_FIXED64)
            result = FieldConstraintRules(self._env, self._funcs, field, fieldLvl)
            return result
        elif type_case == "float":
            check_field_type(
                field,
                descriptor.FieldDescriptor.TYPE_FLOAT,
                "google.protobuf.FloatValue",
            )
            result = FieldConstraintRules(self._env, self._funcs, field, fieldLvl)
            return result
        elif type_case == "double":
            check_field_type(
                field,
                descriptor.FieldDescriptor.TYPE_DOUBLE,
                "google.protobuf.DoubleValue",
            )
            result = FieldConstraintRules(self._env, self._funcs, field, fieldLvl)
            return result
        elif type_case == "int32":
            check_field_type(
                field,
                descriptor.FieldDescriptor.TYPE_INT32,
                "google.protobuf.Int32Value",
            )
            result = FieldConstraintRules(self._env, self._funcs, field, fieldLvl)
            return result
        elif type_case == "int64":
            check_field_type(
                field,
                descriptor.FieldDescriptor.TYPE_INT64,
                "google.protobuf.Int64Value",
            )
            result = FieldConstraintRules(self._env, self._funcs, field, fieldLvl)
            return result
        elif type_case == "sfixed32":
            check_field_type(field, descriptor.FieldDescriptor.TYPE_SFIXED32)
            result = FieldConstraintRules(self._env, self._funcs, field, fieldLvl)
            return result
        elif type_case == "sfixed64":
            check_field_type(field, descriptor.FieldDescriptor.TYPE_SFIXED64)
            result = FieldConstraintRules(self._env, self._funcs, field, fieldLvl)
            return result
        elif type_case == "sint32":
            check_field_type(field, descriptor.FieldDescriptor.TYPE_SINT32)
            result = FieldConstraintRules(self._env, self._funcs, field, fieldLvl)
            return result
        elif type_case == "sint64":
            check_field_type(field, descriptor.FieldDescriptor.TYPE_SINT64)
            result = FieldConstraintRules(self._env, self._funcs, field, fieldLvl)
            return result
        elif type_case == "uint32":
            check_field_type(
                field,
                descriptor.FieldDescriptor.TYPE_UINT32,
                "google.protobuf.UInt32Value",
            )
            result = FieldConstraintRules(self._env, self._funcs, field, fieldLvl)
            return result
        elif type_case == "uint64":
            check_field_type(
                field,
                descriptor.FieldDescriptor.TYPE_UINT64,
                "google.protobuf.UInt64Value",
            )
            result = FieldConstraintRules(self._env, self._funcs, field, fieldLvl)
            return result
        elif type_case == "string":
            check_field_type(
                field,
                descriptor.FieldDescriptor.TYPE_STRING,
                "google.protobuf.StringValue",
            )
            result = FieldConstraintRules(self._env, self._funcs, field, fieldLvl)
            return result
        elif type_case == "any":
            check_field_type(
                field, descriptor.FieldDescriptor.TYPE_MESSAGE, "google.protobuf.Any"
            )
            result = AnyConstraintRules(self._env, self._funcs, field, fieldLvl)
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
            return MapConstraintRules(
                self._env, self._funcs, field, rules, key_rules, value_rules
            )
        item_rule = None
        if rules.repeated.HasField("items"):
            item_rule = self._new_scalar_field_constraint(field, rules.repeated.items)
        return RepeatedConstraintRules(self._env, self._funcs, field, rules, item_rule)

    def _new_constraints(self, desc: descriptor.Descriptor) -> list[ConstraintRules]:
        result = []
        if validate_pb2.message in desc.GetOptions().Extensions:
            msgLvl = desc.GetOptions().Extensions[validate_pb2.message]
            if msgLvl.disabled:
                return []
            if constraint := self._new_message_constraint(msgLvl):
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
                if fieldLvl.skipped:
                    continue
                result.append(self._new_field_constraint(field, fieldLvl))
                if fieldLvl.repeated.items.skipped:
                    continue
            if field.message_type is None:
                continue
            if field.message_type.GetOptions().map_entry:
                value_field = field.message_type.fields_by_name["value"]
                if value_field.type != descriptor.FieldDescriptor.TYPE_MESSAGE:
                    continue
                result.append(MapValMsgConstraint(self, field, value_field))
            elif field.label == descriptor.FieldDescriptor.LABEL_REPEATED:
                result.append(RepeatedMsgConstraint(self, field))
            else:
                result.append(SubMsgConstraint(self, field))
        return result


class SubMsgConstraint:
    def __init__(
        self,
        factory: ConstraintFactory,
        field: descriptor.FieldDescriptor,
    ):
        self._factory = factory
        self._field = field

    def validate(self, ctx: ConstraintContext, message: message.Message):
        if not message.HasField(self._field.name):
            return
        constraints = self._factory.get(self._field.message_type)
        if constraints is None:
            return
        val = getattr(message, self._field.name)
        sub_ctx = ctx.sub_context()
        for constraint in constraints:
            constraint.validate(sub_ctx, val)
        if sub_ctx.has_errors():
            sub_ctx.add_path_prefix(self._field.name)
            ctx.add_errors(sub_ctx)


class MapValMsgConstraint:
    def __init__(
        self,
        factory: ConstraintFactory,
        field: descriptor.FieldDescriptor,
        value_field: descriptor.FieldDescriptor,
    ):
        self._factory = factory
        self._field = field
        self._value_field = value_field

    def validate(self, ctx: ConstraintContext, message: message.Message):
        val = getattr(message, self._field.name)
        if not val:
            return
        constraints = self._factory.get(self._value_field.message_type)
        if constraints is None:
            return
        for key, val in val.items():
            sub_ctx = ctx.sub_context()
            for constraint in constraints:
                constraint.validate(sub_ctx, val)
            if sub_ctx.has_errors():
                sub_ctx.add_path_prefix(f"{self._field.name}[{key}]")
                ctx.add_errors(sub_ctx)


class RepeatedMsgConstraint:
    def __init__(
        self,
        factory: ConstraintFactory,
        field: descriptor.FieldDescriptor,
    ):
        self._factory = factory
        self._field = field

    def validate(self, ctx: ConstraintContext, message: message.Message):
        val = getattr(message, self._field.name)
        if not val:
            return
        constraints = self._factory.get(self._field.message_type)
        if constraints is None:
            return
        for idx, val in enumerate(val):
            sub_ctx = ctx.sub_context()
            for constraint in constraints:
                constraint.validate(sub_ctx, val)
            if sub_ctx.has_errors():
                sub_ctx.add_path_prefix(f"{self._field.name}[{idx}]")
                ctx.add_errors(sub_ctx)
