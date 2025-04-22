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
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WktLevelOne(_message.Message):
    __slots__ = ("two",)
    class WktLevelTwo(_message.Message):
        __slots__ = ("three",)
        class WktLevelThree(_message.Message):
            __slots__ = ("uuid",)
            UUID_FIELD_NUMBER: _ClassVar[int]
            uuid: str
            def __init__(self, uuid: _Optional[str] = ...) -> None: ...
        THREE_FIELD_NUMBER: _ClassVar[int]
        three: WktLevelOne.WktLevelTwo.WktLevelThree
        def __init__(self, three: _Optional[_Union[WktLevelOne.WktLevelTwo.WktLevelThree, _Mapping]] = ...) -> None: ...
    TWO_FIELD_NUMBER: _ClassVar[int]
    two: WktLevelOne.WktLevelTwo
    def __init__(self, two: _Optional[_Union[WktLevelOne.WktLevelTwo, _Mapping]] = ...) -> None: ...
