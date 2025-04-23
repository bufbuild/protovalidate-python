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

from buf.validate.conformance.cases.other_package import embed_pb2 as _embed_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import any_pb2 as _any_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AnEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AN_ENUM_UNSPECIFIED: _ClassVar[AnEnum]
    AN_ENUM_X: _ClassVar[AnEnum]
    AN_ENUM_Y: _ClassVar[AnEnum]
AN_ENUM_UNSPECIFIED: AnEnum
AN_ENUM_X: AnEnum
AN_ENUM_Y: AnEnum

class Embed(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class RepeatedNone(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, val: _Optional[_Iterable[int]] = ...) -> None: ...

class RepeatedEmbedNone(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _containers.RepeatedCompositeFieldContainer[Embed]
    def __init__(self, val: _Optional[_Iterable[_Union[Embed, _Mapping]]] = ...) -> None: ...

class RepeatedEmbedCrossPackageNone(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _containers.RepeatedCompositeFieldContainer[_embed_pb2.Embed]
    def __init__(self, val: _Optional[_Iterable[_Union[_embed_pb2.Embed, _Mapping]]] = ...) -> None: ...

class RepeatedMin(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _containers.RepeatedCompositeFieldContainer[Embed]
    def __init__(self, val: _Optional[_Iterable[_Union[Embed, _Mapping]]] = ...) -> None: ...

class RepeatedMax(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _containers.RepeatedScalarFieldContainer[float]
    def __init__(self, val: _Optional[_Iterable[float]] = ...) -> None: ...

class RepeatedMinMax(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, val: _Optional[_Iterable[int]] = ...) -> None: ...

class RepeatedExact(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, val: _Optional[_Iterable[int]] = ...) -> None: ...

class RepeatedUnique(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, val: _Optional[_Iterable[str]] = ...) -> None: ...

class RepeatedNotUnique(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, val: _Optional[_Iterable[str]] = ...) -> None: ...

class RepeatedMultipleUnique(_message.Message):
    __slots__ = ("a", "b")
    A_FIELD_NUMBER: _ClassVar[int]
    B_FIELD_NUMBER: _ClassVar[int]
    a: _containers.RepeatedScalarFieldContainer[str]
    b: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, a: _Optional[_Iterable[str]] = ..., b: _Optional[_Iterable[int]] = ...) -> None: ...

class RepeatedItemRule(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _containers.RepeatedScalarFieldContainer[float]
    def __init__(self, val: _Optional[_Iterable[float]] = ...) -> None: ...

class RepeatedItemPattern(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, val: _Optional[_Iterable[str]] = ...) -> None: ...

class RepeatedEmbedSkip(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _containers.RepeatedCompositeFieldContainer[Embed]
    def __init__(self, val: _Optional[_Iterable[_Union[Embed, _Mapping]]] = ...) -> None: ...

class RepeatedItemIn(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, val: _Optional[_Iterable[str]] = ...) -> None: ...

class RepeatedItemNotIn(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, val: _Optional[_Iterable[str]] = ...) -> None: ...

class RepeatedEnumIn(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _containers.RepeatedScalarFieldContainer[AnEnum]
    def __init__(self, val: _Optional[_Iterable[_Union[AnEnum, str]]] = ...) -> None: ...

class RepeatedEnumNotIn(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _containers.RepeatedScalarFieldContainer[AnEnum]
    def __init__(self, val: _Optional[_Iterable[_Union[AnEnum, str]]] = ...) -> None: ...

class RepeatedEmbeddedEnumIn(_message.Message):
    __slots__ = ("val",)
    class AnotherInEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ANOTHER_IN_ENUM_UNSPECIFIED: _ClassVar[RepeatedEmbeddedEnumIn.AnotherInEnum]
        ANOTHER_IN_ENUM_A: _ClassVar[RepeatedEmbeddedEnumIn.AnotherInEnum]
        ANOTHER_IN_ENUM_B: _ClassVar[RepeatedEmbeddedEnumIn.AnotherInEnum]
    ANOTHER_IN_ENUM_UNSPECIFIED: RepeatedEmbeddedEnumIn.AnotherInEnum
    ANOTHER_IN_ENUM_A: RepeatedEmbeddedEnumIn.AnotherInEnum
    ANOTHER_IN_ENUM_B: RepeatedEmbeddedEnumIn.AnotherInEnum
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _containers.RepeatedScalarFieldContainer[RepeatedEmbeddedEnumIn.AnotherInEnum]
    def __init__(self, val: _Optional[_Iterable[_Union[RepeatedEmbeddedEnumIn.AnotherInEnum, str]]] = ...) -> None: ...

class RepeatedEmbeddedEnumNotIn(_message.Message):
    __slots__ = ("val",)
    class AnotherNotInEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ANOTHER_NOT_IN_ENUM_UNSPECIFIED: _ClassVar[RepeatedEmbeddedEnumNotIn.AnotherNotInEnum]
        ANOTHER_NOT_IN_ENUM_A: _ClassVar[RepeatedEmbeddedEnumNotIn.AnotherNotInEnum]
        ANOTHER_NOT_IN_ENUM_B: _ClassVar[RepeatedEmbeddedEnumNotIn.AnotherNotInEnum]
    ANOTHER_NOT_IN_ENUM_UNSPECIFIED: RepeatedEmbeddedEnumNotIn.AnotherNotInEnum
    ANOTHER_NOT_IN_ENUM_A: RepeatedEmbeddedEnumNotIn.AnotherNotInEnum
    ANOTHER_NOT_IN_ENUM_B: RepeatedEmbeddedEnumNotIn.AnotherNotInEnum
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _containers.RepeatedScalarFieldContainer[RepeatedEmbeddedEnumNotIn.AnotherNotInEnum]
    def __init__(self, val: _Optional[_Iterable[_Union[RepeatedEmbeddedEnumNotIn.AnotherNotInEnum, str]]] = ...) -> None: ...

class RepeatedAnyIn(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _containers.RepeatedCompositeFieldContainer[_any_pb2.Any]
    def __init__(self, val: _Optional[_Iterable[_Union[_any_pb2.Any, _Mapping]]] = ...) -> None: ...

class RepeatedAnyNotIn(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _containers.RepeatedCompositeFieldContainer[_any_pb2.Any]
    def __init__(self, val: _Optional[_Iterable[_Union[_any_pb2.Any, _Mapping]]] = ...) -> None: ...

class RepeatedMinAndItemLen(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, val: _Optional[_Iterable[str]] = ...) -> None: ...

class RepeatedMinAndMaxItemLen(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, val: _Optional[_Iterable[str]] = ...) -> None: ...

class RepeatedDuration(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _containers.RepeatedCompositeFieldContainer[_duration_pb2.Duration]
    def __init__(self, val: _Optional[_Iterable[_Union[_duration_pb2.Duration, _Mapping]]] = ...) -> None: ...

class RepeatedExactIgnore(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, val: _Optional[_Iterable[int]] = ...) -> None: ...
