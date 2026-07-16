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

from ...buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BenchEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BENCH_ENUM_UNSPECIFIED: _ClassVar[BenchEnum]
    BENCH_ENUM_ONE: _ClassVar[BenchEnum]
    BENCH_ENUM_TWO: _ClassVar[BenchEnum]
BENCH_ENUM_UNSPECIFIED: BenchEnum
BENCH_ENUM_ONE: BenchEnum
BENCH_ENUM_TWO: BenchEnum

class BenchScalar(_message.Message):
    __slots__ = ("x",)
    X_FIELD_NUMBER: _ClassVar[int]
    x: int
    def __init__(self, x: _Optional[int] = ...) -> None: ...

class BenchRepeatedScalar(_message.Message):
    __slots__ = ("x",)
    X_FIELD_NUMBER: _ClassVar[int]
    x: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, x: _Optional[_Iterable[int]] = ...) -> None: ...

class BenchRepeatedMessage(_message.Message):
    __slots__ = ("x",)
    X_FIELD_NUMBER: _ClassVar[int]
    x: _containers.RepeatedCompositeFieldContainer[BenchScalar]
    def __init__(self, x: _Optional[_Iterable[_Union[BenchScalar, _Mapping]]] = ...) -> None: ...

class BenchRepeatedScalarUnique(_message.Message):
    __slots__ = ("x",)
    X_FIELD_NUMBER: _ClassVar[int]
    x: _containers.RepeatedScalarFieldContainer[float]
    def __init__(self, x: _Optional[_Iterable[float]] = ...) -> None: ...

class BenchRepeatedBytesUnique(_message.Message):
    __slots__ = ("x",)
    X_FIELD_NUMBER: _ClassVar[int]
    x: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, x: _Optional[_Iterable[bytes]] = ...) -> None: ...

class BenchMap(_message.Message):
    __slots__ = ("entries",)
    class EntriesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    entries: _containers.ScalarMap[str, str]
    def __init__(self, entries: _Optional[_Mapping[str, str]] = ...) -> None: ...

