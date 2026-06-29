import os
import subprocess
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
RUNTIME = REPO_ROOT / "scripts" / "chowmes-argus-configure-telegram-runtime"


class ArgusTelegramConfigRuntimeTests(unittest.TestCase):
    def make_fixture(self, payload: str, existing_env: str = "GEMINI_API_KEY=test\n"):
        temp = tempfile.TemporaryDirectory()
        root = Path(temp.name)
        profile = root / "profiles" / "argus"
        profile.mkdir(parents=True)
        env_file = profile / ".env"
        env_file.write_text(existing_env)
        payload_file = root / "payload.env"
        payload_file.write_text(payload)
        env = os.environ.copy()
        env.update(
            {
                "ARGUS_PROFILE_DIR": str(profile),
                "ARGUS_ENV_FILE": str(env_file),
            }
        )
        return temp, root, env, payload_file, env_file

    def run_runtime(self, env, payload_file, *args):
        return subprocess.run(
            [str(RUNTIME), "--payload", str(payload_file), *args],
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            env=env,
        )

    def test_refuses_when_payload_has_no_token(self):
        temp, _root, env, payload, _env_file = self.make_fixture("TELEGRAM_HOME_CHANNEL=123\n")
        with temp:
            result = self.run_runtime(env, payload)
        self.assertEqual(result.returncode, 2)
        self.assertIn("payload_token=missing", result.stdout)
        self.assertIn("ARGUS_TELEGRAM_BOT_TOKEN or equivalent local key is missing", result.stdout)

    def test_dry_run_reports_without_mutating_env(self):
        temp, _root, env, payload, env_file = self.make_fixture(
            "TELEGRAM_BOT_TOKEN=secret\nTELEGRAM_HOME_CHANNEL=123\nTELEGRAM_ALLOWED_USERS=456\n"
        )
        with temp:
            before = env_file.read_text()
            result = self.run_runtime(env, payload)
            after = env_file.read_text()
        self.assertEqual(result.returncode, 0, result.stdout)
        self.assertEqual(before, after)
        self.assertIn("argus_telegram_config_mode=dry-run", result.stdout)
        self.assertIn("payload_token=present", result.stdout)
        self.assertNotIn("secret", result.stdout)

    def test_execute_writes_canonical_profile_env_keys(self):
        temp, _root, env, payload, env_file = self.make_fixture(
            "TELEGRAM_BOT_TOKEN=secret\nTELEGRAM_HOME_CHANNEL=123\nTELEGRAM_ALLOWED_USERS=456\n"
        )
        with temp:
            result = self.run_runtime(env, payload, "--execute")
            written = env_file.read_text()
        self.assertEqual(result.returncode, 0, result.stdout)
        self.assertIn("GEMINI_API_KEY=test", written)
        self.assertIn("TELEGRAM_BOT_TOKEN=secret", written)
        self.assertIn("TELEGRAM_HOME_CHANNEL=123", written)
        self.assertIn("TELEGRAM_ALLOWED_USERS=456", written)
        self.assertIn("argus_env_updated=yes", result.stdout)
        self.assertNotIn("secret", result.stdout)

    def test_refuses_to_overwrite_existing_token_without_force(self):
        temp, _root, env, payload, env_file = self.make_fixture(
            "TELEGRAM_BOT_TOKEN=new-secret\n",
            existing_env="TELEGRAM_BOT_TOKEN=old-secret\n",
        )
        with temp:
            result = self.run_runtime(env, payload, "--execute")
            written = env_file.read_text()
        self.assertEqual(result.returncode, 2)
        self.assertIn("already has a Telegram token", result.stdout)
        self.assertEqual(written, "TELEGRAM_BOT_TOKEN=old-secret\n")

    def test_force_replaces_existing_token(self):
        temp, _root, env, payload, env_file = self.make_fixture(
            "TELEGRAM_BOT_TOKEN=new-secret\n",
            existing_env="TELEGRAM_BOT_TOKEN=old-secret\n",
        )
        with temp:
            result = self.run_runtime(env, payload, "--execute", "--force")
            written = env_file.read_text()
        self.assertEqual(result.returncode, 0, result.stdout)
        self.assertIn("TELEGRAM_BOT_TOKEN=new-secret", written)
        self.assertNotIn("old-secret", written)


if __name__ == "__main__":
    unittest.main()
