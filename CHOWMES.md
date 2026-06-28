# Chowmes Hermes Runbook

Chowmes is the Hostinger VPS running Hermes Agent for Telegram and agent work.

## Current live snapshot

Verified on June 26, 2026 from the Hostinger VPS.

| Area | Confirmed live state |
|---|---|
| Host | `chowmes` |
| Containers | `hermes`, `caddy`, `scout`, `temporal`, `temporal-ui`, `temporal-db`, `ac2-lab-backend` |
| Public ports | `22/tcp`, `80/tcp`, `443/tcp` allowed by UFW |
| Local-only ports | Hermes dashboard `127.0.0.1:9119`, Temporal `127.0.0.1:7233`, Temporal UI `127.0.0.1:8088`, Scout `127.0.0.1:8421`, AC2 lab backend `127.0.0.1:8787` |
| Active provider/model | OpenRouter `deepseek/deepseek-v4-pro` |
| Active context length | `131072` |
| Active max turns | `6` |
| Active web backend | `parallel` |
| Active gateways | Default Athena gateway running; Vulcan profile gateway running |
| On-demand profiles | Arjuna, Kubera, and Prometheus profiles exist but were not reported as active gateways |

The older notes below are historical unless they match this verified snapshot. In particular, do not repeat the old "only SSH is public" statement without rechecking UFW and Caddy.

## Current model setup

Hermes now uses OpenRouter directly. Local Ollama/Gemma on the Mac is disabled and should not be restarted unless explicitly requested.

- Default Telegram/Hermes workhorse model: `deepseek/deepseek-v4-pro`
- Provider: OpenRouter
- Context length override: `131072` live as of June 26, 2026
- Deep/delegated judgment model: `anthropic/claude-sonnet-4.6`
- OpenRouter key location on host: `/root/.hermes/.env`
- OpenRouter key location in container: `/opt/data/.env`
- Direct Google/Gemini key: configured on VPS as `GEMINI_API_KEY` in `/opt/data/.env`
- Local Ollama tunnel: not required

Note: `32768` was tested on June 16, 2026, but Hermes Agent rejected it because the runtime requires at least `64000`. That is a minimum requirement, not the desired cap. A previous target used `1048576`, but the currently verified live value is `131072`; verify before changing.

Verified on June 16, 2026:

```text
Model:    deepseek/deepseek-v4-pro
Provider: OpenRouter
Telegram: configured and gateway running
```

OpenRouter pricing checked on June 16, 2026:

- `deepseek/deepseek-v4-flash`: $0.098 per 1M input tokens, $0.196 per 1M output tokens
- `deepseek/deepseek-v4-pro`: $0.435 per 1M input tokens, $0.87 per 1M output tokens
- `moonshotai/kimi-k2.7-code`: $0.75 per 1M input tokens, $3.50 per 1M output tokens
- `google/gemini-2.5-flash`: $0.30 per 1M input tokens, $2.50 per 1M output tokens
- `anthropic/claude-sonnet-4.6`: $3 per 1M input tokens, $15 per 1M output tokens
- `anthropic/claude-opus-4.8`: $5 per 1M input tokens, $25 per 1M output tokens
- `openai/gpt-5.5`: $5 per 1M input tokens, $30 per 1M output tokens

Recommended routing:

- Use `deepseek/deepseek-v4-flash` for fast low-risk work: quick Telegram replies, cleanup, extraction, titles, compression, and cheap side tasks.
- Use `deepseek/deepseek-v4-pro` as the default workhorse for normal Athena/Hermes reasoning, project scans, research synthesis, and bulk serious work.
- Use `anthropic/claude-sonnet-4.6` for trusted coding, judgment escalation, architecture, strategy, complex debugging, security-sensitive planning, and delegated deep work.
- Use `moonshotai/kimi-k2.7-code` only as an experimental open coding comparison, not as the trusted Chowmes coding lane.
- Use `anthropic/claude-opus-4.8` only for final boardroom review of expensive, risky, or company-level decisions.
- Use `openai/gpt-5.5` as a non-Claude frontier second opinion when useful.
- Keep `google/gemini-2.5-flash` for vision or multimodal fallback because DeepSeek V4 Pro is text-only on OpenRouter.

Model aliases configured in Hermes:

