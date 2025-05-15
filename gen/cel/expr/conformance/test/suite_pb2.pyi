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
from cel.expr.conformance import env_config_pb2 as _env_config_pb2
from google.protobuf import any_pb2 as _any_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TestSuite(_message.Message):
    __slots__ = ("name", "description", "sections")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SECTIONS_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    sections: _containers.RepeatedCompositeFieldContainer[TestSection]
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., sections: _Optional[_Iterable[_Union[TestSection, _Mapping]]] = ...) -> None: ...

class TestSection(_message.Message):
    __slots__ = ("name", "description", "tests")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TESTS_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    tests: _containers.RepeatedCompositeFieldContainer[TestCase]
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., tests: _Optional[_Iterable[_Union[TestCase, _Mapping]]] = ...) -> None: ...

class TestCase(_message.Message):
    __slots__ = ("name", "description", "expr", "env", "input", "input_context", "output", "deduced_type", "disable_check")
    class InputEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: InputValue
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[InputValue, _Mapping]] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    EXPR_FIELD_NUMBER: _ClassVar[int]
    ENV_FIELD_NUMBER: _ClassVar[int]
    INPUT_FIELD_NUMBER: _ClassVar[int]
    INPUT_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_FIELD_NUMBER: _ClassVar[int]
    DEDUCED_TYPE_FIELD_NUMBER: _ClassVar[int]
    DISABLE_CHECK_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    expr: str
    env: _env_config_pb2.Environment
    input: _containers.MessageMap[str, InputValue]
    input_context: InputContext
    output: TestOutput
    deduced_type: _checked_pb2.Type
    disable_check: bool
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., expr: _Optional[str] = ..., env: _Optional[_Union[_env_config_pb2.Environment, _Mapping]] = ..., input: _Optional[_Mapping[str, InputValue]] = ..., input_context: _Optional[_Union[InputContext, _Mapping]] = ..., output: _Optional[_Union[TestOutput, _Mapping]] = ..., deduced_type: _Optional[_Union[_checked_pb2.Type, _Mapping]] = ..., disable_check: bool = ...) -> None: ...

class InputContext(_message.Message):
    __slots__ = ("context_message", "context_expr")
    CONTEXT_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_EXPR_FIELD_NUMBER: _ClassVar[int]
    context_message: _any_pb2.Any
    context_expr: str
    def __init__(self, context_message: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., context_expr: _Optional[str] = ...) -> None: ...

class InputValue(_message.Message):
    __slots__ = ("value", "expr")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    EXPR_FIELD_NUMBER: _ClassVar[int]
    value: _value_pb2.Value
    expr: str
    def __init__(self, value: _Optional[_Union[_value_pb2.Value, _Mapping]] = ..., expr: _Optional[str] = ...) -> None: ...

class TestOutput(_message.Message):
    __slots__ = ("result_value", "result_expr", "eval_error", "unknown")
    RESULT_VALUE_FIELD_NUMBER: _ClassVar[int]
    RESULT_EXPR_FIELD_NUMBER: _ClassVar[int]
    EVAL_ERROR_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_FIELD_NUMBER: _ClassVar[int]
    result_value: _value_pb2.Value
    result_expr: str
    eval_error: _eval_pb2.ErrorSet
    unknown: _eval_pb2.UnknownSet
    def __init__(self, result_value: _Optional[_Union[_value_pb2.Value, _Mapping]] = ..., result_expr: _Optional[str] = ..., eval_error: _Optional[_Union[_eval_pb2.ErrorSet, _Mapping]] = ..., unknown: _Optional[_Union[_eval_pb2.UnknownSet, _Mapping]] = ...) -> None: ...
