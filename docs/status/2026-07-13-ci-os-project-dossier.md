# CI-OS Project Dossier

Date: 2026-07-13; refreshed through 2026-07-28 UTC
Status: Phase 3 passed; Phase 4 Audience Demand active; Market Field UX gate passed
Product owner: Arijit Chowdhury
Operating agent: Argus
Runtime: Hermes / MyOS-Core
First tenant: Algolia

## Executive Position

CI-OS is approximately 45 percent complete against the original product goal. The engineering scaffold is approximately 75 percent complete, but the product does not yet deliver a reliable, evidence-backed competitive decision loop.

The system must not be called launch-ready. Phase 1 passed after two consecutive real Hermes runs completed successfully as the dedicated `cios` application user. Phase 2 passed after fresh public artifacts were published through the Hermes wrapper with one run ID, live public JSON agreed with semantic dashboard data, and live dashboard click validation passed. Phase 3 Product Muscle has now passed: Athos, Bloomreach, Google Vertex AI Search, Lucidworks, and Meilisearch evidence work cleared the Product Muscle queue, and CI-OS now blocks cookie-consent boilerplate before it can enter the Product Muscle ledger. The Market Field-first UX / IA surface is implemented, deployed, served from release `cios-20260728T0934Z-manual-b55979e`, and live-validated on `https://ci.chowmes.com/`. The inward demand plane is connected through the approved manual Looker export path, but Audience Demand is not action-grade: a planned-demand evaluator inspected 12 active Argus topics and 11,057 Looker metric rows, found no matching current demand rows for the active plan, and therefore kept recommendations blocked at zero. The broader Product IA beyond the Market Field journey remains unfinished.

The retained implementation now has a clean, published branch, an immutable deployed package baseline, a verified run-bound publication path, and a live-validated Market Field UX entry point. Feature expansion is now gated on current product evidence, intelligence quality, and the remaining Product IA workflows. Recurring GA4 automation remains deferred and is not the current Phase 3 blocker.

## Product Goal

Argus should be a Hermes-native competitive strategist, not a smaller monitoring dashboard. It must merge three evidence planes:

1. Product reality: what competitors and Algolia actually shipped.
2. Market conversation: what companies, executives, analysts, and the market are saying.
3. Audience demand: what Algolia audiences are reading, searching, comparing, and responding to.

The required output is a defensible answer to:

> Across the last seven days, what did competitors ship, what did they say, what did Algolia's audience respond to, and what should Algolia do next?

Every answer must include evidence, confidence, coverage limitations, owner, urgency, and a specific next action.

## Architecture Boundary

The intended architecture remains correct:

- Hermes core owns schedules, execution, profiles, model routing, delivery, generic memory, and runtime infrastructure.
- Argus is the operating CI agent inside Hermes.
- CI-OS is an independently versioned extension package above Hermes core.
- CI-OS owns tenants, competitors, sources, evidence, intelligence, recommendations, learning, briefs, dashboard state, and admin behavior.
- Scout is the product-surface acquisition layer for changelogs, release notes, docs, pricing, integrations, APIs, and product pages.
- GA4 / Looker is the inward audience-demand layer.
- CI-OS must not modify Hermes core to solve domain problems.

The deployed implementation now enforces the runtime boundary: Hermes owns the schedule, `hermes` may only enqueue, and `cios` owns application execution inside a delegated cgroup. Package release discipline is established for Phase 1, and Phase 2 proved shared run identity plus run-bound publication on the fresh public run `cios-20260728T032901Z-3409872`.

## Verified Live State

Evidence was refreshed directly from Chowmes through 2026-07-28 UTC.

### Hermes run

| Item | Verified state |
|---|---|
| Job | `cios-v2-daily` |
| Schedule | `0 9 * * *`, America/New_York |
| Execution mode | Hermes no-agent script |
| Wrapper | `cios-daily.sh` |
| Latest completed schedules | Phase 1 pair: 2026-07-14 03:49 ET and 04:05 ET; Phase 2 verification run: 2026-07-27 23:29 ET; latest Market Field staging run: 2026-07-28 04:42 ET |
| Request IDs | Phase 1: `a70f4e219d294280a26703962c9be4e9`, `1b938c9de92f4568a059bdb84d3f9e6b`; Phase 2 public run: `cios-20260728T032901Z-3409872`; Phase 3 progress runs: `cios-20260728T034702Z-3433185`, `cios-20260728T041240Z-3510681`, `cios-20260728T043002Z-3533427`, `cios-20260728T044324Z-3552802`; Market Field release: `cios-20260728T084235Z-3769892`; current manual release: `cios-20260728T0934Z-manual-b55979e` |
| Results | Exit code 0 for the Phase 1 pair, the Phase 2 verification run, the latest Phase 3 progress run, and the Market Field staging run |
| Runtime owner | `cios`, reached through the Hermes queue handoff |
| Autonomous daily loop | Publication path, Market Field UX serving, and Phase 3 Product Muscle verified; Phase 4 Audience Demand active |

