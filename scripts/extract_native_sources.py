#!/usr/bin/env python3
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

"""Regenerate the vendored C++ sources for the native extension.

To bump the targeted protovalidate-cc version, edit scripts/extract/versions.json
and run this script. This script requires Bazel - it is only used during the bump
and not during normal builds.

What it does:

1. Fetches protovalidate-cc at the pinned ref and overrides transitive dependency
   versions as needed.
2. Builds a probe binary from the extension's real shim
   (crates/protovalidate-sys/shim) plus a trivial main. Compiling the shim
   validates it against the pinned versions; the binary's link anchors the
   closure below.
3. Reads the probe's *link* closure to decide which translation units the
   extension needs. We need to actually build a binary instead of using
   a deps() query since that includes tooling/test dependencies and doesn't
   reflect the actual source we use / need to vendor, only the dependency graph.
4. Vendors the needed sources plus all headers into each crate's vendor/
   directory. Bazel-generated files (ANTLR parser, .pb.cc/.pb.h, cel-cpp's
   descriptor-set embed) are vendored like everything else: for this project
   they are just more files that get deleted and regenerated together.

The action graph also contains actions that are not translation units of the
extension -- exec-configuration tooling like protoc, and `parse_headers`
header-validation compiles. Nothing filters them explicitly: selection is
driven by what the probe's link actually consumed, so they fall out.
"""

from __future__ import annotations

import collections
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tarfile
import urllib.request
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
CONFIG_PATH = REPO_ROOT / "scripts" / "extract" / "versions.json"
WORK_DIR = REPO_ROOT / ".tmp" / "native-extract"
CRATES = REPO_ROOT / "crates"

# Canonical bazel repo name -> crate that vendors it.
REPO_TO_CRATE = {
    "abseil-cpp+": "absl-sys",
    "protobuf+": "protobuf-sys",
    "re2+": "re2-sys",
    "antlr4-cpp-runtime+": "antlr4rt-sys",
    "cel-cpp+": "celcpp-sys",
    "cel-spec+": "celcpp-sys",
    "protovalidate+": "protovalidate-sys",
    "_main": "protovalidate-sys",
}
# protovalidate doesn't use protobuf input/output streams (only bytes) so we
# skip vendoring zlib. If we didn't do this, zlib would still be stripped from
# the final binary since it's unused so this saves us some vendoring for free.
SKIP_REPOS = {"zlib+"}

VENDOR_HEADER_SUFFIXES = (".h", ".hpp", ".inc", ".def")

# The probe package this script injects into the extraction workspace.
PROBE_PACKAGE = "pv_extract"


def copy_file(src: Path, dst: Path) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)
    # bazel-out files are read-only and sometimes executable, and copy2
    # preserves modes: normalize so a second copy to the same destination
    # (the same generated header reached via two staging trees) can write,
    # and so git does not record stray executable bits. chmod does not
    # touch mtime, so the commit-stamp story is unaffected.
    dst.chmod(0o644)


def run(cmd: list[str], cwd: Path, *, capture: bool = False) -> str:
    print(f"  $ {' '.join(cmd[:6])}{' ...' if len(cmd) > 6 else ''}", flush=True)
    if capture:
        result = subprocess.run(
            cmd, cwd=cwd, check=True, text=True, stdout=subprocess.PIPE
        )
        return result.stdout
    subprocess.run(cmd, cwd=cwd, check=True)
    return ""


class Aquery:
    """Indexed view over one `bazel aquery --output=jsonproto` result."""

    def __init__(self, text: str) -> None:
        data = json.loads(text)
        self.data = data
        self._artifacts = {a["id"]: a for a in data.get("artifacts", [])}
        self._fragments = {f["id"]: f for f in data.get("pathFragments", [])}
        self._depsets = {s["id"]: s for s in data.get("depSetOfFiles", [])}

    def path(self, artifact_id: int) -> str:
        parts: list[str] = []
        fragment_id = self._artifacts[artifact_id]["pathFragmentId"]
        while True:
            fragment = self._fragments[fragment_id]
            parts.append(fragment["label"])
            if "parentId" not in fragment:
                break
            fragment_id = fragment["parentId"]
        return "/".join(reversed(parts))

    def expand(self, depset_ids: list[int]) -> set[int]:
        found: set[int] = set()
        seen: set[int] = set()
        stack = list(depset_ids)
        while stack:
            current = stack.pop()
            if current in seen:
                continue
            seen.add(current)
            depset = self._depsets.get(current)
            if depset is None:
                continue
            found.update(depset.get("directArtifactIds", []))
            stack.extend(depset.get("transitiveDepSetIds", []))
        return found

    def actions(self, mnemonic: str) -> list[dict]:
        return [a for a in self.data.get("actions", []) if a["mnemonic"] == mnemonic]


