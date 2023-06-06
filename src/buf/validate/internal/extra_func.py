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

import celpy

from src.buf.validate.internal import string_format


def make_extra_funcs(locale: str) -> dict[str, celpy.CELFunction]:
    string_fmt = string_format.StringFormat(locale)
    return {
        "format": string_fmt.format,
    }


EXTRA_FUNCS = make_extra_funcs("en_US")
