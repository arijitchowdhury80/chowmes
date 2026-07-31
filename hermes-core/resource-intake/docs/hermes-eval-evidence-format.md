# Hermes Eval Evidence Format

Date: 2026-07-13
Status: Phase 2 evidence contract

This file defines the evidence manifest consumed by the Hermes Eval Gate. It is
the bridge between scan outputs, human review, behavior evals, memory checks,
voice checks, runtime checks, and resource promotion.

The manifest does not execute any scanner. It records the evidence that proves
each required gate passed.

## Required Fields

| Field | Type | Required | Meaning |
|---|---|---|---|
| `resource` | string | yes | Resource name exactly as listed in `hermes-eval-gate-schema.json`. |
| `target_state` | string | yes | Requested ledger state, such as `study`, `scan`, `pilot`, `live-candidate`, or `live`. |
| `approval_owner` | string | yes | Human owner who approved the evidence package or promotion request. |
| `rollback` | string | yes | Concrete rollback action or reason the resource remains study-only. |
| `gates` | object | yes | Map of gate ID to gate evidence object. |
| `status` | string | yes per gate | Gate verdict. Use `pass`, `fail`, `warn`, or `missing`. |
| `evidence` | array of strings | yes per gate | Paths to reports, transcripts, benchmark outputs, or review notes. |
| `verification_commands` | array of strings | yes per gate | Commands that produced or verified the evidence. |

## Example: Partial Sentry Skills Evidence

This manifest must block promotion to `pilot` because `Sentry Skills` requires
`security`, `skill_behavior`, and `runtime`, but only `security` is present.

```json
{
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

Expected validation result:

```json
{
  "resource": "Sentry Skills",
  "target_state": "pilot",
  "required_gates": ["security", "skill_behavior", "runtime"],
  "verdict": "block",
  "missing_gates": ["skill_behavior", "runtime"],
  "failed_gates": []
}
```

## Example: Complete Sentry Skills Evidence

This manifest can pass evidence validation for `pilot` because every required
gate exists and has `status` set to `pass`.

```json
{
  "resource": "Sentry Skills",
  "target_state": "pilot",
  "approval_owner": "Arijit",
  "rollback": "remove candidate files and keep source study-only",
  "gates": {
    "security": {
      "status": "pass",
      "evidence": ["security-report.md"],
      "verification_commands": ["skill-verifier local-path"]
    },
    "skill_behavior": {
      "status": "pass",
      "evidence": ["behavior-benchmark.json", "trigger-evals.json"],
      "verification_commands": ["python3 -m pytest hermes-core/resource-intake/tests/test_hermes_resource_intake.py -q"]
    },
    "runtime": {
      "status": "pass",
      "evidence": ["runtime-smoke.md"],
      "verification_commands": ["scripts/chowmes-health-check --repair --send-test"]
    }
  }
}
```

## Validation Rules

- Resource names must match the schema exactly.
- Required gates come from `hermes-eval-gate-schema.json`.
- Missing required gates block strict promotion states.
- Any required gate with `status` other than `pass` is a failed gate.
- Evidence paths and verification commands must be recorded before promotion.
- Secret values must never be copied into evidence paths, command output, or
  report content.
