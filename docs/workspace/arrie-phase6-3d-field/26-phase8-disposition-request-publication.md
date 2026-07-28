# Phase 8 PMM Disposition Request Publication

Status: disposition request published; full Phase 8 exit still open

## Summary

CI-OS now publishes a public-safe Product Marketing disposition request beside the Phase 8 PMM narrative brief. This gives the remaining human/team gate an explicit decision path instead of leaving the next action implicit.

This artifact is intentionally not Phase 8 exit evidence. It asks Product Marketing to choose one final disposition for current recommendation `2`:

- `used`
- `rejected`
- `amended`

Phase 8 still completes only after a final named-team disposition is recorded with a concrete use case and reason. Rejection or amendment also requires learning proof.

## Deployed Package

- CI-OS commit: `8c39f15`
- Active package path: `/opt/cios/app`
- Release bundle: `/opt/cios/releases/8c39f15.tar.gz`
- Release SHA-256: `84a1c27db3ee1386737964b954be6bae99816dcdf055c66100703c14473e3493`
- Public work manifest: `https://ci.chowmes.com/data/phase8/argus-phase8-work-artifacts.json`
- PMM narrative brief: `https://ci.chowmes.com/data/phase8/argus-pmm-narrative-brief.md`
- PMM disposition request: `https://ci.chowmes.com/data/phase8/argus-pmm-disposition-request.md`

## Verification

- Local focused tests: `100 passed`
  - `tests/scripts/test_build_phase8_disposition_request.py`
  - `tests/scripts/test_publish_pilot_recommendation_work_artifact.py`
  - `tests/scripts/test_verify_hermes_package_contract.py`
  - `tests/deploy/test_cios_daily_wrapper.py`
- Python compile checks passed for the changed scripts.
- Remote package contract passed as `cios`.
- Live dashboard click validation passed against `https://ci.chowmes.com/`.
- Public artifact redaction passed: `status=clean`, `redaction_count=0`.
- Public artifact safety scan passed: `status=passed`, `findings=0`.
- Live operational safety passed:
  - `package_commit=8c39f15`
  - `root_owned_artifact_count=0`
  - `orphan_process_count=0`
  - `served_release_ready=true`
- E2E launch readiness passed.
- Controlled-pilot monitoring passed.
- Phase 8 exit correctly failed only on `named_team_disposition_final`.

## Live Gate State

Current recommendation:

- Recommendation ID: `2`
- Owner: `PMM`
- Named team: `Product Marketing`
- Action: `Turn the shipped Agent Studio capability into an evidence-backed market narrative before the demand window cools.`
- Confidence: `0.68`

Current Phase 8 exit artifact:

- Path: `/opt/cios/app/out/phase8/cios-phase8-exit.json`
- Status: `fail`
- Phase 8 exit evidence: `false`
- Blocking requirement: `named_team_disposition_final`
- Current recommendation matches pending disposition: `true`
- Launch readiness: `pass`
- Pilot monitoring: `pass`

## Operational Note

A live wrapper run against the freshly mounted release reached external model-backed Argus synthesis and then hung long enough to stop manually. No orphan CI-OS process remained after cleanup, and the operational-safety gate passed. The disposition request was then generated from the current served public PMM work artifact and published through the package publisher with public redaction and safety checks.

## Remaining Action

Product Marketing must record one final disposition for recommendation `2`:

```bash
python scripts/record_pilot_recommendation_disposition.py \
  --review-packet out/phase8/argus-recommendation-review-packet.json \
  --decision used \
  --named-team "Product Marketing" \
  --decided-by "<name-or-team>" \
  --use-case "<where the recommendation was used>" \
  --reason "<why this disposition is true>" \
  --work-artifact-url https://ci.chowmes.com/data/phase8/argus-pmm-narrative-brief.md \
  --output out/phase8/argus-recommendation-disposition-final.json \
  --markdown-output out/phase8/argus-recommendation-disposition-final.md
```

After that, rerun `/opt/cios/app/scripts/check_phase8_exit.py`. The CI-OS completion goal remains active until the exit artifact reports `status=pass`.
