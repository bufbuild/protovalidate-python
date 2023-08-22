# Copyright 2023 Buf Technologies, Inc.
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

class FloatNone(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: float
    def __init__(self, val: _Optional[float] = ...) -> None: ...

class FloatConst(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: float
    def __init__(self, val: _Optional[float] = ...) -> None: ...

class FloatIn(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: float
    def __init__(self, val: _Optional[float] = ...) -> None: ...

class FloatNotIn(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: float
    def __init__(self, val: _Optional[float] = ...) -> None: ...

class FloatLT(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: float
    def __init__(self, val: _Optional[float] = ...) -> None: ...

class FloatLTE(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: float
    def __init__(self, val: _Optional[float] = ...) -> None: ...

class FloatGT(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: float
    def __init__(self, val: _Optional[float] = ...) -> None: ...

class FloatGTE(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: float
    def __init__(self, val: _Optional[float] = ...) -> None: ...

class FloatGTLT(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: float
    def __init__(self, val: _Optional[float] = ...) -> None: ...

class FloatExLTGT(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: float
    def __init__(self, val: _Optional[float] = ...) -> None: ...

class FloatGTELTE(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: float
    def __init__(self, val: _Optional[float] = ...) -> None: ...

class FloatExGTELTE(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: float
    def __init__(self, val: _Optional[float] = ...) -> None: ...

class FloatFinite(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: float
    def __init__(self, val: _Optional[float] = ...) -> None: ...

class FloatIgnore(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: float
    def __init__(self, val: _Optional[float] = ...) -> None: ...

class FloatIncorrectType(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: float
    def __init__(self, val: _Optional[float] = ...) -> None: ...

class DoubleNone(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: float
    def __init__(self, val: _Optional[float] = ...) -> None: ...

class DoubleConst(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: float
    def __init__(self, val: _Optional[float] = ...) -> None: ...

class DoubleIn(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: float
    def __init__(self, val: _Optional[float] = ...) -> None: ...

class DoubleNotIn(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: float
    def __init__(self, val: _Optional[float] = ...) -> None: ...

class DoubleLT(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: float
    def __init__(self, val: _Optional[float] = ...) -> None: ...

class DoubleLTE(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: float
    def __init__(self, val: _Optional[float] = ...) -> None: ...

class DoubleGT(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: float
    def __init__(self, val: _Optional[float] = ...) -> None: ...

class DoubleGTE(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: float
    def __init__(self, val: _Optional[float] = ...) -> None: ...

class DoubleGTLT(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: float
    def __init__(self, val: _Optional[float] = ...) -> None: ...

class DoubleExLTGT(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: float
    def __init__(self, val: _Optional[float] = ...) -> None: ...

class DoubleGTELTE(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: float
    def __init__(self, val: _Optional[float] = ...) -> None: ...

class DoubleExGTELTE(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: float
    def __init__(self, val: _Optional[float] = ...) -> None: ...

class DoubleFinite(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: float
    def __init__(self, val: _Optional[float] = ...) -> None: ...

class DoubleIgnore(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: float
    def __init__(self, val: _Optional[float] = ...) -> None: ...

class DoubleIncorrectType(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: float
    def __init__(self, val: _Optional[float] = ...) -> None: ...

class Int32None(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class Int32Const(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class Int32In(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class Int32NotIn(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class Int32LT(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class Int32LTE(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class Int32GT(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class Int32GTE(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class Int32GTLT(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class Int32ExLTGT(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class Int32GTELTE(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class Int32ExGTELTE(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class Int32Ignore(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class Int32IncorrectType(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class Int64None(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class Int64Const(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class Int64In(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class Int64NotIn(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class Int64LT(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class Int64LTE(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class Int64GT(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class Int64GTE(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class Int64GTLT(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class Int64ExLTGT(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class Int64GTELTE(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class Int64ExGTELTE(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class Int64Ignore(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class Int64IncorrectType(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class UInt32None(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class UInt32Const(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class UInt32In(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class UInt32NotIn(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class UInt32LT(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class UInt32LTE(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class UInt32GT(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class UInt32GTE(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class UInt32GTLT(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class UInt32ExLTGT(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class UInt32GTELTE(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class UInt32ExGTELTE(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class UInt32Ignore(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class UInt32IncorrectType(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class UInt64None(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class UInt64Const(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class UInt64In(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class UInt64NotIn(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class UInt64LT(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class UInt64LTE(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class UInt64GT(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class UInt64GTE(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class UInt64GTLT(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class UInt64ExLTGT(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class UInt64GTELTE(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class UInt64ExGTELTE(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class UInt64Ignore(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class UInt64IncorrectType(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class SInt32None(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class SInt32Const(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class SInt32In(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class SInt32NotIn(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class SInt32LT(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class SInt32LTE(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class SInt32GT(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class SInt32GTE(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class SInt32GTLT(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class SInt32ExLTGT(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class SInt32GTELTE(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class SInt32ExGTELTE(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class SInt32Ignore(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class SInt32IncorrectType(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class SInt64None(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class SInt64Const(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class SInt64In(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class SInt64NotIn(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class SInt64LT(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class SInt64LTE(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class SInt64GT(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class SInt64GTE(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class SInt64GTLT(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class SInt64ExLTGT(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class SInt64GTELTE(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class SInt64ExGTELTE(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class SInt64Ignore(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class SInt64IncorrectType(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class Fixed32None(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class Fixed32Const(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class Fixed32In(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class Fixed32NotIn(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class Fixed32LT(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class Fixed32LTE(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class Fixed32GT(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class Fixed32GTE(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class Fixed32GTLT(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class Fixed32ExLTGT(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class Fixed32GTELTE(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class Fixed32ExGTELTE(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class Fixed32Ignore(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class Fixed32IncorrectType(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class Fixed64None(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class Fixed64Const(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class Fixed64In(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class Fixed64NotIn(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class Fixed64LT(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class Fixed64LTE(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class Fixed64GT(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class Fixed64GTE(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class Fixed64GTLT(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class Fixed64ExLTGT(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class Fixed64GTELTE(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class Fixed64ExGTELTE(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class Fixed64Ignore(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class Fixed64IncorrectType(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class SFixed32None(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class SFixed32Const(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class SFixed32In(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class SFixed32NotIn(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class SFixed32LT(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class SFixed32LTE(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class SFixed32GT(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class SFixed32GTE(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class SFixed32GTLT(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class SFixed32ExLTGT(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class SFixed32GTELTE(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class SFixed32ExGTELTE(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class SFixed32Ignore(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class SFixed32IncorrectType(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class SFixed64None(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class SFixed64Const(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class SFixed64In(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class SFixed64NotIn(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class SFixed64LT(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class SFixed64LTE(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class SFixed64GT(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class SFixed64GTE(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class SFixed64GTLT(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class SFixed64ExLTGT(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class SFixed64GTELTE(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class SFixed64ExGTELTE(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class SFixed64Ignore(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class SFixed64IncorrectType(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...

class Int64LTEOptional(_message.Message):
    __slots__ = ["val"]
    VAL_FIELD_NUMBER: _ClassVar[int]
    val: int
    def __init__(self, val: _Optional[int] = ...) -> None: ...
