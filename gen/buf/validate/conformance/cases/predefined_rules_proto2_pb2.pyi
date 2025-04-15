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
FLOAT_ABS_RANGE_PROTO2_FIELD_NUMBER: _ClassVar[int]
float_abs_range_proto2: _descriptor.FieldDescriptor
DOUBLE_ABS_RANGE_PROTO2_FIELD_NUMBER: _ClassVar[int]
double_abs_range_proto2: _descriptor.FieldDescriptor
INT32_ABS_IN_PROTO2_FIELD_NUMBER: _ClassVar[int]
int32_abs_in_proto2: _descriptor.FieldDescriptor
INT64_ABS_IN_PROTO2_FIELD_NUMBER: _ClassVar[int]
int64_abs_in_proto2: _descriptor.FieldDescriptor
UINT32_EVEN_PROTO2_FIELD_NUMBER: _ClassVar[int]
uint32_even_proto2: _descriptor.FieldDescriptor
UINT64_EVEN_PROTO2_FIELD_NUMBER: _ClassVar[int]
uint64_even_proto2: _descriptor.FieldDescriptor
SINT32_EVEN_PROTO2_FIELD_NUMBER: _ClassVar[int]
sint32_even_proto2: _descriptor.FieldDescriptor
SINT64_EVEN_PROTO2_FIELD_NUMBER: _ClassVar[int]
sint64_even_proto2: _descriptor.FieldDescriptor
FIXED32_EVEN_PROTO2_FIELD_NUMBER: _ClassVar[int]
fixed32_even_proto2: _descriptor.FieldDescriptor
FIXED64_EVEN_PROTO2_FIELD_NUMBER: _ClassVar[int]
fixed64_even_proto2: _descriptor.FieldDescriptor
SFIXED32_EVEN_PROTO2_FIELD_NUMBER: _ClassVar[int]
sfixed32_even_proto2: _descriptor.FieldDescriptor
SFIXED64_EVEN_PROTO2_FIELD_NUMBER: _ClassVar[int]
sfixed64_even_proto2: _descriptor.FieldDescriptor
BOOL_FALSE_PROTO2_FIELD_NUMBER: _ClassVar[int]
bool_false_proto2: _descriptor.FieldDescriptor
STRING_VALID_PATH_PROTO2_FIELD_NUMBER: _ClassVar[int]
string_valid_path_proto2: _descriptor.FieldDescriptor
BYTES_VALID_PATH_PROTO2_FIELD_NUMBER: _ClassVar[int]
bytes_valid_path_proto2: _descriptor.FieldDescriptor
ENUM_NON_ZERO_PROTO2_FIELD_NUMBER: _ClassVar[int]
enum_non_zero_proto2: _descriptor.FieldDescriptor
REPEATED_AT_LEAST_FIVE_PROTO2_FIELD_NUMBER: _ClassVar[int]
repeated_at_least_five_proto2: _descriptor.FieldDescriptor
DURATION_TOO_LONG_PROTO2_FIELD_NUMBER: _ClassVar[int]
duration_too_long_proto2: _descriptor.FieldDescriptor
TIMESTAMP_IN_RANGE_PROTO2_FIELD_NUMBER: _ClassVar[int]
timestamp_in_range_proto2: _descriptor.FieldDescriptor

