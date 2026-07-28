# Phase 6 Live Deployment And Click Validation

Date: 2026-07-28
Status: verified live on `https://ci.chowmes.com/`

## Deployment

CI-OS package branch deployed to `/opt/cios/app` on Chowmes.

- Deployed commit: `760f03cbdf110c467a5b09b591017774d1db520e`
- Backup before deploy: `/root/.hermes/backups/cios-phase6-redaction-before-20260728T120805Z.tgz`
- Public-store release: `/opt/cios/public-store/releases/cios-20260728T122836Z-3951326`
- Public-store current pointer: `releases/cios-20260728T122836Z-3951326`

The live run completed in `1045.9s` and published the dashboard from `/opt/cios/app`.

## Runtime Evidence

Remote package contract:

```text
PASS: CI-OS Hermes package contract satisfied
```

Public artifact redaction evidence:

- `status=redacted`
- `scanned_file_count=68`
- `redacted_file_count=6`
- `redaction_count=216`
- `findings=0`

Public artifact safety scan evidence:

- `status=passed`
- `public_safe=true`
- `scanned_file_count=68`
- `findings=0`

Generated hidden staging directories were removed from:

- `/opt/cios/public`
- `/opt/cios/public-store/served`
- `/opt/cios/public-store/releases/cios-20260728T122836Z-3951326`

Follow-up CI-OS commit `760f03cbdf110c467a5b09b591017774d1db520e` prevents future `.argus-publish.*` staging directories from being promoted into public-store releases.

## Live URL Evidence

`https://ci.chowmes.com/` returned:

```text
HTTP/2 200
content-type: text/html
last-modified: Tue, 28 Jul 2026 12:28:36 GMT
content-length: 454630
```

`https://ci.chowmes.com/data/semantic-dashboard.json` returned:

- `schema_version=26`
- `product_market_run=true`
- `bytes=5336421`

## Live Click Validation

Command:

```bash
python3 scripts/validate_dashboard_clicks.py --url https://ci.chowmes.com/
```

Result:

```text
PASS market_field: Hotspot selection, time windows, action layer, proof drawer, Evidence, and Admin sections validated
PASS structure: Read, timeline, semantic layer, priority moves, selected competitor, role implications, evidence sections, and Argus assets present
PASS nav_targets: Top nav updates hash/current state and lands on distinct sections
PASS timeline: History controls, holistic coverage, and priority rationale are visible
PASS semantic_layer: Selector, heat map, recommendation, and confidence rubric validated with Google Vertex AI Search
PASS priority_selection: Quiet current run has no priority buttons and shows the no-new-material-moves state
PASS brief_routing: Checked Constructor, Elastic, Algonomy
PASS appendices: Coverage and evidence appendices open and expose brief/source details
PASS viewport_390: 390x844 loaded rebuilt dashboard
PASS viewport_768: 768x1024 loaded rebuilt dashboard
PASS viewport_1280: 1280x900 loaded rebuilt dashboard
PASS dashboard_click_validation
```

## Gate Judgment

The Phase 6 live deployment and click-validation gate is cleared.

Phase 6 final acceptance still needs explicit treatment of the design-authority gap. The live technical gates now pass, but the previously recorded UI/UX SOP/design-authority dependency remains missing unless Arijit's current approval is recorded as a temporary pilot design-authority waiver.
