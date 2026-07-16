# Copyright (c) 2025-2026 Buf Technologies, Inc.
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

import abc
import dataclasses
import datetime
import typing
from collections.abc import Callable, Iterable

import celpy
from celpy import celtypes
from protobuf import (
    DescEnum,
    DescExtension,
    DescField,
    DescFieldValue,
    DescFieldValueEnum,
    DescFieldValueList,
    DescFieldValueMap,
    DescFieldValueMessage,
    DescFieldValueScalar,
    DescMessage,
    DescOneof,
    Extension,
    Message,
    Oneof,
    Registry,
    ScalarType,
)
from protobuf.wkt import Duration, FieldDescriptorProto, Timestamp

from protovalidate._gen.buf.validate import validate_pb
from protovalidate.internal.cel_field_presence import InterpretedRunner, in_has


class CompilationError(Exception):
    pass


_TYPE_CTORS: dict[ScalarType, Callable[..., celtypes.Value]] = {
    ScalarType.BOOL: celtypes.BoolType,
    ScalarType.BYTES: celtypes.BytesType,
    ScalarType.STRING: celtypes.StringType,
    ScalarType.FLOAT: celtypes.DoubleType,
    ScalarType.DOUBLE: celtypes.DoubleType,
    ScalarType.INT32: celtypes.IntType,
    ScalarType.INT64: celtypes.IntType,
    ScalarType.SINT32: celtypes.IntType,
    ScalarType.SINT64: celtypes.IntType,
    ScalarType.SFIXED32: celtypes.IntType,
    ScalarType.SFIXED64: celtypes.IntType,
    ScalarType.UINT32: celtypes.UintType,
    ScalarType.UINT64: celtypes.UintType,
    ScalarType.FIXED32: celtypes.UintType,
    ScalarType.FIXED64: celtypes.UintType,
}


def _scalar_zero(scalar: ScalarType) -> str | bytes | bool | float | int:
    match scalar:
        case ScalarType.STRING:
            return ""
        case ScalarType.BYTES:
            return b""
        case ScalarType.BOOL:
            return False
        case ScalarType.DOUBLE | ScalarType.FLOAT:
            return 0.0
        case _:
            return 0


def _wire_type(field: DescField | DescExtension | ScalarType | DescMessage | DescEnum) -> FieldDescriptorProto.Type:
    """The FieldDescriptorProto.Type for a field path element, reported in validation messages."""
    match field:
        case ScalarType():
            return FieldDescriptorProto.Type(int(field))
        case DescMessage():
            return FieldDescriptorProto.Type.MESSAGE
        case DescEnum():
            return FieldDescriptorProto.Type.ENUM
        case _:
            match field.value:
                case DescFieldValueMessage(delimited_encoding=True) | DescFieldValueList(delimited_encoding=True):
                    return FieldDescriptorProto.Type.GROUP
                case _:
                    return field.proto.type


def _path_name(field: DescField | DescExtension) -> str:
    """The field name for a path element. Extensions are bracketed."""
    return f"[{field.type_name}]" if isinstance(field, DescExtension) else field.name


def _read_key(field: DescField | DescExtension) -> DescField | Extension:
    return field.type if isinstance(field, DescExtension) else field


def _scalar_of(subject: DescField | ScalarType | DescMessage | DescEnum) -> ScalarType | None:
    match subject:
        case ScalarType():
            return subject
        case DescField(value=DescFieldValueScalar(scalar=scalar)):
            return scalar
        case _:
            return None


def _message_of(subject: DescField | ScalarType | DescMessage | DescEnum) -> DescMessage | None:
    match subject:
        case DescMessage():
            return subject
        case DescField(value=DescFieldValueMessage(message=message)):
            return message
        case _:
            return None


def _enum_of(subject: DescField | ScalarType | DescMessage | DescEnum) -> DescEnum | None:
    match subject:
        case DescEnum():
            return subject
        case DescField(value=DescFieldValueEnum(enum=enum)):
            return enum
        case _:
            return None


def make_duration(msg: Duration) -> celtypes.DurationType:
    return celtypes.DurationType(seconds=msg.seconds, nanos=msg.nanos)


def make_timestamp(msg: Timestamp) -> celtypes.TimestampType:
    return celtypes.TimestampType(1970, 1, 1) + celtypes.DurationType(seconds=msg.seconds, nanos=msg.nanos)


