# CI-OS Intelligence Spine Phase 2 Scenario Harness

Date: 2026-07-30
Status: Phase 2 implemented and verified locally
Goal: `docs/goals/2026-07-30-ci-os-intelligence-spine-autonomous-goal.md`
Prior gate: `docs/status/2026-07-30-ci-os-intelligence-spine-phase1-implementation.md`
Runtime boundary: Hermes remains the runtime OS. CI-OS remains a separately versioned extension. No Hermes core changes were made.

## Scope

Phase 2 proves the packet brain against deterministic scenarios before any further UI, runtime, Telegram, deploy, or production work.

Implemented in CI-OS package source:

- `/Users/arijitchowdhury/Dropbox/AI-Development/CI-OS/src/cios/intelligence/argus_packet_scenarios.py`
- `/Users/arijitchowdhury/Dropbox/AI-Development/CI-OS/tests/intelligence/test_argus_packet_scenarios.py`
- `/Users/arijitchowdhury/Dropbox/AI-Development/CI-OS/src/cios/intelligence/__init__.py`

## RED Gate

Command run from `/Users/arijitchowdhury/Dropbox/AI-Development/CI-OS` before implementation:

```bash
python3 -m pytest tests/intelligence/test_argus_packet_scenarios.py -q
```

Result:

```text
10 failed in 0.38s
```

Expected failure:

```text
Missing Phase 2 scenario harness module: No module named 'cios.intelligence.argus_packet_scenarios'
```

## Implemented Scenarios

The harness declares and builds these canonical packet fixtures:

1. `actionable_day`
2. `quiet_verified_day`
3. `degraded_day`
4. `contradiction_day`
5. `stale_evidence_day`
6. `missing_demand_day`
7. `weekly_trend_day`
8. `noisy_duplicate_day`

Each fixture returns an `ArgusIntelligencePacket`, not UI-specific data.

The tests assert:

- action promotion requires recommendation, movement refs, proof refs, and Audience Demand;
- quiet means verified quiet, not missing collection;
- degraded state surfaces source failures without faking actionability;
- contradiction state blocks action and preserves conflict;
- stale evidence cannot publish as current;
- missing Audience Demand blocks recommendation promotion;
- weekly trend is a pattern over time, not a daily recap with a weekly title;
- noisy duplicate input suppresses false urgency;
- existing dashboard/latest-json and Telegram packet consumers can render every scenario without story drift.

## Verification

Commands run from `/Users/arijitchowdhury/Dropbox/AI-Development/CI-OS`:

```bash
python3 -m py_compile src/cios/intelligence/argus_packet_scenarios.py src/cios/intelligence/__init__.py
```

Result:

```text
pass
```

Focused Phase 2 suite:

```bash
python3 -m pytest tests/intelligence/test_argus_packet_scenarios.py -q
```

Result:

```text
11 passed in 0.76s
```

Focused packet and consumer suite:

```bash
python3 -m pytest tests/intelligence/test_argus_packet_scenarios.py tests/intelligence/test_argus_packet_contract.py tests/intelligence/test_argus_packet_adapter.py tests/dashboard/test_packet_consumers.py tests/delivery/test_packet_telegram_format.py -q
```

Result:

```text
29 passed in 0.27s
```

Broader affected-surface suite:

```bash
python3 -m pytest tests/intelligence tests/dashboard tests/delivery -q
```

Result:

```text
302 passed in 1.42s
```

## Phase 2 Gate Result

Phase 2 passes locally:

- all eight required scenario fixtures exist;
- at least one fixture proves action promotion;
- at least one fixture proves action blocking;
- at least one fixture proves weekly pattern formation;
- no fixture requires dashboard, Telegram, or public-status consumers to invent meaning;
- all affected local tests pass.

## Next Phase

Proceed to Phase 3: Engine Implementation And Persistence.

Phase 3 must make real CI-OS evidence produce and persist the canonical packet with one run id across packet, dashboard state, public status, and delivery plan. It must not modify Hermes core.