Both runs completed without root intervention, permission errors, timeout, orphan work, or ownership drift. The systemd service and delegated cgroup were empty after each run, and post-run hashes remained stable. Full evidence is recorded in `docs/status/2026-07-14-ci-os-phase1-hermes-execution-gate.md`.

### Public run status

| Item | Verified state |
|---|---|
| Status | `blocked_on_evidence` |
| Publish status | `published` |
| Generated at | `2026-07-28T09:33:47.175869Z` |
| Public dashboard updated | true |
| Public release | `cios-20260728T0934Z-manual-b55979e` |
| Next Hermes action | `upload_trended_planned_demand_export` |

### Evidence planes

| Plane | Verified state | Meaning |
|---|---:|---|
| Monitored competitors | 27 | Registry exists and is represented publicly. |
| Active sources | 42 | Reported by the latest successful Hermes-wrapper run. |
| Checked sources | 41 fetched | Latest wrapper run fetched 41 of 42 attempted active sources. |
| Blocked sources | 5 | Present in the public source ledger. |
| Failed active source fetches | 1 | Latest wrapper run reported one failed source fetch. |
| Feature-comparison rows | 12 | Latest served semantic dashboard exposes 12 Product Muscle comparison rows. |
| Market Field nodes | 25 | Latest served semantic dashboard exposes 25 Market Field nodes. |
| Product-surface work queue | 0 items | Google Vertex AI Search, Lucidworks, and Meilisearch were extracted and ingested after the Bloomreach pass. |
| Boilerplate extraction guard | Verified | CI-OS commit `b55979e` filters site cookie/privacy boilerplate; the Athos platform extraction that produced 8 bad cookie rows now returns empty. |
| Conversation themes | 500 | Market-conversation evidence exists. |
| Demand signals | 100 | Manual Looker Audience Demand feed is processed, but the latest served status is `processed_no_action_grade_demand`. The Phase 4 evaluator inspected 12 active planned topics and 11,057 Looker metric rows; no planned topic had matching current demand rows. |
| Patterns | 2 | Deterministic pattern primitives produced output in the latest fresh run. |
| Recommendations | 0 | No promoted action; latest served state remains blocked on action-grade Audience Demand. |
| Consumed learnings | 0 | Learning effect on the current run is not proven. |

Blocking the recommendation plane while Audience Demand is not action-grade is the correct behavior. The demand plane is connected for the pilot through the manual Looker export path, but the current export is not action-grade for the active Argus plan. The latest Phase 4 evaluator found off-plan Agent Studio movement, but that does not satisfy the current gate unless the Argus demand plan is explicitly refreshed or amended. The next required demand action is a planned export with current and previous seven-day values for the active topics, or a deliberate plan refresh that makes the validated off-plan demand part of the work order. Recurring GA4 automation remains deferred.

## Repository State

Verified local CI-OS repository state:

| Item | State |
|---|---|
| Branch | `codex/ci-os-phase1-runtime` |
| Branch documentation head | `dea1816` |
| Deployed code commit | `1fa7ac5` |
| Git remote | `https://github.com/arijitchowdhury80/algolia-competitive-intelligence.git` |
| Tracked files changed | 0 |
| Tracked diff | 0 |
| Untracked source files | 0 |
| Full local test suite | 1,251 passed, 3 skipped, 23 deselected |
| Whitespace check | Passed |
| Deployed package mapping | Immutable archive maps to `1fa7ac5` |

The test suite and two live runs prove the Phase 1 runtime contract. They do not yet prove Phase 2 atomic publication, Product Muscle completeness, demand evidence, intelligence usefulness, UI usability, or pilot readiness.

The authoritative remote and branch ownership are reconciled. Commit `dea1816` adds the verified Phase 1 workflow record only; it does not change the deployed code. The deployed archive is `/opt/cios/releases/1fa7ac5.tar.gz` with SHA-256 `63b3c56e7129c8c710e895d29c72a57c02986ef92bdfa10afbe162b275da255c`; its rollback-bundle drill passed without changing the live service.

