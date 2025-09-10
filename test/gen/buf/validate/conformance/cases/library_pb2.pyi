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
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class IsHostname(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: str
    def __init__(self, val: _Optional[str] = ...) -> None: ...

class IsHostAndPort(_message.Message):
    __slots__ = ("val", "port_required")
    VAL_FIELD_NUMBER: _ClassVar[int]
    PORT_REQUIRED_FIELD_NUMBER: _ClassVar[int]
    val: str
    port_required: bool
    def __init__(self, val: _Optional[str] = ..., port_required: bool = ...) -> None: ...

class IsIpPrefix(_message.Message):
    __slots__ = ("val", "version", "strict")
    VAL_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    STRICT_FIELD_NUMBER: _ClassVar[int]
    val: str
    version: int
    strict: bool
    def __init__(self, val: _Optional[str] = ..., version: _Optional[int] = ..., strict: bool = ...) -> None: ...

class IsIp(_message.Message):
    __slots__ = ("val", "version")
    VAL_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    val: str
    version: int
    def __init__(self, val: _Optional[str] = ..., version: _Optional[int] = ...) -> None: ...

class IsEmail(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: str
    def __init__(self, val: _Optional[str] = ...) -> None: ...

class IsUri(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: str
    def __init__(self, val: _Optional[str] = ...) -> None: ...

class IsUriRef(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: str
    def __init__(self, val: _Optional[str] = ...) -> None: ...
