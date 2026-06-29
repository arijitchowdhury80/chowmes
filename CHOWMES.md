# Chowmes Hermes Runbook

Chowmes is the Hostinger VPS running Hermes Agent for Telegram and agent work.

## Current live snapshot

Verified on June 29, 2026 from the Hostinger VPS.

| Area | Confirmed live state |
|---|---|
| Host | `chowmes` |
| Containers | `hermes`, `caddy`, `scout`, `temporal`, `temporal-ui`, `temporal-db`, `ac2-lab-backend` |
| Public ports | `22/tcp`, `80/tcp`, `443/tcp` allowed by UFW |
| Local-only ports | Hermes dashboard `127.0.0.1:9119`, Temporal `127.0.0.1:7233`, Temporal UI `127.0.0.1:8088`, Scout `127.0.0.1:8421`, AC2 lab backend `127.0.0.1:8787` |
| Active provider/model | Direct Gemini API `gemini-2.5-pro` |
| Active context length | `131072` |
| Active max turns | `6` |
| Active web backend | `parallel` |
| Active gateways | Default Athena gateway running; Vulcan profile gateway running |
| On-demand profiles | Arjuna, Kubera, Prometheus, Strategic, and Argus profiles exist but are not active gateways |

The older notes below are historical unless they match this verified snapshot. In particular, do not repeat the old "only SSH is public" statement without rechecking UFW and Caddy.

## Current model setup

Hermes now uses the direct Gemini API through `GEMINI_API_KEY`. OpenRouter remains configured as a historical/backup credential source, but it is not the active Chowmes route as of June 29, 2026. Local Ollama/Gemma on the Mac is disabled and should not be restarted unless explicitly requested.

- Default Telegram/Hermes Athena model: `gemini-2.5-pro`
- Provider: `gemini`
- Context length override: `131072` live as of June 29, 2026
- Routine workhorse / CI synthesis model: `gemini-2.5-flash`
- Deep/delegated judgment model: `gemini-2.5-pro`
- Low-end/fast lane provider: `algolia-inference` using `ALGOLIA_INFERENCE_BASE_URL`, `ALGOLIA_INFERENCE_API_KEY`, and `ALGOLIA_INFERENCE_MODEL` in `/opt/data/.env`
- OpenRouter key location on host: `/root/.hermes/.env`
- OpenRouter key location in container: `/opt/data/.env`
- Direct Google/Gemini key: configured on VPS as `GEMINI_API_KEY` in `/opt/data/.env`
- Local Ollama tunnel: not required

Note: `32768` was tested on June 16, 2026, but Hermes Agent rejected it because the runtime requires at least `64000`. That is a minimum requirement, not the desired cap. A previous target used `1048576`, but the currently verified live value is `131072`; verify before changing.

Verified on June 29, 2026:

