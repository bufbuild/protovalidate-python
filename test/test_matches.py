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

import celpy
from celpy import celtypes

from protovalidate.internal.extra_func import cel_matches


def test_function_matches_re2():
    empty_string = celtypes.StringType("")
    # \z is valid re2 syntax for end of text
    assert cel_matches(empty_string, "^\\z")
    # \Z is invalid re2 syntax
    assert isinstance(cel_matches(empty_string, "^\\Z"), celpy.CELEvalError)
