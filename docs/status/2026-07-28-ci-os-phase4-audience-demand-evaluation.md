# CI-OS Phase 4 Audience Demand Evaluation

Date: 2026-07-28
Status: Phase 4 remains active; gate did not pass
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

Phase 4 did not pass.

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

## Next Required Action

One of these must happen before Phase 4 can pass:

1. Export current and previous seven-day Looker rows for the active Argus topics above.
2. Amend or refresh the Argus demand plan so the validated off-plan demand, especially Agent Studio, becomes an explicit planned topic.
3. Configure a recurring GA4 path that produces the same planned-topic current and previous period fields.

The current blocker is not generic Looker access. The blocker is that the available export does not contain action-grade movement for the active Argus plan topics.

## Verification

Commands run from `/Users/arijitchowdhury/Dropbox/AI-Development/CI-OS`:

```bash
python3 -m pytest tests/scripts/test_evaluate_argus_planned_demand_exports.py -q
python3 -m py_compile scripts/evaluate_argus_planned_demand_exports.py
python3 scripts/evaluate_argus_planned_demand_exports.py --plan /tmp/argus-demand-plan-template.csv --data-dir data --output /tmp/argus-planned-demand-evaluation.json --prepared-output /tmp/argus-planned-demand-prepared.csv
python3 scripts/evaluate_argus_planned_demand_exports.py --plan /tmp/argus-demand-plan-template.csv --data-dir data --output /tmp/argus-planned-demand-evaluation.json --prepared-output /tmp/argus-planned-demand-prepared.csv --amendment-output /tmp/argus-demand-plan-amendment-candidates.csv
```

Results:

- evaluator tests: `4 passed`
- compile check: passed
- real evaluation exit code: `2`, expected for a failed phase gate
- prepared demand CSV contained header only because no planned topic passed
- amendment candidate CSV contained one proposed candidate, Agent Studio
