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

from cel.expr import value_pb2 as _value_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Explain(_message.Message):
    __slots__ = ("values", "expr_steps")
    class ExprStep(_message.Message):
        __slots__ = ("id", "value_index")
        ID_FIELD_NUMBER: _ClassVar[int]
        VALUE_INDEX_FIELD_NUMBER: _ClassVar[int]
        id: int
        value_index: int
        def __init__(self, id: _Optional[int] = ..., value_index: _Optional[int] = ...) -> None: ...
    VALUES_FIELD_NUMBER: _ClassVar[int]
    EXPR_STEPS_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedCompositeFieldContainer[_value_pb2.Value]
    expr_steps: _containers.RepeatedCompositeFieldContainer[Explain.ExprStep]
    def __init__(self, values: _Optional[_Iterable[_Union[_value_pb2.Value, _Mapping]]] = ..., expr_steps: _Optional[_Iterable[_Union[Explain.ExprStep, _Mapping]]] = ...) -> None: ...