## Implemented Capability Inventory

### Substantially implemented

- Multi-tenant Postgres schema and repositories.
- Tenant, competitor, source, source-health, and product-surface registries.
- Competitor/source add, edit, pause, retire scaffolding in local admin.
- Evidence ledger and source provenance structures.
- Product events, capability positions, conversation themes, demand signals, patterns, recommendations, and scorecards.
- Source failure classification and blocked-source handling.
- Competitor-specific brief generation and routes.
- Public monitored-competitor roster.
- Product muscle work queues and demand work orders.
- Manual demand upload and GA4 readiness controls.
- Learning event, challenge, proposal, and apply-plan artifacts.
- Hermes package wrapper and cron registration.
- Reliable Hermes-owned execution through the dedicated `cios` application user.
- Public dashboard renderer, Market Field-first live UX, and selected Playwright interaction checks.

### Partially implemented or unproven

- Current-run Scout product-surface extraction.
- Product feature comparison across every active competitor.
- GA4 / Looker ingestion with validated demand coverage.
- Cross-plane synthesis from product, conversation, and demand.
- Recommendation promotion with human-usable action detail.
- Learning that changes a later run.
- Multi-channel delivery through Hermes rather than duplicated paths.
- Complete competitor onboarding from admin through first successful sweep.
- Historical validity and seven-day / thirty-day pattern views.
- Public release safety and atomicity.

### Not delivered to product standard

- Broader production Argus Read beyond the Market Field entry point.
- Production Product Muscle Matrix.
- Production Conversation Heatmap.
- Production Demand Lens.
- Production Pattern Board.
- Production Actions workflow.
- Coherent Competitor Registry journey.
- Coherent Evidence Lab.
- Coherent Argus Command and Admin separation.
- Exhaustive UI, accessibility, semantic, and live-data E2E validation.

## Completion Assessment

| Workstream | Completion | Current judgment |
|---|---:|---|
| Hermes extension boundary | Phase 1 passed | Hermes schedules, `hermes` enqueues, and `cios` executes without modifying Hermes core. |
| Hermes scheduled execution | Phase 1 passed | Two consecutive real runs exited 0 with clean containment and ownership. |
| Competitor and source registry | 55% | Data/admin/public roster exist; onboarding proof incomplete. |
| Daily outward collection | 55% | Coverage can be reported and the latest Hermes-wrapper publication run exited 0. |
| Scout product muscle | Phase 3 passed | Product Muscle queue is zero after Athos, Bloomreach, Google Vertex AI Search, Lucidworks, and Meilisearch evidence work; cookie-boilerplate pollution is blocked. |
| GA4 / Looker demand | 60% | Manual Looker export is processed with 100 demand signals, but no active planned topic has action-grade movement; recurring GA4 automation is deferred. |
| Pattern intelligence | 30% | Patterns exist; cross-plane validation is incomplete. |
| Recommendations | 10% | Structures exist; current output is zero. |
| Frontend IA and usability | 40% | Market Field-first entry point is live and validated; broader Product IA workflows remain unfinished. |
| History, heatmap, semantic views | 30% | Surfaces exist; business validity is not acceptance-tested. |
| Learning loop | 25% | Artifacts exist; downstream run impact is unproven. |
| E2E and launch validation | 45% | Broad tests exist; live click validation now passes, but full launch validation remains open. |
| Version control and release hygiene | 70% | Clean branch, deployed baseline, Phase 2 status evidence, and renderer hotfix backup exist; production still needs full release-recorded deploy discipline. |

Weighted product completion: approximately 45 percent.

## Critical Code And Operational Findings

### P0

1. Hermes runtime ownership is broken. Root/manual runs recreate files Hermes cannot replace.
2. The daily wrapper can recursively delete an unsafe configured output path.
3. Public publication is not atomic and can expose a partial artifact set as published.
4. The current repository state cannot be audited or rolled back as a coherent release.

### P1 correctness and security

1. Public safety is self-attested rather than derived from a final artifact scan.
2. Launch validation accepts PASS substrings from arbitrary logs.
3. Launch validation does not bind all artifacts to one fresh run identity.
4. Product readiness can pass from historical event counts when current extraction did no work.
5. The existing Playwright suite checks a selected subset, not every interaction or competitor.
6. Admin writes are allowed without a token when the token is unset.
7. Source creation does not prove competitor ownership by the same tenant.
8. Repeated demand uploads can overwrite evidence with the same basename.
9. A GA4 plan sidecar can be scanned as demand evidence.
10. Package verification tests paths and text, not executable behavior.
11. Admin product-surface subprocesses lack an outer timeout.
12. Direct runner defaults diverge from the current Gemini production policy.

