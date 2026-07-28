# aRRIe Phase 6 True 3D Market Field Status

Date: 2026-07-28
Status: Phase 8 controlled monitored pilot released; observation window active

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
- CI-OS reusable visual acceptance verifier implemented:
  - `scripts/validate_market_field_visual_acceptance.py` validates the rendered Market Field across mobile, tablet, and desktop viewports.
  - It checks the 3D canvas, Agent Studio click-to-reveal selection, 30D time-window state, proof drawer behavior, visible story terms, critical selector clipping, Market Field before raw evidence, and console health.
  - Package contract now requires the verifier script.
- Built reusable local artifact under `/tmp/cios-agent-studio-visual-acceptance/`.
- Verified `/tmp/cios-agent-studio-visual-acceptance/market-field-visual-acceptance.json`: `status=passed_with_design_authority_gap`, `design_authority_status=missing_or_unwaived`, `final_visual_acceptance=false`, `viewport_count=3`, `console_errors=[]`, and no clipped critical selectors on mobile/tablet/desktop.
- Verified `python3 -m pytest tests/scripts/test_validate_market_field_visual_acceptance.py tests/scripts/test_verify_hermes_package_contract.py -q` passed with `69 passed`.
- Verified `python3 -m pytest tests/dashboard/test_market_field_view_model.py tests/dashboard/test_state_builder.py tests/dashboard/test_cockpit_renderer.py tests/scripts/test_validate_dashboard_clicks_market_field.py tests/scripts/test_validate_market_field_story.py tests/scripts/test_build_agent_studio_market_field_fixture.py tests/scripts/test_validate_market_field_visual_acceptance.py tests/scripts/test_verify_hermes_package_contract.py -q` passed with `165 passed`.
- Verified `python3 scripts/verify_hermes_package_contract.py --app-dir . --skip-python-imports` passed.
- Verified `python3 -m py_compile scripts/validate_market_field_visual_acceptance.py scripts/validate_market_field_story.py scripts/build_agent_studio_market_field_fixture.py scripts/verify_hermes_package_contract.py` passed.
- Verified `git diff --check` passed.
- CI-OS reusable public artifact safety scan implemented:
  - `scripts/scan_public_artifacts.py` scans public HTML/JS/JSON/CSS/TXT/map artifacts for private local paths, `file://` references, secret-like values, and forbidden external runtime/CDN hosts.
  - Package contract now requires the public-safety scanner.
  - The Agent Studio fixture manifest was hardened to write relative artifact names instead of absolute local paths.
- Built reusable local artifact under `/tmp/cios-agent-studio-public-safety/`.
- Verified `/tmp/cios-agent-studio-public-safety/public-artifact-safety-scan.json`: `status=passed`, `public_safe=true`, `scanned_file_count=3`, `findings=[]`.
- Verified `python3 -m pytest tests/scripts/test_build_agent_studio_market_field_fixture.py tests/scripts/test_scan_public_artifacts.py tests/scripts/test_verify_hermes_package_contract.py -q` passed with `71 passed`.
- Verified `python3 -m pytest tests/dashboard/test_market_field_view_model.py tests/dashboard/test_state_builder.py tests/dashboard/test_cockpit_renderer.py tests/scripts/test_validate_dashboard_clicks_market_field.py tests/scripts/test_validate_market_field_story.py tests/scripts/test_build_agent_studio_market_field_fixture.py tests/scripts/test_validate_market_field_visual_acceptance.py tests/scripts/test_scan_public_artifacts.py tests/scripts/test_verify_hermes_package_contract.py -q` passed with `170 passed`.
- Verified `python3 scripts/verify_hermes_package_contract.py --app-dir . --skip-python-imports` passed.
- Verified `python3 -m py_compile scripts/scan_public_artifacts.py scripts/validate_market_field_visual_acceptance.py scripts/validate_market_field_story.py scripts/build_agent_studio_market_field_fixture.py scripts/verify_hermes_package_contract.py` passed.
- Verified `git diff --check` passed.
- CI-OS public artifact redaction gate implemented:
  - `scripts/redact_public_artifacts.py` redacts internal filesystem paths and `file://` references from staged public HTML/JS/JSON/CSS/TXT/map artifacts.
  - `deploy/cios-daily.sh` now redacts the staged public bundle before running the public artifact safety scan.
  - Package preflight now requires the redaction script and wrapper redaction call.
  - The redactor intentionally does not mask secret-like values, so real secrets still fail `scripts/scan_public_artifacts.py`.
