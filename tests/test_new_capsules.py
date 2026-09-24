import unittest
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
CAPSULES = ("ThemeKits", "WidgetLibrary", "AdminConfiguration")


class NewCapsuleTests(unittest.TestCase):
    def test_capsules_remain_install_blocked(self):
        catalog = yaml.safe_load((ROOT / "catalog.yaml").read_text())
        entries = {item["id"]: item for item in catalog["capsules"]}
        for folder in CAPSULES:
            manifest = yaml.safe_load(
                (ROOT / f"src/Tools/{folder}/capsule.yaml").read_text()
            )
            capsule_id = manifest["capsule"]["id"]
            self.assertEqual("implemented", entries[capsule_id]["maturity"])
            self.assertEqual([], manifest["installation"]["files"])
            self.assertEqual([], manifest["installation"]["edits"])
            self.assertEqual([], manifest["installation"]["migrations"])

    def test_admin_configuration_models_exclude_secret_values(self):
        core = ROOT / "src/Tools/AdminConfiguration/dotnet/Core"
        text = "\n".join(path.read_text() for path in core.glob("*.cs"))
        for forbidden in ("ConnectionString", "Password", "SecretValue", "CredentialValue"):
            self.assertNotIn(forbidden, text)

    def test_widget_core_does_not_accept_raw_html(self):
        source = (
            ROOT / "src/Tools/WidgetLibrary/ts/src/widgets.ts"
        ).read_text()
        self.assertNotIn("innerHTML", source)
        self.assertNotIn("insertAdjacentHTML", source)
        self.assertIn("textContent", source)

    def test_widget_catalog_separates_native_and_external_sources(self):
        native = (ROOT / "src/Tools/WidgetLibrary/ts/src/native/serenity/index.ts").read_text()
        adminlte = (ROOT / "src/Tools/WidgetLibrary/ts/src/external/adminlte/index.ts").read_text()
        manifest = yaml.safe_load(
            (ROOT / "src/Tools/WidgetLibrary/capsule.yaml").read_text()
        )

        self.assertIn('id: "serenity-corelib-10.5"', native)
        self.assertIn('native("Widget"', native)
        self.assertIn('native("EntityGrid"', native)
        self.assertIn('requiredByDefault: false', adminlte)
        self.assertIn('mapping("Info Box"', adminlte)
        self.assertEqual([], manifest["dependencies"]["npm"])


if __name__ == "__main__":
    unittest.main()
