# Phase 6 Public Artifact Redaction Gate

Date: 2026-07-28
Status: verified locally; required before live deploy

## Why This Gate Exists

The deployed CI-OS public JSON currently contains internal filesystem references from the runtime app tree. The public safety scanner correctly treats those as release blockers, but a direct deploy would fail until the staged public bundle is cleaned.

This gate adds a narrow redaction step before the public safety scan:

1. Build the staged public bundle.
2. Redact private filesystem references and `file://` URLs from staged HTML/JS/JSON/CSS/TXT/map artifacts.
3. Run the public artifact safety scan against the redacted staged bundle.
4. Publish only if the safety scan passes.

The redactor does not mask secret-like values. Tokens, API keys, passwords, and similar values must still fail the scanner.

## CI-OS Changes

- Added `scripts/redact_public_artifacts.py`.
- Wired `deploy/cios-daily.sh` to run the redactor against `$STAGE` before `scripts/scan_public_artifacts.py`.
- Updated `scripts/verify_hermes_package_contract.py` so package preflight requires the redactor and the wrapper redaction call.
- Updated deploy-wrapper tests so validated publish paths include `public-redaction` before `public-safety-scan`.

## Verification

Commands run from `/Users/arijitchowdhury/Dropbox/AI-Development/CI-OS`:

```bash
python3 -m pytest tests/scripts/test_redact_public_artifacts.py tests/scripts/test_verify_hermes_package_contract.py::test_preflight_passes_complete_hermes_package_contract -q
```

Result: `4 passed`.

```bash
python3 -m pytest tests/deploy/test_cios_daily_wrapper.py -q
```

Result: `20 passed`.

```bash
python3 -m pytest tests/scripts/test_redact_public_artifacts.py tests/scripts/test_scan_public_artifacts.py tests/scripts/test_verify_hermes_package_contract.py -q
```

Result: `75 passed`.

```bash
python3 -m pytest tests/dashboard/test_market_field_view_model.py tests/dashboard/test_state_builder.py tests/dashboard/test_cockpit_renderer.py tests/scripts/test_validate_dashboard_clicks_market_field.py tests/scripts/test_validate_market_field_story.py tests/scripts/test_build_agent_studio_market_field_fixture.py tests/scripts/test_validate_market_field_visual_acceptance.py tests/scripts/test_redact_public_artifacts.py tests/scripts/test_scan_public_artifacts.py tests/scripts/test_verify_hermes_package_contract.py -q
```

Result: `174 passed`.

```bash
python3 scripts/verify_hermes_package_contract.py --app-dir . --skip-python-imports
```

Result: `PASS: CI-OS Hermes package contract satisfied`.

```bash
python3 -m py_compile scripts/redact_public_artifacts.py scripts/scan_public_artifacts.py scripts/validate_market_field_visual_acceptance.py scripts/validate_market_field_story.py scripts/build_agent_studio_market_field_fixture.py scripts/verify_hermes_package_contract.py
git diff --check
```

Result: both passed.

## Local Redaction Proof

A staged-public proof was created under `/tmp/cios-public-redaction-check` with internal references in HTML and JSON.

```bash
python3 scripts/redact_public_artifacts.py --public-dir /tmp/cios-public-redaction-check --output /tmp/cios-public-redaction-check-redaction.json
python3 scripts/scan_public_artifacts.py --public-dir /tmp/cios-public-redaction-check --output /tmp/cios-public-redaction-check-scan.json
```

Redaction evidence:

- `status=redacted`
- `scanned_file_count=2`
- `redacted_file_count=2`
- `redaction_count=4`

Post-redaction safety scan evidence:

- `status=passed`
- `public_safe=true`
- `scanned_file_count=2`
- `findings=[]`

## Gate Judgment

The local public redaction gate is cleared.

Phase 6 remains active. This gate does not clear final visual acceptance, because the UI/UX SOP/design-authority dependency is still missing or unwaived.