## User And Business Gaps

The present product still does not clearly answer:

- What changed across the whole monitored market, not only one selected competitor?
- What was actually shipped versus merely said?
- What themes are accelerating, cooling, or converging over time?
- Where is Algolia strong, behind, silent, or over-positioned?
- What does Algolia's audience behavior validate or contradict?
- Why is one competitor or action prioritized over another?
- What confidence rubric and evidence produced that judgment?
- What should a PMM, Product, Sales, Content, or executive owner do next?
- What did Argus learn, and how did that learning change the next run?

Without these answers, the application remains monitoring and plumbing rather than a Competitive Intelligence Operating System.

## Remaining Deliverables

1. Safe staging, atomic publication, current-run identity, and trustworthy launch evidence.
2. A real GA4 or Looker demand source with topic coverage and time-series signals.
4. Cross-plane patterns with explicit support, contradiction, confidence, and unknowns.
5. Specific recommendations with owner, urgency, evidence, and generated work products.
6. A proven learning loop whose instruction changes the following run.
7. The accepted Argus Product Muscle IA implemented as one coherent product.
8. Exhaustive backend, frontend, accessibility, semantic, security, and live cron E2E validation.
9. A clean, versioned, reviewable release and an evidence-backed pilot gate.

## Dependencies And Decisions

### Required from Arijit

- Provide or authorize a GA4 / Looker export or connector for the Algolia tenant.
- Confirm who may access public CI-OS status versus internal evidence and admin data.
- Approve the first human-reviewed recommendation as useful enough to operationalize.

### System dependencies

- Hermes runtime and cron.
- CI-OS extension package.
- Scout acquisition and extraction.
- Postgres evidence ledger.
- Gemini model route.
- Algolia GA4 / Looker evidence.
- Public dashboard and local/authenticated admin.

## Definition Of Done

CI-OS is complete for the Algolia pilot only when all of the following are true:

- One scheduled Hermes run completes as Hermes with exit 0 and no orphan work.
- All active sources are checked or explicitly skipped with reason.
- Scout extracts current product evidence across the required competitor set.
- Demand evidence is processed and coverage is visible.
- One fresh run produces a defensible seven-day cross-plane read.
- At least one recommendation is specific, evidence-backed, and accepted by its intended owner.
- Every public click and admin journey reaches the correct entity and action.
- Every displayed data point traces to current-run evidence.
- Keyboard, accessibility, responsive, semantic, and security gates pass.
- Public publication is atomic and public-safe.
- A saved learning demonstrably changes the next successful run.
- The exact deployed package is versioned, reviewable, and reproducible.

## Canonical Supporting Records

- `docs/audits/2026-07-13-ci-os-forensic-status-review.md`
- `docs/decisions/2026-07-13-ci-os-recovery-boundary.md`
- `docs/plan/argus-product-muscle-ia.md`
- CI-OS repository: `docs/plan/e2e-validation.md`
- CI-OS repository: `docs/workspace/cios-intelligence-core/_status.md`
- `docs/status/2026-07-28-ci-os-phase3-product-muscle-progress.md`

## Documentation And Bible Publication

Completed on 2026-07-13:

- Updated the canonical MyOS Competitive Intelligence index and workspace state.
- Updated the Second Brain CI-OS index, task ledger, status, dossier, and completion plan.
- Updated the cross-project tracker with the current CI-OS recovery state while preserving a concurrent Algolia-Central2 tracker update.
- Added the dossier and completion plan to the CI-OS repository documentation.
- Added and tested the canonical Bible route `/ci-os`.
- Made `status.md` the CI-OS Bible landing document.
- Published the public-safe CI-OS status, phase tracker, and completion plan.
- Escaped raw HTML in vault Markdown and removed dynamic `innerHTML` use from Bible search rendering.
- Added a CI-OS public-file allowlist. Only `status.md`, `tracker.md`, and `completion-plan.md` are discoverable or retrievable; the internal index, log, task ledger, doctrine, and full dossier return 404.
- Kept the latest internal task ledger and full internal dossier out of the public mirror.

Live public page: `https://bible.chowmes.com/ci-os`
