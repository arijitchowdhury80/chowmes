# Phase 7 Live Operational Safety Slice

Date: 2026-07-28

## Scope

Phase 7 is active. This artifact records a validation-slice pass, not a Phase 7 exit-gate pass.

The slice hardened CI-OS launch readiness so the final command now requires:

- deployed Hermes package contract evidence
- live dashboard click validation evidence
- public artifact redaction evidence
- public artifact safety-scan evidence
- live operational safety evidence for package commit, public-store release shape, hidden staging leaks, root-owned artifacts, and stale CI-OS run processes

## CI-OS Package Commits

- `13332692b673850f8cc85272748bf19457a9031a`: added `scripts/check_live_operational_safety.py` and launch-readiness wiring.
- `42345adb240086ee6aa6d185337428271aa3ceda`: fixed product-reality readiness to accept count-backed product evidence when the plane does not block action.

Both commits were pushed to `origin/codex/ci-os-phase0-baseline`.

The VPS package at `/opt/cios/app/.cios-package-commit` was stamped to:

```text
42345adb240086ee6aa6d185337428271aa3ceda
```

## Verified Local Evidence

Commands passed locally in `/Users/arijitchowdhury/Dropbox/AI-Development/CI-OS`:

```text
python3 -m pytest tests/scripts/test_check_e2e_launch_readiness.py tests/scripts/test_check_live_operational_safety.py tests/scripts/test_verify_hermes_package_contract.py tests/deploy/test_cios_daily_wrapper.py -q
98 passed in 14.58s

python3 scripts/verify_hermes_package_contract.py --app-dir . --skip-python-imports
PASS: CI-OS Hermes package contract satisfied

python3 -m py_compile scripts/check_live_operational_safety.py scripts/check_e2e_launch_readiness.py scripts/verify_hermes_package_contract.py
pass

git diff --check
pass
```

## Verified VPS Evidence

Commands passed on ChowMes against `/opt/cios/app` as the `cios` application user:

```text
sudo -n -u cios .venv/bin/python scripts/verify_hermes_package_contract.py --app-dir /opt/cios/app --skip-python-imports
PASS: CI-OS Hermes package contract satisfied

sudo -n -u cios .venv/bin/python scripts/check_live_operational_safety.py --app-dir /opt/cios/app --public-dir /opt/cios/public --public-store-dir /opt/cios/public-store --expected-package-commit 42345adb240086ee6aa6d185337428271aa3ceda --output /opt/cios/app/out/live-operational-safety.json
status=passed
operational_safe=true
hidden_staging_dir_count=0
root_owned_artifact_count=0
orphan_process_count=0
served_release_ready=true
current_release_exists=true
```

Live dashboard click validation against `https://ci.chowmes.com/` passed:

```text
PASS market_field
PASS structure
PASS nav_targets
PASS timeline
PASS semantic_layer
PASS priority_selection
PASS brief_routing
PASS appendices
PASS viewport_390
PASS viewport_768
PASS viewport_1280
PASS dashboard_click_validation
```

## Corrected Launch Readiness Result

Artifact directory:

```text
/tmp/cios-phase7-live-42345ad
```

Aggregate command:

```text
python3 scripts/check_e2e_launch_readiness.py --public-status /tmp/cios-phase7-live-42345ad/argus-latest-run-status.json --click-validation-log /tmp/cios-phase7-live-42345ad/dashboard-click-validation.log --package-contract-log /tmp/cios-phase7-live-42345ad/hermes-package-contract.log --public-redaction /tmp/cios-phase7-live-42345ad/public-artifact-redaction.json --public-safety-scan /tmp/cios-phase7-live-42345ad/public-artifact-safety-scan.json --operational-safety /tmp/cios-phase7-live-42345ad/live-operational-safety.json --min-active-sources 1 --max-failed-sources 1 --output /tmp/cios-phase7-live-42345ad/cios-e2e-launch-readiness.json
```

Result:

```text
status=fail
dashboard_click_validation_passed=true
hermes_package_contract_passed=true
live_operational_safety_passed=true
product_reality_present=true
public_artifact_redaction_passed=true
public_artifact_scan_passed=true
public_safety_ok=true
source_coverage_complete=true
source_failure_budget_ok=true
public_status_publishable=false
audience_demand_processed=false
```

Remaining blockers:

```text
public_status_publishable:
publish_status=published status=blocked_on_evidence

audience_demand_processed:
audience_demand.status=processed_partial_plan_coverage demand_signal_count=101
next_action=collect_missing_plan_demand
```

## Decision

Phase 7 has not passed.

The live deployment hygiene, public safety, package contract, click journey, source failure budget, and product-reality evidence gates now pass. The remaining blocker is semantic launch readiness: the public run is still `blocked_on_evidence` because audience demand is only partial-plan coverage.

Next Phase 7 work should resolve or explicitly scope the demand-plan blocker before claiming launch readiness.
