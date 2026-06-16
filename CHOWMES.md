# Chowmes Hermes Runbook

Chowmes is the Hostinger VPS running Hermes Agent for Telegram and agent work.

## Current model setup

Hermes now uses OpenRouter directly. Local Ollama/Gemma on the Mac is disabled and should not be restarted unless explicitly requested.

- Default Telegram/Hermes model: `google/gemini-2.5-flash`
- Provider: OpenRouter
- Context length override: `65536`
- Deep/delegated work model: `anthropic/claude-sonnet-4.6`
- OpenRouter key location on host: `/root/.hermes/.env`
- OpenRouter key location in container: `/opt/data/.env`
- Direct Google/Gemini key: not configured on VPS
- Local Ollama tunnel: not required

Note: `32768` was tested on June 16, 2026, but Hermes Agent rejected it because the runtime requires at least `64000`. Use `65536` unless upstream behavior changes.

Verified on June 16, 2026:

```text
Model:    google/gemini-2.5-flash
Provider: OpenRouter
Telegram: configured and gateway running
```

OpenRouter pricing checked on June 16, 2026:

- `google/gemini-2.5-flash`: $0.30 per 1M input tokens, $2.50 per 1M output tokens
- `anthropic/claude-sonnet-4.6`: $3 per 1M input tokens, $15 per 1M output tokens
- `google/gemini-3.1-flash-lite`: $0.25 per 1M input tokens, $1.50 per 1M output tokens

Recommended routing:

- Use `google/gemini-2.5-flash` for normal Telegram conversation and day-to-day tasks.
- Use `anthropic/claude-sonnet-4.6` for hard planning, architecture, research, debugging, and strategic work.
- Consider `google/gemini-3.1-flash-lite` only if Telegram volume becomes high and cost matters more than answer quality.

## Telegram fast mode

Telegram is configured for fast everyday use, not maximum autonomous agent depth on every message.

Current fast-mode settings:

- `agent.max_turns`: `12`
- `agent.gateway_notify_interval`: `60`
- Enabled Telegram tools: web, vision, skills, todo, memory, clarify
- Disabled Telegram tools: browser, terminal, file, code execution, image generation, text-to-speech, session search, delegation, cron jobs, cross-platform messaging, computer use

Reason: previous Telegram turns were slow because Hermes made many model/tool calls per message, including large session searches and text-to-speech. A direct OpenRouter test responds quickly; the slowdown came from agent orchestration overhead.

For deep work, switch model deliberately:

Inside Telegram or another Hermes chat, switch deliberately when needed:

```text
/model openrouter:anthropic/claude-sonnet-4.6
/model openrouter:google/gemini-2.5-flash
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
- Enabling Telegram terminal, file, or code execution tools.

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
