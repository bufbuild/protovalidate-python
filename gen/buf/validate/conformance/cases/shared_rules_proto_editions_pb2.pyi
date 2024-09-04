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
FLOAT_ABS_RANGE_EDITION_2023_FIELD_NUMBER: _ClassVar[int]
float_abs_range_edition_2023: _descriptor.FieldDescriptor
DOUBLE_ABS_RANGE_EDITION_2023_FIELD_NUMBER: _ClassVar[int]
double_abs_range_edition_2023: _descriptor.FieldDescriptor
INT32_EVEN_EDITION_2023_FIELD_NUMBER: _ClassVar[int]
int32_even_edition_2023: _descriptor.FieldDescriptor
INT64_EVEN_EDITION_2023_FIELD_NUMBER: _ClassVar[int]
int64_even_edition_2023: _descriptor.FieldDescriptor
UINT32_EVEN_EDITION_2023_FIELD_NUMBER: _ClassVar[int]
uint32_even_edition_2023: _descriptor.FieldDescriptor
UINT64_EVEN_EDITION_2023_FIELD_NUMBER: _ClassVar[int]
uint64_even_edition_2023: _descriptor.FieldDescriptor
SINT32_EVEN_EDITION_2023_FIELD_NUMBER: _ClassVar[int]
sint32_even_edition_2023: _descriptor.FieldDescriptor
SINT64_EVEN_EDITION_2023_FIELD_NUMBER: _ClassVar[int]
sint64_even_edition_2023: _descriptor.FieldDescriptor
FIXED32_EVEN_EDITION_2023_FIELD_NUMBER: _ClassVar[int]
fixed32_even_edition_2023: _descriptor.FieldDescriptor
FIXED64_EVEN_EDITION_2023_FIELD_NUMBER: _ClassVar[int]
fixed64_even_edition_2023: _descriptor.FieldDescriptor
SFIXED32_EVEN_EDITION_2023_FIELD_NUMBER: _ClassVar[int]
sfixed32_even_edition_2023: _descriptor.FieldDescriptor
SFIXED64_EVEN_EDITION_2023_FIELD_NUMBER: _ClassVar[int]
sfixed64_even_edition_2023: _descriptor.FieldDescriptor
BOOL_FALSE_EDITION_2023_FIELD_NUMBER: _ClassVar[int]
bool_false_edition_2023: _descriptor.FieldDescriptor
STRING_VALID_PATH_EDITION_2023_FIELD_NUMBER: _ClassVar[int]
string_valid_path_edition_2023: _descriptor.FieldDescriptor
BYTES_VALID_PATH_EDITION_2023_FIELD_NUMBER: _ClassVar[int]
bytes_valid_path_edition_2023: _descriptor.FieldDescriptor
ENUM_NON_ZERO_EDITION_2023_FIELD_NUMBER: _ClassVar[int]
enum_non_zero_edition_2023: _descriptor.FieldDescriptor
REPEATED_AT_LEAST_FIVE_EDITION_2023_FIELD_NUMBER: _ClassVar[int]
repeated_at_least_five_edition_2023: _descriptor.FieldDescriptor
MAP_AT_LEAST_FIVE_EDITION_2023_FIELD_NUMBER: _ClassVar[int]
map_at_least_five_edition_2023: _descriptor.FieldDescriptor
DURATION_TOO_LONG_EDITION_2023_FIELD_NUMBER: _ClassVar[int]
duration_too_long_edition_2023: _descriptor.FieldDescriptor
TIMESTAMP_IN_RANGE_EDITION_2023_FIELD_NUMBER: _ClassVar[int]
timestamp_in_range_edition_2023: _descriptor.FieldDescriptor

class SharedFloatRuleEdition2023(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: float
    def __init__(self, val: _Optional[float] = ...) -> None: ...

class SharedDoubleRuleEdition2023(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: float
    def __init__(self, val: _Optional[float] = ...) -> None: ...

class SharedInt32RuleEdition2023(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class SharedInt64RuleEdition2023(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class SharedUInt32RuleEdition2023(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class SharedUInt64RuleEdition2023(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class SharedSInt32RuleEdition2023(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class SharedSInt64RuleEdition2023(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class SharedFixed32RuleEdition2023(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class SharedFixed64RuleEdition2023(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class SharedSFixed32RuleEdition2023(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class SharedSFixed64RuleEdition2023(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class SharedBoolRuleEdition2023(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: bool
    def __init__(self, val: bool = ...) -> None: ...

class SharedStringRuleEdition2023(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: str
    def __init__(self, val: _Optional[str] = ...) -> None: ...

class SharedBytesRuleEdition2023(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: bytes
    def __init__(self, val: _Optional[bytes] = ...) -> None: ...

class SharedEnumRuleEdition2023(_message.Message):
    __slots__ = ("val",)
    class EnumEdition2023(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ENUM_EDITION2023_ZERO_UNSPECIFIED: _ClassVar[SharedEnumRuleEdition2023.EnumEdition2023]
        ENUM_EDITION2023_ONE: _ClassVar[SharedEnumRuleEdition2023.EnumEdition2023]
    ENUM_EDITION2023_ZERO_UNSPECIFIED: SharedEnumRuleEdition2023.EnumEdition2023
    ENUM_EDITION2023_ONE: SharedEnumRuleEdition2023.EnumEdition2023
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: SharedEnumRuleEdition2023.EnumEdition2023
    def __init__(self, val: _Optional[_Union[SharedEnumRuleEdition2023.EnumEdition2023, str]] = ...) -> None: ...

class SharedRepeatedRuleEdition2023(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, val: _Optional[_Iterable[int]] = ...) -> None: ...

class SharedMapRuleEdition2023(_message.Message):
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

class SharedDurationRuleEdition2023(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _duration_pb2.Duration
    def __init__(self, val: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...

class SharedTimestampRuleEdition2023(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _timestamp_pb2.Timestamp
    def __init__(self, val: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