class BenchComplexSchema(_message.Message):
    __slots__ = ("s1", "s2", "i32", "i64", "u32", "u64", "si32", "si64", "f32", "f64", "sf32", "sf64", "fl", "db", "bl", "by", "nested", "self_ref", "rep_str", "rep_i32", "rep_bytes", "rep_msg", "map_str_str", "map_i32_i64", "map_u64_bool", "map_str_bytes", "map_str_msg", "map_i64_msg", "enum_field", "oneof_str", "oneof_i32", "oneof_msg")
    class MapStrStrEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class MapI32I64Entry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class MapU64BoolEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: bool
        def __init__(self, key: _Optional[int] = ..., value: bool = ...) -> None: ...
    class MapStrBytesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: bytes
        def __init__(self, key: _Optional[str] = ..., value: _Optional[bytes] = ...) -> None: ...
    class MapStrMsgEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: BenchScalar
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[BenchScalar, _Mapping]] = ...) -> None: ...
    class MapI64MsgEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: BenchScalar
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[BenchScalar, _Mapping]] = ...) -> None: ...
    S1_FIELD_NUMBER: _ClassVar[int]
    S2_FIELD_NUMBER: _ClassVar[int]
    I32_FIELD_NUMBER: _ClassVar[int]
    I64_FIELD_NUMBER: _ClassVar[int]
    U32_FIELD_NUMBER: _ClassVar[int]
    U64_FIELD_NUMBER: _ClassVar[int]
    SI32_FIELD_NUMBER: _ClassVar[int]
    SI64_FIELD_NUMBER: _ClassVar[int]
    F32_FIELD_NUMBER: _ClassVar[int]
    F64_FIELD_NUMBER: _ClassVar[int]
    SF32_FIELD_NUMBER: _ClassVar[int]
    SF64_FIELD_NUMBER: _ClassVar[int]
    FL_FIELD_NUMBER: _ClassVar[int]
    DB_FIELD_NUMBER: _ClassVar[int]
    BL_FIELD_NUMBER: _ClassVar[int]
    BY_FIELD_NUMBER: _ClassVar[int]
    NESTED_FIELD_NUMBER: _ClassVar[int]
    SELF_REF_FIELD_NUMBER: _ClassVar[int]
    REP_STR_FIELD_NUMBER: _ClassVar[int]
    REP_I32_FIELD_NUMBER: _ClassVar[int]
    REP_BYTES_FIELD_NUMBER: _ClassVar[int]
    REP_MSG_FIELD_NUMBER: _ClassVar[int]
    MAP_STR_STR_FIELD_NUMBER: _ClassVar[int]
    MAP_I32_I64_FIELD_NUMBER: _ClassVar[int]
    MAP_U64_BOOL_FIELD_NUMBER: _ClassVar[int]
    MAP_STR_BYTES_FIELD_NUMBER: _ClassVar[int]
    MAP_STR_MSG_FIELD_NUMBER: _ClassVar[int]
    MAP_I64_MSG_FIELD_NUMBER: _ClassVar[int]
    ENUM_FIELD_FIELD_NUMBER: _ClassVar[int]
    ONEOF_STR_FIELD_NUMBER: _ClassVar[int]
    ONEOF_I32_FIELD_NUMBER: _ClassVar[int]
    ONEOF_MSG_FIELD_NUMBER: _ClassVar[int]
    s1: str
    s2: str
    i32: int
    i64: int
    u32: int
    u64: int
    si32: int
    si64: int
    f32: int
    f64: int
    sf32: int
    sf64: int
    fl: float
    db: float
    bl: bool
    by: bytes
    nested: BenchScalar
    self_ref: BenchComplexSchema
    rep_str: _containers.RepeatedScalarFieldContainer[str]
    rep_i32: _containers.RepeatedScalarFieldContainer[int]
    rep_bytes: _containers.RepeatedScalarFieldContainer[bytes]
    rep_msg: _containers.RepeatedCompositeFieldContainer[BenchScalar]
    map_str_str: _containers.ScalarMap[str, str]
    map_i32_i64: _containers.ScalarMap[int, int]
    map_u64_bool: _containers.ScalarMap[int, bool]
    map_str_bytes: _containers.ScalarMap[str, bytes]
    map_str_msg: _containers.MessageMap[str, BenchScalar]
    map_i64_msg: _containers.MessageMap[int, BenchScalar]
    enum_field: BenchEnum
    oneof_str: str
    oneof_i32: int
    oneof_msg: BenchScalar
    def __init__(self, s1: _Optional[str] = ..., s2: _Optional[str] = ..., i32: _Optional[int] = ..., i64: _Optional[int] = ..., u32: _Optional[int] = ..., u64: _Optional[int] = ..., si32: _Optional[int] = ..., si64: _Optional[int] = ..., f32: _Optional[int] = ..., f64: _Optional[int] = ..., sf32: _Optional[int] = ..., sf64: _Optional[int] = ..., fl: _Optional[float] = ..., db: _Optional[float] = ..., bl: bool = ..., by: _Optional[bytes] = ..., nested: _Optional[_Union[BenchScalar, _Mapping]] = ..., self_ref: _Optional[_Union[BenchComplexSchema, _Mapping]] = ..., rep_str: _Optional[_Iterable[str]] = ..., rep_i32: _Optional[_Iterable[int]] = ..., rep_bytes: _Optional[_Iterable[bytes]] = ..., rep_msg: _Optional[_Iterable[_Union[BenchScalar, _Mapping]]] = ..., map_str_str: _Optional[_Mapping[str, str]] = ..., map_i32_i64: _Optional[_Mapping[int, int]] = ..., map_u64_bool: _Optional[_Mapping[int, bool]] = ..., map_str_bytes: _Optional[_Mapping[str, bytes]] = ..., map_str_msg: _Optional[_Mapping[str, BenchScalar]] = ..., map_i64_msg: _Optional[_Mapping[int, BenchScalar]] = ..., enum_field: _Optional[_Union[BenchEnum, str]] = ..., oneof_str: _Optional[str] = ..., oneof_i32: _Optional[int] = ..., oneof_msg: _Optional[_Union[BenchScalar, _Mapping]] = ...) -> None: ...
