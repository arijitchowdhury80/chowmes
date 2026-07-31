# Hermes Security Gate

Date: 2026-07-13
Status: Phase 2 control contract
Gate ID: `security`

The security gate decides whether an external repo, skill, MCP server, package,
or tool is safe enough to study, scan, or pilot for Hermes.

Do not replace `skill-verifier`. The existing verifier at
`/Users/arijitchowdhury/.agents/skills/skill-verifier` remains the external
skill security scanner of record. Hermes adds context around it so results are
connected to the resource ledger and promotion decision.

## Required Evidence

- `skill-verifier` report for any external skill, agent workflow, MCP tool, or
  repo that may be installed, copied, ported, or executed.
- `hermes-resource-scan` report with Medusa status recorded or a blocker
  explanation.
- `hermes-inventory-scan` report with Bumblebee status recorded or a blocker
  explanation.
- File inventory covering `AGENTS.md`, `CLAUDE.md`, `SKILL.md`, install scripts,
  package manifests, lockfiles, MCP configs, and hidden files.
- Manual review notes for prompt injection, data exfiltration, credential
  access, runtime code download, shell execution, and permission mismatch.

## Pass Criteria

- No unresolved critical finding.
- No unresolved high finding without explicit review approval.
- No secret value printed into terminal output, reports, docs, or logs.
- License posture is recorded before vendoring, embedding, or copying code.
- Network, filesystem, memory, and runtime permissions match the resource's
  stated purpose.

## Rollback

- Reject the resource and keep it at `study` or `rejected`.
- Remove quarantine clones and local report-only artifacts if they contain no
  useful audit evidence.
- Do not copy, install, enable, or execute the resource in live Hermes.
- If files were staged for a pilot, restore the backed-up files listed in the
  intake report.

## Notes

Medusa and Bumblebee are supporting controls. `skill-verifier` remains the
specialized skill-security gate because it checks prompt injection and malicious
agent behavior that package inventory alone will miss.
