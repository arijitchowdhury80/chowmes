import os
import subprocess
import tempfile
import textwrap
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
RUNTIME = REPO_ROOT / "scripts" / "chowmes-argus-migrate-ci-cron-runtime"


class ArgusCronMigrationRuntimeTests(unittest.TestCase):
    def make_fixture(self, *, token: bool = False, gateway: str = "stopped"):
        temp = tempfile.TemporaryDirectory()
        root = Path(temp.name)
        profile = root / "profiles" / "argus"
        global_scripts = root / "scripts"
        fake_bin = root / "bin"
        profile.mkdir(parents=True)
        global_scripts.mkdir(parents=True)
        fake_bin.mkdir(parents=True)
        (profile / "SOUL.md").write_text("# Argus\n")
        (profile / ".env").write_text(
            ("ARGUS_TELEGRAM_BOT_TOKEN=test\n" if token else "GEMINI_API_KEY=test\n")
        )
        for name in ["competitive-research-daily.sh", "competitive-research-weekly.sh"]:
            path = global_scripts / name
            path.write_text("#!/bin/sh\necho ok\n")
            path.chmod(0o755)
        hermes = fake_bin / "hermes"
        hermes.write_text(
            textwrap.dedent(
                f"""\
                #!/bin/sh
                echo "$*" >> "{root}/hermes-calls.log"
                case "$*" in
                  "-p argus gateway status")
                    echo "Gateway: {gateway}"
                    ;;
                  "-p argus cron list")
                    echo "No jobs"
                    ;;
                  "-p argus cron create"*)
                    echo "created"
                    ;;
                  *)
                    echo "fake hermes: $*" >&2
                    ;;
                esac
                """
            )
        )
        hermes.chmod(0o755)
        env = os.environ.copy()
        env.update(
            {
                "ARGUS_PROFILE_DIR": str(profile),
                "GLOBAL_SCRIPT_DIR": str(global_scripts),
                "PROFILE_SCRIPT_DIR": str(profile / "scripts"),
                "HERMES_BIN": str(hermes),
            }
        )
        return temp, root, env

    def run_runtime(self, env, *args):
        return subprocess.run(
            [str(RUNTIME), *args],
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            env=env,
        )

    def test_refuses_without_argus_token(self):
        temp, _root, env = self.make_fixture(token=False)
        with temp:
            result = self.run_runtime(env)
        self.assertEqual(result.returncode, 2)
        self.assertIn("argus_cron_migration_ready=no", result.stdout)
        self.assertIn("dedicated Argus Telegram bot token/channel is not configured", result.stdout)

    def test_refuses_when_gateway_is_not_running(self):
        temp, _root, env = self.make_fixture(token=True, gateway="stopped")
        with temp:
            result = self.run_runtime(env)
        self.assertEqual(result.returncode, 2)
        self.assertIn("argus_gateway=stopped", result.stdout)
        self.assertIn("Argus gateway is not running", result.stdout)

    def test_dry_run_reports_actions_without_mutation(self):
        temp, root, env = self.make_fixture(token=True, gateway="running")
        with temp:
            result = self.run_runtime(env)
            self.assertEqual(result.returncode, 0, result.stdout)
            self.assertIn("argus_cron_migration_mode=dry-run", result.stdout)
            self.assertIn("would_copy_profile_scripts=yes", result.stdout)
            self.assertIn("would_create_cron=argus-competitive-research-daily", result.stdout)
            self.assertIn("would_create_cron=argus-competitive-research-weekly", result.stdout)
            self.assertFalse((root / "profiles" / "argus" / "scripts").exists())

    def test_execute_copies_wrappers_and_creates_argus_cron_jobs(self):
        temp, root, env = self.make_fixture(token=True, gateway="running")
        with temp:
            result = self.run_runtime(env, "--execute")
            self.assertEqual(result.returncode, 0, result.stdout)
            profile_scripts = root / "profiles" / "argus" / "scripts"
            self.assertTrue((profile_scripts / "competitive-research-daily.sh").exists())
            self.assertTrue((profile_scripts / "competitive-research-weekly.sh").exists())
            calls = (root / "hermes-calls.log").read_text()
            self.assertIn("-p argus cron create", calls)
            self.assertIn("argus-competitive-research-daily", calls)
            self.assertIn("argus-competitive-research-weekly", calls)
            self.assertIn("argus_cron_migration_status=created_or_present", result.stdout)


if __name__ == "__main__":
    unittest.main()
