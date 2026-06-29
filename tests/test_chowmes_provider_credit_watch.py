import py_compile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPT = REPO_ROOT / "scripts" / "chowmes-provider-credit-watch"


class ChowmesProviderCreditWatchTests(unittest.TestCase):
    def test_script_is_python_entrypoint_for_hermes_cron(self):
        text = SCRIPT.read_text()

        self.assertTrue(text.startswith("#!/usr/bin/env python3"))
        self.assertNotIn("if [ -f /opt/data/.env ]; then", text)
        self.assertIn("def load_env_file(", text)
        self.assertIn("REMOTE_ENV = Path(\"/opt/data/.env\")", text)
        py_compile.compile(str(SCRIPT), doraise=True)


if __name__ == "__main__":
    unittest.main()
