from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class IgnoreEmptyEditionsScalarExplicitPresence(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class IgnoreEmptyEditionsScalarExplicitPresenceWithDefault(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class IgnoreEmptyEditionsScalarImplicitPresence(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class IgnoreEmptyEditionsScalarLegacyRequired(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class IgnoreEmptyEditionsScalarLegacyRequiredWithDefault(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class IgnoreEmptyEditionsMessageExplicitPresence(_message.Message):
    __slots__ = ("val",)
    class Msg(_message.Message):
        __slots__ = ("val",)
        VAL_FIELD_NUMBER: _ClassVar[int]
        val: str
        def __init__(self, val: _Optional[str] = ...) -> None: ...
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: IgnoreEmptyEditionsMessageExplicitPresence.Msg
    def __init__(self, val: _Optional[_Union[IgnoreEmptyEditionsMessageExplicitPresence.Msg, _Mapping]] = ...) -> None: ...

class IgnoreEmptyEditionsMessageExplicitPresenceDelimited(_message.Message):
    __slots__ = ("val",)
    class Msg(_message.Message):
        __slots__ = ("val",)
        VAL_FIELD_NUMBER: _ClassVar[int]
        val: str
        def __init__(self, val: _Optional[str] = ...) -> None: ...
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: IgnoreEmptyEditionsMessageExplicitPresenceDelimited.Msg
    def __init__(self, val: _Optional[_Union[IgnoreEmptyEditionsMessageExplicitPresenceDelimited.Msg, _Mapping]] = ...) -> None: ...

class IgnoreEmptyEditionsMessageLegacyRequired(_message.Message):
    __slots__ = ("val",)
    class Msg(_message.Message):
        __slots__ = ("val",)
        VAL_FIELD_NUMBER: _ClassVar[int]
        val: str
        def __init__(self, val: _Optional[str] = ...) -> None: ...
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: IgnoreEmptyEditionsMessageLegacyRequired.Msg
    def __init__(self, val: _Optional[_Union[IgnoreEmptyEditionsMessageLegacyRequired.Msg, _Mapping]] = ...) -> None: ...

class IgnoreEmptyEditionsMessageLegacyRequiredDelimited(_message.Message):
    __slots__ = ("val",)
    class Msg(_message.Message):
        __slots__ = ("val",)
        VAL_FIELD_NUMBER: _ClassVar[int]
        val: str
        def __init__(self, val: _Optional[str] = ...) -> None: ...
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: IgnoreEmptyEditionsMessageLegacyRequiredDelimited.Msg
    def __init__(self, val: _Optional[_Union[IgnoreEmptyEditionsMessageLegacyRequiredDelimited.Msg, _Mapping]] = ...) -> None: ...

class IgnoreEmptyEditionsOneof(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class IgnoreEmptyEditionsRepeated(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, val: _Optional[_Iterable[int]] = ...) -> None: ...

class IgnoreEmptyEditionsRepeatedExpanded(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, val: _Optional[_Iterable[int]] = ...) -> None: ...

class IgnoreEmptyEditionsMap(_message.Message):
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
