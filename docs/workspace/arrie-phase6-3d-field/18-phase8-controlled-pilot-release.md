# Phase 8 Controlled Pilot Release

Date: 2026-07-28
Status: released to controlled monitored pilot; observation window active

## Release

- Pilot release ID: `cios-pilot-algolia-20260728-b4d7423`
- CI-OS package commit: `b4d7423cff92b719dd48bc4b34af0ff21faefc16`
- CI-OS branch: `codex/ci-os-phase0-baseline`
- Package path: `/opt/cios/app`
- Runtime owner: `cios`
- Public URL: `https://ci.chowmes.com/`

## Versioned Bundle

- Release bundle: `/opt/cios/releases/b4d7423.tar.gz`
- SHA-256: `4ef05bc3466ffc36d4729eb2a375973a2128ba9f9ae0f71e32a25417b441cc31`
- Previous release bundle: `/opt/cios/releases/47ef4d5.tar.gz`
- Source release verification: package contract passed with Python imports skipped.
- Deployed package verification: package contract passed with app virtualenv.

## Rollback

- Rollback bundle: `/opt/cios/releases/rollback-before-phase8-20260728T141016Z-pre-2b88539.tar.gz`
- Rollback bundle size: `47M`
- Rollback test: extracted to a temporary directory and passed package contract with Python imports skipped.

## Live Verification

The deployed package passed:

- Package contract.
- Live operational safety.
- Public artifact redaction.
- Public artifact safety scan.
- Live dashboard click validation.
- Aggregate launch readiness.
- Controlled pilot monitoring.

## Monitoring State

`scripts/check_pilot_monitoring.py` is now part of the package contract and produced:

- `status`: `pass`
- Source coverage: `42` active, `42` checked, `4` failed
- Source failure ratio: `0.0952`, below the controlled-pilot ceiling `0.10`
- Audience demand: `101` demand signals
- Demand plan coverage: `1 / 12`
- Product reality: `500` product events
- Product-surface failed captures: `3`
- Pattern count: `4`
- Next monitoring actions: `2`
- Current recommendation count in public run status: `1`
- Current recommendation owner: `PMM`
- Current recommendation action: turn the shipped Agent Studio capability into an evidence-backed market narrative before the demand window cools.

Monitoring debt preserved:

- Public status is `limited_by_evidence`.
- Demand plan is missing `11` of `12` planned topics.
- `4` active sources failed this run.
- `3` product-surface captures failed.
The earlier public-status `recommendation_count=0` was corrected in CI-OS commit `b4d7423cff92b719dd48bc4b34af0ff21faefc16`. The live public URL now exposes one sanitized current recommendation.

Next Hermes action:

> Run product-surface extraction for Athos Commerce, then refresh Argus from the evidence ledger to resolve the A/B Testing matrix cell.

## Public And Internal Boundaries

Public pilot surface:

- `https://ci.chowmes.com/`
- Public status JSON under `/data/`
- Public-safe dashboard and brief artifacts only.

Internal/admin boundaries:

- CI-OS admin remains localhost-only.
- Package and runtime files remain owned by `cios:hermes`.
- Hermes core remains unchanged.
- Secrets, host paths, raw private files, and internal staging directories are excluded from public artifacts by redaction and safety scans.

## Pilot Operating Plan

Pilot users:

- Arijit: product owner and usefulness judge.
- Product Marketing reviewer: validate whether the Argus read is usable as a PMM narrative/action input.
- Evidence auditor role: spot-check cited evidence, unknowns, and confidence limitations.

Cadence:

- Daily automated CI-OS run on the existing Hermes schedule.
- Daily monitor check from `scripts/check_pilot_monitoring.py`.
- Review after each generated Argus read during the observation window.

Observation window:

- Start: 2026-07-28
- Minimum window before completion claim: three successful daily observations or an explicit shorter acceptance by Arijit after real use.

Feedback rubric:

- Is the top read understandable without explanation?
- Is every claim source-backed?
- Are unknowns and limitations visible?
- Is there a named owner or team?
- Is the action specific enough to use?
- Did the read change, confirm, or reject a real GTM/Product/Content decision?
- Did Argus learn from acceptance, rejection, or correction?

Decision owners:

- Product Marketing: narrative and positioning actions.
- Product: product capability or gap investigation.
- Sales Enablement: talk track and competitive-response actions.
- Executive Review: high-materiality or low-confidence strategic calls.

## Exit Judgment

The controlled Algolia pilot is released and monitored.

The full Phase 8 exit gate is not yet complete. It requires repeatable trusted decisions during the observation window and at least one real team use of an Argus recommendation.
