---
name: hostinger-vps-ssh
description: Connect to and administer the user's Hermes Hostinger VPS via SSH. Use by default for VPS login, server inspection, deployment, configuration, software setup, Docker/service checks, or Hermes/chowmes administration whenever Codex is working from the ChowMes workspace. Also use when the user asks to log in to Hostinger, inspect or configure the Hermes/chowmes server, compare VPS suitability for Hermes or AI model hosting, run read-only VPS audits, or set up software on root@72.61.72.147 using credentials from the workspace .env.local file. Includes the required SSH_ASKPASS workaround for Codex sessions where normal SSH password prompts cannot read /dev/tty.
---

# Hostinger VPS SSH

## Core Rule

Never store VPS secrets in this skill, print them, or repeat them back to the user. Read credentials from the active project's `.env.local`.

When the current working directory is the ChowMes workspace, assume VPS tasks refer to the Hostinger `chowmes` VPS and use this skill automatically. Do not ask the user to explicitly invoke the skill or re-provide the SSH method. Still request network permission when the Codex environment requires it, and still confirm before risky server changes.

Expected env keys:

```text
SSH_HOST=72.61.72.147
SSH_USER=chowmesadmin
SSH_KEY=/Users/arijitchowdhury/.ssh/chowmes_ed25519
```

`SSH_PASS` is legacy-only. The server was hardened on June 15, 2026: root SSH login is disabled, SSH password login is disabled, and access should use `chowmesadmin` with the private key above. The active ChowMes workspace path is:

```text
/Users/arijitchowdhury/Dropbox/AI-Development/Personal/ChowMes
```

## Connection Workflow

1. Request network permission before any SSH command.
2. Confirm `.env.local` is plain text and owner-readable only when touching it:

```bash
file .env.local
chmod 600 .env.local
```

3. Use the bundled helper instead of raw `ssh`, `expect`, or `source .env.local`:

```bash
/Users/arijitchowdhury/Dropbox/AI-Development/Personal/ChowMes/scripts/chowmes-ssh-helper "hostname; id; uptime"
```

For another env file:

```bash
/Users/arijitchowdhury/Dropbox/AI-Development/Personal/ChowMes/scripts/chowmes-ssh-helper --env /path/to/.env.local "hostname"
```

The helper reads `SSH_HOST`, optional `SSH_USER`, `SSH_KEY`, and legacy `SSH_PASS` literally with `awk`. Prefer key auth. The legacy password path uses `SSH_ASKPASS` because normal automated SSH password entry can fail in Codex with:

```text
read_passphrase: can't open /dev/tty: Operation not permitted
```

## Read-Only Audit

Use this command shape to inspect the VPS before making setup recommendations:

```bash
/Users/arijitchowdhury/Dropbox/AI-Development/Personal/ChowMes/scripts/chowmes-ssh-helper "printf '=== CONNECTED ===\n'; hostname; grep PRETTY_NAME /etc/os-release; uname -srmo; systemd-detect-virt 2>/dev/null || true; lscpu | grep -E '^(Architecture|CPU\\(s\\)|Model name|Thread\\(s\\) per core|Core\\(s\\) per socket|Socket\\(s\\)|Hypervisor vendor|Virtualization type)'; free -h; df -hT /; if command -v nvidia-smi >/dev/null 2>&1; then nvidia-smi; else echo 'nvidia-smi: not found'; fi; if command -v docker >/dev/null 2>&1; then docker --version; else echo 'docker: not found'; fi; if command -v ollama >/dev/null 2>&1; then ollama --version; else echo 'ollama: not found'; fi"
```

Known snapshot from June 15, 2026:

```text
Host: chowmes
OS: Ubuntu 24.04.3 LTS
Virtualization: KVM
CPU: 2 vCPU, AMD EPYC 9354P
RAM: 7.8 GiB
Disk: 100 GB total, about 86 GB free
GPU: none detected
Docker: installed
Ollama: not installed
```

Treat the snapshot as stale until re-verified.

Known hardening snapshot from June 15, 2026:

```text
SSH user: chowmesadmin
SSH auth: key-only
Root SSH login: disabled
SSH password login: disabled
Firewall: UFW active, only TCP 22 public
fail2ban: active for sshd
unattended-upgrades: active
Dashboard: 127.0.0.1:9119 only
Local Ollama tunnel: 127.0.0.1:11435 only on VPS
Docker: use sudo docker from chowmesadmin
```

Telegram setup note from June 15, 2026:

```text
Bot username: chowmes_bot
Telegram is configured on chowmes with TELEGRAM_ALLOWED_USERS and TELEGRAM_HOME_CHANNEL set to the owner Telegram DM.
Do not enable an open Telegram bot. Dashboard/model ports must remain localhost-only; Telegram should use outbound bot polling unless the user explicitly chooses a webhook design.
The local Hermes workspace .env.local may contain a token key named chowmes_bot; never print it.
```

Known model-routing note from June 15, 2026:

```text
The user uninstalled Ollama/Gemma from the Mac because local LLM inference made the laptop too slow and unusable.
Do not start Ollama, pull local models, open a chowmes Ollama tunnel, or troubleshoot local model directories unless the user explicitly asks to revisit local LLMs.
The previous local Ollama path caused confusion because model blobs existed under a Google Drive local-models folder, while the running Ollama app used its default empty store.
OpenRouter is configured on chowmes as OPENROUTER_API_KEY in /root/.hermes/.env; never print or repeat it.
Current direction: Hermes/chowmes should use direct Gemini for Telegram and agent work, with Algolia inference reserved for explicit fast/casual low-risk tasks. OpenRouter is historical/backup only unless Arijit explicitly reopens it.
Current verified Hermes default: direct Gemini model gemini-2.5-flash.
Current verified delegation/deep-work model: direct Gemini model gemini-2.5-pro.
Pricing snapshot checked on June 16, 2026: google/gemini-2.5-flash is $0.30/M input and $2.50/M output; anthropic/claude-sonnet-4.6 is $3/M input and $15/M output; google/gemini-3.1-flash-lite is $0.25/M input and $1.50/M output.
Before changing models, verify the active Hermes config and OpenRouter pricing/model ID; do not assume stale model names or prices.
If SSH banner exchange, model pull, docker restart, or config verification exceeds a short bounded wait, stop and report the exact blocker instead of retrying in circles.
```

## Recent Failure Lessons

- Do not keep retrying a local-Ollama setup if `ollama list` is empty or the server is not running; the user wants OpenRouter for now.
- Do not run long `find` scans over Google Drive model folders; they can hang and add no value unless explicitly requested.
- Do not launch or restart local Ollama from this skill without explicit user consent.
- For VPS changes, prefer one bounded command that patches config, restarts Hermes, and prints verification. If it times out, stop and tell the user.

## Default Chowmes Admin Permissions

The user has authorized routine Chowmes administration without asking every time:

- Read server status and logs.
- Inspect Hermes config.
- Check Docker containers.
- Check firewall and SSH status.
- Back up config before editing.
- Restart Hermes after config-only changes.
- Update runbooks and local config docs.
- Run bounded smoke tests.

Always ask before:

- Opening public ports or changing firewall rules.
- Deleting data or old sessions.
- Rotating credentials.
- Changing SSH configuration.
- Installing long-running or heavy software.
- Adding broad access to private personal data.
- Connecting the full Obsidian vault.
- Re-enabling local LLMs.
- Enabling Telegram terminal, file, or code execution tools.

Chowmes operating modes:

- Fast Telegram mode is default: low turn budget, minimal tools, no TTS, no terminal/file/code execution, no delegation, no session search.
- Deep Architect mode is deliberate: stronger model, research and broader tools only when needed and allowed.

## Administration Safety

Start with read-only inspection. Confirm with the user before changing firewall rules, deleting data, rotating credentials, restarting critical services, replacing SSH config, or running long installs.

For Hermes and AI-model planning, a 2 vCPU / 8 GB RAM / no-GPU VPS is suitable for a lightweight web service, reverse proxy, dashboard, queue, or orchestration layer. It is not suitable for powerful local model inference. Prefer the user's Apple Silicon Mac or a real GPU server for model inference unless the VPS hardware has changed.