```text
Model:    gemini-2.5-pro
Provider: gemini
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

Current routing:

- Use `gemini-2.5-pro` for Athena/default Telegram, everyday reasoning where voice and judgment matter, deep/judge/boardroom/delegated work.
- Use `gemini-2.5-flash` for CI synthesis, web extraction, vision, compression, approval/safety, and other bounded content-critical auxiliary tasks with quality gates.
- Use `algolia-inference` for explicit low-end modes and cheap housekeeping tasks only: `/model fast`, `/model casual`, `title_generation`, `triage_specifier`, `profile_describer`, `monitor`, and `skills_hub`.
- Do not route production Chowmes through OpenRouter while the active policy is "forget OpenRouter".
- Do not add GLM/Z.ai or direct DeepSeek to live routing until direct `ZAI_API_KEY` / `GLM_API_KEY` or `DEEPSEEK_API_KEY` credentials exist and the provider path has passed a smoke test.

Model aliases configured in Hermes as of June 29, 2026:

```text
/model fast        -> algolia-inference:${ALGOLIA_INFERENCE_MODEL}
/model casual      -> algolia-inference:${ALGOLIA_INFERENCE_MODEL}
/model workhorse   -> gemini:gemini-2.5-flash
/model repair      -> gemini:gemini-2.5-flash
/model vision      -> gemini:gemini-2.5-flash
/model coding      -> gemini:gemini-2.5-pro
/model judge       -> gemini:gemini-2.5-pro
/model boardroom   -> gemini:gemini-2.5-pro
/model emergency   -> gemini:gemini-2.5-pro
```

Operating rule: Gemini Flash handles volume and routine synthesis; Gemini Pro handles authority. Do not confuse "paid key" with "infinite budget"; keep context and tool-loop guardrails active.

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
- Argus: Competitive Intelligence operator/analyst, profile `argus`; dedicated Telegram gateway running and owning daily/weekly CI delivery.

COO, CFO, and CMO remain role cards for now. COO becomes live only after recurring operating loops need a separate operator memory.

Do not confuse "gateway stopped" with "profile does not exist." Some advisor gateways may be started only when needed. Athena should answer "Vulcan" when Arijit asks who the CTO is, and should route technical critique to the `vulcan` profile when live collaboration is needed.

### Argus CI bot activation state

Argus is now the dedicated Competitive Intelligence Telegram delivery bot. To verify final state, run:

```sh
scripts/chowmes-ci-e2e-status --require-final-argus-only
```

Current verified final state after June 29, 2026 cutover:

```text
argus_profile=present
argus_telegram_token_key=present
argus_gateway=running
argus_daily_cron=present
argus_weekly_cron=present
ci_target_argus_e2e_ready=yes
ci_final_argus_only_ready=yes
```

Activation and cutover commands used:

```sh
scripts/chowmes-argus-complete-activation --env-file .env.local --to telegram --execute
scripts/chowmes-argus-cutover-ci-cron --execute
```

The cutover pauses, not deletes, the temporary default CI cron jobs.

`scripts/chowmes-argus-activate` intentionally exits with code `2` when the dedicated token is missing. That is a safe blocker, not a runtime failure.

`scripts/chowmes-argus-complete-activation` is the preferred one-command activation path if Argus ever needs to be reinstalled. In execute mode it installs the Argus Telegram key, starts and smoke-tests the Argus gateway, creates Argus-owned daily/weekly CI cron jobs, then runs `scripts/chowmes-ci-e2e-status --require-argus-e2e`.

`scripts/chowmes-argus-cutover-ci-cron` is the final guarded cutover after Argus E2E delivery is ready. It refuses unless the Argus token, gateway, and Argus daily/weekly cron jobs are present. In execute mode it pauses the temporary default `competitive-research-daily` and `competitive-research-weekly` cron jobs. It does not delete them.

`scripts/chowmes-argus-configure-telegram` installs only Argus Telegram keys from a local env file and never prints secret values. Expected local keys are `ARGUS_TELEGRAM_BOT_TOKEN` or `ARGUS_BOT_TOKEN` or `TELEGRAM_BOT_TOKEN_ARGUS`; optional channel keys are `ARGUS_TELEGRAM_HOME_CHANNEL` and `ARGUS_TELEGRAM_ALLOWED_USERS`. It refuses to overwrite an existing Argus token unless `--force` is supplied.

`scripts/chowmes-argus-migrate-ci-cron` intentionally exits with code `2` when the dedicated token is missing or the Argus gateway is not running. That helper copies the daily/weekly CI wrappers into `/opt/data/profiles/argus/scripts/` and creates Argus-profile cron jobs named `argus-competitive-research-daily` and `argus-competitive-research-weekly` only with explicit `--execute`. It never pauses the current default CI cron jobs.

### CI pipeline health status - June 29, 2026

Current verified state:

- Argus daily CI cron is active at `0 9 * * *` through the dedicated Argus Telegram profile.
- Argus weekly CI cron is active at `0 9 * * 0` through the dedicated Argus Telegram profile.
- Temporary default daily/weekly CI cron jobs are paused.
- Both wrappers run provider preflight before synthesis.
- Both wrappers run post-run self-check after Markdown, HTML, ledger, and dashboard publish steps.
- Live daily self-check for `2026-06-29` passed against Markdown, HTML, `ci.sqlite`, dashboard publish log, and weak-language gate.
- Live weekly self-check for `2026-06-29` passed against Markdown, HTML, `ci.sqlite`, dashboard publish log, and weak-language gate.
- Argus post-run review is wired after the self-check. It writes `run-reviews/YYYY-MM-DD-{cadence}.json`, Markdown, and `run-reviews/argus-learning-log.md`.
- The first live Argus review found a quiet-day `missing_links` quality warning; the CI quality gate was patched so full-coverage quiet days are not falsely penalized while material reports still require links. The rerun produced daily quality score `1.00`, self-check `pass`, and Argus review `healthy`.
- Dashboard publishing is wired through the CI app repository publisher.
- Forced Hermes cron runs on June 29, 2026 verified the scheduler path:
  - Daily last run: `2026-06-29T06:52:45.692560-04:00 ok`.
  - Weekly last run: `2026-06-29T06:53:16.805569-04:00 ok`.
- A dashboard publish warning appeared after the forced runs because the VPS app repo was `ahead 2, behind 1` from GitHub `main`; the repo was rebased and pushed, then dashboard publish and both self-checks returned to `pass`.
- `scripts/chowmes-argus-status` is a Mac-side operator helper. Run it from this repository, not from inside `/opt/data/scripts` on the container.
- `scripts/chowmes-ci-e2e-status` is the canonical current-vs-target health helper. It reports current default CI delivery health, daily/weekly wrapper wiring, latest daily/weekly audit status, Argus profile/persona contract readiness, CI skill Argus ownership/self-review contract readiness, target Argus E2E readiness, and the exact blocker when Argus delivery is not ready.
- Use `scripts/chowmes-ci-e2e-status --require-final-argus-only` for the final health gate.

Fresh manual wrapper verification on June 29, 2026:

- Daily wrapper executed manually on the VPS. Initial run generated the report but dashboard publish failed because `/opt/data/apps/algolia-competitive-intelligence` was behind GitHub and had a local generated dashboard commit.
- The VPS dashboard repo was rebased onto `origin/main` and pushed. Dashboard publish was rerun successfully.
- Daily self-check was rerun and passed. Argus daily post-run review was rerun and reported `healthy`.
- Weekly wrapper executed manually on the VPS and passed self-check and Argus post-run review.
- `scripts/chowmes-ci-e2e-status` reported `ci_current_pipeline_mechanically_healthy=yes`.
- The same helper reported `argus_profile_contract_ready=yes` and `ci_skill_argus_contract_ready=yes`, proving Argus has the dedicated CI identity/persona contract and the competitive-research skill has the Argus ownership/self-review contract.
- A later audit found the CI synthesis prompts in `ci_core.py` still said `You are Athena` even though the skill contract said Argus owned CI. This was fixed in both the workspace skill and the standalone `algolia-competitive-intelligence` repo. The readiness helper now reports `ci_synthesis_identity_ready=yes` and fails if synthesis prompts regress to Athena.
- Current default daily/weekly wrappers now include an explicit Telegram delivery identity notice: Argus generated and reviewed the run, the delivery path is the temporary default Chowmes Telegram gateway, and Athena is supervisor only. `scripts/chowmes-ci-e2e-status` now reports `default_daily_delivery_identity_notice=present` and `default_weekly_delivery_identity_notice=present`.
- After Argus activation and cutover, the same helper reports `ci_target_argus_e2e_ready=yes` and `ci_final_argus_only_ready=yes`.

Interpretation:

- The final CI delivery architecture is active: Argus owns daily/weekly CI delivery and Athena remains supervisor/CEO.
- Athena remains supervisor/CEO. She should not be described as the final daily CI operator once Argus is activated.

### Athena live voice status - June 29, 2026

Confirmed root cause of the robotic provider-failure messages: the model-provider error copy was hardcoded in `/opt/hermes/gateway/run.py`, so those Telegram bubbles bypassed `SOUL.md` entirely.

Live hotfix applied:

- Provider/auth/rate-limit/credit failures now use Athena-style operational language with `blocked by`, `effect`, and `next move`, without raw provider details or emoji.
- Greeting-only Telegram messages now use a narrow deterministic Athena guard instead of spending a model call and drifting into canned phrases such as "what's on your mind?"
- The guard only catches exact low-context greetings such as `hi`, `hello`, and `whats up`; substantive messages like `whats up with CI` still go to the agent.

Verification:

- Gateway source compiled with `/opt/hermes/.venv/bin/python -m py_compile /opt/hermes/gateway/run.py`.
- Live helper check returned `Hey. I am here.` for `whats up`.
- Live provider-credit helper check returned the new provider-agnostic message.
- Gateway restarted successfully; `scripts/chowmes-health-check --repair --send-test` passed and delivered the Telegram test.
- `scripts/chowmes-athena-gateway-voice-guard --check` verifies the hotfix is present after Hermes updates or container rebuilds.
- `scripts/chowmes-athena-gateway-voice-guard --apply --restart-gateway` reapplies the guard and restarts the default gateway if the guard is missing.

Voice refactor update:

- `SOUL.md` now has a Living Voice Kernel that forces Athena to read the moment before answering: comfort, truth, decision, action, or proof.
- The source prompt now explicitly separates casual human replies, serious decision replies, and operational failure replies.
- Operational failures must state blocker, effect, and next move, and duplicate failure messages are explicitly forbidden.
- Gemini Flash ignored the hard-banned casual phrase rule in live CLI smoke tests and replied with variants of "what's on your mind." Gemini Pro passed the same smoke with concise Athena-like replies, so Athena/default was moved to `gemini-2.5-pro`.
- This prompt-level refactor complements the gateway hotfix. The gateway guard catches tiny greetings, robotic tiny final replies, and provider failures before they reach Telegram; `SOUL.md` governs normal Athena responses after the model is reached.

Live gateway hotfix backups:

- `/opt/hermes/gateway/run.py.bak.athena-provider-voice-`
- `/opt/hermes/gateway/run.py.bak.athena-casual-guard-20260629074019`
- `/opt/hermes/gateway/run.py.bak.athena-voice-guard-20260629084843`

Live config backup from Athena Pro cutover:

- `/opt/data/config.yaml.bak.athena-pro-`

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

Run a tiny Gemini smoke test:

```sh
/Users/arijitchowdhury/.codex/skills/hostinger-vps-ssh/scripts/ssh-hermes-vps "sudo docker exec -u hermes -e HOME=/opt/data hermes /opt/hermes/.venv/bin/hermes -z 'Reply exactly: gemini hermes online'"
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

