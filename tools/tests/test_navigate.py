"""Navigation behavior in isolated fixtures; no project files or decisions are changed.

Проверки навигации в отдельных временных репозиториях; решения авторов не создаются.
"""
from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from navigate import (CATALOG_PATH, END, GENERATED, MAP_PATH, START, NavigationError,
                      Repository, replace_navigation, safe_relative, without_navigation)


class NavigationTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        subprocess.run(["git", "init", "-q", str(self.root)], check=True)
        self.put(".gitignore", "__pycache__/\nprivate-local/\n")
        for folder in ("", "studio", "templates", "narrative", "narrative/scenes", "narrative/scenes/drafts", "narrative/scenes/canon", "narrative/scenes/archive"):
            self.put((folder + "/" if folder else "") + "README.md", f"# {folder or 'Project'}\n\nManual text remains here.\n")
        for name in ("AGENTS.md", "studio/WORKFLOW.md", "studio/REPOSITORY_RULES.md", "studio/CANON_POLICY.md", "studio/LANGUAGE_POLICY.md", "studio/NAMING_AND_METADATA.md", "studio/NAVIGATION.md", "templates/scene.md"):
            self.put(name, "# Fixture instructions\n")
        self.put("studio/structure.json", json.dumps({"content_areas": [{"path": "narrative/scenes", "title": "Сцены"}]}))
        self.route = {"id": "scene", "title": {"ru": "Сцена", "en": "Scene"},
                      "description": {"ru": "Отдельная сцена", "en": "A single scene"},
                      "aliases": ["сцена", "scene"], "target": "narrative/scenes/drafts",
                      "templates": ["templates/scene.md"], "context": ["studio/CANON_POLICY.md"]}
        self.config([self.route])
        self.card = "narrative/scenes/drafts/scene-a.md"
        self.put(self.card, '---\nid: SCENE-1\ntitle: "Мост / Bridge"\nstatus: draft\nowner: ivan\nversion: v0-1\n---\n# Мост\n\nПод мостом спрятан маяк.\n')

    def put(self, name, text):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")

    def config(self, routes):
        self.put("studio/navigation.json", json.dumps({"schema_version": 1, "routes": routes}, ensure_ascii=False))

    def test_build_is_idempotent_and_check_detects_new_content(self):
        changed = Repository(self.root).refresh(write=True)
        self.assertIn(MAP_PATH, changed)
        self.assertIn(CATALOG_PATH, changed)
        self.assertEqual([], Repository(self.root).refresh(write=False))
        self.assertEqual([], Repository(self.root).refresh(write=True))
        self.put("narrative/scenes/drafts/second.md", "# Another scene\n")
        self.assertIn("narrative/scenes/drafts/README.md", Repository(self.root).refresh(write=False))

    def test_manual_text_before_and_after_block_is_unchanged(self):
        original = "# Manual\n\nKeep  double spaces.\n\n"
        self.put("README.md", original + START + "\nold\n" + END + "\n\nManual footer!\n")
        Repository(self.root).refresh(write=True)
        actual = (self.root / "README.md").read_text(encoding="utf-8")
        self.assertEqual(original + "\n\nManual footer!\n", without_navigation(actual))

    def test_inline_marker_documentation_is_preserved(self):
        manual = f"# Tool guide\n\nThe markers are `{START}` and `{END}`.\n"
        self.put("README.md", manual)
        Repository(self.root).refresh(write=True)
        result = (self.root / "README.md").read_text(encoding="utf-8")
        self.assertTrue(without_navigation(result).startswith(manual))
        self.assertEqual([], Repository(self.root).refresh(write=False))

    def test_malformed_marker_prevents_any_write(self):
        self.put("narrative/scenes/drafts/README.md", "# Broken\n" + START)
        root_before = (self.root / "README.md").read_bytes()
        with self.assertRaises(NavigationError):
            Repository(self.root).refresh(write=True)
        self.assertEqual(root_before, (self.root / "README.md").read_bytes())
        self.assertFalse((self.root / MAP_PATH).exists())

    def test_handwritten_generated_destination_is_not_overwritten(self):
        self.put(MAP_PATH, "# A person's notes\n")
        with self.assertRaises(NavigationError):
            Repository(self.root).refresh(write=True)
        self.assertEqual("# A person's notes\n", (self.root / MAP_PATH).read_text())

    def test_ignored_generated_destination_is_not_created_or_overwritten(self):
        self.put(".gitignore", MAP_PATH + "\n")
        with self.assertRaisesRegex(NavigationError, "ignored"):
            Repository(self.root).refresh(write=True)
        self.assertFalse((self.root / MAP_PATH).exists())
        self.put(MAP_PATH, "# Private handwritten notes\n")
        with self.assertRaisesRegex(NavigationError, "ignored"):
            Repository(self.root).refresh(write=True)
        self.assertEqual("# Private handwritten notes\n", (self.root / MAP_PATH).read_text())

    def test_readme_bytes_with_invalid_encoding_are_not_overwritten(self):
        path = self.root / "README.md"
        path.write_bytes(b"\xff\xfe\x00\x00")
        with self.assertRaises(NavigationError):
            Repository(self.root).refresh(write=True)
        self.assertEqual(b"\xff\xfe\x00\x00", path.read_bytes())

    def test_missing_folder_readme_is_reported(self):
        self.put("narrative/scenes/drafts/new-area/test.md", "# A scene\n")
        with self.assertRaisesRegex(NavigationError, "README"):
            Repository(self.root).refresh(write=False)

    def test_ignored_files_do_not_appear_or_get_read(self):
        self.put("private-local/secret.md", "secret text")
        self.put("__pycache__/cached.pyc", "cache")
        repo = Repository(self.root)
        self.assertNotIn("private-local/secret.md", repo.files)
        self.assertEqual([], repo.find("secret text", all_text=True))
        with self.assertRaises(NavigationError):
            repo.context("private-local/secret.md")

    def test_route_cannot_escape_or_target_missing_path(self):
        for target in ("../outside", "/tmp/outside", "C:\\outside", "missing/place"):
            with self.subTest(target=target):
                self.config([{**self.route, "target": target}])
                with self.assertRaises(NavigationError):
                    Repository(self.root)

    def test_symlink_cannot_read_or_write_outside(self):
        outside = self.root.parent / (self.root.name + "-outside")
        outside.write_text("Do not read or edit", encoding="utf-8")
        self.addCleanup(lambda: outside.unlink(missing_ok=True))
        (self.root / "linked.md").symlink_to(outside)
        with self.assertRaises(NavigationError):
            Repository(self.root)
        self.assertEqual("Do not read or edit", outside.read_text())

    def test_portable_paths(self):
        for path in ("../x", "x/../y", "x\\y", "CON.md", "x/NUL", "x ", "x//y", "x:1", ".git/config"):
            with self.subTest(path=path), self.assertRaises(NavigationError):
                safe_relative(path)
        self.assertEqual("narrative/scenes/drafts", safe_relative("narrative/scenes/drafts"))

    def test_russian_and_english_route_queries(self):
        repo = Repository(self.root)
        self.assertEqual("scene", repo.where("Куда положить сцену scene")[0]["id"])
        self.assertEqual("scene", repo.where("СЦЕНА")[0]["id"])
        self.assertEqual("scene", repo.where("scene")[0]["id"])
        self.assertEqual([], repo.where("nonexistentword"))

    def test_find_exact_id_and_unicode_body(self):
        repo = Repository(self.root)
        self.assertEqual(self.card, repo.find("SCENE-1")[0]["path"])
        self.assertEqual("draft", repo.find("SCENE-1")[0]["status"])
        self.assertEqual(self.card, repo.find("МАЯК")[0]["path"])

    def test_large_source_body_is_opt_in(self):
        self.put("narrative/scenes/drafts/large.md", "# Source\n" + "x" * 140000 + "\nUNIQUE-SOURCE-TERM\n")
        repo = Repository(self.root)
        self.assertEqual([], repo.find("UNIQUE-SOURCE-TERM"))
        self.assertEqual(1, len(repo.find("UNIQUE-SOURCE-TERM", all_text=True)))

    def test_context_includes_scoped_rules_and_real_canon(self):
        self.put("narrative/AGENTS.md", "# Scoped instruction\n")
        self.put("narrative/scenes/canon/accepted.md", "# Fixture only\n")
        result = Repository(self.root).context(self.card)
        self.assertEqual("AGENTS.md", result[0])
        self.assertIn("narrative/AGENTS.md", result)
        self.assertIn("narrative/scenes/drafts/README.md", result)
        self.assertIn("narrative/scenes/canon/accepted.md", result)
        self.assertEqual(self.card, result[-1])
        self.assertEqual(len(result), len(set(result)))

    def test_catalogue_reads_status_without_changing_source(self):
        before = (self.root / self.card).read_bytes()
        Repository(self.root).refresh(write=True)
        catalogue = (self.root / CATALOG_PATH).read_text(encoding="utf-8")
        self.assertIn("SCENE-1", catalogue)
        self.assertIn("| draft | ivan |", catalogue)
        self.assertEqual(before, (self.root / self.card).read_bytes())

    def test_real_asset_sidecars_are_searchable_and_catalogued(self):
        sidecar = "narrative/scenes/drafts/sketch.png.asset.json"
        self.put(sidecar, json.dumps({"id": "ART-0001", "title": "Bridge sketch", "status": "draft", "owner": "ivan"}))
        self.put("templates/dummy.png.asset.json", json.dumps({"id": "EXAMPLE-ONLY", "title": "Example"}))
        repo = Repository(self.root)
        self.assertEqual(sidecar, repo.find("ART-0001")[0]["path"])
        self.assertEqual("draft", repo.find("ART-0001")[0]["status"])
        catalogue = repo.content_catalogue()
        self.assertIn("ART-0001", catalogue)
        self.assertIn("паспорт / sidecar", catalogue)
        self.assertNotIn("EXAMPLE-ONLY", catalogue)

    def test_duplicate_route_id_rejected(self):
        self.config([self.route, self.route])
        with self.assertRaisesRegex(NavigationError, "Duplicate"):
            Repository(self.root)


if __name__ == "__main__":
    unittest.main()
