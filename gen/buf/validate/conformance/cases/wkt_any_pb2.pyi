from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import any_pb2 as _any_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AnyNone(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _any_pb2.Any
    def __init__(self, val: _Optional[_Union[_any_pb2.Any, _Mapping]] = ...) -> None: ...

class AnyRequired(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _any_pb2.Any
    def __init__(self, val: _Optional[_Union[_any_pb2.Any, _Mapping]] = ...) -> None: ...

class AnyIn(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _any_pb2.Any
    def __init__(self, val: _Optional[_Union[_any_pb2.Any, _Mapping]] = ...) -> None: ...

class AnyNotIn(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _any_pb2.Any
    def __init__(self, val: _Optional[_Union[_any_pb2.Any, _Mapping]] = ...) -> None: ...