## Provider credit incident response

Known failure pattern from June 28, 2026:

- OpenRouter credits were exhausted. The credit API reported `total_credits=35`, `total_usage=35.258734652`, leaving roughly `-$0.2587`.
- Athena/default Telegram, Vulcan, and CI synthesis all depended on OpenRouter, so a provider-credit failure affected multiple agents.
- The gateway originally replied with a generic provider failure. The live gateway was patched so HTTP 402 / insufficient-credit failures return a credit-specific Telegram message.
- The first credit-specific gateway patch still sounded robotic and could arrive twice because provider failures were delivered once through the status callback path and again as the final response. The live gateway was patched again so Telegram provider-failure status callbacks are suppressed and only the final response is delivered.
- CI cron jobs originally caught Hermes synthesis failures, fell back to local synthesis, returned success, and could publish weak fallback artifacts. Production daily/weekly wrappers now run a provider preflight and pass `--fail-on-synthesis-error`.
- The daily Chowmes provider credit watch cron runs at `08:45 America/New_York`, before the 09:00 CI jobs, and delivers a Telegram alert if credits are below the configured floor.
- Current status as of June 29, 2026: Chowmes has been switched off OpenRouter for production routing. Default Athena uses direct Gemini Pro, CI synthesis uses direct Gemini Flash, and explicit fast/casual low-risk routes use Algolia inference. The historical OpenRouter incident remains useful as a failure-mode lesson, not as the active provider path.

