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

from cel.expr import syntax_pb2 as _syntax_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CheckedExpr(_message.Message):
    __slots__ = ("reference_map", "type_map", "source_info", "expr_version", "expr")
    class ReferenceMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: Reference
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[Reference, _Mapping]] = ...) -> None: ...
    class TypeMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: Type
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[Type, _Mapping]] = ...) -> None: ...
    REFERENCE_MAP_FIELD_NUMBER: _ClassVar[int]
    TYPE_MAP_FIELD_NUMBER: _ClassVar[int]
    SOURCE_INFO_FIELD_NUMBER: _ClassVar[int]
    EXPR_VERSION_FIELD_NUMBER: _ClassVar[int]
    EXPR_FIELD_NUMBER: _ClassVar[int]
    reference_map: _containers.MessageMap[int, Reference]
    type_map: _containers.MessageMap[int, Type]
    source_info: _syntax_pb2.SourceInfo
    expr_version: str
    expr: _syntax_pb2.Expr
    def __init__(self, reference_map: _Optional[_Mapping[int, Reference]] = ..., type_map: _Optional[_Mapping[int, Type]] = ..., source_info: _Optional[_Union[_syntax_pb2.SourceInfo, _Mapping]] = ..., expr_version: _Optional[str] = ..., expr: _Optional[_Union[_syntax_pb2.Expr, _Mapping]] = ...) -> None: ...

class Type(_message.Message):
    __slots__ = ("dyn", "null", "primitive", "wrapper", "well_known", "list_type", "map_type", "function", "message_type", "type_param", "type", "error", "abstract_type")
    class PrimitiveType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PRIMITIVE_TYPE_UNSPECIFIED: _ClassVar[Type.PrimitiveType]
        BOOL: _ClassVar[Type.PrimitiveType]
        INT64: _ClassVar[Type.PrimitiveType]
        UINT64: _ClassVar[Type.PrimitiveType]
        DOUBLE: _ClassVar[Type.PrimitiveType]
        STRING: _ClassVar[Type.PrimitiveType]
        BYTES: _ClassVar[Type.PrimitiveType]
    PRIMITIVE_TYPE_UNSPECIFIED: Type.PrimitiveType
    BOOL: Type.PrimitiveType
    INT64: Type.PrimitiveType
    UINT64: Type.PrimitiveType
    DOUBLE: Type.PrimitiveType
    STRING: Type.PrimitiveType
    BYTES: Type.PrimitiveType
    class WellKnownType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        WELL_KNOWN_TYPE_UNSPECIFIED: _ClassVar[Type.WellKnownType]
        ANY: _ClassVar[Type.WellKnownType]
        TIMESTAMP: _ClassVar[Type.WellKnownType]
        DURATION: _ClassVar[Type.WellKnownType]
    WELL_KNOWN_TYPE_UNSPECIFIED: Type.WellKnownType
    ANY: Type.WellKnownType
    TIMESTAMP: Type.WellKnownType
    DURATION: Type.WellKnownType
    class ListType(_message.Message):
        __slots__ = ("elem_type",)
        ELEM_TYPE_FIELD_NUMBER: _ClassVar[int]
        elem_type: Type
        def __init__(self, elem_type: _Optional[_Union[Type, _Mapping]] = ...) -> None: ...
    class MapType(_message.Message):
        __slots__ = ("key_type", "value_type")
        KEY_TYPE_FIELD_NUMBER: _ClassVar[int]
        VALUE_TYPE_FIELD_NUMBER: _ClassVar[int]
        key_type: Type
        value_type: Type
        def __init__(self, key_type: _Optional[_Union[Type, _Mapping]] = ..., value_type: _Optional[_Union[Type, _Mapping]] = ...) -> None: ...
    class FunctionType(_message.Message):
        __slots__ = ("result_type", "arg_types")
        RESULT_TYPE_FIELD_NUMBER: _ClassVar[int]
        ARG_TYPES_FIELD_NUMBER: _ClassVar[int]
        result_type: Type
        arg_types: _containers.RepeatedCompositeFieldContainer[Type]
        def __init__(self, result_type: _Optional[_Union[Type, _Mapping]] = ..., arg_types: _Optional[_Iterable[_Union[Type, _Mapping]]] = ...) -> None: ...
    class AbstractType(_message.Message):
        __slots__ = ("name", "parameter_types")
        NAME_FIELD_NUMBER: _ClassVar[int]
        PARAMETER_TYPES_FIELD_NUMBER: _ClassVar[int]
        name: str
        parameter_types: _containers.RepeatedCompositeFieldContainer[Type]
        def __init__(self, name: _Optional[str] = ..., parameter_types: _Optional[_Iterable[_Union[Type, _Mapping]]] = ...) -> None: ...
    DYN_FIELD_NUMBER: _ClassVar[int]
    NULL_FIELD_NUMBER: _ClassVar[int]
    PRIMITIVE_FIELD_NUMBER: _ClassVar[int]
    WRAPPER_FIELD_NUMBER: _ClassVar[int]
    WELL_KNOWN_FIELD_NUMBER: _ClassVar[int]
    LIST_TYPE_FIELD_NUMBER: _ClassVar[int]
    MAP_TYPE_FIELD_NUMBER: _ClassVar[int]
    FUNCTION_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    TYPE_PARAM_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ABSTRACT_TYPE_FIELD_NUMBER: _ClassVar[int]
    dyn: _empty_pb2.Empty
    null: _struct_pb2.NullValue
    primitive: Type.PrimitiveType
    wrapper: Type.PrimitiveType
    well_known: Type.WellKnownType
    list_type: Type.ListType
    map_type: Type.MapType
    function: Type.FunctionType
    message_type: str
    type_param: str
    type: Type
    error: _empty_pb2.Empty
    abstract_type: Type.AbstractType
    def __init__(self, dyn: _Optional[_Union[_empty_pb2.Empty, _Mapping]] = ..., null: _Optional[_Union[_struct_pb2.NullValue, str]] = ..., primitive: _Optional[_Union[Type.PrimitiveType, str]] = ..., wrapper: _Optional[_Union[Type.PrimitiveType, str]] = ..., well_known: _Optional[_Union[Type.WellKnownType, str]] = ..., list_type: _Optional[_Union[Type.ListType, _Mapping]] = ..., map_type: _Optional[_Union[Type.MapType, _Mapping]] = ..., function: _Optional[_Union[Type.FunctionType, _Mapping]] = ..., message_type: _Optional[str] = ..., type_param: _Optional[str] = ..., type: _Optional[_Union[Type, _Mapping]] = ..., error: _Optional[_Union[_empty_pb2.Empty, _Mapping]] = ..., abstract_type: _Optional[_Union[Type.AbstractType, _Mapping]] = ...) -> None: ...

