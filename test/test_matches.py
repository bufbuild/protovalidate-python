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

from protovalidate.internal.matches import matches

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
    r"^\Z",
]


class TestMatches(unittest.TestCase):
    def test_invalid_re2_syntax(self):
        for pattern in invalid_patterns:
            try:
                matches("test", pattern)
                self.fail(f"expected an error on pattern {pattern}")
            except celpy.CELEvalError as e:
                self.assertEqual(str(e), f"error evaluating pattern {pattern}, invalid RE2 syntax")