Current user-facing provider-failure style:

```text
Arijit, I’m blocked at the model provider before I can think. The effect is that Athena and scheduled agent work may fail until the provider check passes. I’m keeping the raw vendor details in the logs and checking the active route next.
```

Live gateway hotfix backups:

- `/opt/hermes/gateway/run.py.bak.credit-message-20260628231108`
- `/opt/hermes/gateway/run.py.bak.credit-voice-20260628234617`

Current protective checks:

- CI production preflight: `/opt/data/knowledge/obsidian/MyOS/Projects/Competitive Intelligence/skills/competitive-research/scripts/ci-provider-preflight.py`
- Daily wrapper: `/opt/data/scripts/competitive-research-daily.sh`
- Weekly wrapper: `/opt/data/scripts/competitive-research-weekly.sh`
- Chowmes credit watch: `/opt/data/scripts/chowmes-provider-credit-watch`
- Hermes cron job: `chowmes-provider-credit-watch`, schedule `45 8 * * *`, delivery `telegram`
- Provider watch was converted from a shell wrapper to a Python entrypoint on June 29, 2026 because Hermes cron executed the extensionless script as Python. Verification: direct script exit `0`; cron-triggered last run `2026-06-29T12:46:24.584451-04:00 ok`.

Recovery loop:

1. Check provider credits before debugging agent identity, prompts, or CI quality.
2. If credits are below floor, add credits or switch provider/model before the next scheduled run.
3. Run the CI daily or weekly wrapper manually and expect exit `0`; exit `75` means the job intentionally failed closed.
4. Run `scripts/chowmes-health-check --repair --send-test`.
5. Confirm `hermes cron list` shows CI jobs and credit watch with truthful status.

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
