from ...buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BenchGT(_message.Message):
    __slots__ = ("gt", "gte", "lt", "lte", "gtltin", "gtltein", "gtltex", "gtlteex", "gteltin", "gteltein", "gteltex", "gtelteex", "const", "constgt", "in_test", "not_in_test")
    GT_FIELD_NUMBER: _ClassVar[int]
    GTE_FIELD_NUMBER: _ClassVar[int]
    LT_FIELD_NUMBER: _ClassVar[int]
    LTE_FIELD_NUMBER: _ClassVar[int]
    GTLTIN_FIELD_NUMBER: _ClassVar[int]
    GTLTEIN_FIELD_NUMBER: _ClassVar[int]
    GTLTEX_FIELD_NUMBER: _ClassVar[int]
    GTLTEEX_FIELD_NUMBER: _ClassVar[int]
    GTELTIN_FIELD_NUMBER: _ClassVar[int]
    GTELTEIN_FIELD_NUMBER: _ClassVar[int]
    GTELTEX_FIELD_NUMBER: _ClassVar[int]
    GTELTEEX_FIELD_NUMBER: _ClassVar[int]
    CONST_FIELD_NUMBER: _ClassVar[int]
    CONSTGT_FIELD_NUMBER: _ClassVar[int]
    IN_TEST_FIELD_NUMBER: _ClassVar[int]
    NOT_IN_TEST_FIELD_NUMBER: _ClassVar[int]
    gt: int
    gte: int
    lt: int
    lte: int
    gtltin: int
    gtltein: int
    gtltex: int
    gtlteex: int
    gteltin: int
    gteltein: int
    gteltex: int
    gtelteex: int
    const: int
    constgt: int
    in_test: int
    not_in_test: int
    def __init__(self, gt: _Optional[int] = ..., gte: _Optional[int] = ..., lt: _Optional[int] = ..., lte: _Optional[int] = ..., gtltin: _Optional[int] = ..., gtltein: _Optional[int] = ..., gtltex: _Optional[int] = ..., gtlteex: _Optional[int] = ..., gteltin: _Optional[int] = ..., gteltein: _Optional[int] = ..., gteltex: _Optional[int] = ..., gtelteex: _Optional[int] = ..., const: _Optional[int] = ..., constgt: _Optional[int] = ..., in_test: _Optional[int] = ..., not_in_test: _Optional[int] = ...) -> None: ...

class TestByteMatching(_message.Message):
    __slots__ = ("ip_addr", "ipv4_addr", "ipv6_addr", "uuid")
    IP_ADDR_FIELD_NUMBER: _ClassVar[int]
    IPV4_ADDR_FIELD_NUMBER: _ClassVar[int]
    IPV6_ADDR_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    ip_addr: bytes
    ipv4_addr: bytes
    ipv6_addr: bytes
    uuid: bytes
    def __init__(self, ip_addr: _Optional[bytes] = ..., ipv4_addr: _Optional[bytes] = ..., ipv6_addr: _Optional[bytes] = ..., uuid: _Optional[bytes] = ...) -> None: ...

class StringMatching(_message.Message):
    __slots__ = ("hostname", "host_and_port", "email", "uuid")
    HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    HOST_AND_PORT_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    hostname: str
    host_and_port: str
    email: str
    uuid: str
    def __init__(self, hostname: _Optional[str] = ..., host_and_port: _Optional[str] = ..., email: _Optional[str] = ..., uuid: _Optional[str] = ...) -> None: ...

class WrapperTesting(_message.Message):
    __slots__ = ("i32", "d", "f", "i64", "u64", "u32", "b", "s", "bs")
    I32_FIELD_NUMBER: _ClassVar[int]
    D_FIELD_NUMBER: _ClassVar[int]
    F_FIELD_NUMBER: _ClassVar[int]
    I64_FIELD_NUMBER: _ClassVar[int]
    U64_FIELD_NUMBER: _ClassVar[int]
    U32_FIELD_NUMBER: _ClassVar[int]
    B_FIELD_NUMBER: _ClassVar[int]
    S_FIELD_NUMBER: _ClassVar[int]
    BS_FIELD_NUMBER: _ClassVar[int]
    i32: _wrappers_pb2.Int32Value
    d: _wrappers_pb2.DoubleValue
    f: _wrappers_pb2.FloatValue
    i64: _wrappers_pb2.Int64Value
    u64: _wrappers_pb2.UInt64Value
    u32: _wrappers_pb2.UInt32Value
    b: _wrappers_pb2.BoolValue
    s: _wrappers_pb2.StringValue
    bs: _wrappers_pb2.BytesValue
    def __init__(self, i32: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., d: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ..., f: _Optional[_Union[_wrappers_pb2.FloatValue, _Mapping]] = ..., i64: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., u64: _Optional[_Union[_wrappers_pb2.UInt64Value, _Mapping]] = ..., u32: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ..., b: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ..., s: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., bs: _Optional[_Union[_wrappers_pb2.BytesValue, _Mapping]] = ...) -> None: ...

class MultiRule(_message.Message):
    __slots__ = ("many",)
    MANY_FIELD_NUMBER: _ClassVar[int]
    many: int
    def __init__(self, many: _Optional[int] = ...) -> None: ...
