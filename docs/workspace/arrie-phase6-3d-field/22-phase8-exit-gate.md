# Phase 8 Exit Gate

Date: 2026-07-28
Status: gate installed and verified; full Phase 8 exit still open

## Source

CI-OS now has a package-level Phase 8 exit checker. It prevents the controlled pilot from being marked complete while the recommendation disposition remains pending.

- CI-OS commit: `44f78fee009f3773698e89083cd3249e41c6582b`
- Release ID: `cios-pilot-algolia-20260728-44f78fe`
- Release bundle: `/opt/cios/releases/44f78fe.tar.gz`
- SHA-256: `2467154f7072fed446f6e029bcbef80d7a28e4d4936f25fd5a327331c88bf9ae`
- Phase 8 exit artifact: `/opt/cios/app/out/phase8/cios-phase8-exit.json`
- Pending disposition artifact: `/opt/cios/app/out/phase8/argus-recommendation-disposition-pending.json`

## Verification

- `pytest tests/scripts/test_check_phase8_exit.py tests/scripts/test_record_pilot_recommendation_disposition.py tests/scripts/test_check_pilot_monitoring.py tests/scripts/test_check_e2e_launch_readiness.py tests/scripts/test_verify_hermes_package_contract.py -q`: `94 passed`
- `python3 -m py_compile scripts/check_phase8_exit.py scripts/record_pilot_recommendation_disposition.py scripts/check_pilot_monitoring.py scripts/check_e2e_launch_readiness.py scripts/verify_hermes_package_contract.py`: passed
- `python3 scripts/verify_hermes_package_contract.py --app-dir .`: passed
- Live package contract: passed as `cios`
- Live operational safety: `passed`
- Live E2E launch readiness: `pass`
- Live controlled-pilot monitoring: `pass`
- Live Phase 8 exit checker: `fail`, as expected, because the disposition is pending.

## Current Gate Result

The live Phase 8 exit artifact reports:

- Status: `fail`
- Phase 8 exit evidence: `false`
- Blocking requirement: `named_team_disposition_final`
- Actual: `decision=pending`, `phase8_exit_evidence=False`, `named_team=Product Marketing`, `use_case_present=False`
- Next step: record a final named-team use, rejection, or amendment with concrete use case and reason.

## Why This Matters

The controlled pilot is released, monitored, and has a current PMM recommendation, but the original goal requires repeatable trusted decisions used in real work. This checker makes that requirement explicit and auditable.

The goal must not be marked complete until `/opt/cios/app/out/phase8/cios-phase8-exit.json` reports `status=pass`.

## Final Gate Command

After the recommendation is used, rejected, or amended, rerun:

```bash
/opt/cios/app/.venv/bin/python /opt/cios/app/scripts/check_phase8_exit.py \
  --pilot-monitoring /opt/cios/app/out/cios-pilot-monitoring.json \
  --launch-readiness /opt/cios/app/out/cios-e2e-launch-readiness.json \
  --public-status /opt/cios/public-store/served/data/argus-latest-run-status.json \
  --disposition /opt/cios/app/out/phase8/argus-recommendation-disposition-final.json \
  --release-id cios-pilot-algolia-20260728-44f78fe \
  --package-commit 44f78fee009f3773698e89083cd3249e41c6582b \
  --output /opt/cios/app/out/phase8/cios-phase8-exit.json
```
