# Copyright 2023-2025 Buf Technologies, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar
from typing import Optional as _Optional
from typing import Union as _Union

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers

from buf.validate import validate_pb2 as _validate_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class MultipleValidations(_message.Message):
    __slots__ = ("name", "title")
    TITLE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    title: str
    name: str
    def __init__(self, title: str | None = ..., name: str | None = ...) -> None: ...

class DoubleFinite(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: float
    def __init__(self, val: float | None = ...) -> None: ...

class SFixed64ExLTGT(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: int | None = ...) -> None: ...

class TestOneofMsg(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: bool
    def __init__(self, val: bool = ...) -> None: ...

class Oneof(_message.Message):
    __slots__ = ("x", "y", "z")
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    Z_FIELD_NUMBER: _ClassVar[int]
    x: str
    y: int
    z: TestOneofMsg
    def __init__(self, x: str | None = ..., y: int | None = ..., z: TestOneofMsg | _Mapping | None = ...) -> None: ...

class ProtovalidateOneof(_message.Message):
    __slots__ = ("a", "b", "unrelated")
    A_FIELD_NUMBER: _ClassVar[int]
    B_FIELD_NUMBER: _ClassVar[int]
    UNRELATED_FIELD_NUMBER: _ClassVar[int]
    a: str
    b: str
    unrelated: bool
    def __init__(self, a: str | None = ..., b: str | None = ..., unrelated: bool = ...) -> None: ...

class ProtovalidateOneofRequired(_message.Message):
    __slots__ = ("a", "b", "unrelated")
    A_FIELD_NUMBER: _ClassVar[int]
    B_FIELD_NUMBER: _ClassVar[int]
    UNRELATED_FIELD_NUMBER: _ClassVar[int]
    a: str
    b: str
    unrelated: bool
    def __init__(self, a: str | None = ..., b: str | None = ..., unrelated: bool = ...) -> None: ...

class ProtovalidateOneofUnknownFieldName(_message.Message):
    __slots__ = ("a", "b", "unrelated")
    A_FIELD_NUMBER: _ClassVar[int]
    B_FIELD_NUMBER: _ClassVar[int]
    UNRELATED_FIELD_NUMBER: _ClassVar[int]
    a: str
    b: str
    unrelated: bool
    def __init__(self, a: str | None = ..., b: str | None = ..., unrelated: bool = ...) -> None: ...

class TimestampGTNow(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _timestamp_pb2.Timestamp
    def __init__(self, val: _timestamp_pb2.Timestamp | _Mapping | None = ...) -> None: ...

class MapMinMax(_message.Message):
    __slots__ = ("val",)
    class ValEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: bool
        def __init__(self, key: str | None = ..., value: bool = ...) -> None: ...

    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _containers.ScalarMap[str, bool]
    def __init__(self, val: _Mapping[str, bool] | None = ...) -> None: ...

class MapKeys(_message.Message):
    __slots__ = ("val",)
    class ValEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: str
        def __init__(self, key: int | None = ..., value: str | None = ...) -> None: ...

    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _containers.ScalarMap[int, str]
    def __init__(self, val: _Mapping[int, str] | None = ...) -> None: ...

class Embed(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: int | None = ...) -> None: ...

class RepeatedEmbedSkip(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _containers.RepeatedCompositeFieldContainer[Embed]
    def __init__(self, val: _Iterable[Embed | _Mapping] | None = ...) -> None: ...

class InvalidRESyntax(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: str
    def __init__(self, value: str | None = ...) -> None: ...

class ConcatenatedValues(_message.Message):
    __slots__ = ("bar", "baz")
    BAR_FIELD_NUMBER: _ClassVar[int]
    BAZ_FIELD_NUMBER: _ClassVar[int]
    bar: _containers.RepeatedScalarFieldContainer[str]
    baz: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, bar: _Iterable[str] | None = ..., baz: _Iterable[str] | None = ...) -> None: ...