class MessageConverter:
    """Converts protobuf-py values into celpy celtypes for CEL evaluation."""

    def __init__(self):
        self._fields_by_name: dict[DescMessage, dict[str, DescField]] = {}
        # Well-known types convert to native CEL values rather than maps.
        self._wkt: dict[str, Callable[..., celtypes.Value]] = {
            "google.protobuf.Duration": make_duration,
            "google.protobuf.Timestamp": make_timestamp,
            "google.protobuf.StringValue": self._unwrap,
            "google.protobuf.BytesValue": self._unwrap,
            "google.protobuf.Int32Value": self._unwrap,
            "google.protobuf.Int64Value": self._unwrap,
            "google.protobuf.UInt32Value": self._unwrap,
            "google.protobuf.UInt64Value": self._unwrap,
            "google.protobuf.FloatValue": self._unwrap,
            "google.protobuf.DoubleValue": self._unwrap,
            "google.protobuf.BoolValue": self._unwrap,
        }

    def fields_by_name(self, desc: DescMessage) -> dict[str, DescField]:
        fields = self._fields_by_name.get(desc)
        if fields is None:
            fields = {field.name: field for field in desc.fields}
            self._fields_by_name[desc] = fields
        return fields

    def message(self, msg: Message) -> celtypes.Value:
        wkt_ctor = self._wkt.get(type(msg).desc().type_name)
        if wkt_ctor is not None:
            return wkt_ctor(msg)
        return MessageType(msg, self)

    def field(self, msg: Message, field: DescField | DescExtension) -> celtypes.Value:
        key = _read_key(field)
        if isinstance(field.value, DescFieldValueMessage) and key not in msg:
            return None
        return self.field_value(msg[key], field.value)

    def field_value(self, val: typing.Any, kind: DescFieldValue) -> celtypes.Value:
        match kind:
            case DescFieldValueMap(key=key_kind, value=value_kind):
                result = celtypes.MapType()
                for k, v in val.items():
                    result[self.scalar(k, key_kind)] = self.scalar(v, value_kind)
                return result
            case DescFieldValueList(element=element):
                return celtypes.ListType(self.scalar(item, element) for item in val)
            case DescFieldValueMessage():
                return self.message(val)
            case DescFieldValueEnum():
                return celtypes.IntType(int(val))
            case DescFieldValueScalar(scalar=scalar):
                return self.scalar(val, scalar)

    def scalar(self, val: typing.Any, kind: ScalarType | DescMessage | DescEnum) -> celtypes.Value:
        match kind:
            case DescMessage():
                return self.message(val)
            case DescEnum():
                return celtypes.IntType(int(val))
            case ScalarType():
                ctor = _TYPE_CTORS.get(kind)
                if ctor is None:
                    msg = "unknown field type"
                    raise CompilationError(msg)
                return ctor(val)

    def zero(self, field: DescField) -> celtypes.Value:
        match field.value:
            case DescFieldValueMap():
                return celtypes.MapType()
            case DescFieldValueList():
                return celtypes.ListType()
            case DescFieldValueMessage(message=message):
                return self.message(message.type())
            case DescFieldValueEnum():
                return celtypes.IntType(0)
            case DescFieldValueScalar(scalar=scalar):
                return self.scalar(_scalar_zero(scalar), scalar)

    def _unwrap(self, msg: Message) -> celtypes.Value:
        return self.field(msg, self.fields_by_name(type(msg).desc())["value"])


class MessageType(celtypes.MapType):
    """A protobuf-py message wrapped as a celpy map for CEL evaluation."""

    msg: Message

    def __init__(self, msg: Message, conv: MessageConverter):
        super().__init__()
        self.msg = msg
        self._conv = conv
        self._fields = conv.fields_by_name(type(msg).desc())
        for field in msg:
            self[celtypes.StringType(field.name)] = conv.field(msg, field)

    def get_field(self, name: str) -> DescField | None:
        return self._fields.get(name)

    def convert_field(self, field: DescField) -> celtypes.Value:
        """Convert one of this message's fields to its CEL value."""
        return self._conv.field(self.msg, field)

    def __getitem__(self, key):
        field = self._fields[key]
        if field not in self.msg:
            if in_has():
                raise KeyError
            return self._conv.zero(field)
        return super().__getitem__(key)


def _field_to_element(field: DescField | DescExtension) -> validate_pb.FieldPathElement:
    return validate_pb.FieldPathElement(
        field_number=field.number,
        field_name=_path_name(field),
        field_type=_wire_type(field),
    )


def _indexed_field_element(field: DescField, index: int) -> validate_pb.FieldPathElement:
    return validate_pb.FieldPathElement(
        field_number=field.number,
        field_name=field.name,
        field_type=_wire_type(field),
        subscript=Oneof(field="index", value=index),
    )


def _oneof_to_element(oneof: DescOneof) -> validate_pb.FieldPathElement:
    return validate_pb.FieldPathElement(field_name=oneof.name)


def _map_key_element(field: DescField, key: typing.Any) -> validate_pb.FieldPathElement:
    value = field.value
    assert isinstance(value, DescFieldValueMap)  # noqa: S101
    subscript: Oneof
    match value.key:
        case ScalarType.BOOL:
            subscript = Oneof(field="bool_key", value=key)
        case (
            ScalarType.INT32
            | ScalarType.SFIXED32
            | ScalarType.INT64
            | ScalarType.SFIXED64
            | ScalarType.SINT32
            | ScalarType.SINT64
        ):
            subscript = Oneof(field="int_key", value=key)
        case ScalarType.UINT32 | ScalarType.FIXED32 | ScalarType.UINT64 | ScalarType.FIXED64:
            subscript = Oneof(field="uint_key", value=key)
        case ScalarType.STRING:
            subscript = Oneof(field="string_key", value=key)
        case _:
            msg = "unexpected map type"
            raise CompilationError(msg)
    return validate_pb.FieldPathElement(
        field_number=field.number,
        field_name=field.name,
        field_type=_wire_type(field),
        key_type=_wire_type(value.key),
        value_type=_wire_type(value.value),
        subscript=subscript,
    )


def _spec_field(rules_cls: type[Message], name: str) -> DescField:
    return next(f for f in rules_cls.desc().fields if f.name == name)


