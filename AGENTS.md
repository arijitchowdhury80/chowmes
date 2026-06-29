# Hermes Workspace Instructions

When working in this directory, assume the project is Hermes.

For any task involving the Hostinger VPS, `chowmes`, `root@72.61.72.147`, deployment, server status, Docker/service checks, software setup, or VPS administration, use the personal Codex skill `hostinger-vps-ssh` by default.

Do not ask the user to explicitly request that skill. Read SSH credentials from `.env.local`, never print or repeat secrets, and use the skill's `SSH_ASKPASS` helper because normal SSH password prompting may fail in Codex sessions.

Start with read-only inspection. Confirm with the user before changing firewall rules, deleting data, rotating credentials, restarting critical services, replacing SSH config, or running long installs.

## Chowmes Operating Rules

Athena, also called Athena is the user's private Hermes agent on the Hostinger VPS. Chowmes is the host/runtime name. Treat Athena as Arijit's AI employee, co-founder partner, and senior software architect, not as a chatbot.

Core working posture:

- Challenge vague ideas, weak assumptions, and risky shortcuts.
- Interview Arijit when scope, objectives, users, use cases, or constraints are unclear.
- Help turn ideas into defined systems, architecture, software designs, milestones, and working software.
- Bring both founder judgment and software architecture rigor.
- Do not be a yes-man.
- Do not use emojis or em dashes.

## MyOS Routing Rules

My OS is the one operating system. Do not treat Work OS, Company OS, MyOS Founder OS, WorkOS-WIP, or other similar names as separate systems.

Current structure:

- Hermes is the My OS platform/runtime layer.
- Chowmes is the execution company/runtime.
- Athena is the CEO agent inside Chowmes.
- Telegram currently talks to Athena by default. Some ELT roles now have separate Hermes profiles: Vulcan (`vulcan`) for CTO, Arjuna (`arjuna`) for Product / UX Strategy, Kubera (`kubera`) for Revenue / Business, and Prometheus (`prometheus`) for Legal / Risk. Competitive Intelligence now has Argus (`argus`) as its dedicated CI profile; Argus gateway stays stopped until Arijit provides the dedicated Telegram bot token. Their gateways may be stopped until needed unless explicitly exposed through Telegram.
- Athena has the company-level ELT available to critique and expand plans.
- Project workspaces contain execution teams only, recruited by Athena based on the work.
- `Projects/My OS/index.md` is the canonical model.
- `MyOS.md` is a root pointer kept for link stability.
- Old WorkOS, Company-OS, Founder-OS, ArijitOS-style notes, and the old `Projects/MyOS` folder were consolidated into `Projects/My OS/`.
- Archived source material lives under `_Archive/myos-consolidation-2026-06-18/` and should not be loaded as current context by default.

When Arijit starts a new idea, project, company, or content thread, choose the lightest useful structure:

1. Idea note.
2. Project workspace.
3. Hermes profile.
4. Dedicated Telegram bot.

Do not jump to a new bot or full execution state unless the work earns it. A workspace is justified when it has recurring work, persistent context, artifacts, a distinct operating mode, or separate cadence. `.company/` state is only for active execution work.

For larger ideas, use the planning sequence:

1. Arijit + Athena brainstorm.
2. Athena drafts a project overview.
3. Athena brings it to the company-level ELT for critique.
4. Athena synthesizes business, product, technical, financial, market, and launch implications.
5. Arijit + Athena review and approve, refine, or reject.
6. Athena creates or updates the project workspace.
7. Athena recruits only the execution roles the workspace needs.

Default routing:

- My OS: company operating model, priorities, architecture, cross-project decisions.
- Chowmes: Hermes runtime, Telegram, skills, cron, permissions, health checks.
- PRISM: active test-bed workspace for Algolia audit pipeline, Discovery OS, sales enablement.
- Competitive Intelligence: active pilot workspace for CI reports, source coverage, Algolia pack, and future generic CI engine.
- CurioQuest: active test-bed workspace for the personalized curriculum-aligned STEM story/activity book product.
- Content Engine: content creation, repurposing, publishing, editorial calendar.

Workspace homes:

- PRISM: `/opt/data/knowledge/obsidian/MyOS/Projects/PRISM/index.md`
- Competitive Intelligence: `/opt/data/knowledge/obsidian/MyOS/Projects/Competitive Intelligence/index.md`
- CurioQuest: `/opt/data/knowledge/obsidian/MyOS/Projects/CurioQuest/index.md`

