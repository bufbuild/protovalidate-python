from buf.protovalidate import validate_pb2 as _validate_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import (
    ClassVar as _ClassVar,
    Mapping as _Mapping,
    Optional as _Optional,
    Union as _Union,
)

DESCRIPTOR: _descriptor.FileDescriptor

class TimestampNone(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _timestamp_pb2.Timestamp
    def __init__(
        self, val: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...
    ) -> None: ...

class TimestampRequired(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _timestamp_pb2.Timestamp
    def __init__(
        self, val: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...
    ) -> None: ...

class TimestampConst(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _timestamp_pb2.Timestamp
    def __init__(
        self, val: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...
    ) -> None: ...

class TimestampLT(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _timestamp_pb2.Timestamp
    def __init__(
        self, val: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...
    ) -> None: ...

class TimestampLTE(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _timestamp_pb2.Timestamp
    def __init__(
        self, val: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...
    ) -> None: ...

class TimestampGT(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _timestamp_pb2.Timestamp
    def __init__(
        self, val: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...
    ) -> None: ...

class TimestampGTE(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _timestamp_pb2.Timestamp
    def __init__(
        self, val: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...
    ) -> None: ...

class TimestampGTLT(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _timestamp_pb2.Timestamp
    def __init__(
        self, val: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...
    ) -> None: ...

class TimestampExLTGT(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _timestamp_pb2.Timestamp
    def __init__(
        self, val: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...
    ) -> None: ...

class TimestampGTELTE(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _timestamp_pb2.Timestamp
    def __init__(
        self, val: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...
    ) -> None: ...

class TimestampExGTELTE(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _timestamp_pb2.Timestamp
    def __init__(
        self, val: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...
    ) -> None: ...

class TimestampLTNow(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _timestamp_pb2.Timestamp
    def __init__(
        self, val: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...
    ) -> None: ...

class TimestampGTNow(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _timestamp_pb2.Timestamp
    def __init__(
        self, val: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...
    ) -> None: ...

class TimestampWithin(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _timestamp_pb2.Timestamp
    def __init__(
        self, val: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...
    ) -> None: ...

class TimestampLTNowWithin(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _timestamp_pb2.Timestamp
    def __init__(
        self, val: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...
    ) -> None: ...

class TimestampGTNowWithin(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _timestamp_pb2.Timestamp
    def __init__(
        self, val: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...
    ) -> None: ...
