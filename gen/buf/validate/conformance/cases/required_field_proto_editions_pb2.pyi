from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RequiredEditionsScalarExplicitPresence(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: str
    def __init__(self, val: _Optional[str] = ...) -> None: ...

class RequiredEditionsScalarExplicitPresenceDefault(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: str
    def __init__(self, val: _Optional[str] = ...) -> None: ...

class RequiredEditionsScalarImplicitPresence(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: str
    def __init__(self, val: _Optional[str] = ...) -> None: ...

class RequiredEditionsScalarLegacyRequired(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: str
    def __init__(self, val: _Optional[str] = ...) -> None: ...

class RequiredEditionsMessageExplicitPresence(_message.Message):
    __slots__ = ("val",)
    class Msg(_message.Message):
        __slots__ = ("val",)
        VAL_FIELD_NUMBER: _ClassVar[int]
        val: str
        def __init__(self, val: _Optional[str] = ...) -> None: ...
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: RequiredEditionsMessageExplicitPresence.Msg
    def __init__(self, val: _Optional[_Union[RequiredEditionsMessageExplicitPresence.Msg, _Mapping]] = ...) -> None: ...

class RequiredEditionsMessageExplicitPresenceDelimited(_message.Message):
    __slots__ = ("val",)
    class Msg(_message.Message):
        __slots__ = ("val",)
        VAL_FIELD_NUMBER: _ClassVar[int]
        val: str
        def __init__(self, val: _Optional[str] = ...) -> None: ...
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: RequiredEditionsMessageExplicitPresenceDelimited.Msg
    def __init__(self, val: _Optional[_Union[RequiredEditionsMessageExplicitPresenceDelimited.Msg, _Mapping]] = ...) -> None: ...

class RequiredEditionsMessageLegacyRequired(_message.Message):
    __slots__ = ("val",)
    class Msg(_message.Message):
        __slots__ = ("val",)
        VAL_FIELD_NUMBER: _ClassVar[int]
        val: str
        def __init__(self, val: _Optional[str] = ...) -> None: ...
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: RequiredEditionsMessageLegacyRequired.Msg
    def __init__(self, val: _Optional[_Union[RequiredEditionsMessageLegacyRequired.Msg, _Mapping]] = ...) -> None: ...

class RequiredEditionsMessageLegacyRequiredDelimited(_message.Message):
    __slots__ = ("val",)
    class Msg(_message.Message):
        __slots__ = ("val",)
        VAL_FIELD_NUMBER: _ClassVar[int]
        val: str
        def __init__(self, val: _Optional[str] = ...) -> None: ...
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: RequiredEditionsMessageLegacyRequiredDelimited.Msg
    def __init__(self, val: _Optional[_Union[RequiredEditionsMessageLegacyRequiredDelimited.Msg, _Mapping]] = ...) -> None: ...

class RequiredEditionsOneof(_message.Message):
    __slots__ = ("a", "b")
    A_FIELD_NUMBER: _ClassVar[int]
    B_FIELD_NUMBER: _ClassVar[int]
    a: str
    b: str
    def __init__(self, a: _Optional[str] = ..., b: _Optional[str] = ...) -> None: ...

class RequiredEditionsRepeated(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, val: _Optional[_Iterable[str]] = ...) -> None: ...

class RequiredEditionsRepeatedExpanded(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, val: _Optional[_Iterable[str]] = ...) -> None: ...

class RequiredEditionsMap(_message.Message):
    __slots__ = ("val",)
    class ValEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _containers.ScalarMap[str, str]
    def __init__(self, val: _Optional[_Mapping[str, str]] = ...) -> None: ...
