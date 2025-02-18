# Copyright 2023 Buf Technologies, Inc.
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

import celpy  # type: ignore
from celpy import celtypes  # type: ignore


class StringFormat:
    """An implementation of string.format() in CEL."""

    def __init__(self, locale: str):
        self.locale = locale

    def format(self, fmt: celtypes.Value, _: celtypes.Value) -> celpy.Result:
        if not isinstance(fmt, celtypes.StringType):
            return celpy.CELEvalError("format() requires a string as the first argument")
        return celtypes.StringType(fmt)


_default_format = StringFormat("en_US")
format = _default_format.format  # noqa: A001
