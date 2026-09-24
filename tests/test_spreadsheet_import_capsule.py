import unittest
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]


class SpreadsheetImportCapsuleTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.catalog = yaml.safe_load((ROOT / "catalog.yaml").read_text())
        cls.manifest_path = ROOT / "src/Tools/SpreadsheetImport/capsule.yaml"
        cls.manifest = yaml.safe_load(cls.manifest_path.read_text())

    def test_catalog_and_manifest_identity_match(self):
        entry = next(
            item for item in self.catalog["capsules"]
            if item["id"] == "saysol.serenity.spreadsheet-import"
        )
        self.assertEqual("implemented", entry["maturity"])
        self.assertEqual(str(self.manifest_path.relative_to(ROOT)), entry["manifest"])
        self.assertEqual(self.manifest["capsule"]["id"], entry["id"])
        self.assertEqual(self.manifest["capsule"]["version"], entry["version"])

    def test_unverified_capsule_has_no_mutating_operations(self):
        installation = self.manifest["installation"]
        self.assertEqual([], installation["files"])
        self.assertEqual([], installation["migrations"])
        self.assertEqual([], installation["edits"])
        evidence = {
            lane["evidence"] for lane in self.manifest["compatibility"]["serenity"]
        }
        self.assertEqual({"planned"}, evidence)

    def test_only_supported_adapter_is_present(self):
        adapters = ROOT / "src/Tools/SpreadsheetImport/dotnet/Adapters"
        self.assertTrue((adapters / "Serenity10/Serenity10SpreadsheetImportAdapter.cs").is_file())
        self.assertFalse(
            (adapters / "Serenity9/Serenity9SpreadsheetImportAdapter.cs").exists()
        )

    def test_serenity_compatibility_starts_at_10_5(self):
        self.assertEqual({"net10"}, set(self.catalog["compatibility_lanes"]))
        lanes = self.manifest["compatibility"]["serenity"]
        self.assertEqual(["net10"], [lane["lane"] for lane in lanes])
        self.assertEqual(">=10.5.0 <11.0.0", lanes[0]["version"])

    def test_no_shared_promotion_was_made(self):
        self.assertFalse(self.manifest["dependencies"]["shared"]["required"])


if __name__ == "__main__":
    unittest.main()
