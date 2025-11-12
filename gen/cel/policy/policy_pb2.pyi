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

from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PolicySpec(_message.Message):
    __slots__ = ("name", "imports", "variables", "output", "description", "explanation", "match", "rule")
    class Import(_message.Message):
        __slots__ = ("name",)
        NAME_FIELD_NUMBER: _ClassVar[int]
        name: str
        def __init__(self, name: _Optional[str] = ...) -> None: ...
    class Variable(_message.Message):
        __slots__ = ("name", "description", "expression")
        NAME_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        EXPRESSION_FIELD_NUMBER: _ClassVar[int]
        name: str
        description: str
        expression: str
        def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., expression: _Optional[str] = ...) -> None: ...
    class Rule(_message.Message):
        __slots__ = ("id", "description", "variables", "match")
        ID_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        VARIABLES_FIELD_NUMBER: _ClassVar[int]
        MATCH_FIELD_NUMBER: _ClassVar[int]
        id: str
        description: str
        variables: _containers.RepeatedCompositeFieldContainer[PolicySpec.Variable]
        match: _containers.RepeatedCompositeFieldContainer[PolicySpec.Match]
        def __init__(self, id: _Optional[str] = ..., description: _Optional[str] = ..., variables: _Optional[_Iterable[_Union[PolicySpec.Variable, _Mapping]]] = ..., match: _Optional[_Iterable[_Union[PolicySpec.Match, _Mapping]]] = ...) -> None: ...
    class Match(_message.Message):
        __slots__ = ("condition", "output", "rule", "explanation")
        CONDITION_FIELD_NUMBER: _ClassVar[int]
        OUTPUT_FIELD_NUMBER: _ClassVar[int]
        RULE_FIELD_NUMBER: _ClassVar[int]
        EXPLANATION_FIELD_NUMBER: _ClassVar[int]
        condition: str
        output: str
        rule: PolicySpec.Rule
        explanation: str
        def __init__(self, condition: _Optional[str] = ..., output: _Optional[str] = ..., rule: _Optional[_Union[PolicySpec.Rule, _Mapping]] = ..., explanation: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    IMPORTS_FIELD_NUMBER: _ClassVar[int]
    VARIABLES_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    EXPLANATION_FIELD_NUMBER: _ClassVar[int]
    MATCH_FIELD_NUMBER: _ClassVar[int]
    RULE_FIELD_NUMBER: _ClassVar[int]
    name: str
    imports: _containers.RepeatedCompositeFieldContainer[PolicySpec.Import]
    variables: _containers.RepeatedCompositeFieldContainer[PolicySpec.Variable]
    output: str
    description: str
    explanation: str
    match: _containers.RepeatedCompositeFieldContainer[PolicySpec.Match]
    rule: PolicySpec.Rule
    def __init__(self, name: _Optional[str] = ..., imports: _Optional[_Iterable[_Union[PolicySpec.Import, _Mapping]]] = ..., variables: _Optional[_Iterable[_Union[PolicySpec.Variable, _Mapping]]] = ..., output: _Optional[str] = ..., description: _Optional[str] = ..., explanation: _Optional[str] = ..., match: _Optional[_Iterable[_Union[PolicySpec.Match, _Mapping]]] = ..., rule: _Optional[_Union[PolicySpec.Rule, _Mapping]] = ...) -> None: ...
