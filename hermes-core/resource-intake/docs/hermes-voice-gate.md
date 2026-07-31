# Hermes Voice Gate

Date: 2026-07-13
Status: Phase 2 control contract
Gate ID: `voice`

The voice gate decides whether Hermes profile changes preserve the intended
identity, role boundaries, and operating style of Athena, Argus, Vulcan, and
other profiles.

## Required Evidence

- Persona smoke prompts for every touched profile.
- Regression prompts from prior voice failures, especially Argus robotic voice
  drift and Athena yes-man drift.
- Comparison against profile source files such as `SOUL.md`, `USER.md`,
  `MEMORY.md`, and profile-specific role definitions.
- Fresh-session or fresh-prompt transcript after prompt, memory, model, or
  routing changes.
- Explicit review of whether the change alters authority, tool permissions,
  delegation behavior, or Telegram operating mode.

## Pass Criteria

- Athena remains a cofounder-level architect and does not collapse into generic
  chatbot behavior.
- Argus preserves the expected CI voice and does not become robotic or bland.
- Vulcan and other ELT profiles stay within their role cards and routing rules.
- No profile claims tools, memory, permissions, or authority it does not have.
- Fresh-session output confirms the new prompt context is actually loaded.

## Rollback

- Restore previous prompt, profile, model, memory, or session files.
- Run the fresh-session reset required for the affected profile.
- Re-run runtime checks if Telegram, gateway, or profile state changed.

## Notes

File inspection is not enough for persona changes. The live or fresh-prompt
answer is the evidence.
