import json
import os
import subprocess
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
RESOURCE_SCAN = REPO_ROOT / "scripts" / "hermes-resource-scan"
INVENTORY_SCAN = REPO_ROOT / "scripts" / "hermes-inventory-scan"
LEDGER = REPO_ROOT / "docs" / "hermes-external-resource-ledger.md"
CHECKLIST = REPO_ROOT / "docs" / "hermes-skill-intake-checklist.md"
THREAT_MODEL = REPO_ROOT / "docs" / "hermes-resource-threat-model.md"
EVAL_GATE = REPO_ROOT / "docs" / "hermes-eval-gate.md"
SECURITY_GATE = REPO_ROOT / "docs" / "hermes-security-gate.md"
SKILL_BEHAVIOR_GATE = REPO_ROOT / "docs" / "hermes-skill-behavior-gate.md"
MEMORY_GATE = REPO_ROOT / "docs" / "hermes-memory-gate.md"
VOICE_GATE = REPO_ROOT / "docs" / "hermes-voice-gate.md"
RUNTIME_GATE = REPO_ROOT / "docs" / "hermes-runtime-gate.md"
GATE_SCHEMA = REPO_ROOT / "docs" / "hermes-eval-gate-schema.json"


class HermesResourceIntakeTests(unittest.TestCase):
    def test_resource_scan_refuses_broad_personal_directory_by_default(self):
        with tempfile.TemporaryDirectory() as tmp:
            result = subprocess.run(
                [str(RESOURCE_SCAN), str(Path.home()), "--output-dir", tmp, "--no-medusa"],
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
            )

        self.assertEqual(result.returncode, 2, result.stdout)
        self.assertIn("refusing_broad_scan=yes", result.stdout)
        self.assertIn("--allow-broad-scan", result.stdout)

    def test_resource_scan_writes_private_report_and_flags_agent_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            candidate = root / "candidate"
            candidate.mkdir()
            (candidate / "AGENTS.md").write_text("instructions\n")
            (candidate / "SKILL.md").write_text("skill\n")
            (candidate / "mcp.json").write_text('{"servers": {}}\n')
            (candidate / "install.sh").write_text("echo install\n")
            (candidate / ".env").write_text("TOKEN=SECRET_VALUE_SHOULD_NOT_PRINT\n")
            reports = root / "reports"

            result = subprocess.run(
                [str(RESOURCE_SCAN), str(candidate), "--output-dir", str(reports), "--no-medusa"],
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
            )

            self.assertEqual(result.returncode, 0, result.stdout)
            self.assertNotIn("SECRET_VALUE_SHOULD_NOT_PRINT", result.stdout)
            report_files = list(reports.glob("*/hermes-resource-scan.json"))
            self.assertEqual(len(report_files), 1)
            report = json.loads(report_files[0].read_text())
            self.assertEqual(report["target_type"], "local_path")
            self.assertEqual(report["scanner"]["medusa_status"], "skipped")
            self.assertIn("agent_instruction:AGENTS.md", report["risk_flags"])
            self.assertIn("skill_file:SKILL.md", report["risk_flags"])
            self.assertIn("mcp_config:mcp.json", report["risk_flags"])
            self.assertIn("install_script:install.sh", report["risk_flags"])
            self.assertNotIn("SECRET_VALUE_SHOULD_NOT_PRINT", report_files[0].read_text())

    def test_inventory_scan_writes_report_without_requiring_bumblebee(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            candidate = root / "candidate"
            candidate.mkdir()
            (candidate / "package.json").write_text('{"dependencies": {"x": "1.0.0"}}\n')
            reports = root / "reports"

            result = subprocess.run(
                [str(INVENTORY_SCAN), str(candidate), "--output-dir", str(reports), "--no-bumblebee"],
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
            )

            self.assertEqual(result.returncode, 0, result.stdout)
            report_files = list(reports.glob("*/hermes-inventory-scan.json"))
            self.assertEqual(len(report_files), 1)
            report = json.loads(report_files[0].read_text())
            self.assertEqual(report["target_type"], "local_path")
            self.assertEqual(report["scanner"]["bumblebee_status"], "skipped")
            self.assertIn("package_manifest:package.json", report["inventory_hints"])

    def test_inventory_scan_runs_bumblebee_with_project_profile_and_root(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            candidate = root / "candidate"
            candidate.mkdir()
            fake_bin = root / "bin"
            fake_bin.mkdir()
            calls = root / "calls.txt"
            bumblebee = fake_bin / "bumblebee"
            bumblebee.write_text(
                "#!/bin/sh\n"
                f"printf '%s\\n' \"$*\" > {calls}\n"
                "printf '%s\\n' '{\"record_type\":\"scan_summary\"}'\n"
            )
            bumblebee.chmod(0o755)
            reports = root / "reports"
            env = os.environ.copy()
            env["PATH"] = f"{fake_bin}:{env['PATH']}"

            result = subprocess.run(
                [
                    str(INVENTORY_SCAN),
                    str(candidate),
                    "--output-dir",
                    str(reports),
                    "--run-bumblebee",
                ],
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                env=env,
            )

            self.assertEqual(result.returncode, 0, result.stdout)
            self.assertIn(f"scan --profile project --root {candidate}", calls.read_text())
            report = json.loads(next(reports.glob("*/hermes-inventory-scan.json")).read_text())
            self.assertEqual(report["scanner"]["bumblebee_status"], "ran")

    def test_first_layer_documents_exist_and_define_gates(self):
        ledger = LEDGER.read_text()
        checklist = CHECKLIST.read_text()
        threat_model = THREAT_MODEL.read_text()

        for source in [
            "hermes-agent.nousresearch.com/docs/user-guide/features/honcho",
            "hermes-agent.nousresearch.com/docs/user-guide/features/skills",
            "github.com/Pantheon-Security/medusa",
            "github.com/getsentry/skills",
            "github.com/NousResearch/hermes-agent-self-evolution",
            "github.com/perplexityai/bumblebee",
            "github.com/garrytan/gbrain",
            "github.com/RyanCodrai/turbovec",
            "github.com/nexu-io/open-design",
        ]:
            self.assertIn(source, ledger)

        self.assertIn("Approval Gate", checklist)
        self.assertIn("Rollback", checklist)
        self.assertIn("Trust Boundary", threat_model)
        self.assertIn("No Live Runtime Change", threat_model)

    def test_eval_gate_docs_define_all_layers_and_reuse_existing_skill_verifier(self):
        docs = {
            "security": SECURITY_GATE,
            "skill_behavior": SKILL_BEHAVIOR_GATE,
            "memory": MEMORY_GATE,
            "voice": VOICE_GATE,
            "runtime": RUNTIME_GATE,
        }
        overview = EVAL_GATE.read_text()

        for gate_id, path in docs.items():
            self.assertTrue(path.exists(), f"{path} is missing")
            content = path.read_text()
            self.assertIn(f"Gate ID: `{gate_id}`", content)
            self.assertIn("Required Evidence", content)
            self.assertIn("Pass Criteria", content)
            self.assertIn("Rollback", content)
            self.assertIn(str(path.name), overview)

        security = SECURITY_GATE.read_text()
        self.assertIn("/Users/arijitchowdhury/.agents/skills/skill-verifier", security)
        self.assertIn("Do not replace `skill-verifier`", security)
        self.assertIn("Medusa", security)
        self.assertIn("Bumblebee", security)

    def test_eval_gate_schema_requires_gate_evidence_and_resource_coverage(self):
        schema = json.loads(GATE_SCHEMA.read_text())

        self.assertEqual(schema["schema_version"], 1)
        self.assertEqual(
            [gate["id"] for gate in schema["gates"]],
            ["security", "skill_behavior", "memory", "voice", "runtime"],
        )
        for gate in schema["gates"]:
            self.assertIn("required_evidence", gate)
            self.assertIn("pass_criteria", gate)
            self.assertIn("rollback", gate)
            self.assertGreaterEqual(len(gate["required_evidence"]), 2)

        resources = {resource["name"]: resource for resource in schema["resources"]}
        self.assertEqual(resources["Honcho Memory"]["required_gates"], ["security", "memory", "voice", "runtime"])
        self.assertEqual(resources["Sentry Skills"]["required_gates"], ["security", "skill_behavior", "runtime"])
        self.assertEqual(resources["Hermes Agent Self-Evolution"]["required_gates"], ["security", "skill_behavior", "voice", "runtime"])
        self.assertEqual(resources["GBrain"]["required_gates"], ["security", "memory", "runtime"])


if __name__ == "__main__":
    unittest.main()