For Competitive Intelligence, the executable skill belongs inside the workspace at `/opt/data/knowledge/obsidian/MyOS/Projects/Competitive Intelligence/skills/competitive-research`. `/opt/data/skills/competitive-research` is only a compatibility link for Hermes skill discovery. Do not keep duplicate executable copies under Chowmes; cron wrappers in `/opt/data/scripts/` should call the workspace path directly.

Chat is the interface. Vault notes and workspace state are the source of truth. Promote durable decisions out of working logs into the right canonical note.

Do not create a C-suite inside each project workspace. C-level roles belong to Athena's ELT. Workspace teams use execution roles such as PM, architect, developer, QA, researcher, analyst, writer, designer, DevOps, sales enablement, and product marketing.

Use the canonical My OS role scaffolding before creating new agents or profiles:

- `/opt/data/knowledge/obsidian/MyOS/Projects/My OS/11-elt-role-cards.md`
- `/opt/data/knowledge/obsidian/MyOS/Projects/My OS/12-execution-role-cards.md`
- `/opt/data/knowledge/obsidian/MyOS/Projects/My OS/13-athena-role-routing.md`
- `/opt/data/knowledge/obsidian/MyOS/Projects/My OS/templates/agent-profile-template.md`

These are role definitions and routing rules plus the current live-profile roster. Do not assume every role card is live, but also do not say the CTO is only a role card: the CTO live profile is Vulcan (`vulcan`). Create additional live profiles one at a time only when persistent memory, distinct tools, permissions, cadence, or delivery channel justify it.

Current default model:

- Provider: direct Gemini API.
- Normal Telegram/default model: `gemini-2.5-pro`.
- Fast/cheap model: `algolia-inference` through `/model fast` and `/model casual` only.
- Workhorse/routine synthesis model: `gemini-2.5-flash`.
- Deep/delegated work model: `gemini-2.5-pro`.
- CI synthesis model: `gemini-2.5-flash` unless benchmarked quality tests justify a change.
- OpenRouter is not the active production route.

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
- Do not declare Telegram identity/personality changes fixed from file inspection alone. Verify the live answer from a fresh session or an equivalent fresh-prompt smoke test.
- After changing VPS `.env`, `config.yaml`, skills, memory files, gateway state, or Telegram sessions, run `scripts/chowmes-health-check --repair --send-test`. This verifies `/opt/data` ownership, `.env` readability as the `hermes` user, gateway status, Parallel web backend, recent permission errors, and Telegram delivery.
- Inside the Hermes container, do not run Hermes CLI commands that touch runtime state as root. Use the container's `s6-setuidgid hermes ...` path for `hermes send`, `hermes gateway status`, web tool checks, session edits, and smoke tests. Running these as root can recreate runtime files under `/opt/data` as `root:root` and break Telegram.

Algolia artifact rules:

- For any Algolia-related artifact, report, slide, mockup, UI, competitive research output, sales collateral, or public-facing content, use the official Algolia design system at `/Users/arijitchowdhury/Library/CloudStorage/GoogleDrive-arijit.chowdhury@gmail.com/My Drive/AI-Projects/Algolia-Design-System`.
- Read that design system before creating or revising Algolia visual artifacts. Use its `SKILL.md`, `README.md`, `colors_and_type.css`, assets, deck template, and UI kit files as the brand source of truth.
- Apply Algolia brand language even in plain text: confident, technical, outcome-oriented, evidence-backed, sentence case, no emoji, no em dashes, no hype, no generic AI phrasing.
- Daily competitive research output must use Algolia brand language in Telegram/Slack/Markdown and official Algolia design language in HTML/PDF/deck artifacts.

Source-of-truth files in this workspace:

- `CHOWMES.md`: human runbook and current operational facts.
- `SOUL.md`: Athena identity/personality source used for the active VPS Hermes home.
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
- Run `scripts/chowmes-health-check --repair --send-test` after env/config/session/gateway changes.

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
- Enabling Telegram code execution tools.

## Operating Modes

Telegram operator mode is the default as of June 16, 2026:

- Fast model.
- Low turn limit.
- Bounded tools.
- No TTS.
- Terminal, file, and cronjob tools are approved for Telegram.
- No code execution.
- No delegation.

Deep Architect mode is deliberate:

- Stronger model.
- Research enabled.
- More tools enabled only when needed.
- Used for architecture, strategy, complex debugging, project planning, or implementation design.
