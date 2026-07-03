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

import re
import shutil
import subprocess
from pathlib import Path

from test.versions import PROTOVALIDATE_VERSION


def main() -> None:
    version = PROTOVALIDATE_VERSION
    if re.match(r"^v\d+\.\d+\.\d+(\-.+)?$", version):
        # Version tag, fetch from BSR
        protovalidate_path = f"buf.build/bufbuild/protovalidate:{version}"
        protovalidate_testing_path = f"buf.build/bufbuild/protovalidate-testing:{version}"
    else:
        # Not a tag, generally an unreleased commit, fetch directly from git
        protovalidate_path = f"https://github.com/bufbuild/protovalidate.git#subdir=proto/protovalidate,ref={version}"
        protovalidate_testing_path = (
            f"https://github.com/bufbuild/protovalidate.git#subdir=proto/protovalidate-testing,ref={version}"
        )

    repo = Path(__file__).parent.parent

    protos_dir = repo / "proto"
    shutil.rmtree(protos_dir, ignore_errors=True)
    protos_dir.mkdir(parents=True, exist_ok=True)
    subprocess.run(["buf", "export", protovalidate_path, "-o", protos_dir], check=True)  # noqa: S603, S607
    subprocess.run(["buf", "generate"], cwd=repo, check=True)  # noqa: S607

    subprocess.run(  # noqa: S603
        ["buf", "export", protovalidate_testing_path, "-o", repo / "test" / "proto"],  # noqa: S607
        check=True,
    )
