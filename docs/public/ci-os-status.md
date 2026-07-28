---
title: CI-OS Project Status
type: project-status
status: phase-3-product-muscle
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
| Deployed package | Verified | CI-OS commit `54b5d2f` is deployed at `/opt/cios/app`; package contract passes as `cios`. |
| Competitor registry | Partial | 27 competitors represented. |
| Source coverage | Current with one fetch failure | Latest Hermes wrapper run reported 42 active sources, 41 fetched, and 1 failed source fetch. |
| Product reality | Partial | Phase 3 has verified Product Muscle progress, but the latest served public state is still blocked on evidence and has `0` promoted recommendations. |
| Market conversation | Present | 500 themes and 2 current candidate patterns. |
| Audience demand | Connected manual feed | Fresh semantic data reports `demand_plane_status=processed` and `demand_signal_count=100`; recurring GA4 automation remains deferred. |
| Recommendations | Blocked | 0 current recommendations because Product Muscle evidence is still incomplete. |
| Learning | Unproven | No learning effect visible in the current run. |
| Production UI | Market Field live gate passed | Market Field-first UX is live at `https://ci.chowmes.com/` and passed live click validation on release `cios-20260728T084235Z-3769892`; broader Product IA remains pending. |
| Launch readiness | Not ready | Market Field UX and publication are live-verified, but Product Muscle, Argus recommendation quality, broader IA, and final E2E gates remain open. |

## What Comes Next

1. Complete Scout-backed product and feature comparison.
2. Keep the manual Audience Demand feed as the pilot input while recurring GA4 automation is deferred.
3. Prove one useful cross-plane Argus recommendation and one learning effect.
4. Complete the remaining Product IA workflows beyond the live Market Field journey: Product Muscle Matrix, Conversation/Demand drilldowns, Pattern Board, Actions, Registry, Evidence Lab, and Command/Admin.
5. Complete exhaustive frontend, backend, semantic, accessibility, security, and live-cron validation.
6. Release a controlled Algolia pilot only after every gate passes.

## Next Gate

Phase 3 is active. Product Muscle must produce current evidence or explicit unknown states for every active competitor and matrix cell.

The next live actions are to inspect why the latest served run is `blocked_on_evidence` with `0` promoted recommendations, then continue the remaining Product Muscle evidence work. Recurring GA4 automation is deferred and does not block Phase 3.

## Project Records

- [[tracker|Open the current phase tracker]]
- [[completion-plan|Read the full completion plan]]
