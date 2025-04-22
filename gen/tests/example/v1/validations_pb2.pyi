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

from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DoubleFinite(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: float
    def __init__(self, val: _Optional[float] = ...) -> None: ...

class SFixed64ExLTGT(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

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
    def __init__(self, x: _Optional[str] = ..., y: _Optional[int] = ..., z: _Optional[_Union[TestOneofMsg, _Mapping]] = ...) -> None: ...

class TimestampGTNow(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _timestamp_pb2.Timestamp
    def __init__(self, val: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class MapMinMax(_message.Message):
    __slots__ = ("val",)
    class ValEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: bool
        def __init__(self, key: _Optional[str] = ..., value: bool = ...) -> None: ...
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _containers.ScalarMap[str, bool]
    def __init__(self, val: _Optional[_Mapping[str, bool]] = ...) -> None: ...

class MapKeys(_message.Message):
    __slots__ = ("val",)
    class ValEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: str
        def __init__(self, key: _Optional[int] = ..., value: _Optional[str] = ...) -> None: ...
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _containers.ScalarMap[int, str]
    def __init__(self, val: _Optional[_Mapping[int, str]] = ...) -> None: ...

class Embed(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class RepeatedEmbedSkip(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _containers.RepeatedCompositeFieldContainer[Embed]
    def __init__(self, val: _Optional[_Iterable[_Union[Embed, _Mapping]]] = ...) -> None: ...
