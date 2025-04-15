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
from buf.validate.conformance.cases.yet_another_package import embed2_pb2 as _embed2_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TestEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TEST_ENUM_UNSPECIFIED: _ClassVar[TestEnum]
    TEST_ENUM_ONE: _ClassVar[TestEnum]
    TEST_ENUM_TWO: _ClassVar[TestEnum]

class TestEnumAlias(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TEST_ENUM_ALIAS_UNSPECIFIED: _ClassVar[TestEnumAlias]
    TEST_ENUM_ALIAS_A: _ClassVar[TestEnumAlias]
    TEST_ENUM_ALIAS_B: _ClassVar[TestEnumAlias]
    TEST_ENUM_ALIAS_C: _ClassVar[TestEnumAlias]
    TEST_ENUM_ALIAS_ALPHA: _ClassVar[TestEnumAlias]
    TEST_ENUM_ALIAS_BETA: _ClassVar[TestEnumAlias]
    TEST_ENUM_ALIAS_GAMMA: _ClassVar[TestEnumAlias]
TEST_ENUM_UNSPECIFIED: TestEnum
TEST_ENUM_ONE: TestEnum
TEST_ENUM_TWO: TestEnum
TEST_ENUM_ALIAS_UNSPECIFIED: TestEnumAlias
TEST_ENUM_ALIAS_A: TestEnumAlias
TEST_ENUM_ALIAS_B: TestEnumAlias
TEST_ENUM_ALIAS_C: TestEnumAlias
TEST_ENUM_ALIAS_ALPHA: TestEnumAlias
TEST_ENUM_ALIAS_BETA: TestEnumAlias
TEST_ENUM_ALIAS_GAMMA: TestEnumAlias

class EnumNone(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: TestEnum
    def __init__(self, val: _Optional[_Union[TestEnum, str]] = ...) -> None: ...

class EnumConst(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: TestEnum
    def __init__(self, val: _Optional[_Union[TestEnum, str]] = ...) -> None: ...

class EnumAliasConst(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: TestEnumAlias
    def __init__(self, val: _Optional[_Union[TestEnumAlias, str]] = ...) -> None: ...

class EnumDefined(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: TestEnum
    def __init__(self, val: _Optional[_Union[TestEnum, str]] = ...) -> None: ...

class EnumAliasDefined(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: TestEnumAlias
    def __init__(self, val: _Optional[_Union[TestEnumAlias, str]] = ...) -> None: ...

class EnumIn(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: TestEnum
    def __init__(self, val: _Optional[_Union[TestEnum, str]] = ...) -> None: ...

class EnumAliasIn(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: TestEnumAlias
    def __init__(self, val: _Optional[_Union[TestEnumAlias, str]] = ...) -> None: ...

class EnumNotIn(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: TestEnum
    def __init__(self, val: _Optional[_Union[TestEnum, str]] = ...) -> None: ...

class EnumAliasNotIn(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: TestEnumAlias
    def __init__(self, val: _Optional[_Union[TestEnumAlias, str]] = ...) -> None: ...

class EnumExternal(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _embed_pb2.Embed.Enumerated
    def __init__(self, val: _Optional[_Union[_embed_pb2.Embed.Enumerated, str]] = ...) -> None: ...

class EnumExternal2(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _embed_pb2.Embed.DoubleEmbed.DoubleEnumerated
    def __init__(self, val: _Optional[_Union[_embed_pb2.Embed.DoubleEmbed.DoubleEnumerated, str]] = ...) -> None: ...

class RepeatedEnumDefined(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _containers.RepeatedScalarFieldContainer[TestEnum]
    def __init__(self, val: _Optional[_Iterable[_Union[TestEnum, str]]] = ...) -> None: ...

class RepeatedExternalEnumDefined(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _containers.RepeatedScalarFieldContainer[_embed_pb2.Embed.Enumerated]
    def __init__(self, val: _Optional[_Iterable[_Union[_embed_pb2.Embed.Enumerated, str]]] = ...) -> None: ...

class RepeatedYetAnotherExternalEnumDefined(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _containers.RepeatedScalarFieldContainer[_embed2_pb2.Embed.Enumerated]
    def __init__(self, val: _Optional[_Iterable[_Union[_embed2_pb2.Embed.Enumerated, str]]] = ...) -> None: ...

class MapEnumDefined(_message.Message):
    __slots__ = ("val",)
    class ValEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: TestEnum
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[TestEnum, str]] = ...) -> None: ...
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _containers.ScalarMap[str, TestEnum]
    def __init__(self, val: _Optional[_Mapping[str, TestEnum]] = ...) -> None: ...

class MapExternalEnumDefined(_message.Message):
    __slots__ = ("val",)
    class ValEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _embed_pb2.Embed.Enumerated
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_embed_pb2.Embed.Enumerated, str]] = ...) -> None: ...
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _containers.ScalarMap[str, _embed_pb2.Embed.Enumerated]
    def __init__(self, val: _Optional[_Mapping[str, _embed_pb2.Embed.Enumerated]] = ...) -> None: ...

class EnumInsideOneof(_message.Message):
    __slots__ = ("val", "val2")
    VAL_FIELD_NUMBER: _ClassVar[int]
    VAL2_FIELD_NUMBER: _ClassVar[int]
    val: TestEnum
    val2: TestEnum
    def __init__(self, val: _Optional[_Union[TestEnum, str]] = ..., val2: _Optional[_Union[TestEnum, str]] = ...) -> None: ...

class EnumExample(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: TestEnum
    def __init__(self, val: _Optional[_Union[TestEnum, str]] = ...) -> None: ...
