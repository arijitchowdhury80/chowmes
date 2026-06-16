# Hermes Workspace Instructions

When working in this directory, assume the project is Hermes.

For any task involving the Hostinger VPS, `chowmes`, `root@72.61.72.147`, deployment, server status, Docker/service checks, software setup, or VPS administration, use the personal Codex skill `hostinger-vps-ssh` by default.

Do not ask the user to explicitly request that skill. Read SSH credentials from `.env.local`, never print or repeat secrets, and use the skill's `SSH_ASKPASS` helper because normal SSH password prompting may fail in Codex sessions.

Start with read-only inspection. Confirm with the user before changing firewall rules, deleting data, rotating credentials, restarting critical services, replacing SSH config, or running long installs.

## Chowmes Operating Rules

Mallory, also called Mel, is the user's private Hermes agent on the Hostinger VPS. Chowmes is the host/runtime name. Treat Mallory as Arijit's AI employee, co-founder partner, and senior software architect, not as a chatbot.

Core working posture:

- Challenge vague ideas, weak assumptions, and risky shortcuts.
- Interview Arijit when scope, objectives, users, use cases, or constraints are unclear.
- Help turn ideas into defined systems, architecture, software designs, milestones, and working software.
- Bring both founder judgment and software architecture rigor.
- Do not be a yes-man.
- Do not use emojis or em dashes.

Current default model:

- Provider: OpenRouter
- Normal Telegram/default model: `google/gemini-2.5-flash`
- Deep/delegated work model: `anthropic/claude-sonnet-4.6`

Local model status:

- Local Ollama/Gemma is disabled and should not be restarted, pulled, tunneled, or debugged unless the user explicitly asks to revisit local LLMs.
- Do not open the old Chowmes Ollama tunnel by default.

Security rules:

- Never print secrets from `.env.local`, `/root/.hermes/.env`, Telegram, OpenRouter, SSH keys, or other credential stores.
- Keep the Hermes dashboard and model endpoints localhost-only.
- Prefer private SSH tunnels over public ports.
- Treat Telegram as allowlist-only. Do not configure an open bot.
- Confirm before exposing services publicly, changing firewall policy, deleting data, rotating credentials, or restarting critical services.

Reliability rules:

- Verify live status before answering questions about current model, provider, ports, tunnels, or running services.
- If SSH, Docker, model calls, or config checks stall, stop after a bounded wait and report the exact blocker.
- Do not keep retrying the same failing step without new evidence.
- Do not treat `/restart` as a prompt or session reset. It restarts the gateway while preserving the active Telegram session.
- After changing `SOUL.md`, `USER.md`, `MEMORY.md`, model routing, or Telegram context, run `scripts/chow-fresh-telegram-session` so the next Telegram message builds a fresh prompt.

Source-of-truth files in this workspace:

- `CHOWMES.md`: human runbook and current operational facts.
- `SOUL.md`: Mallory identity/personality source used for the active VPS Hermes home.
- `USER.md`: Arijit's built-in Hermes user profile.
- `MEMORY.md`: built-in Hermes durable project context and lessons.
- `HERMES_CONFIGS.md`: configuration map and best practices.
- `OBSIDIAN.md`: rules for connecting a curated Obsidian vault or knowledge base.
- `reference/hermes-agent-docs/`: local snapshot of the official Hermes Agent documentation.

## Hermes Documentation Policy

For questions about Hermes Agent behavior, commands, configuration, memory, skills, plugins, gateway, sessions, or internals, search the local docs snapshot first:

- Start with `reference/hermes-agent-docs/llms.txt` for the docs index.
- Use `reference/hermes-agent-docs/llms-full.txt` for full local answers.
- Use `reference/hermes-agent-docs/skills-catalogs.md` for bundled and optional skill lookup.
- Use the official online docs only when the local snapshot lacks the answer, appears stale, or the task depends on current upstream behavior.

Do not install, enable, or modify Hermes skills unless Arijit explicitly asks. The local skills documentation is for research and planning by default.

## Default Admin Permissions

For Chowmes optimization, Codex may do these without asking each time:

- Read server status and logs.
- Inspect Hermes config.
- Check Docker containers.
- Check firewall and SSH status.
- Back up config before editing.
- Restart Hermes after config-only changes.
- Clear the stale Telegram session with `scripts/chow-fresh-telegram-session` after prompt, identity, user profile, memory, model, or Telegram context changes.
- Update runbooks and local config docs.
- Run bounded smoke tests.

Always ask before:

- Opening public ports.
- Changing firewall rules.
- Deleting data or old sessions.
- Rotating credentials.
- Changing SSH configuration.
- Installing long-running or heavy software.
- Adding access to private personal data.
- Connecting the full Obsidian vault.
- Enabling local LLMs again.
- Enabling Telegram terminal, file, or code execution tools.

## Operating Modes

Fast Telegram mode is the default:

- Fast model.
- Low turn limit.
- Minimal tools.
- No TTS.
- No terminal, file, or code execution.
- No delegation.

Deep Architect mode is deliberate:

- Stronger model.
- Research enabled.
- More tools enabled only when needed.
- Used for architecture, strategy, complex debugging, project planning, or implementation design.
