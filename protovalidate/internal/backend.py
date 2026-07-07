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

"""Which CEL backend is available."""


def _detect() -> bool:
    try:
        import cel_expr_python  # noqa: F401, PLC0415
        import google.protobuf.message  # noqa: F401, PLC0415
    except ImportError:
        return False
    return True


CEL_EXPR_AVAILABLE = _detect()
