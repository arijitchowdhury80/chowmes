# CI-OS Intelligence Spine Goal Phase 0 Baseline

Date: 2026-07-30
Status: Phase 0 truth baseline passed; runtime and product blockers carried forward
Goal: `docs/goals/2026-07-30-ci-os-intelligence-spine-autonomous-goal.md`
Workflow: `development-loop`
Runtime boundary: Hermes remains the runtime OS. CI-OS remains a separately versioned extension. No Hermes core changes were made.

## Phase 0 Objective

Establish the real current state before changing anything:

1. Local source state.
2. Authoritative source and remote.
3. Deployed package and public artifact state.
4. Hermes cron, CI-OS queue, `cios` ownership, daily/weekly delivery state.
5. Current public dashboard/status/DB evidence.
6. Product-question gap matrix.

This artifact is a truth baseline only. It does not claim CI-OS is healthy or complete.

## Source Of Truth

| Item | Current truth |
|---|---|
| ChowMes workspace | `/Users/arijitchowdhury/Dropbox/AI-Development/Personal/ChowMes` |
| CI-OS source | `/Users/arijitchowdhury/Dropbox/AI-Development/CI-OS` |
| CI-OS GitHub remote | `https://github.com/arijitchowdhury80/algolia-competitive-intelligence.git` |
| CI-OS branch | `codex/ci-os-phase0-baseline` tracking `origin/codex/ci-os-phase0-baseline` |
| CI-OS local head | `e02d680 Clean up daily runner on wrapper interruption` |
| Deployed package marker | `/opt/cios/app/.cios-release-commit` exists |
| Deployed package commit | `e02d680` from Phase 8 exit evidence |
| Release bundle | `/opt/cios/releases/e02d680.tar.gz` |
| Release SHA-256 | `34b5f8e15fd0238d586759ce36f0b820cdf6f6c764b3d2c846ffc683ecb04fac` |
| Public site root | `/opt/cios/public` |

## Local Worktree Inventory

### ChowMes Repo

Current branch:

- `codex/hermes-resource-intake` tracking `origin/codex/hermes-resource-intake`
- Head: `abd2f42 Record CI-OS Phase 8 pilot exit`

Tracked dirty files:

- `CHOW_TRACKING.md`: pre-existing operational note update from 2026-07-09 documenting stale dashboard and earlier CI-OS v2 permission/timeout repair notes.
- `README.md`: pre-existing boundary note adding `hermes-core/` and `ci-os/` workspace descriptions.

Untracked goal/status files created by this work:

- `docs/goals/2026-07-30-ci-os-intelligence-spine-autonomous-goal.md`
- `docs/status/2026-07-30-ci-os-intelligence-spine-phase0-baseline.md`

Other untracked ChowMes material is classified as existing docs, mockups, Playwright captures, brainstorm artifacts, handoff bundles, knowledge imports, and embedded CI-OS planning material. These are not active CI-OS source-code changes for this goal. They must not be deleted or reverted without explicit approval.

### CI-OS Repo

Current branch:

- `codex/ci-os-phase0-baseline` tracking `origin/codex/ci-os-phase0-baseline`
- Head: `e02d680 Clean up daily runner on wrapper interruption`

Tracked dirty files:

- none

Untracked files:

- `data/` Looker / GA export inputs and processed archive/rejected outputs.
- Top-level export examples include:
  - `data/algolia-looker-demand_2026-07-07_2026-07-13.csv`
  - `data/algolia-looker-demand-manifest_2026-07-07_2026-07-13.json`
  - campaign, landing-page, page, source, and device/session CSV exports.
- Processed data also exists under `data/looker/algolia/_archive/20260728T061812Z/` and `data/looker/algolia/_rejected/20260728T061812Z/`.

No Dropbox-style conflicted source files were found in the active CI-OS repo during this Phase 0 pass.

## VPS And Runtime State

Read-only inspection through `scripts/chowmes-ssh-helper`:

| Item | Current truth |
|---|---|
| Host | `chowmes` |
| OS | Ubuntu 24.04.4 LTS |
| Connected user | `chowmesadmin` |
| `cios-runner.path` | active |
| `cios-runner.service` | inactive, last success 2026-07-28 04:42 EDT |
| `cios-admin.service` | active |
| `cios-claude-shim.service` | active |
| `cios-postgres` container | up, healthy |
| `hermes` container | up |
| `caddy` container | up |

Host path permissions:

| Path | Owner | Mode | Finding |
|---|---:|---:|---|
| `/opt/cios` | `root:root` | `755` | expected host root |
| `/opt/cios/app` | `cios:hermes` | `755` | not group writable |
| `/opt/cios/app/run-queue` | `cios:hermes` | `2755` | not group writable; likely causes Hermes enqueue failure |
| `/opt/cios/app/out` | `cios:hermes` | `2755` | not group writable |
| `/opt/cios/public` | `cios:hermes` | `2775` | group writable |
| `/opt/cios/releases` | `root:root` | `755` | contains mixed root-owned older bundles and cios-owned latest bundles |
| `/etc/cios-env` | `cios:hermes` | `640` | expected restricted env file |