class Decl(_message.Message):
    __slots__ = ("name", "ident", "function")
    class IdentDecl(_message.Message):
        __slots__ = ("type", "value", "doc")
        TYPE_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        DOC_FIELD_NUMBER: _ClassVar[int]
        type: Type
        value: _syntax_pb2.Constant
        doc: str
        def __init__(self, type: _Optional[_Union[Type, _Mapping]] = ..., value: _Optional[_Union[_syntax_pb2.Constant, _Mapping]] = ..., doc: _Optional[str] = ...) -> None: ...
    class FunctionDecl(_message.Message):
        __slots__ = ("overloads", "doc")
        class Overload(_message.Message):
            __slots__ = ("overload_id", "params", "type_params", "result_type", "is_instance_function", "doc")
            OVERLOAD_ID_FIELD_NUMBER: _ClassVar[int]
            PARAMS_FIELD_NUMBER: _ClassVar[int]
            TYPE_PARAMS_FIELD_NUMBER: _ClassVar[int]
            RESULT_TYPE_FIELD_NUMBER: _ClassVar[int]
            IS_INSTANCE_FUNCTION_FIELD_NUMBER: _ClassVar[int]
            DOC_FIELD_NUMBER: _ClassVar[int]
            overload_id: str
            params: _containers.RepeatedCompositeFieldContainer[Type]
            type_params: _containers.RepeatedScalarFieldContainer[str]
            result_type: Type
            is_instance_function: bool
            doc: str
            def __init__(self, overload_id: _Optional[str] = ..., params: _Optional[_Iterable[_Union[Type, _Mapping]]] = ..., type_params: _Optional[_Iterable[str]] = ..., result_type: _Optional[_Union[Type, _Mapping]] = ..., is_instance_function: bool = ..., doc: _Optional[str] = ...) -> None: ...
        OVERLOADS_FIELD_NUMBER: _ClassVar[int]
        DOC_FIELD_NUMBER: _ClassVar[int]
        overloads: _containers.RepeatedCompositeFieldContainer[Decl.FunctionDecl.Overload]
        doc: str
        def __init__(self, overloads: _Optional[_Iterable[_Union[Decl.FunctionDecl.Overload, _Mapping]]] = ..., doc: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    IDENT_FIELD_NUMBER: _ClassVar[int]
    FUNCTION_FIELD_NUMBER: _ClassVar[int]
    name: str
    ident: Decl.IdentDecl
    function: Decl.FunctionDecl
    def __init__(self, name: _Optional[str] = ..., ident: _Optional[_Union[Decl.IdentDecl, _Mapping]] = ..., function: _Optional[_Union[Decl.FunctionDecl, _Mapping]] = ...) -> None: ...

class Reference(_message.Message):
    __slots__ = ("name", "overload_id", "value")
    NAME_FIELD_NUMBER: _ClassVar[int]
    OVERLOAD_ID_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    name: str
    overload_id: _containers.RepeatedScalarFieldContainer[str]
    value: _syntax_pb2.Constant
    def __init__(self, name: _Optional[str] = ..., overload_id: _Optional[_Iterable[str]] = ..., value: _Optional[_Union[_syntax_pb2.Constant, _Mapping]] = ...) -> None: ...