def _which_type(field_level: validate_pb.FieldRules) -> str | None:
    return field_level.type.field if field_level.type is not None else None


class Violation:
    """A singular rule violation."""

    field_value: typing.Any
    rule_value: typing.Any

    def __init__(
        self,
        *,
        field_value: typing.Any = None,
        rule_value: typing.Any = None,
        field: validate_pb.FieldPath | None = None,
        rule: validate_pb.FieldPath | None = None,
        rule_id: str = "",
        message: str = "",
        for_key: bool = False,
    ):
        self.field_value = field_value
        self.rule_value = rule_value
        self._field_elements: list[validate_pb.FieldPathElement] = list(field.elements) if field is not None else []
        self._rule_elements: list[validate_pb.FieldPathElement] = list(rule.elements) if rule is not None else []
        self._rule_id = rule_id
        self._message = message
        self._for_key = for_key

    @property
    def proto(self) -> validate_pb.Violation:
        kwargs: dict[str, typing.Any] = {
            "rule_id": self._rule_id,
            "message": self._message,
            "for_key": self._for_key,
        }
        if self._field_elements:
            kwargs["field"] = validate_pb.FieldPath(elements=list(self._field_elements))
        if self._rule_elements:
            kwargs["rule"] = validate_pb.FieldPath(elements=list(self._rule_elements))
        return validate_pb.Violation(**kwargs)

    def _finalize_paths(self) -> None:
        self._field_elements.reverse()
        self._rule_elements.reverse()

    def _append_field_element(self, element: validate_pb.FieldPathElement) -> None:
        self._field_elements.append(element)

    def _extend_rule_elements(self, elements: list[validate_pb.FieldPathElement]) -> None:
        self._rule_elements.extend(elements)


class RuleContext:
    """The state associated with a single rule evaluation."""

    _violations: list[Violation]

    def __init__(self, *, fail_fast: bool = False):
        self._fail_fast = fail_fast
        self._violations = []

    @property
    def violations(self) -> list[Violation]:
        return self._violations

    def add(self, violation: Violation):
        self._violations.append(violation)

    def add_errors(self, other_ctx: "RuleContext"):
        self._violations.extend(other_ctx.violations)

    def add_field_path_element(self, element: validate_pb.FieldPathElement):
        for violation in self._violations:
            violation._append_field_element(element)

    def add_rule_path_elements(self, elements: list[validate_pb.FieldPathElement]):
        for violation in self._violations:
            violation._extend_rule_elements(elements)

    @property
    def done(self) -> bool:
        return self._fail_fast and self.has_errors()

    def has_errors(self) -> bool:
        return len(self._violations) > 0

    def sub_context(self) -> "RuleContext":
        return RuleContext(fail_fast=self._fail_fast)


class Rules(abc.ABC):
    """The rules associated with a single 'rules' message."""

    @abc.abstractmethod
    def validate(self, ctx: RuleContext, message: Message) -> None:
        """Validate the message against the rules in this rule."""
        ...


@dataclasses.dataclass
class CelRunner:
    runner: celpy.Runner
    rule: validate_pb.Rule
    rule_value: typing.Any | None = None
    rule_cel: celtypes.Value | None = None
    rule_path: validate_pb.FieldPath | None = None


class CelRules(Rules):
    """A rule that has rules written in CEL."""

    _cel: list[CelRunner]
    _rules: Message | None = None
    _rules_cel: celtypes.Value | None = None
    _uses_now: bool = False

    def __init__(
        self,
        rules: Message | None,
        *,
        env: celpy.Environment,
        funcs: dict[str, celpy.CELFunction],
        conv: MessageConverter,
    ):
        self._env = env
        self._funcs = funcs
        self._conv = conv
        self._cel = []
        if rules is not None:
            self._rules = rules
            self._rules_cel = conv.message(rules)

    def _validate_cel(
        self,
        ctx: RuleContext,
        *,
        this_value: typing.Any | None = None,
        this_cel: celtypes.Value | None = None,
        for_key: bool = False,
    ):
        if not self._cel:
            return
        activation: dict[str, celtypes.Value] = {}
        if this_cel is not None:
            activation["this"] = this_cel
        activation["rules"] = self._rules_cel
        if self._uses_now:
            activation["now"] = celtypes.TimestampType(datetime.datetime.now(tz=datetime.timezone.utc))
        for cel in self._cel:
            activation["rule"] = cel.rule_cel
            result = cel.runner.evaluate(activation)
            match result:
                case celtypes.BoolType() if not result:
                    message = cel.rule.message
                    if len(message) == 0:
                        message = f'"{cel.rule.expression}" returned false'
                    ctx.add(
                        Violation(
                            field_value=this_value,
                            rule=cel.rule_path,
                            rule_value=cel.rule_value,
                            rule_id=cel.rule.id,
                            message=message,
                            for_key=for_key,
                        ),
                    )
                case celtypes.StringType() if result:
                    ctx.add(
                        Violation(
                            field_value=this_value,
                            rule=cel.rule_path,
                            rule_value=cel.rule_value,
                            rule_id=cel.rule.id,
                            message=result,
                            for_key=for_key,
                        ),
                    )
                case Exception():
                    raise result

    def add_rule(
        self,
        rules: validate_pb.Rule | str,
        *,
        rule_field: DescField | DescExtension | None = None,
        rule_path: validate_pb.FieldPath | None = None,
    ):
        if isinstance(rules, str):
            expression = rules
            rules = validate_pb.Rule(id=expression, expression=expression)
        if "now" in rules.expression:
            self._uses_now = True
        ast = self._env.compile(rules.expression)
        prog = self._env.program(ast, functions=self._funcs)
        rule_value = None
        rule_cel = None
        if rule_field is not None and self._rules is not None:
            rule_value = self._rules[_read_key(rule_field)]
            rule_cel = self._conv.field(self._rules, rule_field)
        self._cel.append(
            CelRunner(
                runner=prog,
                rule=rules,
                rule_value=rule_value,
                rule_cel=rule_cel,
                rule_path=rule_path,
            )
        )


