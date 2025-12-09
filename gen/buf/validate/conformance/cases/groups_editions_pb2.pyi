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
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GroupDelimited(_message.Message):
    __slots__ = ("value",)
    class Value(_message.Message):
        __slots__ = ("x",)
        X_FIELD_NUMBER: _ClassVar[int]
        x: bool
        def __init__(self, x: bool = ...) -> None: ...
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: GroupDelimited.Value
    def __init__(self, value: _Optional[_Union[GroupDelimited.Value, _Mapping]] = ...) -> None: ...
