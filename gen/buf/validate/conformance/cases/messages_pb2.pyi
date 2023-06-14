from buf.protovalidate.conformance.cases.other_package import embed_pb2 as _embed_pb2
from buf.protovalidate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import (
    ClassVar as _ClassVar,
    Mapping as _Mapping,
    Optional as _Optional,
    Union as _Union,
)

DESCRIPTOR: _descriptor.FileDescriptor

class TestMsg(_message.Message):
    __slots__ = ["const", "nested"]
    CONST_FIELD_NUMBER: _ClassVar[int]
    NESTED_FIELD_NUMBER: _ClassVar[int]
    const: str
    nested: TestMsg
    def __init__(
        self,
        const: _Optional[str] = ...,
        nested: _Optional[_Union[TestMsg, _Mapping]] = ...,
    ) -> None: ...

class MessageNone(_message.Message):
    __slots__ = ["val"]

    class NoneMsg(_message.Message):
        __slots__ = []
        def __init__(self) -> None: ...
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: MessageNone.NoneMsg
    def __init__(
        self, val: _Optional[_Union[MessageNone.NoneMsg, _Mapping]] = ...
    ) -> None: ...

class MessageDisabled(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class Message(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: TestMsg
    def __init__(self, val: _Optional[_Union[TestMsg, _Mapping]] = ...) -> None: ...

class MessageCrossPackage(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _embed_pb2.Embed
    def __init__(
        self, val: _Optional[_Union[_embed_pb2.Embed, _Mapping]] = ...
    ) -> None: ...

class MessageSkip(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: TestMsg
    def __init__(self, val: _Optional[_Union[TestMsg, _Mapping]] = ...) -> None: ...

class MessageRequired(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: TestMsg
    def __init__(self, val: _Optional[_Union[TestMsg, _Mapping]] = ...) -> None: ...

class MessageRequiredButOptional(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: TestMsg
    def __init__(self, val: _Optional[_Union[TestMsg, _Mapping]] = ...) -> None: ...

class MessageRequiredOneof(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: TestMsg
    def __init__(self, val: _Optional[_Union[TestMsg, _Mapping]] = ...) -> None: ...

class MessageWith3dInside(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
