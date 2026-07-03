# Copyright 2023-2026 Buf Technologies, Inc.
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

"""Which CEL backend is available.

The cel-expr-python engine needs both ``cel_expr_python`` (the cel-cpp binding)
and ``google.protobuf`` (the pool/message model it evaluates against). When both
import, ``Validator`` selects it automatically; otherwise it falls back to the
pure-Python celpy engine, which is always present. There is no public switch —
this is pure auto-detect. Tests force the fallback by monkeypatching
``CEL_EXPR_AVAILABLE`` to ``False`` before constructing a ``Validator``.
"""

import importlib.util


def _detect() -> bool:
    return all(importlib.util.find_spec(name) is not None for name in ("cel_expr_python", "google.protobuf"))


CEL_EXPR_AVAILABLE: bool = _detect()