- Verified `python3 -m pytest tests/scripts/test_redact_public_artifacts.py tests/scripts/test_verify_hermes_package_contract.py::test_preflight_passes_complete_hermes_package_contract -q` passed with `4 passed`.
- Verified `python3 -m pytest tests/deploy/test_cios_daily_wrapper.py -q` passed with `20 passed`.
- Verified `python3 -m pytest tests/scripts/test_redact_public_artifacts.py tests/scripts/test_scan_public_artifacts.py tests/scripts/test_verify_hermes_package_contract.py -q` passed with `75 passed`.
- Verified `python3 -m pytest tests/dashboard/test_market_field_view_model.py tests/dashboard/test_state_builder.py tests/dashboard/test_cockpit_renderer.py tests/scripts/test_validate_dashboard_clicks_market_field.py tests/scripts/test_validate_market_field_story.py tests/scripts/test_build_agent_studio_market_field_fixture.py tests/scripts/test_validate_market_field_visual_acceptance.py tests/scripts/test_redact_public_artifacts.py tests/scripts/test_scan_public_artifacts.py tests/scripts/test_verify_hermes_package_contract.py -q` passed with `174 passed`.
- Verified `python3 scripts/verify_hermes_package_contract.py --app-dir . --skip-python-imports` passed.
- Verified `python3 -m py_compile scripts/redact_public_artifacts.py scripts/scan_public_artifacts.py scripts/validate_market_field_visual_acceptance.py scripts/validate_market_field_story.py scripts/build_agent_studio_market_field_fixture.py scripts/verify_hermes_package_contract.py` passed.
- Verified `git diff --check` passed.
- Verified local staged-public redaction proof under `/tmp/cios-public-redaction-check`: redaction `status=redacted`, `redacted_file_count=2`, `redaction_count=4`; post-redaction scan `status=passed`, `findings=[]`.
- CI-OS live deployment completed on Chowmes:
  - Deployed commit `760f03cbdf110c467a5b09b591017774d1db520e` to `/opt/cios/app`.
  - Backup before deploy: `/root/.hermes/backups/cios-phase6-redaction-before-20260728T120805Z.tgz`.
  - Live wrapper completed in `1045.9s` and published `https://ci.chowmes.com/`.
  - Public-store current release: `/opt/cios/public-store/releases/cios-20260728T122836Z-3951326`.
  - Remote package contract passed.
  - Public redaction evidence: `status=redacted`, `scanned_file_count=68`, `redacted_file_count=6`, `redaction_count=216`.
  - Public safety scan evidence: `status=passed`, `public_safe=true`, `scanned_file_count=68`, `findings=0`.
  - Hidden `.argus-publish.*` staging directories were removed from public roots after verification.
  - Follow-up CI-OS commit `760f03cbdf110c467a5b09b591017774d1db520e` prevents future staged bundle directories from being promoted into public-store releases.
- Verified `https://ci.chowmes.com/` returned HTTP 200 with content length `454630` and `last-modified: Tue, 28 Jul 2026 12:28:36 GMT`.
- Verified live semantic dashboard JSON: `schema_version=26`, `product_market_run=true`, `bytes=5336421`.
- Verified `python3 scripts/validate_dashboard_clicks.py --url https://ci.chowmes.com/` passed:
  - Market Field hotspot/time/proof interactions.
  - Structure, navigation, timeline, semantic heat map, priority state, competitor briefs, and appendices.
  - Responsive checks at `390x844`, `768x1024`, and `1280x900`.
- Arijit's 2026-07-28 approval is recorded as a temporary pilot design-authority waiver for Phase 6:
  - The missing UI/UX SOP/design-authority path is no longer a Phase 6 blocker for the controlled pilot.
  - Formal five-user comprehension, full accessibility, and restored design-authority validation move to post-pilot UX hardening.
  - The waiver does not authorize skipping Phase 7 or Phase 8 gates.
- CI-OS deployment-store and rollback-preparation slice implemented:
  - `deploy/cios-daily.sh` now runs `scripts/scan_public_artifacts.py` against the staged public bundle before copying anything to the public site.
  - `promote_public_store_if_present` now refreshes the public-store `served` root from the promoted release.
  - The publication manifest records the previous `current` release pointer and no longer writes the internal source public directory.
  - The previous served directory is retained as `served.previous`.
  - Package contract now fails if the wrapper omits the public artifact safety scan.
- Verified `python3 -m pytest tests/deploy/test_cios_daily_wrapper.py -q` passed with `20 passed`.
- Verified `python3 -m pytest tests/deploy/test_cios_daily_wrapper.py tests/scripts/test_scan_public_artifacts.py tests/scripts/test_verify_hermes_package_contract.py -q` passed with `92 passed`.
- Verified `python3 -m pytest tests/dashboard/test_market_field_view_model.py tests/dashboard/test_state_builder.py tests/dashboard/test_cockpit_renderer.py tests/scripts/test_validate_dashboard_clicks_market_field.py tests/scripts/test_validate_market_field_story.py tests/scripts/test_build_agent_studio_market_field_fixture.py tests/scripts/test_validate_market_field_visual_acceptance.py tests/scripts/test_scan_public_artifacts.py tests/scripts/test_verify_hermes_package_contract.py -q` passed with `171 passed`.
- Verified `python3 scripts/verify_hermes_package_contract.py --app-dir . --skip-python-imports` passed.
- Verified `python3 -m py_compile scripts/scan_public_artifacts.py scripts/validate_market_field_visual_acceptance.py scripts/validate_market_field_story.py scripts/build_agent_studio_market_field_fixture.py scripts/verify_hermes_package_contract.py` passed.
- Verified `git diff --check` passed.

## Gate

The human direction gate is cleared.

Reusable local story, visual verifier, public-safety, public-redaction, deployment-mechanics, live deployment, and live dashboard click-validation gates are cleared for the Agent Studio Market Field artifact.

Phase 6 is passed for the controlled pilot.

Next production work: run the Phase 8 observation window from deployed package `b4d7423cff92b719dd48bc4b34af0ff21faefc16`, record usage, rejection, or amendment of current PMM recommendation `2` by a named team, and review learning effects before any completion claim.
