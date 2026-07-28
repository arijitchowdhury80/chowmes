# Phase 7 Technical E2E Gate

Date: 2026-07-28
Status: technical gate passed for controlled pilot; human usefulness acceptance still required before Phase 8

## Scope

This artifact records the production Phase 7 technical validation pass for the controlled Algolia pilot. It does not release the pilot by itself. Phase 8 may start only after Arijit accepts that the live decision surface is useful enough for a controlled pilot.

## Deployed Package

- CI-OS commit: `2f7385f4afdcdd2af771e34d8e92bdc629a990fa`
- Branch: `codex/ci-os-phase0-baseline`
- Package path: `/opt/cios/app`
- Runtime owner: `cios`
- Stamp: `/opt/cios/app/.cios-package-commit`

## Live Run Evidence

- Daily wrapper completed in `903.8s`.
- Active sources: `42`
- Checked sources: `42`
- Fetched sources: `38`
- Failed active source fetches: `4`
- Facts: `361`
- Deltas: `361`
- Signals: `3`
- Quality: `passed`
- Dashboard published to `https://ci.chowmes.com/`

## Demand And Evidence Limits

The demand plane is intentionally limited for the controlled pilot:

- `argus-demand-readiness.status`: `processed_limited_plan_coverage`
- Demand signals: `101`
- Planned demand topic coverage: `1 / 12`
- Missing planned topics remain monitoring debt.

The data plane remains honest about confidence limits:

- `argus-data-plane-manifest.status`: `limited_by_evidence`
- `argus-operator-handoff.status`: `limited_by_evidence`
- Product Muscle limiting items: `39`

## Gate Results

Verified artifacts:

- Package contract: passed.
- Public artifact redaction: `redacted`.
- Public artifact safety scan: `passed`.
- Live operational safety: `passed`.
- Live dashboard click validation: passed across desktop, tablet, and mobile viewports.
- Aggregate E2E launch readiness: `pass`.

Controlled-pilot source-failure policy:

- Absolute failed-source budget: `1`
- Controlled-pilot ratio budget: `0.10`
- Actual failed-source ratio: `4 / 42 = 0.0952`
- Result: passed by explicit ratio policy, with the failed sources still visible in the launch artifact.

## Validation Commands

The deployed package gate was run from `/opt/cios/app`:

```bash
.venv/bin/python scripts/verify_hermes_package_contract.py --app-dir /opt/cios/app
.venv/bin/python scripts/check_live_operational_safety.py \
  --expected-package-commit 2f7385f4afdcdd2af771e34d8e92bdc629a990fa \
  --output /opt/cios/app/out/live-operational-safety.json
.venv/bin/python scripts/check_e2e_launch_readiness.py \
  --public-status /opt/cios/public/data/argus-latest-run-status.json \
  --click-validation-log-text 'PASS dashboard_click_validation' \
  --package-contract-log /opt/cios/app/out/hermes-package-contract.log \
  --public-redaction /opt/cios/app/out/public-artifact-redaction.json \
  --public-safety-scan /opt/cios/app/out/public-artifact-safety-scan.json \
  --operational-safety /opt/cios/app/out/live-operational-safety.json \
  --min-active-sources 1 \
  --max-failed-sources 1 \
  --max-failed-source-ratio 0.10 \
  --output /opt/cios/app/out/cios-e2e-launch-readiness.json
```

Local verification for the source-failure policy:

- RED confirmed before implementation: `2 failed, 8 passed` in `tests/scripts/test_check_e2e_launch_readiness.py`.
- Focused green suite: `10 passed`.
- Affected package-contract suite: `79 passed`.
- Package contract: passed.
- `py_compile` and `git diff --check`: passed.

Broader `tests/scripts` status:

- `409 passed`, `1 failed`.
- The failing test is `tests/scripts/test_check_argus_demand_source_gate.py::test_strict_gate_passes_when_dashboard_has_processed_demand`.
- It reproduces independently and is not caused by the Phase 7 launch-readiness policy diff.

## Exit Judgment

Phase 7 technical validation is passed for the controlled pilot basis.

Phase 7 is not fully closed until Arijit accepts the live decision surface as useful enough to advance to Phase 8.
