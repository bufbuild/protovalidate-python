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

from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

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

class FieldExpressions(_message.Message):
    __slots__ = ("a", "b", "c")
    class Nested(_message.Message):
        __slots__ = ("a",)
        A_FIELD_NUMBER: _ClassVar[int]
        a: int
        def __init__(self, a: _Optional[int] = ...) -> None: ...
    A_FIELD_NUMBER: _ClassVar[int]
    B_FIELD_NUMBER: _ClassVar[int]
    C_FIELD_NUMBER: _ClassVar[int]
    a: int
    b: Enum
    c: FieldExpressions.Nested
    def __init__(self, a: _Optional[int] = ..., b: _Optional[_Union[Enum, str]] = ..., c: _Optional[_Union[FieldExpressions.Nested, _Mapping]] = ...) -> None: ...

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
