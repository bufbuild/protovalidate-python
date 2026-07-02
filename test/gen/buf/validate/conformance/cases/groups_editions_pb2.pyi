from .....buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GroupDelimited(_message.Message):
    __slots__ = ("value",)
    class Value(_message.Message):
        __slots__ = ("x",)
        X_FIELD_NUMBER: _ClassVar[int]
        x: bool
        def __init__(self, x: bool = ...) -> None: ...
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: GroupDelimited.Value
    def __init__(self, value: _Optional[_Union[GroupDelimited.Value, _Mapping]] = ...) -> None: ...
