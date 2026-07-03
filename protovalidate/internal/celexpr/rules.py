# Copyright 2023-2026 Buf Technologies, Inc.
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

"""The rule engine.

Rules are *discovered* from protobuf-py descriptors: the message structure is
read off the google mirror (the validated types are registered in google's pool
by the bridge anyway), but the ``buf.validate`` *options* are read off the
relocatable protobuf-py stub (``validate_pb``), so nothing needs ``buf.validate``
in google's global pool for discovery. Rules are *evaluated* by cel-expr-python,
which only ingests google messages, so the message under validation and the rule
messages bound as ``rules``/``rule`` are bridged to google (see
``celexpr.bridge.GoogleBridge``). Output ``Violation``\\s are protobuf-py
``validate_pb`` messages — the public type, shared with the celpy engine via
``protovalidate.internal._core``.
"""

import dataclasses
import datetime
import functools
import typing
from collections.abc import Container

import protobuf
from cel_expr_python import cel
from cel_expr_python.ext import ext_strings
from google.protobuf import any_pb2, descriptor, descriptor_pool, message, wrappers_pb2
from protobuf import Oneof
from protobuf.wkt import FieldDescriptorProto

from protovalidate._gen.buf.validate import validate_pb

# Backend-agnostic primitives shared with the celpy engine (protovalidate.internal.rules).
from protovalidate.internal._core import CompilationError, RuleContext, Rules, Violation
from protovalidate.internal.celexpr.bridge import GoogleBridge

# protobuf 7+ removed FieldDescriptor.label / LABEL_REPEATED in favour of is_repeated.
_FieldDescriptorClass = descriptor.FieldDescriptor
if hasattr(_FieldDescriptorClass, "is_repeated"):

    def _is_repeated(field: descriptor.FieldDescriptor) -> bool:
        return field.is_repeated

else:

    def _is_repeated(field: descriptor.FieldDescriptor) -> bool:
        return field.label == descriptor.FieldDescriptor.LABEL_REPEATED


_FIELD_TYPE_NAMES: dict[int, str] = {
    descriptor.FieldDescriptor.TYPE_MESSAGE: "message",
    descriptor.FieldDescriptor.TYPE_GROUP: "group",
    descriptor.FieldDescriptor.TYPE_ENUM: "enum",
    descriptor.FieldDescriptor.TYPE_BOOL: "bool",
    descriptor.FieldDescriptor.TYPE_BYTES: "bytes",
    descriptor.FieldDescriptor.TYPE_STRING: "string",
    descriptor.FieldDescriptor.TYPE_FLOAT: "float",
    descriptor.FieldDescriptor.TYPE_DOUBLE: "double",
    descriptor.FieldDescriptor.TYPE_INT32: "int32",
    descriptor.FieldDescriptor.TYPE_INT64: "int64",
    descriptor.FieldDescriptor.TYPE_SINT32: "sint32",
    descriptor.FieldDescriptor.TYPE_SINT64: "sint64",
    descriptor.FieldDescriptor.TYPE_SFIXED32: "sfixed32",
    descriptor.FieldDescriptor.TYPE_SFIXED64: "sfixed64",
    descriptor.FieldDescriptor.TYPE_UINT32: "uint32",
    descriptor.FieldDescriptor.TYPE_UINT64: "uint64",
    descriptor.FieldDescriptor.TYPE_FIXED32: "fixed32",
    descriptor.FieldDescriptor.TYPE_FIXED64: "fixed64",
}


def _get_type_name(fd: typing.Any) -> str:
    return _FIELD_TYPE_NAMES.get(fd, "unknown")


def _proto_message_has_field(msg: message.Message, field: descriptor.FieldDescriptor) -> typing.Any:
    if field.is_extension:
        return msg.HasExtension(field)  # ty: ignore[invalid-argument-type]
    return msg.HasField(field.name)


def _proto_message_get_field(msg: message.Message, field: descriptor.FieldDescriptor) -> typing.Any:
    if field.is_extension:
        return msg.Extensions[field]  # ty: ignore[invalid-argument-type]
    return getattr(msg, field.name)


_UNSIGNED_FIELD_TYPES = frozenset(
    (
        descriptor.FieldDescriptor.TYPE_UINT32,
        descriptor.FieldDescriptor.TYPE_UINT64,
        descriptor.FieldDescriptor.TYPE_FIXED32,
        descriptor.FieldDescriptor.TYPE_FIXED64,
    )
)


