# Chow Tracking

Last updated: 2026-06-16

This file is the persistent operational dashboard for Chowmes.

## Current State

- Runtime: Hostinger VPS, Hermes in Docker container `hermes`
- Telegram: configured and running
- Default model provider: OpenRouter
- Default model: `google/gemini-2.5-flash`
- Context length override: `65536`
- Direct Google routing: not active because no `GOOGLE_API_KEY` or `GEMINI_API_KEY` is present on the VPS
- Deep work model: `anthropic/claude-sonnet-4.6`
- Telegram mode: fast mode
- Local Ollama/Gemma: disabled

## Security Audit

Sanitized key check:

- `/root/.hermes/.env`: exists
- Container env path: `/opt/data/.env`
- `TELEGRAM_BOT_TOKEN`: set
- `OPENROUTER_API_KEY`: set
- `GOOGLE_API_KEY`: not set
- `GEMINI_API_KEY`: not set
- `/opt/data/workspace/.env.local`: missing

Listening ports:

- `127.0.0.1:9119`: Hermes dashboard, localhost-only
- `0.0.0.0:22` and `[::]:22`: SSH
- local DNS resolver ports on `127.0.0.53` and `127.0.0.54`

Firewall:

- UFW active
- Default incoming policy: deny
- Public allowed port: `22/tcp` only

SSH:

- `PermitRootLogin no`
- `PasswordAuthentication no`
- `KbdInteractiveAuthentication no`
- `PubkeyAuthentication yes`
- `AllowUsers chowmesadmin`

## Model And Pricing Snapshot

OpenRouter API snapshot from 2026-06-16:

- `google/gemini-2.5-flash`: $0.30 input / $2.50 output per 1M tokens
- `google/gemini-3.1-flash-lite`: $0.25 input / $1.50 output per 1M tokens
- `anthropic/claude-sonnet-4.6`: $3 input / $15 output per 1M tokens
- `google/gemini-3-flash-preview`: $0.50 input / $3 output per 1M tokens
- `openai/gpt-5.4-mini`: $0.75 input / $4.50 output per 1M tokens
- `openai/gpt-5.4`: $2.50 input / $15 output per 1M tokens

OpenRouter model directory checked on 2026-06-16 confirms `google/gemini-2.5-flash` is available. The pasted playbook target `gemini-1.5-flash` is stale for Chowmes.

## Config Optimizations Applied

Config backup:

- `/opt/data/config.yaml.bak.playbook-20260616054509`
- `/opt/data/config.yaml.bak.context-fix-20260616054719`
- `/opt/data/config.yaml.bak.gemini25flash-20260616055447`

Applied runtime settings:

```yaml
model:
  provider: openrouter
  default: google/gemini-2.5-flash
  api_mode: chat_completions
  context_length: 65536

compression:
  enabled: true
  threshold: 0.80
  target_ratio: 0.20

memory:
  memory_enabled: true
  user_profile_enabled: true
  write_approval: true
  memory_char_limit: 2200
  user_char_limit: 1375
  provider: ""

security:
  redact_secrets: true
```

Notes:

- Hermes represents built-in memory with `memory.provider: ""`, not `built-in`.
- Direct Google routing was not activated because no direct Gemini API key exists on the VPS.
- The requested `32768` context value was attempted, but Hermes rejected it because Hermes Agent requires at least `64000`. The live config uses `65536`.
- Dashboard remains localhost-only with empty `dashboard.public_url`.

## Telegram Fast Mode

Enabled Telegram tools:

- web
- vision
- skills
- todo
- memory
- clarify

Disabled Telegram tools:

- browser
- terminal
- file
- code execution
- image generation
- text-to-speech
- session search
- delegation
- cron jobs
- messaging
- computer use

## Fresh Session Helper

Installed:

```text
/opt/data/workspace/scripts/chow-fresh-telegram-session
```

Purpose:

- Back up `/opt/data/sessions/sessions.json`
- Reset it to `{}`
- Force the next Telegram interaction to start from fresh loaded context

## Next Decisions

1. Add a direct `GEMINI_API_KEY` or `GOOGLE_API_KEY` if direct Google routing is still desired.
2. After a direct key is added, switch fast mode to:

```yaml
model:
  provider: google
  default: gemini-2.5-flash
  context_length: 65536
```

3. Keep OpenRouter available for Claude/Sonnet deep work.
4. Do not connect the full Obsidian vault. Start with a curated Chowmes knowledge folder.
