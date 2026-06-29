import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPT = REPO_ROOT / "scripts" / "chowmes-argus-complete-activation"


class ArgusCompleteActivationScriptTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.text = SCRIPT.read_text()

    def test_script_is_executable(self):
        self.assertTrue(SCRIPT.exists())
        self.assertTrue(SCRIPT.stat().st_mode & 0o111)

    def test_default_mode_is_dry_run_and_execute_is_explicit(self):
        self.assertIn("execute=0", self.text)
        self.assertIn("argus_complete_activation_mode=dry-run", self.text)
        self.assertIn("--execute)", self.text)
        self.assertIn("argus_complete_activation_mode=execute", self.text)

    def test_execute_sequence_is_configure_then_activate_then_cron_then_e2e(self):
        configure = self.text.index("argus-configure-telegram")
        activate = self.text.index("argus-activate")
        migrate = self.text.index("argus-migrate-ci-cron")
        status = self.text.index("argus-e2e-status")

        self.assertLess(configure, activate)
        self.assertLess(activate, migrate)
        self.assertLess(migrate, status)
        self.assertIn("chowmes-ci-e2e-status\" --require-argus-e2e", self.text)

    def test_dry_run_does_not_start_gateway_or_migrate_cron(self):
        self.assertIn("activation and cron migration are not executed in this dry run", self.text)
        self.assertIn('if [ "$execute" != "1" ]; then', self.text)


if __name__ == "__main__":
    unittest.main()
