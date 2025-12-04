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
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GroupOptional(_message.Message):
    __slots__ = ("optional",)
    class Optional(_message.Message):
        __slots__ = ("value",)
        VALUE_FIELD_NUMBER: _ClassVar[int]
        value: str
        def __init__(self, value: _Optional[str] = ...) -> None: ...
    OPTIONAL_FIELD_NUMBER: _ClassVar[int]
    optional: GroupOptional.Optional
    def __init__(self, optional: _Optional[_Union[GroupOptional.Optional, _Mapping]] = ...) -> None: ...

class GroupRepeated(_message.Message):
    __slots__ = ("repeated",)
    class Repeated(_message.Message):
        __slots__ = ("value",)
        VALUE_FIELD_NUMBER: _ClassVar[int]
        value: int
        def __init__(self, value: _Optional[int] = ...) -> None: ...
    REPEATED_FIELD_NUMBER: _ClassVar[int]
    repeated: _containers.RepeatedCompositeFieldContainer[GroupRepeated.Repeated]
    def __init__(self, repeated: _Optional[_Iterable[_Union[GroupRepeated.Repeated, _Mapping]]] = ...) -> None: ...

class GroupRequired(_message.Message):
    __slots__ = ("required",)
    class Required(_message.Message):
        __slots__ = ("value",)
        VALUE_FIELD_NUMBER: _ClassVar[int]
        value: bool
        def __init__(self, value: bool = ...) -> None: ...
    REQUIRED_FIELD_NUMBER: _ClassVar[int]
    required: GroupRequired.Required
    def __init__(self, required: _Optional[_Union[GroupRequired.Required, _Mapping]] = ...) -> None: ...

class GroupCustom(_message.Message):
    __slots__ = ("custom",)
    class Custom(_message.Message):
        __slots__ = ("value", "div")
        VALUE_FIELD_NUMBER: _ClassVar[int]
        DIV_FIELD_NUMBER: _ClassVar[int]
        value: int
        div: int
        def __init__(self, value: _Optional[int] = ..., div: _Optional[int] = ...) -> None: ...
    CUSTOM_FIELD_NUMBER: _ClassVar[int]
    custom: GroupCustom.Custom
    def __init__(self, custom: _Optional[_Union[GroupCustom.Custom, _Mapping]] = ...) -> None: ...