class MessageOneofRule(Rules):
    """Validates a single buf.validate.MessageOneofRule given via the (buf.validate.message).oneof option."""

    def __init__(self, fields: list[DescField], *, required: bool):
        self._fields = fields
        self._required = required

    def validate(self, ctx: RuleContext, message: Message):
        num_set_fields = sum(1 for field in self._fields if field in message)
        if num_set_fields > 1:
            ctx.add(
                Violation(
                    rule_id="message.oneof",
                    message=f"only one of {', '.join(field.name for field in self._fields)} can be set",
                )
            )
        if self._required and num_set_fields == 0:
            ctx.add(
                Violation(
                    rule_id="message.oneof",
                    message=f"one of {', '.join(field.name for field in self._fields)} must be set",
                )
            )


class MessageRules(CelRules):
    """Message-level rules."""

    _oneofs: list[MessageOneofRule]

    def __init__(
        self,
        rules: Message | None,
        desc: DescMessage,
        *,
        env: celpy.Environment,
        funcs: dict[str, celpy.CELFunction],
        conv: MessageConverter,
    ):
        super().__init__(rules, env=env, funcs=funcs, conv=conv)
        self._oneofs = []
        self._desc = desc

    def validate(self, ctx: RuleContext, message: Message):
        if self._cel:
            self._validate_cel(ctx, this_cel=self._conv.message(message))
            if ctx.done:
                return
        for oneof in self._oneofs:
            oneof.validate(ctx, message)
            if ctx.done:
                return

    def add_oneof(self, rule: validate_pb.MessageOneofRule):
        fields = []
        seen = set()
        if len(rule.fields) == 0:
            msg = f"at least one field must be specified in oneof rule for the message {self._desc.type_name}"
            raise CompilationError(msg)
        desc_fields = {f.name: f for f in self._desc.fields}
        for name in rule.fields:
            if name in desc_fields:
                if name in seen:
                    msg = f"duplicate {name} in oneof rule for the message {self._desc.type_name}"
                    raise CompilationError(msg)
                fields.append(desc_fields[name])
                seen.add(name)
            else:
                msg = f'field "{name}" not found in message {self._desc.type_name}'
                raise CompilationError(msg)
        self._oneofs.append(MessageOneofRule(fields, required=rule.required))


# For each scalar FieldRules.type case: the scalar the field must be, and the
# well-known wrapper message it may be instead. A None scalar means the field
# must be the wrapper message (no scalar form).
_RULE_FIELD_TYPES: dict[str, tuple[ScalarType | None, str | None]] = {
    "duration": (None, "google.protobuf.Duration"),
    "field_mask": (None, "google.protobuf.FieldMask"),
    "timestamp": (None, "google.protobuf.Timestamp"),
    "bool": (ScalarType.BOOL, "google.protobuf.BoolValue"),
    "bytes": (ScalarType.BYTES, "google.protobuf.BytesValue"),
    "fixed32": (ScalarType.FIXED32, None),
    "fixed64": (ScalarType.FIXED64, None),
    "float": (ScalarType.FLOAT, "google.protobuf.FloatValue"),
    "double": (ScalarType.DOUBLE, "google.protobuf.DoubleValue"),
    "int32": (ScalarType.INT32, "google.protobuf.Int32Value"),
    "int64": (ScalarType.INT64, "google.protobuf.Int64Value"),
    "sfixed32": (ScalarType.SFIXED32, None),
    "sfixed64": (ScalarType.SFIXED64, None),
    "sint32": (ScalarType.SINT32, None),
    "sint64": (ScalarType.SINT64, None),
    "uint32": (ScalarType.UINT32, "google.protobuf.UInt32Value"),
    "uint64": (ScalarType.UINT64, "google.protobuf.UInt64Value"),
    "string": (ScalarType.STRING, "google.protobuf.StringValue"),
}


def _type_mismatch(subject: DescField | ScalarType | DescMessage | DescEnum, expected: str) -> CompilationError:
    actual = _wire_type(subject).name.lower()
    name = subject.name if isinstance(subject, DescField) else actual
    return CompilationError(f"field {name} has type {actual} but expected {expected}")


def _check_field_type(
    subject: DescField | ScalarType | DescMessage | DescEnum,
    expected: ScalarType | None,
    wrapper_name: str | None = None,
) -> None:
    if (expected is not None and _scalar_of(subject) == expected) or (
        (message := _message_of(subject)) is not None and message.type_name == wrapper_name
    ):
        return
    raise _type_mismatch(subject, (wrapper_name or "message") if expected is None else expected.name.lower())


