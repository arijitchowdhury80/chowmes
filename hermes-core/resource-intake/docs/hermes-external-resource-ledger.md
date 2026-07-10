# Hermes External Resource Ledger

Date: 2026-07-10
Status: First-layer control artifact

This ledger is the front door for external Hermes resources. A resource listed here is not approved for installation. It is approved only for study until the scan, intake, approval, and rollback gates are complete.

## Gate States

- `study`: source reviewed, no local install.
- `scan`: local security or inventory report required.
- `pilot`: isolated local or lab-profile trial allowed.
- `live-candidate`: ready for explicit live-change approval.
- `live`: installed in active Hermes runtime with verification evidence.
- `rejected`: not allowed in this adoption wave.

## Resources

| Resource | URL | Touches | License | Decision | First Gate | Notes |
|---|---|---|---|---|---|---|
| Honcho Memory | https://hermes-agent.nousresearch.com/docs/user-guide/features/honcho | memory, sessions, gateway identity, cloud/server-side data | Upstream Hermes feature | `pilot` later | Memory eval harness | Lab profile only; no Athena/default replacement. |
| Hermes Skills System | https://hermes-agent.nousresearch.com/docs/user-guide/features/skills | skills, prompts, scripts, assets, tool behavior | Upstream Hermes feature | `live-candidate` process | Skill intake checklist | Adopt governance, not random skill installation. |
| Medusa | https://github.com/Pantheon-Security/medusa | security scanning, repo/agent config inspection | AGPL-3.0 | `scan` installed locally | External CLI only | v2026.7.0 installed under `.tools/medusa-venv`; do not vendor or embed. |
| Sentry Skills | https://github.com/getsentry/skills | skills, agent workflows, review prompts | Apache-2.0 | `study` | Per-skill review | Port useful patterns into Chowmes-native skills. |
| Hermes Agent Self-Evolution | https://github.com/NousResearch/hermes-agent-self-evolution | prompts, skills, evals, possible code variants | Not declared by GitHub API on 2026-07-10 | `study` | Eval harness first | Proposal-only variants; no production auto-apply. |
| Bumblebee | https://github.com/perplexityai/bumblebee | package, extension, MCP, skill inventory | Apache-2.0 | `scan` installed locally | Scoped local inventory | v0.1.2 installed under `.tools/bin/bumblebee`; read-only inventory; no broad personal scans. |
| GBrain | https://github.com/garrytan/gbrain | markdown brain, database, retrieval, MCP, skills | MIT | `pilot` later | Bounded-domain mapping | Architecture pilot only; do not replace Obsidian/MEMORY.md. |
| Turbovec | https://github.com/RyanCodrai/turbovec | vector index, Python/Rust dependency | MIT | `rejected` for now | Retrieval bottleneck proof | Watchlist only. |
| Open Design | https://github.com/nexu-io/open-design | local app, design skills, exports, possible providers | Apache-2.0 | `pilot` later | Local artifact security scan | Local only; not VPS or Telegram runtime. |

## Approval Rule

No item moves beyond `study` or `scan` unless its report names:

- trust boundary
- data touched
- files changed
- runtime services changed
- approval owner
- rollback procedure
- verification command

## Current First-Layer Deliverables

- `hermes-core/resource-intake/scripts/hermes-resource-scan`: creates a Medusa-oriented resource intake report.
- `hermes-core/resource-intake/scripts/hermes-inventory-scan`: creates a Bumblebee-oriented inventory report.
- `hermes-core/resource-intake/docs/hermes-skill-intake-checklist.md`: defines approval gates for skills.
- `hermes-core/resource-intake/docs/hermes-resource-threat-model.md`: defines first-layer threat model and non-goals.
