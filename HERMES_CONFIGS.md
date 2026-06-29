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
- Active Obsidian vault path for live Hermes: `/opt/data/knowledge/obsidian/MyOS`
- Persistent workspace for project guidance: `/opt/data/workspace`

The local Dropbox project folder and Obsidian vault are the editable source-of-truth for human-readable project files. The VPS has the active copies that Telegram uses.

Important session behavior:

- `SOUL.md`, `USER.md`, `MEMORY.md`, and project context are snapshotted when a session starts.
- `/restart` restarts the gateway but preserves the active Telegram session.
- Existing Telegram sessions can keep stale prompt context after config changes.
- Run `scripts/chow-fresh-telegram-session` after identity, memory, model, or Telegram context changes.

## What belongs in SOUL.md

Put stable identity and behavior here:

- The agent is Athena, also called Athena, Arijit's AI employee, co-founder partner, and senior software architect.
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
- He wants Athena to challenge him, interview him, and improve ideas.
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

Use `memory.write_approval: true` while Athena/Chowmes is being tuned so bad assumptions do not get silently saved.

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

Stacking rule:

- Gemini Flash handles volume.
- Gemini Pro handles authority.
- Context length override: `131072`, verified live as of June 29, 2026.

Default workhorse:

- Direct Gemini API `gemini-2.5-flash`
- Use for normal Athena/Hermes reasoning, project scans, research synthesis, CI synthesis, web extraction, vision, compression, titles, and low-risk auxiliary work.

Judgment escalation:

- Direct Gemini API `gemini-2.5-pro`
- Use for architecture, strategy, complex debugging, security-sensitive planning, boardroom review, and delegated deep work.

Future model candidates:

- Z.ai / GLM is supported by Hermes provider id `zai`, aliases `glm`, `z-ai`, `z.ai`, and `zhipu`, but no `ZAI_API_KEY` / `GLM_API_KEY` is currently configured.
- Direct DeepSeek is supported by Hermes provider id `deepseek`, but no `DEEPSEEK_API_KEY` is currently configured.
- Do not route production Chowmes through OpenRouter while the active policy is "forget OpenRouter".

Disabled for now:

- Local Ollama/Gemma on the Mac.
- The old local model tunnel.

Direct Google:

- `GEMINI_API_KEY` is present on the VPS and is the active route.
- Use provider id `gemini` in config. `google`, `google-gemini`, and `google-ai-studio` are Hermes aliases, but `gemini` is the canonical live config value.
- Do not use stale `gemini-1.5-flash` for Chowmes.

## Web access policy

Hermes native web tools:

- `web_search`: web search.
- `web_extract`: page/PDF extraction into markdown.

Preferred premium provider for Chowmes:

- Parallel.
- Rationale: search, extraction, deep research, enrichment, entity/list discovery, monitoring, and structured agent-friendly output.

Current installed research skill:

- `research/parallel-cli` at `/opt/data/skills/research/parallel-cli/SKILL.md`.

Active configuration:

```yaml
web:
  backend: parallel
```

Active credential:

```text
PARALLEL_API_KEY=<set in VPS Hermes environment, never in markdown>
```

Do not store API keys in this file. Normal Telegram research should use the native `web` toolset; the `parallel-cli` skill is for deliberate deep-research workflows, monitors, FindAll, enrichment, or async research jobs. Telegram `terminal`, `file`, and `cronjob` are enabled by explicit approval from Arijit; keep Telegram `code_execution` disabled unless separately approved.

Parallel CLI runtime:

```text
/usr/local/bin/parallel-cli
/opt/data/bin/parallel-cli
/opt/data/tools/parallel-web-cli
```

System `python3` in the Hermes container has `python3-yaml` installed, so the `competitive-research` scripts work with their documented commands, for example `python3 scripts/setup-monitors.py --dry-run` and `python3 scripts/daily-research-run.py --dry-run`, when run as the `hermes` user. The `parallel-cli` wrapper loads `PARALLEL_API_KEY` from `/opt/data/.env`; raw Python processes do not automatically expose that key in `os.environ`.

When changing the VPS Hermes environment:

- Preserve the canonical env var name `PARALLEL_API_KEY`.
- Keep `/opt/data/.env` private with mode `600`.
- Keep `/opt/data` owned by `hermes:hermes`, because the gateway runs as `hermes`.
- After any `.env` or config edit, verify gateway status and a Telegram delivery smoke test as the `hermes` user, not root.
- Use `scripts/chowmes-health-check --repair --send-test` for the post-change check.

## Telegram speed policy

Telegram should stay bounded, but Arijit explicitly approved Telegram `terminal`, `file`, and `cronjob` tools on June 16, 2026 for deeper operator workflows.

Current Telegram profile:

- `agent.max_turns`: `12`
- Enabled: web, terminal, file, vision, skills, todo, memory, clarify, cronjob
- Disabled: browser, code execution, image generation, text-to-speech, session search, delegation, cross-platform messaging, computer use

If Telegram feels slow again, first check:

- number of API calls per turn
- tool turns per turn
- prompt size
- whether session search or text-to-speech has been re-enabled
- whether the active session needs `/new`
- whether prompt size/tool use is creating context drag despite the `131072` context override

## Operating modes

Telegram operator mode is for everyday interaction plus explicitly approved operational work:

- OpenRouter `deepseek/deepseek-v4-pro` by default, with `/model fast` available for low-risk speed/cost-sensitive replies.
- low turn budget
- bounded tools
- terminal, file, and cronjob allowed
- no code execution, TTS, delegation, or session search

Deep Architect mode is for serious project work:

- OpenRouter `anthropic/claude-sonnet-4.6` via `/model judge` or delegation
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
