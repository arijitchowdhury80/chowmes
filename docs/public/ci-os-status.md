---
title: CI-OS Project Status
type: project-status
status: phase-5-argus-intelligence
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

Current product completion is approximately **55 percent**. The engineering scaffold is approximately **80 percent** complete. CI-OS is **not launch-ready**.

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
| Deployed package | Verified | CI-OS commit `fa2f31f` is deployed for the demand-amendment handoff integration; package contract and source compile checks passed as `cios`. |
| Competitor registry | Partial | 27 competitors represented. |
| Source coverage | Current with one fetch failure | Latest Hermes wrapper run reported 42 active sources, 41 fetched, and 1 failed source fetch. |
| Product reality | Passed for Phase 3 | Product Muscle queue is now `0` after verified Google Vertex AI Search, Lucidworks, Meilisearch, Bloomreach, and Athos evidence work. The latest served semantic dashboard has 12 feature-comparison rows and explicit unknown states where proof is absent. |
| Market conversation | Present | 500 themes and 2 current candidate patterns. |
| Audience demand | Passed with limited confidence | Agent Studio was explicitly accepted into the Argus demand plan, imported into the demand ledger, and refreshed. The live run now reports 101 demand signals, 1 rising demand topic, and partial plan coverage. Confidence remains limited because the accepted trend compares comparable but not identical Looker export families. |
| Recommendations | Phase 5 review active | The live run now has 1 recommendation: turn the shipped Agent Studio capability into an evidence-backed market narrative before the demand window cools. Human acceptance is still required before Phase 5 can pass. |
| Learning | Unproven | No learning effect visible in the current run. |
| Production UI | Market Field live gate passed | Market Field-first UX is live at `https://ci.chowmes.com/` and passed live click validation on release `cios-20260728T102723Z-manual-d6d4b6e`; broader Product IA remains pending. |
| Launch readiness | Not ready | Product Muscle, Audience Demand, and Market Field publication are live-verified, but Argus recommendation acceptance, broader IA, and final E2E gates remain open. |

## What Comes Next

1. Review the generated Agent Studio recommendation for accuracy, novelty, and direct usefulness to a named team.
2. If accepted, record the accepted recommendation and create the learning instruction required by Phase 5.
3. If rejected or amended, record the reason and rerun Argus with the corrected learning or evidence requirement.
4. Complete the remaining Product IA workflows beyond the live Market Field journey: Product Muscle Matrix, Conversation/Demand drilldowns, Pattern Board, Actions, Registry, Evidence Lab, and Command/Admin.
5. Complete exhaustive frontend, backend, semantic, accessibility, security, and live-cron validation.
6. Release a controlled Algolia pilot only after every gate passes.

## Next Gate

Phase 5 is active. Argus must prove one accepted cross-plane recommendation and one auditable learning effect.

The latest served release is `cios-20260728T102723Z-manual-d6d4b6e`. Agent Studio was explicitly amended into the Argus demand plan, imported as a traceable demand signal, and refreshed into one recommendation. Phase 4 is treated as passed with limited confidence, not perfect coverage: the live readiness state is `processed_partial_plan_coverage`, with 1 of the planned topics covered by rising demand. Recurring GA4 automation remains deferred.

## Project Records

- [[tracker|Open the current phase tracker]]
- [[completion-plan|Read the full completion plan]]
