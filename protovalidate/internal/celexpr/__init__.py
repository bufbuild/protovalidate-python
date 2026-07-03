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

"""The optional cel-expr-python (cel-cpp) validation engine.

Importing this package requires ``cel_expr_python`` and ``google.protobuf`` to be
installed; the validator only reaches for it when it imports successfully (see
``protovalidate.internal.backend``). Everything below the engine boundary speaks
google.protobuf descriptors and messages — protobuf-py values cross in through
``GoogleBridge``.
"""

from protovalidate.internal.celexpr.bridge import GoogleBridge
from protovalidate.internal.celexpr.extra_func import make_extension
from protovalidate.internal.celexpr.rules import RuleFactory

__all__ = ["GoogleBridge", "RuleFactory", "make_extension"]