class FieldRules(CelRules):
    """Field-level rules."""

    _ignore_empty = False
    _required = False

    _required_rule_path: typing.ClassVar[validate_pb.FieldPath] = validate_pb.FieldPath(
        elements=[_field_to_element(_spec_field(validate_pb.FieldRules, "required"))]
    )

    def __init__(
        self,
        env: celpy.Environment,
        funcs: dict[str, celpy.CELFunction],
        field: DescField | ScalarType | DescMessage | DescEnum,
        field_level: validate_pb.FieldRules,
        *,
        for_items: bool = False,
        force_ignore_empty: bool = False,
        registry: Registry | None = None,
        conv: MessageConverter,
    ):
        type_oneof = field_level.type
        type_case = type_oneof.field if type_oneof is not None else None
        rules_pb = type_oneof.value if type_oneof is not None else None
        super().__init__(rules_pb, env=env, funcs=funcs, conv=conv)
        self._field = field
        self._ignore_empty = (
            field_level.ignore == validate_pb.Ignore.IF_ZERO_VALUE
            or force_ignore_empty
            # A presence-tracking field (not a map/list element) ignores empty by default.
            or (not for_items and isinstance(field, DescField) and field.presence.name != "IMPLICIT")
        )
        self._required = field_level.required
        if rules_pb is not None:
            assert type_case is not None  # noqa: S101
            type_field = _spec_field(validate_pb.FieldRules, type_case)
            # For each set rule sub-field, look for the private predefined-rule
            # extension that implements it. Standard rules carry these as
            # declared fields known to the bundled stub.
            for rule_field_desc in type(rules_pb).desc().fields:
                if rule_field_desc not in rules_pb:
                    continue
                opts = rule_field_desc.proto.options
                if opts is None or validate_pb.ext_predefined not in opts:
                    continue
                rule_field = rule_field_desc
                for cel in opts[validate_pb.ext_predefined].cel:
                    self.add_rule(
                        cel,
                        rule_field=rule_field,
                        rule_path=validate_pb.FieldPath(
                            elements=[_field_to_element(rule_field), _field_to_element(type_field)]
                        ),
                    )
            # Custom predefined rules are extensions on the rules message,
            # read using the user-provided Registry.
            if registry is not None:
                rules_type_name = type(rules_pb).desc().type_name
                for ext in registry:
                    if (
                        not isinstance(ext, DescExtension)
                        or ext.extendee.type_name != rules_type_name
                        or ext.proto.options is None
                        or validate_pb.ext_predefined not in ext.proto.options
                        or ext.type not in rules_pb
                    ):
                        continue
                    ext_field = ext
                    for cel in ext.proto.options[validate_pb.ext_predefined].cel:
                        self.add_rule(
                            cel,
                            rule_field=ext_field,
                            rule_path=validate_pb.FieldPath(
                                elements=[_field_to_element(ext_field), _field_to_element(type_field)]
                            ),
                        )
        cel_expression_field = _spec_field(validate_pb.FieldRules, "cel_expression")
        for i, cel in enumerate(field_level.cel_expression):
            self.add_rule(
                cel,
                rule_path=validate_pb.FieldPath(elements=[_indexed_field_element(cel_expression_field, i)]),
            )
        cel_field = _spec_field(validate_pb.FieldRules, "cel")
        for i, cel in enumerate(field_level.cel):
            self.add_rule(cel, rule_path=validate_pb.FieldPath(elements=[_indexed_field_element(cel_field, i)]))

    @property
    def _read_field(self) -> DescField:
        # validate() reads from a message, so it only runs on real fields, never
        # on the leaf value types used for map/list element rules.
        assert isinstance(self._field, DescField)  # noqa: S101
        return self._field

    def validate(self, ctx: RuleContext, message: Message):
        field = self._read_field
        if field not in message:
            if self._required:
                ctx.add(
                    Violation(
                        field=validate_pb.FieldPath(elements=[_field_to_element(field)]),
                        rule=FieldRules._required_rule_path,
                        rule_value=self._required,
                        rule_id="required",
                        message="value is required",
                    ),
                )
                return
            if self._ignore_empty:
                return
        val = message[field]
        cel_val = self._conv.field_value(val, field.value)
        sub_ctx = ctx.sub_context()
        self._validate_value(sub_ctx, val)
        self._validate_cel(sub_ctx, this_value=val, this_cel=cel_val)
        if sub_ctx.has_errors():
            sub_ctx.add_field_path_element(_field_to_element(field))
            ctx.add_errors(sub_ctx)

    def validate_item(
        self,
        ctx: RuleContext,
        value: typing.Any,
        item_field: ScalarType | DescMessage | DescEnum,
        *,
        for_key: bool = False,
    ):
        self._validate_value(ctx, value, for_key=for_key)
        self._validate_cel(ctx, this_value=value, this_cel=self._conv.scalar(value, item_field), for_key=for_key)

    def _validate_value(self, ctx: RuleContext, value: typing.Any, *, for_key: bool = False):
        pass


