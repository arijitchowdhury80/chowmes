# Phase 6 Public Artifact Safety Scan

Date: 2026-07-28
Status: verified locally against reusable Agent Studio artifact

## Purpose

Add a reusable public-safety gate before any Phase 6 dashboard artifact is treated as deployable or launch-ready.

The scan is static and intentionally conservative. It looks for private local paths, `file://` references, secret-like values, and forbidden external runtime/CDN hosts in public HTML, JS, JSON, CSS, TXT, and source-map files.

## Added CI-OS Artifact

Path: `scripts/scan_public_artifacts.py`

The script scans a public artifact directory and writes a machine-readable JSON verdict.

Failure classes:

- `private_path`
- `file_url`
- `secret_like_value`
- `external_runtime_host`
- `missing_public_dir`

## Fixture Hardening

The Agent Studio fixture manifest previously wrote absolute local artifact paths. The new safety scan caught this on the real `/tmp` artifact.

Fix implemented:

- `scripts/build_agent_studio_market_field_fixture.py` now writes relative artifact names in its manifest:
  - `argus-dashboard.html`
  - `argus-dashboard.json`
- Regression test added so local output paths do not leak into the manifest.

## Verified Local Artifact

Artifact directory: `/tmp/cios-agent-studio-public-safety/`

Commands verified:

```bash
python3 scripts/build_agent_studio_market_field_fixture.py --out-dir /tmp/cios-agent-studio-public-safety
python3 scripts/scan_public_artifacts.py --public-dir /tmp/cios-agent-studio-public-safety --output /tmp/cios-agent-studio-public-safety/public-artifact-safety-scan.json
```

Result:

```json
{
  "status": "passed",
  "public_safe": true,
  "scanned_file_count": 3,
  "findings": []
}
```

## Verification

```bash
python3 -m pytest tests/scripts/test_build_agent_studio_market_field_fixture.py tests/scripts/test_scan_public_artifacts.py tests/scripts/test_verify_hermes_package_contract.py -q
```

Result: `71 passed`

```bash
python3 -m pytest tests/dashboard/test_market_field_view_model.py tests/dashboard/test_state_builder.py tests/dashboard/test_cockpit_renderer.py tests/scripts/test_validate_dashboard_clicks_market_field.py tests/scripts/test_validate_market_field_story.py tests/scripts/test_build_agent_studio_market_field_fixture.py tests/scripts/test_validate_market_field_visual_acceptance.py tests/scripts/test_scan_public_artifacts.py tests/scripts/test_verify_hermes_package_contract.py -q
```

Result: `170 passed`

```bash
python3 scripts/verify_hermes_package_contract.py --app-dir . --skip-python-imports
python3 -m py_compile scripts/scan_public_artifacts.py scripts/validate_market_field_visual_acceptance.py scripts/validate_market_field_story.py scripts/build_agent_studio_market_field_fixture.py scripts/verify_hermes_package_contract.py
git diff --check
```

Result: all passed.

## Gate Interpretation

This clears the local reusable public-safety gate for the Agent Studio Market Field artifact.

It does not clear the live deployment gate. The public production artifact still needs to be scanned after deployment/staging generation, and Phase 6 visual acceptance remains gated by the missing UI/UX SOP/design-authority dependency unless explicitly waived.
