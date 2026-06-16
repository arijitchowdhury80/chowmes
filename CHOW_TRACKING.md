# Chow Tracking

Last updated: 2026-06-16

This file is the persistent operational dashboard for Chowmes.

## Current State

- Runtime: Hostinger VPS, Hermes in Docker container `hermes`
- Telegram: configured and running
- Default model provider: OpenRouter
- Default model: `deepseek/deepseek-v4-pro`
- Context length override: `65536`
- Direct Google routing: not active because no `GOOGLE_API_KEY` or `GEMINI_API_KEY` is present on the VPS
- Deep work / judgment model: `anthropic/claude-sonnet-4.6`
- Boardroom review model: `anthropic/claude-opus-4.8`
- GPT second-opinion model: `openai/gpt-5.5`
- Telegram mode: fast mode
- Local Ollama/Gemma: disabled
- Media tools: FFmpeg installed on VPS host and Hermes container; yt-dlp installed in Hermes container
- Local wiki: `/opt/data/workspace/Knowledge`

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

- `deepseek/deepseek-v4-flash`: $0.098 input / $0.196 output per 1M tokens
- `deepseek/deepseek-v4-pro`: $0.435 input / $0.87 output per 1M tokens
- `moonshotai/kimi-k2.7-code`: $0.75 input / $3.50 output per 1M tokens
- `google/gemini-2.5-flash`: $0.30 input / $2.50 output per 1M tokens
- `anthropic/claude-sonnet-4.6`: $3 input / $15 output per 1M tokens
- `anthropic/claude-opus-4.8`: $5 input / $25 output per 1M tokens
- `openai/gpt-5.5`: $5 input / $30 output per 1M tokens

OpenRouter model directory checked on 2026-06-16 confirms the active stack is available: DeepSeek V4 Flash, DeepSeek V4 Pro, Kimi K2.7 Code, Claude Sonnet 4.6, Claude Opus 4.8, GPT-5.5, and Gemini 2.5 Flash. Kimi is experimental only; Sonnet is the trusted coding lane.

## Config Optimizations Applied

Config backup:

- `/opt/data/config.yaml.bak.playbook-20260616054509`
- `/opt/data/config.yaml.bak.context-fix-20260616054719`
- `/opt/data/config.yaml.bak.gemini25flash-20260616055447`

Applied runtime settings:

```yaml
model:
  provider: openrouter
  default: deepseek/deepseek-v4-pro
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
- Model stack policy: DeepSeek handles volume, frontier models handle authority.
- Configured aliases: `/model fast`, `/model workhorse`, `/model coding`, `/model kimi-code`, `/model judge`, `/model boardroom`, `/model gpt-review`, `/model vision`.

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
- Remove AC's Telegram DM routing pointer.
- Delete the stale Hermes session id with `/opt/hermes/.venv/bin/hermes sessions delete <id> --yes`.
- Reset `/opt/data/sessions/sessions.json` to `{}` when no session mappings remain.
- Restart the gateway.
- Force the next Telegram interaction to start from fresh loaded context.

Failure lesson from 2026-06-16:

- Checking live `SOUL.md` is not enough.
- `/restart` preserves the active Telegram session and can keep answering from stale prompt state.
- The actual stale state can be the Telegram DM mapping in `/opt/data/sessions/sessions.json` pointing at an old session id.
- Do not declare identity/personality fixes complete until a fresh prompt or Telegram message returns the new identity.

## Media And Knowledge Capture

Installed on 2026-06-16:

- VPS host FFmpeg: installed through Ubuntu apt.
- Hermes container FFmpeg: present and verified.
- Hermes container yt-dlp: installed through Debian apt.
- Codex-wide skill: `youtube-knowledge` under `~/.codex/skills/youtube-knowledge`.
- Hermes skill: `youtube-knowledge` under `/opt/data/skills/youtube-knowledge`.
- Chowmes working wiki: `/opt/data/workspace/Knowledge`.

Current wiki structure:

```text
Knowledge/
  YouTube/
  Raw/
  Synthesis/
  Wiki/
  Assets/
```

The YouTube workflow stores raw captions and metadata, then creates a synthesis scaffold. It does not dump full copyrighted transcripts into chat.

Hermes video skill research:

- No standalone official `ffmpeg` skill was found.
- Installed media/video skills already include `creative/ascii-video`, `creative/manim-video`, `media/youtube-content`, and `media/songsee`.
- Optional video skills available in the Hermes image include `creative/hyperframes` and `creative/kanban-video-orchestrator`.
- For practical video editing, use FFmpeg directly for quick operations; use `hyperframes` for HTML/CSS/JS motion graphics; use `kanban-video-orchestrator` for larger multi-step video production.

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
4. Later, connect the Obsidian vault using a scoped access model and migrate this local wiki into the centralized vault.
