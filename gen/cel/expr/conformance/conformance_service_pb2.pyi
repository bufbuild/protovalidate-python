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
from cel.expr import syntax_pb2 as _syntax_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ParseRequest(_message.Message):
    __slots__ = ("cel_source", "syntax_version", "source_location", "disable_macros")
    CEL_SOURCE_FIELD_NUMBER: _ClassVar[int]
    SYNTAX_VERSION_FIELD_NUMBER: _ClassVar[int]
    SOURCE_LOCATION_FIELD_NUMBER: _ClassVar[int]
    DISABLE_MACROS_FIELD_NUMBER: _ClassVar[int]
    cel_source: str
    syntax_version: str
    source_location: str
    disable_macros: bool
    def __init__(self, cel_source: _Optional[str] = ..., syntax_version: _Optional[str] = ..., source_location: _Optional[str] = ..., disable_macros: bool = ...) -> None: ...

class ParseResponse(_message.Message):
    __slots__ = ("parsed_expr", "issues")
    PARSED_EXPR_FIELD_NUMBER: _ClassVar[int]
    ISSUES_FIELD_NUMBER: _ClassVar[int]
    parsed_expr: _syntax_pb2.ParsedExpr
    issues: _containers.RepeatedCompositeFieldContainer[_status_pb2.Status]
    def __init__(self, parsed_expr: _Optional[_Union[_syntax_pb2.ParsedExpr, _Mapping]] = ..., issues: _Optional[_Iterable[_Union[_status_pb2.Status, _Mapping]]] = ...) -> None: ...

class CheckRequest(_message.Message):
    __slots__ = ("parsed_expr", "type_env", "container", "no_std_env")
    PARSED_EXPR_FIELD_NUMBER: _ClassVar[int]
    TYPE_ENV_FIELD_NUMBER: _ClassVar[int]
    CONTAINER_FIELD_NUMBER: _ClassVar[int]
    NO_STD_ENV_FIELD_NUMBER: _ClassVar[int]
    parsed_expr: _syntax_pb2.ParsedExpr
    type_env: _containers.RepeatedCompositeFieldContainer[_checked_pb2.Decl]
    container: str
    no_std_env: bool
    def __init__(self, parsed_expr: _Optional[_Union[_syntax_pb2.ParsedExpr, _Mapping]] = ..., type_env: _Optional[_Iterable[_Union[_checked_pb2.Decl, _Mapping]]] = ..., container: _Optional[str] = ..., no_std_env: bool = ...) -> None: ...

class CheckResponse(_message.Message):
    __slots__ = ("checked_expr", "issues")
    CHECKED_EXPR_FIELD_NUMBER: _ClassVar[int]
    ISSUES_FIELD_NUMBER: _ClassVar[int]
    checked_expr: _checked_pb2.CheckedExpr
    issues: _containers.RepeatedCompositeFieldContainer[_status_pb2.Status]
    def __init__(self, checked_expr: _Optional[_Union[_checked_pb2.CheckedExpr, _Mapping]] = ..., issues: _Optional[_Iterable[_Union[_status_pb2.Status, _Mapping]]] = ...) -> None: ...

class EvalRequest(_message.Message):
    __slots__ = ("parsed_expr", "checked_expr", "bindings", "container")
    class BindingsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _eval_pb2.ExprValue
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_eval_pb2.ExprValue, _Mapping]] = ...) -> None: ...
    PARSED_EXPR_FIELD_NUMBER: _ClassVar[int]
    CHECKED_EXPR_FIELD_NUMBER: _ClassVar[int]
    BINDINGS_FIELD_NUMBER: _ClassVar[int]
    CONTAINER_FIELD_NUMBER: _ClassVar[int]
    parsed_expr: _syntax_pb2.ParsedExpr
    checked_expr: _checked_pb2.CheckedExpr
    bindings: _containers.MessageMap[str, _eval_pb2.ExprValue]
    container: str
    def __init__(self, parsed_expr: _Optional[_Union[_syntax_pb2.ParsedExpr, _Mapping]] = ..., checked_expr: _Optional[_Union[_checked_pb2.CheckedExpr, _Mapping]] = ..., bindings: _Optional[_Mapping[str, _eval_pb2.ExprValue]] = ..., container: _Optional[str] = ...) -> None: ...

class EvalResponse(_message.Message):
    __slots__ = ("result", "issues")
    RESULT_FIELD_NUMBER: _ClassVar[int]
    ISSUES_FIELD_NUMBER: _ClassVar[int]
    result: _eval_pb2.ExprValue
    issues: _containers.RepeatedCompositeFieldContainer[_status_pb2.Status]
    def __init__(self, result: _Optional[_Union[_eval_pb2.ExprValue, _Mapping]] = ..., issues: _Optional[_Iterable[_Union[_status_pb2.Status, _Mapping]]] = ...) -> None: ...

class SourcePosition(_message.Message):
    __slots__ = ("location", "offset", "line", "column")
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    LINE_FIELD_NUMBER: _ClassVar[int]
    COLUMN_FIELD_NUMBER: _ClassVar[int]
    location: str
    offset: int
    line: int
    column: int
    def __init__(self, location: _Optional[str] = ..., offset: _Optional[int] = ..., line: _Optional[int] = ..., column: _Optional[int] = ...) -> None: ...

class IssueDetails(_message.Message):
    __slots__ = ("severity", "position", "id")
    class Severity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SEVERITY_UNSPECIFIED: _ClassVar[IssueDetails.Severity]
        DEPRECATION: _ClassVar[IssueDetails.Severity]
        WARNING: _ClassVar[IssueDetails.Severity]
        ERROR: _ClassVar[IssueDetails.Severity]
    SEVERITY_UNSPECIFIED: IssueDetails.Severity
    DEPRECATION: IssueDetails.Severity
    WARNING: IssueDetails.Severity
    ERROR: IssueDetails.Severity
    SEVERITY_FIELD_NUMBER: _ClassVar[int]
    POSITION_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    severity: IssueDetails.Severity
    position: SourcePosition
    id: int
    def __init__(self, severity: _Optional[_Union[IssueDetails.Severity, str]] = ..., position: _Optional[_Union[SourcePosition, _Mapping]] = ..., id: _Optional[int] = ...) -> None: ...