class PredefinedFloatRuleProto2(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: float
    def __init__(self, val: _Optional[float] = ...) -> None: ...

class PredefinedDoubleRuleProto2(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: float
    def __init__(self, val: _Optional[float] = ...) -> None: ...

class PredefinedInt32RuleProto2(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class PredefinedInt64RuleProto2(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class PredefinedUInt32RuleProto2(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class PredefinedUInt64RuleProto2(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class PredefinedSInt32RuleProto2(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class PredefinedSInt64RuleProto2(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class PredefinedFixed32RuleProto2(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class PredefinedFixed64RuleProto2(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class PredefinedSFixed32RuleProto2(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class PredefinedSFixed64RuleProto2(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class PredefinedBoolRuleProto2(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: bool
    def __init__(self, val: bool = ...) -> None: ...

class PredefinedStringRuleProto2(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: str
    def __init__(self, val: _Optional[str] = ...) -> None: ...

class PredefinedBytesRuleProto2(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: bytes
    def __init__(self, val: _Optional[bytes] = ...) -> None: ...

class PredefinedEnumRuleProto2(_message.Message):
    __slots__ = ("val",)
    class EnumProto2(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ENUM_PROTO2_ZERO_UNSPECIFIED: _ClassVar[PredefinedEnumRuleProto2.EnumProto2]
        ENUM_PROTO2_ONE: _ClassVar[PredefinedEnumRuleProto2.EnumProto2]
    ENUM_PROTO2_ZERO_UNSPECIFIED: PredefinedEnumRuleProto2.EnumProto2
    ENUM_PROTO2_ONE: PredefinedEnumRuleProto2.EnumProto2
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: PredefinedEnumRuleProto2.EnumProto2
    def __init__(self, val: _Optional[_Union[PredefinedEnumRuleProto2.EnumProto2, str]] = ...) -> None: ...

class PredefinedRepeatedRuleProto2(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, val: _Optional[_Iterable[int]] = ...) -> None: ...

class PredefinedDurationRuleProto2(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _duration_pb2.Duration
    def __init__(self, val: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...

class PredefinedTimestampRuleProto2(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _timestamp_pb2.Timestamp
    def __init__(self, val: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class PredefinedWrappedFloatRuleProto2(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _wrappers_pb2.FloatValue
    def __init__(self, val: _Optional[_Union[_wrappers_pb2.FloatValue, _Mapping]] = ...) -> None: ...

class PredefinedWrappedDoubleRuleProto2(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _wrappers_pb2.DoubleValue
    def __init__(self, val: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ...) -> None: ...

class PredefinedWrappedInt32RuleProto2(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _wrappers_pb2.Int32Value
    def __init__(self, val: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ...) -> None: ...

class PredefinedWrappedInt64RuleProto2(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _wrappers_pb2.Int64Value
    def __init__(self, val: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ...) -> None: ...

class PredefinedWrappedUInt32RuleProto2(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _wrappers_pb2.UInt32Value
    def __init__(self, val: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ...) -> None: ...

class PredefinedWrappedUInt64RuleProto2(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _wrappers_pb2.UInt64Value
    def __init__(self, val: _Optional[_Union[_wrappers_pb2.UInt64Value, _Mapping]] = ...) -> None: ...

class PredefinedWrappedBoolRuleProto2(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _wrappers_pb2.BoolValue
    def __init__(self, val: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...) -> None: ...

class PredefinedWrappedStringRuleProto2(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _wrappers_pb2.StringValue
    def __init__(self, val: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...) -> None: ...

class PredefinedWrappedBytesRuleProto2(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _wrappers_pb2.BytesValue
    def __init__(self, val: _Optional[_Union[_wrappers_pb2.BytesValue, _Mapping]] = ...) -> None: ...

class PredefinedRepeatedWrappedFloatRuleProto2(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _containers.RepeatedCompositeFieldContainer[_wrappers_pb2.FloatValue]
    def __init__(self, val: _Optional[_Iterable[_Union[_wrappers_pb2.FloatValue, _Mapping]]] = ...) -> None: ...

class PredefinedRepeatedWrappedDoubleRuleProto2(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _containers.RepeatedCompositeFieldContainer[_wrappers_pb2.DoubleValue]
    def __init__(self, val: _Optional[_Iterable[_Union[_wrappers_pb2.DoubleValue, _Mapping]]] = ...) -> None: ...

class PredefinedRepeatedWrappedInt32RuleProto2(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _containers.RepeatedCompositeFieldContainer[_wrappers_pb2.Int32Value]
    def __init__(self, val: _Optional[_Iterable[_Union[_wrappers_pb2.Int32Value, _Mapping]]] = ...) -> None: ...

class PredefinedRepeatedWrappedInt64RuleProto2(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _containers.RepeatedCompositeFieldContainer[_wrappers_pb2.Int64Value]
    def __init__(self, val: _Optional[_Iterable[_Union[_wrappers_pb2.Int64Value, _Mapping]]] = ...) -> None: ...

class PredefinedRepeatedWrappedUInt32RuleProto2(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _containers.RepeatedCompositeFieldContainer[_wrappers_pb2.UInt32Value]
    def __init__(self, val: _Optional[_Iterable[_Union[_wrappers_pb2.UInt32Value, _Mapping]]] = ...) -> None: ...

class PredefinedRepeatedWrappedUInt64RuleProto2(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _containers.RepeatedCompositeFieldContainer[_wrappers_pb2.UInt64Value]
    def __init__(self, val: _Optional[_Iterable[_Union[_wrappers_pb2.UInt64Value, _Mapping]]] = ...) -> None: ...

class PredefinedRepeatedWrappedBoolRuleProto2(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _containers.RepeatedCompositeFieldContainer[_wrappers_pb2.BoolValue]
    def __init__(self, val: _Optional[_Iterable[_Union[_wrappers_pb2.BoolValue, _Mapping]]] = ...) -> None: ...

class PredefinedRepeatedWrappedStringRuleProto2(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _containers.RepeatedCompositeFieldContainer[_wrappers_pb2.StringValue]
    def __init__(self, val: _Optional[_Iterable[_Union[_wrappers_pb2.StringValue, _Mapping]]] = ...) -> None: ...

class PredefinedRepeatedWrappedBytesRuleProto2(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _containers.RepeatedCompositeFieldContainer[_wrappers_pb2.BytesValue]
    def __init__(self, val: _Optional[_Iterable[_Union[_wrappers_pb2.BytesValue, _Mapping]]] = ...) -> None: ...

class PredefinedAndCustomRuleProto2(_message.Message):
    __slots__ = ("a", "b")
    class Nested(_message.Message):
        __slots__ = ("c",)
        C_FIELD_NUMBER: _ClassVar[int]
        c: int
        def __init__(self, c: _Optional[int] = ...) -> None: ...
    A_FIELD_NUMBER: _ClassVar[int]
    B_FIELD_NUMBER: _ClassVar[int]
    a: int
    b: PredefinedAndCustomRuleProto2.Nested
    def __init__(self, a: _Optional[int] = ..., b: _Optional[_Union[PredefinedAndCustomRuleProto2.Nested, _Mapping]] = ...) -> None: ...

class StandardPredefinedAndCustomRuleProto2(_message.Message):
    __slots__ = ("a",)
    A_FIELD_NUMBER: _ClassVar[int]
    a: int
    def __init__(self, a: _Optional[int] = ...) -> None: ...
