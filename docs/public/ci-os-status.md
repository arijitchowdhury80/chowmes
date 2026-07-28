---
title: CI-OS Project Status
type: project-status
status: phase-4-audience-demand
updated: 2026-07-28
---

# CI-OS Project Status

Last verified: 2026-07-28 UTC

## Current Position

CI-OS is an Algolia-first Competitive Intelligence Operating System operated by Argus on Hermes. It is designed to connect three kinds of evidence:

1. What competitors shipped.
2. What the market is saying.
3. What Algolia audiences are responding to.

The target output is an evidence-backed recommendation for Product, Product Marketing, Sales, Content, or executive teams.

Current product completion is approximately **45 percent**. The engineering scaffold is approximately **75 percent** complete. CI-OS is **not launch-ready**.

## What Has Been Built

- Hermes extension package and Argus operating model.
- Multi-tenant competitor and source registry.
- Source collection and evidence ledger.
- Product event, conversation, demand, pattern, recommendation, and learning models.
- Competitor-specific briefs and monitored-competitor views.
- Product Muscle and demand work queues.
- Local administration for competitors, sources, product surfaces, demand, and runs.
- Dashboard renderer, Market Field-first live UX, and selected browser-validation journeys.
- 1,251 passing local tests in the latest verified suite.
- Dedicated `cios` application user, secure Hermes queue handoff, and delegated cgroup containment.
- Run-bound public publication through the Hermes wrapper and served release store.
- Manual Audience Demand ingestion from the approved Looker export path.

## Current Verified State

| Area | Status | Current evidence |
|---|---|---|
| Phase 0 baseline | Passed | Clean, published CI-OS recovery baseline. |
| Phase 1 Hermes execution | Passed | Two consecutive real Hermes runs exited 0 as `cios`, with no permission error, timeout, orphan work, or ownership drift. |
| Phase 2 publication | Passed | Fresh public run `cios-20260728T032901Z-3409872` published through the Hermes wrapper with matching public status and semantic dashboard run IDs. |
| Deployed package | Verified | CI-OS commit `b55979e` is deployed for the product-surface exporter; package source compile-check passed as `cios`. |
| Competitor registry | Partial | 27 competitors represented. |
| Source coverage | Current with one fetch failure | Latest Hermes wrapper run reported 42 active sources, 41 fetched, and 1 failed source fetch. |
| Product reality | Passed for Phase 3 | Product Muscle queue is now `0` after verified Google Vertex AI Search, Lucidworks, Meilisearch, Bloomreach, and Athos evidence work. The latest served semantic dashboard has 12 feature-comparison rows and explicit unknown states where proof is absent. |
| Market conversation | Present | 500 themes and 2 current candidate patterns. |
| Audience demand | Connected but not action-grade | Fresh semantic data reports `demand_plane_status=processed` and `demand_signal_count=100`, but no topic crossed the rising-demand threshold. A planned-demand evaluation inspected 12 active Argus topics and 11,057 Looker metric rows; no active planned topic had matching current demand rows. The evaluator now emits one amendment candidate: Agent Studio, with 1,619 current sessions versus 751 previous sessions. The current next action is `upload_trended_planned_demand_export` or explicitly amend the demand plan. |
| Recommendations | Blocked | 0 current recommendations because the current demand feed is not yet action-grade. |
| Learning | Unproven | No learning effect visible in the current run. |
| Production UI | Market Field live gate passed | Market Field-first UX is live at `https://ci.chowmes.com/` and passed live click validation on release `cios-20260728T0934Z-manual-b55979e`; broader Product IA remains pending. |
| Launch readiness | Not ready | Product Muscle and Market Field publication are live-verified, but Audience Demand, Argus recommendation quality, broader IA, and final E2E gates remain open. |

## What Comes Next

1. Replace or enrich the manual Audience Demand feed with planned topic mapping plus previous-period or `change_pct` values for the active Argus topics, or explicitly refresh the demand plan to include the observed off-plan Agent Studio demand.
2. Refresh Argus and prove that Audience Demand either becomes action-grade or remains explicitly blocked.
3. Prove one useful cross-plane Argus recommendation and one learning effect.
4. Complete the remaining Product IA workflows beyond the live Market Field journey: Product Muscle Matrix, Conversation/Demand drilldowns, Pattern Board, Actions, Registry, Evidence Lab, and Command/Admin.
5. Complete exhaustive frontend, backend, semantic, accessibility, security, and live-cron validation.
6. Release a controlled Algolia pilot only after every gate passes.

## Next Gate

Phase 4 is active. Audience Demand must provide planned-topic time-series evidence, either through a trended manual Looker export or a configured GA4 path.

The latest served run is `blocked_on_evidence` with `0` promoted recommendations because demand movement is not action-grade. The local Phase 4 evaluator found no matching current demand rows for the 12 active planned topics. It did find off-plan Agent Studio movement, but that cannot pass the gate unless Argus explicitly plans against it. The next live action is to upload a trended planned demand export with previous-period or `change_pct` values, or refresh the Argus demand plan, then refresh Argus. Recurring GA4 automation remains deferred; the immediate blocker is the missing action-grade planned demand movement, not the connector itself.

## Project Records

- [[tracker|Open the current phase tracker]]
- [[completion-plan|Read the full completion plan]]
