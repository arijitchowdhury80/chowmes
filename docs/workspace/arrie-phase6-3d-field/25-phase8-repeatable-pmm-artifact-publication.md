# Phase 8 Repeatable PMM Artifact Publication

Date: 2026-07-28
Status: wrapper hardened; full Phase 8 exit still open

## What Changed

The CI-OS daily wrapper now republishes the Phase 8 Product Marketing work artifact through the normal staged public release path whenever the current run has a reviewable Argus recommendation.

This replaces the one-off manual publication path with repeatable package behavior:

1. Export the current recommendation review packet.
2. Generate the Product Marketing work artifact.
3. Publish the artifact into the staged public release under `data/phase8/`.
4. Run public redaction and safety scan before promotion.
5. Promote `data/phase8/` into both `data/phase8/` and `v2/data/phase8/`.

If a run has no current reviewable recommendation, the wrapper logs a skip message and does not publish a stale PMM artifact.

## Release Evidence

- CI-OS commit: `2a4923973857ac035ba53b58168792ffb85c3fa2`
- Release ID: `cios-pilot-algolia-20260728-2a49239`
- Release bundle: `/opt/cios/releases/2a49239.tar.gz`
- Release bundle SHA-256: `0a7224a914aab459f7409f3e870d51865b22305e06fdc066dfe1f704fdc5fb28`
- Existing public manifest: `https://ci.chowmes.com/data/phase8/argus-phase8-work-artifacts.json`
- Existing public Markdown artifact: `https://ci.chowmes.com/data/phase8/argus-pmm-narrative-brief.md`

## Verification

- `pytest tests/deploy/test_cios_daily_wrapper.py::test_hermes_wrapper_enables_product_market_spine_by_default_and_publishes_same_run_artifacts tests/scripts/test_publish_pilot_recommendation_work_artifact.py tests/scripts/test_verify_hermes_package_contract.py -q`: `74 passed`
- `python -m py_compile scripts/verify_hermes_package_contract.py scripts/publish_pilot_recommendation_work_artifact.py scripts/export_pilot_recommendation_work_artifact.py`: passed
- Local package contract: `PASS: CI-OS Hermes package contract satisfied`
- Live package contract: `PASS: CI-OS Hermes package contract satisfied`
- Live served public safety scan: `passed`, `0` findings
- Live operational safety: `passed`
- Live E2E launch readiness: `pass`
- Live controlled-pilot monitoring: `pass`
- Live Phase 8 exit checker: `fail`, as expected, on `named_team_disposition_final`

## Remaining Gate

This work makes the Product Marketing artifact durable across future pilot publications. It still does not complete Phase 8.

The remaining Phase 8 exit requirement is unchanged: Product Marketing must record a final disposition of the current recommendation as `used`, `rejected`, or `amended`.
