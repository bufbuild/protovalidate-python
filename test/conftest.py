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

import protovalidate
from protovalidate.internal import backend

BACKENDS: list[str] = ["celpy", *(["cel-expr"] if backend.CEL_EXPR_AVAILABLE else [])]


def make_validator(cel_backend: str, **kwargs) -> protovalidate.Validator:
    original = backend.CEL_EXPR_AVAILABLE
    backend.CEL_EXPR_AVAILABLE = cel_backend == "cel-expr"
    try:
        return protovalidate.Validator(**kwargs)
    finally:
        backend.CEL_EXPR_AVAILABLE = original


def backend_validators(**kwargs) -> list[protovalidate.Validator]:
    return [make_validator(name, **kwargs) for name in BACKENDS]