```text
/model fast        -> openrouter:deepseek/deepseek-v4-flash
/model workhorse   -> openrouter:deepseek/deepseek-v4-pro
/model coding      -> openrouter:anthropic/claude-sonnet-4.6
/model kimi-code   -> openrouter:moonshotai/kimi-k2.7-code
/model judge       -> openrouter:anthropic/claude-sonnet-4.6
/model boardroom   -> openrouter:anthropic/claude-opus-4.8
/model gpt-review  -> openrouter:openai/gpt-5.5
/model vision      -> openrouter:google/gemini-2.5-flash
```

Operating rule: DeepSeek handles volume, frontier models handle authority. DeepSeek can draft and reason, but production infrastructure, security, credentials, destructive actions, major architecture, and CEO/company strategy need frontier review before being treated as final.

## Telegram operator mode

Telegram is now configured for deeper operator workflows. On June 16, 2026, Arijit explicitly approved enabling Telegram `terminal`, `file`, and `cronjob` tools.

Current Telegram settings:

- `agent.max_turns`: `12`
- `agent.gateway_notify_interval`: `60`
- Enabled Telegram tools: web, terminal, file, vision, skills, todo, memory, clarify, cronjob
- Disabled Telegram tools: browser, code execution, image generation, text-to-speech, session search, delegation, cross-platform messaging, computer use

Reason: Arijit wants Athena/Hermes to operate as an AI employee and run scheduled or file-backed workflows from Telegram. Keep code execution, delegation, session search, and TTS disabled unless separately approved.

Reliability rule: Telegram can start operator work, receive progress, and receive compact artifact links. It should not be the place where Athena repairs dependencies, rewrites skills, runs broad exploratory diagnostics, or carries full raw reports through the chat history. If a Telegram task hits repeated tool errors, API interruptions, or the 12-turn iteration limit, stop the task, preserve artifacts, patch the skill or runtime from Codex/local operator mode, then refresh the Telegram session if the DM context is bloated.

## Web access

Hermes has native `web_search` and `web_extract` tools. For Chowmes/Athena, the preferred premium web provider is Parallel because it supports AI-native search, extraction, deep research, enrichment, FindAll-style discovery, and monitoring.

Installed on June 16, 2026:

- Hermes skill: `research/parallel-cli`
- Location in container: `/opt/data/skills/research/parallel-cli/SKILL.md`
- CLI package: `parallel-web-cli`
- CLI wrapper: `/usr/local/bin/parallel-cli`
- Persistent CLI install: `/opt/data/tools/parallel-web-cli`
- Status: installed, authenticated by `PARALLEL_API_KEY`, and verified with a live JSON search
- Active provider credential: `PARALLEL_API_KEY` configured in the VPS Hermes environment.
- Active web backend: `parallel`
- Verification: standalone Hermes web tools reported `Web backend: parallel` and a live Parallel search smoke test returned results.

Recommended operating model:

- Use native Hermes `web_search` and `web_extract` for normal Telegram web lookups.
- Keep `PARALLEL_API_KEY` in the VPS Hermes environment and `web.backend: parallel`.
- Use the `parallel-cli` skill for deeper research workflows that specifically need Parallel's CLI features, monitors, FindAll, enrichment, or async research jobs.
- Telegram `terminal`, `file`, and `cronjob` are enabled by explicit approval from Arijit. Keep `code_execution`, delegation, session search, and TTS disabled unless separately approved.

Permission lesson:

- The Docker gateway drops privileges and runs as the `hermes` user.
- `/opt/data` is Hermes' home and must be traversable by `hermes`.
- Do not run Hermes CLI runtime commands as root inside the container. Use `s6-setuidgid hermes ...` for status checks, send tests, session edits, and web backend smoke tests.
- After editing `/opt/data/.env`, `/opt/data/config.yaml`, or syncing files with `sudo docker exec`, verify ownership and gateway status.
- Safe expected state: `/opt/data` owned by `hermes:hermes`, `.env` mode `600`, `config.yaml` mode `640`, gateway status running.
- If Telegram goes silent after a gateway restart and logs show `PermissionError`, check the exact path. Known paths include `/opt/data/.env` and `/opt/data/pairing/telegram-approved.json`. Restore ownership with `chown -R hermes:hermes /opt/data`, keep `.env` at `600`, restart the gateway, and verify with a Telegram send test run as `hermes`.
- Use `scripts/chowmes-health-check --repair --send-test` after env/config/session/gateway changes. It checks permissions as the `hermes` user, gateway status, Parallel web backend, recent permission errors, and Telegram delivery.

## Media and knowledge wiki

Chowmes has a local working wiki before Obsidian is connected:

```text
/opt/data/workspace/Knowledge
```

Obsidian is now the intended central source of truth. The local Mac vault is:

