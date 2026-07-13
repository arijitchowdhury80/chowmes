# Hermes Eval Gate Automation Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build the executable Hermes Eval Gate so external resources cannot move to `pilot`, `live-candidate`, or `live` without required security, skill behavior, memory, voice, runtime, rollback, and verification evidence.

**Architecture:** Keep `skill-verifier` focused as the security scanner of record. Add a small repo-local gate checker that reads `hermes-eval-gate-schema.json`, validates resource evidence manifests, writes deterministic reports, and blocks promotion when required gates are missing or failing. Do not touch live Hermes, VPS config, Telegram, or profile files in this implementation phase.

**Tech Stack:** Python standard library only, `unittest`, `subprocess`, JSON files, Markdown docs, existing `hermes-resource-scan`, existing `hermes-inventory-scan`, existing external `skill-verifier` reports.

## Global Constraints

- No live Hermes runtime changes in this phase.
- Do not mutate `/Users/arijitchowdhury/.agents/skills/skill-verifier`.
- Do not install external resources.
- Do not print secrets from `.env`, local reports, scan output, or vault files.
- Use TDD: write a failing test, verify red, implement minimally, verify green.
- Keep changes scoped under `hermes-core/resource-intake` except vault release records.
- A repeated identical failure gets a maximum of 3 patch attempts, then stop and escalate.

---

## Execution Goal

Create an executable, test-backed promotion gate for Hermes external-resource
adoption. The gate must answer four questions for any resource:

1. Which gates are required for this resource?
2. Which evidence files prove those gates passed?
3. Is promotion to the requested state allowed?
4. If not allowed, what exact missing or failed evidence blocks promotion?

The target command for the first executable slice is:

```sh
hermes-core/resource-intake/scripts/hermes-eval-gate-check \
  --resource "Sentry Skills" \
  --target-state pilot \
  --evidence-file .artifacts/hermes-resource-intake/examples/sentry-skills-evidence.json \
  --output-dir .artifacts/hermes-resource-intake/eval-gates
```

Expected successful output:

```text
resource=Sentry Skills
target_state=pilot
required_gates=security,skill_behavior,runtime
verdict=pass
report=...
```

Expected blocked output:

```text
resource=Sentry Skills
target_state=pilot
required_gates=security,skill_behavior,runtime
verdict=block
missing_gates=runtime
report=...
```

## Execution Loop

Every task executes through this loop:

1. Write or extend the focused failing test.
2. Run `python3 -m pytest hermes-core/resource-intake/tests/test_hermes_resource_intake.py -q`.
3. Confirm failure is caused by the missing planned behavior.
4. Implement the smallest change that can pass that test.
5. Run the same test command again.
6. Run the full verification set listed in the task.
7. Inspect `git diff --check -- hermes-core/resource-intake`.
8. Commit only the files owned by that task.

No task may claim completion unless its test first failed and then passed.

## Self-Patching Loop

When a task fails verification:

1. Classify the failure as one of:
   - schema mismatch
   - missing evidence
   - command-line parsing failure
   - report content failure
   - promotion-rule failure
   - documentation drift
   - unrelated environment failure
2. Patch the smallest responsible file.
3. Re-run the exact failing command.
4. If the failure changes, restart the loop from classification.
5. If the same failure repeats, attempt a maximum of 3 patch attempts.
6. After the third identical failure, stop and escalate with:
   - command run
   - exit code
   - failing output
   - files changed
   - hypothesis
   - safest rollback

The loop is allowed to self-patch tests only when the red failure proves the
test asserted the wrong contract. It is not allowed to weaken tests to pass an
implementation that violates the gate docs.

## Measurement Matrix

| Surface | Measurement | Passing Threshold | Blocking Failure |
|---|---|---|---|
| Schema validity | `python3 -m json.tool hermes-core/resource-intake/docs/hermes-eval-gate-schema.json` | exit 0 | invalid JSON |
| Gate coverage | unit tests over all schema resources | every non-rejected resource has required gates | missing gate list |
| Evidence validation | unit tests with pass and block fixtures | exact verdict and missing gate list | false pass or false block |
| CLI behavior | subprocess tests for `hermes-eval-gate-check` | exit 0 on pass, exit 2 on block | wrong exit code |
| Secret hygiene | tests using fake secret values | fake secret absent from stdout and report | secret appears |
| Promotion rule | tests for `study`, `scan`, `pilot`, `live-candidate`, `live` | No resource moves to `pilot`, `live-candidate`, or `live` without evidence | promotion allowed without required gate |
| Report determinism | JSON report snapshot shape | stable keys and sorted gate names | nondeterministic report shape |
| Docs alignment | tests for docs and schema terms | docs mention the same gate IDs as schema | drift between docs and schema |