def fetch_source_archive(spec: dict, destination: Path) -> None:
    """Downloads and unpacks a GitHub source archive at a pinned ref."""
    url = spec["archive"].format(ref=spec["ref"])
    cache = WORK_DIR / "cache"
    cache.mkdir(parents=True, exist_ok=True)
    archive = cache / f"{spec['ref']}.tar.gz"

    if not archive.exists():
        print(f"downloading {url}")
        with urllib.request.urlopen(url) as response:  # noqa: S310 - pinned https URL
            archive.write_bytes(response.read())

    digest = hashlib.sha256(archive.read_bytes()).hexdigest()
    expected = spec.get("sha256")
    if expected and digest != expected:
        archive.unlink()
        message = (
            f"checksum mismatch for {url}\n  expected {expected}\n  got      {digest}"
        )
        raise SystemExit(message)
    if not expected:
        print(f"  note: no sha256 pinned; archive digest is {digest}")

    print(f"unpacking protovalidate-cc {spec['ref']}")
    destination.mkdir(parents=True, exist_ok=True)
    with tarfile.open(archive) as tar:
        members = tar.getmembers()
        # GitHub archives nest everything under a single `<repo>-<ref>/`
        # directory.
        root = members[0].name.split("/")[0]
        for member in members:
            parts = member.name.split("/")
            if parts[0] != root:
                message = f"unexpected archive layout: {member.name}"
                raise SystemExit(message)
            relative = "/".join(parts[1:])
            if not relative:
                continue  # the top-level directory entry itself
            if relative.startswith("/") or ".." in parts:
                message = f"refusing unsafe archive path: {member.name}"
                raise SystemExit(message)
            member.name = relative
            tar.extract(member, destination, filter="data")


def prepare_workspace(config: dict) -> Path:
    """Fetch protovalidate-cc at the pinned ref and apply our overrides."""
    pvcc = config["protovalidate_cc"]
    work = WORK_DIR / "protovalidate-cc"
    stamp = work / ".extract-ref"
    if work.exists() and stamp.exists() and stamp.read_text().strip() == pvcc["ref"]:
        print(f"reusing existing source tree at {work} ({pvcc['ref']})")
    else:
        if work.exists():
            shutil.rmtree(work)
        fetch_source_archive(pvcc, work)
        stamp.write_text(pvcc["ref"] + "\n")

    module = work / "MODULE.bazel"
    text = module.read_text()
    marker = "# --- protovalidate-python extraction overrides ---"
    overrides = [
        f'single_version_override(\n    module_name = "{name}",\n    version = "{version}",\n)'
        for name, version in config["module_overrides"].items()
        if not name.startswith("_")
    ]
    updated = (
        text.partition(marker)[0].rstrip("\n")
        + "\n\n"
        + marker
        + "\n"
        + "\n".join(overrides)
        + "\n"
    )
    if updated != text:
        module.write_text(updated)
        # The lock pins the old resolution; drop it so bazel re-resolves with our overrides.
        (work / "MODULE.bazel.lock").unlink(missing_ok=True)

    write_probe_package(work)
    return work


def bazel_flags(config: dict) -> list[str]:
    """Configuration flags for every bazel build/aquery the extraction runs."""
    flags = [
        # Ensure reproducibility across envs (default from Bazel 9).
        "--incompatible_strict_action_env",
        # Java needed to generate cel parser with ANTLR
        f"--java_runtime_version={config['bazel']['java_runtime_version']}",
        # protovalidate-cc and cel-cpp, etc can have different versions, and
        # Bazel warns for this but it's fine to take the highest and not warn.
        "--check_direct_dependencies=off",
    ]
    if sys.platform == "darwin":
        # Flags needed for macOS builds of protovalidate-cc, which should be
        # upstreamed there eventually.
        flags += [
            "--repo_env=BAZEL_NO_APPLE_CPP_TOOLCHAIN=1",
            "--macos_minimum_os=10.15",
            "--cxxopt=-faligned-allocation",
        ]
    return flags


