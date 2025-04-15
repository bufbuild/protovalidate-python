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
from google.protobuf import any_pb2 as _any_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ComplexTestEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    COMPLEX_TEST_ENUM_UNSPECIFIED: _ClassVar[ComplexTestEnum]
    COMPLEX_TEST_ENUM_ONE: _ClassVar[ComplexTestEnum]
    COMPLEX_TEST_ENUM_TWO: _ClassVar[ComplexTestEnum]
COMPLEX_TEST_ENUM_UNSPECIFIED: ComplexTestEnum
COMPLEX_TEST_ENUM_ONE: ComplexTestEnum
COMPLEX_TEST_ENUM_TWO: ComplexTestEnum

class ComplexTestMsg(_message.Message):
    __slots__ = ("const", "nested", "int_const", "bool_const", "float_val", "dur_val", "ts_val", "another", "float_const", "double_in", "enum_const", "any_val", "rep_ts_val", "map_val", "bytes_val", "x", "y")
    class MapValEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: str
        def __init__(self, key: _Optional[int] = ..., value: _Optional[str] = ...) -> None: ...
    CONST_FIELD_NUMBER: _ClassVar[int]
    NESTED_FIELD_NUMBER: _ClassVar[int]
    INT_CONST_FIELD_NUMBER: _ClassVar[int]
    BOOL_CONST_FIELD_NUMBER: _ClassVar[int]
    FLOAT_VAL_FIELD_NUMBER: _ClassVar[int]
    DUR_VAL_FIELD_NUMBER: _ClassVar[int]
    TS_VAL_FIELD_NUMBER: _ClassVar[int]
    ANOTHER_FIELD_NUMBER: _ClassVar[int]
    FLOAT_CONST_FIELD_NUMBER: _ClassVar[int]
    DOUBLE_IN_FIELD_NUMBER: _ClassVar[int]
    ENUM_CONST_FIELD_NUMBER: _ClassVar[int]
    ANY_VAL_FIELD_NUMBER: _ClassVar[int]
    REP_TS_VAL_FIELD_NUMBER: _ClassVar[int]
    MAP_VAL_FIELD_NUMBER: _ClassVar[int]
    BYTES_VAL_FIELD_NUMBER: _ClassVar[int]
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    const: str
    nested: ComplexTestMsg
    int_const: int
    bool_const: bool
    float_val: _wrappers_pb2.FloatValue
    dur_val: _duration_pb2.Duration
    ts_val: _timestamp_pb2.Timestamp
    another: ComplexTestMsg
    float_const: float
    double_in: float
    enum_const: ComplexTestEnum
    any_val: _any_pb2.Any
    rep_ts_val: _containers.RepeatedCompositeFieldContainer[_timestamp_pb2.Timestamp]
    map_val: _containers.ScalarMap[int, str]
    bytes_val: bytes
    x: str
    y: int
    def __init__(self, const: _Optional[str] = ..., nested: _Optional[_Union[ComplexTestMsg, _Mapping]] = ..., int_const: _Optional[int] = ..., bool_const: bool = ..., float_val: _Optional[_Union[_wrappers_pb2.FloatValue, _Mapping]] = ..., dur_val: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., ts_val: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., another: _Optional[_Union[ComplexTestMsg, _Mapping]] = ..., float_const: _Optional[float] = ..., double_in: _Optional[float] = ..., enum_const: _Optional[_Union[ComplexTestEnum, str]] = ..., any_val: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., rep_ts_val: _Optional[_Iterable[_Union[_timestamp_pb2.Timestamp, _Mapping]]] = ..., map_val: _Optional[_Mapping[int, str]] = ..., bytes_val: _Optional[bytes] = ..., x: _Optional[str] = ..., y: _Optional[int] = ...) -> None: ...

class KitchenSinkMessage(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: ComplexTestMsg
    def __init__(self, val: _Optional[_Union[ComplexTestMsg, _Mapping]] = ...) -> None: ...
