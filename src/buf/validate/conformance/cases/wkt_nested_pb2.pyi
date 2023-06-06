from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WktLevelOne(_message.Message):
    __slots__ = ["two"]
    class WktLevelTwo(_message.Message):
        __slots__ = ["three"]
        class WktLevelThree(_message.Message):
            __slots__ = ["uuid"]
            UUID_FIELD_NUMBER: _ClassVar[int]
            uuid: str
            def __init__(self, uuid: _Optional[str] = ...) -> None: ...
        THREE_FIELD_NUMBER: _ClassVar[int]
        three: WktLevelOne.WktLevelTwo.WktLevelThree
        def __init__(self, three: _Optional[_Union[WktLevelOne.WktLevelTwo.WktLevelThree, _Mapping]] = ...) -> None: ...
    TWO_FIELD_NUMBER: _ClassVar[int]
    two: WktLevelOne.WktLevelTwo
    def __init__(self, two: _Optional[_Union[WktLevelOne.WktLevelTwo, _Mapping]] = ...) -> None: ...
