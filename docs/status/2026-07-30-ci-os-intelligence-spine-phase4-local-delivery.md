# CI-OS Intelligence Spine Phase 4 Local Delivery Gate

Date: 2026-07-30
Status: Human-usefulness gate failed after live Telegram review; corrective package deployed with no-send previews verified; resend pending human approval
CI-OS branch: `codex/ci-os-phase0-baseline`

## Scope

Phase 4 objective is to make Telegram consume the canonical Argus Intelligence Packet instead of becoming a parallel narrative or error stream.

This local slice implemented and verified:

- Daily Telegram command brief body from `ArgusIntelligencePacket`.
- Weekly packet brief body that can be forced without waiting for Sunday.
- Packet-backed `DeliveryRequest` builder.
- `packet_id` and `run_id` propagation through `ReportReadyEvent`, `BotDeliveryRecord`, and `DeliveryCommander`.
- Postgres `bot_deliveries` persistence of packet/run identity.
- Existing-DB schema bridge for delivery identity columns.
- Operator script for forced daily/weekly Telegram validation from an exported packet JSON.
- Runtime packet identity fix: packet `run_id` now uses execution time while the packet time window keeps the evidence timestamp.
- Runtime package identity fix: packet `run.package_commit` now resolves from `CIOS_PACKAGE_COMMIT`, `CIOS_RELEASE_COMMIT`, `.cios-release-commit`, or `.cios-package-commit` before falling back to `local`.

## CI-OS Source Changes

- `src/cios/delivery/packet_delivery.py`
- `src/cios/delivery/packet_telegram_format.py`
- `src/cios/delivery/types.py`
- `src/cios/delivery/commander.py`
- `src/cios/db/repos/delivery.py`
- `src/cios/db/schema.sql`
- `scripts/apply_product_market_schema.py`
- `scripts/send_argus_packet_telegram.py`
- `src/cios/intelligence/runner.py`

## Tests Added

- `tests/delivery/test_packet_delivery.py`
- `tests/db/test_delivery_repo.py`
- `tests/db/test_delivery_schema_contract.py`
- `tests/scripts/test_send_argus_packet_telegram.py`
- `tests/intelligence/test_runner.py`

## Verification

RED evidence:

- `python3 -m pytest tests/delivery/test_packet_delivery.py -q`
  - Result: `3 failed`
  - Expected cause: `ModuleNotFoundError: No module named 'cios.delivery.packet_delivery'`
- `python3 -m pytest tests/delivery/test_packet_delivery.py tests/db/test_delivery_repo.py tests/db/test_delivery_schema_contract.py -q`
  - Result: `5 failed`
  - Expected causes: missing packet delivery module, missing delivery schema identity fields, fake repository harness not yet crossing tenant context.
- `python3 -m pytest tests/scripts/test_send_argus_packet_telegram.py -q`
  - Result: `2 failed`
  - Expected cause: `scripts/send_argus_packet_telegram.py` absent.
- `python3 -m pytest tests/db/test_delivery_schema_contract.py -q`
  - Result: `1 failed, 1 passed`
  - Expected cause: schema apply bridge did not yet alter existing `bot_deliveries`.
- `python3 -m pytest tests/intelligence/test_runner.py::test_argus_packet_run_identity_uses_execution_time_not_evidence_time -q`
  - Result: `1 failed`
  - Expected cause: packet run identity used evidence timestamp instead of execution timestamp.
- Live VPS forced send attempt against deployed `df50441` returned `ModuleNotFoundError: No module named 'cios.delivery.packet_delivery'`.
  - Expected cause after inspection: direct script execution did not add package `src/` to `sys.path`.
- `python3 -m pytest tests/intelligence/test_runner.py::test_argus_packet_uses_package_commit_from_environment -q`
  - Result: `1 failed`
  - Expected cause: packet `run.package_commit` was hardcoded to `local`.

GREEN evidence:

- `python3 -m pytest tests/delivery/test_packet_delivery.py tests/db/test_delivery_repo.py tests/db/test_delivery_schema_contract.py -q`
  - Result: `5 passed in 1.31s`
- `python3 -m pytest tests/scripts/test_send_argus_packet_telegram.py tests/delivery/test_packet_delivery.py -q`
  - Result: `5 passed in 0.23s`
- `python3 -m py_compile scripts/apply_product_market_schema.py scripts/send_argus_packet_telegram.py`
  - Result: passed
- `python3 -m py_compile src/cios/delivery/packet_delivery.py src/cios/delivery/packet_telegram_format.py src/cios/delivery/types.py src/cios/delivery/commander.py src/cios/db/repos/delivery.py`
  - Result: passed
