# Hermes Skill Behavior Gate

Date: 2026-07-13
Status: Phase 2 control contract
Gate ID: `skill_behavior`

The skill behavior gate decides whether a Hermes skill, imported workflow, or
agent prompt actually does the intended job and stays quiet when it should.

This gate reuses the benchmark pattern proven by the existing
`should-we-build-this` eval workspace: explicit behavior tests and separate
trigger-readiness tests.

## Required Evidence

- Behavior eval set with prompts, expected outputs, and expectation bullets.
- Negative eval set for prompts where the skill must not trigger.
- Baseline result and candidate result, kept in a durable report.
- Trigger precision and trigger recall summary.
- Conflict check against `AGENTS.md`, `SOUL.md`, `USER.md`, `MEMORY.md`, and
  Telegram operator-mode restrictions.

## Pass Criteria

- Candidate output improves or preserves quality against baseline.
- Negative trigger cases do not hijack implementation, debugging, runtime, or
  unrelated research tasks.
- Trigger recall is strong enough for automatic routing, or the skill remains
  explicit-invocation only.
- The skill does not silently change identity, memory, gateway behavior, tool
  permissions, or live profile routing.

## Rollback

- Keep the candidate as study-only.
- Revert skill prompt, description, or routing metadata to the previous version.
- Record the failed trigger or behavior case as a future regression fixture.

## Notes

Answer quality and trigger readiness are separate gates. A skill can perform
well when explicitly invoked and still be unsafe for automatic triggering.
