# Hermes Memory Gate

Date: 2026-07-13
Status: Phase 2 control contract
Gate ID: `memory`

The memory gate decides whether Honcho, GBrain, retrieval tooling, session
changes, or durable-memory changes improve Hermes without damaging profile
identity, privacy boundaries, or prompt budget.

## Required Evidence

- Recall eval prompts drawn from real Chowmes/MyOS questions.
- Baseline answers from current built-in memory and docs search.
- Candidate answers from the memory pilot.
- Prompt-size and context-growth measurement.
- Profile-isolation checks for Athena, Argus, Vulcan, PRISM, and any lab
  profile used for the pilot.
- Sensitive-memory leakage check across profiles and tools.

## Pass Criteria

- Candidate recall is measurably better on the approved eval set.
- No sensitive memory appears in an unrelated profile or tool context.
- Prompt growth stays within the approved budget for the profile.
- Obsidian and repo docs remain the source of truth unless a source-of-truth
  boundary change is explicitly approved.
- Rollback restores the previous memory path without losing canonical notes.

## Rollback

- Disable the memory pilot for the lab profile.
- Restore previous config and session routing.
- Keep exported pilot data only if it contains no sensitive leakage.
- Re-run the runtime gate if any gateway, session, or profile config changed.

## Notes

Memory changes are identity changes. They must remain isolated until they prove
better recall, privacy safety, and operational value.
