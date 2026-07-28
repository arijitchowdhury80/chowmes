# CI-OS Demand Readiness Gate Status

Date: 2026-07-28
Status: Phase 3 active; recommendation gate still blocked

## What Changed

Live inspection showed that the imported Looker Audience Demand feed contained 100 demand signals, but every top row had `change_pct=null`. The same import path also allowed generic Looker report metadata such as "Web Analytics" to influence planned-topic matching, which polluted earlier demand rows with false topic metadata.

CI-OS was patched and deployed through commit `22e6467` so that:

- generic `source_label` and `source_url` fields no longer drive demand-plan matching;
- current-period-only demand is blocked explicitly;
- processed demand with zero rising-demand topics is reported as `processed_no_action_grade_demand`;
- the data-plane manifest prefers the current readiness action over stale demand-intake sidecar actions;
- blocker titles now match the readiness state shown in the live dashboard.

## Verified Live State

- Public URL: `https://ci.chowmes.com/`
- Latest public status: `blocked_on_evidence`
- Next action: `upload_trended_planned_demand_export`
- Blocker title: `Demand movement not action-grade`
- Blocker next step: upload a planned demand export with previous-period or `change_pct` values, then refresh Argus.
- Dashboard generated at: `2026-07-28T09:09:44.242136Z`

## Verification

- Local focused tests: `48 passed`
- Local evidence-gate slice: `104 passed, 2 deselected`
- Server compile check passed for the changed scripts/modules.
- Live dashboard validation passed with `scripts/validate_dashboard_clicks.py --url https://ci.chowmes.com/`.
- Live public JSON confirmed `status=blocked_on_evidence`, `next_hermes_action=upload_trended_planned_demand_export`, and blocker title `Demand movement not action-grade`.

## Remaining Gate

This does not pass the recommendation gate. It makes the blocker precise. The next demand input must include approved/planned topic mapping plus previous-period or `change_pct` values so Argus can decide whether Audience Demand is actually rising enough to support a recommendation.
