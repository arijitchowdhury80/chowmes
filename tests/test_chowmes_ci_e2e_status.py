import json
import os
import subprocess
import tempfile
import textwrap
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
RUNTIME = REPO_ROOT / "scripts" / "chowmes-ci-e2e-status-runtime"


class CiE2eStatusRuntimeTests(unittest.TestCase):
    def make_fixture(self, *, token=False, gateway="stopped", argus_crons=False):
        temp = tempfile.TemporaryDirectory()
        root = Path(temp.name)
        profile = root / "profiles" / "argus"
        profile.mkdir(parents=True)
        (profile / "SOUL.md").write_text("# Argus\n")
        (profile / ".env").write_text("TELEGRAM_BOT_TOKEN=test\n" if token else "GEMINI_API_KEY=test\n")

        scripts = root / "scripts"
        scripts.mkdir()
        for cadence in ["daily", "weekly"]:
            (scripts / f"competitive-research-{cadence}.sh").write_text(
                "\n".join(
                    [
                        "ci-provider-preflight.py",
                        "ci_run_self_check.py",
                        "ci_run_review.py",
                        "publish-dashboard.py",
                    ]
                )
                + "\n"
            )

        artifact = root / "artifacts" / "run-audits"
        artifact.mkdir(parents=True)
        for cadence in ["daily", "weekly"]:
            (artifact / f"2026-06-29-{cadence}.json").write_text(
                json.dumps({"status": "pass", "date": "2026-06-29", "cadence": cadence})
            )

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
                    Name:      argus-competitive-research-daily
                    Schedule:  0 9 * * *
                    Deliver:   telegram
                    Name:      argus-competitive-research-weekly
                    Schedule:  0 9 * * 0
                    Deliver:   telegram
                EOF
                  fi
                  exit 0
                fi
                if [ "$1" = "cron" ]; then
                  cat <<'EOF'
                    Name:      competitive-research-daily
                    Schedule:  0 9 * * *
                    Deliver:   telegram
                    Script:    competitive-research-daily.sh
                    Mode:      no-agent (script stdout delivered directly)
                    Last run:  2026-06-29T06:52:45-04:00  ok
                    Name:      competitive-research-weekly
                    Schedule:  0 9 * * 0
                    Deliver:   telegram
                    Script:    competitive-research-weekly.sh
                    Mode:      no-agent (script stdout delivered directly)
                    Last run:  2026-06-29T06:53:16-04:00  ok
                EOF
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
                "GLOBAL_SCRIPT_DIR": str(scripts),
                "CI_ARTIFACT_ROOT": str(root / "artifacts"),
                "HERMES_BIN": str(hermes),
                "PYTHON_BIN": "python3",
            }
        )
        return temp, env

    def run_runtime(self, env, *args):
        return subprocess.run(
            [str(RUNTIME), *args],
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            env=env,
        )

    def test_reports_current_healthy_but_target_blocked_without_token(self):
        temp, env = self.make_fixture(token=False)
        with temp:
            result = self.run_runtime(env)
        self.assertEqual(result.returncode, 0, result.stdout)
        self.assertIn("ci_current_pipeline_mechanically_healthy=yes", result.stdout)
        self.assertIn("ci_target_argus_e2e_ready=no", result.stdout)
        self.assertIn("ci_target_argus_e2e_blocker=dedicated Argus Telegram bot token/channel is not configured", result.stdout)

    def test_require_argus_e2e_fails_when_target_path_not_ready(self):
        temp, env = self.make_fixture(token=False)
        with temp:
            result = self.run_runtime(env)
            required = subprocess.run(
                [str(RUNTIME)],
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                env={**env, "REQUIRE_ARGUS_E2E": "1"},
            )
        self.assertEqual(result.returncode, 0, result.stdout)
        self.assertEqual(required.returncode, 2, required.stdout)

    def test_reports_target_ready_when_token_gateway_and_argus_crons_exist(self):
        temp, env = self.make_fixture(token=True, gateway="running", argus_crons=True)
        with temp:
            result = self.run_runtime(env)
        self.assertEqual(result.returncode, 0, result.stdout)
        self.assertIn("ci_current_pipeline_mechanically_healthy=yes", result.stdout)
        self.assertIn("argus_telegram_token_key=present", result.stdout)
        self.assertIn("argus_gateway=running", result.stdout)
        self.assertIn("argus_daily_cron=present", result.stdout)
        self.assertIn("argus_weekly_cron=present", result.stdout)
        self.assertIn("ci_target_argus_e2e_ready=yes", result.stdout)


if __name__ == "__main__":
    unittest.main()
