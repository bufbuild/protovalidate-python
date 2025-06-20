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
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import descriptor_pb2 as _descriptor_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Environment(_message.Message):
    __slots__ = ("name", "description", "container", "imports", "stdlib", "extensions", "context_variable", "declarations", "validators", "features", "disable_standard_cel_declarations", "message_type_extension", "enable_macro_call_tracking")
    class Import(_message.Message):
        __slots__ = ("name",)
        NAME_FIELD_NUMBER: _ClassVar[int]
        name: str
        def __init__(self, name: _Optional[str] = ...) -> None: ...
    class ContextVariable(_message.Message):
        __slots__ = ("type_name",)
        TYPE_NAME_FIELD_NUMBER: _ClassVar[int]
        type_name: str
        def __init__(self, type_name: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CONTAINER_FIELD_NUMBER: _ClassVar[int]
    IMPORTS_FIELD_NUMBER: _ClassVar[int]
    STDLIB_FIELD_NUMBER: _ClassVar[int]
    EXTENSIONS_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_VARIABLE_FIELD_NUMBER: _ClassVar[int]
    DECLARATIONS_FIELD_NUMBER: _ClassVar[int]
    VALIDATORS_FIELD_NUMBER: _ClassVar[int]
    FEATURES_FIELD_NUMBER: _ClassVar[int]
    DISABLE_STANDARD_CEL_DECLARATIONS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_TYPE_EXTENSION_FIELD_NUMBER: _ClassVar[int]
    ENABLE_MACRO_CALL_TRACKING_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    container: str
    imports: _containers.RepeatedCompositeFieldContainer[Environment.Import]
    stdlib: LibrarySubset
    extensions: _containers.RepeatedCompositeFieldContainer[Extension]
    context_variable: Environment.ContextVariable
    declarations: _containers.RepeatedCompositeFieldContainer[_checked_pb2.Decl]
    validators: _containers.RepeatedCompositeFieldContainer[Validator]
    features: _containers.RepeatedCompositeFieldContainer[Feature]
    disable_standard_cel_declarations: bool
    message_type_extension: _descriptor_pb2.FileDescriptorSet
    enable_macro_call_tracking: bool
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., container: _Optional[str] = ..., imports: _Optional[_Iterable[_Union[Environment.Import, _Mapping]]] = ..., stdlib: _Optional[_Union[LibrarySubset, _Mapping]] = ..., extensions: _Optional[_Iterable[_Union[Extension, _Mapping]]] = ..., context_variable: _Optional[_Union[Environment.ContextVariable, _Mapping]] = ..., declarations: _Optional[_Iterable[_Union[_checked_pb2.Decl, _Mapping]]] = ..., validators: _Optional[_Iterable[_Union[Validator, _Mapping]]] = ..., features: _Optional[_Iterable[_Union[Feature, _Mapping]]] = ..., disable_standard_cel_declarations: bool = ..., message_type_extension: _Optional[_Union[_descriptor_pb2.FileDescriptorSet, _Mapping]] = ..., enable_macro_call_tracking: bool = ...) -> None: ...

class Validator(_message.Message):
    __slots__ = ("name", "config")
    class ConfigEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _struct_pb2.Value
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_struct_pb2.Value, _Mapping]] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    name: str
    config: _containers.MessageMap[str, _struct_pb2.Value]
    def __init__(self, name: _Optional[str] = ..., config: _Optional[_Mapping[str, _struct_pb2.Value]] = ...) -> None: ...

class Feature(_message.Message):
    __slots__ = ("name", "enabled")
    NAME_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    name: str
    enabled: bool
    def __init__(self, name: _Optional[str] = ..., enabled: bool = ...) -> None: ...

class Extension(_message.Message):
    __slots__ = ("name", "version")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    name: str
    version: str
    def __init__(self, name: _Optional[str] = ..., version: _Optional[str] = ...) -> None: ...

class LibrarySubset(_message.Message):
    __slots__ = ("disabled", "disable_macros", "include_macros", "exclude_macros", "include_functions", "exclude_functions")
    DISABLED_FIELD_NUMBER: _ClassVar[int]
    DISABLE_MACROS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_MACROS_FIELD_NUMBER: _ClassVar[int]
    EXCLUDE_MACROS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_FUNCTIONS_FIELD_NUMBER: _ClassVar[int]
    EXCLUDE_FUNCTIONS_FIELD_NUMBER: _ClassVar[int]
    disabled: bool
    disable_macros: bool
    include_macros: _containers.RepeatedScalarFieldContainer[str]
    exclude_macros: _containers.RepeatedScalarFieldContainer[str]
    include_functions: _containers.RepeatedCompositeFieldContainer[_checked_pb2.Decl]
    exclude_functions: _containers.RepeatedCompositeFieldContainer[_checked_pb2.Decl]
    def __init__(self, disabled: bool = ..., disable_macros: bool = ..., include_macros: _Optional[_Iterable[str]] = ..., exclude_macros: _Optional[_Iterable[str]] = ..., include_functions: _Optional[_Iterable[_Union[_checked_pb2.Decl, _Mapping]]] = ..., exclude_functions: _Optional[_Iterable[_Union[_checked_pb2.Decl, _Mapping]]] = ...) -> None: ...
