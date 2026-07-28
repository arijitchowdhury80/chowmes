# Phase 8 Wrapper Interrupt Cleanup

Status: deployed and verified; full Phase 8 exit still open

## Summary

The Phase 8 observation path exposed a reliability issue: an operator-interrupted wrapper run could leave the active daily runner or watchdog alive if the wrapper process was interrupted during external model-backed synthesis.

CI-OS now tracks the active daily runner PID, process group, and watchdog PID. The daily wrapper installs `EXIT`, `INT`, `HUP`, and `TERM` cleanup hooks so interrupting the wrapper terminates the active daily run tree and watchdog before the wrapper exits.

This improves the monitored pilot release path. It does not complete Phase 8, because Product Marketing still needs to record a final disposition for recommendation `2`.

## Deployed Package

- CI-OS commit: `e02d680`
- Active package path: `/opt/cios/app`
- Release bundle: `/opt/cios/releases/e02d680.tar.gz`
- Release SHA-256: `34b5f8e15fd0238d586759ce36f0b820cdf6f6c764b3d2c846ffc683ecb04fac`

## Verification

- Local focused tests: `91 passed`
  - `tests/deploy/test_cios_daily_wrapper.py`
  - `tests/scripts/test_verify_hermes_package_contract.py`
- Broader reliability/publication tests: `104 passed`
  - `tests/deploy/test_cios_daily_wrapper.py`
  - `tests/scripts/test_verify_hermes_package_contract.py`
  - `tests/scripts/test_check_live_operational_safety.py`
  - `tests/scripts/test_build_phase8_disposition_request.py`
  - `tests/scripts/test_publish_pilot_recommendation_work_artifact.py`
- `git diff --check`: passed.
- Remote package contract passed as `cios`.
- Controlled VPS interrupt smoke test passed:
  - `supervisor_code=130`
  - `actual_wrapper_cleaned=yes`
  - `daily_child_cleaned=yes`
- Live operational safety passed after cleanup:
  - `package_commit=e02d680`
  - `orphan_process_count=0`
  - `root_owned_artifact_count=0`
  - `served_release_ready=true`
- E2E launch readiness passed.
- Controlled-pilot monitoring passed.
- Phase 8 exit correctly failed only on `named_team_disposition_final`.

## Current Gate State

Current recommendation:

- Recommendation ID: `2`
- Owner: `PMM`
- Named team: `Product Marketing`
- Public PMM brief: `https://ci.chowmes.com/data/phase8/argus-pmm-narrative-brief.md`
- Public PMM disposition request: `https://ci.chowmes.com/data/phase8/argus-pmm-disposition-request.md`

Current Phase 8 exit artifact:

- Path: `/opt/cios/app/out/phase8/cios-phase8-exit.json`
- Status: `fail`
- Blocking requirement: `named_team_disposition_final`
- Current recommendation matches pending disposition: `true`
- Launch readiness: `pass`
- Pilot monitoring: `pass`

## Remaining Action

Product Marketing must record `used`, `rejected`, or `amended` for recommendation `2` with a concrete use case and reason. After that, rerun the Phase 8 exit checker.
