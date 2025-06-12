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

import operator
import re
from functools import reduce

import celpy
from celpy import celtypes

# Patterns that are supported in Python's re package and not in re2.
# RE2: https://github.com/google/re2/wiki/syntax
invalid_patterns = [
    r"\\[1-9]",  # backreference
    r"\\k<\w+>",  # backreference
    r"\(\?\=",  # lookahead
    r"\(\?\!",  # negative lookahead
    r"\(\?\<\=",  # lookbehind
    r"\(\?\<\!",  # negative lookbehind
    r"\\c[A-Z]",  # control character
    r"\\u[0-9a-fA-F]{4}",  # UTF-16 code-unit
    r"\\0(?!\d)",  # NUL
    r"\[\\b.*\]",  # Backspace eg: [\b]
]

# Regex for searching a regex pattern for flags.
flag_pattern = re.compile(r"^\(\?(?P<flags>[ims\-]+)\)")

# See https://docs.python.org/3/library/re.html#flags
flag_mapping = {
    "a": re.A,
    "i": re.I,
    "L": re.L,
    "m": re.M,
    "s": re.S,
    "u": re.U,
    "x": re.X,
}


def cel_matches(text: celtypes.Value, pattern: celtypes.Value) -> celpy.Result:
    """Return True if the given pattern matches text. False otherwise.

    CEL uses RE2 syntax which diverges from Python re in various ways. Ideally, we
    would use the google-re2 package, which is an extra dep in celpy, but at press
    time it does not provide a pre-built binary for the latest version of Python (3.13)
    which means those using this version will run into many issues.

    Instead of foisting this issue on users, we instead mimic re2 syntax by failing
    to compile the regex for patterns not compatible with re2.

    If users really want a pure re2 engine, they can provide their own via a config
    parameter when creating a validator.
    """
    if not isinstance(text, celtypes.StringType):
        msg = "invalid argument for text, expected string"
        raise celpy.CELEvalError(msg)
    if not isinstance(pattern, celtypes.StringType):
        msg = "invalid argument for pattern, expected string"
        raise celpy.CELEvalError(msg)

    # Simulate re2 by failing on any patterns not compatible with re2 syntax
    for invalid_pattern in invalid_patterns:
        r = re.search(invalid_pattern, pattern)
        if r is not None:
            msg = f"error evaluating pattern {pattern}, invalid RE2 syntax"
            raise celpy.CELEvalError(msg)
    # The conformance tests use flags at the very beginning of the sequence, which
    # is likely the most common place where this rare feature will be used.
    #
    # So we check for the flags at the very beginning and if present, apply them
    # using Python re enums.
    flags = ""
    flag_matches = re.match(flag_pattern, pattern)
    if flag_matches is not None:
        flag_group = flag_matches.groupdict()["flags"]
        for fl in flag_group:
            # Flag removal, don't include it in the output
            if fl == "-":
                continue
            flags += fl
        # Grab the rest of the expression minus the flags
        pattern_str = pattern[len(flag_matches[0]) :]
        # Convert a string of flags (i.e. aiLm) into the actual re.A, re.I enums
        flags_enums = reduce(operator.or_, (flag_mapping[c] for c in flags if c in flag_mapping), 0)
        exp = re.compile(pattern_str, flags=flags_enums)
    else:
        exp = re.compile(pattern)

    try:
        m = re.search(exp, text)
    except re.error as ex:
        return celpy.CELEvalError("match error", ex.__class__, ex.args)

    return celtypes.BoolType(m is not None)
