# CI-OS Phase 2 publication gate

Date: 2026-07-27 ET / 2026-07-28 UTC
Status: passed
Runtime: Hermes wrapper -> `cios` app-user runner

## Result

Phase 2 is passed. CI-OS produced a fresh, public, run-bound dashboard through
the real Hermes wrapper path after the Audience Demand manual feed was imported.

Fresh verified run:

- Run ID: `cios-20260728T032901Z-3409872`
- Public run status: `published`
- Publish status: `published`
- Generated at: `2026-07-28T03:39:54.169253Z`
- Public dashboard updated: `true`
- Runner service: `cios-runner.service`
- Runtime result: exit code `0`
- Runtime duration: `10min 53.952s`
- Runtime owner: `cios`
- Public status URL: `https://ci.chowmes.com/data/argus-latest-run-status.json`
- Public semantic data URL: `https://ci.chowmes.com/v2/data/semantic-dashboard.json`

Public status and semantic dashboard now agree on the same run ID.

## Live Evidence

Live public status summary:

```json
{
  "status": "published",
  "publish_status": "published",
  "run_id": "cios-20260728T032901Z-3409872",
  "generated_at": "2026-07-28T03:39:54.169253Z",
  "public_dashboard_updated": true
}
```

Live semantic dashboard summary:

```json
{
  "status": "ran",
  "run_id": "cios-20260728T032901Z-3409872",
  "demand_plane_status": "processed",
  "demand_signal_count": 100,
  "recommendation_count": 0,
  "pattern_count": 2
}
```

Live page validation:

```text
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

Focused local publication and demand tests:

```text
198 passed, 2 deselected in 16.16s
```

Focused renderer regression tests:

```text
34 passed in 0.77s
```

## Fix Applied During Gate

The first fresh run after demand import passed backend publication but failed
live click validation because the deployed renderer still served the older
navigation contract. The source branch already had the correct Timeline and
Patterns navigation; production `/opt/cios/app` was behind the branch.

Corrective action:

- Added a regression assertion in CI-OS commit `95caab9`.
- Backed up deployed renderer/test files to
  `/opt/cios/backups/nav-contract-95caab9-20260728T032838Z`.
- Installed the renderer and regression test from commit `95caab9`.
- Reran the Hermes wrapper and live click validation.

No Hermes core, SSH, firewall, Caddy, or credential settings were changed.

## Remaining Gate Boundary

Phase 2 publication is no longer the active blocker.

Phase 3 is now active. The fresh public status names the next Hermes action:

```text
Run product-surface extraction for Athos Commerce, then refresh Argus from the evidence ledger to resolve the 200+ third-party publishers (e.g., Google, Apple, Amazon Alexa, Bing) matrix cell.
```

Audience Demand is connected through the approved manual Looker export path and
is visible in the fresh public semantic data as `demand_plane_status=processed`
with `demand_signal_count=100`. Recurring GA4 automation remains deferred until
the GA4 property and credential env values are provided. This deferral does not
block Phase 3 Product Muscle work.
