# aRRIe Phase 6 True 3D Market Field Status

Date: 2026-07-28
Status: true 3D Product IA direction accepted; reusable Agent Studio validation artifact verified locally

## Scope

Create the next Product IA review artifact for CI-OS / Argus after Phase 5 acceptance.

This workspace supersedes the earlier 2.5D-only Market Field mockup as the next review direction. It does not modify Hermes core, deploy production UI, or claim Phase 6 completion.

## Current Task

Build and validate a true 3D constellation-style Market Field prototype that uses the accepted Agent Studio recommendation as the first story:

- product proof
- competitor / market conversation context
- Audience Demand
- confidence limits
- named-team action
- proof drawer
- Today / 7D / 30D / Custom time behavior

## Completed

- Design-thinking artifact written.
- Prototype contract written.
- True 3D Three.js Market Field mockup created at `docs/mockups/arrie/2026-07-28-market-field-true-3d.html`.
- Desktop and mobile screenshots captured.
- Local Playwright validation passed with WebGL canvas-pixel check and interaction checks.
- Production implementation plan written.
- Phase 6 acceptance checklist written.
- 3D runtime dependency review written, including Three.js `0.160.0` license, integrity, tarball checksum, candidate vendoring path, CDN rejection rule, and production validation requirements.
- Human direction gate accepted by Arijit on 2026-07-28: true 3D constellation Market Field is the Product IA spine for production implementation.
- CI-OS production guardrail slice committed: vendored Three.js runtime, license/checksum manifest, package verifier required paths, checksum validation, and CDN rejection coverage.
- CI-OS production shell slice implemented: `#market-field-3d` canvas, serialized Market Field graph JSON, reviewed runtime metadata, and deterministic canvas rendering from existing graph state.
- Verified `python3 -m pytest tests/dashboard/test_cockpit_renderer.py -q` passed.
- Verified `python3 -m pytest tests/scripts/test_verify_hermes_package_contract.py -q` passed.
- Verified `python3 scripts/verify_hermes_package_contract.py --app-dir . --skip-python-imports` passed.
- Verified local Playwright browser smoke on `/tmp/cios-market-field-shell.html`: canvas exists, pixel probe nonblank, no console errors.
- CI-OS production interaction slice implemented: hotspot buttons now carry click-to-reveal payload, selected read/facts/unknowns update from clicked hotspots, graph nodes mirror selected hotspot context, time-window controls update Market Field state, and the 3D canvas redraws from the selected context.
- `scripts/validate_dashboard_clicks.py` now requires `#market-field-3d`, checks canvas pixels, verifies selected hotspot state, and verifies Today / 7D / 30D / Custom state changes.
- Verified `python3 -m pytest tests/dashboard/test_cockpit_renderer.py tests/scripts/test_validate_dashboard_clicks_market_field.py tests/scripts/test_verify_hermes_package_contract.py -q` passed.
- Verified local Playwright browser smoke on `/tmp/cios-market-field-interactions.html`: second hotspot click updated selected read, facts, unknowns, selected graph nodes, 30D time state, proof drawer, canvas pixels, and produced no console errors.
- CI-OS Agent Studio story slice implemented in the state builder: Market Field now emits product reality, market conversation, Audience Demand, Argus action, confidence-limit nodes/edges, and proof planes from the accepted recommendation evidence rather than only a generic top-pattern node.
- Verified `python3 -m pytest tests/dashboard/test_market_field_view_model.py tests/dashboard/test_state_builder.py tests/dashboard/test_cockpit_renderer.py tests/scripts/test_validate_dashboard_clicks_market_field.py tests/scripts/test_verify_hermes_package_contract.py -q` passed.
- Verified local Playwright browser smoke on `/tmp/cios-agent-studio-story.html`: Agent Studio product reality, market conversation, Audience Demand, Product Marketing action, confidence boundary, graph payload, canvas pixels, and console health all passed.
- CI-OS reusable local validation artifact slice implemented:
  - `scripts/build_agent_studio_market_field_fixture.py` builds deterministic `argus-dashboard.html`, `argus-dashboard.json`, and fixture manifest from package state models.
  - `scripts/validate_market_field_story.py` validates the rendered dashboard with Playwright, checks the embedded Market Field story payload, checks required node/edge/proof planes, checks Product Marketing ownership, checks nonblank canvas pixels, and writes JSON evidence.
  - Package contract now requires both scripts.
- Verified `python3 -m pytest tests/dashboard/test_market_field_view_model.py tests/dashboard/test_state_builder.py tests/dashboard/test_cockpit_renderer.py tests/scripts/test_validate_dashboard_clicks_market_field.py tests/scripts/test_validate_market_field_story.py tests/scripts/test_build_agent_studio_market_field_fixture.py tests/scripts/test_verify_hermes_package_contract.py -q` passed.
- Verified `python3 scripts/verify_hermes_package_contract.py --app-dir . --skip-python-imports` passed.
- Built reusable local artifact under `/tmp/cios-agent-studio-validation/`.
- Verified `/tmp/cios-agent-studio-validation/agent-studio-market-field-fixture-manifest.json`: selected hotspot `Agent Studio`, node types include product reality / market conversation / Audience Demand / Argus action / unknown boundary, proof planes include product reality / market conversation / Audience Demand / Argus recommendation.
- Verified `/tmp/cios-agent-studio-validation/market-field-story-validation.json`: `status=passed`, `canvas_nonblank=true`, `console_errors=[]`, `action_owners=["Product Marketing"]`, `node_count=9`, `edge_count=8`, `proof_count=4`.

## Gate

The human direction gate is cleared.

Next production work: resolve or explicitly waive the missing UI/UX SOP path, run visual acceptance against the reusable local artifact, then prepare the live deployment/staging gate.
