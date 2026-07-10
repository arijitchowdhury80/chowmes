# Hermes Skill Intake Checklist

Date: 2026-07-10
Status: First-layer gate

Use this before installing, porting, enabling, or modifying any external Hermes skill, skillpack, plugin, MCP integration, or agent-brain repo.

## 1. Source And Provenance

- [ ] Source URL recorded in `hermes-core/resource-intake/docs/hermes-external-resource-ledger.md`.
- [ ] License recorded.
- [ ] Maintainer or publisher recorded.
- [ ] Current commit, tag, or version recorded.
- [ ] External install instructions reviewed but not executed.

## 2. Trust Boundary

- [ ] Skill declares what data it reads.
- [ ] Skill declares what data it writes.
- [ ] Skill declares network access requirements.
- [ ] Skill declares script or binary execution requirements.
- [ ] Skill declares whether it touches memory, sessions, prompts, gateway config, or MCP config.

## 3. Security Scan

- [ ] `hermes-core/resource-intake/scripts/hermes-resource-scan <target>` report created.
- [ ] Medusa status recorded or blocker explained.
- [ ] `AGENTS.md`, `CLAUDE.md`, `SKILL.md`, MCP configs, install scripts, and package manifests reviewed.
- [ ] No secrets printed into terminal, reports, or docs.
- [ ] Critical findings resolved or the skill is rejected.

## 4. Inventory Scan

- [ ] `hermes-core/resource-intake/scripts/hermes-inventory-scan <target>` report created.
- [ ] Bumblebee status recorded or blocker explained.
- [ ] Package manifests and lockfiles reviewed.
- [ ] New dependencies justified.

## 5. Behavior Review

- [ ] Trigger conditions are narrow and explicit.
- [ ] Skill does not conflict with `AGENTS.md`, `SOUL.md`, `USER.md`, or `MEMORY.md`.
- [ ] Skill does not silently change Athena, Argus, or Vulcan identity.
- [ ] Skill does not enable Telegram code execution, delegation, TTS, browser tools, public ports, or session search.
- [ ] Skill does not require broad Obsidian or personal-data access unless explicitly approved.

## 6. Test And Smoke Gate

- [ ] Minimal smoke test written.
- [ ] Negative trigger test written when trigger pollution is possible.
- [ ] Test output saved or summarized in the intake report.
- [ ] Rollback tested in local or lab context.

## 7. Approval Gate

Installation or live enablement requires explicit approval after the above gates. The approval note must say:

- approved scope
- target profile
- files to change
- tools to enable, if any
- verification commands
- rollback command or file restore path

## 8. Rollback

- [ ] Original files backed up.
- [ ] New files listed.
- [ ] Config changes listed.
- [ ] Session refresh requirement named.
- [ ] Health-check command named.

## Hard Stops

- Critical security finding unresolved.
- Unknown license on code we would vendor or embed.
- Skill tries to change identity, memory, gateway behavior, or MCP config outside its approved scope.
- Skill requires public service exposure without separate approval.
- Skill cannot be removed cleanly.
