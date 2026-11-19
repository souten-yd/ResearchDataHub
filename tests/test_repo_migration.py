"""Migration compatibility checks: QNAP and Linux share the legacy server and data identity."""
import json
import unittest
from pathlib import Path
import qnaplibrary
from qnaplibrary.config import DEFAULTS
from qnaplibrary.updater import asset_name, API

ROOT = Path(__file__).resolve().parents[1]


class ResearchDataHubMigrationTest(unittest.TestCase):
    def test_release_channel(self):
        self.assertEqual(qnaplibrary.REPO, "souten-yd/ResearchDataHub")
        self.assertEqual(qnaplibrary.APP_NAME, "ResearchDataHub")
        self.assertIn("/souten-yd/ResearchDataHub/releases/latest", API)

    def test_qnap_identity_and_asset_names(self):
        cfg = (ROOT / "qpkg/qpkg.cfg").read_text()
        self.assertIn('QPKG_NAME="QnapLibrary"', cfg)
        self.assertIn('QPKG_SERVICE_PORT="17871"', cfg)
        self.assertEqual(DEFAULTS["server"]["port"], 17871)
        self.assertEqual(asset_name(qnaplibrary.VERSION, "qpkg"), f"QnapLibrary_{qnaplibrary.VERSION}_x86_64.qpkg")
        self.assertEqual(asset_name(qnaplibrary.VERSION, "linux"), f"qnaplibrary-{qnaplibrary.VERSION}-linux.tar.gz")

    def test_both_packages_include_server_alias(self):
        linux = (ROOT / "scripts/build-linux.sh").read_text()
        qnap = (ROOT / "scripts/build-qpkg.sh").read_text()
        self.assertIn('"$ROOT/researchdatahub"', linux)
        self.assertIn('"$ROOT/researchdatahub"', qnap)
        self.assertIn('researchdatahub/cli.py', (ROOT / "scripts/inspect-qpkg.py").read_text())
        self.assertTrue((ROOT / "qpkg/shared/qnaplibrary.sh").is_file())
        self.assertTrue((ROOT / "rdh.sh").is_file())

    def test_auth_and_addon_compat(self):
        self.assertEqual(DEFAULTS["auth"]["rp_id"], "")
        self.assertEqual(DEFAULTS["auth"]["session_hours"], 720)
        manifest = json.loads((ROOT / "addon.json").read_text())
        self.assertEqual(manifest["version"], qnaplibrary.VERSION)


if __name__ == "__main__":
    unittest.main()
