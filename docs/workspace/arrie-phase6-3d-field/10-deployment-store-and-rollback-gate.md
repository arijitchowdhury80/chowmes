# Phase 6 Deployment Store And Rollback Gate

Date: 2026-07-28
Status: package deployment mechanics verified locally

## Purpose

Close the local deployment-mechanics gap before Phase 6 live staging. The dashboard must not depend on a loose copy into a public folder with no rollback trail.

This gate verifies that the CI-OS daily wrapper:

- publishes from the CI-OS package path,
- stages public artifacts before touching the public site,
- runs the public artifact safety scan before publication,
- writes a public-store release manifest without leaking internal source paths,
- records the previous release pointer for rollback,
- refreshes the `served` public root from the promoted release,
- preserves the previous release directory.

## CI-OS Changes

Path: `deploy/cios-daily.sh`

Changes:

- `promote_public_store_if_present` now records `previous_release` from the existing `current` symlink.
- `publication-manifest.json` no longer writes `source_public_dir`.
- The public-store `served` directory is refreshed from the promoted release via a staged directory swap.
- The previous served directory is retained as `served.previous`.
- `scripts/scan_public_artifacts.py` runs against `$STAGE` before any staged artifact is copied to `$PUB`.
- Package preflight now fails if the daily wrapper omits `scan_public_artifacts.py`.

## Verified Behavior

Tested behavior:

- unsafe staged public content blocks before `public/index.html` or `public/data/semantic-dashboard.json` is written,
- public-store `current` points to a new release,
- public-store `served/index.html` is updated to the current cockpit,
- release manifest includes `previous_release`,
- release manifest does not include `source_public_dir`,
- old release directory remains available for rollback,
- package preflight enforces the safety-scan wrapper hook.

## Verification

```bash
python3 -m pytest tests/deploy/test_cios_daily_wrapper.py -q
```

Result: `20 passed`

```bash
python3 -m pytest tests/deploy/test_cios_daily_wrapper.py tests/scripts/test_scan_public_artifacts.py tests/scripts/test_verify_hermes_package_contract.py -q
```

Result: `92 passed`

```bash
python3 -m pytest tests/dashboard/test_market_field_view_model.py tests/dashboard/test_state_builder.py tests/dashboard/test_cockpit_renderer.py tests/scripts/test_validate_dashboard_clicks_market_field.py tests/scripts/test_validate_market_field_story.py tests/scripts/test_build_agent_studio_market_field_fixture.py tests/scripts/test_validate_market_field_visual_acceptance.py tests/scripts/test_scan_public_artifacts.py tests/scripts/test_verify_hermes_package_contract.py -q
```

Result: `171 passed`

```bash
python3 scripts/verify_hermes_package_contract.py --app-dir . --skip-python-imports
python3 -m py_compile scripts/scan_public_artifacts.py scripts/validate_market_field_visual_acceptance.py scripts/validate_market_field_story.py scripts/build_agent_studio_market_field_fixture.py scripts/verify_hermes_package_contract.py
git diff --check
```

Result: all passed.

## Gate Interpretation

This clears the local deployment-mechanics and rollback-preparation slice.

It does not clear the live deployment/staging gate. The package still needs to be deployed to the Chowmes CI-OS app path, executed there as the `cios` application user, and validated live against `https://ci.chowmes.com/`.