class AnyRules(FieldRules):
    """Rules for an Any field."""

    _in_rule_path: typing.ClassVar[validate_pb.FieldPath] = validate_pb.FieldPath(
        elements=[
            _field_to_element(_spec_field(validate_pb.AnyRules, "in")),
            _field_to_element(_spec_field(validate_pb.FieldRules, "any")),
        ],
    )

    _not_in_rule_path: typing.ClassVar[validate_pb.FieldPath] = validate_pb.FieldPath(
        elements=[
            _field_to_element(_spec_field(validate_pb.AnyRules, "not_in")),
            _field_to_element(_spec_field(validate_pb.FieldRules, "any")),
        ],
    )

    def __init__(
        self,
        env: celpy.Environment,
        funcs: dict[str, celpy.CELFunction],
        field: DescField | ScalarType | DescMessage | DescEnum,
        field_level: validate_pb.FieldRules,
        *,
        registry: Registry | None = None,
        conv: MessageConverter,
    ):
        super().__init__(env, funcs, field, field_level, registry=registry, conv=conv)
        type_oneof = field_level.type
        assert type_oneof is not None and type_oneof.field == "any"  # noqa: S101
        any_rules = type_oneof.value
        self._in: list[str] = list(any_rules.in_)
        self._not_in: list[str] = list(any_rules.not_in)

    def _validate_value(self, ctx: RuleContext, value: typing.Any, *, for_key: bool = False):
        if len(self._in) > 0 and value.type_url not in self._in:
            ctx.add(
                Violation(
                    rule=AnyRules._in_rule_path,
                    rule_value=self._in,
                    rule_id="any.in",
                    message="type URL must be in the allow list",
                    for_key=for_key,
                )
            )
        if value.type_url in self._not_in:
            ctx.add(
                Violation(
                    rule=AnyRules._not_in_rule_path,
                    rule_value=self._not_in,
                    rule_id="any.not_in",
                    message="type URL must not be in the block list",
                    for_key=for_key,
                )
            )


class EnumRules(FieldRules):
    """Rules for an enum field."""

    _defined_only = False

    _defined_only_rule_path: typing.ClassVar[validate_pb.FieldPath] = validate_pb.FieldPath(
        elements=[
            _field_to_element(_spec_field(validate_pb.EnumRules, "defined_only")),
            _field_to_element(_spec_field(validate_pb.FieldRules, "enum")),
        ],
    )

    def __init__(
        self,
        env: celpy.Environment,
        funcs: dict[str, celpy.CELFunction],
        field: DescField | ScalarType | DescMessage | DescEnum,
        field_level: validate_pb.FieldRules,
        *,
        for_items: bool = False,
        force_ignore_empty: bool = False,
        registry: Registry | None = None,
        conv: MessageConverter,
    ):
        super().__init__(
            env,
            funcs,
            field,
            field_level,
            for_items=for_items,
            force_ignore_empty=force_ignore_empty,
            registry=registry,
            conv=conv,
        )
        type_oneof = field_level.type
        assert type_oneof is not None and type_oneof.field == "enum"  # noqa: S101
        if type_oneof.value.defined_only:
            self._defined_only = True
        enum = _enum_of(field)
        # _new_scalar_field_rule only constructs EnumRules for enum-typed fields.
        assert enum is not None  # noqa: S101
        self._defined_numbers = {v.number for v in enum.values}

    def validate(self, ctx: RuleContext, message: Message):
        super().validate(ctx, message)
        if ctx.done:
            return
        field = self._read_field
        if self._defined_only and int(message[field]) not in self._defined_numbers:
            ctx.add(
                Violation(
                    field=validate_pb.FieldPath(elements=[_field_to_element(field)]),
                    rule=EnumRules._defined_only_rule_path,
                    rule_value=self._defined_only,
                    rule_id="enum.defined_only",
                    message="value must be one of the defined enum values",
                ),
            )


class RepeatedRules(FieldRules):
    """Rules for a repeated field."""

    _item_rules: FieldRules | None = None

    _items_rules_suffix: typing.ClassVar[list[validate_pb.FieldPathElement]] = [
        _field_to_element(_spec_field(validate_pb.RepeatedRules, "items")),
        _field_to_element(_spec_field(validate_pb.FieldRules, "repeated")),
    ]

    def __init__(
        self,
        env: celpy.Environment,
        funcs: dict[str, celpy.CELFunction],
        field: DescField,
        field_level: validate_pb.FieldRules,
        item_rules: FieldRules | None,
        *,
        registry: Registry | None = None,
        conv: MessageConverter,
    ):
        super().__init__(env, funcs, field, field_level, registry=registry, conv=conv)
        if item_rules is not None:
            self._item_rules = item_rules

    def validate(self, ctx: RuleContext, message: Message):
        super().validate(ctx, message)
        if ctx.done:
            return
        if self._item_rules is None:
            return
        field = self._read_field
        value = field.value
        assert isinstance(value, DescFieldValueList)  # noqa: S101
        for i, item in enumerate(message[field]):
            if self._item_rules._ignore_empty and not item:
                continue
            sub_ctx = ctx.sub_context()
            self._item_rules.validate_item(sub_ctx, item, value.element)
            if sub_ctx.has_errors():
                sub_ctx.add_field_path_element(_indexed_field_element(field, i))
                sub_ctx.add_rule_path_elements(RepeatedRules._items_rules_suffix)
                ctx.add_errors(sub_ctx)
            if ctx.done:
                return