def _scalar_field_value_to_cel(val: typing.Any, field: descriptor.FieldDescriptor) -> typing.Any:
    # The runtime converts Python scalars and messages (including the
    # well-known wrapper, timestamp, and duration types) to CEL values
    # natively, so most values pass through unchanged. The exceptions ride in
    # on well-known wrapper messages, which the runtime unwraps natively:
    #
    # - Bytes: raw Python bytes trigger a runtime bug where values reaching
    #   custom functions or equality against message fields are corrupted.
    # - Unsigned ints: a Python int always converts to a CEL int; the wrapper
    #   is the only way to produce a CEL uint for uint-typed fields.
    # - Strings containing NUL: the conversion truncates at the first NUL.
    if field.type == descriptor.FieldDescriptor.TYPE_BYTES:
        return wrappers_pb2.BytesValue(value=val)
    if field.type in _UNSIGNED_FIELD_TYPES:
        if field.type in (descriptor.FieldDescriptor.TYPE_UINT32, descriptor.FieldDescriptor.TYPE_FIXED32):
            return wrappers_pb2.UInt32Value(value=val)
        return wrappers_pb2.UInt64Value(value=val)
    if field.type == descriptor.FieldDescriptor.TYPE_STRING and "\x00" in val:
        return wrappers_pb2.StringValue(value=val)
    return val


def _field_value_to_cel(val: typing.Any, field: descriptor.FieldDescriptor) -> typing.Any:
    if _is_repeated(field):
        if field.message_type is not None and field.message_type.GetOptions().map_entry:
            return dict(val)
        return list(val)
    return _scalar_field_value_to_cel(val, field)


def _is_empty_field(msg: message.Message, field: descriptor.FieldDescriptor) -> bool:
    if field.has_presence:
        return not _proto_message_has_field(msg, field)
    if _is_repeated(field):
        return len(_proto_message_get_field(msg, field)) == 0
    return _proto_message_get_field(msg, field) == field.default_value


def field_to_cel(msg: message.Message, field: descriptor.FieldDescriptor) -> typing.Any:
    return _field_value_to_cel(_proto_message_get_field(msg, field), field)


# ----- protobuf-py validate_pb path construction (output is always validate_pb) -----


def _ftype(google_type: int) -> FieldDescriptorProto.Type:
    """Maps a google FieldDescriptor.type int to the protobuf-py enum value."""
    return FieldDescriptorProto.Type(google_type)


def _field_to_element(field: descriptor.FieldDescriptor) -> validate_pb.FieldPathElement:
    """A FieldPathElement for a (google) field of the message being validated."""
    return validate_pb.FieldPathElement(
        field_number=field.number,
        field_name=field.name if not field.is_extension else f"[{field.full_name}]",
        field_type=_ftype(field.type),
    )


def _indexed_field_element(field: descriptor.FieldDescriptor, index: int) -> validate_pb.FieldPathElement:
    return validate_pb.FieldPathElement(
        field_number=field.number,
        field_name=field.name if not field.is_extension else f"[{field.full_name}]",
        field_type=_ftype(field.type),
        subscript=Oneof(field="index", value=index),
    )


def _oneof_to_element(oneof: descriptor.OneofDescriptor) -> validate_pb.FieldPathElement:
    return validate_pb.FieldPathElement(field_name=oneof.name)


_INT_KEY_TYPES = frozenset(
    (
        descriptor.FieldDescriptor.TYPE_INT32,
        descriptor.FieldDescriptor.TYPE_SFIXED32,
        descriptor.FieldDescriptor.TYPE_INT64,
        descriptor.FieldDescriptor.TYPE_SFIXED64,
        descriptor.FieldDescriptor.TYPE_SINT32,
        descriptor.FieldDescriptor.TYPE_SINT64,
    )
)
_UINT_KEY_TYPES = frozenset(
    (
        descriptor.FieldDescriptor.TYPE_UINT32,
        descriptor.FieldDescriptor.TYPE_FIXED32,
        descriptor.FieldDescriptor.TYPE_UINT64,
        descriptor.FieldDescriptor.TYPE_FIXED64,
    )
)


def _map_key_element(
    field: descriptor.FieldDescriptor,
    key: typing.Any,
    key_field: descriptor.FieldDescriptor,
    value_field: descriptor.FieldDescriptor,
) -> validate_pb.FieldPathElement:
    subscript: Oneof
    if key_field.type == descriptor.FieldDescriptor.TYPE_BOOL:
        subscript = Oneof(field="bool_key", value=key)
    elif key_field.type in _INT_KEY_TYPES:
        subscript = Oneof(field="int_key", value=key)
    elif key_field.type in _UINT_KEY_TYPES:
        subscript = Oneof(field="uint_key", value=key)
    elif key_field.type == descriptor.FieldDescriptor.TYPE_STRING:
        subscript = Oneof(field="string_key", value=key)
    else:
        msg = "unexpected map type"
        raise CompilationError(msg)
    return validate_pb.FieldPathElement(
        field_number=field.number,
        field_name=field.name if not field.is_extension else f"[{field.full_name}]",
        field_type=_ftype(field.type),
        key_type=_ftype(key_field.type),
        value_type=_ftype(value_field.type),
        subscript=subscript,
    )


# Rule-spec path elements reference the buf.validate rule messages themselves,
# whose descriptors come from the bundled protobuf-py stub.
def _spec_element(pb_field: protobuf.DescField) -> validate_pb.FieldPathElement:
    return validate_pb.FieldPathElement(
        field_number=pb_field.number,
        field_name=pb_field.name,
        field_type=pb_field.proto.type,
    )


