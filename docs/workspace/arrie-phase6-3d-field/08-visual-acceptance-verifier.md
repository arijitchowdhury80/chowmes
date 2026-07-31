# Phase 6 Visual Acceptance Verifier

Date: 2026-07-28
Status: verified with design-authority gap

## Purpose

Create a repeatable visual acceptance check for the CI-OS / Argus Market Field so Phase 6 can be judged on rendered behavior rather than screenshots or subjective memory.

This verifier does not close Phase 6 visual acceptance by itself. The documented UI/UX SOP or an explicit temporary pilot-design-authority waiver is still required before the Phase 6 visual gate can pass.

## Added CI-OS Artifact

Path: `scripts/validate_market_field_visual_acceptance.py`

The script validates a rendered dashboard URL across:

- mobile: 390 x 844
- tablet: 768 x 1024
- desktop: 1280 x 900

## Checks

- `#market-field`, `#market-field-3d`, `#market-field-state`, and hotspot controls exist.
- The Market Field appears before raw evidence.
- The expected hotspot is `Agent Studio`.
- Click-to-reveal selection updates the selected title.
- The `30D` time-window control updates `#market-field[data-selected-time-window]`.
- The proof drawer opens and stays visible.
- The 3D canvas pixel probe is nonblank.
- Critical controls and story elements are reachable without horizontal clipping.
- Required story terms are visible:
  - Agent Studio
  - Product reality
  - Market conversation
  - Audience Demand
  - Product Marketing
  - Confidence boundaries
- Browser console has no errors.

## Verified Local Artifact

Artifact directory: `/tmp/cios-agent-studio-visual-acceptance/`

Commands verified:

```bash
python3 scripts/build_agent_studio_market_field_fixture.py --out-dir /tmp/cios-agent-studio-visual-acceptance
python3 scripts/validate_market_field_visual_acceptance.py --url file:///private/tmp/cios-agent-studio-visual-acceptance/argus-dashboard.html --output /tmp/cios-agent-studio-visual-acceptance/market-field-visual-acceptance.json
```

Result:

```json
{
  "status": "passed_with_design_authority_gap",
  "design_authority_status": "missing_or_unwaived",
  "final_visual_acceptance": false,
  "viewport_count": 3,
  "console_errors": []
}
```

Viewport checks passed:

- mobile: canvas nonblank, selected hotspot `Agent Studio`, no clipped critical selectors
- tablet: canvas nonblank, selected hotspot `Agent Studio`, no clipped critical selectors
- desktop: canvas nonblank, selected hotspot `Agent Studio`, no clipped critical selectors

## Verification

```bash
python3 -m pytest tests/scripts/test_validate_market_field_visual_acceptance.py tests/scripts/test_verify_hermes_package_contract.py -q
```

Result: `69 passed`

```bash
python3 -m pytest tests/dashboard/test_market_field_view_model.py tests/dashboard/test_state_builder.py tests/dashboard/test_cockpit_renderer.py tests/scripts/test_validate_dashboard_clicks_market_field.py tests/scripts/test_validate_market_field_story.py tests/scripts/test_build_agent_studio_market_field_fixture.py tests/scripts/test_validate_market_field_visual_acceptance.py tests/scripts/test_verify_hermes_package_contract.py -q
```

Result: `165 passed`

```bash
python3 scripts/verify_hermes_package_contract.py --app-dir . --skip-python-imports
python3 -m py_compile scripts/validate_market_field_visual_acceptance.py scripts/validate_market_field_story.py scripts/build_agent_studio_market_field_fixture.py scripts/verify_hermes_package_contract.py
git diff --check
```

Result: all passed.

## Gate Interpretation

This passes the reusable engineering verifier for the current Agent Studio Market Field story. It does not pass the final Phase 6 visual acceptance gate until the missing UI/UX SOP/design-authority dependency is restored or explicitly waived for the pilot.
