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
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WrapperNone(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _wrappers_pb2.Int32Value
    def __init__(self, val: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ...) -> None: ...

class WrapperFloat(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _wrappers_pb2.FloatValue
    def __init__(self, val: _Optional[_Union[_wrappers_pb2.FloatValue, _Mapping]] = ...) -> None: ...

class WrapperDouble(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _wrappers_pb2.DoubleValue
    def __init__(self, val: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ...) -> None: ...

class WrapperInt64(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _wrappers_pb2.Int64Value
    def __init__(self, val: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ...) -> None: ...

class WrapperInt32(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _wrappers_pb2.Int32Value
    def __init__(self, val: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ...) -> None: ...

class WrapperUInt64(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _wrappers_pb2.UInt64Value
    def __init__(self, val: _Optional[_Union[_wrappers_pb2.UInt64Value, _Mapping]] = ...) -> None: ...

class WrapperUInt32(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _wrappers_pb2.UInt32Value
    def __init__(self, val: _Optional[_Union[_wrappers_pb2.UInt32Value, _Mapping]] = ...) -> None: ...

class WrapperBool(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _wrappers_pb2.BoolValue
    def __init__(self, val: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...) -> None: ...

class WrapperString(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _wrappers_pb2.StringValue
    def __init__(self, val: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...) -> None: ...

class WrapperBytes(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _wrappers_pb2.BytesValue
    def __init__(self, val: _Optional[_Union[_wrappers_pb2.BytesValue, _Mapping]] = ...) -> None: ...

class WrapperRequiredString(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _wrappers_pb2.StringValue
    def __init__(self, val: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...) -> None: ...

class WrapperRequiredEmptyString(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _wrappers_pb2.StringValue
    def __init__(self, val: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...) -> None: ...

class WrapperOptionalUuidString(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _wrappers_pb2.StringValue
    def __init__(self, val: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...) -> None: ...

class WrapperRequiredFloat(_message.Message):
    __slots__ = ("val",)
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: _wrappers_pb2.FloatValue
    def __init__(self, val: _Optional[_Union[_wrappers_pb2.FloatValue, _Mapping]] = ...) -> None: ...
