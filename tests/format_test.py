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

# from gen.cel.expr import checked_pb2
from gen.cel.expr.conformance.test import simple_pb2
from protovalidate.internal import extra_func
from protovalidate.internal.cel_field_presence import InterpretedRunner

CEL_SPEC_VERSION = "v0.24.0"

def read_textproto():
    msg = simple_pb2.SimpleTestFile()
    with open(f"tests/testdata/string_ext_{CEL_SPEC_VERSION}.textproto") as f:
        text_data = f.read()
        text_format.Parse(text_data, msg)
    return msg


class TestFormat(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        test_data = read_textproto()
        cls._format_tests = [x for x in test_data.section if x.name == "format"]
        cls._format_error_tests = [x for x in test_data.section if x.name == "format_errors"]
        cls._env = celpy.Environment(runner_class=InterpretedRunner)

    def _binding(self, bindings) -> dict[Any, Any]:
        binder = {}
        for key, value in bindings.items():
            if value.HasField("value"):
                val = value.value
                if val.HasField("string_value"):
                    binder[key] = celtypes.StringType(val.string_value)

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
        return binder

    def test_format_success(self):
        format_tests = self._format_tests[0]
        for test in format_tests.test:
            ast = self._env.compile(test.expr)
            prog = self._env.program(ast, functions=extra_func.EXTRA_FUNCS)

            binders = self._binding(test.bindings)
            with self.subTest(test.name):
                try:
                    result = prog.evaluate(binders)
                    if test.value.HasField("string_value"):
                        self.assertEqual(result, test.value.string_value)
                except celpy.CELEvalError as e:
                    self.fail(e)
