import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPT = REPO_ROOT / "scripts" / "chow-fresh-argus-telegram-session"


class ChowFreshArgusTelegramSessionScriptTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.text = SCRIPT.read_text()

    def test_script_exists_and_targets_argus_profile(self):
        self.assertTrue(SCRIPT.exists())
        self.assertIn("/opt/data/profiles/argus", self.text)
        self.assertIn("-p argus gateway restart", self.text)
        self.assertIn("-p argus gateway status", self.text)

    def test_clears_argus_specific_telegram_dm_keys(self):
        self.assertIn("argus:telegram:dm:", self.text)
        self.assertIn("agent:argus:telegram:dm:", self.text)
        self.assertIn("telegram:dm:", self.text)
        self.assertIn("argus_cleared_sessions=", self.text)

    def test_preserves_argus_owner_approval_in_profile_pairing(self):
        self.assertIn('profile_dir / "pairing"', self.text)
        self.assertIn('profile_dir / "platforms" / "pairing"', self.text)
        self.assertIn("preserved_owner_approval_during_argus_fresh_session_reset", self.text)


if __name__ == "__main__":
    unittest.main()
