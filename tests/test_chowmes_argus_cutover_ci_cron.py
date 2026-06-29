import os
import subprocess
import tempfile
import textwrap
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
RUNTIME = REPO_ROOT / "scripts" / "chowmes-argus-cutover-ci-cron-runtime"
WRAPPER = REPO_ROOT / "scripts" / "chowmes-argus-cutover-ci-cron"


class ArgusCutoverCiCronRuntimeTests(unittest.TestCase):
    def test_wrapper_requires_final_argus_only_after_execute(self):
        text = WRAPPER.read_text()

        self.assertIn("--require-final-argus-only", text)
        self.assertIn('if [ "$execute_arg" = "--execute" ]; then', text)

    def make_fixture(self, *, token=False, gateway="stopped", argus_crons=False):
        temp = tempfile.TemporaryDirectory()
        root = Path(temp.name)
        profile = root / "profiles" / "argus"
        profile.mkdir(parents=True)
        (profile / ".env").write_text("TELEGRAM_BOT_TOKEN=test\n" if token else "GEMINI_API_KEY=test\n")
        pauses = root / "pauses.log"
        hermes = root / "fake-hermes"
        hermes.write_text(
            textwrap.dedent(
                f"""\
                #!/bin/sh
                if [ "$1" = "-p" ] && [ "$2" = "argus" ] && [ "$3" = "gateway" ]; then
                  echo "Gateway: {gateway}"
                  exit 0
                fi
                if [ "$1" = "-p" ] && [ "$2" = "argus" ] && [ "$3" = "cron" ]; then
                  if [ "{argus_crons}" = "True" ]; then
                    cat <<'EOF'
                    aaaaaaaa1111 [active]
                      Name:      argus-competitive-research-daily
                      Schedule:  0 9 * * *

                    bbbbbbbb2222 [active]
                      Name:      argus-competitive-research-weekly
                      Schedule:  0 9 * * 0
                EOF
                  fi
                  exit 0
                fi
                if [ "$1" = "cron" ] && [ "$2" = "list" ]; then
                  cat <<'EOF'
                    57d4ec29e7ad [active]
                      Name:      competitive-research-daily
                      Schedule:  0 9 * * *

                    d14daa705276 [active]
                      Name:      competitive-research-weekly
                      Schedule:  0 9 * * 0
                EOF
                  exit 0
                fi
                if [ "$1" = "cron" ] && [ "$2" = "pause" ]; then
                  echo "$3" >> "{pauses}"
                  echo "paused $3"
                  exit 0
                fi
                exit 0
                """
            )
        )
        hermes.chmod(0o755)
        env = os.environ.copy()
        env.update(
            {
                "ARGUS_PROFILE_DIR": str(profile),
                "HERMES_BIN": str(hermes),
            }
        )
        return temp, env, pauses

    def run_runtime(self, env, *args):
        return subprocess.run(
            [str(RUNTIME), *args],
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            env=env,
        )

    def test_refuses_without_argus_token(self):
        temp, env, _pauses = self.make_fixture(token=False)
        with temp:
            result = self.run_runtime(env)
        self.assertEqual(result.returncode, 2)
        self.assertIn("argus_cutover_ready=no", result.stdout)
        self.assertIn("dedicated Argus Telegram bot token/channel is not configured", result.stdout)

    def test_dry_run_reports_default_jobs_to_pause_when_argus_ready(self):
        temp, env, pauses = self.make_fixture(token=True, gateway="running", argus_crons=True)
        with temp:
            result = self.run_runtime(env)
            pause_text = pauses.read_text() if pauses.exists() else ""
        self.assertEqual(result.returncode, 0, result.stdout)
        self.assertIn("argus_cutover_ready=yes", result.stdout)
        self.assertIn("argus_cutover_mode=dry-run", result.stdout)
        self.assertIn("would_pause_default_cron=57d4ec29e7ad", result.stdout)
        self.assertIn("would_pause_default_cron=d14daa705276", result.stdout)
        self.assertEqual(pause_text, "")

    def test_execute_pauses_default_jobs_when_argus_ready(self):
        temp, env, pauses = self.make_fixture(token=True, gateway="running", argus_crons=True)
        with temp:
            result = self.run_runtime(env, "--execute")
            pause_text = pauses.read_text()
        self.assertEqual(result.returncode, 0, result.stdout)
        self.assertIn("argus_cutover_mode=execute", result.stdout)
        self.assertIn("default_daily_pause=paused", result.stdout)
        self.assertIn("default_weekly_pause=paused", result.stdout)
        self.assertEqual(pause_text.splitlines(), ["57d4ec29e7ad", "d14daa705276"])


if __name__ == "__main__":
    unittest.main()
