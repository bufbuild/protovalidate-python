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

import unittest
from typing import Any

import celpy
from celpy import celtypes
from google.protobuf import text_format

from gen.cel.expr import eval_pb2
from gen.cel.expr.conformance.test import simple_pb2
from protovalidate.internal import extra_func
from protovalidate.internal.cel_field_presence import InterpretedRunner

# Version of the cel-spec that this implementation is conformant with
# This should be kept in sync with the version in the Makefile
CEL_SPEC_VERSION = "v0.24.0"

skipped_tests = [
    # cel-python seems to have a bug with ints and booleans in the same map which evaluate to the same value
    # which the test data for this test has. For example: {1: 'value1', true: 'value2'}]).
    # This throws an error like:
    # "no such overload: IntType(0) <class 'celpy.celtypes.IntType'> !=
    #    BoolType(False) <class 'celpy.celtypes.BoolType'>",))
    "map support (all key types)",
]
skipped_error_tests = [
    # cel-python does not support Protobuf messages at the moment and these tests use a MessageType
    # See https://github.com/cloud-custodian/cel-python/issues/43
    "object not allowed",
    "object inside list",
    "object inside map",
]


def read_textproto() -> simple_pb2.SimpleTestFile:
    msg = simple_pb2.SimpleTestFile()
    with open(f"tests/testdata/string_ext_{CEL_SPEC_VERSION}.textproto") as file:
        text_data = file.read()
        text_format.Parse(text_data, msg)
    return msg


class TestFormat(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        test_data = read_textproto()
        cls._format_test_section = next((x for x in test_data.section if x.name == "format"), None)
        cls._format_error_test_section = next((x for x in test_data.section if x.name == "format_errors"), None)
        cls._env = celpy.Environment(runner_class=InterpretedRunner)

    def _binding(self, bindings: dict[str, eval_pb2.ExprValue]) -> dict[Any, Any]:
        binder = {}
        for key, value in bindings.items():
            if value.HasField("value"):
                val = value.value
                if val.HasField("string_value"):
                    binder[key] = celtypes.StringType(val.string_value)
        return binder

    def get_eval_error_message(self, test) -> celtypes.Value:
        if test.HasField("eval_error"):
            err_set = test.eval_error
            if len(err_set.errors) == 1:
                return celtypes.StringType(err_set.errors[0].message)

        # for type_env in test.type_env:
        #     print(type_env)
        #     if type_env.HasField("ident"):
        #         ident = type_env.ident
        #         if ident.type.HasField("primitive"):
        #             prim = ident.type.primitive
        #             if prim == checked_pb2.Type.PrimitiveType.STRING:
        #                 print("das string")
        #     elif type_env.HasField("function"):
        #         print('funker')
        #         print(type_env.function)

    def test_format_successes(self):
        section = self._format_test_section
        if section is None:
            return
        print(f"Running {len(section.test)} subtests for formatting")
        for test in section.test:
            if test.name in skipped_tests:
                continue
            ast = self._env.compile(test.expr)
            prog = self._env.program(ast, functions=extra_func.EXTRA_FUNCS)

            bindings = self._binding(test.bindings)
            with self.subTest(test.name):
                try:
                    result = prog.evaluate(bindings)
                    if test.value.HasField("string_value"):
                        self.assertEqual(result, test.value.string_value)
                except celpy.CELEvalError as e:
                    self.fail(e)

    def test_format_errors(self):
        section = self._format_error_test_section
        if section is None:
            return
        print(f"Running {len(section.test)} subtests for formatting errors")
        for test in section.test:
            if test.name in skipped_error_tests:
                continue
            ast = self._env.compile(test.expr)
            prog = self._env.program(ast, functions=extra_func.EXTRA_FUNCS)

            bindings = self._binding(test.bindings)
            with self.subTest(test.name):
                try:
                    prog.evaluate(bindings)
                    self.fail("expected error")
                except celpy.CELEvalError as e:
                    msg = self.convert_result_matcher(test)
                    self.assertEqual(str(e), msg)
