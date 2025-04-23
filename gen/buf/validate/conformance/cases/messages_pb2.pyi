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

from buf.validate.conformance.cases.other_package import embed_pb2 as _embed_pb2
from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TestMsg(_message.Message):
    __slots__ = ("const", "nested")
    CONST_FIELD_NUMBER: _ClassVar[int]
    NESTED_FIELD_NUMBER: _ClassVar[int]
    const: str
    nested: TestMsg
    def __init__(self, const: _Optional[str] = ..., nested: _Optional[_Union[TestMsg, _Mapping]] = ...) -> None: ...

class MessageNone(_message.Message):
    __slots__ = ("val",)
    class NoneMsg(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: MessageNone.NoneMsg
    def __init__(self, val: _Optional[_Union[MessageNone.NoneMsg, _Mapping]] = ...) -> None: ...

class MessageDisabled(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class Message(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: TestMsg
    def __init__(self, val: _Optional[_Union[TestMsg, _Mapping]] = ...) -> None: ...

class MessageCrossPackage(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _embed_pb2.Embed
    def __init__(self, val: _Optional[_Union[_embed_pb2.Embed, _Mapping]] = ...) -> None: ...

class MessageSkip(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: TestMsg
    def __init__(self, val: _Optional[_Union[TestMsg, _Mapping]] = ...) -> None: ...

class MessageRequired(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: TestMsg
    def __init__(self, val: _Optional[_Union[TestMsg, _Mapping]] = ...) -> None: ...

class MessageRequiredButOptional(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: TestMsg
    def __init__(self, val: _Optional[_Union[TestMsg, _Mapping]] = ...) -> None: ...

class MessageRequiredOneof(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: TestMsg
    def __init__(self, val: _Optional[_Union[TestMsg, _Mapping]] = ...) -> None: ...

class MessageWith3dInside(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
