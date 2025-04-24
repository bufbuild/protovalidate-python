# Copyright 2023-2025 Buf Technologies, Inc.
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

from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Enum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ENUM_UNSPECIFIED: _ClassVar[Enum]
    ENUM_ONE: _ClassVar[Enum]
ENUM_UNSPECIFIED: Enum
ENUM_ONE: Enum

class NoExpressions(_message.Message):
    __slots__ = ("a", "b", "c")
    class Nested(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    A_FIELD_NUMBER: _ClassVar[int]
    B_FIELD_NUMBER: _ClassVar[int]
    C_FIELD_NUMBER: _ClassVar[int]
    a: int
    b: Enum
    c: NoExpressions.Nested
    def __init__(self, a: _Optional[int] = ..., b: _Optional[_Union[Enum, str]] = ..., c: _Optional[_Union[NoExpressions.Nested, _Mapping]] = ...) -> None: ...

class MessageExpressions(_message.Message):
    __slots__ = ("a", "b", "c", "d", "e", "f")
    class Nested(_message.Message):
        __slots__ = ("a", "b")
        A_FIELD_NUMBER: _ClassVar[int]
        B_FIELD_NUMBER: _ClassVar[int]
        a: int
        b: int
        def __init__(self, a: _Optional[int] = ..., b: _Optional[int] = ...) -> None: ...
    A_FIELD_NUMBER: _ClassVar[int]
    B_FIELD_NUMBER: _ClassVar[int]
    C_FIELD_NUMBER: _ClassVar[int]
    D_FIELD_NUMBER: _ClassVar[int]
    E_FIELD_NUMBER: _ClassVar[int]
    F_FIELD_NUMBER: _ClassVar[int]
    a: int
    b: int
    c: Enum
    d: Enum
    e: MessageExpressions.Nested
    f: MessageExpressions.Nested
    def __init__(self, a: _Optional[int] = ..., b: _Optional[int] = ..., c: _Optional[_Union[Enum, str]] = ..., d: _Optional[_Union[Enum, str]] = ..., e: _Optional[_Union[MessageExpressions.Nested, _Mapping]] = ..., f: _Optional[_Union[MessageExpressions.Nested, _Mapping]] = ...) -> None: ...

class MissingField(_message.Message):
    __slots__ = ("a",)
    A_FIELD_NUMBER: _ClassVar[int]
    a: int
    def __init__(self, a: _Optional[int] = ...) -> None: ...

class IncorrectType(_message.Message):
    __slots__ = ("a",)
    A_FIELD_NUMBER: _ClassVar[int]
    a: int
    def __init__(self, a: _Optional[int] = ...) -> None: ...

class DynRuntimeError(_message.Message):
    __slots__ = ("a",)
    A_FIELD_NUMBER: _ClassVar[int]
    a: int
    def __init__(self, a: _Optional[int] = ...) -> None: ...

class NowEqualsNow(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class FieldExpressionMultipleScalar(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class FieldExpressionNestedScalar(_message.Message):
    __slots__ = ("nested",)
    NESTED_FIELD_NUMBER: _ClassVar[int]
    nested: FieldExpressionScalar
    def __init__(self, nested: _Optional[_Union[FieldExpressionScalar, _Mapping]] = ...) -> None: ...

class FieldExpressionOptionalScalar(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class FieldExpressionScalar(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class FieldExpressionEnum(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: Enum
    def __init__(self, val: _Optional[_Union[Enum, str]] = ...) -> None: ...

class FieldExpressionMessage(_message.Message):
    __slots__ = ("val",)
    class Msg(_message.Message):
        __slots__ = ("a",)
        A_FIELD_NUMBER: _ClassVar[int]
        a: int
        def __init__(self, a: _Optional[int] = ...) -> None: ...
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: FieldExpressionMessage.Msg
    def __init__(self, val: _Optional[_Union[FieldExpressionMessage.Msg, _Mapping]] = ...) -> None: ...

class FieldExpressionMapInt32(_message.Message):
    __slots__ = ("val",)
    class ValEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _containers.ScalarMap[int, int]
    def __init__(self, val: _Optional[_Mapping[int, int]] = ...) -> None: ...

class FieldExpressionMapInt64(_message.Message):
    __slots__ = ("val",)
    class ValEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _containers.ScalarMap[int, int]
    def __init__(self, val: _Optional[_Mapping[int, int]] = ...) -> None: ...

class FieldExpressionMapUint32(_message.Message):
    __slots__ = ("val",)
    class ValEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _containers.ScalarMap[int, int]
    def __init__(self, val: _Optional[_Mapping[int, int]] = ...) -> None: ...

class FieldExpressionMapUint64(_message.Message):
    __slots__ = ("val",)
    class ValEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _containers.ScalarMap[int, int]
    def __init__(self, val: _Optional[_Mapping[int, int]] = ...) -> None: ...

class FieldExpressionMapBool(_message.Message):
    __slots__ = ("val",)
    class ValEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: bool
        value: bool
        def __init__(self, key: bool = ..., value: bool = ...) -> None: ...
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _containers.ScalarMap[bool, bool]
    def __init__(self, val: _Optional[_Mapping[bool, bool]] = ...) -> None: ...

class FieldExpressionMapString(_message.Message):
    __slots__ = ("val",)
    class ValEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _containers.ScalarMap[str, str]
    def __init__(self, val: _Optional[_Mapping[str, str]] = ...) -> None: ...

class FieldExpressionMapEnum(_message.Message):
    __slots__ = ("val",)
    class ValEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: Enum
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[Enum, str]] = ...) -> None: ...
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _containers.ScalarMap[int, Enum]
    def __init__(self, val: _Optional[_Mapping[int, Enum]] = ...) -> None: ...

class FieldExpressionMapMessage(_message.Message):
    __slots__ = ("val",)
    class ValEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: FieldExpressionMapMessage.Msg
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[FieldExpressionMapMessage.Msg, _Mapping]] = ...) -> None: ...
    class Msg(_message.Message):
        __slots__ = ("a",)
        A_FIELD_NUMBER: _ClassVar[int]
        a: int
        def __init__(self, a: _Optional[int] = ...) -> None: ...
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _containers.MessageMap[int, FieldExpressionMapMessage.Msg]
    def __init__(self, val: _Optional[_Mapping[int, FieldExpressionMapMessage.Msg]] = ...) -> None: ...

class FieldExpressionMapKeys(_message.Message):
    __slots__ = ("val",)
    class ValEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _containers.ScalarMap[int, int]
    def __init__(self, val: _Optional[_Mapping[int, int]] = ...) -> None: ...

class FieldExpressionMapScalarValues(_message.Message):
    __slots__ = ("val",)
    class ValEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _containers.ScalarMap[int, int]
    def __init__(self, val: _Optional[_Mapping[int, int]] = ...) -> None: ...

class FieldExpressionMapEnumValues(_message.Message):
    __slots__ = ("val",)
    class ValEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: Enum
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[Enum, str]] = ...) -> None: ...
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _containers.ScalarMap[int, Enum]
    def __init__(self, val: _Optional[_Mapping[int, Enum]] = ...) -> None: ...