def write_probe_package(work: Path) -> None:
    probe = work / PROBE_PACKAGE
    if probe.exists():
        shutil.rmtree(probe)
    probe.mkdir()
    shim_dir = CRATES / "protovalidate-sys" / "shim"
    for name in ("pv_shim.h", "pv_shim.cc"):
        shutil.copy(shim_dir / name, probe / name)
    # The main only has to make the binary linkable. The vendored set comes
    # from the link action's inputs -- every dep archive, target-level -- so
    # nothing needs to reference the shim's symbols; pv_shim.cc being a src
    # is what compile-checks the shim against the pins.
    (probe / "probe_main.cc").write_text("int main() { return 0; }\n")
    (probe / "BUILD").write_text(
        "cc_binary(\n"
        '    name = "probe",\n'
        '    srcs = ["pv_shim.cc", "pv_shim.h", "probe_main.cc"],\n'
        '    deps = ["//buf/validate:validator"],\n'
        ")\n"
    )


def build_probe(work: Path, flags: list[str]) -> None:
    """Builds the probe."""
    print("building probe")
    run(["bazel", "build", *flags, f"//{PROBE_PACKAGE}:probe"], cwd=work)


def collect_link_closure(
    work: Path, flags: list[str]
) -> tuple[dict[str, set[str]], dict[str, set[str]]]:
    """Maps the probe's link inputs back to the source files that fed them.

    This is 3 steps:

    - Find all the .o and .a files used in the final link
    - Find all the .o files in the used .a files
    - Find the source file that produced the .o file
    """
    probe = f"//{PROBE_PACKAGE}:probe"
    expr = f'mnemonic("CppLink|CppArchive|CppCompile", deps({probe}))'
    graph = Aquery(
        run(
            ["bazel", "aquery", *flags, "--output=jsonproto", expr],
            cwd=work,
            capture=True,
        )
    )

    # deps() reaches exec-configuration tooling like protoc, so the
    # probe's own link action is picked out by its output path to get the
    # real closure.
    link_actions = [
        action
        for action in graph.actions("CppLink")
        if graph.path(action["outputIds"][0]).endswith(f"/{PROBE_PACKAGE}/probe")
    ]
    if len(link_actions) != 1:
        message = f"expected exactly one probe link action, got {len(link_actions)}"
        raise SystemExit(message)
    link_inputs = {
        graph.path(i) for i in graph.expand(link_actions[0]["inputDepSetIds"])
    }

    # Archives contributed by cc_library targets, expanded to their objects.
    archive_objects: dict[str, set[str]] = {}
    for action in graph.actions("CppArchive"):
        out = graph.path(action["outputIds"][0])
        objects = {graph.path(i) for i in graph.expand(action["inputDepSetIds"])}
        archive_objects[out] = {o for o in objects if o.endswith(".o")}

    needed = {p for p in link_inputs if p.endswith(".o")}
    # Retrieve object file paths from inside archives.
    for path in (p for p in link_inputs if p.endswith(".a")):
        needed |= archive_objects[path]

    # Reverse mapping from a compile action's output to the source it
    # compiles.
    object_to_source: dict[str, str] = {}
    for action in graph.actions("CppCompile"):
        args = action["arguments"]
        object_to_source[graph.path(action["outputIds"][0])] = args[
            args.index("-c") + 1
        ]

    sources: dict[str, set[str]] = collections.defaultdict(set)
    generated: dict[str, set[str]] = collections.defaultdict(set)
    for obj in needed:
        source = object_to_source[obj]
        repo = bazel_repo(source)
        if repo in SKIP_REPOS:
            continue
        if repo == "_main" and source.startswith(f"{PROBE_PACKAGE}/"):
            continue  # the shim and probe main are not vendored sources
        if source.startswith("bazel-out/"):
            generated[repo].add(source)
        else:
            sources[repo].add(source)

    return sources, generated


def bazel_repo(source: str) -> str:
    """The bazel repo a source path belongs to, generated outputs included."""
    if source.startswith("bazel-out/"):
        if "/bin/external/" in source:
            return source.split("/bin/external/", 1)[1].partition("/")[0]
        return "_main"
    if source.startswith("external/"):
        return source.split("/")[1]
    return "_main"


