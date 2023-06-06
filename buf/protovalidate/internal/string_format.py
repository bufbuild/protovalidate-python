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

from celpy import celtypes
import celpy


class StringFormat:
    """An implementation of string.format() in CEL."""

    def __init__(self, locale: str):
        self.locale = locale

    def format(self, fmt: celtypes.Value, args: celtypes.Value) -> celpy.Result:
        if not isinstance(fmt, celtypes.StringType):
            return celpy.native_to_cel(
                celpy.new_error("format() requires a string as the first argument")
            )
        if not isinstance(args, celtypes.ListType):
            return celpy.native_to_cel(
                celpy.new_error("format() requires a list as the second argument")
            )
        return celtypes.StringType(fmt)
