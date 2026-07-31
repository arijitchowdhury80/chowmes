# Hermes Eval Gate

Date: 2026-07-13
Status: Phase 2 control contract

The Hermes Eval Gate is the promotion contract for external resources before
they can affect Athena, Argus, Vulcan, Hermes skills, memory, gateway config,
Telegram sessions, or runtime behavior.

This is not a replacement for `skill-verifier`. The gate system wraps the
existing security verifier and adds the missing Hermes-specific checks for
behavior, trigger precision, memory quality, persona drift, and live runtime
health.

## Gate Layers

| Gate | Doc | Purpose |
|---|---|---|
| Security | hermes-security-gate.md | Prove the external repo, skill, package, or tool is safe enough to study, scan, or pilot. |
| Skill behavior | hermes-skill-behavior-gate.md | Prove a skill does the intended job and does not trigger on unrelated work. |
| Memory | hermes-memory-gate.md | Prove memory changes improve recall without contaminating profiles or leaking sensitive context. |
| Voice | hermes-voice-gate.md | Prove Athena, Argus, Vulcan, and other profiles preserve role, tone, boundaries, and operating posture. |
| Runtime | hermes-runtime-gate.md | Prove live Hermes services, sessions, Telegram delivery, and health checks still work after a change. |

## Promotion Rule

Every resource in `hermes-external-resource-ledger.md` must declare required
gates before moving beyond `study` or `scan`. The declaration lives in
`hermes-eval-gate-schema.json` so tests can enforce it.

No resource moves to `pilot`, `live-candidate`, or `live` without:

- required gate list
- evidence location
- pass criteria
- rollback path
- approval owner
- fresh verification output

## Execution Order

1. Run the security gate first for every external resource.
2. Run the skill behavior gate for any skill, prompt, agent workflow, MCP tool,
   self-evolution proposal, or workflow imported from another repo.
3. Run the memory gate for Honcho, GBrain, retrieval, session, or durable-memory
   changes.
4. Run the voice gate for any change touching `SOUL.md`, profile prompts,
   routing, role behavior, or self-evolution outputs.
5. Run the runtime gate before claiming any live Hermes, gateway, or Telegram
   change is ready.

## Non-Goals

- Do not install external skills wholesale.
- Do not merge all checks into `skill-verifier`.
- Do not allow self-evolution to patch live profiles directly.
- Do not expose dashboards, memory services, or model endpoints publicly.
- Do not treat docs-only approval as live-runtime approval.

## Current Slice

This phase creates the gate contract, per-gate docs, and test-enforced resource
coverage. Later slices may add executable wrappers, report aggregation, and
Hermes runtime smoke commands.