The deployed `deploy/cios-host-permissions.sh` contract says host permissions should apply `chmod 2775 "$APP" "$APP/run-queue" "$APP/out" "$APP/tmp" ...`, but live `app`, `run-queue`, and `out` are `755`/`2755` rather than group-writable `2775`. This is a concrete runtime drift.

## Cron And Delivery State

Hermes main cron inside the `hermes` container:

- Job: `cios-v2-daily`
- Enabled: `true`
- State: `scheduled`
- Schedule: `0 9 * * *`
- Script: `cios-daily.sh`
- Delivery: `local`
- Last run: `2026-07-30T09:00:44.541599-04:00`
- Last status: `error`
- Last error: `Script exited with code 2`, `CI-OS queue operation failed: Permission denied`
- Next run: `2026-07-31T09:00:00-04:00`

Argus legacy profile cron inside the `hermes` container:

- `argus-competitive-research-daily`: paused, last ok `2026-07-07T09:00:46.513762-04:00`, delivery `telegram`.
- `argus-competitive-research-weekly`: paused, last ok `2026-07-05T09:01:14.479123-04:00`, delivery `telegram`.

CI-OS DB delivery rows:

- Latest Telegram `bot_deliveries` row: `id=99`, status `sent`, report `100`, created `2026-07-28 13:37:12.813135+00`.
- Delivery status counts: `sent=97`, `blocked=1`, `failed=1`.
- There are no successful Telegram delivery rows after 2026-07-28.

Weekly report rows:

- Latest weekly reports are `id=32` through `41`, all rendered on `2026-07-12`.
- No current weekly synthesis exists after 2026-07-12.

## Public Artifact State

Public status:

- URL: `https://ci.chowmes.com/data/argus-latest-run-status.json`
- Bytes: `19576`
- `status`: `limited_by_evidence`
- `publish_status`: `published`
- `generated_at`: `2026-07-28T14:31:38.284219Z`
- `dashboard_generated_at`: `2026-07-28T13:45:06.039823Z`
- Tenant: `algolia`
- Source coverage: `42` active, `42` checked, `4` failed.
- Current public recommendation: recommendation `2`, owner `PMM`, urgency `this_week`, confidence `0.68`.

Public dashboard:

- URL: `https://ci.chowmes.com/data/semantic-dashboard.json`
- Bytes: `5369998`
- `schema_version`: `26`
- `generated_at`: `2026-07-28T13:45:06.039823Z`
- `run_health.run_id`: `daily-algolia-1785245335`
- `run_health.generated_at`: `2026-07-28T13:37:13.733290Z`
- `run_health.delivery_status`: `sent`
- `run_health.quality_review_status`: `passed`
- `product_market_run.status`: `ran`
- `product_market_run.runner_verdict`: `watch`
- `product_market_run.product_event_count`: `500`
- `product_market_run.conversation_theme_count`: `500`
- `product_market_run.demand_signal_count`: `101`
- `product_market_run.pattern_count`: `4`
- `product_market_run.recommendation_count`: `0`
- `argus_recommendations` count: `1`
- `demand_signals` rendered count: `20`
- `source_health` rendered count: `48`
- Market Field counts: `27` nodes, `26` edges, `1` hotspot, `1` action, `22` proof items.

Public `latest.json`:

- URL: `https://ci.chowmes.com/data/latest.json`
- Bytes: `1741`
- `generated_at`: `2026-07-07T09:00:44`
- This is stale relative to the semantic dashboard and public run status.

## Current Intelligence Rows

Latest `product_market_run_intelligence`:

- `id=154`
- tenant `1`
- verdict `watch`
- created `2026-07-28 13:43:54.703927+00`
- brief begins with Agent Studio demand read and watchlist entries.

Latest `pattern_observations`:

- `312`: `Shopping Assistant`, `competitive_pressure`, confidence `0.580`, created `2026-07-28 13:43:54+00`.
- `311`: `AI Assistant`, `competitive_pressure`, confidence `0.580`, created `2026-07-28 13:43:54+00`.
- `310`: `Agent Studio`, `product_without_market_conversation`, confidence `0.680`, created `2026-07-28 13:43:54+00`.
- `309`: `Documentation`, `competitive_pressure`, confidence `0.580`, created `2026-07-28 13:43:54+00`.

Latest `argus_recommendations`:

- `id=2`
- owner `PMM`
- urgency `this_week`
- status `open`
- confidence `0.680`
- created `2026-07-28 10:26:27+00`
- action: turn shipped Agent Studio capability into an evidence-backed market narrative before the demand window cools.

