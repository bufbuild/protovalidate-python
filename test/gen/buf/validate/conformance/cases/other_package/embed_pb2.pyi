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
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Embed(_message.Message):
    __slots__ = ("val",)
    class Enumerated(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ENUMERATED_UNSPECIFIED: _ClassVar[Embed.Enumerated]
        ENUMERATED_VALUE: _ClassVar[Embed.Enumerated]
    ENUMERATED_UNSPECIFIED: Embed.Enumerated
    ENUMERATED_VALUE: Embed.Enumerated
    class DoubleEmbed(_message.Message):
        __slots__ = ()
        class DoubleEnumerated(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            DOUBLE_ENUMERATED_UNSPECIFIED: _ClassVar[Embed.DoubleEmbed.DoubleEnumerated]
            DOUBLE_ENUMERATED_VALUE: _ClassVar[Embed.DoubleEmbed.DoubleEnumerated]
        DOUBLE_ENUMERATED_UNSPECIFIED: Embed.DoubleEmbed.DoubleEnumerated
        DOUBLE_ENUMERATED_VALUE: Embed.DoubleEmbed.DoubleEnumerated
        def __init__(self) -> None: ...
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...
