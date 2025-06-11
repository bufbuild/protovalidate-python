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

import celpy
from celpy import celtypes

from protovalidate.internal import extra_func

invalid_patterns = [
    r"\1",
    r"\k<name>",
    r"Jack(?=Sprat)",
    "Jack(?!Sprat)",
    "(?<=Sprat)Jack",
    "(?<!Sprat)Jack",
    r"\cM\cJ",
    r"\u0041",
    r"\0 \01 \0a \012",
    r"[\b]",
]


class TestMatches(unittest.TestCase):
    def test_invalid_re2_syntax(self):
        for pattern in invalid_patterns:
            cel_pattern = celtypes.StringType(pattern)
            try:
                extra_func.cel_matches(celtypes.StringType("test"), cel_pattern)
                self.fail(f"expected an error on pattern {cel_pattern}")
            except celpy.CELEvalError as e:
                self.assertEqual(str(e), f"error evaluating pattern {cel_pattern}, invalid RE2 syntax")

    def test_flags(self) -> None:
        result = extra_func.cel_matches(celtypes.StringType("!@#$%^&*()"), celtypes.StringType("(?i)^[a-z0-9]+$"))
        self.assertFalse(result)