class FieldExpressionMapMessageValues(_message.Message):
    __slots__ = ("val",)
    class ValEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: FieldExpressionMapMessageValues.Msg
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[FieldExpressionMapMessageValues.Msg, _Mapping]] = ...) -> None: ...
    class Msg(_message.Message):
        __slots__ = ("a",)
        A_FIELD_NUMBER: _ClassVar[int]
        a: int
        def __init__(self, a: _Optional[int] = ...) -> None: ...
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _containers.MessageMap[int, FieldExpressionMapMessageValues.Msg]
    def __init__(self, val: _Optional[_Mapping[int, FieldExpressionMapMessageValues.Msg]] = ...) -> None: ...

class FieldExpressionRepeatedScalar(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, val: _Optional[_Iterable[int]] = ...) -> None: ...

class FieldExpressionRepeatedEnum(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _containers.RepeatedScalarFieldContainer[Enum]
    def __init__(self, val: _Optional[_Iterable[_Union[Enum, str]]] = ...) -> None: ...

class FieldExpressionRepeatedMessage(_message.Message):
    __slots__ = ("val",)
    class Msg(_message.Message):
        __slots__ = ("a",)
        A_FIELD_NUMBER: _ClassVar[int]
        a: int
        def __init__(self, a: _Optional[int] = ...) -> None: ...
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _containers.RepeatedCompositeFieldContainer[FieldExpressionRepeatedMessage.Msg]
    def __init__(self, val: _Optional[_Iterable[_Union[FieldExpressionRepeatedMessage.Msg, _Mapping]]] = ...) -> None: ...

class FieldExpressionRepeatedScalarItems(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, val: _Optional[_Iterable[int]] = ...) -> None: ...

class FieldExpressionRepeatedEnumItems(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _containers.RepeatedScalarFieldContainer[Enum]
    def __init__(self, val: _Optional[_Iterable[_Union[Enum, str]]] = ...) -> None: ...

class FieldExpressionRepeatedMessageItems(_message.Message):
    __slots__ = ("val",)
    class Msg(_message.Message):
        __slots__ = ("a",)
        A_FIELD_NUMBER: _ClassVar[int]
        a: int
        def __init__(self, a: _Optional[int] = ...) -> None: ...
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _containers.RepeatedCompositeFieldContainer[FieldExpressionRepeatedMessageItems.Msg]
    def __init__(self, val: _Optional[_Iterable[_Union[FieldExpressionRepeatedMessageItems.Msg, _Mapping]]] = ...) -> None: ...
