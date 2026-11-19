#!/usr/bin/env python3
"""Read-only, standard-library repository checks for the 48/24 studio.

Run from anywhere: python tools/validate_repo.py --root . [--base COMMIT]
This checks records, not a person's identity, consent or legal title.
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path, PurePosixPath
from urllib.parse import unquote, urlsplit

LIFECYCLE = {"drafts": {"draft", "review"}, "canon": {"canonical"},
             "archive": {"rejected", "superseded", "archived"}}
REQUIRED_META = {"id", "title", "status", "owner", "updated", "source", "ai_assistance"}
ASSET_EXTS = {".png", ".jpg", ".jpeg", ".webp", ".gif", ".svg", ".tif", ".tiff",
              ".psd", ".kra", ".xcf", ".blend", ".fbx", ".obj", ".gltf", ".glb",
              ".ttf", ".otf", ".woff", ".woff2", ".wav", ".mp3", ".flac", ".ogg",
              ".mp4", ".mov", ".webm", ".pdf", ".docx", ".pptx", ".xlsx", ".zip"}
EXCLUDED = {".git", ".venv", "venv", "node_modules", "__pycache__", ".pytest_cache"}
RESERVED = re.compile(r"^(CON|PRN|AUX|NUL|COM[1-9]|LPT[1-9])(?:\.|$)", re.I)
SECRET_TOKEN = re.compile(r"(?:gh[pousr]_[A-Za-z0-9]{36,255}|github_pat_[A-Za-z0-9_]{70,255}|-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----)")
LINK = re.compile(r"!?\[[^\]\n]*\]\((<[^>]+>|[^\s)]+)(?:\s+['\"][^\n]*?['\"])?\)")
REF_LINK = re.compile(r"^\s*\[[^\]]+\]:\s*(\S+)", re.M)
MAX_FILE = 20 * 1024 * 1024


class Invalid(ValueError):
    pass


def strict_json(text: str):
    def pairs(items):
        result = {}
        for key, value in items:
            if key in result:
                raise Invalid(f"duplicate JSON key {key}")
            result[key] = value
        return result
    return json.loads(text, object_pairs_hook=pairs)


def coauthors(team: dict) -> set[str]:
    return {p.get("id") for p in team.get("people", [])
            if isinstance(p, dict) and p.get("role") == "coauthor" and isinstance(p.get("id"), str)}


def git(root: Path, *args: str, check: bool = True) -> subprocess.CompletedProcess:
    return subprocess.run(["git", "-C", str(root), *args], capture_output=True,
                          text=True, encoding="utf-8", errors="replace", check=check)


def inventory(root: Path) -> list[str]:
    """Tracked and nonignored new files locally; tracked files in clean CI."""
    result = git(root, "rev-parse", "--show-toplevel", check=False)
    if result.returncode == 0 and Path(result.stdout.strip()).resolve() == root:
        result = git(root, "ls-files", "--cached", "--others", "--exclude-standard", "-z")
        return sorted(set(filter(None, result.stdout.split("\0"))))
    return sorted(p.relative_to(root).as_posix() for p in root.rglob("*")
                  if (p.is_file() or p.is_symlink())
                  and not any(part in EXCLUDED for part in p.relative_to(root).parts))


def safe_path(value: str) -> bool:
    if not isinstance(value, str) or not value or "\\" in value or value.startswith("/"):
        return False
    parts = value.split("/")
    return all(p not in {"", ".", ".."} and not re.search(r'[<>:"|?*\x00-\x1f]', p)
               and not p.endswith((" ", ".")) and not RESERVED.match(p) for p in parts)


def frontmatter(text: str) -> dict:
    lines = text.splitlines()
    if not lines or lines[0] != "---":
        raise Invalid("missing opening --- front matter")
    try:
        end = lines.index("---", 1)
    except ValueError:
        raise Invalid("missing closing --- front matter") from None
    values = {}
    for line in lines[1:end]:
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        match = re.fullmatch(r"([a-z][a-z0-9_]*):\s*(.*?)\s*", line)
        if not match:
            raise Invalid("front matter uses flat key: scalar or JSON-array values only")
        key, value = match.groups()
        if key in values:
            raise Invalid(f"duplicate metadata key {key}")
        if not value:
            raise Invalid(f"empty metadata value {key}; use 'unassigned' where appropriate")
        if value.startswith(('"', '[')):
            try:
                value = json.loads(value)
            except json.JSONDecodeError as exc:
                raise Invalid(f"invalid JSON value in {key}: {exc.msg}") from None
            if not isinstance(value, (str, list)):
                raise Invalid(f"{key} must be a string or JSON array")
        elif value.startswith("'"):
            if not value.endswith("'") or len(value) < 2:
                raise Invalid(f"unclosed single quote in {key}")
            value = value[1:-1].replace("''", "'")
        elif value.startswith(("{", "|", ">", "&", "*", "!")):
            raise Invalid(f"unsupported YAML syntax in {key}; use a quoted scalar")
        values[key] = value
    return values


def manifest_paths(manifest: dict) -> tuple[set[str], set[str]]:
    if manifest.get("schema_version") != 1 or manifest.get("lifecycle") != list(LIFECYCLE):
        raise Invalid("structure.json needs schema_version 1 and lifecycle [drafts, canon, archive]")
    dirs = set(manifest.get("infrastructure_directories", []))
    files = set(manifest.get("required_files", []))
    areas = manifest.get("content_areas")
    if not isinstance(areas, list) or not areas:
        raise Invalid("structure.json needs nonempty content_areas")
    for area in areas:
        if not isinstance(area, dict) or not isinstance(area.get("path"), str):
            raise Invalid("each content area needs a path")
        path = area["path"]
        dirs.add(path)
        dirs.update(f"{path}/{status}" for status in LIFECYCLE)
    for value in dirs | files:
        if not safe_path(value):
            raise Invalid(f"unsafe manifest path: {value!r}")
    dirs |= {p.as_posix() for d in list(dirs) for p in PurePosixPath(d).parents if str(p) != "."}
    files |= {f"{d}/README.md" for d in dirs}
    files.add("README.md")
    return dirs, files


class Validator:
    def __init__(self, root: Path, base: str | None = None):
        self.root = root.resolve()
        self.base = base
        self.errors: list[str] = []
        self.warnings: list[str] = []
        self.files: set[str] = set()
        self.manifest: dict = {}
        self.team: set[str] = set()
        self.team_changed = False
        self.ids: dict[tuple[str, str], str] = {}

    def error(self, path: str, message: str) -> None:
        self.errors.append(f"{path}: {message}")

    def read_json(self, rel: str) -> dict:
        try:
            value = strict_json((self.root / rel).read_text(encoding="utf-8"))
            if not isinstance(value, dict):
                raise Invalid("expected a JSON object")
            return value
        except (OSError, UnicodeError, json.JSONDecodeError, Invalid) as exc:
            self.error(rel, str(exc))
            return {}

    def approvals(self, rel: str, scope: str) -> bool:
        if not safe_path(rel) or not rel.startswith("studio/approvals/") or not rel.endswith(".json"):
            self.error(scope, "decision_ref must name studio/approvals/<id>.json")
            return False
        record = self.read_json(rel)
        good = set()
        approvals = record.get("approvals", [])
        if not isinstance(approvals, list):
            approvals = []
        for item in approvals:
            if not isinstance(item, dict):
                continue
            if item.get("person") in self.team and str(item.get("evidence", "")).strip():
                try:
                    dt.date.fromisoformat(str(item.get("date", "")))
                    good.add(item["person"])
                except ValueError:
                    pass
        digest = record.get("content_sha256", {}).get(scope) if isinstance(record.get("content_sha256"), dict) else None
        content = self.root / scope
        matching_content = content.is_file() and digest == hashlib.sha256(content.read_bytes()).hexdigest()
        scopes = record.get("scope", [])
        valid = (record.get("decision") == "approved" and isinstance(scopes, list) and scope in scopes
                 and len(good) >= 2 and matching_content)
        if not valid:
            self.error(scope, f"{rel} needs scope, matching content_sha256, decision approved and two distinct coauthor records with date/evidence")
        return valid

    def metadata(self, path: str, values: dict, stage: str) -> None:
        missing = REQUIRED_META - values.keys()
        if missing:
            self.error(path, "missing metadata: " + ", ".join(sorted(missing)))
        for key in REQUIRED_META & values.keys():
            if not isinstance(values[key], str) or not values[key].strip():
                self.error(path, f"{key} must be a nonempty string")
        if values.get("status") not in LIFECYCLE[stage]:
            self.error(path, f"status must be one of {sorted(LIFECYCLE[stage])}")
        if "version" in values and (not isinstance(values["version"], str) or not values["version"].strip()):
            self.error(path, "version must be a nonempty string")
        try:
            dt.date.fromisoformat(str(values.get("updated", "")))
        except ValueError:
            self.error(path, "updated must be YYYY-MM-DD")
        for key in ("reviewers", "canon_refs", "supersedes"):
            if key in values and not isinstance(values[key], list):
                self.error(path, f"{key} must be a JSON array")
        if stage == "archive":
            for key in ("archived_reason", "superseded_by"):
                if not isinstance(values.get(key), str) or not values[key].strip():
                    self.error(path, f"archive record needs {key}")
        if stage == "canon":
            self.approvals(str(values.get("decision_ref", "")), path)
        if isinstance(values.get("id"), str):
            identity = (values["id"], str(values.get("version", "unversioned")))
            if identity in self.ids:
                self.error(path, f"duplicate id/version also in {self.ids[identity]}")
            self.ids[identity] = path

    def links(self, path: str, text: str) -> None:
        # Fenced and inline code examples are not navigation links.
        text = re.sub(r"(?ms)^\s*(`{3,}|~{3,})[^\n]*\n.*?^\s*\1\s*$", "", text)
        text = re.sub(r"`+[^`]*`+", "", text)
        targets = [m.group(1).strip("<>") for m in LINK.finditer(text)]
        targets += [m.group(1).strip("<>") for m in REF_LINK.finditer(text)]
        for target in targets:
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            if parsed.path.startswith("/"):
                resolved = self.root / unquote(parsed.path.lstrip("/"))
            else:
                resolved = (self.root / path).parent / unquote(parsed.path)
            try:
                rel = resolved.resolve().relative_to(self.root).as_posix()
            except ValueError:
                self.error(path, f"link escapes repository: {target}")
                continue
            if rel != "." and rel not in self.files and not any(f.startswith(rel + "/") for f in self.files):
                self.error(path, f"broken relative link: {target}")

    def stage(self, path: str) -> str | None:
        for area in self.manifest.get("content_areas", []):
            for stage in LIFECYCLE:
                if path.startswith(area["path"] + "/" + stage + "/"):
                    return stage
        return None

    def compare_base(self) -> None:
        if not self.base:
            return
        if not re.fullmatch(r"[0-9a-fA-F]{40}", self.base):
            self.error("--base", "use a full 40-character commit SHA")
            return
        baseline = git(self.root, "show", f"{self.base}:studio/structure.json", check=False)
        if baseline.returncode:
            self.error("--base", "base commit lacks structure.json; omit --base for initial bootstrap only")
            return
        try:
            previous = strict_json(baseline.stdout)
            _, required = manifest_paths(previous)
        except (ValueError, TypeError) as exc:
            self.error("--base", f"invalid base manifest: {exc}")
            return
        old_list = git(self.root, "ls-tree", "-r", "--name-only", "-z", self.base)
        old_files = set(filter(None, old_list.stdout.split("\0")))
        protected = required | {f for f in old_files if f.endswith("/README.md") or f == "README.md"
                                or "/canon/" in f or "/archive/" in f}
        removed = (protected & old_files) - self.files
        manifest_changed = previous != self.manifest
        changed_archives = set()
        for path in sorted(old_files & self.files):
            if "/archive/" in path and not path.endswith("/README.md"):
                old = subprocess.run(["git", "-C", str(self.root), "show", f"{self.base}:{path}"], capture_output=True, check=True).stdout
                if (self.root / path).is_file() and old != (self.root / path).read_bytes():
                    changed_archives.add(path)
        affected = (removed | changed_archives | ({"studio/structure.json"} if manifest_changed else set())
                    | ({"studio/team.json"} if self.team_changed else set()))
        if not affected:
            return
        covered = set()
        for path in sorted(self.files):
            if not path.startswith("studio/migrations/") or not path.endswith(".json") or path in old_files:
                continue
            record = self.read_json(path)
            if record.get("base_sha") != self.base or not record.get("reason"):
                continue
            changes = record.get("changes", [])
            if not isinstance(changes, list):
                continue
            if not self.approvals(str(record.get("decision_ref", "")), path):
                continue
            for change in changes:
                if not isinstance(change, dict) or change.get("from") not in affected:
                    continue
                destination = change.get("to")
                # Deletion is not an archive. Every protected record keeps a reachable successor.
                if isinstance(destination, str) and destination in self.files:
                    covered.add(change["from"])
        for path in sorted(affected - covered):
            self.error(path, "protected removal/structure change needs a new migration record with base SHA, successor and two recorded coauthor approvals")

    def run(self) -> int:
        self.files = set(inventory(self.root))
        self.manifest = self.read_json("studio/structure.json")
        team = self.read_json("studio/team.json")
        self.team = coauthors(team)
        if self.base and re.fullmatch(r"[0-9a-fA-F]{40}", self.base):
            old_team = git(self.root, "show", f"{self.base}:studio/team.json", check=False)
            try:
                if old_team.returncode:
                    raise Invalid("base commit lacks studio/team.json")
                trusted_team = coauthors(strict_json(old_team.stdout))
                self.team_changed = trusted_team != self.team
                self.team = trusted_team
            except (ValueError, TypeError, AttributeError) as exc:
                self.error("studio/team.json", f"cannot establish base approval authority: {exc}")
                self.team = set()
        try:
            _, required = manifest_paths(self.manifest)
        except (Invalid, TypeError, KeyError) as exc:
            self.error("studio/structure.json", str(exc))
            return 1
        for path in sorted(required - self.files):
            self.error(path, "required file is missing")
        directories = {""}
        folded = {}
        for path in sorted(self.files):
            if not safe_path(path):
                self.error(path, "unsafe or Windows-incompatible path")
                continue
            for component in PurePosixPath(path).parents:
                if str(component) != ".":
                    directories.add(component.as_posix())
            for component in [PurePosixPath(path), *PurePosixPath(path).parents]:
                name = component.as_posix()
                key = name.casefold()
                if key in folded and folded[key] != name:
                    self.error(path, f"case collision with {folded[key]}")
                folded[key] = name
            actual = self.root / path
            if actual.is_symlink() or any(p.is_symlink() for p in actual.parents if p != self.root.parent):
                self.error(path, "symlinks are not allowed")
                continue
            if not actual.is_file():
                self.error(path, "tracked file is absent from worktree")
                continue
            if actual.stat().st_size > MAX_FILE:
                self.error(path, "file exceeds 20 MiB; store master outside Git and commit its manifest/preview")
                continue
            name = actual.name.lower()
            if (name.startswith(".env") and name not in {".env.example", ".env.template"}) or actual.suffix.lower() in {".pem", ".p12", ".pfx", ".key"}:
                self.error(path, "possible credential/private-key file is not allowed")
            stage = self.stage(path)
            if any(part in LIFECYCLE for part in PurePosixPath(path).parts[:-1]) and stage is None:
                self.error(path, "lifecycle folder is outside the registered content areas; update the structure contract")
            is_sidecar = path.endswith(".asset.json")
            if is_sidecar and stage and path[:-len(".asset.json")] not in self.files:
                self.error(path, "orphan sidecar has no associated artifact")
            needs_sidecar = (actual.suffix.lower() in ASSET_EXTS
                             or (stage in {"canon", "archive"} and actual.suffix.lower() != ".md" and not is_sidecar))
            if needs_sidecar:
                sidecar = path + ".asset.json"
                if sidecar not in self.files:
                    self.error(path, f"asset needs provenance/rights sidecar {sidecar}")
                else:
                    data = self.read_json(sidecar)
                    for field in REQUIRED_META | {"rights_holder", "license", "clearance", "sha256"}:
                        if not isinstance(data.get(field), str) or not data[field].strip():
                            self.error(sidecar, f"missing/non-string asset field {field}")
                    if data.get("clearance") not in {"project-authorized", "permission-on-file", "public-domain", "licensed"}:
                        self.error(sidecar, "unresolved rights: do not upload a binary while clearance is pending")
                    if data.get("sha256") != hashlib.sha256(actual.read_bytes()).hexdigest():
                        self.error(sidecar, "sha256 does not match the asset bytes")
                    if stage:
                        self.metadata(sidecar, data, stage)
            try:
                text = actual.read_text(encoding="utf-8")
            except UnicodeError:
                continue
            if SECRET_TOKEN.search(text):
                self.error(path, "possible live credential/private key detected; do not print or publish it")
            if actual.suffix.lower() == ".md":
                self.links(path, text)
                if stage and actual.name != "README.md":
                    try:
                        self.metadata(path, frontmatter(text), stage)
                    except Invalid as exc:
                        self.error(path, str(exc))
        for directory in sorted(directories):
            readme = f"{directory}/README.md" if directory else "README.md"
            if readme not in self.files:
                self.error(readme, "each versioned folder needs its own README.md")
        self.compare_base()
        return 1 if self.errors else 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=".", type=Path)
    parser.add_argument("--base", help="full base commit SHA for removal/migration checks")
    args = parser.parse_args()
    validator = Validator(args.root, args.base)
    try:
        result = validator.run()
    except (OSError, subprocess.CalledProcessError, ValueError, TypeError) as exc:
        print(f"ERROR: validator could not complete: {exc}", file=sys.stderr)
        return 2
    for message in validator.errors:
        print("ERROR: " + message)
    for message in validator.warnings:
        print("WARNING: " + message)
    print(f"Repository checks: {'FAIL' if result else 'PASS'}; {len(validator.files)} files; {len(validator.errors)} error(s).")
    return result


if __name__ == "__main__":
    raise SystemExit(main())
