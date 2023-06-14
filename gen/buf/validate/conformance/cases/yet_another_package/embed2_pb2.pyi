from buf.protovalidate import validate_pb2 as _validate_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Embed(_message.Message):
    __slots__ = ["val"]

    class Enumerated(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        ENUMERATED_UNSPECIFIED: _ClassVar[Embed.Enumerated]
        ENUMERATED_VALUE: _ClassVar[Embed.Enumerated]
    ENUMERATED_UNSPECIFIED: Embed.Enumerated
    ENUMERATED_VALUE: Embed.Enumerated
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...
