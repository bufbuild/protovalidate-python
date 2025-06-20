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

from buf.validate.conformance.harness import harness_pb2 as _harness_pb2
from google.protobuf import any_pb2 as _any_pb2
from google.protobuf import descriptor_pb2 as _descriptor_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ResultOptions(_message.Message):
    __slots__ = ("suite_filter", "case_filter", "verbose", "strict_message", "strict_error")
    SUITE_FILTER_FIELD_NUMBER: _ClassVar[int]
    CASE_FILTER_FIELD_NUMBER: _ClassVar[int]
    VERBOSE_FIELD_NUMBER: _ClassVar[int]
    STRICT_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    STRICT_ERROR_FIELD_NUMBER: _ClassVar[int]
    suite_filter: str
    case_filter: str
    verbose: bool
    strict_message: bool
    strict_error: bool
    def __init__(self, suite_filter: _Optional[str] = ..., case_filter: _Optional[str] = ..., verbose: bool = ..., strict_message: bool = ..., strict_error: bool = ...) -> None: ...

class ResultSet(_message.Message):
    __slots__ = ("successes", "failures", "suites", "options", "expected_failures")
    SUCCESSES_FIELD_NUMBER: _ClassVar[int]
    FAILURES_FIELD_NUMBER: _ClassVar[int]
    SUITES_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_FAILURES_FIELD_NUMBER: _ClassVar[int]
    successes: int
    failures: int
    suites: _containers.RepeatedCompositeFieldContainer[SuiteResults]
    options: ResultOptions
    expected_failures: int
    def __init__(self, successes: _Optional[int] = ..., failures: _Optional[int] = ..., suites: _Optional[_Iterable[_Union[SuiteResults, _Mapping]]] = ..., options: _Optional[_Union[ResultOptions, _Mapping]] = ..., expected_failures: _Optional[int] = ...) -> None: ...

class SuiteResults(_message.Message):
    __slots__ = ("name", "successes", "failures", "cases", "fdset", "expected_failures")
    NAME_FIELD_NUMBER: _ClassVar[int]
    SUCCESSES_FIELD_NUMBER: _ClassVar[int]
    FAILURES_FIELD_NUMBER: _ClassVar[int]
    CASES_FIELD_NUMBER: _ClassVar[int]
    FDSET_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_FAILURES_FIELD_NUMBER: _ClassVar[int]
    name: str
    successes: int
    failures: int
    cases: _containers.RepeatedCompositeFieldContainer[CaseResult]
    fdset: _descriptor_pb2.FileDescriptorSet
    expected_failures: int
    def __init__(self, name: _Optional[str] = ..., successes: _Optional[int] = ..., failures: _Optional[int] = ..., cases: _Optional[_Iterable[_Union[CaseResult, _Mapping]]] = ..., fdset: _Optional[_Union[_descriptor_pb2.FileDescriptorSet, _Mapping]] = ..., expected_failures: _Optional[int] = ...) -> None: ...

class CaseResult(_message.Message):
    __slots__ = ("name", "success", "wanted", "got", "input", "expected_failure")
    NAME_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    WANTED_FIELD_NUMBER: _ClassVar[int]
    GOT_FIELD_NUMBER: _ClassVar[int]
    INPUT_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_FAILURE_FIELD_NUMBER: _ClassVar[int]
    name: str
    success: bool
    wanted: _harness_pb2.TestResult
    got: _harness_pb2.TestResult
    input: _any_pb2.Any
    expected_failure: bool
    def __init__(self, name: _Optional[str] = ..., success: bool = ..., wanted: _Optional[_Union[_harness_pb2.TestResult, _Mapping]] = ..., got: _Optional[_Union[_harness_pb2.TestResult, _Mapping]] = ..., input: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., expected_failure: bool = ...) -> None: ...
