# Phase 8 Public PMM Work Artifact Publication

Date: 2026-07-28
Status: public artifact published; full Phase 8 exit still open

## What Changed

The Phase 8 Product Marketing work artifact is now reachable from the controlled pilot public surface, not only from the VPS filesystem.

- CI-OS commit: `8aff99a26a6f4825e682f4be31b4fd4c223507e6`
- Release ID: `cios-pilot-algolia-20260728-8aff99a`
- Release bundle: `/opt/cios/releases/8aff99a.tar.gz`
- Release bundle SHA-256: `54125d5bf8dd85ee2cba654d688a96509fdfe4b6c3ea60ade79df83adaf70715`
- Public manifest: `https://ci.chowmes.com/data/phase8/argus-phase8-work-artifacts.json`
- Public JSON artifact: `https://ci.chowmes.com/data/phase8/argus-pmm-narrative-brief.json`
- Public Markdown artifact: `https://ci.chowmes.com/data/phase8/argus-pmm-narrative-brief.md`

The public manifest reports:

- Status: `published`
- Recommendation ID: `2`
- Named team: `Product Marketing`
- Artifact status: `draft_for_named_team_review`
- Phase 8 exit evidence: `false`

## Verification

- `pytest tests/scripts/test_publish_pilot_recommendation_work_artifact.py tests/scripts/test_export_pilot_recommendation_work_artifact.py tests/scripts/test_verify_hermes_package_contract.py -q`: `76 passed`
- `python -m py_compile scripts/publish_pilot_recommendation_work_artifact.py scripts/export_pilot_recommendation_work_artifact.py scripts/verify_hermes_package_contract.py`: passed
- Local package contract: `PASS: CI-OS Hermes package contract satisfied`
- Live package contract: `PASS: CI-OS Hermes package contract satisfied`
- Served public root redaction: `clean`
- Served public root safety scan: `passed`, `0` findings
- External URL check: public manifest and Markdown artifact returned HTTP 200
- Live operational safety: `passed`
- Live E2E launch readiness: `pass`
- Live controlled-pilot monitoring: `pass`
- Live Phase 8 exit checker: `fail`, as expected, on `named_team_disposition_final`

## Debug Note

The first publication attempt wrote to `/opt/cios/public`, but `ci.chowmes.com` is served by a Python `http.server` process rooted at `/opt/cios/public-store/served`. The artifact was then published into `/opt/cios/public-store/served`, which resolved the external `404`.

The public safety scan initially found two stale `/opt/cios/app` references in `argus-learning-policy-audit.json`. These were existing public artifacts, not the new PMM brief. Running the existing public redaction gate removed both references; the subsequent public safety scan passed with zero findings.

## Remaining Gate

This publication makes the artifact accessible for Product Marketing review. It still does not complete Phase 8.

Phase 8 completes only after a named-team disposition is recorded:

- `used`
- `rejected`
- `amended`

The live exit checker still correctly reports `phase8_exit_evidence=false` until that disposition exists.
