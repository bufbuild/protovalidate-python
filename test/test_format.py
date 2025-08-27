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

from collections.abc import Iterable, MutableMapping
from itertools import chain
from typing import Any, Optional

import celpy
import pytest
from celpy import celtypes
from google.protobuf import text_format

from gen.cel.expr import eval_pb2
from gen.cel.expr.conformance.test import simple_pb2
from protovalidate.internal import extra_func
from protovalidate.internal.cel_field_presence import InterpretedRunner

# Version of the cel-spec that this implementation is conformant with.
# This should be kept in sync with the version in ../Makefile.
CEL_SPEC_VERSION = "v0.24.0"

skipped_tests = [
    # cel-python seems to have a bug with ints and booleans in the same map which evaluate to the same value
    # which the test data for this test has. For example: {1: 'value1', true: 'value2'}]).
    # This throws an error like:
    # "no such overload: IntType(0) <class 'celpy.celtypes.IntType'> !=
    #    BoolType(False) <class 'celpy.celtypes.BoolType'>",))
    # TODO: Check if this bug is fixed in newer versions of cel-python.
    "map support (all key types)",
]
skipped_error_tests = [
    # cel-python does not support Protobuf messages at the moment and these tests use a MessageType
    # See https://github.com/cloud-custodian/cel-python/issues/43
    "object not allowed",
    "object inside list",
    "object inside map",
]


def load_test_data(file_name: str) -> simple_pb2.SimpleTestFile:
    msg = simple_pb2.SimpleTestFile()
    with open(file_name) as file:
        text_data = file.read()
        text_format.Parse(text_data, msg)
    return msg


def build_variables(bindings: MutableMapping[str, eval_pb2.ExprValue]) -> dict[Any, Any]:
    binder = {}
    for key, value in bindings.items():
        if value.HasField("value"):
            val = value.value
            if val.HasField("string_value"):
                binder[key] = celtypes.StringType(val.string_value)
    return binder


def get_expected_result(test: simple_pb2.SimpleTest) -> Optional[str]:
    if test.HasField("value"):
        val = test.value
        if val.HasField("string_value"):
            return val.string_value
    return None


def get_eval_error_message(test: simple_pb2.SimpleTest) -> Optional[str]:
    if test.HasField("eval_error"):
        err_set = test.eval_error
        if len(err_set.errors) == 1:
            return celtypes.StringType(err_set.errors[0].message)
    return None


# The test data from the cel-spec conformance tests
cel_test_data = load_test_data(f"test/testdata/string_ext_{CEL_SPEC_VERSION}.textproto")
# Our supplemental tests of functionality not in the cel conformance file, but defined in the spec.
supplemental_test_data = load_test_data("test/testdata/string_ext_supplemental.textproto")

# Combine the test data from both files into one
sections = cel_test_data.section
sections.extend(supplemental_test_data.section)

# Find the format tests which test successful formatting
_format_tests: Iterable[simple_pb2.SimpleTest] = chain.from_iterable(x.test for x in sections if x.name == "format")
# Find the format error tests which test errors during formatting
_format_error_tests: Iterable[simple_pb2.SimpleTest] = chain.from_iterable(
    x.test for x in sections if x.name == "format_errors"
)

env = celpy.Environment(runner_class=InterpretedRunner)


@pytest.mark.parametrize("format_test", _format_tests)
def test_format_successes(format_test):
    """Tests success scenarios for string.format"""
    if format_test.name in skipped_tests:
        pytest.skip(f"skipped test: {format_test.name}")
    ast = env.compile(format_test.expr)
    prog = env.program(ast, functions=extra_func.make_extra_funcs())

    bindings = build_variables(format_test.bindings)
    result = prog.evaluate(bindings)
    expected = get_expected_result(format_test)
    assert expected is not None, f"[{format_test.name}]: expected a success result to be defined"
    assert result == expected


@pytest.mark.parametrize("format_error_test", _format_error_tests)
def test_format_errors(format_error_test):
    """Tests error scenarios for string.format"""
    if format_error_test.name in skipped_error_tests:
        pytest.skip(f"skipped test: {format_error_test.name}")
    ast = env.compile(format_error_test.expr)
    prog = env.program(ast, functions=extra_func.make_extra_funcs())

    bindings = build_variables(format_error_test.bindings)
    try:
        prog.evaluate(bindings)
        pytest.fail(f"[{format_error_test.name}]: expected an error to be raised during evaluation")
    except celpy.CELEvalError as e:
        msg = get_eval_error_message(format_error_test)
        assert msg is not None, f"[{format_error_test.name}]: expected an eval error to be defined"
        assert str(e) == msg
