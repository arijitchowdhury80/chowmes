# Hermes External Resource Threat Model

Date: 2026-07-10
Status: First-layer gate

## Trust Boundary

External Hermes resources cross the trust boundary when they introduce any of the following:

- agent instructions such as `AGENTS.md`, `CLAUDE.md`, `.hermes.md`, or `SKILL.md`
- executable scripts or binaries
- package dependencies
- MCP server configuration
- memory provider configuration
- gateway, Telegram, or session behavior
- provider credentials or network calls
- generated artifacts that could be published or delivered

The default stance is study-only until the resource passes scan, inventory, review, and explicit approval.

## Primary Threats

| Threat | Failure Mode | First-Layer Control |
|---|---|---|
| Instruction poisoning | External skill changes Athena/Argus behavior or overrides local operating rules. | Manual review plus `hermes-resource-scan` flagging instruction files. |
| Secret leakage | Scanner, install script, or generated report prints tokens or private config. | Reports record paths and metadata only; broad scans require approval. |
| MCP overreach | Resource adds tools that can read/write beyond intended scope. | MCP configs flagged before install. |
| Memory contamination | Honcho/GBrain-like systems mix profile memory or inject low-quality conclusions. | Lab-profile pilot only; eval harness required. |
| Runtime drift | New skill/plugin silently changes Telegram, gateway, session, or model behavior. | No live runtime change without explicit approval and health checks. |
| Dependency risk | External app adds vulnerable packages or install-time scripts. | Inventory scan plus package manifest review. |
| License risk | AGPL or unknown-license code is vendored into Hermes. | Ledger license gate; Medusa external CLI only. |
| Artifact risk | Generated decks/dashboards imply unsupported facts or leak internal data. | Local artifact pilot and visual/source QA. |

## No Live Runtime Change

The first layer does not install external resources, change VPS config, enable tools, alter Telegram behavior, or modify Athena/Argus memory.

Live changes require a later approval note naming:

- exact profile
- exact files
- exact config keys
- rollback path
- verification command
- session refresh requirement

## Broad Scan Rule

Do not scan `/`, `$HOME`, Dropbox roots, full Obsidian vaults, or personal-data directories unless Arijit explicitly approves that exact target. Use scoped repo or cloned candidate directories first.

## Required Evidence

An intake decision must include:

- resource scan report
- inventory report
- license and source metadata
- behavior review
- approval or rejection reason
- rollback path

## First-Layer Non-Goals

- No Honcho setup.
- No GBrain setup.
- No Open Design install.
- No Sentry skill install.
- No self-evolution run.
- No Turbovec evaluation.
- No VPS live change.
