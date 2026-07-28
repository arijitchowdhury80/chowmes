# Market Field Local Implementation Validation

Date: 2026-07-28
Status: local implementation validation passed

## Scope

This validates the CI-OS Market Field implementation locally before staging or live deployment.
It does not claim the live `https://ci.chowmes.com/` UX gate has passed.

## CI-OS Commits Validated

- `8103d10` Add Market Field dashboard state types
- `f0c2c8d` Build Market Field state from intelligence data
- `9decd9d` Render Market Field first dashboard surface
- `f3bf23e` Validate Market Field dashboard journey
- `9a0b280` Score movement maps against evidence window

## Commands

- `python3 -m pytest tests/scripts/test_validate_dashboard_clicks_market_field.py tests/scripts/test_validate_dashboard_clicks_dependencies.py tests/dashboard/test_cockpit_renderer.py tests/dashboard/test_market_field_view_model.py -q`
- `python3 -m pytest tests/dashboard tests/scripts -q`
- `python3 -m pytest tests/dashboard tests/scripts tests/intelligence -q`
- Generated a local validation dashboard fixture at `/tmp/cios-market-field-render/index.html` using the committed `cios.dashboard.cockpit_renderer.render_cockpit_html` and committed dashboard state types.
- `python3 -m http.server 8787 --bind 127.0.0.1 --directory /tmp/cios-market-field-render`
- `python3 scripts/validate_dashboard_clicks.py --url http://127.0.0.1:8787/`
- `"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new --disable-gpu --hide-scrollbars --window-size=1440,1100 --screenshot=/tmp/cios-market-field-desktop.png http://127.0.0.1:8787/`
- `"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new --disable-gpu --hide-scrollbars --window-size=390,1100 --screenshot=/tmp/cios-market-field-mobile.png http://127.0.0.1:8787/`
- `file /tmp/cios-market-field-desktop.png /tmp/cios-market-field-mobile.png`
- Screenshot nonblank check with Pillow image dimensions, mean RGB, and extrema.

## Results

- Focused tests: `39 passed in 0.77s`
- Dashboard + scripts package subset: `501 passed in 9.11s`
- Dashboard + scripts + intelligence package subset: `596 passed in 10.86s`
- Local click validation: passed.
- Desktop screenshot: `/tmp/cios-market-field-desktop.png`, `1440 x 1100`, nonblank.
- Mobile screenshot: `/tmp/cios-market-field-mobile.png`, `390 x 1100`, nonblank.

## Click Validation Output

```text
PASS market_field: Hotspot selection, time windows, action layer, proof drawer, Evidence, and Admin sections validated
PASS structure: Read, timeline, semantic layer, priority moves, selected competitor, role implications, evidence sections, and Argus assets present
PASS nav_targets: Top nav updates hash/current state and lands on distinct sections
PASS timeline: History controls, holistic coverage, and priority rationale are visible
PASS semantic_layer: Selector, heat map, recommendation, and confidence rubric validated with Bloomreach
PASS priority_selection: Elastic selection updates selected panel and role implications
PASS brief_routing: Checked Constructor, Elastic, Algonomy
PASS appendices: Coverage and evidence appendices open and expose brief/source details
PASS viewport_390: 390x844 loaded rebuilt dashboard
PASS viewport_768: 768x1024 loaded rebuilt dashboard
PASS viewport_1280: 1280x900 loaded rebuilt dashboard
PASS dashboard_click_validation
```

## Screenshot Check

```text
/tmp/cios-market-field-desktop.png: PNG image data, 1440 x 1100, 8-bit/color RGB, non-interlaced
/tmp/cios-market-field-mobile.png:  PNG image data, 390 x 1100, 8-bit/color RGB, non-interlaced
/tmp/cios-market-field-desktop.png (1440, 1100) mean= (186.67, 184.06, 177.64) extrema= ((0, 255), (0, 253))
/tmp/cios-market-field-mobile.png (390, 1100) mean= (183.42, 180.81, 173.99) extrema= ((20, 254), (21, 252))
```

## Package Test Follow-Up

The earlier `looker_export_count` package-test failure did not reproduce:

- Narrow reproduction: `tests/scripts/test_daily_run.py::test_product_market_chain_runs_plan_execute_payload_and_runner` passed.
- Script suite: `359 passed in 8.51s`.
- Dashboard + scripts subset: `501 passed in 9.11s`.

The first `tests/dashboard tests/scripts tests/intelligence` run exposed a deterministic movement-map failure in `tests/intelligence/test_runner.py::test_run_product_market_payload_embeds_market_movement_map_in_brief`.
Root cause: market movement scoring used wall-clock `datetime.now()` instead of the current run's evidence window, so historical July 8 evidence aged out when replayed on July 28.
CI-OS commit `9a0b280` fixed this by deriving movement-map `as_of` from product, conversation, and demand evidence timestamps.
The package subset then passed with `596 passed in 10.86s`.

## Judgment

`ready_for_staging`

The local Market Field UX implementation is ready for staging validation. The live UX gate is not cleared until package tests, deployment, public run-state checks, and live click validation pass on `https://ci.chowmes.com/`.