- `python3 -m pytest tests/delivery/test_packet_delivery.py tests/delivery/test_packet_telegram_format.py tests/delivery/test_commander.py tests/delivery/test_gated_commander.py tests/db/test_delivery_repo.py tests/db/test_delivery_schema_contract.py tests/db/test_product_market_schema_contract.py tests/intelligence/test_argus_packet_contract.py tests/intelligence/test_argus_packet_scenarios.py tests/dashboard/test_packet_consumers.py -q`
  - Result: `51 passed in 0.49s`
- `python3 -m pytest tests/delivery tests/db tests/intelligence tests/dashboard tests/scripts/test_send_argus_packet_telegram.py -q`
  - Result: `355 passed in 1.09s`
- After fresh-run identity correction:
  - `python3 -m pytest tests/delivery tests/db tests/intelligence tests/dashboard tests/scripts/test_send_argus_packet_telegram.py -q`
  - Result: `356 passed in 0.80s`
- After direct-script execution correction:
  - `python3 -m pytest tests/delivery tests/db tests/intelligence tests/dashboard tests/scripts/test_send_argus_packet_telegram.py -q`
  - Result: `357 passed in 1.07s`
- After package identity correction:
  - `python3 -m pytest tests/delivery tests/db tests/intelligence tests/dashboard tests/scripts/test_send_argus_packet_telegram.py -q`
  - Result: `358 passed in 1.08s`

## Deployment And Live Evidence

Source commits pushed:

- `9cab347` - packet-backed Telegram delivery path.
- `df50441` - packet run identity uses execution time rather than evidence timestamp.
- `ea9f864` - direct execution of the packet Telegram sender works without external `PYTHONPATH`.
- `a291dcb` - packets are stamped with deployed package identity.

Deployed package:

- Active deployed commit: `a291dcb792604bac5653f2230f05ae6c1b53a48b`.
- Final archive SHA-256: `7eded7f67d319f74921e2847631b9cb1610190eca61719350822c842cf8ff0de`.
- Rollback bundle before final deploy: `/opt/cios/releases/rollback-before-phase4-package-identity-20260730T204924Z.tar.gz`.
- Remote package contract: `PASS: CI-OS Hermes package contract satisfied`.
- Existing-DB schema bridge: `product-market schema ready`.
- Delivery schema readback: `columns=packet_id,run_id`, `packet_index_count=1`.

Fresh packet generated on VPS:

- Packet path: `/opt/cios/app/out/argus-phase4-fresh-packet.json`.
- Packet id: `packet-product-market-local-tenant-1-20260730T204949Z`.
- Run id: `product-market-local-tenant-1-20260730T204949Z`.
- Generated at: `2026-07-30T20:49:49.828410Z`.
- Evidence window end: `2026-07-28T13:43:30.626789Z`.
- Package commit: `a291dcb792604bac5653f2230f05ae6c1b53a48b`.
- Verdict: `watch`.
- Recommendation count: `0`.

Forced Telegram sends from the same packet:

- Daily send output: `/opt/cios/app/out/argus-phase4-forced-daily-send.json`.
  - Delivered: `true`.
  - Bot delivery id: `100`.
  - Delivery attempt id: `101`.
  - Report id: `101`.
  - Status: `sent`.
- Weekly send output: `/opt/cios/app/out/argus-phase4-forced-weekly-send.json`.
  - Delivered: `true`.
  - Bot delivery id: `101`.
  - Delivery attempt id: `102`.
  - Report id: `102`.
  - Status: `sent`.

Delivery ledger readback:

- `bot_deliveries.id=100`, cadence `daily`, channel `telegram`, status `sent`, packet id `packet-product-market-local-tenant-1-20260730T204949Z`, run id `product-market-local-tenant-1-20260730T204949Z`, error `null`.
- `bot_deliveries.id=101`, cadence `weekly`, channel `telegram`, status `sent`, packet id `packet-product-market-local-tenant-1-20260730T204949Z`, run id `product-market-local-tenant-1-20260730T204949Z`, error `null`.
- `delivery_attempts.id=101`, status `sent`, provider message ref `275`.
- `delivery_attempts.id=102`, status `sent`, provider message ref `276`.

Served dashboard/public identity check:

- `/opt/cios/public/data/semantic-dashboard.json` is still generated at `2026-07-28T13:45:06.039823Z`, with `run_health.run_id=daily-algolia-1785245335`, and no `packet_id`.
- `/opt/cios/public/data/argus-latest-run-status.json` is still generated at `2026-07-28T14:31:38.284219Z`, and has no packet id.
- Therefore the Phase 4 Telegram send proof is passed, but the exit-gate clause "Telegram and dashboard point to the same run id and same core read" is not yet passed by the live dashboard.

## Human Review Failure

