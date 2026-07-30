# CI-OS Intelligence Spine Phase 1 RED Gate

Date: 2026-07-30
Status: Phase 1 contract drafted; RED packet and consumer tests added; human semantic approval still required before implementation
Goal: `docs/goals/2026-07-30-ci-os-intelligence-spine-autonomous-goal.md`
Contract: `docs/plan/2026-07-30-ci-os-argus-intelligence-packet-contract.md`
Runtime boundary: Hermes remains the runtime OS. CI-OS remains a separately versioned extension. No Hermes core changes were made.

## What Changed

Phase 1 required schema and contract tests before implementation. The CI-OS repo now has RED tests for the canonical packet contract and the first consumer contract boundaries:

- `/Users/arijitchowdhury/Dropbox/AI-Development/CI-OS/tests/intelligence/test_argus_packet_contract.py`
- `/Users/arijitchowdhury/Dropbox/AI-Development/CI-OS/tests/intelligence/test_argus_packet_adapter.py`
- `/Users/arijitchowdhury/Dropbox/AI-Development/CI-OS/tests/dashboard/test_packet_consumers.py`
- `/Users/arijitchowdhury/Dropbox/AI-Development/CI-OS/tests/delivery/test_packet_telegram_format.py`

No CI-OS production source files were changed in this step.

## Test Command

Run from `/Users/arijitchowdhury/Dropbox/AI-Development/CI-OS`:

```bash
python3 -m py_compile tests/intelligence/test_argus_packet_contract.py tests/intelligence/test_argus_packet_adapter.py tests/dashboard/test_packet_consumers.py tests/delivery/test_packet_telegram_format.py
python3 -m pytest tests/intelligence/test_argus_packet_contract.py tests/intelligence/test_argus_packet_adapter.py tests/dashboard/test_packet_consumers.py tests/delivery/test_packet_telegram_format.py -q
```

Result:

```text
py_compile: pass
pytest: 18 failed in 0.30s
```

Expected RED reason:

```text
Missing cios.intelligence.argus_packet.
Phase 2/3 must implement ArgusIntelligencePacket from the approved contract.
Missing cios.dashboard.packet_consumers.
Dashboard, Market Field, and public status must consume ArgusIntelligencePacket.
Missing cios.delivery.packet_telegram_format.
Daily and weekly Telegram briefs must consume ArgusIntelligencePacket.
```

The failures prove the tests are targeting missing canonical packet behavior and missing packet-consumer boundaries, not a currently passing or post-hoc implementation.

## Covered Behaviors

The RED contract tests require:

1. Run identity, package commit, cadence, and time window.
2. Actionable packet recommendations with proof refs and scorecards.
3. Watch-state restraint when Audience Demand is missing.
4. Quiet-verified status only after source coverage is actually checked.
5. Degraded packet disclosure for source failures and stale freshness.
6. Consumer run-id parity across Telegram, dashboard, Market Field, Evidence Lab, Admin, and public status.
7. Contradictions, unknowns, and rejected reads as first-class packet data.
8. Adapter mapping from current `ProductMarketIntelligenceBrief`, `ArgusDecisionRead`, `MarketMovementMap`, and recommendation rows into the packet.
9. Dashboard state generation from the packet run id, executive read, and primary action.
10. Market Field hotspots and actions referencing packet movement ids.
11. Public status recommendation counts coming from the packet, not a separate dashboard fragment.
12. Stale packet publication disclosure in `latest.json`.
13. Daily Telegram rendering from packet headline, named action, Audience Demand, proof, dashboard link, and run id.
14. Weekly Telegram rendering as a pattern brief, not a daily recap with a weekly title.
15. Failed packet rendering as an honest failure message, not fake intelligence.

## Gate Status

Phase 1 is not complete yet.

The contract changes product semantics by making `ArgusIntelligencePacket` the canonical source for all consumers. Per the goal charter, Arijit must approve the packet contract or request changes before implementation starts.

## Do Not Start Yet

Until the Phase 1 human gate passes, do not start:

- packet implementation;
- runtime permission repair;
- Telegram daily or weekly rendering changes;
- dashboard rebuild;
- 3D Market Field implementation;
- Evidence Lab or Admin implementation;
- production deployment.

## Next Step After Approval

Implement `cios.intelligence.argus_packet` minimally enough to turn the RED tests green, then continue into the Phase 2 scenario harness.
