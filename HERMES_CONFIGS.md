# Hermes Configuration Map

This file explains which configuration files should exist for Chowmes and what belongs in each one.

## Best-practice layout

Use a small set of focused files:

- `SOUL.md`: identity, personality, tone, and durable behavioral posture.
- `USER.md`: built-in Hermes user profile. Arijit's boss/user profile, preferences, and collaboration style.
- `MEMORY.md`: built-in Hermes durable memory. Project context, lessons, decisions, and conventions that should compound over time.
- `AGENTS.md`: workspace rules for Codex/Hermes agents working in this project.
- `CHOWMES.md`: human runbook with operational facts, commands, model choices, and security state.
- `OBSIDIAN.md`: vault access policy and knowledge-base boundaries.
- `reference/hermes-agent-docs/`: local snapshot of the official Hermes Agent docs and skills catalogs.
- `.env.local`: local secrets and SSH connection values. Never commit or print this file.
- VPS `/root/.hermes/.env`: active Hermes secrets on the VPS. Never print this file.
- VPS `/root/.hermes/config.yaml`: active Hermes runtime settings.

Avoid creating duplicate instruction files such as `.cursorrules` or `CLAUDE.md` unless a specific tool needs them. Too many overlapping instruction files make the agent inconsistent.

## Active Chowmes runtime

The active Telegram agent runs on the Hostinger VPS.

- Container path for Hermes home: `/opt/data`
- Host path for Hermes home: `/root/.hermes`
- Active identity file: `/opt/data/SOUL.md`
- Active built-in user profile: `/opt/data/memories/USER.md`
- Active built-in memory: `/opt/data/memories/MEMORY.md`
- Active runtime config: `/opt/data/config.yaml`
- Persistent workspace for project guidance: `/opt/data/workspace`

The local Google Drive folder is the editable source-of-truth for human-readable project files. The VPS has the active copies that Telegram uses.

Important session behavior:

- `SOUL.md`, `USER.md`, `MEMORY.md`, and project context are snapshotted when a session starts.
- `/restart` restarts the gateway but preserves the active Telegram session.
- Existing Telegram sessions can keep stale prompt context after config changes.
- Run `scripts/chow-fresh-telegram-session` after identity, memory, model, or Telegram context changes.

## What belongs in SOUL.md

Put stable identity and behavior here:

- The agent is Chow, Arijit's AI employee, co-founder partner, and senior software architect.
- Communication style.
- Product and architecture posture.
- How to challenge assumptions.
- How to interview Arijit when ideas are underdefined.
- Security posture.
- Verification posture.
- High-level model posture.
- What the agent should never do without explicit approval.

Do not put secrets, host passwords, raw API keys, or long operational runbooks in `SOUL.md`.

## What belongs in USER.md

Put Arijit's durable working preferences here:

- He wants an AI employee and co-founder partner, not a chatbot.
- He wants direct, practical collaboration.
- He wants strong architectural judgment and founder judgment.
- He wants Chow to challenge him, interview him, and improve ideas.
- He does not want emojis, em dashes, fluff, filler, or apologetic language.
- He prefers research-backed recommendations when current facts matter.

Do not put private credentials, raw personal identifiers, or secrets in `USER.md`.

## What belongs in MEMORY.md

Put durable project memory here:

- Current operating facts.
- Project decisions.
- Known bugs and fixes.
- Tool choices.
- Lessons from feedback.
- Reusable conventions.
- Context that should survive across sessions.

Do not use `MEMORY.md` as a dumping ground for transcripts. Keep it compressed and useful.

Use `memory.write_approval: true` while Chowmes is being tuned so bad assumptions do not get silently saved.

## What belongs in AGENTS.md

Put operational instructions for agents working in this folder:

- Always use the Hostinger VPS SSH skill for chowmes tasks.
- Read credentials from `.env.local` without printing secrets.
- Start with read-only inspection.
- Confirm before risky admin actions.
- Use OpenRouter by default.
- Do not restart local Ollama unless explicitly asked.

Keep it direct. This file is for behavior, not storytelling.

