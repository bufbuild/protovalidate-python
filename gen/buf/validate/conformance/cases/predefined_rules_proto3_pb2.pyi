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

from buf.validate.conformance.cases import predefined_rules_proto2_pb2 as _predefined_rules_proto2_pb2
from buf.validate.conformance.cases import predefined_rules_proto_editions_pb2 as _predefined_rules_proto_editions_pb2
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

class PredefinedFloatRuleProto3(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: float
    def __init__(self, val: _Optional[float] = ...) -> None: ...

class PredefinedDoubleRuleProto3(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: float
    def __init__(self, val: _Optional[float] = ...) -> None: ...

class PredefinedInt32RuleProto3(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class PredefinedInt64RuleProto3(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class PredefinedUInt32RuleProto3(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class PredefinedUInt64RuleProto3(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class PredefinedSInt32RuleProto3(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class PredefinedSInt64RuleProto3(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class PredefinedFixed32RuleProto3(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class PredefinedFixed64RuleProto3(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class PredefinedSFixed32RuleProto3(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class PredefinedSFixed64RuleProto3(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class PredefinedBoolRuleProto3(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: bool
    def __init__(self, val: bool = ...) -> None: ...

class PredefinedStringRuleProto3(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: str
    def __init__(self, val: _Optional[str] = ...) -> None: ...

class PredefinedBytesRuleProto3(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: bytes
    def __init__(self, val: _Optional[bytes] = ...) -> None: ...

class PredefinedEnumRuleProto3(_message.Message):
    __slots__ = ("val",)
    class EnumProto3(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ENUM_PROTO3_ZERO_UNSPECIFIED: _ClassVar[PredefinedEnumRuleProto3.EnumProto3]
        ENUM_PROTO3_ONE: _ClassVar[PredefinedEnumRuleProto3.EnumProto3]
    ENUM_PROTO3_ZERO_UNSPECIFIED: PredefinedEnumRuleProto3.EnumProto3
    ENUM_PROTO3_ONE: PredefinedEnumRuleProto3.EnumProto3
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: PredefinedEnumRuleProto3.EnumProto3
    def __init__(self, val: _Optional[_Union[PredefinedEnumRuleProto3.EnumProto3, str]] = ...) -> None: ...

class PredefinedMapRuleProto3(_message.Message):
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

class PredefinedRepeatedRuleProto3(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, val: _Optional[_Iterable[int]] = ...) -> None: ...

class PredefinedDurationRuleProto3(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _duration_pb2.Duration
    def __init__(self, val: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...

class PredefinedTimestampRuleProto3(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _timestamp_pb2.Timestamp
    def __init__(self, val: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class PredefinedWrappedFloatRuleProto3(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _wrappers_pb2.FloatValue
    def __init__(self, val: _Optional[_Union[_wrappers_pb2.FloatValue, _Mapping]] = ...) -> None: ...

class PredefinedWrappedDoubleRuleProto3(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _wrappers_pb2.DoubleValue
    def __init__(self, val: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ...) -> None: ...

class PredefinedWrappedInt32RuleProto3(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _wrappers_pb2.Int32Value
    def __init__(self, val: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ...) -> None: ...

class PredefinedWrappedInt64RuleProto3(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _wrappers_pb2.Int64Value
    def __init__(self, val: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ...) -> None: ...

class PredefinedWrappedUInt32RuleProto3(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _wrappers_pb2.UInt32Value
    def __init__(self, val: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ...) -> None: ...

class PredefinedWrappedUInt64RuleProto3(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _wrappers_pb2.UInt64Value
    def __init__(self, val: _Optional[_Union[_wrappers_pb2.UInt64Value, _Mapping]] = ...) -> None: ...

class PredefinedWrappedBoolRuleProto3(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _wrappers_pb2.BoolValue
    def __init__(self, val: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...) -> None: ...

class PredefinedWrappedStringRuleProto3(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _wrappers_pb2.StringValue
    def __init__(self, val: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...) -> None: ...

class PredefinedWrappedBytesRuleProto3(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _wrappers_pb2.BytesValue
    def __init__(self, val: _Optional[_Union[_wrappers_pb2.BytesValue, _Mapping]] = ...) -> None: ...

class PredefinedRepeatedWrappedFloatRuleProto3(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _containers.RepeatedCompositeFieldContainer[_wrappers_pb2.FloatValue]
    def __init__(self, val: _Optional[_Iterable[_Union[_wrappers_pb2.FloatValue, _Mapping]]] = ...) -> None: ...

class PredefinedRepeatedWrappedDoubleRuleProto3(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _containers.RepeatedCompositeFieldContainer[_wrappers_pb2.DoubleValue]
    def __init__(self, val: _Optional[_Iterable[_Union[_wrappers_pb2.DoubleValue, _Mapping]]] = ...) -> None: ...

class PredefinedRepeatedWrappedInt32RuleProto3(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _containers.RepeatedCompositeFieldContainer[_wrappers_pb2.Int32Value]
    def __init__(self, val: _Optional[_Iterable[_Union[_wrappers_pb2.Int32Value, _Mapping]]] = ...) -> None: ...

class PredefinedRepeatedWrappedInt64RuleProto3(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _containers.RepeatedCompositeFieldContainer[_wrappers_pb2.Int64Value]
    def __init__(self, val: _Optional[_Iterable[_Union[_wrappers_pb2.Int64Value, _Mapping]]] = ...) -> None: ...

class PredefinedRepeatedWrappedUInt32RuleProto3(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _containers.RepeatedCompositeFieldContainer[_wrappers_pb2.UInt32Value]
    def __init__(self, val: _Optional[_Iterable[_Union[_wrappers_pb2.UInt32Value, _Mapping]]] = ...) -> None: ...

class PredefinedRepeatedWrappedUInt64RuleProto3(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _containers.RepeatedCompositeFieldContainer[_wrappers_pb2.UInt64Value]
    def __init__(self, val: _Optional[_Iterable[_Union[_wrappers_pb2.UInt64Value, _Mapping]]] = ...) -> None: ...

class PredefinedRepeatedWrappedBoolRuleProto3(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _containers.RepeatedCompositeFieldContainer[_wrappers_pb2.BoolValue]
    def __init__(self, val: _Optional[_Iterable[_Union[_wrappers_pb2.BoolValue, _Mapping]]] = ...) -> None: ...

class PredefinedRepeatedWrappedStringRuleProto3(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _containers.RepeatedCompositeFieldContainer[_wrappers_pb2.StringValue]
    def __init__(self, val: _Optional[_Iterable[_Union[_wrappers_pb2.StringValue, _Mapping]]] = ...) -> None: ...

class PredefinedRepeatedWrappedBytesRuleProto3(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _containers.RepeatedCompositeFieldContainer[_wrappers_pb2.BytesValue]
    def __init__(self, val: _Optional[_Iterable[_Union[_wrappers_pb2.BytesValue, _Mapping]]] = ...) -> None: ...

class PredefinedAndCustomRuleProto3(_message.Message):
    __slots__ = ("a", "b")
    class Nested(_message.Message):
        __slots__ = ("c",)
        C_FIELD_NUMBER: _ClassVar[int]
        c: int
        def __init__(self, c: _Optional[int] = ...) -> None: ...
    A_FIELD_NUMBER: _ClassVar[int]
    B_FIELD_NUMBER: _ClassVar[int]
    a: int
    b: PredefinedAndCustomRuleProto3.Nested
    def __init__(self, a: _Optional[int] = ..., b: _Optional[_Union[PredefinedAndCustomRuleProto3.Nested, _Mapping]] = ...) -> None: ...

class StandardPredefinedAndCustomRuleProto3(_message.Message):
    __slots__ = ("a",)
    A_FIELD_NUMBER: _ClassVar[int]
    a: int
    def __init__(self, a: _Optional[int] = ...) -> None: ...

class PredefinedRulesProto3UnusedImportBugWorkaround(_message.Message):
    __slots__ = ("dummy_1", "dummy_2")
    DUMMY_1_FIELD_NUMBER: _ClassVar[int]
    DUMMY_2_FIELD_NUMBER: _ClassVar[int]
    dummy_1: _predefined_rules_proto2_pb2.StandardPredefinedAndCustomRuleProto2
    dummy_2: _predefined_rules_proto_editions_pb2.StandardPredefinedAndCustomRuleEdition2023
    def __init__(self, dummy_1: _Optional[_Union[_predefined_rules_proto2_pb2.StandardPredefinedAndCustomRuleProto2, _Mapping]] = ..., dummy_2: _Optional[_Union[_predefined_rules_proto_editions_pb2.StandardPredefinedAndCustomRuleEdition2023, _Mapping]] = ...) -> None: ...