def _indexed_spec_element(pb_field: protobuf.DescField, index: int) -> validate_pb.FieldPathElement:
    return validate_pb.FieldPathElement(
        field_number=pb_field.number,
        field_name=pb_field.name,
        field_type=pb_field.proto.type,
        subscript=Oneof(field="index", value=index),
    )


def _spec_field(rules_cls: typing.Any, name: str) -> protobuf.DescField:
    return rules_cls.desc()._fields_by_name[name]


def _which_type(field_level: typing.Any) -> str | None:
    """The set sub-field name of a FieldRules ``type`` oneof, or None."""
    return field_level.type.field if field_level.type is not None else None


@functools.lru_cache(maxsize=1)
def _google_predefined_ext() -> typing.Any:
    """The google ``buf.validate.predefined`` extension descriptor.

    Resolved lazily off the global pool, into which the bridge mirrors
    ``buf.validate`` (and the user's files, which define any custom predefined
    rule extensions) when it bridges rule messages.
    """
    return descriptor_pool.Default().FindExtensionByName("buf.validate.predefined")


def _message_child(pb_field: protobuf.DescField) -> protobuf.DescMessage | None:
    """The protobuf-py descriptor of a message-typed field, list item, or map value."""
    value = pb_field.value
    if isinstance(value, protobuf.DescFieldValueMessage):
        return value.message
    if isinstance(value, protobuf.DescFieldValueList) and isinstance(value.element, protobuf.DescMessage):
        return value.element
    if isinstance(value, protobuf.DescFieldValueMap) and isinstance(value.value, protobuf.DescMessage):
        return value.value
    return None


@dataclasses.dataclass
class CelRunner:
    runner: cel.Expression
    rule: typing.Any
    rule_value: typing.Any | None = None
    rule_cel: typing.Any | None = None
    rule_path: validate_pb.FieldPath | None = None


class CelRules(Rules):
    """A rule that has rules written in CEL.

    ``_rules`` holds the *google* rule message (the buf.validate rules bridged
    from protobuf-py), so it can be bound as the ``rules`` CEL variable.
    """

    _cel: list[CelRunner]
    _rules: message.Message | None = None
    _uses_now: bool = False

    def __init__(self, rules_google: message.Message | None):
        self._cel = []
        self._rules = rules_google

    def _validate_cel(
        self,
        ctx: RuleContext,
        *,
        this_value: typing.Any | None = None,
        this_cel: typing.Any | None = None,
        for_key: bool = False,
    ):
        if not self._cel:
            return
        activation: dict[str, typing.Any] = {}
        if this_cel is not None:
            activation["this"] = this_cel
        activation["rules"] = self._rules
        if self._uses_now:
            activation["now"] = datetime.datetime.now(tz=datetime.timezone.utc)
        for runner in self._cel:
            activation["rule"] = runner.rule_cel
            result = runner.runner.eval(data=activation)
            result_type = result.type()
            if result_type == cel.Type.BOOL:
                if not result.plain_value():
                    msg = runner.rule.message
                    if len(msg) == 0:
                        msg = f'"{runner.rule.expression}" returned false'
                    ctx.add(
                        Violation(
                            field_value=this_value,
                            rule=runner.rule_path,
                            rule_value=runner.rule_value,
                            rule_id=runner.rule.id,
                            message=msg,
                            for_key=for_key,
                        ),
                    )
            elif result_type == cel.Type.STRING:
                # Formatting bytes with %s can yield a CEL string that is not
                # valid UTF-8, which cannot convert to a Python str.
                try:
                    result_message = result.plain_value()
                except TypeError:
                    result_message = f'"{runner.rule.expression}" returned false'
                if result_message:
                    ctx.add(
                        Violation(
                            field_value=this_value,
                            rule=runner.rule_path,
                            rule_value=runner.rule_value,
                            rule_id=runner.rule.id,
                            message=result_message,  # ty: ignore[invalid-argument-type]
                            for_key=for_key,
                        ),
                    )
            elif result_type == cel.Type.ERROR:
                raise RuntimeError(str(result.plain_value()))

    def add_rule(
        self,
        env: cel.Env,
        rules: typing.Any,
        *,
        rule_field: descriptor.FieldDescriptor | None = None,
        rule_path: validate_pb.FieldPath | None = None,
    ):
        if isinstance(rules, str):
            expression = rules
            rules = validate_pb.Rule(id=expression, expression=expression)
        if "now" in rules.expression:
            self._uses_now = True
        try:
            prog = env.compile(rules.expression)
        except RuntimeError as ex:
            raise CompilationError(str(ex)) from ex
        rule_value = None
        rule_cel = None
        if rule_field is not None and self._rules is not None:
            rule_value = _proto_message_get_field(self._rules, rule_field)
            rule_cel = field_to_cel(self._rules, rule_field)
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
    """Validates a single buf.validate.MessageOneofRule given via the message option (buf.validate.message).oneof"""

    def __init__(self, fields: list[descriptor.FieldDescriptor], *, required: bool):
        self._fields = fields
        self._required = required

    def validate(self, ctx: RuleContext, message: message.Message):
        num_set_fields = sum(1 for field in self._fields if not _is_empty_field(message, field))
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

    def __init__(self, rules_google: message.Message | None, desc: descriptor.Descriptor):
        super().__init__(rules_google)
        self._oneofs = []
        self._desc = desc

    def validate(self, ctx: RuleContext, message: message.Message):
        if self._cel:
            self._validate_cel(ctx, this_cel=message)
            if ctx.done:
                return
        for oneof in self._oneofs:
            oneof.validate(ctx, message)
            if ctx.done:
                return

    def add_oneof(self, rule: typing.Any):
        fields = []
        seen = set()
        if len(rule.fields) == 0:
            msg = f"at least one field must be specified in oneof rule for the message {self._desc.full_name}"
            raise CompilationError(msg)
        for name in rule.fields:
            if name in self._desc.fields_by_name:
                if name in seen:
                    msg = f"duplicate {name} in oneof rule for the message {self._desc.full_name}"
                    raise CompilationError(msg)
                fields.append(self._desc.fields_by_name[name])
                seen.add(name)
            else:
                msg = f'field "{name}" not found in message {self._desc.full_name}'
                raise CompilationError(msg)
        self._oneofs.append(MessageOneofRule(fields, required=rule.required))


