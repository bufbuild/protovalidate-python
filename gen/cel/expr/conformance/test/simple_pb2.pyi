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

from cel.expr import checked_pb2 as _checked_pb2
from cel.expr import eval_pb2 as _eval_pb2
from cel.expr import value_pb2 as _value_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SimpleTestFile(_message.Message):
    __slots__ = ("name", "description", "section")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SECTION_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    section: _containers.RepeatedCompositeFieldContainer[SimpleTestSection]
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., section: _Optional[_Iterable[_Union[SimpleTestSection, _Mapping]]] = ...) -> None: ...

class SimpleTestSection(_message.Message):
    __slots__ = ("name", "description", "test")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TEST_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    test: _containers.RepeatedCompositeFieldContainer[SimpleTest]
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., test: _Optional[_Iterable[_Union[SimpleTest, _Mapping]]] = ...) -> None: ...

class SimpleTest(_message.Message):
    __slots__ = ("name", "description", "expr", "disable_macros", "disable_check", "check_only", "type_env", "container", "locale", "bindings", "value", "typed_result", "eval_error", "any_eval_errors", "unknown", "any_unknowns")
    class BindingsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _eval_pb2.ExprValue
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_eval_pb2.ExprValue, _Mapping]] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    EXPR_FIELD_NUMBER: _ClassVar[int]
    DISABLE_MACROS_FIELD_NUMBER: _ClassVar[int]
    DISABLE_CHECK_FIELD_NUMBER: _ClassVar[int]
    CHECK_ONLY_FIELD_NUMBER: _ClassVar[int]
    TYPE_ENV_FIELD_NUMBER: _ClassVar[int]
    CONTAINER_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    BINDINGS_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    TYPED_RESULT_FIELD_NUMBER: _ClassVar[int]
    EVAL_ERROR_FIELD_NUMBER: _ClassVar[int]
    ANY_EVAL_ERRORS_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_FIELD_NUMBER: _ClassVar[int]
    ANY_UNKNOWNS_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    expr: str
    disable_macros: bool
    disable_check: bool
    check_only: bool
    type_env: _containers.RepeatedCompositeFieldContainer[_checked_pb2.Decl]
    container: str
    locale: str
    bindings: _containers.MessageMap[str, _eval_pb2.ExprValue]
    value: _value_pb2.Value
    typed_result: TypedResult
    eval_error: _eval_pb2.ErrorSet
    any_eval_errors: ErrorSetMatcher
    unknown: _eval_pb2.UnknownSet
    any_unknowns: UnknownSetMatcher
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., expr: _Optional[str] = ..., disable_macros: bool = ..., disable_check: bool = ..., check_only: bool = ..., type_env: _Optional[_Iterable[_Union[_checked_pb2.Decl, _Mapping]]] = ..., container: _Optional[str] = ..., locale: _Optional[str] = ..., bindings: _Optional[_Mapping[str, _eval_pb2.ExprValue]] = ..., value: _Optional[_Union[_value_pb2.Value, _Mapping]] = ..., typed_result: _Optional[_Union[TypedResult, _Mapping]] = ..., eval_error: _Optional[_Union[_eval_pb2.ErrorSet, _Mapping]] = ..., any_eval_errors: _Optional[_Union[ErrorSetMatcher, _Mapping]] = ..., unknown: _Optional[_Union[_eval_pb2.UnknownSet, _Mapping]] = ..., any_unknowns: _Optional[_Union[UnknownSetMatcher, _Mapping]] = ...) -> None: ...

class TypedResult(_message.Message):
    __slots__ = ("result", "deduced_type")
    RESULT_FIELD_NUMBER: _ClassVar[int]
    DEDUCED_TYPE_FIELD_NUMBER: _ClassVar[int]
    result: _value_pb2.Value
    deduced_type: _checked_pb2.Type
    def __init__(self, result: _Optional[_Union[_value_pb2.Value, _Mapping]] = ..., deduced_type: _Optional[_Union[_checked_pb2.Type, _Mapping]] = ...) -> None: ...

class ErrorSetMatcher(_message.Message):
    __slots__ = ("errors",)
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    errors: _containers.RepeatedCompositeFieldContainer[_eval_pb2.ErrorSet]
    def __init__(self, errors: _Optional[_Iterable[_Union[_eval_pb2.ErrorSet, _Mapping]]] = ...) -> None: ...

class UnknownSetMatcher(_message.Message):
    __slots__ = ("unknowns",)
    UNKNOWNS_FIELD_NUMBER: _ClassVar[int]
    unknowns: _containers.RepeatedCompositeFieldContainer[_eval_pb2.UnknownSet]
    def __init__(self, unknowns: _Optional[_Iterable[_Union[_eval_pb2.UnknownSet, _Mapping]]] = ...) -> None: ...