def generated_destination(source: str) -> str:
    """Where a generated source belongs inside a crate's vendor/ directory.

    We strip prefixes Bazel adds depending on the type of file.
    """
    for marker in ("_virtual_imports/", "_virtual_includes/"):
        if marker in source:
            tail = source.split(marker, 1)[1]
            return tail.split("/", 1)[1]
    if "/bin/external/" in source:
        after = source.split("/bin/external/", 1)[1]
        return after.split("/", 1)[1]
    return source.split("/bin/", 1)[1]


# Maps bazel platform-select condition labels (canonical form, leading @s
# stripped) to cargo's CARGO_CFG_TARGET_OS values, which is how build.rs
# decides whether to compile a tagged file.
SELECT_KEY_TO_TARGET_OS = {
    "platforms//os:windows": "windows",
    "platforms//os:linux": "linux",
    "platforms//os:osx": "macos",
    "platforms//os:macos": "macos",
}


def parse_label(label: str) -> tuple[str, str]:
    """Splits a canonical label into (repo, repo-relative path)."""
    repo, _, rest = label.lstrip("@").partition("//")
    package, _, name = rest.partition(":")
    return repo or "_main", f"{package}/{name}" if package else name


def collect_platform_sources(
    work: Path, sources: dict[str, set[str]]
) -> dict[str, set[tuple[str, str]]]:
    """Finds sources that bazel adds via platform select(), per repo.

    The extraction host's link closure only contains that host's selection
    (absl's time_zone_name_win.cc is in srcs only on windows), so the other
    platforms' branches are read from the target graph: unconfigured `bazel
    query` preserves select() structure when asked not to flatten it. Only
    packages that already contribute a file to the closure are considered,
    which keeps tooling-only packages out without a hand-maintained list.
    """
    packages: dict[str, set[str]] = collections.defaultdict(set)
    for repo, files in sources.items():
        for file in files:
            rel = file if repo == "_main" else file.split(f"external/{repo}/", 1)[1]
            packages[repo].add(str(Path(rel).parent))

    text = run(
        [
            "bazel",
            "query",
            "--output=streamed_jsonproto",
            "--proto:flatten_selects=false",
            "--consistent_labels",
            f'kind("cc_.*", deps(//{PROBE_PACKAGE}:probe))',
        ],
        cwd=work,
        capture=True,
    )

    found: dict[str, set[tuple[str, str]]] = collections.defaultdict(set)
    for line in text.splitlines():
        if not line.strip():
            continue
        target = json.loads(line)
        rule = target.get("rule")
        if rule is None:
            continue
        rule_repo, rule_path = parse_label(rule["name"])
        rule_package = str(Path(rule_path).parent)
        if not any(
            p == rule_package or p.startswith(f"{rule_package}/")
            for p in packages.get(rule_repo, ())
        ):
            continue
        for attribute in rule.get("attribute", []):
            if attribute["name"] != "srcs" or "selectorList" not in attribute:
                continue
            for element in attribute["selectorList"].get("elements", []):
                for entry in element.get("entries", []):
                    target_os = SELECT_KEY_TO_TARGET_OS.get(entry["label"].lstrip("@"))
                    files = [
                        parse_label(label)[1]
                        for label in entry.get("stringListValue", [])
                        if label.endswith((".cc", ".cpp"))
                    ]
                    if not files:
                        continue
                    if target_os is None:
                        if not entry["label"].endswith("//conditions:default"):
                            print(
                                f"  warning: unmapped select key {entry['label']} "
                                f"with sources in {rule['name']}",
                                file=sys.stderr,
                            )
                        continue
                    for file in files:
                        found[rule_repo].add((target_os, file))
    return found