## Semantic Drift Findings

The current public surfaces contain intelligence-like fields, but they are not yet a proven canonical packet:

1. Public status exposes one current recommendation, but `semantic-dashboard.json.product_market_run.recommendation_count` is `0`.
2. Public status is generated at `2026-07-28T14:31:38Z`, dashboard at `2026-07-28T13:45:06Z`, run health at `2026-07-28T13:37:13Z`, and `latest.json` at `2026-07-07T09:00:44`.
3. The latest scheduled cron run on 2026-07-30 failed before enqueue, so current public intelligence is stale.
4. Dashboard `intelligence_spine.verdict` is `watch`, while `intelligence_spine.can_recommend` is `true`, `next_operator_action` says safe to promote the top recommendation, and `primary_action` is null.
5. The dashboard has only one Market Field hotspot even though the latest run has four recent pattern rows.
6. Weekly synthesis exists in DB only from 2026-07-12 and is not current.
7. Telegram delivery truth is stale at 2026-07-28 even though the active daily job ran and failed on 2026-07-30.

These findings justify Phase 1: one canonical Argus Intelligence Packet must become the source of truth for all consumers.

## Product Question Gap Matrix

| Question | Engine evidence | Dashboard evidence | Telegram evidence | Current judgment |
|---|---|---|---|---|
| What is the main market movement? | patterns and movement map exist | one Market Field hotspot exists | stale latest delivery | partial, stale |
| Which competitors or partners drive it? | leading entities exist | leading entities rendered | stale latest delivery | partial, stale |
| What changed over selected time window? | window comparison objects exist | time-window data exists | no current proof | partial, not live-current |
| Daily, weekly, monthly, or custom movement? | daily and weekly logic exist | UI/data suggests time windows | weekly stale since 2026-07-12 | fail for weekly/current |
| Why does it matter to Algolia? | decision read/top insight exist | top insight rendered | stale latest delivery | partial, semantically inconsistent |
| What should a named team do next? | recommendation row exists | PMM recommendation rendered | stale latest delivery | partial, stale |
| Why is that action prioritized? | scorecard exists | scorecard/evidence rendered | stale latest delivery | partial |
| What evidence supports the read? | evidence refs exist | proof count is nonzero | stale latest delivery | partial |
| What contradicts or weakens it? | not proven in current live output | confidence limits exist but contradiction path not proven | no current proof | fail/unproven |
| What is unknown or confidence-limiting? | confidence limits exist | confidence limits/unknowns exist | stale latest delivery | partial |
| What sources failed and how does trust change? | source health exists | source health rendered | no current proof | partial |
| What should Argus monitor next? | next monitoring actions exist | public status renders actions | stale latest delivery | partial |
| Can I drill into proof without losing the story? | proof graph fragments exist | proof items exist | not applicable | unproven UX |
| Can I switch from Telegram to dashboard and see same run? | delivery rows have report ids | dashboard has run health | latest Telegram stale | fail/currently unproven |
| How do I know Hermes executed and CI-OS produced this? | cron exists but latest run failed | dashboard run health is stale success | latest delivery stale | fail/currently stale |

## Phase 0 Gate Result

Phase 0 truth baseline passes because:

- authoritative CI-OS source and GitHub remote are identified;
- local ChowMes and CI-OS dirty states are classified;
- no active CI-OS tracked source changes are dirty;
- deployed package identity is known;
- live cron, queue, public status, dashboard, DB intelligence, reports, and delivery states are documented;
- the product-question gap matrix exists.

Phase 1 may start only as the Intelligence Packet Contract phase. Runtime repairs, Telegram changes, dashboard implementation, and production release work must not begin before their predecessor gates.

## Blockers Carried Forward

1. The active daily schedule is unhealthy: `cios-v2-daily` failed on 2026-07-30 with queue permission denied.
2. `/opt/cios/app/run-queue` and `/opt/cios/app/out` are not group-writable despite package permission contract expectations.
3. Public CI-OS intelligence is stale since 2026-07-28.
4. Weekly synthesis is stale since 2026-07-12.
5. Telegram delivery is stale since 2026-07-28.
6. Public status, semantic dashboard, run health, DB recommendation count, and `latest.json` do not currently form one run-bound truth.
7. The live product contains intelligence fields but does not yet prove the canonical Argus Intelligence Packet contract.

## Next Gate

Proceed to Phase 1: Intelligence Packet Contract.

The next artifact must decide whether to create a new `ArgusIntelligencePacket` type or evolve the existing `ProductMarketIntelligenceBrief` contract, and it must define the consumer rule for Telegram, dashboard, 3D Market Field, Evidence Lab, Admin, weekly synthesis, and public status.

