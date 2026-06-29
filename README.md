# Chowmes

Chowmes is Arijit's private Hermes Agent workspace: the operating home for Athena, also called Athena, a personal AI work OS, architect partner, founder partner, second brain, confidant, and challenger.

The repo contains the human-readable source of truth for Athena's identity, Arijit's working preferences, durable project memory, Chowmes operating runbooks, and local reference material for the Hermes Agent documentation.

## What This Repo Contains

- `SOUL.md`: Athena's core identity, personality, voice, trust model, and operating posture.
- `USER.md`: Arijit's durable collaboration preferences and communication style.
- `MEMORY.md`: compressed project memory, operating facts, durable lessons, and safety rules.
- `AGENTS.md`: instructions for Codex or other agents working inside this workspace.
- `CHOWMES.md`: operational runbook for the Hostinger VPS running Hermes.
- `CHOW_TRACKING.md`: current state, audits, model choices, and optimization notes.
- `HERMES_CONFIGS.md`: map of which configuration belongs where.
- `OBSIDIAN.md`: policy and paths for using the local Obsidian `MyOS` vault as the central source of truth.
- `scripts/`: helper scripts for Chowmes operations.
- `reference/hermes-agent-docs/`: local snapshot of official Hermes Agent docs for local-first lookup.

## Core Idea

Athena is not a chatbot. She is designed to help Arijit think, build, decide, and execute with continuity.

Her operating style:

- challenge weak assumptions and vague ideas
- turn raw thoughts into systems, architecture, requirements, and milestones
- verify facts before asserting them
- separate fact, inference, and judgment
- use a sharp, witty, layered voice instead of sterile assistant-speak
- learn from corrections and convert lessons into better memory, rules, and workflows

Chowmes is the infrastructure and runtime. Athena is the agent.

## Safety Rules

Do not commit secrets. This repo intentionally ignores local `.env` files, tunnel logs, and runtime pid files.

Keep these out of Git:

- API keys
- Telegram bot tokens
- SSH keys
- VPS passwords
- OpenRouter keys
- private Obsidian vault contents
- raw session dumps unless explicitly sanitized

## Hermes Docs Policy

For Hermes Agent questions, use the local docs first:

```sh
rg -n "search terms" reference/hermes-agent-docs
```

If the answer is missing locally or depends on current upstream behavior, then check the official docs:

- https://hermes-agent.nousresearch.com/docs/
- https://hermes-agent.nousresearch.com/docs/skills/

## VPS Policy

Start with read-only inspection. Confirm before risky operations such as firewall changes, public exposure, credential rotation, deletion, SSH config changes, or long installs.

The Hermes dashboard and model endpoints should remain localhost-only unless Arijit explicitly accepts the risk.

## Current Direction

Chowmes runs Hermes on a Hostinger VPS using direct Gemini by default. Telegram operator mode is intentionally bounded: web, terminal, file, vision, skills, todo, memory, clarify, and cronjob are enabled; code execution, TTS, delegation, and session search stay disabled unless deliberately enabled later. OpenRouter remains historical/backup only unless Arijit explicitly reopens it.
