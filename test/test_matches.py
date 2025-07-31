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

import importlib.util
import unittest

import celpy
from celpy import celtypes

from protovalidate.internal.extra_func import cel_matches_re, cel_matches_re2

_USE_RE2 = True
spec = importlib.util.find_spec("re2")
if spec is None:
    _USE_RE2 = False


class TestCollectViolations(unittest.TestCase):
    @unittest.skipUnless(_USE_RE2, "Requires 're2'")
    def test_function_matches_re2(self):
        empty_string = celtypes.StringType("")
        # \z is valid re2 syntax for end of text
        self.assertTrue(cel_matches_re2(empty_string, "^\\z"))
        # \Z is invalid re2 syntax
        self.assertIsInstance(cel_matches_re2(empty_string, "^\\Z"), celpy.CELEvalError)

    @unittest.skipUnless(_USE_RE2 is False, "Requires 're'")
    def test_function_matches_re(self):
        empty_string = celtypes.StringType("")
        # \z is invalid re syntax
        self.assertIsInstance(cel_matches_re(empty_string, "^\\z"), celpy.CELEvalError)
        # \Z is valid re syntax for end of text
        self.assertTrue(cel_matches_re(empty_string, "^\\Z"))
