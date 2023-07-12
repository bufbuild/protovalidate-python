from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TestOneofMsg(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: bool
    def __init__(self, val: bool = ...) -> None: ...

class OneofNone(_message.Message):
    __slots__ = ["x", "y"]
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    x: str
    y: int
    def __init__(self, x: _Optional[str] = ..., y: _Optional[int] = ...) -> None: ...

class Oneof(_message.Message):
    __slots__ = ["x", "y", "z"]
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    Z_FIELD_NUMBER: _ClassVar[int]
    x: str
    y: int
    z: TestOneofMsg
    def __init__(self, x: _Optional[str] = ..., y: _Optional[int] = ..., z: _Optional[_Union[TestOneofMsg, _Mapping]] = ...) -> None: ...

class OneofRequired(_message.Message):
    __slots__ = ["x", "y", "name_with_underscores", "under_and_1_number"]
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    NAME_WITH_UNDERSCORES_FIELD_NUMBER: _ClassVar[int]
    UNDER_AND_1_NUMBER_FIELD_NUMBER: _ClassVar[int]
    x: str
    y: int
    name_with_underscores: int
    under_and_1_number: int
    def __init__(self, x: _Optional[str] = ..., y: _Optional[int] = ..., name_with_underscores: _Optional[int] = ..., under_and_1_number: _Optional[int] = ...) -> None: ...

class OneofIgnoreEmpty(_message.Message):
    __slots__ = ["x", "y", "z"]
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    Z_FIELD_NUMBER: _ClassVar[int]
    x: str
    y: bytes
    z: int
    def __init__(self, x: _Optional[str] = ..., y: _Optional[bytes] = ..., z: _Optional[int] = ...) -> None: ...
