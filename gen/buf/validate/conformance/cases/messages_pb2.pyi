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

class MessageOneofSingleField(_message.Message):
    __slots__ = ("str_field", "bool_field")
    STR_FIELD_FIELD_NUMBER: _ClassVar[int]
    BOOL_FIELD_FIELD_NUMBER: _ClassVar[int]
    str_field: str
    bool_field: bool
    def __init__(self, str_field: _Optional[str] = ..., bool_field: bool = ...) -> None: ...

class MessageOneofSingleFieldRequired(_message.Message):
    __slots__ = ("str_field", "bool_field")
    STR_FIELD_FIELD_NUMBER: _ClassVar[int]
    BOOL_FIELD_FIELD_NUMBER: _ClassVar[int]
    str_field: str
    bool_field: bool
    def __init__(self, str_field: _Optional[str] = ..., bool_field: bool = ...) -> None: ...

class MessageOneofMultipleFields(_message.Message):
    __slots__ = ("str_field", "bool_field")
    STR_FIELD_FIELD_NUMBER: _ClassVar[int]
    BOOL_FIELD_FIELD_NUMBER: _ClassVar[int]
    str_field: str
    bool_field: bool
    def __init__(self, str_field: _Optional[str] = ..., bool_field: bool = ...) -> None: ...

class MessageOneofMultipleFieldsRequired(_message.Message):
    __slots__ = ("str_field", "bool_field")
    STR_FIELD_FIELD_NUMBER: _ClassVar[int]
    BOOL_FIELD_FIELD_NUMBER: _ClassVar[int]
    str_field: str
    bool_field: bool
    def __init__(self, str_field: _Optional[str] = ..., bool_field: bool = ...) -> None: ...

class MessageOneofMultipleSharedFields(_message.Message):
    __slots__ = ("str_field", "bool_field", "int_field")
    STR_FIELD_FIELD_NUMBER: _ClassVar[int]
    BOOL_FIELD_FIELD_NUMBER: _ClassVar[int]
    INT_FIELD_FIELD_NUMBER: _ClassVar[int]
    str_field: str
    bool_field: bool
    int_field: int
    def __init__(self, str_field: _Optional[str] = ..., bool_field: bool = ..., int_field: _Optional[int] = ...) -> None: ...

class MessageOneofUnknownFieldName(_message.Message):
    __slots__ = ("str_field",)
    STR_FIELD_FIELD_NUMBER: _ClassVar[int]
    str_field: str
    def __init__(self, str_field: _Optional[str] = ...) -> None: ...

class MessageOneofDuplicateField(_message.Message):
    __slots__ = ("str_field", "bool_field")
    STR_FIELD_FIELD_NUMBER: _ClassVar[int]
    BOOL_FIELD_FIELD_NUMBER: _ClassVar[int]
    str_field: str
    bool_field: bool
    def __init__(self, str_field: _Optional[str] = ..., bool_field: bool = ...) -> None: ...

class MessageOneofZeroFields(_message.Message):
    __slots__ = ("str_field", "bool_field")
    STR_FIELD_FIELD_NUMBER: _ClassVar[int]
    BOOL_FIELD_FIELD_NUMBER: _ClassVar[int]
    str_field: str
    bool_field: bool
    def __init__(self, str_field: _Optional[str] = ..., bool_field: bool = ...) -> None: ...

class MessageOneofUnsatisfiable(_message.Message):
    __slots__ = ("a", "b", "c")
    A_FIELD_NUMBER: _ClassVar[int]
    B_FIELD_NUMBER: _ClassVar[int]
    C_FIELD_NUMBER: _ClassVar[int]
    a: bool
    b: bool
    c: bool
    def __init__(self, a: bool = ..., b: bool = ..., c: bool = ...) -> None: ...

class MessageOneofIgnoreUnpopulated(_message.Message):
    __slots__ = ("str_field", "bool_field")
    STR_FIELD_FIELD_NUMBER: _ClassVar[int]
    BOOL_FIELD_FIELD_NUMBER: _ClassVar[int]
    str_field: str
    bool_field: bool
    def __init__(self, str_field: _Optional[str] = ..., bool_field: bool = ...) -> None: ...

class MessageOneofIgnoreUnpopulatedRequired(_message.Message):
    __slots__ = ("str_field", "bool_field")
    STR_FIELD_FIELD_NUMBER: _ClassVar[int]
    BOOL_FIELD_FIELD_NUMBER: _ClassVar[int]
    str_field: str
    bool_field: bool
    def __init__(self, str_field: _Optional[str] = ..., bool_field: bool = ...) -> None: ...

class MessageOneofIgnoreOverride(_message.Message):
    __slots__ = ("msg_field", "bool_field")
    MSG_FIELD_FIELD_NUMBER: _ClassVar[int]
    BOOL_FIELD_FIELD_NUMBER: _ClassVar[int]
    msg_field: TestMsg
    bool_field: bool
    def __init__(self, msg_field: _Optional[_Union[TestMsg, _Mapping]] = ..., bool_field: bool = ...) -> None: ...
