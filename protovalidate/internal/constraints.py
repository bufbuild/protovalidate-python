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

import datetime
import typing

import celpy  # type: ignore
from celpy import celtypes  # type: ignore
from google.protobuf import any_pb2, descriptor, message, message_factory

from buf.validate import expression_pb2, validate_pb2  # type: ignore
from buf.validate.priv import private_pb2  # type: ignore
from protovalidate.internal import string_format
from protovalidate.internal.cel_field_presence import InterpretedRunner, in_has


class CompilationError(Exception):
    pass


def make_key_path(field_name: str, key: celtypes.Value) -> str:
    return f"{field_name}[{string_format.format_value(key)}]"


def make_duration(msg: message.Message) -> celtypes.DurationType:
    return celtypes.DurationType(
        seconds=msg.seconds,  # type: ignore
        nanos=msg.nanos,  # type: ignore
    )


def make_timestamp(msg: message.Message) -> celtypes.TimestampType:
    return make_duration(msg) + celtypes.TimestampType(1970, 1, 1)


def unwrap(msg: message.Message) -> celtypes.Value:
    return _field_to_cel(msg, msg.DESCRIPTOR.fields_by_name["value"])


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


class MessageType(celtypes.MapType):
    msg: message.Message
    desc: descriptor.Descriptor

    def __init__(self, msg: message.Message):
        super().__init__()
        self.msg = msg
        self.desc = msg.DESCRIPTOR
        field: descriptor.FieldDescriptor
        for field in self.desc.fields:
            if field.containing_oneof is not None and not self.msg.HasField(field.name):
                continue
            self[field.name] = _field_to_cel(self.msg, field)

    def __getitem__(self, name):
        field = self.desc.fields_by_name[name]
        if not in_has() and field.has_presence and not self.msg.HasField(name):
            return _zero_value(field)
        return super().__getitem__(name)


def _msg_to_cel(msg: message.Message) -> typing.Dict[str, celtypes.Value]:
    ctor = _MSG_TYPE_URL_TO_CTOR.get(msg.DESCRIPTOR.full_name)
    if ctor is not None:
        return ctor(msg)
    return MessageType(msg)


