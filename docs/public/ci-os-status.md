---
title: CI-OS Project Status
type: project-status
status: recovery
updated: 2026-07-13
---

# CI-OS Project Status

Last verified: 2026-07-13

## Current Position

CI-OS is an Algolia-first Competitive Intelligence Operating System operated by Argus on Hermes. It is designed to connect three kinds of evidence:

1. What competitors shipped.
2. What the market is saying.
3. What Algolia audiences are responding to.

The target output is an evidence-backed recommendation for Product, Product Marketing, Sales, Content, or executive teams.

Current product completion is approximately **35 percent**. The engineering scaffold is approximately **65 percent** complete. CI-OS is **not launch-ready**.

## What Has Been Built

- Hermes extension package and Argus operating model.
- Multi-tenant competitor and source registry.
- Source collection and evidence ledger.
- Product event, conversation, demand, pattern, recommendation, and learning models.
- Competitor-specific briefs and monitored-competitor views.
- Product Muscle and demand work queues.
- Local administration for competitors, sources, product surfaces, demand, and runs.
- Dashboard renderer and selected browser-validation journeys.
- 1,184 passing local tests in the latest verified suite.

## Current Verified State

| Area | Status | Current evidence |
|---|---|---|
| Phase 0 baseline | Passed | Clean CI-OS branch at `149e63c`; deployed package mapped to `13731ac` plus non-code status-note drift. |
| Hermes daily execution | Blocked | Latest scheduled run failed because runtime output ownership drifted. |
| Competitor registry | Partial | 27 competitors represented. |
| Source coverage | Partial | 43 active sources reported checked; latest successful autonomous cycle is not proven. |
| Product reality | Partial | 12 historical product events; current product-surface extraction is not proven. |
| Market conversation | Present | 500 themes and 3 candidate patterns. |
| Audience demand | Blocked | No ready GA4 / Looker source; 0 demand signals. |
| Recommendations | Blocked | 0 current recommendations because required evidence is incomplete. |
| Learning | Unproven | No learning effect visible in the current run. |
| Production UI | In redesign | Accepted Product Muscle IA is not yet the live application. |
| Launch readiness | Failed | Public run status is blocked and the dashboard was not updated by the latest run. |

## What Comes Next

1. Restore Hermes-owned scheduled execution.
2. Make publication atomic, current-run bound, and safety-validated.
3. Complete Scout-backed product and feature comparison.
4. Connect GA4 / Looker audience-demand evidence.
5. Prove one useful cross-plane Argus recommendation and one learning effect.
6. Build the accepted Argus Read, Product Muscle Matrix, Conversation Heatmap, Demand Lens, Pattern Board, Actions, Registry, Evidence Lab, and Command/Admin workflows.
7. Complete exhaustive frontend, backend, semantic, accessibility, security, and live-cron validation.
8. Release a controlled Algolia pilot only after every gate passes.

## Next Gate

The immediate gate is deliberately narrow: repair runtime ownership, harden output handling, and prove a complete scheduled Hermes run with no root intervention.

No additional product feature work should begin before that gate passes.

## Project Records

- [[tracker|Open the current phase tracker]]
- [[completion-plan|Read the full completion plan]]
