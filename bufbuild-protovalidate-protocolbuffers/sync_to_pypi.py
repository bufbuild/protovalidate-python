# Copyright 2023-2025 Buf Technologies, Inc.
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

# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "cyclopts",
#     "httpx",
#     "loguru",
# ]
# ///

"""
This script is used to sync the tagged versions of https://buf.build/bufbuild/protovalidate/ to the
pypi package bufbuild-protovalidate-protocolbuffers.

Intended to run on a cron schedule, the script will query the available versions of the protovalidate
module on buf.build and compare it to the versions available on pypi. If there are any versions on buf.build
that are not on pypi, it will generate a python package for that version and save the wheels and sdists to
the dist/ directory on the current path.

A follow-up publish step can then be configured to publish the packages in `dist/` to pypi.
"""

import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
from typing import Optional, Set, Tuple
from cyclopts import App
import httpx
from loguru import logger

app = App()


def query_pypi_versions(pypi_url: str) -> set[str]:
    """
    Query the PyPI JSON API for a list of published versions of the package.

    Args:
        pypi_url: The base URL of the PyPI instance to query. For example, https://pypi.org/ or https://test.pypi.org/.

    Returns:
        A set of version strings. For example, {"0.14.0", "0.14.1"}.
    """
    pypi_url = pypi_url.rstrip("/")
    response = httpx.get(f"{pypi_url}/pypi/bufbuild-protovalidate-protocolbuffers/json")
    response.raise_for_status()
    return set(response.json()["releases"].keys())


def query_buf_module_tags() -> Set[str]:
    """
    Query the buf registry for a list of tags for the bufbuild/protovalidate module

    Returns:
        A set of tag strings without the "v" prefix. For example, {"0.14.0", "0.14.1"}.
    """
    tags = set()
    page_token = None
    while True:  # paginate through the pages of results
        page_tags, page_token = _query_buf_module_labels(page_token)
        tags.update(page_tags)
        if page_token is None:
            break
    return tags


def _query_buf_module_labels(page_token: Optional[str] = None) -> Tuple[Set[str], Optional[str]]:
    """Fetch a single page of tags for the bufbuild/protovalidate module."""
    request_data = {
        "pageSize": 100,
        "resourceRef": {"name": {"owner": "bufbuild", "module": "protovalidate"}},
        "order": "ORDER_UPDATE_TIME_DESC",
        "archiveFilter": "ARCHIVE_FILTER_UNARCHIVED_ONLY",
    }
    if page_token:
        request_data["pageToken"] = page_token

    response = httpx.post(
        "https://buf.build/buf.registry.module.v1beta1.LabelService/ListLabels",
        headers={"Content-Type": "application/json"},
        content=json.dumps(request_data),
    )
    response.raise_for_status()
    response_data = response.json()
    tags = {label["name"][1:] for label in response_data["labels"] if label["name"].startswith("v")}
    next_page_token = response_data.get("nextPageToken")  # is not there on the last page
    return tags, next_page_token


def _generate_package_for_version(version: str):
    """
    Generate a python package for the given version of the bufbuild/protovalidate module.

    Args:
        version: The bufbuild/protovalidate version to generate a python package for. Expected without the "v" prefix,
            for example, "0.14.0".
    """
    logger.info(f"Generating package for version {version}")
    repo_path = Path(__file__).parent.parent.absolute()
    built_dist_path = repo_path / "bufbuild-protovalidate-protocolbuffers" / "dist"
    (repo_path / built_dist_path).mkdir(exist_ok=True)

    with tempfile.TemporaryDirectory() as tmpdir:
        # since buf generate overwrites files checked into git, we copy the whole repo to a temporary directory
        # (the whole repo since we also need the .git)
        package_path = Path(tmpdir) / "protovalidate-python" / "bufbuild-protovalidate-protocolbuffers"
        shutil.copytree(repo_path, package_path.parent)

        shutil.rmtree(package_path / "buf" / "validate" / "proto5")
        shutil.rmtree(package_path / "buf" / "validate" / "proto6")

        buf_binary = package_path / ".tmp" / "bin" / "buf"
        subprocess.run([buf_binary, "generate", f"buf.build/bufbuild/protovalidate:v{version}"], cwd=package_path)

        license_header_binary = package_path / ".tmp" / "bin" / "license-header"
        subprocess.run(
            [
                license_header_binary,
                "--license-type",
                "apache",
                "--copyright-holder",
                "Buf Technologies, Inc.",
                "--year-range",
                "2023-2025",
            ],
            cwd=package_path,
        )
        subprocess.run(["uv", "version", f"v{version}"], cwd=package_path)
        subprocess.run(["uv", "build"], cwd=package_path)

        build_output = package_path / "dist"
        if not build_output.exists():
            raise RuntimeError(
                f"Failed to build package for version {version}, no wheels or sdists found in {build_output}"
            )

        for package in (package_path / "dist").iterdir():
            shutil.copy(package, built_dist_path)


@app.default
def main(pypi_url: str = "https://pypi.org/"):
    logger.info(f"Querying pypi for existing versions of bufbuild-protovalidate-protocolbuffers (on pypi {pypi_url})")
    pypi_versions = query_pypi_versions(pypi_url)
    logger.info(f"Found {len(pypi_versions)} versions on pypi: {pypi_versions}")

    logger.info("Querying buf.build for existing tags of bufbuild/protovalidate")
    buf_tags = query_buf_module_tags()
    logger.info(f"Found {len(buf_tags)} tags on buf.build: {buf_tags}")

    existing_versions = pypi_versions & buf_tags
    logger.info(f"Found {len(existing_versions)} existing versions: {existing_versions}")
    versions_to_generate = buf_tags - pypi_versions
    logger.info(f"Found {len(versions_to_generate)} versions to generate: {versions_to_generate}")

    for i, version in enumerate(versions_to_generate):
        if i >= 2:
            logger.info("Generated 2 packages, stopping for now to test the sync script.")
            return
        _generate_package_for_version(version)


if __name__ == "__main__":
    # configure logging
    logger.remove()
    logger.add(sys.stdout, format="{time:%Y-%m-%d %H:%M:%S} | {level} | {message}", level="DEBUG")
    # invoke the CLI
    app()
