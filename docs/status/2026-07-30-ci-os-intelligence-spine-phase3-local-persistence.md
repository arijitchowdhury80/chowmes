# CI-OS Intelligence Spine Phase 3 Local Persistence

Date: 2026-07-30
Status: Phase 3 local implementation and verification passed
Goal: `docs/goals/2026-07-30-ci-os-intelligence-spine-autonomous-goal.md`
Prior gate: `docs/status/2026-07-30-ci-os-intelligence-spine-phase2-scenario-harness.md`
Runtime boundary: Hermes remains the runtime OS. CI-OS remains a separately versioned extension. No Hermes core changes were made.

## Scope

Phase 3 local work makes real product-market runner output produce and persist the canonical `ArgusIntelligencePacket`, then exports packet-backed consumer views with one shared run identity.

This was local package work only:

- no VPS deployment;
- no production cron or Telegram changes;
- no Hermes core modification;
- no Phase 4 delivery send.

## RED Gates

Targeted Phase 3 tests before implementation:

```bash
python3 -m pytest tests/intelligence/test_runner.py::test_run_product_market_payload_produces_canonical_argus_packet tests/db/test_product_market_schema_contract.py::test_run_intelligence_has_canonical_argus_packet_contract tests/db/test_product_market_repo.py::test_save_run_intelligence_summary_targets_product_market_run_intelligence tests/db/test_product_market_repo.py::test_get_latest_run_intelligence_reads_latest_brain_record -q
```

Result:

```text
4 failed in 0.74s
```

Expected failures:

- `ProductMarketRunSummary` had no `argus_packet`;
- schema had no `argus_packet` column or contract;
- repository insert did not write `argus_packet`;
- latest-run reader did not select `argus_packet`.

Export RED:

```bash
python3 -m pytest tests/intelligence/test_argus_packet_export.py -q
```

Result:

```text
1 failed in 0.21s
```

Expected failure:

```text
No module named 'cios.intelligence.argus_packet_export'
```

Dashboard read-through RED:

```bash
python3 -m pytest tests/dashboard/test_state_builder.py::test_product_market_run_history_preserves_canonical_argus_packet -q
```

Result:

```text
1 failed in 1.66s
```

Expected failure:

```text
ProductMarketRunHistoryEntry object has no attribute 'argus_packet'
```

## Implemented In CI-OS

Package source:

- `/Users/arijitchowdhury/Dropbox/AI-Development/CI-OS`

Implemented or modified:

- `src/cios/intelligence/runner.py`
- `src/cios/intelligence/argus_packet.py`
- `src/cios/intelligence/argus_packet_export.py`
- `src/cios/db/schema.sql`
- `src/cios/db/repos/product_market.py`
- `src/cios/dashboard/types.py`
- `src/cios/dashboard/state_builder.py`
- `scripts/apply_product_market_schema.py`

Tests added or modified:

- `tests/intelligence/test_runner.py`
- `tests/intelligence/test_argus_packet_export.py`
- `tests/db/test_product_market_schema_contract.py`
- `tests/db/test_product_market_repo.py`
- `tests/dashboard/conftest.py`
- `tests/dashboard/test_state_builder.py`

The implementation adds:

1. `ProductMarketRunSummary.argus_packet`.
2. A product-market summary to `ArgusIntelligencePacket` mapping.
3. Runner-generated local packet run identity.
4. Packet persistence in `product_market_run_intelligence.argus_packet`.
5. Latest-run read-through of `argus_packet`.
6. Packet export bundle files:
   - `argus-intelligence-packet.json`
   - `argus-latest-packet.json`
   - `argus-packet-dashboard-state.json`
   - `argus-packet-public-status.json`
   - `argus-packet-delivery-plan.json`
7. Dashboard run-history preservation of the canonical packet.
8. Adapter normalization from old runner `quiet` verdicts into packet `quiet_verified` status.
9. Adapter normalization from runner monitoring actions into packet monitoring actions.

## Verification

Commands run from `/Users/arijitchowdhury/Dropbox/AI-Development/CI-OS`:

```bash
python3 -m py_compile src/cios/intelligence/runner.py src/cios/intelligence/argus_packet.py src/cios/intelligence/argus_packet_export.py src/cios/intelligence/__init__.py src/cios/db/repos/product_market.py src/cios/dashboard/state_builder.py src/cios/dashboard/types.py scripts/apply_product_market_schema.py
```

Result:

```text
pass
```

Focused Phase 3 suite:

```bash
python3 -m pytest tests/intelligence/test_runner.py tests/intelligence/test_argus_packet_contract.py tests/intelligence/test_argus_packet_adapter.py tests/intelligence/test_argus_packet_scenarios.py tests/intelligence/test_argus_packet_export.py tests/dashboard/test_packet_consumers.py tests/dashboard/test_state_builder.py tests/delivery/test_packet_telegram_format.py tests/db/test_product_market_schema_contract.py tests/db/test_product_market_repo.py -q
```

Result:

```text
137 passed in 0.63s
```

Broader affected-surface suite:

```bash
python3 -m pytest tests/intelligence tests/dashboard tests/delivery tests/db -q
```

Result:

```text
347 passed in 2.58s
```

## Phase 3 Gate Result

Phase 3 passes locally:

- a fresh local product-market run summary produces a canonical packet;
- the packet is persisted in run intelligence;
- latest run intelligence can return the packet;
- dashboard run history preserves the packet for app-layer consumers;
- packet, latest pointer, dashboard state, public status, and delivery plan exports all share one `packet_id` and one `run_id`;
- scenario, packet, dashboard, delivery, and DB contract tests pass.

## Next Phase

Proceed to Phase 4: Telegram Daily And Weekly Gateway.

Phase 4 must send forced daily and weekly Telegram briefs from fresh packets, record true delivery rows, and prove Telegram and dashboard point to the same run id. No failure message may pretend to be intelligence.