```text
/Users/arijitchowdhury/Dropbox/AI-Development/Personal/Obsidian-Vault/MyOS
```

Live Hermes reads and writes the VPS mirror at:

```text
/opt/data/knowledge/obsidian/MyOS
```

Generated Hermes notes should default to:

```text
/opt/data/knowledge/obsidian/MyOS/Chowmes-Inbox
```

Use `scripts/sync-obsidian-to-hermes` to refresh the VPS mirror from the Mac vault and `scripts/sync-obsidian-inbox-from-hermes` to pull generated inbox notes back into the local Obsidian vault.

### Competitive Intelligence sync safety

The Competitive Intelligence workspace has runtime-only artifacts that must not be deleted by vault syncs:

```text
/opt/data/knowledge/obsidian/MyOS/Projects/Competitive Intelligence/artifacts/competitive-research/ci.sqlite
/opt/data/knowledge/obsidian/MyOS/Projects/Competitive Intelligence/artifacts/competitive-research/raw/
```

Use `scripts/sync-competitive-intelligence-to-hermes` when syncing only the CI project. The broad `scripts/sync-obsidian-to-hermes` also preserves these paths before replacing the MyOS mirror. If either artifact is missing, rebuild the ledger from the latest daily collection before trusting quiet-day reports.

Current CI stabilization evidence from June 26, 2026:

```text
ci_sqlite_bytes=483328
raw_files=1
daily resume: 0 material signals, quality 1.00
weekly wrapper: Markdown, HTML, and PDF generated
```

## My OS team and agent structure

Current canonical My OS notes live in the Obsidian vault under:

```text
MyOS/Projects/My OS/
```

As of June 19, 2026, the current decision is:

- Athena is the CEO/orchestrator and synthesis layer.
- ELT roles are company-level advisors, not copied into every project workspace.
- Some ELT roles have become live Hermes profiles because they need persistent role memory, evolving judgment, and repeated founder/advisor dialogue.
- Persistent memory and independent judgment alone can justify a live profile; distinct tools are not required.
- Workspaces still receive execution roles, not their own mini C-suite.

Current existing advisory profiles as of June 20, 2026:

- Athena: CEO/orchestrator, default Hermes profile and primary Telegram agent.
- Vulcan: CTO, profile `vulcan`.
- Arjuna: Product / UX Strategy, profile `arjuna`.
- Kubera: Revenue / Business, profile `kubera`.
- Prometheus: Legal / Risk, profile `prometheus`.

COO, CFO, and CMO remain role cards for now. COO becomes live only after recurring operating loops need a separate operator memory.

Do not confuse "gateway stopped" with "profile does not exist." Some advisor gateways may be started only when needed. Athena should answer "Vulcan" when Arijit asks who the CTO is, and should route technical critique to the `vulcan` profile when live collaboration is needed.

New canonical My OS files:

```text
Projects/My OS/14-agent-communication-model.md
Projects/My OS/15-elt-agent-research.md
Projects/My OS/16-role-agent-build-plan.md
Projects/My OS/templates/role-agent-charter-template.md
Projects/My OS/templates/athena-delegation-packet-template.md
```

Installed media tooling:

- FFmpeg on the VPS host.
- FFmpeg in the Hermes container.
- yt-dlp in the Hermes container.
- `youtube-knowledge` skill in Hermes at `/opt/data/skills/youtube-knowledge`.
- `youtube-knowledge` skill in Codex at `~/.codex/skills/youtube-knowledge`.

Use `youtube-knowledge` to capture YouTube captions/metadata into raw and synthesized markdown notes. Keep raw captures and synthesis separate. Do not paste full copyrighted transcripts into chat.

Hermes video skill research:

- No standalone official `ffmpeg` skill was found.
- Use FFmpeg directly for quick media editing operations.
- Installed relevant skills: `ascii-video`, `manim-video`, `youtube-content`, `songsee`.
- Optional relevant skills available in the image: `hyperframes`, `kanban-video-orchestrator`.

## Visual explainer skill

Installed skill:

```text
/opt/data/skills/sketch-explainer
```

Local companion installs:

```text
~/.codex/skills/sketch-explainer
~/.claude/skills/sketch-explainer
```

Use for whiteboard-style visual explanations, diagram prompts, and optional generated sketch images. The installed copies exclude local `.env` files and macOS metadata. Image generation uses `GEMINI_API_KEY` or `GOOGLE_API_KEY` from the runtime environment or approved local env files; otherwise the skill should still return the structured breakdown and copy-pasteable prompt.

