# Hermes Runtime Gate

Date: 2026-07-13
Status: Phase 2 control contract
Gate ID: `runtime`

The runtime gate decides whether live Hermes behavior still works after a
config, skill, memory, gateway, Telegram, model, or profile change.

## Required Evidence

- Fresh relevant health-check command output.
- Gateway status for the affected Hermes instance and profile.
- Telegram delivery evidence when Telegram behavior is touched.
- Fresh-session reset evidence when prompt, identity, memory, model, or Telegram
  context changed.
- Ownership and permission checks for `/opt/data` when VPS files are changed.
- Rollback command or file restore path.

## Pass Criteria

- Affected gateway process is running.
- Fresh-session or fresh-prompt path uses the intended context.
- Telegram sends and receives the expected smoke message when Telegram is in
  scope.
- No recent permission errors or root-owned runtime files are introduced.
- Dashboard and model endpoints remain localhost-only unless separately
  approved.

## Rollback

- Restore backed-up config, prompt, memory, or skill files.
- Restart only the affected service when required by the runbook.
- Re-run `scripts/chowmes-health-check --repair --send-test` after env, config,
  session, gateway, or skill changes.
- Document the failed smoke case in the resource intake report.

## Notes

Runtime readiness cannot be inferred from local docs or config diffs. It needs
fresh live or equivalent smoke evidence.
