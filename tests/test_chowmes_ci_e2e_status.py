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
    def make_fixture(
        self,
        *,
        token=False,
        gateway="stopped",
        argus_crons=False,
        valid_profile=True,
        valid_skill=True,
        synthesis_identity="argus",
        default_state="active",
    ):
        temp = tempfile.TemporaryDirectory()
        root = Path(temp.name)
        profile = root / "profiles" / "argus"
        profile.mkdir(parents=True)
        if valid_profile:
            (profile / "SOUL.md").write_text(
                "\n".join(
                    [
                        "# Argus Soul",
                        "You are Argus, Arijit's dedicated competitive intelligence agent.",
                        "You are male.",
                        "You are not Athena.",
                        "## Competitive Intelligence Doctrine",
                        "## Algolia CI Wedge",
                        "No evidence, no claim.",
                        "## Current Activation State",
                    ]
                )
                + "\n"
            )
        else:
            (profile / "SOUL.md").write_text("# Argus\n")
        (profile / ".env").write_text("TELEGRAM_BOT_TOKEN=test\n" if token else "GEMINI_API_KEY=test\n")

        skill = root / "skill"
        (skill / "scripts").mkdir(parents=True)
        (skill / "SKILL.md").write_text(
            (
                "\n".join(
                    [
                        "# Competitive Research",
                        "Operational owner: Argus",
                        "Athena supervises quality and escalation",
                        "ci_run_self_check.py",
                        "ci_run_review.py",
                        "## Argus CI Agent Mandate",
                        "Current live delivery mode is Argus-owned Telegram delivery through the `argus` Hermes profile",
                        "The old default daily/weekly CI cron jobs are paused, not deleted.",
                    ]
                )
                + "\n"
            )
            if valid_skill
            else "# Competitive Research\n"
        )
        if synthesis_identity == "argus":
            (skill / "scripts" / "ci_core.py").write_text(
                "prompt = 'You are Argus. Athena supervises quality and escalation.'\n"
            )
        elif synthesis_identity == "athena":
            (skill / "scripts" / "ci_core.py").write_text("prompt = 'You are Athena, writing CI.'\n")
        else:
            (skill / "scripts" / "ci_core.py").write_text("prompt = 'Generic CI writer.'\n")

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
                        "dedicated Argus Telegram gateway",
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
                    57d4ec29e7ad [{default_state}]
                    Name:      competitive-research-daily
                    Schedule:  0 9 * * *
                    Deliver:   telegram
                    Script:    competitive-research-daily.sh
                    Mode:      no-agent (script stdout delivered directly)
                    Last run:  2026-06-29T06:52:45-04:00  ok
                    d14daa705276 [{default_state}]
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
                "CI_SKILL_ROOT": str(skill),
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
        self.assertIn("default_daily_cron_state=active", result.stdout)
        self.assertIn("default_weekly_cron_state=active", result.stdout)
        self.assertIn("default_daily_delivery_identity_notice=present", result.stdout)
        self.assertIn("default_weekly_delivery_identity_notice=present", result.stdout)
        self.assertIn("argus_profile_contract_ready=yes", result.stdout)
        self.assertIn("ci_skill_argus_contract_ready=yes", result.stdout)
        self.assertIn("ci_synthesis_identity_ready=yes", result.stdout)
        self.assertIn("ci_target_argus_e2e_ready=no", result.stdout)
        self.assertIn("ci_target_argus_e2e_blocker=dedicated Argus Telegram bot token/channel is not configured", result.stdout)

    def test_blocks_target_when_argus_profile_contract_is_incomplete(self):
        temp, env = self.make_fixture(token=True, gateway="running", argus_crons=True, valid_profile=False)
        with temp:
            result = self.run_runtime(env)
        self.assertEqual(result.returncode, 0, result.stdout)
        self.assertIn("argus_profile_contract_ready=no", result.stdout)
        self.assertIn("ci_target_argus_e2e_ready=no", result.stdout)
        self.assertIn(
            "ci_target_argus_e2e_blocker=Argus SOUL.md is missing required CI identity/persona contract markers",
            result.stdout,
        )

    def test_blocks_target_when_skill_contract_is_incomplete(self):
        temp, env = self.make_fixture(token=True, gateway="running", argus_crons=True, valid_skill=False)
        with temp:
            result = self.run_runtime(env)
        self.assertEqual(result.returncode, 0, result.stdout)
        self.assertIn("ci_skill_argus_contract_ready=no", result.stdout)
        self.assertIn("ci_target_argus_e2e_ready=no", result.stdout)
        self.assertIn(
            "ci_target_argus_e2e_blocker=competitive-research skill is missing required Argus ownership/self-review contract markers",
            result.stdout,
        )

    def test_blocks_target_when_synthesis_prompt_still_names_athena(self):
        temp, env = self.make_fixture(token=True, gateway="running", argus_crons=True, synthesis_identity="athena")
        with temp:
            result = self.run_runtime(env)
        self.assertEqual(result.returncode, 0, result.stdout)
        self.assertIn("ci_synthesis_identity_ready=no", result.stdout)
        self.assertIn("ci_synthesis_identity_problem=missing Argus synthesis prompt", result.stdout)
        self.assertIn("ci_target_argus_e2e_ready=no", result.stdout)
        self.assertIn(
            "ci_target_argus_e2e_blocker=competitive-research synthesis prompt is not routed through Argus",
            result.stdout,
        )

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
        self.assertIn("argus_profile_contract_ready=yes", result.stdout)
        self.assertIn("ci_skill_argus_contract_ready=yes", result.stdout)
        self.assertIn("ci_synthesis_identity_ready=yes", result.stdout)
        self.assertIn("argus_telegram_token_key=present", result.stdout)
        self.assertIn("argus_gateway=running", result.stdout)
        self.assertIn("argus_daily_cron=present", result.stdout)
        self.assertIn("argus_weekly_cron=present", result.stdout)
        self.assertIn("ci_target_argus_e2e_ready=yes", result.stdout)
        self.assertIn("ci_final_argus_only_ready=no", result.stdout)
        self.assertIn("ci_final_argus_only_blocker=temporary default daily CI cron is still active", result.stdout)

    def test_reports_final_argus_only_ready_when_default_crons_are_paused(self):
        temp, env = self.make_fixture(token=True, gateway="running", argus_crons=True, default_state="paused")
        with temp:
            result = self.run_runtime(env)
        self.assertEqual(result.returncode, 0, result.stdout)
        self.assertIn("ci_target_argus_e2e_ready=yes", result.stdout)
        self.assertIn("default_daily_cron_state=paused", result.stdout)
        self.assertIn("default_weekly_cron_state=paused", result.stdout)
        self.assertIn("ci_final_argus_only_ready=yes", result.stdout)

    def test_require_final_argus_only_fails_until_default_crons_are_paused(self):
        temp, env = self.make_fixture(token=True, gateway="running", argus_crons=True, default_state="active")
        with temp:
            result = subprocess.run(
                [str(RUNTIME)],
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                env={**env, "REQUIRE_FINAL_ARGUS_ONLY": "1"},
            )
        self.assertEqual(result.returncode, 2, result.stdout)
        self.assertIn("ci_target_argus_e2e_ready=yes", result.stdout)
        self.assertIn("ci_final_argus_only_ready=no", result.stdout)


if __name__ == "__main__":
    unittest.main()
