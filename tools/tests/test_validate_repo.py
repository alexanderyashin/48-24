"""Meaningful failure cases for a guard that protects collaborative content."""
import hashlib
import importlib.util
import json
import subprocess
import tempfile
import unittest
from pathlib import Path

SPEC = importlib.util.spec_from_file_location("validate_repo", Path(__file__).resolve().parents[1] / "validate_repo.py")
guard = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(guard)


class RepositoryGuardTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.manifest = {
            "schema_version": 1,
            "lifecycle": ["drafts", "canon", "archive"],
            "content_areas": [{"path": "world/bible", "title": "Bible", "description": "Fixture"}],
            "required_files": ["README.md", "AGENTS.md", "LICENSE", "studio/structure.json", "studio/team.json"],
            "infrastructure_directories": ["studio", "studio/approvals", "studio/migrations"],
        }
        self.json("studio/structure.json", self.manifest)
        self.json("studio/team.json", {"people": [
            {"id": "author-one", "role": "coauthor"},
            {"id": "author-two", "role": "coauthor"},
        ]})
        _, required = guard.manifest_paths(self.manifest)
        for path in required:
            if not (self.root / path).exists():
                self.write(path, "# Fixture\n")
        self.content("world/bible/drafts/test.md")

    def write(self, path, text):
        target = self.root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(text, encoding="utf-8")

    def json(self, path, value):
        self.write(path, json.dumps(value, indent=2) + "\n")

    def content(self, path, status="draft", extra="", identity="fixture-object"):
        self.write(path, f'''---
id: {identity}
title: Fixture content
status: {status}
version: "0.1.0"
owner: author-one
updated: "2026-11-19"
source: test fixture
ai_assistance: none
{extra}---
# Fixture

Meaningful text.
''')

    def run_guard(self, base=None):
        validator = guard.Validator(self.root, base)
        code = validator.run()
        return code, "\n".join(validator.errors)

    def assertFails(self, contains, base=None):
        code, errors = self.run_guard(base)
        self.assertNotEqual(code, 0, errors)
        self.assertIn(contains, errors)

    def shellgit(self, *args):
        return subprocess.run(["git", "-C", str(self.root), *args], capture_output=True,
                              text=True, check=True).stdout.strip()

    def baseline(self):
        self.shellgit("init", "-q")
        self.shellgit("-c", "user.name=Guard fixture", "-c", "user.email=fixture@example.invalid", "add", ".")
        self.shellgit("-c", "user.name=Guard fixture", "-c", "user.email=fixture@example.invalid", "commit", "-qm", "fixture")
        return self.shellgit("rev-parse", "HEAD")

    def approval(self, target, path="studio/approvals/test.json", people=None):
        self.json(path, {
            "id": "fixture-approval", "scope": [target], "decision": "approved",
            "content_sha256": {target: hashlib.sha256((self.root / target).read_bytes()).hexdigest()},
            "approvals": [{"person": p, "date": "2026-11-19", "evidence": "TEST FIXTURE ONLY"}
                          for p in (people or ["author-one", "author-two"])],
        })

    def test_valid_initial_repository(self):
        self.assertEqual(self.run_guard(), (0, ""))

    def test_missing_readme_is_rejected(self):
        (self.root / "world/bible/drafts/README.md").unlink()
        self.assertFails("README.md")

    def test_new_nested_folder_needs_readme(self):
        self.content("world/bible/drafts/nested/other.md", identity="other")
        self.assertFails("nested/README.md")

    def test_unregistered_canon_folder_cannot_bypass_reviews(self):
        self.write("other/README.md", "# Fixture\n")
        self.write("other/canon/README.md", "# Fixture\n")
        self.write("other/canon/unreviewed.md", "# Unreviewed\n")
        self.assertFails("outside the registered content areas")

    def test_draft_cannot_call_itself_canonical(self):
        self.content("world/bible/drafts/test.md", status="canonical")
        self.assertFails("status must be")

    def test_canon_needs_two_humans_and_exact_approved_bytes(self):
        target = "world/bible/canon/accepted.md"
        self.content(target, status="canonical", extra="decision_ref: studio/approvals/test.json\n", identity="accepted")
        self.approval(target, people=["author-one", "author-one"])
        self.assertFails("two distinct coauthor")
        self.approval(target)
        self.assertEqual(self.run_guard(), (0, ""))
        self.write(target, (self.root / target).read_text() + "\nUnreviewed change.\n")
        self.assertFails("matching content_sha256")

    def test_archive_requires_explanation_and_successor_field(self):
        self.content("world/bible/archive/old.md", status="rejected", identity="old")
        self.assertFails("archived_reason")

    def test_versioned_identity_cannot_silently_duplicate(self):
        self.content("world/bible/drafts/duplicate.md")
        self.assertFails("duplicate id/version")

    def test_broken_link_is_rejected(self):
        self.write("README.md", "[Missing](world/no-file.md)\n")
        self.assertFails("broken relative link")

    def test_fenced_examples_are_not_checked_as_links(self):
        self.write("README.md", "# Fixture\n\n```md\n[example](replace-me.md)\n```\n")
        self.assertEqual(self.run_guard(), (0, ""))

    def test_case_collision_is_rejected(self):
        self.write("world/bible/drafts/Test.md", "# Not a portable path\n")
        self.assertFails("case collision")

    def test_windows_reserved_name_is_rejected(self):
        self.write("CON.txt", "reserved\n")
        self.assertFails("Windows-incompatible")

    def test_symlink_is_rejected(self):
        (self.root / "secret-link.txt").symlink_to(self.root / "LICENSE")
        self.assertFails("symlinks are not allowed")

    def test_binary_requires_rights_record(self):
        (self.root / "world/bible/drafts/test.png").write_bytes(b"\x89PNG\x00fixture")
        self.assertFails("provenance/rights sidecar")

    def test_pending_clearance_is_not_publication_permission(self):
        asset = "world/bible/drafts/test.png"
        (self.root / asset).write_bytes(b"\x89PNG\x00fixture")
        self.json(asset + ".asset.json", {
            "id": "fixture-image", "title": "Image", "status": "draft", "owner": "author-one",
            "updated": "2026-11-19", "source": "fixture", "rights_holder": "unknown",
            "license": "unknown", "clearance": "pending", "ai_assistance": "none",
        })
        self.assertFails("clearance is pending")

    def test_asset_change_invalidates_its_provenance_record(self):
        asset = "world/bible/drafts/test.png"
        data = b"\x89PNG\x00fixture"
        (self.root / asset).write_bytes(data)
        self.json(asset + ".asset.json", {
            "id": "fixture-image", "title": "Image", "status": "draft", "owner": "author-one",
            "updated": "2026-11-19", "source": "fixture", "rights_holder": "fixture",
            "license": "fixture only", "clearance": "project-authorized", "ai_assistance": "none",
            "sha256": hashlib.sha256(data).hexdigest(),
        })
        self.assertEqual(self.run_guard(), (0, ""))
        (self.root / asset).write_bytes(data + b"changed")
        self.assertFails("sha256 does not match")

    def test_env_file_is_rejected_without_revealing_content(self):
        self.write(".env", "LOCAL_VALUE=fixture\n")
        self.assertFails("credential/private-key file")

    def test_live_token_shape_is_rejected_without_printing_token(self):
        token = "ghp" + "_" + "A" * 36
        self.write("notes.md", token)
        _, errors = self.run_guard()
        self.assertIn("possible live credential", errors)
        self.assertNotIn(token, errors)

    def test_structure_shrink_cannot_be_hidden_by_editing_manifest(self):
        base = self.baseline()
        self.manifest["required_files"].remove("LICENSE")
        self.json("studio/structure.json", self.manifest)
        self.shellgit("rm", "LICENSE")
        self.assertFails("protected removal/structure change", base)

    def test_append_only_archive_enforced_against_baseline(self):
        target = "world/bible/archive/old.md"
        self.content(target, status="rejected", identity="old",
                     extra="archived_reason: Rejected for fixture\nsuperseded_by: none\n")
        base = self.baseline()
        self.write(target, (self.root / target).read_text() + "\nAltered historical record.\n")
        self.assertFails("protected removal/structure change", base)

    def test_plain_canonical_json_cannot_bypass_approval(self):
        self.json("world/bible/canon/palette.json", {"background": "#010203"})
        self.assertFails("provenance/rights sidecar")

    def test_canonical_data_uses_hashed_approved_sidecar(self):
        artifact = "world/bible/canon/palette.json"
        self.json(artifact, {"background": "#010203"})
        sidecar = artifact + ".asset.json"
        self.json(sidecar, {
            "id": "fixture-palette", "title": "Palette", "status": "canonical", "owner": "author-one",
            "updated": "2026-11-19", "source": "fixture", "rights_holder": "fixture where applicable",
            "license": "fixture only", "clearance": "project-authorized", "ai_assistance": "none",
            "sha256": hashlib.sha256((self.root / artifact).read_bytes()).hexdigest(),
            "decision_ref": "studio/approvals/test.json",
        })
        self.approval(sidecar)
        self.assertEqual(self.run_guard(), (0, ""))
        self.json(artifact, {"background": "#abcdef"})
        self.assertFails("sha256 does not match")

    def test_draft_csv_register_remains_lightweight(self):
        self.write("world/bible/drafts/register.csv", "id,title\nEXAMPLE,Fixture\n")
        self.assertEqual(self.run_guard(), (0, ""))

    def test_orphan_canonical_sidecar_is_rejected(self):
        self.json("world/bible/canon/nothing.json.asset.json", {"status": "canonical"})
        self.assertFails("orphan sidecar")

    def test_duplicate_front_matter_key_is_rejected(self):
        self.content("world/bible/drafts/test.md", extra="status: canonical\n")
        self.assertFails("duplicate metadata key status")

    def test_duplicate_json_key_is_rejected(self):
        self.write("studio/team.json", '{"people": [], "people": []}\n')
        self.assertFails("duplicate JSON key people")

    def test_new_team_members_cannot_approve_themselves_in_same_change(self):
        base = self.baseline()
        self.json("studio/team.json", {"people": [
            {"id": "new-one", "role": "coauthor"}, {"id": "new-two", "role": "coauthor"}
        ]})
        target = "world/bible/canon/injected.md"
        self.content(target, status="canonical", identity="injected",
                     extra="decision_ref: studio/approvals/test.json\n")
        self.approval(target, people=["new-one", "new-two"])
        self.assertFails("two distinct coauthor", base)

    def test_broken_local_image_is_a_broken_link(self):
        self.write("README.md", "![Preview](missing.png)\n")
        self.assertFails("broken relative link")

    def test_root_directory_link_and_anchor_are_allowed(self):
        self.write("world/README.md", "[Root](..)\n[Heading](#heading)\n")
        self.assertEqual(self.run_guard(), (0, ""))

    def test_documented_approved_migration_can_preserve_successor(self):
        base = self.baseline()
        self.manifest["required_files"].remove("LICENSE")
        self.manifest["required_files"].append("LICENSE.txt")
        self.json("studio/structure.json", self.manifest)
        self.shellgit("mv", "LICENSE", "LICENSE.txt")
        migration = "studio/migrations/test.json"
        self.json(migration, {
            "base_sha": base, "reason": "Test migration fixture", "decision_ref": "studio/approvals/test.json",
            "changes": [{"from": "LICENSE", "to": "LICENSE.txt"},
                        {"from": "studio/structure.json", "to": "studio/structure.json"}],
        })
        self.approval(migration)
        self.assertEqual(self.run_guard(base), (0, ""))


if __name__ == "__main__":
    unittest.main()
