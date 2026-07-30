# Copyright (c) 2023-2026 Buf Technologies, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import annotations

from protovalidate._funcs import _is_hostname


def test_hostname_trailing_dot_excluded_from_length() -> None:
    name253 = ("a" * 63 + ".") * 3 + "a" * 61
    name254 = ("a" * 63 + ".") * 3 + "a" * 62
    assert len(name253) == 253
    assert len(name254) == 254
    # The 253-character limit excludes the optional trailing dot (RFC 3339).
    assert _is_hostname(name253)
    assert _is_hostname(name253 + ".")
    assert not _is_hostname(name254)
    assert not _is_hostname(name254 + ".")