## What belongs in reference/hermes-agent-docs

Put local copies of official Hermes Agent documentation here:

- `llms.txt`: concise index for fast lookup.
- `llms-full.txt`: full docs snapshot for local answers.
- `skills-catalogs.md`: bundled and optional skill catalog excerpt.
- `skills-hub.html`: saved Skills Hub page shell.
- `README.md`: source URLs, refresh command, and lookup policy.

For Hermes questions, search this folder before browsing. Browse the official docs only when the local snapshot is missing the answer, appears stale, or the question depends on current upstream behavior.

Do not treat the skills catalog as permission to install skills. Skills remain read-only research material unless Arijit explicitly asks to install, enable, or modify one.

## What belongs in CHOWMES.md

Put facts and commands here:

- Current model/provider.
- Security baseline.
- Dashboard tunnel instructions.
- Telegram setup state.
- Useful health checks.
- Known pricing snapshots with dates.
- Operational decisions and why they were made.

This file can be longer because it is a runbook.

## What belongs in config.yaml

Hermes runtime settings belong in the VPS `config.yaml`, not in markdown:

- Default model and provider.
- Delegation model.
- Toolsets.
- Gateway behavior.
- Terminal backend and working directory.
- Session/compression settings.
- Auxiliary model routing.
- MCP servers.

Do not store secrets directly in `config.yaml`; use `.env` when possible.

## Current model policy

Default:

- OpenRouter `google/gemini-2.5-flash`
- Use for Telegram, ordinary chat, quick tasks, and normal agent work.
- Context length override: `65536`

Deep work:

- OpenRouter `anthropic/claude-sonnet-4.6`
- Use for architecture, strategy, complex debugging, research synthesis, and high-stakes planning.

Disabled for now:

- Local Ollama/Gemma on the Mac.
- The old local model tunnel.

Direct Google:

- Not active until `GOOGLE_API_KEY` or `GEMINI_API_KEY` is present on the VPS.
- Use `provider: google` and `default: gemini-2.5-flash` when the key is configured.
- Do not use stale `gemini-1.5-flash` for Chowmes.

## Telegram speed policy

Telegram should be fast by default. Do not enable every tool for Telegram unless the user explicitly asks for a deep autonomous agent mode.

Current fast Telegram profile:

- `agent.max_turns`: `12`
- Enabled: web, vision, skills, todo, memory, clarify
- Disabled: browser, terminal, file, code execution, image generation, text-to-speech, session search, delegation, cron jobs, cross-platform messaging, computer use

If Telegram feels slow again, first check:

- number of API calls per turn
- tool turns per turn
- prompt size
- whether session search or text-to-speech has been re-enabled
- whether the active session needs `/new`
- whether prompt size/tool use is creating context drag despite the `65536` context override

## Operating modes

Fast Telegram mode is for everyday interaction:

- OpenRouter `google/gemini-2.5-flash`
- low turn budget
- lightweight tools
- no terminal, file access, code execution, TTS, delegation, or session search

Deep Architect mode is for serious project work:

- OpenRouter `anthropic/claude-sonnet-4.6`
- research and stronger reasoning
- broader tools only when needed and explicitly allowed
- used for architecture, strategy, complex debugging, planning, and implementation design

## Admin permission model

Allowed by default:

- read logs/status/config
- check Docker, SSH, firewall, and tunnel state
- back up config before editing
- restart Hermes after config-only changes
- update runbooks and configuration notes
- run bounded smoke tests

Requires explicit approval:

- public ports or firewall changes
- deletion of sessions/data
- credential rotation
- SSH config changes
- heavy installs
- broad personal-data access
- full Obsidian vault access
- local LLMs
- Telegram terminal/file/code execution tools

## Security policy

Public internet exposure should stay minimal:

- Public SSH only.
- Key-only SSH.
- Root SSH disabled.
- Password SSH disabled.
- UFW deny incoming by default.
- Dashboard localhost-only.
- Telegram bot allowlisted.

Any change that exposes a new public port should require explicit approval.
