# Phase 8 Observation 1

Date: 2026-07-28
Status: observation recorded; full Phase 8 exit still open

## Source

Observation 1 is based on the live controlled-pilot monitor artifact:

- `/opt/cios/app/out/cios-pilot-monitoring.json`
- Release ID: `cios-pilot-algolia-20260728-47ef4d5`
- Package commit: `47ef4d565f00e8907c42280f62cf9943678805c4`

## Monitor Verdict

- Controlled pilot monitoring: `pass`
- Publication current: true
- Launch readiness passed: true
- Source coverage complete: true
- Source failure ratio OK: true
- Audience demand present: true
- Product reality present: true
- Decision activity present: true

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
- Current public recommendation count: `0`

## Monitoring Debt

- Public status is `limited_by_evidence`.
- Demand plan is missing `11` of `12` planned topics.
- `4` active sources failed this run.
- `3` product-surface captures failed.
- No current recommendation appears in public run status.

## Usage Status

No named-team usage, rejection, or amendment of a current Argus recommendation is recorded for this observation.

The earlier Agent Studio recommendation acceptance remains valid Phase 5 evidence, but Phase 8 still needs real pilot-window usage proof before the full goal can close.

## Next Observation

Run the next scheduled CI-OS daily cycle, then rerun:

```bash
/opt/cios/app/.venv/bin/python /opt/cios/app/scripts/check_pilot_monitoring.py \
  --public-status /opt/cios/public/data/argus-latest-run-status.json \
  --launch-readiness /opt/cios/app/out/cios-e2e-launch-readiness.json \
  --release-id cios-pilot-algolia-20260728-47ef4d5 \
  --package-commit 47ef4d565f00e8907c42280f62cf9943678805c4 \
  --max-failed-source-ratio 0.10 \
  --output /opt/cios/app/out/cios-pilot-monitoring.json
```

Phase 8 completion requires repeatable trusted decisions during the observation window and at least one named-team use, rejection, or amendment of an Argus recommendation.
