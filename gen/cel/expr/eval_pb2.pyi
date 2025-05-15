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

from google.protobuf import any_pb2 as _any_pb2
from cel.expr import value_pb2 as _value_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EvalState(_message.Message):
    __slots__ = ("values", "results")
    class Result(_message.Message):
        __slots__ = ("expr", "value")
        EXPR_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        expr: int
        value: int
        def __init__(self, expr: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    VALUES_FIELD_NUMBER: _ClassVar[int]
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedCompositeFieldContainer[ExprValue]
    results: _containers.RepeatedCompositeFieldContainer[EvalState.Result]
    def __init__(self, values: _Optional[_Iterable[_Union[ExprValue, _Mapping]]] = ..., results: _Optional[_Iterable[_Union[EvalState.Result, _Mapping]]] = ...) -> None: ...

class ExprValue(_message.Message):
    __slots__ = ("value", "error", "unknown")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_FIELD_NUMBER: _ClassVar[int]
    value: _value_pb2.Value
    error: ErrorSet
    unknown: UnknownSet
    def __init__(self, value: _Optional[_Union[_value_pb2.Value, _Mapping]] = ..., error: _Optional[_Union[ErrorSet, _Mapping]] = ..., unknown: _Optional[_Union[UnknownSet, _Mapping]] = ...) -> None: ...

class ErrorSet(_message.Message):
    __slots__ = ("errors",)
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    errors: _containers.RepeatedCompositeFieldContainer[Status]
    def __init__(self, errors: _Optional[_Iterable[_Union[Status, _Mapping]]] = ...) -> None: ...

class Status(_message.Message):
    __slots__ = ("code", "message", "details")
    CODE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    code: int
    message: str
    details: _containers.RepeatedCompositeFieldContainer[_any_pb2.Any]
    def __init__(self, code: _Optional[int] = ..., message: _Optional[str] = ..., details: _Optional[_Iterable[_Union[_any_pb2.Any, _Mapping]]] = ...) -> None: ...

class UnknownSet(_message.Message):
    __slots__ = ("exprs",)
    EXPRS_FIELD_NUMBER: _ClassVar[int]
    exprs: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, exprs: _Optional[_Iterable[int]] = ...) -> None: ...