def check_field_type(field: descriptor.FieldDescriptor, expected: int, wrapper_name: str | None = None):
    if field.type != expected and (
        field.type != descriptor.FieldDescriptor.TYPE_MESSAGE or field.message_type.full_name != wrapper_name
    ):
        field_type_str = _get_type_name(field.type)
        if expected == 0:
            if wrapper_name is not None:
                expected_type_str = wrapper_name
            else:
                expected_type_str = _get_type_name(descriptor.FieldDescriptor.TYPE_MESSAGE)
        else:
            expected_type_str = _get_type_name(expected)
        msg = f"field {field.name} has type {field_type_str} but expected {expected_type_str}"
        raise CompilationError(msg)


def _is_map(field: descriptor.FieldDescriptor):
    return _is_repeated(field) and field.message_type is not None and field.message_type.GetOptions().map_entry


def _is_list(field: descriptor.FieldDescriptor):
    return _is_repeated(field) and not _is_map(field)


class FieldRules(CelRules):
    """Field-level rules."""

    _ignore_empty = False
    _required = False

    _required_rule_path: typing.ClassVar[validate_pb.FieldPath] = validate_pb.FieldPath(
        elements=[_spec_element(_spec_field(validate_pb.FieldRules, "required"))]
    )

    def __init__(
        self,
        env: cel.Env,
        bridge: GoogleBridge,
        field: descriptor.FieldDescriptor,
        field_level: typing.Any,
        *,
        for_items: bool = False,
        force_ignore_empty: bool = False,
    ):
        type_case = _which_type(field_level)
        rules_pb = field_level.type.value if type_case is not None else None
        super().__init__(bridge.to_google(rules_pb) if rules_pb is not None else None)
        self._field = field
        self._ignore_empty = (
            field_level.ignore == validate_pb.Ignore.IF_ZERO_VALUE
            or force_ignore_empty
            or (field.has_presence and not for_items)
        )
        self._required = field_level.required
        if rules_pb is not None:
            # Each set rule sub-field (standard rules like `gt`, and custom
            # extension rules alike) may carry a private predefined-rule
            # extension whose CEL implements it. Read these off the bridged
            # google rules message: it is parsed against the global pool, into
            # which the bridge has mirrored both buf.validate and the user's
            # files, so custom extension rules decode (they would otherwise
            # remain undecoded on the relocatable protobuf-py stub).
            g_rules = self._rules
            assert g_rules is not None  # rules_pb set implies the bridged rules # noqa: S101
            assert type_case is not None  # rules_pb set implies a type oneof # noqa: S101
            type_field = _spec_field(validate_pb.FieldRules, type_case)
            predefined_ext = _google_predefined_ext()
            for rule_field, _value in g_rules.ListFields():
                options = rule_field.GetOptions()
                if not options.HasExtension(predefined_ext):
                    continue
                for cel_rule in options.Extensions[predefined_ext].cel:
                    self.add_rule(
                        env,
                        cel_rule,
                        rule_field=rule_field,
                        rule_path=validate_pb.FieldPath(
                            elements=[_field_to_element(rule_field), _spec_element(type_field)]
                        ),
                    )
        cel_expression_field = _spec_field(validate_pb.FieldRules, "cel_expression")
        for i, cel_rule in enumerate(field_level.cel_expression):
            self.add_rule(
                env,
                cel_rule,
                rule_path=validate_pb.FieldPath(elements=[_indexed_spec_element(cel_expression_field, i)]),
            )
        cel_field = _spec_field(validate_pb.FieldRules, "cel")
        for i, cel_rule in enumerate(field_level.cel):
            self.add_rule(
                env,
                cel_rule,
                rule_path=validate_pb.FieldPath(elements=[_indexed_spec_element(cel_field, i)]),
            )

    def validate(self, ctx: RuleContext, message: message.Message):
        if _is_empty_field(message, self._field):
            if self._required:
                ctx.add(
                    Violation(
                        field=validate_pb.FieldPath(elements=[_field_to_element(self._field)]),
                        rule=FieldRules._required_rule_path,
                        rule_value=self._required,
                        rule_id="required",
                        message="value is required",
                    ),
                )
                return
            if self._ignore_empty:
                return
        val = _proto_message_get_field(message, self._field)
        cel_val = _field_value_to_cel(val, self._field)
        sub_ctx = ctx.sub_context()
        self._validate_value(sub_ctx, val)
        self._validate_cel(sub_ctx, this_value=val, this_cel=cel_val)
        if sub_ctx.has_errors():
            element = _field_to_element(self._field)
            sub_ctx.add_field_path_element(element)
            ctx.add_errors(sub_ctx)

    def validate_item(self, ctx: RuleContext, value: typing.Any, *, for_key: bool = False):
        self._validate_value(ctx, value, for_key=for_key)
        self._validate_cel(
            ctx, this_value=value, this_cel=_scalar_field_value_to_cel(value, self._field), for_key=for_key
        )

    def _validate_value(self, ctx: RuleContext, value: typing.Any, *, for_key: bool = False):
        pass