class MapRules(FieldRules):
    """Rules for a map field."""

    _key_rules: FieldRules | None = None
    _value_rules: FieldRules | None = None

    _key_rules_suffix: typing.ClassVar[list[validate_pb.FieldPathElement]] = [
        _field_to_element(_spec_field(validate_pb.MapRules, "keys")),
        _field_to_element(_spec_field(validate_pb.FieldRules, "map")),
    ]

    _value_rules_suffix: typing.ClassVar[list[validate_pb.FieldPathElement]] = [
        _field_to_element(_spec_field(validate_pb.MapRules, "values")),
        _field_to_element(_spec_field(validate_pb.FieldRules, "map")),
    ]

    def __init__(
        self,
        env: celpy.Environment,
        funcs: dict[str, celpy.CELFunction],
        field: DescField,
        field_level: validate_pb.FieldRules,
        key_rules: FieldRules | None,
        value_rules: FieldRules | None,
        *,
        registry: Registry | None = None,
        conv: MessageConverter,
    ):
        super().__init__(env, funcs, field, field_level, registry=registry, conv=conv)
        if key_rules is not None:
            self._key_rules = key_rules
        if value_rules is not None:
            self._value_rules = value_rules

    def validate(self, ctx: RuleContext, message: Message):
        super().validate(ctx, message)
        if ctx.done:
            return
        field = self._read_field
        value = field.value
        assert isinstance(value, DescFieldValueMap)  # noqa: S101
        for k, v in message[field].items():
            key_ctx = ctx.sub_context()
            if self._key_rules is not None and (not self._key_rules._ignore_empty or k):
                self._key_rules.validate_item(key_ctx, k, value.key, for_key=True)
                if key_ctx.has_errors():
                    key_ctx.add_rule_path_elements(MapRules._key_rules_suffix)
            map_ctx = ctx.sub_context()
            if self._value_rules is not None and (not self._value_rules._ignore_empty or v):
                self._value_rules.validate_item(map_ctx, v, value.value)
                if map_ctx.has_errors():
                    map_ctx.add_rule_path_elements(MapRules._value_rules_suffix)
            map_ctx.add_errors(key_ctx)
            if map_ctx.has_errors():
                map_ctx.add_field_path_element(_map_key_element(field, k))
                ctx.add_errors(map_ctx)


class OneofRules(Rules):
    """Rules for a oneof definition."""

    required = True

    def __init__(self, oneof: DescOneof, rules: validate_pb.OneofRules):
        self._oneof = oneof
        if not rules.required:
            self.required = False

    def validate(self, ctx: RuleContext, message: Message):
        if getattr(message, self._oneof.local_name) is None:
            if self.required:
                ctx.add(
                    Violation(
                        field=validate_pb.FieldPath(elements=[_oneof_to_element(self._oneof)]),
                        rule_id="required",
                        message="exactly one field is required in oneof",
                    )
                )
            return


def _message_child(field: DescField) -> DescMessage | None:
    """The sub-message a field recurses into: a map value, list element, or
    singular message, if message-typed."""
    match field.value:
        case DescFieldValueMap(value=DescMessage() as message):
            return message
        case DescFieldValueList(element=DescMessage() as message):
            return message
        case DescFieldValueMessage(message=message):
            return message
        case _:
            return None


