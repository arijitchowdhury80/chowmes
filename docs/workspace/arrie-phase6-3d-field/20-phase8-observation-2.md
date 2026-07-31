# Phase 8 Observation 2

Date: 2026-07-28
Status: observation recorded; full Phase 8 exit still open

## Source

Observation 2 is based on the corrected live controlled-pilot release and public URL:

- Public URL: `https://ci.chowmes.com/data/argus-latest-run-status.json`
- Live served path: `/opt/cios/public-store/served/data/argus-latest-run-status.json`
- Pilot monitor artifact: `/opt/cios/app/out/cios-pilot-monitoring.json`
- Review packet: `/opt/cios/app/out/phase8/argus-recommendation-review-packet.json`
- Release record: `/opt/cios/app/out/cios-controlled-pilot-release.json`
- Release ID: `cios-pilot-algolia-20260728-b4d7423`
- Package commit at observation time: `b4d7423cff92b719dd48bc4b34af0ff21faefc16`
- Current follow-up release with disposition handoff: `63f819b649fedf2625fad126dcd776fb5fe66788`

## Correction From Observation 1

Observation 1 found that the public status reported `recommendation_count=0` even though the live dashboard contained one open Argus recommendation. CI-OS commit `b4d7423cff92b719dd48bc4b34af0ff21faefc16` corrected the public-status and review-packet path:

- Public status now counts current open `argus_recommendations`.
- Public status now exposes sanitized `current_recommendations`.
- Recommendation review packets now fall back to the live open recommendation when the stale intelligence spine has no primary action.
- The review packet rationale now comes from the live recommendation when the recommendation supplies the action.

## Monitor Verdict

- Controlled pilot monitoring: `pass`
- Aggregate launch readiness: `pass`
- Live operational safety: `passed`
- Public artifact redaction: `redacted`
- Public artifact safety scan: `passed`
- Live dashboard click validation: `PASS dashboard_click_validation`
- Package contract: `PASS: CI-OS Hermes package contract satisfied`

## Evidence Snapshot

- Public status: `limited_by_evidence`
- Publish status: `published`
- Active sources: `42`
- Checked sources: `42`
- Failed active sources: `4`
- Failed-source ratio: `0.0952`
- Demand signals: `101`
- Demand plan coverage: `1 / 12`
- Product events: `500`
- Product-surface failed captures: `3`
- Pattern count: `4`
- Next monitoring actions: `2`
- Current public recommendation count: `1`

## Current Recommendation

- Recommendation ID: `2`
- Owner: `PMM`
- Urgency: `this_week`
- Confidence: `0.68`
- Action: Turn the shipped Agent Studio capability into an evidence-backed market narrative before the demand window cools.
- Why now: Product reality and audience demand align, but the captured conversation does not yet explain the capability.
- Public evidence URL count: `3`

## Monitoring Debt

- Public status is `limited_by_evidence`.
- Demand plan is missing `11` of `12` planned topics.
- `4` active sources failed this run.
- `3` product-surface captures failed.

## Usage Status

The pilot now has a current, public, named-owner recommendation. Full Phase 8 exit still requires explicit pilot-window disposition by a named team or owner:

- use the recommendation in real work,
- reject it with reason, or
- amend it with a correction that CI-OS records as learning.

No new pilot-window use, rejection, or amendment is recorded in this observation.

## Release Bundle

- Release bundle: `/opt/cios/releases/b4d7423.tar.gz`
- SHA-256: `4ef05bc3466ffc36d4729eb2a375973a2128ba9f9ae0f71e32a25417b441cc31`

## Next Observation

Run the next scheduled CI-OS daily cycle, then rerun:

```bash
/opt/cios/app/.venv/bin/python /opt/cios/app/scripts/check_pilot_monitoring.py \
  --public-status /opt/cios/public-store/served/data/argus-latest-run-status.json \
  --launch-readiness /opt/cios/app/out/cios-e2e-launch-readiness.json \
  --release-id cios-pilot-algolia-20260728-b4d7423 \
  --package-commit b4d7423cff92b719dd48bc4b34af0ff21faefc16 \
  --max-failed-source-ratio 0.10 \
  --output /opt/cios/app/out/cios-pilot-monitoring.json
```

Phase 8 completion requires repeatable trusted decisions during the observation window and at least one named-team use, rejection, or amendment of the current Argus recommendation.

Follow-up handoff for recording the final disposition is in `docs/workspace/arrie-phase6-3d-field/21-phase8-disposition-handoff.md`.
