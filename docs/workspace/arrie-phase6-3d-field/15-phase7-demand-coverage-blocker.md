# Phase 7 Demand Coverage Blocker

Date: 2026-07-28

## Scope

This records the live Phase 7 run after fixing the daily wrapper demand sequencing. Phase 7 still has not passed.

## CI-OS Fixes Shipped

Commits pushed to `origin/codex/ci-os-phase0-baseline` and deployed to `/opt/cios/app`:

- `09b415a6c112aa7f3491f413e8d4b72d4add8c2c`: daily wrapper accepts limited planned demand evidence.
- `30ca06f01b7557ef78a22e620faa15aef1b965b7`: daily wrapper prepares planned demand before running demand intake.

Deployed package stamp:

```text
30ca06f01b7557ef78a22e620faa15aef1b965b7
```

## Live Daily Run

Command shape:

```text
sudo -n -u cios env CIOS_DISABLE_RUNNER_HANDOFF=1 CIOS_APP_DIR=/opt/cios/app CIOS_PUBLIC_DIR=/opt/cios/public CIOS_ENV_FILE=/etc/cios-env CIOS_PUBLIC_STORE_DIR=/opt/cios/public-store CIOS_DAILY_RUN_TIMEOUT_SECONDS=1350 deploy/cios-daily.sh
```

Result:

```text
Run complete in 1052.4s
active_sources=42
attempted=42
fetched=41
failed=1
facts=454
deltas=454
signals=4
quality=passed
delivered=True
product_market=ran
PASS public_artifact_redaction
PASS public_artifact_safety_scan
dashboard published to ci.chowmes.com
```

## Post-Run Gate Evidence

Artifact directory:

```text
/tmp/cios-phase7-live-30ca06f
```

Live dashboard click validation passed:

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

Aggregate launch readiness still failed:

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

The public status remains:

```text
publish_status=published
status=blocked_on_evidence
next_action=collect_missing_plan_demand
```

## Demand Coverage Result

The wrapper fix worked: planned demand is now consumed before intake. The live demand plane covers one planned topic:

```text
Agent Studio: value=1619.0, change_pct=1.1558
```

The live readiness gate still requires coverage for the full Argus demand plan. Current coverage:

```text
covered_topic_count=1
planned_topic_count=12
coverage_ratio=0.0833
missing_topic_count=11
```

Missing topics:

```text
30-day Free Trial
A/B testing
A/B Testing & Optimization
ABRA
Account & Billing Management
analyst_recognition
AI Assistant
market_positioning
Product Branding
product_capability
Shopping Assistant
```

## Decision Point

There is no remaining deployment hygiene blocker in this slice. The remaining blocker is semantic launch policy:

1. Strict Phase 7: collect/import demand rows for the 11 missing planned topics, then rerun the daily path and aggregate launch gate.
2. Controlled-pilot waiver: explicitly accept `1/12` demand-topic coverage with limited confidence, then update the launch-readiness gate and public status policy so this is not mislabeled as fully evidence-complete.

Until one of those decisions is made and verified, Phase 7 remains active and Phase 8 must not start.
