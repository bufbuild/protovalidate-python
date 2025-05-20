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

from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ParsedExpr(_message.Message):
    __slots__ = ("expr", "source_info")
    EXPR_FIELD_NUMBER: _ClassVar[int]
    SOURCE_INFO_FIELD_NUMBER: _ClassVar[int]
    expr: Expr
    source_info: SourceInfo
    def __init__(self, expr: _Optional[_Union[Expr, _Mapping]] = ..., source_info: _Optional[_Union[SourceInfo, _Mapping]] = ...) -> None: ...

class Expr(_message.Message):
    __slots__ = ("id", "const_expr", "ident_expr", "select_expr", "call_expr", "list_expr", "struct_expr", "comprehension_expr")
    class Ident(_message.Message):
        __slots__ = ("name",)
        NAME_FIELD_NUMBER: _ClassVar[int]
        name: str
        def __init__(self, name: _Optional[str] = ...) -> None: ...
    class Select(_message.Message):
        __slots__ = ("operand", "field", "test_only")
        OPERAND_FIELD_NUMBER: _ClassVar[int]
        FIELD_FIELD_NUMBER: _ClassVar[int]
        TEST_ONLY_FIELD_NUMBER: _ClassVar[int]
        operand: Expr
        field: str
        test_only: bool
        def __init__(self, operand: _Optional[_Union[Expr, _Mapping]] = ..., field: _Optional[str] = ..., test_only: bool = ...) -> None: ...
    class Call(_message.Message):
        __slots__ = ("target", "function", "args")
        TARGET_FIELD_NUMBER: _ClassVar[int]
        FUNCTION_FIELD_NUMBER: _ClassVar[int]
        ARGS_FIELD_NUMBER: _ClassVar[int]
        target: Expr
        function: str
        args: _containers.RepeatedCompositeFieldContainer[Expr]
        def __init__(self, target: _Optional[_Union[Expr, _Mapping]] = ..., function: _Optional[str] = ..., args: _Optional[_Iterable[_Union[Expr, _Mapping]]] = ...) -> None: ...
    class CreateList(_message.Message):
        __slots__ = ("elements", "optional_indices")
        ELEMENTS_FIELD_NUMBER: _ClassVar[int]
        OPTIONAL_INDICES_FIELD_NUMBER: _ClassVar[int]
        elements: _containers.RepeatedCompositeFieldContainer[Expr]
        optional_indices: _containers.RepeatedScalarFieldContainer[int]
        def __init__(self, elements: _Optional[_Iterable[_Union[Expr, _Mapping]]] = ..., optional_indices: _Optional[_Iterable[int]] = ...) -> None: ...
    class CreateStruct(_message.Message):
        __slots__ = ("message_name", "entries")
        class Entry(_message.Message):
            __slots__ = ("id", "field_key", "map_key", "value", "optional_entry")
            ID_FIELD_NUMBER: _ClassVar[int]
            FIELD_KEY_FIELD_NUMBER: _ClassVar[int]
            MAP_KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            OPTIONAL_ENTRY_FIELD_NUMBER: _ClassVar[int]
            id: int
            field_key: str
            map_key: Expr
            value: Expr
            optional_entry: bool
            def __init__(self, id: _Optional[int] = ..., field_key: _Optional[str] = ..., map_key: _Optional[_Union[Expr, _Mapping]] = ..., value: _Optional[_Union[Expr, _Mapping]] = ..., optional_entry: bool = ...) -> None: ...
        MESSAGE_NAME_FIELD_NUMBER: _ClassVar[int]
        ENTRIES_FIELD_NUMBER: _ClassVar[int]
        message_name: str
        entries: _containers.RepeatedCompositeFieldContainer[Expr.CreateStruct.Entry]
        def __init__(self, message_name: _Optional[str] = ..., entries: _Optional[_Iterable[_Union[Expr.CreateStruct.Entry, _Mapping]]] = ...) -> None: ...
    class Comprehension(_message.Message):
        __slots__ = ("iter_var", "iter_var2", "iter_range", "accu_var", "accu_init", "loop_condition", "loop_step", "result")
        ITER_VAR_FIELD_NUMBER: _ClassVar[int]
        ITER_VAR2_FIELD_NUMBER: _ClassVar[int]
        ITER_RANGE_FIELD_NUMBER: _ClassVar[int]
        ACCU_VAR_FIELD_NUMBER: _ClassVar[int]
        ACCU_INIT_FIELD_NUMBER: _ClassVar[int]
        LOOP_CONDITION_FIELD_NUMBER: _ClassVar[int]
        LOOP_STEP_FIELD_NUMBER: _ClassVar[int]
        RESULT_FIELD_NUMBER: _ClassVar[int]
        iter_var: str
        iter_var2: str
        iter_range: Expr
        accu_var: str
        accu_init: Expr
        loop_condition: Expr
        loop_step: Expr
        result: Expr
        def __init__(self, iter_var: _Optional[str] = ..., iter_var2: _Optional[str] = ..., iter_range: _Optional[_Union[Expr, _Mapping]] = ..., accu_var: _Optional[str] = ..., accu_init: _Optional[_Union[Expr, _Mapping]] = ..., loop_condition: _Optional[_Union[Expr, _Mapping]] = ..., loop_step: _Optional[_Union[Expr, _Mapping]] = ..., result: _Optional[_Union[Expr, _Mapping]] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    CONST_EXPR_FIELD_NUMBER: _ClassVar[int]
    IDENT_EXPR_FIELD_NUMBER: _ClassVar[int]
    SELECT_EXPR_FIELD_NUMBER: _ClassVar[int]
    CALL_EXPR_FIELD_NUMBER: _ClassVar[int]
    LIST_EXPR_FIELD_NUMBER: _ClassVar[int]
    STRUCT_EXPR_FIELD_NUMBER: _ClassVar[int]
    COMPREHENSION_EXPR_FIELD_NUMBER: _ClassVar[int]
    id: int
    const_expr: Constant
    ident_expr: Expr.Ident
    select_expr: Expr.Select
    call_expr: Expr.Call
    list_expr: Expr.CreateList
    struct_expr: Expr.CreateStruct
    comprehension_expr: Expr.Comprehension
    def __init__(self, id: _Optional[int] = ..., const_expr: _Optional[_Union[Constant, _Mapping]] = ..., ident_expr: _Optional[_Union[Expr.Ident, _Mapping]] = ..., select_expr: _Optional[_Union[Expr.Select, _Mapping]] = ..., call_expr: _Optional[_Union[Expr.Call, _Mapping]] = ..., list_expr: _Optional[_Union[Expr.CreateList, _Mapping]] = ..., struct_expr: _Optional[_Union[Expr.CreateStruct, _Mapping]] = ..., comprehension_expr: _Optional[_Union[Expr.Comprehension, _Mapping]] = ...) -> None: ...

class Constant(_message.Message):
    __slots__ = ("null_value", "bool_value", "int64_value", "uint64_value", "double_value", "string_value", "bytes_value", "duration_value", "timestamp_value")
    NULL_VALUE_FIELD_NUMBER: _ClassVar[int]
    BOOL_VALUE_FIELD_NUMBER: _ClassVar[int]
    INT64_VALUE_FIELD_NUMBER: _ClassVar[int]
    UINT64_VALUE_FIELD_NUMBER: _ClassVar[int]
    DOUBLE_VALUE_FIELD_NUMBER: _ClassVar[int]
    STRING_VALUE_FIELD_NUMBER: _ClassVar[int]
    BYTES_VALUE_FIELD_NUMBER: _ClassVar[int]
    DURATION_VALUE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_VALUE_FIELD_NUMBER: _ClassVar[int]
    null_value: _struct_pb2.NullValue
    bool_value: bool
    int64_value: int
    uint64_value: int
    double_value: float
    string_value: str
    bytes_value: bytes
    duration_value: _duration_pb2.Duration
    timestamp_value: _timestamp_pb2.Timestamp
    def __init__(self, null_value: _Optional[_Union[_struct_pb2.NullValue, str]] = ..., bool_value: bool = ..., int64_value: _Optional[int] = ..., uint64_value: _Optional[int] = ..., double_value: _Optional[float] = ..., string_value: _Optional[str] = ..., bytes_value: _Optional[bytes] = ..., duration_value: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., timestamp_value: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class SourceInfo(_message.Message):
    __slots__ = ("syntax_version", "location", "line_offsets", "positions", "macro_calls", "extensions")
    class PositionsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    class MacroCallsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: Expr
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[Expr, _Mapping]] = ...) -> None: ...
    class Extension(_message.Message):
        __slots__ = ("id", "affected_components", "version")
        class Component(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            COMPONENT_UNSPECIFIED: _ClassVar[SourceInfo.Extension.Component]
            COMPONENT_PARSER: _ClassVar[SourceInfo.Extension.Component]
            COMPONENT_TYPE_CHECKER: _ClassVar[SourceInfo.Extension.Component]
            COMPONENT_RUNTIME: _ClassVar[SourceInfo.Extension.Component]
        COMPONENT_UNSPECIFIED: SourceInfo.Extension.Component
        COMPONENT_PARSER: SourceInfo.Extension.Component
        COMPONENT_TYPE_CHECKER: SourceInfo.Extension.Component
        COMPONENT_RUNTIME: SourceInfo.Extension.Component
        class Version(_message.Message):
            __slots__ = ("major", "minor")
            MAJOR_FIELD_NUMBER: _ClassVar[int]
            MINOR_FIELD_NUMBER: _ClassVar[int]
            major: int
            minor: int
            def __init__(self, major: _Optional[int] = ..., minor: _Optional[int] = ...) -> None: ...
        ID_FIELD_NUMBER: _ClassVar[int]
        AFFECTED_COMPONENTS_FIELD_NUMBER: _ClassVar[int]
        VERSION_FIELD_NUMBER: _ClassVar[int]
        id: str
        affected_components: _containers.RepeatedScalarFieldContainer[SourceInfo.Extension.Component]
        version: SourceInfo.Extension.Version
        def __init__(self, id: _Optional[str] = ..., affected_components: _Optional[_Iterable[_Union[SourceInfo.Extension.Component, str]]] = ..., version: _Optional[_Union[SourceInfo.Extension.Version, _Mapping]] = ...) -> None: ...
    SYNTAX_VERSION_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    LINE_OFFSETS_FIELD_NUMBER: _ClassVar[int]
    POSITIONS_FIELD_NUMBER: _ClassVar[int]
    MACRO_CALLS_FIELD_NUMBER: _ClassVar[int]
    EXTENSIONS_FIELD_NUMBER: _ClassVar[int]
    syntax_version: str
    location: str
    line_offsets: _containers.RepeatedScalarFieldContainer[int]
    positions: _containers.ScalarMap[int, int]
    macro_calls: _containers.MessageMap[int, Expr]
    extensions: _containers.RepeatedCompositeFieldContainer[SourceInfo.Extension]
    def __init__(self, syntax_version: _Optional[str] = ..., location: _Optional[str] = ..., line_offsets: _Optional[_Iterable[int]] = ..., positions: _Optional[_Mapping[int, int]] = ..., macro_calls: _Optional[_Mapping[int, Expr]] = ..., extensions: _Optional[_Iterable[_Union[SourceInfo.Extension, _Mapping]]] = ...) -> None: ...