Arijit reviewed the forced Telegram messages and rejected the content as not making sense. The failure was not Telegram transport: the bot delivered successfully. The failure was the intelligence packaging and channel copy.

Observed root causes:

- The canonical packet could carry repeated market movement rows because packet movements were emitted per heat cell instead of being collapsed by capability.
- The daily Telegram brief rendered raw packet fields directly, which repeated the same missing-demand statement as headline, plain read, why, and blocked evidence.
- The weekly forced send used a daily packet as if it were a weekly synthesis, producing repeated "weekly pattern" rows from a daily view.
- The report title preserved the raw packet sentence, so even successful delivery ledger rows could carry the confusing headline.

Corrective patch:

- Collapse duplicate movement cells into one packet movement per capability.
- Convert blocker-derived `needed_evidence` into evidence requests instead of repeating blocker explanations.
- Render watch/degraded/stale no-recommendation daily packets as a compact mobile operator brief: read state, one market movement, one reason action is withheld, one next check, and a compact proof line.
- Make weekly Telegram rendering refuse to masquerade a daily packet as a weekly synthesis.
- Use the same channel-specific titles for delivery reports and rendered Telegram bodies.
- Align weekly-unavailable next checks with the displayed movement so a cadence warning does not introduce a contradictory subject.

Corrected deployed no-send preview from the same rejected server packet:

```text
Argus read: Watch, no owner action
Run: product-market-local-tenant-1-20260730T204949Z
Window: today

Market movement: Shopping Assistant
Shopping Assistant is heating up across Luigi's Box, Constructor, and Bloomreach.

Why it matters: Product and market-conversation proof exist, but no tenant-side demand evidence was captured, so Argus is watching instead of promoting an owner action.

Next check: Collect GA / Looker demand evidence for Shopping Assistant before promoting it into a recommendation.

Proof: Product Reality present (524); Market Conversation present (80); Audience Demand missing
```

Corrected deployed weekly-unavailable no-send preview:

```text
Weekly synthesis unavailable
This is a daily packet, not a weekly synthesis packet.
Run: product-market-local-tenant-1-20260730T204949Z

Next check: Collect GA / Looker demand evidence for Shopping Assistant before promoting it into a recommendation.
```

Local verification:

- `python3 -m pytest tests/delivery/test_packet_telegram_format.py::test_watch_packet_telegram_brief_compresses_repeated_packet_text -q`
  - Result: `1 passed in 0.10s`
- `python3 -m pytest tests/delivery tests/db tests/intelligence tests/dashboard tests/scripts/test_send_argus_packet_telegram.py -q`
  - Result: `362 passed in 1.33s`
- `python3 -m py_compile src/cios/intelligence/argus_packet.py src/cios/delivery/packet_telegram_format.py src/cios/delivery/packet_delivery.py`
  - Result: passed

Deployment verification:

- CI-OS commits pushed:
  - `36d3326` - Fix Argus Telegram watch brief semantics.
  - `3188c81` - Align weekly unavailable Telegram next check.
- Deployed package marker: `3188c81db5f3e393c920f2ea69147f61e35e2bf6`.
- Release archive SHA-256: `5a65af434c42e3c7170fc5019e446c7fba8098ae3dbca2d83737e8d13bae0826`.
- Rollback bundle before final deploy: `/opt/cios/releases/rollback-before-weekly-unavailable-next-check-20260731T061153Z.tar.gz`.
- Remote package contract: `PASS: CI-OS Hermes package contract satisfied`.
- Deployed no-send preview artifacts:
  - `/opt/cios/app/out/argus-phase4-deployed-daily-preview.txt`
  - `/opt/cios/app/out/argus-phase4-deployed-weekly-preview.txt`
- Preview checks:
  - Daily `no tenant-side demand evidence` repetition count: `1`.
  - Weekly unavailable notice present: `true`.
  - Weekly unavailable preview Support mismatch: `false`.

Gate implication:

- Phase 4 is not accepted yet.
- Do not send more Telegram messages until Arijit approves the deployed no-send preview.
- Weekly delivery cannot be accepted from a daily packet. A true weekly packet or an explicit "weekly synthesis unavailable" message is required.
- Dashboard same-run parity remains pending.

## Gate Status

The Telegram transport portion of Phase 4 was verified live, but the Telegram human-usefulness portion failed.

Phase 4 should remain at its human gate until Arijit confirms the corrected Telegram preview is useful and until the dashboard same-run clause is either satisfied by Phase 5 packet-dashboard work or explicitly moved to Phase 5 by decision.

Next step: request human review of the deployed no-send preview before any resend. If accepted, resend the corrected daily brief only; keep weekly as unavailable until a true weekly packet exists.
