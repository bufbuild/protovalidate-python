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

from buf.validate import validate_pb2  # type: ignore
from protovalidate.internal import string_format


def string(path: validate_pb2.FieldPath) -> str:
    result: list[str] = []
    for element in path.elements:
        if len(result) > 0:
            result.append(".")
        subscript_case = element.WhichOneof("subscript")
        if subscript_case is not None:
            result.extend(
                (
                    element.field_name,
                    "[",
                    string_format.format_value(getattr(element, subscript_case)),
                    "]",
                )
            )
        else:
            result.append(element.field_name)
    return "".join(result)
