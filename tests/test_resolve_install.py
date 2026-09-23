import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("resolve_install", ROOT / "tools/resolve_install.py")
RESOLVER = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(RESOLVER)


class ResolverTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.host = self.root / "host.json"
        self.host.write_text(json.dumps({
            "repository": {"root": "/host", "branch": "main", "head": "a" * 40, "worktree_clean": True},
            "serenity_version": "10.5.2", "dotnet_version": "10.0.1", "capabilities": ["navigation"]
        }))

    def tearDown(self):
        self.temp.cleanup()

    def write_case(self, capsules):
        catalog = {
            "defaults": {"lockfile": ".saysol/saysol.lock.yaml"},
            "compatibility_lanes": {"net10": {"serenity": ">=10.5.0 <11.0.0", "dotnet": "10.0"}},
            "capsules": []
        }
        for capsule_id, values in capsules.items():
            path = f"{capsule_id}.yaml"
            catalog["capsules"].append({"id": capsule_id, "version": "1.0.0", "maturity": "released", "manifest": path})
            manifest = {
                "capsule": {"id": capsule_id, "version": "1.0.0", "delivery": "source-copy"},
                "compatibility": {"serenity": [{"lane": "net10", "version": ">=10.5.0 <11.0.0", "dotnet": "10.0", "evidence": "verified"}], "required_capabilities": values.get("capabilities", [])},
                "dependencies": {"shared": values.get("shared", {"required": False, "version": None}), "capsules": values.get("dependencies", []), "nuget": values.get("nuget", []), "npm": [], "conflicts": values.get("conflicts", []), "supersedes": [], "integrates_with": [], "provided_by_host": []},
                "ownership": {"claims": values.get("claims", [])},
                "installation": {"files": [], "migrations": [], "edits": [], "human_gates": []},
                "validation": {"commands": [], "behavioral_checks": []}
            }
            (self.root / path).write_text(yaml.safe_dump(manifest))
        catalog_path = self.root / "catalog.yaml"
        catalog_path.write_text(yaml.safe_dump(catalog))
        return catalog_path

    def test_resolves_required_dependency_first(self):
        catalog = self.write_case({
            "base": {},
            "feature": {"dependencies": [{"id": "base", "version": ">=1.0.0", "optional": False}]}
        })
        plan = RESOLVER.build_plan(catalog, self.host, ["feature"])
        self.assertEqual(["base", "feature"], plan["install_order"])
        self.assertFalse(plan["mutates_host"])

    def test_rejects_exclusive_ownership_collision(self):
        claim = [{"kind": "route", "key": "/api/tool", "policy": "exclusive"}]
        catalog = self.write_case({"one": {"claims": claim}, "two": {"claims": claim}})
        with self.assertRaisesRegex(RESOLVER.ResolutionError, "Ownership collision"):
            RESOLVER.build_plan(catalog, self.host, ["one", "two"])

    def test_rejects_missing_host_capability(self):
        catalog = self.write_case({"feature": {"capabilities": ["background-jobs"]}})
        with self.assertRaisesRegex(RESOLVER.ResolutionError, "background-jobs"):
            RESOLVER.build_plan(catalog, self.host, ["feature"])

    def test_rejects_package_version_collision(self):
        catalog = self.write_case({
            "one": {"nuget": [{"id": "Example.Package", "version": "1.0.0"}]},
            "two": {"nuget": [{"id": "Example.Package", "version": "2.0.0"}]}
        })
        with self.assertRaisesRegex(RESOLVER.ResolutionError, "version collision"):
            RESOLVER.build_plan(catalog, self.host, ["one", "two"])


if __name__ == "__main__":
    unittest.main()
