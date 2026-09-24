import json
import stat
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]


class SandboxContractTests(unittest.TestCase):
    def test_candidate_is_not_falsely_approved(self):
        manifest = yaml.safe_load((ROOT / "sandbox/manifest.yaml").read_text())
        self.assertEqual("candidate-unvalidated", manifest["state"])
        self.assertFalse(manifest["approved"])
        self.assertEqual([], manifest["control_host"]["capsules_installed"])
        self.assertGreaterEqual(tuple(map(int, manifest["serenity"]["minimum_supported"].split("."))), (10, 5, 0))

    def test_dependency_pins_and_seed_contract(self):
        manifest = yaml.safe_load((ROOT / "sandbox/manifest.yaml").read_text())
        package = json.loads((ROOT / "sandbox/host/package.json").read_text())
        self.assertEqual("10.5.1", package["dependencies"]["@serenity-is/corelib"])
        self.assertEqual("10.5.2", manifest["serenity"]["nuget"]["Serenity.Net.Web"])
        self.assertEqual(100, manifest["seed"]["counts"]["orders"])
        self.assertEqual(300, manifest["seed"]["counts"]["order_details"])

    def test_lifecycle_scripts_are_executable_and_guarded(self):
        for name in ("preflight.sh", "instantiate.sh", "dispose.sh", "instance-sandboxctl.sh"):
            mode = (ROOT / "sandbox/scripts" / name).stat().st_mode
            self.assertTrue(mode & stat.S_IXUSR, name)
        disposal = (ROOT / "sandbox/scripts/dispose.sh").read_text()
        self.assertIn(".saysol-sandbox-instance", disposal)
        self.assertNotIn("rm -rf", disposal)

    def test_evidence_schema_and_required_warning(self):
        json.loads((ROOT / "sandbox/evidence/evidence.schema.json").read_text())
        guide = (ROOT / "wiki/Sandbox-Testing-Guide.md").read_text()
        self.assertIn("Do not test a SaySol tool against a sandbox that has not first passed baseline validation.", guide)


if __name__ == "__main__":
    unittest.main()