For deep work, switch model deliberately:

Inside Telegram or another Hermes chat, switch deliberately when needed:

```text
/model judge
/model workhorse
/model fast
/model boardroom
```

## Memory policy

Current built-in memory policy:

- Built-in memory: enabled
- User profile: enabled
- External memory provider: none
- Context engine: compressor
- Memory write approval: enabled during tuning
- `MEMORY.md` limit: 2200 chars
- `USER.md` limit: 1375 chars
- Context engine: compressor
- Compression threshold: 80%
- Compression target ratio: 20%

Keep `MEMORY.md` small and curated. Do not use it as transcript storage. Keep session search disabled in normal Telegram mode.

## Admin permission model

Allowed by default for Chowmes admin work:

- Read server status, logs, and config.
- Check Docker, SSH, firewall, and tunnel state.
- Back up config before editing.
- Restart Hermes after config-only changes.
- Update runbooks and local configuration docs.
- Run bounded smoke tests.

Requires explicit approval:

- Public ports or firewall changes.
- Deleting data or sessions.
- Rotating credentials.
- Changing SSH configuration.
- Heavy installs.
- Broad personal-data access.
- Connecting the full Obsidian vault.
- Enabling local LLMs.
- Enabling Telegram code execution tools.

## Tracking file

Persistent operational tracking lives at:

```text
/opt/data/workspace/CHOW_TRACKING.md
```

Local source copy:

```text
CHOW_TRACKING.md
```

## VPS install

- Source checkout: `/opt/hermes-agent`
- Runtime compose directory: `/opt/chowmes`
- Data/config volume: `/root/.hermes`
- Container: `hermes`
- Dashboard: `http://127.0.0.1:9119` on the VPS only

## Security baseline

- SSH user: `chowmesadmin`
- SSH key: `~/.ssh/chowmes_ed25519`
- Root SSH login: disabled
- SSH password login: disabled
- Firewall: UFW enabled; only TCP 22 is public
- Brute-force protection: fail2ban enabled for SSH
- Security updates: unattended-upgrades enabled
- Docker admin commands require `sudo`
- Dashboard and any model ports must remain localhost-only on the VPS
- Telegram uses polling mode; no Telegram webhook or public web port is open

## Local Ollama status

Local Ollama/Gemma was removed because it made the laptop slow and unusable.

Do not:

- Start Ollama
- Pull Gemma models
- Open the chowmes Ollama tunnel
- Reconfigure Telegram back to a local model

Only revisit local models if explicitly requested later.

## Useful checks

Check live Hermes status:

```sh
/Users/arijitchowdhury/.codex/skills/hostinger-vps-ssh/scripts/ssh-hermes-vps "sudo docker exec hermes hermes status"
```

Check the active model config:

```sh
/Users/arijitchowdhury/.codex/skills/hostinger-vps-ssh/scripts/ssh-hermes-vps "sudo docker exec hermes python3 -c 'import yaml,json; c=yaml.safe_load(open(\"/opt/data/config.yaml\")); print(json.dumps({\"model\": c.get(\"model\"), \"delegation\": c.get(\"delegation\")}, indent=2))'"
```

Run a tiny OpenRouter smoke test:

```sh
/Users/arijitchowdhury/.codex/skills/hostinger-vps-ssh/scripts/ssh-hermes-vps "sudo docker exec hermes hermes -z 'Reply exactly: openrouter hermes online'"
```

## Fresh Telegram session

`/restart` does not clear Telegram prompt state. It restarts the gateway and preserves the active Telegram session.

`/reset` is not the Chowmes-approved fix for this deployment unless Hermes upstream explicitly documents it and it is verified against `sessions.json`. The reliable reset path is the local script below because it clears the Telegram DM session pointer, deletes the stale Hermes session, restarts the gateway, and leaves an auditable command trail.

After changing `SOUL.md`, `USER.md`, `MEMORY.md`, model routing, or Telegram context, run:

```sh
./scripts/chow-fresh-telegram-session
```

This removes AC's Telegram DM session pointer, deletes the stale Hermes session when present, and restarts the gateway. The next Telegram message creates a fresh session that snapshots the current `SOUL.md`, `/root/.hermes/memories/USER.md`, `/root/.hermes/memories/MEMORY.md`, and workspace `AGENTS.md`.

If Telegram still answers with the old identity, do not re-check only `SOUL.md` and call it fixed. Check the active routing pointer and stale session:

```sh
/Users/arijitchowdhury/.codex/skills/hostinger-vps-ssh/scripts/ssh-hermes-vps "sudo docker exec hermes sh -lc 'cat /opt/data/sessions/sessions.json; /opt/hermes/.venv/bin/hermes sessions list | head -n 80'"
```

The known failure pattern is a Telegram DM key like `agent:main:telegram:dm:<chat_id>` still pointing at an old session id. Delete that session and clear the pointer:

```sh
/Users/arijitchowdhury/.codex/skills/hostinger-vps-ssh/scripts/ssh-hermes-vps "sudo docker exec hermes sh -lc '/opt/hermes/.venv/bin/hermes sessions delete <session_id> --yes || true; python3 -c '\''import json; p=\"/opt/data/sessions/sessions.json\"; d=json.load(open(p)); d.pop(\"agent:main:telegram:dm:6789423537\", None); open(p,\"w\").write((json.dumps(d, indent=2) if d else \"{}\")+\"\\n\")'\''; /opt/hermes/.venv/bin/hermes gateway restart; cat /opt/data/sessions/sessions.json'"
```

Then verify with both a fresh-prompt smoke test and a fresh Telegram message:

```sh
/Users/arijitchowdhury/.codex/skills/hostinger-vps-ssh/scripts/ssh-hermes-vps "sudo docker exec hermes sh -lc '/opt/hermes/.venv/bin/hermes -z \"What is your name? Reply with only the name.\"'"
```

```text
What's your name?
```

Only call the fix complete after the live answer is correct. File contents alone are necessary evidence, not sufficient evidence.

## Context-limit incident response

Known failure pattern from June 16-17, 2026:

- The active Telegram DM session reached roughly 143K prompt tokens.
- Gateway logs showed repeated `Iteration budget exhausted (12/12)` and `Interrupted during API call`.
- The competitive-research workflow had been asked to install/repair Parallel, execute the skill, update the skill library, and redesign the report from inside the same Telegram thread.
- Telegram delivery, gateway status, permissions, web backend, and direct model smoke tests were healthy, so the failure was session/tool-loop bloat rather than a dead bot.
- After the fresh session reset, outbound Telegram still worked but inbound DMs did not create a new session. The owner approval file `/opt/data/pairing/telegram-approved.json` was missing. Restore Telegram owner approval from `TELEGRAM_ALLOWED_USERS` / `TELEGRAM_HOME_CHANNEL` as part of repair, then verify inbound with a fresh DM.

Response loop:

1. Inspect live status and logs first.
2. Identify the workflow or skill that expanded the context.
3. Patch that skill so future Telegram runs are bounded, artifact-first, and fail closed on dependency/auth/path problems.
4. Run `scripts/chowmes-health-check --repair --send-test`; this now restores missing Telegram owner approval files and verifies they exist.
5. If the active Telegram session is oversized or stale, ask Arijit for approval and run `./scripts/chow-fresh-telegram-session`; this now preserves/restores owner approval while clearing only the stale DM session.
6. Verify both directions: direct send test plus a fresh inbound Telegram DM that creates a new `agent:main:telegram:dm:<chat_id>` session.

Verify in Telegram:

```text
who are you and what do you know about me
```

## Dashboard access

From this Hermes directory on the Mac:

```sh
./scripts/chowmes-dashboard-tunnel --background
```

Then open:

```text
http://127.0.0.1:9119
```

Stop the dashboard tunnel:

```sh
kill "$(cat .chowmes-dashboard-tunnel.pid)"
```

Manual tunnel equivalent:

```sh
ssh -i ~/.ssh/chowmes_ed25519 -L 9119:127.0.0.1:9119 chowmesadmin@72.61.72.147
```

## Telegram setup

Hermes Telegram requires:

- `TELEGRAM_BOT_TOKEN`: created with Telegram `@BotFather`
- `TELEGRAM_ALLOWED_USERS`: owner numeric Telegram user ID
- `TELEGRAM_HOME_CHANNEL`: owner DM numeric Telegram user ID

Keep the allowlist set. If it is empty, anyone who finds the bot can use it.

Current state:

- Bot username: `chowmes_bot`
- Telegram is configured on chowmes.
- `TELEGRAM_ALLOWED_USERS` is set to the owner numeric Telegram user ID.
- `TELEGRAM_HOME_CHANNEL` is set to the owner DM.
- Gateway uses Telegram polling mode.

After Telegram env changes, restart Hermes:

```sh
/Users/arijitchowdhury/.codex/skills/hostinger-vps-ssh/scripts/ssh-hermes-vps "cd /opt/chowmes && sudo docker compose restart hermes"
```
