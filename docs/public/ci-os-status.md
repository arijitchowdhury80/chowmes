---
title: CI-OS Project Status
type: project-status
status: phase-8-controlled-pilot-released
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

Current product completion is approximately **80 percent**. The engineering scaffold is approximately **90 percent** complete. CI-OS is released to a controlled monitored pilot, with observation still active.

## What Has Been Built

- Hermes extension package and Argus operating model.
- Multi-tenant competitor and source registry.
- Source collection and evidence ledger.
- Product event, conversation, demand, pattern, recommendation, and learning models.
- Competitor-specific briefs and monitored-competitor views.
- Product Muscle and demand work queues.
- Local administration for competitors, sources, product surfaces, demand, and runs.
- Dashboard renderer, Market Field-first live UX, and selected browser-validation journeys.
- 1,251 passing local tests in the latest broad verified suite, plus 81 focused Phase 5 learning-gate tests.
- Dedicated `cios` application user, secure Hermes queue handoff, and delegated cgroup containment.
- Run-bound public publication through the Hermes wrapper and served release store.
- Manual Audience Demand ingestion from the approved Looker export path.
- Accepted Agent Studio recommendation review packet and package-scoped learning policy.

## Current Verified State

| Area | Status | Current evidence |
|---|---|---|
| Phase 0 baseline | Passed | Clean, published CI-OS recovery baseline. |
| Phase 1 Hermes execution | Passed | Two consecutive real Hermes runs exited 0 as `cios`, with no permission error, timeout, orphan work, or ownership drift. |
| Phase 2 publication | Passed | Fresh public run `cios-20260728T032901Z-3409872` published through the Hermes wrapper with matching public status and semantic dashboard run IDs. |
| Deployed package | Verified | CI-OS commit `2a4923973857ac035ba53b58168792ffb85c3fa2` is deployed at `/opt/cios/app`; package contract passed as `cios`. |
| Competitor registry | Partial | 27 competitors represented. |
| Source coverage | Current with controlled-pilot limitation | Latest Hermes wrapper run reported 42 active sources, 42 checked, 38 fetched, and 4 failed source fetches. This passes the controlled-pilot ratio policy, `0.0952 <= 0.10`, but remains a visible limitation. |
| Product reality | Passed for Phase 3 | Product Muscle queue is now `0` after verified Google Vertex AI Search, Lucidworks, Meilisearch, Bloomreach, and Athos evidence work. The latest served semantic dashboard has 12 feature-comparison rows and explicit unknown states where proof is absent. |
| Market conversation | Present | 500 themes and 2 current candidate patterns. |
| Audience demand | Passed with limited confidence | Agent Studio was explicitly accepted into the Argus demand plan, imported into the demand ledger, and refreshed. The live run now reports 101 demand signals, 1 rising demand topic, and partial plan coverage. Confidence remains limited because the accepted trend compares comparable but not identical Looker export families. |
| Recommendations | Phase 5 passed with confidence caveat; Phase 8 observation active | The live public status now exposes one current PMM recommendation: turn the shipped Agent Studio capability into an evidence-backed market narrative before the demand window cools. |
| Learning | Phase 5 proof passed | Acceptance was recorded as learning event `2` and approved improvement `3`; next-sweep plan, apply plan, approved policy, and policy audit are publicly available. |
| Production UI | Phase 6 passed for controlled pilot | Market Field-first Product IA is live at `https://ci.chowmes.com/`, public artifact redaction and safety scan passed, and live click validation passed across desktop, tablet, and mobile. |
| Launch readiness | Controlled pilot released | Package contract, operational safety, public redaction, public safety scan, live dashboard click validation, aggregate E2E launch readiness, human usefulness acceptance, rollback preservation, and pilot monitoring passed. Observation window is active. |

## What Comes Next

1. Run the controlled pilot observation window.
2. Record whether a named team uses, rejects, or amends an Argus recommendation.
3. Preserve monitoring debt: partial demand-plan coverage, 4 failed source fetches, and 3 product-surface failed captures.

## Next Gate

Phase 7 technical validation and human usefulness acceptance have passed. CI-OS is released to the Phase 8 controlled Algolia pilot observation window.

The latest served package is `2a4923973857ac035ba53b58168792ffb85c3fa2`. Agent Studio was explicitly amended into the Argus demand plan, imported as a traceable demand signal, refreshed into one recommendation, accepted by Arijit, and recorded into an approved learning policy. The current live public status exposes one open PMM recommendation for pilot-window disposition, and the package publishes `https://ci.chowmes.com/data/phase8/argus-pmm-narrative-brief.md` as the Product Marketing draft work artifact plus `/opt/cios/app/out/phase8/cios-phase8-exit.json` as the formal exit gate. The daily wrapper now republishes the PMM artifact through the staged public release path whenever a current reviewable recommendation exists. That gate currently fails only because disposition is still pending. Phase 4 and Phase 5 are treated as passed with limited confidence, not perfect coverage. Phase 6 is passed for the controlled pilot with a temporary design-authority waiver. Phase 7 is passed. Phase 8 release is live, with observation still required before the full goal can close. Recurring GA4 automation remains deferred.

## Project Records

- [[tracker|Open the current phase tracker]]
- [[completion-plan|Read the full completion plan]]