class AnyRules(FieldRules):
    """Rules for an Any field."""

    _in_rule_path: typing.ClassVar[validate_pb.FieldPath] = validate_pb.FieldPath(
        elements=[
            _spec_element(_spec_field(validate_pb.AnyRules, "in")),
            _spec_element(_spec_field(validate_pb.FieldRules, "any")),
        ],
    )

    _not_in_rule_path: typing.ClassVar[validate_pb.FieldPath] = validate_pb.FieldPath(
        elements=[
            _spec_element(_spec_field(validate_pb.AnyRules, "not_in")),
            _spec_element(_spec_field(validate_pb.FieldRules, "any")),
        ],
    )

    def __init__(
        self,
        env: cel.Env,
        bridge: GoogleBridge,
        field: descriptor.FieldDescriptor,
        field_level: typing.Any,
    ):
        super().__init__(env, bridge, field, field_level)
        any_rules = field_level.type.value
        self._in = list(any_rules.in_) or []
        self._not_in: Container[str] = list(any_rules.not_in) or []

    def _validate_value(self, ctx: RuleContext, value: any_pb2.Any, *, for_key: bool = False):
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
            _spec_element(_spec_field(validate_pb.EnumRules, "defined_only")),
            _spec_element(_spec_field(validate_pb.FieldRules, "enum")),
        ],
    )

    def __init__(
        self,
        env: cel.Env,
        bridge: GoogleBridge,
        field: descriptor.FieldDescriptor,
        field_level: typing.Any,
        *,
        for_items: bool = False,
        force_ignore_empty: bool = False,
    ):
        super().__init__(env, bridge, field, field_level, for_items=for_items, force_ignore_empty=force_ignore_empty)
        if field_level.type.value.defined_only:
            self._defined_only = True

    def validate(self, ctx: RuleContext, message: message.Message):
        super().validate(ctx, message)
        if ctx.done:
            return
        if self._defined_only and getattr(message, self._field.name) not in self._field.enum_type.values_by_number:
            ctx.add(
                Violation(
                    field=validate_pb.FieldPath(elements=[_field_to_element(self._field)]),
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
        _spec_element(_spec_field(validate_pb.RepeatedRules, "items")),
        _spec_element(_spec_field(validate_pb.FieldRules, "repeated")),
    ]

    def __init__(
        self,
        env: cel.Env,
        bridge: GoogleBridge,
        field: descriptor.FieldDescriptor,
        field_level: typing.Any,
        item_rules: FieldRules | None,
    ):
        super().__init__(env, bridge, field, field_level)
        if item_rules is not None:
            self._item_rules = item_rules

    def validate(self, ctx: RuleContext, message: message.Message):
        super().validate(ctx, message)
        if ctx.done:
            return
        value = getattr(message, self._field.name)
        if self._item_rules is not None:
            for i, item in enumerate(value):
                if self._item_rules._ignore_empty and not item:
                    continue
                sub_ctx = ctx.sub_context()
                self._item_rules.validate_item(sub_ctx, item)
                if sub_ctx.has_errors():
                    sub_ctx.add_field_path_element(_indexed_field_element(self._field, i))
                    sub_ctx.add_rule_path_elements(RepeatedRules._items_rules_suffix)
                    ctx.add_errors(sub_ctx)
                if ctx.done:
                    return


class MapRules(FieldRules):
    """Rules for a map field."""

    _key_rules: FieldRules | None = None
    _value_rules: FieldRules | None = None

    _key_rules_suffix: typing.ClassVar[list[validate_pb.FieldPathElement]] = [
        _spec_element(_spec_field(validate_pb.MapRules, "keys")),
        _spec_element(_spec_field(validate_pb.FieldRules, "map")),
    ]

    _value_rules_suffix: typing.ClassVar[list[validate_pb.FieldPathElement]] = [
        _spec_element(_spec_field(validate_pb.MapRules, "values")),
        _spec_element(_spec_field(validate_pb.FieldRules, "map")),
    ]

    def __init__(
        self,
        env: cel.Env,
        bridge: GoogleBridge,
        field: descriptor.FieldDescriptor,
        field_level: typing.Any,
        key_rules: FieldRules | None,
        value_rules: FieldRules | None,
    ):
        super().__init__(env, bridge, field, field_level)
        if key_rules is not None:
            self._key_rules = key_rules
        if value_rules is not None:
            self._value_rules = value_rules

    def validate(self, ctx: RuleContext, message: message.Message):
        super().validate(ctx, message)
        if ctx.done:
            return
        value = getattr(message, self._field.name)
        key_field = self._field.message_type.fields_by_name["key"]
        value_field = self._field.message_type.fields_by_name["value"]
        for k, v in value.items():
            key_ctx = ctx.sub_context()
            if self._key_rules is not None:
                if not self._key_rules._ignore_empty or k:
                    self._key_rules.validate_item(key_ctx, k, for_key=True)
                    if key_ctx.has_errors():
                        key_ctx.add_rule_path_elements(MapRules._key_rules_suffix)
            map_ctx = ctx.sub_context()
            if self._value_rules is not None:
                if not self._value_rules._ignore_empty or v:
                    self._value_rules.validate_item(map_ctx, v)
                    if map_ctx.has_errors():
                        map_ctx.add_rule_path_elements(MapRules._value_rules_suffix)
            map_ctx.add_errors(key_ctx)
            if map_ctx.has_errors():
                map_ctx.add_field_path_element(_map_key_element(self._field, k, key_field, value_field))
                ctx.add_errors(map_ctx)


class OneofRules(Rules):
    """Rules for a oneof definition."""

    required = True

    def __init__(self, oneof: descriptor.OneofDescriptor, rules: typing.Any):
        self._oneof = oneof
        if not rules.required:
            self.required = False

    def validate(self, ctx: RuleContext, message: message.Message):
        if not message.WhichOneof(self._oneof.name):
            if self.required:
                ctx.add(
                    Violation(
                        field=validate_pb.FieldPath(elements=[_oneof_to_element(self._oneof)]),
                        rule_id="required",
                        message="exactly one field is required in oneof",
                    )
                )
            return


class RuleFactory:
    """Factory for creating and caching rules, keyed on protobuf-py descriptors."""

    _env: cel.Env

    def __init__(self, extension: cel.CelExtensionBase, bridge: GoogleBridge):
        self._bridge = bridge
        # cel-expr-python evaluates against — and type-checks bindings against —
        # the global pool the bridge populates.
        self._env = cel.NewEnv(
            descriptor_pool=descriptor_pool.Default(),
            variables={
                "this": cel.Type.DYN,
                "rules": cel.Type.DYN,
                "rule": cel.Type.DYN,
                "now": cel.Type.TIMESTAMP,
            },
            extensions=[ext_strings.ExtStrings(), extension],
        )
        self._cache: dict[str, list[Rules] | Exception] = {}

    def get(self, desc: protobuf.DescMessage) -> list[Rules]:
        key = desc.type_name
        if key not in self._cache:
            try:
                self._cache[key] = self._new_rules(desc)
            except Exception as e:
                self._cache[key] = e
        result = self._cache[key]
        if isinstance(result, Exception):
            raise result
        return result

    def _new_message_rule(self, rules: typing.Any, desc: descriptor.Descriptor) -> MessageRules:
        result = MessageRules(self._bridge.to_google(rules), desc)
        for oneof in rules.oneof:
            result.add_oneof(oneof)
        for expr in rules.cel_expression:
            result.add_rule(self._env, expr)
        for cel_rule in rules.cel:
            result.add_rule(self._env, cel_rule)
        return result

    def _new_scalar_field_rule(
        self,
        field: descriptor.FieldDescriptor,
        field_level: typing.Any,
        *,
        for_items: bool = False,
        force_ignore_empty: bool = False,
    ):
        if field_level.ignore == validate_pb.Ignore.ALWAYS:
            return None
        type_case = _which_type(field_level)
        kw = {"for_items": for_items, "force_ignore_empty": force_ignore_empty}
        if type_case is None:
            return FieldRules(self._env, self._bridge, field, field_level, **kw)
        if type_case == "duration":
            check_field_type(field, 0, "google.protobuf.Duration")
            return FieldRules(self._env, self._bridge, field, field_level, **kw)
        if type_case == "field_mask":
            check_field_type(field, 0, "google.protobuf.FieldMask")
            return FieldRules(self._env, self._bridge, field, field_level, **kw)
        if type_case == "timestamp":
            check_field_type(field, 0, "google.protobuf.Timestamp")
            return FieldRules(self._env, self._bridge, field, field_level, **kw)
        if type_case == "enum":
            check_field_type(field, descriptor.FieldDescriptor.TYPE_ENUM)
            return EnumRules(self._env, self._bridge, field, field_level, **kw)
        if type_case == "bool":
            check_field_type(field, descriptor.FieldDescriptor.TYPE_BOOL, "google.protobuf.BoolValue")
            return FieldRules(self._env, self._bridge, field, field_level, **kw)
        if type_case == "bytes":
            check_field_type(field, descriptor.FieldDescriptor.TYPE_BYTES, "google.protobuf.BytesValue")
            return FieldRules(self._env, self._bridge, field, field_level, **kw)
        if type_case == "fixed32":
            check_field_type(field, descriptor.FieldDescriptor.TYPE_FIXED32)
            return FieldRules(self._env, self._bridge, field, field_level, **kw)
        if type_case == "fixed64":
            check_field_type(field, descriptor.FieldDescriptor.TYPE_FIXED64)
            return FieldRules(self._env, self._bridge, field, field_level, **kw)
        if type_case == "float":
            check_field_type(field, descriptor.FieldDescriptor.TYPE_FLOAT, "google.protobuf.FloatValue")
            return FieldRules(self._env, self._bridge, field, field_level, **kw)
        if type_case == "double":
            check_field_type(field, descriptor.FieldDescriptor.TYPE_DOUBLE, "google.protobuf.DoubleValue")
            return FieldRules(self._env, self._bridge, field, field_level, **kw)
        if type_case == "int32":
            check_field_type(field, descriptor.FieldDescriptor.TYPE_INT32, "google.protobuf.Int32Value")
            return FieldRules(self._env, self._bridge, field, field_level, **kw)
        if type_case == "int64":
            check_field_type(field, descriptor.FieldDescriptor.TYPE_INT64, "google.protobuf.Int64Value")
            return FieldRules(self._env, self._bridge, field, field_level, **kw)
        if type_case == "sfixed32":
            check_field_type(field, descriptor.FieldDescriptor.TYPE_SFIXED32)
            return FieldRules(self._env, self._bridge, field, field_level, **kw)
        if type_case == "sfixed64":
            check_field_type(field, descriptor.FieldDescriptor.TYPE_SFIXED64)
            return FieldRules(self._env, self._bridge, field, field_level, **kw)
        if type_case == "sint32":
            check_field_type(field, descriptor.FieldDescriptor.TYPE_SINT32)
            return FieldRules(self._env, self._bridge, field, field_level, **kw)
        if type_case == "sint64":
            check_field_type(field, descriptor.FieldDescriptor.TYPE_SINT64)
            return FieldRules(self._env, self._bridge, field, field_level, **kw)
        if type_case == "uint32":
            check_field_type(field, descriptor.FieldDescriptor.TYPE_UINT32, "google.protobuf.UInt32Value")
            return FieldRules(self._env, self._bridge, field, field_level, **kw)
        if type_case == "uint64":
            check_field_type(field, descriptor.FieldDescriptor.TYPE_UINT64, "google.protobuf.UInt64Value")
            return FieldRules(self._env, self._bridge, field, field_level, **kw)
        if type_case == "string":
            check_field_type(field, descriptor.FieldDescriptor.TYPE_STRING, "google.protobuf.StringValue")
            return FieldRules(self._env, self._bridge, field, field_level, **kw)
        if type_case == "any":
            check_field_type(field, 0, "google.protobuf.Any")
            return AnyRules(self._env, self._bridge, field, field_level)
        msg = f"unknown rule type {type_case!r}"
        raise CompilationError(msg)

    def _new_field_rule(
        self,
        field: descriptor.FieldDescriptor,
        field_level: typing.Any,
        *,
        force_ignore_empty: bool = False,
    ) -> FieldRules:
        if not _is_repeated(field):
            return self._new_scalar_field_rule(field, field_level, force_ignore_empty=force_ignore_empty)
        type_case = _which_type(field_level)
        if field.message_type is not None and field.message_type.GetOptions().map_entry:
            map_rules = field_level.type.value if type_case == "map" else None
            key_rules = None
            value_rules = None
            if map_rules is not None and map_rules.keys is not None:
                key_field = field.message_type.fields_by_name["key"]
                key_rules = self._new_scalar_field_rule(key_field, map_rules.keys, for_items=True)
            if map_rules is not None and map_rules.values is not None:
                value_field = field.message_type.fields_by_name["value"]
                value_rules = self._new_scalar_field_rule(value_field, map_rules.values, for_items=True)
            return MapRules(self._env, self._bridge, field, field_level, key_rules, value_rules)
        item_rule = None
        rep_rules = field_level.type.value if type_case == "repeated" else None
        if rep_rules is not None and rep_rules.items is not None:
            item_rule = self._new_scalar_field_rule(field, rep_rules.items)
        return RepeatedRules(self._env, self._bridge, field, field_level, item_rule)

    def _new_rules(self, pb_desc: protobuf.DescMessage) -> list[Rules]:
        gdesc = typing.cast(descriptor.Descriptor, self._bridge.google_class(pb_desc).DESCRIPTOR)
        result: list[Rules] = []
        all_msg_oneof_fields: set[str] = set()

        msg_opts = pb_desc.proto.options
        if msg_opts is not None and validate_pb.ext_message in msg_opts:
            message_level: typing.Any = msg_opts[validate_pb.ext_message]
            for oneof in message_level.oneof:
                all_msg_oneof_fields.update(oneof.fields)
            if rule := self._new_message_rule(message_level, gdesc):
                result.append(rule)

        pb_oneofs = {o.name: o for o in pb_desc.oneofs}
        for goneof in gdesc.oneofs:
            pb_oneof = pb_oneofs.get(goneof.name)
            if pb_oneof is None:
                continue
            oneof_opts = pb_oneof.proto.options
            if oneof_opts is not None and validate_pb.ext_oneof in oneof_opts:
                result.append(OneofRules(goneof, oneof_opts[validate_pb.ext_oneof]))

        ignore_field = _spec_field(validate_pb.FieldRules, "ignore")
        for gfield in gdesc.fields:
            pb_field = pb_desc._fields_by_name.get(gfield.name)
            field_level: typing.Any = None
            if pb_field is not None:
                field_opts = pb_field.proto.options
                if field_opts is not None and validate_pb.ext_field in field_opts:
                    field_level = field_opts[validate_pb.ext_field]
            if field_level is not None:
                # A field in a message-level oneof rule that does not set its own
                # ignore behaviour is treated as ignore-if-zero-value.
                force_ignore_empty = ignore_field not in field_level and gfield.name in all_msg_oneof_fields
                if field_level.ignore == validate_pb.Ignore.ALWAYS:
                    continue
                result.append(self._new_field_rule(gfield, field_level, force_ignore_empty=force_ignore_empty))
                if _which_type(field_level) == "repeated":
                    rep: typing.Any = field_level.type.value  # ty: ignore[unresolved-attribute]
                    if rep.items is not None and rep.items.ignore == validate_pb.Ignore.ALWAYS:
                        continue
            if gfield.message_type is None or pb_field is None:
                continue
            sub_desc = _message_child(pb_field)
            if sub_desc is None:
                continue
            if gfield.message_type.GetOptions().map_entry:
                key_field = gfield.message_type.fields_by_name["key"]
                value_field = gfield.message_type.fields_by_name["value"]
                result.append(MapValMsgRule(self, gfield, key_field, value_field, sub_desc))
            elif _is_repeated(gfield):
                result.append(RepeatedMsgRule(self, gfield, sub_desc))
            else:
                result.append(SubMsgRule(self, gfield, sub_desc))
        return result


class SubMsgRule(Rules):
    def __init__(self, factory: RuleFactory, field: descriptor.FieldDescriptor, sub_desc: protobuf.DescMessage):
        self._factory = factory
        self._field = field
        self._sub_desc = sub_desc

    def validate(self, ctx: RuleContext, message: message.Message):
        if not message.HasField(self._field.name):
            return
        rules = self._factory.get(self._sub_desc)
        if not rules:
            return
        val = getattr(message, self._field.name)
        sub_ctx = ctx.sub_context()
        for rule in rules:
            rule.validate(sub_ctx, val)
        if sub_ctx.has_errors():
            sub_ctx.add_field_path_element(_field_to_element(self._field))
            ctx.add_errors(sub_ctx)


class MapValMsgRule(Rules):
    def __init__(
        self,
        factory: RuleFactory,
        field: descriptor.FieldDescriptor,
        key_field: descriptor.FieldDescriptor,
        value_field: descriptor.FieldDescriptor,
        sub_desc: protobuf.DescMessage,
    ):
        self._factory = factory
        self._field = field
        self._key_field = key_field
        self._value_field = value_field
        self._sub_desc = sub_desc

    def validate(self, ctx: RuleContext, message: message.Message):
        val = getattr(message, self._field.name)
        if not val:
            return
        rules = self._factory.get(self._sub_desc)
        if not rules:
            return
        for k, v in val.items():
            sub_ctx = ctx.sub_context()
            for rule in rules:
                rule.validate(sub_ctx, v)
            if sub_ctx.has_errors():
                sub_ctx.add_field_path_element(_map_key_element(self._field, k, self._key_field, self._value_field))
                ctx.add_errors(sub_ctx)


class RepeatedMsgRule(Rules):
    def __init__(self, factory: RuleFactory, field: descriptor.FieldDescriptor, sub_desc: protobuf.DescMessage):
        self._factory = factory
        self._field = field
        self._sub_desc = sub_desc

    def validate(self, ctx: RuleContext, message: message.Message):
        val = getattr(message, self._field.name)
        if not val:
            return
        rules = self._factory.get(self._sub_desc)
        if not rules:
            return
        for idx, item in enumerate(val):
            sub_ctx = ctx.sub_context()
            for rule in rules:
                rule.validate(sub_ctx, item)
            if sub_ctx.has_errors():
                sub_ctx.add_field_path_element(_indexed_field_element(self._field, idx))
                ctx.add_errors(sub_ctx)
