# CI-OS Phase 4 Audience Demand Evaluation

Date: 2026-07-28
Status: Phase 4 passed with limited confidence after explicit demand-plan amendment
Scope: Algolia pilot Audience Demand gate

## What Was Evaluated

Codex added and ran a planned-demand evaluator against:

- active live Argus demand plan: `https://ci.chowmes.com/data/argus-demand-plan-template.csv`
- local Looker export folder: `/Users/arijitchowdhury/Dropbox/AI-Development/CI-OS/data`
- evaluator script: `/Users/arijitchowdhury/Dropbox/AI-Development/CI-OS/scripts/evaluate_argus_planned_demand_exports.py`

The evaluator inspected 12 active Argus demand-plan topics and 11,057 metric rows from the available Looker exports.

## Gate Rule Used

The evaluator uses the CI-OS demand quality rule from `src/cios/intelligence/demand_quality.py`:

- current value must be at least 50 sessions
- `change_pct` must be at least 0.05
- evidence must map to a topic in the active Argus demand plan
- generic helper terms such as `search`, `studio`, `commerce`, or `rules` are not allowed to create matches by themselves
- Looker metadata fields such as `source_url` are not used for topic matching

## Result

The first evaluation did not pass because Agent Studio was off-plan.

The generated report status was:

```json
{
  "status": "blocked_no_action_grade_planned_demand",
  "phase4_gate_passed": false,
  "plan_topic_count": 12,
  "metric_row_count": 11057,
  "demand_change_floor": 0.05,
  "demand_value_floor": 50.0
}
```

Every active planned topic returned `no_matching_current_rows`:

- Analytics Studio, Commerce Studio
- Commerce Studio
- Commerce Studio (Attribute Rules)
- Commerce Studio (Rules)
- Commerce Studio (Rules and Rewrites API)
- Database upgrade
- Dynamic Search Rules API
- Dynamic Search Rules (DSR)
- Dynamic Search Rules (DSR) API
- Dynamic Search Rules performance
- Experimental features
- Federated document fetching

## Important Finding

The available Looker exports do contain off-plan audience movement:

- Agent Studio: 1,619 current sessions versus 751 previous sessions, `change_pct=1.1558`
- Generative experiences: 177 current sessions versus 301 previous sessions, `change_pct=-0.412`
- AI Recommendations: 106 current sessions versus 107 previous sessions, `change_pct=-0.0093`

Agent Studio is meaningful audience demand, but it is not in the active Argus demand plan. It cannot pass Phase 4 unless the Argus demand plan is explicitly amended to include Agent Studio or the product/conversation work order is refreshed so Agent Studio becomes a planned topic.

The evaluator now emits a plan-amendment candidate CSV when off-plan movement qualifies. The real run produced one candidate:

| Candidate | Current sessions | Previous sessions | Change | Suggested filters | Caveat |
|---|---:|---:|---:|---|---|
| Agent Studio | 1,619 | 751 | 1.1558 | Agent Studio; agentic ai; ai agent; ai agents | Comparison quality is `comparable_limited` because current landing-page metrics are compared to previous landing-page device sessions. |

This candidate should be treated as a work-order amendment proposal, not as a passed gate by itself.

CI-OS now carries this proposal into the Argus operator handoff when the evaluator report is available. The daily wrapper can run the planned-demand evaluator from the configured Looker export data directory, publish the evaluation and amendment CSV artifacts, and pass the report into `build_argus_operator_handoff.py`. The dashboard renderer now has a public-safe “Suggested demand-plan amendment” panel, but the handoff still keeps `status=blocked_on_evidence` until an amended plan produces planned-topic gate evidence.

This integration is deployed on Chowmes in CI-OS package commit `fa2f31f` and served from public release `cios-20260728T101358Z-manual-fa2f31f`. The live page at `https://ci.chowmes.com/` contains the Suggested demand-plan amendment panel for Agent Studio, and the public data endpoints expose both `argus-planned-demand-evaluation.json` and `argus-operator-handoff.json`.

CI-OS commit `d6d4b6e` then added an explicit amendment tool and limited-confidence evaluator mode. The Agent Studio candidate was accepted into the Argus demand plan, evaluated as a planned topic, imported into the demand ledger, and refreshed through Argus.

The amended evaluator result was:

```json
{
  "status": "passed_limited",
  "phase4_gate_passed": true,
  "phase4_gate_confidence": "limited",
  "phase4_gate_topics": ["Agent Studio"]
}
```

The runtime import result was:

```json
{
  "status": "refreshed",
  "prepared_rows": 1,
  "persisted_demand_signals": 1,
  "recommendations": 1
}
```

The current served release is `cios-20260728T102723Z-manual-d6d4b6e`. Public `argus-dashboard.json` reports 101 demand signals, 3 patterns, and 1 recommendation. Public `argus-demand-readiness.json` reports `processed_partial_plan_coverage`, 1 rising topic, and 1 top topic.

## Next Required Action

Phase 4 is now sufficient to enter Phase 5, with a confidence caveat:

1. Human-review the generated Agent Studio recommendation for accuracy, novelty, and direct usefulness.
2. If accepted, record the accepted read and create the Phase 5 learning instruction.
3. If rejected or amended, record the critique and rerun Argus against the corrected read.

The remaining demand caveat is coverage, not absence. Agent Studio is planned and rising, but the demand plan still has partial coverage and the accepted trend has limited confidence because it compares comparable but not identical Looker export families.

## Verification

Commands run from `/Users/arijitchowdhury/Dropbox/AI-Development/CI-OS`:

```bash
python3 -m pytest tests/scripts/test_evaluate_argus_planned_demand_exports.py -q
python3 -m py_compile scripts/evaluate_argus_planned_demand_exports.py
python3 scripts/evaluate_argus_planned_demand_exports.py --plan /tmp/argus-demand-plan-template.csv --data-dir data --output /tmp/argus-planned-demand-evaluation.json --prepared-output /tmp/argus-planned-demand-prepared.csv
python3 scripts/evaluate_argus_planned_demand_exports.py --plan /tmp/argus-demand-plan-template.csv --data-dir data --output /tmp/argus-planned-demand-evaluation.json --prepared-output /tmp/argus-planned-demand-prepared.csv --amendment-output /tmp/argus-demand-plan-amendment-candidates.csv
python3 scripts/build_argus_operator_handoff.py --tenant algolia --work-queue <empty queue fixture> --demand-readiness <processed_no_action_grade_demand fixture> --demand-plan-amendments /tmp/argus-planned-demand-evaluation.json --output /tmp/argus-operator-handoff-with-amendments.json
```

Results:

- wrapper and package-contract tests: `81 passed`
- renderer, handoff, attach, and evaluator tests: `55 passed`
- compile check: passed
- shell syntax check for `deploy/cios-daily.sh`: passed
- real evaluation exit code: `2`, expected for a failed phase gate
- local handoff build with the real evaluator report kept `blocked_on_evidence`, titled the blocker `Demand movement not action-grade`, and carried `1` amendment candidate: Agent Studio
- prepared demand CSV contained header only because no planned topic passed
- amendment candidate CSV contained one proposed candidate, Agent Studio
- VPS package contract check as `cios`: `PASS: CI-OS Hermes package contract satisfied`
- VPS handoff rebuild: `blocked_on_evidence`, amendment candidate count `1`, first candidate `Agent Studio`
- public JSON checks: `argus-planned-demand-evaluation.json` reports `phase4_gate_passed=False` and one `plan_amendment_candidates` row; `argus-operator-handoff.json` reports one public-safe `demand_plan_amendments` candidate
- live dashboard validation: `python3 scripts/validate_dashboard_clicks.py --url https://ci.chowmes.com/` passed market field, structure, nav targets, timeline, semantic layer, priority selection, brief routing, appendices, and 390 / 768 / 1280 viewport checks
- local amended evaluator proof: `passed_limited`, `phase4_gate_passed=True`, gate topic `Agent Studio`, prepared rows `1`
- VPS package commit: `d6d4b6e`
- VPS amended import: `status=refreshed`, prepared rows `1`, persisted demand signals `1`, refresh `0`, rerender `0`
- current public release: `cios-20260728T102723Z-manual-d6d4b6e`
- current public JSON checks: recommendation count `1`, demand signal count `101`, rising topic count `1`, primary action `Turn the shipped Agent Studio capability into an evidence-backed market narrative before the demand window cools.`
- current live dashboard validation: `python3 scripts/validate_dashboard_clicks.py --url https://ci.chowmes.com/` passed after restoring the served competitor brief routes
