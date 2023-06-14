from buf.protovalidate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class BytesNone(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: bytes
    def __init__(self, val: _Optional[bytes] = ...) -> None: ...

class BytesConst(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: bytes
    def __init__(self, val: _Optional[bytes] = ...) -> None: ...

class BytesIn(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: bytes
    def __init__(self, val: _Optional[bytes] = ...) -> None: ...

class BytesNotIn(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: bytes
    def __init__(self, val: _Optional[bytes] = ...) -> None: ...

class BytesLen(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: bytes
    def __init__(self, val: _Optional[bytes] = ...) -> None: ...

class BytesMinLen(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: bytes
    def __init__(self, val: _Optional[bytes] = ...) -> None: ...

class BytesMaxLen(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: bytes
    def __init__(self, val: _Optional[bytes] = ...) -> None: ...

class BytesMinMaxLen(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: bytes
    def __init__(self, val: _Optional[bytes] = ...) -> None: ...

class BytesEqualMinMaxLen(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: bytes
    def __init__(self, val: _Optional[bytes] = ...) -> None: ...

class BytesPattern(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: bytes
    def __init__(self, val: _Optional[bytes] = ...) -> None: ...

class BytesPrefix(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: bytes
    def __init__(self, val: _Optional[bytes] = ...) -> None: ...

class BytesContains(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: bytes
    def __init__(self, val: _Optional[bytes] = ...) -> None: ...

class BytesSuffix(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: bytes
    def __init__(self, val: _Optional[bytes] = ...) -> None: ...

class BytesIP(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: bytes
    def __init__(self, val: _Optional[bytes] = ...) -> None: ...

class BytesIPv4(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: bytes
    def __init__(self, val: _Optional[bytes] = ...) -> None: ...

class BytesIPv6(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: bytes
    def __init__(self, val: _Optional[bytes] = ...) -> None: ...

class BytesIPv6Ignore(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: bytes
    def __init__(self, val: _Optional[bytes] = ...) -> None: ...