class RuleFactory:
    """Factory for creating and caching rules, keyed on protobuf-py descriptors."""

    _env: celpy.Environment
    _funcs: dict[str, celpy.CELFunction]

    def __init__(self, funcs: dict[str, celpy.CELFunction], registry: Registry | None = None):
        self._env = celpy.Environment(runner_class=InterpretedRunner)
        self._funcs = funcs
        self._registry = registry
        self._conv = MessageConverter()
        self._cache: dict[DescMessage, list[Rules] | Exception] = {}

    def get(self, desc: DescMessage) -> list[Rules]:
        if desc not in self._cache:
            try:
                self._cache[desc] = self._new_rules(desc)
            except Exception as e:
                self._cache[desc] = e
        result = self._cache[desc]
        if isinstance(result, Exception):
            raise result
        return result

    def _new_message_rule(self, rules: validate_pb.MessageRules, desc: DescMessage) -> MessageRules:
        result = MessageRules(rules, desc, env=self._env, funcs=self._funcs, conv=self._conv)
        for oneof in rules.oneof:
            result.add_oneof(oneof)
        for expr in rules.cel_expression:
            result.add_rule(expr)
        for cel in rules.cel:
            result.add_rule(cel)
        return result

    def _new_scalar_field_rule(
        self,
        field: DescField | ScalarType | DescMessage | DescEnum,
        field_level: validate_pb.FieldRules,
        *,
        for_items: bool = False,
        force_ignore_empty: bool = False,
    ) -> FieldRules | None:
        if field_level.ignore == validate_pb.Ignore.ALWAYS:
            return None
        type_case = _which_type(field_level)
        kw = {
            "for_items": for_items,
            "force_ignore_empty": force_ignore_empty,
            "registry": self._registry,
            "conv": self._conv,
        }
        match type_case:
            case None:
                return FieldRules(self._env, self._funcs, field, field_level, **kw)
            case "enum":
                if _enum_of(field) is None:
                    raise _type_mismatch(field, "enum")
                return EnumRules(self._env, self._funcs, field, field_level, **kw)
            case "any":
                _check_field_type(field, None, "google.protobuf.Any")
                return AnyRules(self._env, self._funcs, field, field_level, registry=self._registry, conv=self._conv)
            case _ if type_case in _RULE_FIELD_TYPES:
                expected, wrapper = _RULE_FIELD_TYPES[type_case]
                _check_field_type(field, expected, wrapper)
                return FieldRules(self._env, self._funcs, field, field_level, **kw)
            case _:
                msg = f"unknown rule type {type_case!r}"
                raise CompilationError(msg)

    def _new_field_rule(
        self, field: DescField, rules: validate_pb.FieldRules, *, force_ignore_empty: bool = False
    ) -> FieldRules | None:
        type_oneof = rules.type
        match field.value:
            case DescFieldValueMap() as value:
                map_rules = type_oneof.value if type_oneof is not None and type_oneof.field == "map" else None
                key_rules = None
                value_rules = None
                if map_rules is not None and map_rules.keys is not None:
                    key_rules = self._new_scalar_field_rule(value.key, map_rules.keys, for_items=True)
                if map_rules is not None and map_rules.values is not None:
                    value_rules = self._new_scalar_field_rule(value.value, map_rules.values, for_items=True)
                return MapRules(
                    self._env,
                    self._funcs,
                    field,
                    rules,
                    key_rules,
                    value_rules,
                    registry=self._registry,
                    conv=self._conv,
                )
            case DescFieldValueList() as value:
                item_rule = None
                rep_rules = type_oneof.value if type_oneof is not None and type_oneof.field == "repeated" else None
                if rep_rules is not None and rep_rules.items is not None:
                    item_rule = self._new_scalar_field_rule(value.element, rep_rules.items)
                return RepeatedRules(
                    self._env, self._funcs, field, rules, item_rule, registry=self._registry, conv=self._conv
                )
            case _:
                return self._new_scalar_field_rule(field, rules, force_ignore_empty=force_ignore_empty)

    def _new_rules(self, desc: DescMessage) -> list[Rules]:
        result: list[Rules] = []
        all_msg_oneof_fields: set[str] = set()

        msg_opts = desc.proto.options
        if msg_opts is not None and validate_pb.ext_message in msg_opts:
            message_level: validate_pb.MessageRules = msg_opts[validate_pb.ext_message]
            for oneof in message_level.oneof:
                all_msg_oneof_fields.update(oneof.fields)
            if rule := self._new_message_rule(message_level, desc):
                result.append(rule)

        for oneof in desc.oneofs:
            oneof_opts = oneof.proto.options
            if oneof_opts is not None and validate_pb.ext_oneof in oneof_opts:
                result.append(OneofRules(oneof, oneof_opts[validate_pb.ext_oneof]))

        ignore_field = _spec_field(validate_pb.FieldRules, "ignore")
        for field in desc.fields:
            field_opts = field.proto.options
            field_level: validate_pb.FieldRules | None = None
            if field_opts is not None and validate_pb.ext_field in field_opts:
                field_level = field_opts[validate_pb.ext_field]
            if field_level is not None:
                force_ignore_empty = ignore_field not in field_level and field.name in all_msg_oneof_fields
                if field_level.ignore == validate_pb.Ignore.ALWAYS:
                    continue
                if field_rule := self._new_field_rule(field, field_level, force_ignore_empty=force_ignore_empty):
                    result.append(field_rule)
                type_oneof = field_level.type
                if type_oneof is not None and type_oneof.field == "repeated":
                    rep = type_oneof.value
                    if rep.items is not None and rep.items.ignore == validate_pb.Ignore.ALWAYS:
                        continue
            sub_desc = _message_child(field)
            if sub_desc is None:
                continue
            match field.value:
                case DescFieldValueMap():
                    result.append(MapValMsgRule(self, field, sub_desc))
                case DescFieldValueList():
                    result.append(RepeatedMsgRule(self, field, sub_desc))
                case _:
                    result.append(SubMsgRule(self, field, sub_desc))
        return result


class _SubMessageRule(Rules):
    """Recurses into a message-typed field's own rules. Subclasses supply how to
    enumerate the sub-messages to validate (singular, map values, list items)
    as (sub_message, field_path_element) pairs."""

    def __init__(self, factory: RuleFactory, field: DescField, sub_desc: DescMessage):
        self._factory = factory
        self._field = field
        self._sub_desc = sub_desc

    def _validate_each(self, ctx: RuleContext, items: Iterable[tuple[Message, validate_pb.FieldPathElement]]):
        rules = self._factory.get(self._sub_desc)
        if not rules:
            return
        for value, element in items:
            sub_ctx = ctx.sub_context()
            for rule in rules:
                rule.validate(sub_ctx, value)
            if sub_ctx.has_errors():
                sub_ctx.add_field_path_element(element)
                ctx.add_errors(sub_ctx)


class SubMsgRule(_SubMessageRule):
    def validate(self, ctx: RuleContext, message: Message):
        if self._field in message:
            self._validate_each(ctx, [(message[self._field], _field_to_element(self._field))])


class MapValMsgRule(_SubMessageRule):
    def validate(self, ctx: RuleContext, message: Message):
        val = message[self._field]
        self._validate_each(ctx, ((v, _map_key_element(self._field, k)) for k, v in val.items()))


class RepeatedMsgRule(_SubMessageRule):
    def validate(self, ctx: RuleContext, message: Message):
        val = message[self._field]
        self._validate_each(ctx, ((item, _indexed_field_element(self._field, i)) for i, item in enumerate(val)))