## Definition Of Done

The Hermes Eval Gate automation phase is done only when all conditions below
are true:

- `hermes-eval-gate-check` exists and is tested.
- Gate schema has required gates for every external resource.
- Evidence manifest format is documented and tested.
- Passing fixture produces `verdict=pass`.
- Missing-evidence fixture produces `verdict=block`.
- Promotion to `pilot`, `live-candidate`, or `live` is blocked without all
  required gate evidence.
- Reports include resource, target state, required gates, gate verdicts, missing
  gates, approval owner, rollback path, and verification commands.
- Fake secret values do not appear in stdout or report files.
- `python3 -m py_compile hermes-core/resource-intake/scripts/hermes-resource-scan hermes-core/resource-intake/scripts/hermes-inventory-scan hermes-core/resource-intake/scripts/hermes-eval-gate-check hermes-core/resource-intake/tests/test_hermes_resource_intake.py` exits 0.
- `python3 -m pytest hermes-core/resource-intake/tests/test_hermes_resource_intake.py -q` exits 0.
- `python3 -m json.tool hermes-core/resource-intake/docs/hermes-eval-gate-schema.json` exits 0.
- `git diff --check -- hermes-core/resource-intake` exits 0.
- Vault release record is written after verification.
- Branch is committed and pushed with only intended files staged.

---

### Task 1: Gate Plan Guardrails

**Files:**
- Modify: `hermes-core/resource-intake/tests/test_hermes_resource_intake.py`
- Modify: `hermes-core/resource-intake/docs/hermes-eval-gate-execution-plan.md`

**Interfaces:**
- Consumes: existing gate docs and schema.
- Produces: test-enforced execution-plan requirements.

- [ ] **Step 1: Write the failing test**

Add a test named `test_eval_gate_execution_plan_defines_goal_loops_measurements_and_done` that reads `docs/hermes-eval-gate-execution-plan.md` and asserts:

```python
plan = EXECUTION_PLAN.read_text()
self.assertTrue(plan.startswith("# Hermes Eval Gate Automation Implementation Plan"))
self.assertIn("## Execution Goal", plan)
self.assertIn("## Execution Loop", plan)
self.assertIn("## Self-Patching Loop", plan)
self.assertIn("## Measurement Matrix", plan)
self.assertIn("## Definition Of Done", plan)
self.assertIn("maximum of 3 patch attempts", plan)
self.assertIn("stop and escalate", plan)
```

- [ ] **Step 2: Run the test to verify red**

Run:

```sh
python3 -m pytest hermes-core/resource-intake/tests/test_hermes_resource_intake.py -q
```

Expected: failure with `FileNotFoundError` for
`hermes-eval-gate-execution-plan.md`.

- [ ] **Step 3: Write the minimal plan**

Create `hermes-eval-gate-execution-plan.md` with the execution goal, loop,
self-patching loop, measurement matrix, definition of done, and tasks in this
file.

- [ ] **Step 4: Run the test to verify green**

Run:

```sh
python3 -m pytest hermes-core/resource-intake/tests/test_hermes_resource_intake.py -q
```

Expected: all tests pass.

### Task 2: Gate Evidence Model

**Files:**
- Modify: `hermes-core/resource-intake/tests/test_hermes_resource_intake.py`
- Create: `hermes-core/resource-intake/docs/hermes-eval-evidence-format.md`
- Modify: `hermes-core/resource-intake/docs/hermes-eval-gate-schema.json`

**Interfaces:**
- Consumes: gate IDs from `hermes-eval-gate-schema.json`.
- Produces: evidence manifest JSON contract used by the CLI.

- [ ] **Step 1: Write the failing evidence-format test**

Add a test that creates this evidence fixture:

```python
evidence = {
    "resource": "Sentry Skills",
    "target_state": "pilot",
    "approval_owner": "Arijit",
    "rollback": "keep study-only",
    "gates": {
        "security": {
            "status": "pass",
            "evidence": ["security-report.md"],
            "verification_commands": ["skill-verifier local-path"]
        }
    }
}
```

The test must assert the future validator blocks it because
`skill_behavior` and `runtime` are missing for `Sentry Skills`.

- [ ] **Step 2: Run the test to verify red**

Run:

```sh
python3 -m pytest hermes-core/resource-intake/tests/test_hermes_resource_intake.py -q
```

Expected: failure because the validator and evidence format do not exist yet.

- [ ] **Step 3: Document the evidence format**

Create `hermes-eval-evidence-format.md` with required fields:

```json
{
  "resource": "Sentry Skills",
  "target_state": "pilot",
  "approval_owner": "Arijit",
  "rollback": "keep study-only",
  "gates": {
    "security": {
      "status": "pass",
      "evidence": ["path/to/report.md"],
      "verification_commands": ["command that produced evidence"]
    }
  }
}
```

- [ ] **Step 4: Run the test to verify green after Task 3 implements the validator**

Run:

```sh
python3 -m pytest hermes-core/resource-intake/tests/test_hermes_resource_intake.py -q
```

Expected: all tests pass once the validator exists.

### Task 3: Gate Check CLI

**Files:**
- Create: `hermes-core/resource-intake/scripts/hermes-eval-gate-check`
- Modify: `hermes-core/resource-intake/tests/test_hermes_resource_intake.py`
- Modify: `hermes-core/resource-intake/README.md`

**Interfaces:**
- Consumes: `load_schema(schema_path: Path) -> dict`.
- Consumes: `validate_evidence(schema: dict, evidence: dict) -> dict`.
- Produces: CLI report JSON with keys `resource`, `target_state`, `verdict`, `required_gates`, `missing_gates`, `failed_gates`, `report_path`.

- [ ] **Step 1: Write the failing CLI pass test**

Create a temp evidence file for `Sentry Skills` with `security`,
`skill_behavior`, and `runtime` all set to `pass`. Run:

```python
result = subprocess.run(
    [
        str(EVAL_GATE_CHECK),
        "--resource", "Sentry Skills",
        "--target-state", "pilot",
        "--evidence-file", str(evidence_file),
        "--output-dir", str(reports),
    ],
    text=True,
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT,
)
self.assertEqual(result.returncode, 0, result.stdout)
self.assertIn("verdict=pass", result.stdout)
```

- [ ] **Step 2: Write the failing CLI block test**

Use the same resource but omit `runtime`. Expected:

```python
self.assertEqual(result.returncode, 2, result.stdout)
self.assertIn("verdict=block", result.stdout)
self.assertIn("missing_gates=runtime", result.stdout)
```

- [ ] **Step 3: Implement minimal CLI**

Implement Python standard-library parsing:

```python
def load_schema(path):
    return json.loads(path.read_text())

def required_gates_for(schema, resource):
    for item in schema["resources"]:
        if item["name"] == resource:
            return item["required_gates"]
    raise ValueError(f"unknown resource: {resource}")
```

- [ ] **Step 4: Run verification**

Run:

```sh
python3 -m py_compile hermes-core/resource-intake/scripts/hermes-eval-gate-check
python3 -m pytest hermes-core/resource-intake/tests/test_hermes_resource_intake.py -q
```

Expected: py-compile exits 0 and tests pass.

### Task 4: Resource Promotion Enforcement

**Files:**
- Modify: `hermes-core/resource-intake/scripts/hermes-eval-gate-check`
- Modify: `hermes-core/resource-intake/tests/test_hermes_resource_intake.py`
- Modify: `hermes-core/resource-intake/docs/hermes-eval-evidence-format.md`

**Interfaces:**
- Consumes: `target_state`.
- Produces: `promotion_allowed: bool`.

- [ ] **Step 1: Write failing promotion tests**

Assert:

```python
study_without_evidence_returns_pass_or_warn()
scan_without_all_evidence_returns_pass_or_warn()
pilot_without_all_evidence_returns_block()
live_candidate_without_all_evidence_returns_block()
live_without_all_evidence_returns_block()
```

- [ ] **Step 2: Run red**

Run:

```sh
python3 -m pytest hermes-core/resource-intake/tests/test_hermes_resource_intake.py -q
```

Expected: promotion-state tests fail because the CLI does not yet enforce
state-specific blocking.

- [ ] **Step 3: Implement state rules**

Rules:

```python
STRICT_STATES = {"pilot", "live-candidate", "live"}
SOFT_STATES = {"study", "scan"}
```

If `target_state` is strict and any required gate is missing or failed, exit 2.
If `target_state` is soft, write a report with warnings and exit 0.

- [ ] **Step 4: Run green**

Run:

```sh
python3 -m pytest hermes-core/resource-intake/tests/test_hermes_resource_intake.py -q
```

Expected: all tests pass.

### Task 5: Report Aggregation

**Files:**
- Modify: `hermes-core/resource-intake/scripts/hermes-eval-gate-check`
- Modify: `hermes-core/resource-intake/tests/test_hermes_resource_intake.py`
- Modify: `hermes-core/resource-intake/README.md`

**Interfaces:**
- Consumes: evidence manifest.
- Produces: deterministic report file at `<output-dir>/<slug>/hermes-eval-gate-report.json`.

- [ ] **Step 1: Write failing report-shape test**

Assert report JSON includes:

```python
[
    "resource",
    "target_state",
    "verdict",
    "required_gates",
    "missing_gates",
    "failed_gates",
    "approval_owner",
    "rollback",
    "verification_commands",
]
```

- [ ] **Step 2: Run red**

Run:

```sh
python3 -m pytest hermes-core/resource-intake/tests/test_hermes_resource_intake.py -q
```

Expected: report-shape test fails until report aggregation is implemented.

- [ ] **Step 3: Implement deterministic report writing**

Use:

```python
report_path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
```

- [ ] **Step 4: Run green and secret hygiene check**

Run:

```sh
python3 -m pytest hermes-core/resource-intake/tests/test_hermes_resource_intake.py -q
```

Expected: all tests pass and fake secret values are absent from stdout and
report files.

### Task 6: Vault And Release Record

**Files:**
- Create: `hermes-core/resource-intake/docs/hermes-eval-gate-release-record-template.md`
- Modify: `hermes-core/resource-intake/README.md`
- Copy after verification: `/Users/arijitchowdhury/Dropbox/AI-Development/Personal/Obsidian-Vault/MyOS/Projects/Chowmes/logs/YYYY-MM-DD-hermes-eval-gate-automation.md`

**Interfaces:**
- Consumes: final command outputs.
- Produces: vault release record.

- [ ] **Step 1: Write failing release-record test**

Assert the release template includes:

```python
self.assertIn("Verification Output", template)
self.assertIn("Definition Of Done", template)
self.assertIn("Rollback", template)
self.assertIn("Known Gaps", template)
```

- [ ] **Step 2: Run red**

Run:

```sh
python3 -m pytest hermes-core/resource-intake/tests/test_hermes_resource_intake.py -q
```

Expected: missing release template failure.

- [ ] **Step 3: Add the release template**

Create the template with exact sections:

```markdown
# Hermes Eval Gate Automation Release Record

## Verification Output
## Definition Of Done
## Rollback
## Known Gaps
```

- [ ] **Step 4: Run final verification**

Run:

```sh
python3 -m py_compile hermes-core/resource-intake/scripts/hermes-resource-scan hermes-core/resource-intake/scripts/hermes-inventory-scan hermes-core/resource-intake/scripts/hermes-eval-gate-check hermes-core/resource-intake/tests/test_hermes_resource_intake.py
python3 -m pytest hermes-core/resource-intake/tests/test_hermes_resource_intake.py -q
python3 -m json.tool hermes-core/resource-intake/docs/hermes-eval-gate-schema.json
git diff --check -- hermes-core/resource-intake
```

Expected:

- py-compile exits 0.
- pytest exits 0.
- json.tool exits 0.
- diff check exits 0.

## Final Handoff

After all tasks pass:

1. Write the vault release record.
2. Stage only `hermes-core/resource-intake` and the intended vault artifact if
   it is repo-tracked.
3. Commit with `feat: add Hermes eval gate checker`.
4. Push `codex/hermes-resource-intake`.
5. Report exact verification outputs and remaining gaps.