def vendor(
    work: Path, sources: dict[str, set[str]], generated: dict[str, set[str]]
) -> None:
    """Regenerates crate vendored trees."""
    for crate in sorted(set(REPO_TO_CRATE.values())):
        for subdirectory in ("vendor", "gen"):
            tree = CRATES / crate / subdirectory
            if tree.exists():
                shutil.rmtree(tree)

    output_base = Path(
        run(["bazel", "info", "output_base"], cwd=work, capture=True).strip()
    )
    execroot = Path(
        run(["bazel", "info", "execution_root"], cwd=work, capture=True).strip()
    )

    filelists: dict[str, list[str]] = collections.defaultdict(list)
    platform_sources = collect_platform_sources(work, sources)
    vendor_sources(work, output_base / "external", sources, platform_sources, filelists)
    vendor_generated(execroot, generated, filelists)

    for crate, files in filelists.items():
        path = CRATES / crate / "filelist.txt"
        content = (
            "# Generated by scripts/extract_native_sources.py -- do not edit.\n"
            "# Files the extension links. Paths are relative to this crate's vendor/ dir.\n"
            "# A `windows:`/`linux:`/`macos:` prefix compiles a file on that OS only.\n"
            + "\n".join(sorted(files))
            + "\n"
        )
        if not path.exists() or path.read_text() != content:
            path.write_text(content)

        vendor_dir = CRATES / crate / "vendor"
        # Files all have mtime set to the time of the git commit for a source archive.
        # To keep build cache keys stable, we set the mtime of directories we create
        # to the same time.
        stamp = min(
            (vendor_dir / file.split(":", 1)[-1]).stat().st_mtime for file in files
        )
        os.utime(vendor_dir, (stamp, stamp))
        for directory in vendor_dir.rglob("*"):
            if directory.is_dir():
                os.utime(directory, (stamp, stamp))


def vendor_sources(
    work: Path,
    external: Path,
    sources: dict[str, set[str]],
    platform_sources: dict[str, set[tuple[str, str]]],
    filelists: dict[str, list[str]],
) -> None:
    """Copies each repo's translation units, all its headers, and licenses.

    Headers are copied wholesale rather than from the compile closure: the
    closure only contains what this host's build read, and platform-specific
    headers (absl's spinlock_linux.inc, win32 .incs) must be vendored even
    though the extracting machine never touches them.
    """
    for repo, files in sorted(sources.items()):
        crate = REPO_TO_CRATE.get(repo)
        if crate is None:
            print(
                f"  warning: no crate mapping for repo {repo}, skipping",
                file=sys.stderr,
            )
            continue
        tree = work if repo == "_main" else external / repo
        vendor_dir = CRATES / crate / "vendor"
        # Sources are keyed relative to the tree root.
        rel_files = sorted(
            f if repo == "_main" else f.split(f"external/{repo}/", 1)[1] for f in files
        )
        for rel in rel_files:
            copy_file(tree / rel, vendor_dir / rel)
        for target_os, rel in sorted(platform_sources.get(repo, set())):
            copy_file(tree / rel, vendor_dir / rel)
            filelists[crate].append(f"{target_os}:{rel}")
        for header in tree.rglob("*"):
            if header.suffix in VENDOR_HEADER_SUFFIXES and header.is_file():
                copy_file(header, vendor_dir / header.relative_to(tree))
        copy_licenses(repo, tree, vendor_dir)
        filelists[crate].extend(rel_files)


def vendor_generated(
    execroot: Path, generated: dict[str, set[str]], filelists: dict[str, list[str]]
) -> None:
    """Copies every bazel-generated file the extension needs into vendor/.

    Translation units come from the link closure; headers are every generated
    header under bazel-out (`.pb.h`, the descriptor-set embed `.inc`) -- the
    build only generates what some consumer needed, and generated code is
    platform-independent, so the sweep is both complete and portable.
    """
    merged: dict[str, set[str]] = collections.defaultdict(set)
    for repo, files in generated.items():
        merged[repo] |= files
    for path in (execroot / "bazel-out").rglob("*"):
        if path.suffix not in VENDOR_HEADER_SUFFIXES or not path.is_file():
            continue
        source = str(path.relative_to(execroot))
        if "-exec" in source.split("/")[1]:
            continue
        merged[bazel_repo(source)].add(source)
    for repo, files in sorted(merged.items()):
        if repo in SKIP_REPOS:
            continue
        crate = REPO_TO_CRATE.get(repo)
        if crate is None:
            print(
                f"  warning: no crate mapping for generated repo {repo}",
                file=sys.stderr,
            )
            continue
        vendor_dir = CRATES / crate / "vendor"
        for source in sorted(files):
            dest = generated_destination(source)
            copy_file(execroot / source, vendor_dir / dest)
            if dest.endswith((".cc", ".cpp")):
                filelists[crate].append(dest)


