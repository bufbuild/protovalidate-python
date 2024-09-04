from buf.validate.shared import constraints_pb2 as _constraints_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor
FLOAT_ABS_RANGE_PROTO2_FIELD_NUMBER: _ClassVar[int]
float_abs_range_proto2: _descriptor.FieldDescriptor
DOUBLE_ABS_RANGE_PROTO2_FIELD_NUMBER: _ClassVar[int]
double_abs_range_proto2: _descriptor.FieldDescriptor
INT32_EVEN_PROTO2_FIELD_NUMBER: _ClassVar[int]
int32_even_proto2: _descriptor.FieldDescriptor
INT64_EVEN_PROTO2_FIELD_NUMBER: _ClassVar[int]
int64_even_proto2: _descriptor.FieldDescriptor
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

class SharedFloatRuleProto2(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: float
    def __init__(self, val: _Optional[float] = ...) -> None: ...

class SharedDoubleRuleProto2(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: float
    def __init__(self, val: _Optional[float] = ...) -> None: ...

class SharedInt32RuleProto2(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class SharedInt64RuleProto2(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class SharedUInt32RuleProto2(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class SharedUInt64RuleProto2(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class SharedSInt32RuleProto2(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class SharedSInt64RuleProto2(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class SharedFixed32RuleProto2(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class SharedFixed64RuleProto2(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class SharedSFixed32RuleProto2(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class SharedSFixed64RuleProto2(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class SharedBoolRuleProto2(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: bool
    def __init__(self, val: bool = ...) -> None: ...

class SharedStringRuleProto2(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: str
    def __init__(self, val: _Optional[str] = ...) -> None: ...

class SharedBytesRuleProto2(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: bytes
    def __init__(self, val: _Optional[bytes] = ...) -> None: ...

class SharedEnumRuleProto2(_message.Message):
    __slots__ = ("val",)
    class EnumProto2(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ENUM_PROTO2_ZERO_UNSPECIFIED: _ClassVar[SharedEnumRuleProto2.EnumProto2]
        ENUM_PROTO2_ONE: _ClassVar[SharedEnumRuleProto2.EnumProto2]
    ENUM_PROTO2_ZERO_UNSPECIFIED: SharedEnumRuleProto2.EnumProto2
    ENUM_PROTO2_ONE: SharedEnumRuleProto2.EnumProto2
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: SharedEnumRuleProto2.EnumProto2
    def __init__(self, val: _Optional[_Union[SharedEnumRuleProto2.EnumProto2, str]] = ...) -> None: ...

class SharedRepeatedRuleProto2(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, val: _Optional[_Iterable[int]] = ...) -> None: ...

class SharedDurationRuleProto2(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _duration_pb2.Duration
    def __init__(self, val: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...

class SharedTimestampRuleProto2(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _timestamp_pb2.Timestamp
    def __init__(self, val: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