_TYPE_TO_CTOR = {
    descriptor.FieldDescriptor.TYPE_MESSAGE: _msg_to_cel,
    descriptor.FieldDescriptor.TYPE_GROUP: _msg_to_cel,
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


def _scalar_field_value_to_cel(val: typing.Any, field: descriptor.FieldDescriptor) -> celtypes.Value:
    ctor = _TYPE_TO_CTOR.get(field.type)
    if ctor is None:
        msg = "unknown field type"
        raise CompilationError(msg)
    return ctor(val)


def _field_value_to_cel(val: typing.Any, field: descriptor.FieldDescriptor) -> celtypes.Value:
    if field.label == descriptor.FieldDescriptor.LABEL_REPEATED:
        if field.message_type is not None and field.message_type.GetOptions().map_entry:
            return _map_field_value_to_cel(val, field)
        return _repeated_field_value_to_cel(val, field)
    return _scalar_field_value_to_cel(val, field)


def _is_empty_field(msg: message.Message, field: descriptor.FieldDescriptor) -> bool:
    if field.has_presence:  # type: ignore[attr-defined]
        return not msg.HasField(field.name)
    if field.label == descriptor.FieldDescriptor.LABEL_REPEATED:
        return len(getattr(msg, field.name)) == 0
    return getattr(msg, field.name) == field.default_value


def _repeated_field_to_cel(msg: message.Message, field: descriptor.FieldDescriptor) -> celtypes.Value:
    if field.message_type is not None and field.message_type.GetOptions().map_entry:
        return _map_field_to_cel(msg, field)
    return _repeated_field_value_to_cel(getattr(msg, field.name), field)


def _repeated_field_value_to_cel(val: typing.Any, field: descriptor.FieldDescriptor) -> celtypes.Value:
    result = celtypes.ListType()
    for item in val:
        result.append(_scalar_field_value_to_cel(item, field))
    return result


def _map_field_value_to_cel(mapping: typing.Any, field: descriptor.FieldDescriptor) -> celtypes.Value:
    result = celtypes.MapType()
    key_field = field.message_type.fields[0]
    val_field = field.message_type.fields[1]
    for key, val in mapping.items():
        result[_field_value_to_cel(key, key_field)] = _field_value_to_cel(val, val_field)
    return result


def _map_field_to_cel(msg: message.Message, field: descriptor.FieldDescriptor) -> celtypes.Value:
    return _map_field_value_to_cel(getattr(msg, field.name), field)


def _field_to_cel(msg: message.Message, field: descriptor.FieldDescriptor) -> celtypes.Value:
    if field.label == descriptor.FieldDescriptor.LABEL_REPEATED:
        return _repeated_field_to_cel(msg, field)
    elif field.message_type is not None and not msg.HasField(field.name):
        return None
    else:
        return _scalar_field_value_to_cel(getattr(msg, field.name), field)


class ConstraintContext:
    """The state associated with a single constraint evaluation."""

    def __init__(self, fail_fast: bool = False, violations: expression_pb2.Violations = None):  # noqa: FBT001, FBT002
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

    def add(self, field_name: str, constraint_id: str, message: str, *, for_key: bool = False):
        self._violations.violations.append(
            expression_pb2.Violation(
                field_path=field_name,
                constraint_id=constraint_id,
                message=message,
                for_key=for_key,
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
        return self._fail_fast and self.has_errors()

    def has_errors(self) -> bool:
        return len(self._violations.violations) > 0

    def sub_context(self):
        return ConstraintContext(self._fail_fast)


class ConstraintRules:
    """The constraints associated with a single 'rules' message."""

    def validate(self, ctx: ConstraintContext, message: message.Message):  # noqa: ARG002
        """Validate the message against the rules in this constraint."""
        ctx.add("", "unimplemented", "Unimplemented")


class CelConstraintRules(ConstraintRules):
    """A constraint that has rules written in CEL."""

    _runners: typing.List[typing.Tuple[celpy.Runner, typing.Union[expression_pb2.Constraint, private_pb2.Constraint]]]
    _rules_cel: celtypes.Value = None

    def __init__(self, rules: typing.Optional[message.Message]):
        self._runners = []
        if rules is not None:
            self._rules_cel = _msg_to_cel(rules)

    def _validate_cel(
        self,
        ctx: ConstraintContext,
        field_name: str,
        activation: typing.Dict[str, typing.Any],
        *,
        for_key: bool = False,
    ):
        activation["rules"] = self._rules_cel
        activation["now"] = celtypes.TimestampType(datetime.datetime.now(tz=datetime.timezone.utc))
        for runner, constraint in self._runners:
            result = runner.evaluate(activation)
            if isinstance(result, celtypes.BoolType):
                if not result:
                    ctx.add(field_name, constraint.id, constraint.message, for_key=for_key)
            elif isinstance(result, celtypes.StringType):
                if result:
                    ctx.add(field_name, constraint.id, result, for_key=for_key)
            elif isinstance(result, Exception):
                raise result

    def add_rule(
        self,
        env: celpy.Environment,
        funcs: typing.Dict[str, celpy.CELFunction],
        rules: typing.Union[expression_pb2.Constraint, private_pb2.Constraint],
    ):
        ast = env.compile(rules.expression)
        prog = env.program(ast, functions=funcs)
        self._runners.append((prog, rules))


class MessageConstraintRules(CelConstraintRules):
    """Message-level rules."""

    def validate(self, ctx: ConstraintContext, message: message.Message):
        self._validate_cel(ctx, "", {"this": _msg_to_cel(message)})


def check_field_type(field: descriptor.FieldDescriptor, expected: int, wrapper_name: typing.Optional[str] = None):
    if field.type != expected and (
        field.type != descriptor.FieldDescriptor.TYPE_MESSAGE or field.message_type.full_name != wrapper_name
    ):
        msg = f"field {field.name} has type {field.type} but expected {expected}"
        raise CompilationError(msg)


def _is_map(field: descriptor.FieldDescriptor):
    return (
        field.label == descriptor.FieldDescriptor.LABEL_REPEATED
        and field.message_type is not None
        and field.message_type.GetOptions().map_entry
    )


def _is_list(field: descriptor.FieldDescriptor):
    return field.label == descriptor.FieldDescriptor.LABEL_REPEATED and not _is_map(field)


def _zero_value(field: descriptor.FieldDescriptor):
    if field.message_type is not None and field.label != descriptor.FieldDescriptor.LABEL_REPEATED:
        return _field_value_to_cel(message_factory.GetMessageClass(field.message_type)(), field)
    else:
        return _field_value_to_cel(field.default_value, field)


class FieldConstraintRules(CelConstraintRules):
    """Field-level rules."""

    _ignore_empty = False
    _ignore_default = False
    _required = False
    _zero = None

    def __init__(
        self,
        env: celpy.Environment,
        funcs: typing.Dict[str, celpy.CELFunction],
        field: descriptor.FieldDescriptor,
        field_level: validate_pb2.FieldConstraints,
        *,
        for_items: bool = False,
    ):
        type_case = field_level.WhichOneof("type")
        super().__init__(None if type_case is None else getattr(field_level, type_case))
        self._field = field
        self._ignore_empty = (
            field_level.ignore_empty
            or field_level.ignore in (validate_pb2.IGNORE_IF_UNPOPULATED, validate_pb2.IGNORE_IF_DEFAULT_VALUE)
            or field.has_presence  # type: ignore[attr-defined]
            and not for_items
        )
        self._ignore_default = field.has_presence and field_level.ignore == validate_pb2.IGNORE_IF_DEFAULT_VALUE  # type: ignore[attr-defined]
        self._required = field_level.required
        if self._ignore_default:
            self._zero = _zero_value(field)
        type_case = field_level.WhichOneof("type")
        if type_case is not None:
            rules = getattr(field_level, type_case)
            # For each set field in the message, look for the private constraint
            # extension.
            for list_field, _ in rules.ListFields():
                if private_pb2.field in list_field.GetOptions().Extensions:
                    for cel in list_field.GetOptions().Extensions[private_pb2.field].cel:
                        self.add_rule(env, funcs, cel)
        for cel in field_level.cel:
            self.add_rule(env, funcs, cel)

    def validate(self, ctx: ConstraintContext, message: message.Message):
        if _is_empty_field(message, self._field):
            if self._required:
                ctx.add(
                    self._field.name,
                    "required",
                    "value is required",
                )
                return
            if self._ignore_empty:
                return
        val = getattr(message, self._field.name)
        cel_val = _field_value_to_cel(val, self._field)
        if self._ignore_default and cel_val == self._zero:
            return
        self._validate_value(ctx, self._field.name, val)
        self._validate_cel(ctx, self._field.name, {"this": cel_val})

    def validate_item(self, ctx: ConstraintContext, field_path: str, val: typing.Any, *, for_key: bool = False):
        self._validate_value(ctx, field_path, val, for_key=for_key)
        self._validate_cel(ctx, field_path, {"this": _scalar_field_value_to_cel(val, self._field)}, for_key=for_key)

    def _validate_value(self, ctx: ConstraintContext, field_path: str, val: typing.Any, *, for_key: bool = False):
        pass


class AnyConstraintRules(FieldConstraintRules):
    """Rules for an Any field."""

    _in: typing.List[str] = []  # noqa: RUF012
    _not_in: typing.List[str] = []  # noqa: RUF012

    def __init__(
        self,
        env: celpy.Environment,
        funcs: typing.Dict[str, celpy.CELFunction],
        field: descriptor.FieldDescriptor,
        field_level: validate_pb2.FieldConstraints,
    ):
        super().__init__(env, funcs, field, field_level)
        if getattr(field_level.any, "in"):
            self._in = getattr(field_level.any, "in")
        if field_level.any.not_in:
            self._not_in = field_level.any.not_in

    def _validate_value(self, ctx: ConstraintContext, field_path: str, value: any_pb2.Any, *, for_key: bool = False):
        if len(self._in) > 0:
            if value.type_url not in self._in:
                ctx.add(
                    field_path,
                    "any.in",
                    "type URL must be in the allow list",
                    for_key=for_key,
                )
        if value.type_url in self._not_in:
            ctx.add(
                field_path,
                "any.not_in",
                "type URL must not be in the block list",
                for_key=for_key,
            )


class EnumConstraintRules(FieldConstraintRules):
    """Rules for an enum field."""

    _defined_only = False

    def __init__(
        self,
        env: celpy.Environment,
        funcs: typing.Dict[str, celpy.CELFunction],
        field: descriptor.FieldDescriptor,
        field_level: validate_pb2.FieldConstraints,
        *,
        for_items: bool = False,
    ):
        super().__init__(env, funcs, field, field_level, for_items=for_items)
        if field_level.enum.defined_only:
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

    _item_rules: typing.Optional[FieldConstraintRules] = None

    def __init__(
        self,
        env: celpy.Environment,
        funcs: typing.Dict[str, celpy.CELFunction],
        field: descriptor.FieldDescriptor,
        field_level: validate_pb2.FieldConstraints,
        item_rules: typing.Optional[FieldConstraintRules],
    ):
        super().__init__(env, funcs, field, field_level)
        if item_rules is not None:
            self._item_rules = item_rules

    def validate(self, ctx: ConstraintContext, message: message.Message):
        super().validate(ctx, message)
        if ctx.done:
            return
        value = getattr(message, self._field.name)
        if self._item_rules is not None:
            for i, item in enumerate(value):
                if self._item_rules._ignore_empty and not item:
                    continue
                sub_ctx = ctx.sub_context()
                self._item_rules.validate_item(sub_ctx, "", item)
                if sub_ctx.has_errors():
                    sub_ctx.add_path_prefix(f"{self._field.name}[{i}]", "")
                    ctx.add_errors(sub_ctx)
                if ctx.done:
                    return


class MapConstraintRules(FieldConstraintRules):
    """Rules for a map field."""

    _key_rules: typing.Optional[FieldConstraintRules] = None
    _value_rules: typing.Optional[FieldConstraintRules] = None

    def __init__(
        self,
        env: celpy.Environment,
        funcs: typing.Dict[str, celpy.CELFunction],
        field: descriptor.FieldDescriptor,
        field_level: validate_pb2.FieldConstraints,
        key_rules: typing.Optional[FieldConstraintRules],
        value_rules: typing.Optional[FieldConstraintRules],
    ):
        super().__init__(env, funcs, field, field_level)
        if key_rules is not None:
            self._key_rules = key_rules
        if value_rules is not None:
            self._value_rules = value_rules

    def validate(self, ctx: ConstraintContext, message: message.Message):
        super().validate(ctx, message)
        if ctx.done:
            return
        value = getattr(message, self._field.name)
        for k, v in value.items():
            key_field_path = make_key_path(self._field.name, k)
            if self._key_rules is not None:
                if not self._key_rules._ignore_empty or k:
                    self._key_rules.validate_item(ctx, key_field_path, k, for_key=True)
            if self._value_rules is not None:
                if not self._value_rules._ignore_empty or v:
                    self._value_rules.validate_item(ctx, key_field_path, v)


class OneofConstraintRules(ConstraintRules):
    """Rules for a oneof definition."""

    required = True

    def __init__(self, oneof: descriptor.OneofDescriptor, rules: validate_pb2.OneofConstraints):
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
    _funcs: typing.Dict[str, celpy.CELFunction]
    _cache: typing.Dict[descriptor.Descriptor, typing.Union[typing.List[ConstraintRules], Exception]]

    def __init__(self, funcs: typing.Dict[str, celpy.CELFunction]):
        self._env = celpy.Environment(runner_class=InterpretedRunner)
        self._funcs = funcs
        self._cache = {}

    def get(self, descriptor: descriptor.Descriptor) -> typing.List[ConstraintRules]:
        if descriptor not in self._cache:
            try:
                self._cache[descriptor] = self._new_constraints(descriptor)
            except Exception as e:
                self._cache[descriptor] = e
        result = self._cache[descriptor]
        if isinstance(result, Exception):
            raise result
        return result

    def _new_message_constraint(self, rules: validate_pb2.message) -> MessageConstraintRules:
        result = MessageConstraintRules(rules)
        for cel in rules.cel:
            result.add_rule(self._env, self._funcs, cel)
        return result

    def _new_scalar_field_constraint(
        self,
        field: descriptor.FieldDescriptor,
        field_level: validate_pb2.field,
        *,
        for_items: bool = False,
    ):
        if field_level.ignore == validate_pb2.IGNORE_ALWAYS or field_level.skipped:
            return None
        type_case = field_level.WhichOneof("type")
        if type_case is None:
            result = FieldConstraintRules(self._env, self._funcs, field, field_level, for_items=for_items)
            return result
        elif type_case == "duration":
            check_field_type(field, 0, "google.protobuf.Duration")
            result = FieldConstraintRules(self._env, self._funcs, field, field_level, for_items=for_items)
            return result
        elif type_case == "timestamp":
            check_field_type(field, 0, "google.protobuf.Timestamp")
            result = FieldConstraintRules(self._env, self._funcs, field, field_level, for_items=for_items)
            return result
        elif type_case == "enum":
            check_field_type(field, descriptor.FieldDescriptor.TYPE_ENUM)
            result = EnumConstraintRules(self._env, self._funcs, field, field_level, for_items=for_items)
            return result
        elif type_case == "bool":
            check_field_type(field, descriptor.FieldDescriptor.TYPE_BOOL, "google.protobuf.BoolValue")
            result = FieldConstraintRules(self._env, self._funcs, field, field_level, for_items=for_items)
            return result
        elif type_case == "bytes":
            check_field_type(
                field,
                descriptor.FieldDescriptor.TYPE_BYTES,
                "google.protobuf.BytesValue",
            )
            result = FieldConstraintRules(self._env, self._funcs, field, field_level, for_items=for_items)
            return result
        elif type_case == "fixed32":
            check_field_type(field, descriptor.FieldDescriptor.TYPE_FIXED32)
            result = FieldConstraintRules(self._env, self._funcs, field, field_level, for_items=for_items)
            return result
        elif type_case == "fixed64":
            check_field_type(field, descriptor.FieldDescriptor.TYPE_FIXED64)
            result = FieldConstraintRules(self._env, self._funcs, field, field_level, for_items=for_items)
            return result
        elif type_case == "float":
            check_field_type(
                field,
                descriptor.FieldDescriptor.TYPE_FLOAT,
                "google.protobuf.FloatValue",
            )
            result = FieldConstraintRules(self._env, self._funcs, field, field_level, for_items=for_items)
            return result
        elif type_case == "double":
            check_field_type(
                field,
                descriptor.FieldDescriptor.TYPE_DOUBLE,
                "google.protobuf.DoubleValue",
            )
            result = FieldConstraintRules(self._env, self._funcs, field, field_level, for_items=for_items)
            return result
        elif type_case == "int32":
            check_field_type(
                field,
                descriptor.FieldDescriptor.TYPE_INT32,
                "google.protobuf.Int32Value",
            )
            result = FieldConstraintRules(self._env, self._funcs, field, field_level, for_items=for_items)
            return result
        elif type_case == "int64":
            check_field_type(
                field,
                descriptor.FieldDescriptor.TYPE_INT64,
                "google.protobuf.Int64Value",
            )
            result = FieldConstraintRules(self._env, self._funcs, field, field_level, for_items=for_items)
            return result
        elif type_case == "sfixed32":
            check_field_type(field, descriptor.FieldDescriptor.TYPE_SFIXED32)
            result = FieldConstraintRules(self._env, self._funcs, field, field_level, for_items=for_items)
            return result
        elif type_case == "sfixed64":
            check_field_type(field, descriptor.FieldDescriptor.TYPE_SFIXED64)
            result = FieldConstraintRules(self._env, self._funcs, field, field_level, for_items=for_items)
            return result
        elif type_case == "sint32":
            check_field_type(field, descriptor.FieldDescriptor.TYPE_SINT32)
            result = FieldConstraintRules(self._env, self._funcs, field, field_level, for_items=for_items)
            return result
        elif type_case == "sint64":
            check_field_type(field, descriptor.FieldDescriptor.TYPE_SINT64)
            result = FieldConstraintRules(self._env, self._funcs, field, field_level, for_items=for_items)
            return result
        elif type_case == "uint32":
            check_field_type(
                field,
                descriptor.FieldDescriptor.TYPE_UINT32,
                "google.protobuf.UInt32Value",
            )
            result = FieldConstraintRules(self._env, self._funcs, field, field_level, for_items=for_items)
            return result
        elif type_case == "uint64":
            check_field_type(
                field,
                descriptor.FieldDescriptor.TYPE_UINT64,
                "google.protobuf.UInt64Value",
            )
            result = FieldConstraintRules(self._env, self._funcs, field, field_level, for_items=for_items)
            return result
        elif type_case == "string":
            check_field_type(
                field,
                descriptor.FieldDescriptor.TYPE_STRING,
                "google.protobuf.StringValue",
            )
            result = FieldConstraintRules(self._env, self._funcs, field, field_level, for_items=for_items)
            return result
        elif type_case == "any":
            check_field_type(field, descriptor.FieldDescriptor.TYPE_MESSAGE, "google.protobuf.Any")
            result = AnyConstraintRules(self._env, self._funcs, field, field_level)
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
                key_rules = self._new_scalar_field_constraint(key_field, rules.map.keys, for_items=True)
            value_rules = None
            if rules.map.HasField("values"):
                value_field = field.message_type.fields_by_name["value"]
                value_rules = self._new_scalar_field_constraint(value_field, rules.map.values, for_items=True)
            return MapConstraintRules(self._env, self._funcs, field, rules, key_rules, value_rules)
        item_rule = None
        if rules.repeated.HasField("items"):
            item_rule = self._new_scalar_field_constraint(field, rules.repeated.items)
        return RepeatedConstraintRules(self._env, self._funcs, field, rules, item_rule)

    def _new_constraints(self, desc: descriptor.Descriptor) -> typing.List[ConstraintRules]:
        result: typing.List[ConstraintRules] = []
        constraint: typing.Optional[ConstraintRules] = None
        if validate_pb2.message in desc.GetOptions().Extensions:
            message_level = desc.GetOptions().Extensions[validate_pb2.message]
            if message_level.disabled:
                return []
            if constraint := self._new_message_constraint(message_level):
                result.append(constraint)

        for oneof in desc.oneofs:
            if validate_pb2.oneof in oneof.GetOptions().Extensions:
                if constraint := OneofConstraintRules(oneof, oneof.GetOptions().Extensions[validate_pb2.oneof]):
                    result.append(constraint)

        for field in desc.fields:
            if validate_pb2.field in field.GetOptions().Extensions:
                field_level = field.GetOptions().Extensions[validate_pb2.field]
                if field_level.ignore == validate_pb2.IGNORE_ALWAYS or field_level.skipped:
                    continue
                result.append(self._new_field_constraint(field, field_level))
                if (
                    field_level.repeated.items.ignore == validate_pb2.IGNORE_ALWAYS
                    or field_level.repeated.items.skipped
                ):
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


class SubMsgConstraint(ConstraintRules):
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


class MapValMsgConstraint(ConstraintRules):
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
        for k, v in val.items():
            sub_ctx = ctx.sub_context()
            for constraint in constraints:
                constraint.validate(sub_ctx, v)
            if sub_ctx.has_errors():
                sub_ctx.add_path_prefix(f"{self._field.name}[{k}]")
                ctx.add_errors(sub_ctx)


class RepeatedMsgConstraint(ConstraintRules):
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
        for idx, item in enumerate(val):
            sub_ctx = ctx.sub_context()
            for constraint in constraints:
                constraint.validate(sub_ctx, item)
            if sub_ctx.has_errors():
                sub_ctx.add_path_prefix(f"{self._field.name}[{idx}]")
                ctx.add_errors(sub_ctx)
