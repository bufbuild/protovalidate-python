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

from buf.validate import validate_pb2 as _validate_pb2
from google.protobuf import any_pb2 as _any_pb2
from google.protobuf import descriptor_pb2 as _descriptor_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TestConformanceRequest(_message.Message):
    __slots__ = ("fdset", "cases")
    class CasesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _any_pb2.Any
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_any_pb2.Any, _Mapping]] = ...) -> None: ...
    FDSET_FIELD_NUMBER: _ClassVar[int]
    CASES_FIELD_NUMBER: _ClassVar[int]
    fdset: _descriptor_pb2.FileDescriptorSet
    cases: _containers.MessageMap[str, _any_pb2.Any]
    def __init__(self, fdset: _Optional[_Union[_descriptor_pb2.FileDescriptorSet, _Mapping]] = ..., cases: _Optional[_Mapping[str, _any_pb2.Any]] = ...) -> None: ...

class TestConformanceResponse(_message.Message):
    __slots__ = ("results",)
    class ResultsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: TestResult
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[TestResult, _Mapping]] = ...) -> None: ...
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.MessageMap[str, TestResult]
    def __init__(self, results: _Optional[_Mapping[str, TestResult]] = ...) -> None: ...

class TestResult(_message.Message):
    __slots__ = ("success", "validation_error", "compilation_error", "runtime_error", "unexpected_error")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    VALIDATION_ERROR_FIELD_NUMBER: _ClassVar[int]
    COMPILATION_ERROR_FIELD_NUMBER: _ClassVar[int]
    RUNTIME_ERROR_FIELD_NUMBER: _ClassVar[int]
    UNEXPECTED_ERROR_FIELD_NUMBER: _ClassVar[int]
    success: bool
    validation_error: _validate_pb2.Violations
    compilation_error: str
    runtime_error: str
    unexpected_error: str
    def __init__(self, success: bool = ..., validation_error: _Optional[_Union[_validate_pb2.Violations, _Mapping]] = ..., compilation_error: _Optional[str] = ..., runtime_error: _Optional[str] = ..., unexpected_error: _Optional[str] = ...) -> None: ...
