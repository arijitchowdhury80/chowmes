# Hermes Memory

## Operating Facts

- Chowmes is the Hostinger VPS running Hermes for Arijit.
- Default provider is OpenRouter.
- Model selection policy: DeepSeek handles volume, frontier models handle authority. Use `deepseek/deepseek-v4-flash` for fast low-risk work, `deepseek/deepseek-v4-pro` for bulk serious work, `anthropic/claude-sonnet-4.6` for trusted coding and high-stakes judgment, and `moonshotai/kimi-k2.7-code` only as an experimental open coding comparison via `/model kimi-code`.
- Default normal/workhorse model is `deepseek/deepseek-v4-pro`.
- Deep work / judgment escalation model is `anthropic/claude-sonnet-4.6`; final boardroom review can use `anthropic/claude-opus-4.8`; GPT second opinion can use `openai/gpt-5.5`.
- Telegram is configured with allowlisted user access.
- Telegram fast mode is intentional: low turn budget, no TTS, no terminal/file/code execution, no delegation, no session search.
- Local Ollama/Gemma is disabled because it slowed the laptop.
- Working knowledge wiki is `/opt/data/workspace/Knowledge`; use `youtube-knowledge` to capture YouTube captions, metadata, raw notes, and synthesis scaffolds there before future Obsidian migration.
- Hermes native web tools are enabled in Telegram with Parallel as the premium provider. `PARALLEL_API_KEY` is configured on the VPS, `web.backend` is `parallel`, and `research/parallel-cli` is installed for deeper Parallel workflows. Normal Telegram web lookup should use native `web_search` and `web_extract`.

## Durable Lessons

- Melorie/Chowmes should challenge Arijit when ideas are vague, risky, or under-scoped.
- Melorie/Chowmes should interview Arijit to clarify product and architecture before implementation when requirements are unclear.
- Melorie/Chowmes should use research and tools when current facts matter.
- If a workflow fails repeatedly, stop and report the exact blocker instead of retrying in circles.
- A Telegram identity or personality fix is not verified by checking files alone. Confirm the live VPS `SOUL.md`, remove the Telegram DM session pointer from `/opt/data/sessions/sessions.json`, delete the stale session id with `/opt/hermes/.venv/bin/hermes sessions delete <id> --yes`, restart the gateway, and verify a fresh prompt answers with the new identity.
- If Telegram goes dead after a gateway restart, check gateway status and logs before guessing. The known failure from June 16, 2026 was `/opt/data` and key subdirectories owned by `root:root` with `700`, while the gateway runs as `hermes`, causing `PermissionError: '/opt/data/.env'`. Fix by restoring `chown -R hermes:hermes /opt/data`, keeping `.env` at `600`, restarting the gateway, and verifying Telegram delivery.
- After VPS env/config/session/gateway changes, run `scripts/chowmes-health-check --repair --send-test` instead of relying on manual inspection. This is now the required stability gate for Chowmes changes.
- Do not run Hermes CLI runtime commands as root inside the container. Run gateway status, send tests, session edits, and web backend checks as the `hermes` user, or root may recreate `/opt/data` runtime files such as pairing state with bad ownership and break Telegram again.

## Safety

- Never store secrets in markdown.
- Never print secrets from `.env.local`, `/root/.hermes/.env`, Telegram, OpenRouter, SSH keys, or credential stores.
- Confirm before destructive operations or public exposure changes.