def copy_licenses(repo: str, tree: Path, vendor_dir: Path) -> None:
    """Copies upstream license/notice files from the repo's module root.

    If a vendored dependency doesn't have a LICENSE file in the bazel package,
    for example antlr4rt-sys, there must be a hand-maintained LICENSE file in
    the crate's root or we raise an error here to know to copy one in.
    """
    copied: list[str] = []
    for path in sorted(tree.glob("*")):
        if not path.is_file():
            continue
        stem = path.name.upper()
        if stem.startswith(
            ("LICENSE", "LICENCE", "NOTICE", "COPYING", "AUTHORS", "PATENTS")
        ):
            copy_file(path, vendor_dir / path.name)
            copied.append(path.name)
    if not copied:
        crate_root = vendor_dir.parent
        carried = sorted(f.name for f in crate_root.glob("LICENSE*") if f.is_file())
        if carried:
            print(
                f"  note: {repo} ships no license file; carrying {', '.join(carried)}"
            )
        else:
            message = (
                f"{repo} has no license file at its module root and {crate_root} carries none.",
            )
            raise SystemExit(message)


def module_versions(work: Path) -> dict[str, dict[str, str]]:
    """Resolved module versions and the registry hashes that identify them."""
    lock = work / "MODULE.bazel.lock"
    data = json.loads(lock.read_text())
    versions: dict[str, dict[str, str]] = {}
    for url, digest in sorted(data.get("registryFileHashes", {}).items()):
        if not url.endswith("/source.json"):
            continue
        parts = url.rstrip("/").split("/")
        name, version = parts[-3], parts[-2]
        versions[name] = {"version": version, "source_json_sha256": digest, "url": url}
    return versions


def check_protovalidate_version(versions: dict) -> None:
    """Fails if the linked protovalidate differs from what we target."""
    resolved = versions.get("protovalidate", {}).get("version")
    targeted = None
    versions_py = REPO_ROOT / "test" / "versions.py"
    if versions_py.exists():
        for line in versions_py.read_text().splitlines():
            if line.startswith("PROTOVALIDATE_VERSION"):
                # The line reads `= os.getenv("PROTOVALIDATE_VERSION", "v1.2.0")`,
                # so pick out the version literal rather than a quoted position.
                found = re.search(r'"v?(\d+\.\d+\.\d+[^"]*)"', line)
                if found:
                    targeted = found.group(1)
                break
    if resolved and targeted and resolved != targeted:
        message = (
            f"linked protovalidate is {resolved} but this package targets "
            f"{targeted} (test/versions.py). Violation messages would differ "
            f"from what conformance tests. Pin a protovalidate-cc ref that "
            f"targets {targeted}, or move test/versions.py with it."
        )
        raise SystemExit(message)


def main() -> None:
    config = json.loads(CONFIG_PATH.read_text())
    if not shutil.which("bazel"):
        message = "bazel is required to run the extraction"
        raise SystemExit(message)

    work = prepare_workspace(config)
    build_flags = bazel_flags(config)
    build_probe(work, build_flags)
    sources, generated = collect_link_closure(work, build_flags)
    versions = module_versions(work)
    check_protovalidate_version(versions)

    print("\ntranslation units to vendor:")
    total = 0
    for repo, files in sorted(sources.items(), key=lambda kv: -len(kv[1])):
        print(f"  {repo:24s} {len(files):4d}  -> {REPO_TO_CRATE.get(repo, '??')}")
        total += len(files)
    for repo, files in sorted(generated.items()):
        print(
            f"  {repo + ' (generated)':24s} {len(files):4d}  -> {REPO_TO_CRATE.get(repo, '??')}"
        )
        total += len(files)
    print(f"  {'TOTAL':24s} {total:4d}")

    print("\nvendoring")
    vendor(work, sources, generated)

    print("\nresolved module versions:")
    for name, info in sorted(versions.items()):
        if name in (
            "abseil-cpp",
            "protobuf",
            "re2",
            "antlr4-cpp-runtime",
            "cel-cpp",
            "cel-spec",
            "protovalidate",
        ):
            print(f"  {name:22s} {info['version']}")

    print("\nnext: cargo test, then the conformance suite")


if __name__ == "__main__":
    main()
