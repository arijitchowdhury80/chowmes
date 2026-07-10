# Hermes Resource Adoption Plan

Date: 2026-07-10
Status: Active - Phase 1 complete
Scope: Chowmes, MyOS-Core, Athena, Argus, Hermes skills, memory, security, retrieval, and artifact workflows

## Executive Read

The resource list is valuable, but it should not be treated as an install list.
Most of these projects change agent behavior, memory, security posture, or supply-chain surface. The strongest path is:

1. Add security and skill-governance gates first.
2. Pilot memory systems in isolated profiles before touching Athena/default.
3. Use self-evolution only after benchmark suites exist.
4. Treat design/artifact tooling as local operator tooling, not Telegram runtime.
5. Defer custom vector infrastructure until a measured retrieval bottleneck exists.

Recommended near-term additions:

- Adopt `medusa` as a local and CI security gate, but do not vendor or embed it because it is AGPL-3.0.
- Adopt `bumblebee` as a read-only inventory and exposure scanner for developer/package/MCP/skill state.
- Add a Hermes skill intake workflow using the native Hermes skills model, with Sentry skills as examples to study and selectively port.
- Pilot Honcho in a non-default profile or tools-only mode for memory quality evaluation.
- Study GBrain as the stronger long-term model for Obsidian-backed operating memory, but do not replace the current vault/MEMORY.md system yet.
- Use Hermes self-evolution only for scored prompt/skill experiments after tests and voice-quality benchmarks exist.
- Use Open Design locally for dashboards, decks, and artifacts after security review, not as a production Hermes dependency.

Recommended deferrals:

- Do not install all Sentry, GBrain, or Open Design skills wholesale.
- Do not replace built-in Hermes memory with Honcho or GBrain until privacy, cost, prompt-size, and retrieval-quality tests pass.
- Do not enable autonomous self-evolution against live Athena, Argus, or gateway code.
- Do not add turbovec now unless retrieval latency or privacy constraints become a proven blocker.
- Do not enable Telegram code execution, delegation, broad browser tools, or new public services as part of this adoption.

## Current Hermes Baseline This Plan Respects

Chowmes is the host and service umbrella. Hermes is the runtime. MyOS-Core is the primary Hermes instance using `/opt/data`. Athena is the default CEO/orchestrator profile. Argus owns Competitive Intelligence delivery.

Current constraints from local runbooks:

- Production provider is direct Gemini, with `gemini-2.5-pro` for Athena/default and `gemini-2.5-flash` for bounded synthesis lanes.
- Telegram is operator mode: bounded turns, no code execution, no delegation, no TTS, no session search.
- `SOUL.md`, `USER.md`, `MEMORY.md`, and project context are snapshotted when a session starts.
- After prompt, memory, model, gateway, env, or config changes, use the fresh-session and health-check scripts.
- Skills are not installed just because they exist in a catalog.
- Local Dropbox docs and the Obsidian vault are human-readable sources of truth; VPS `/opt/data` is the live runtime copy.

This matters because several candidate projects include agent instructions, skill files, plugin manifests, MCP configs, or external services. Those can improve Hermes, but they can also silently shift behavior.

## Source-by-Source Findings

### 1. Hermes Honcho Memory

Source: https://hermes-agent.nousresearch.com/docs/user-guide/features/honcho

What it is:

- Honcho is a Hermes memory provider plugin.
- It adds server-side persistent memory, automatic dialectic reasoning, session summaries, multi-agent peer separation, semantic search over conclusions, and optional auto-injected memory context.
- Key settings include `contextCadence`, `dialecticCadence`, `dialecticDepth`, `recallMode`, `contextTokens`, `sessionStrategy`, and gateway identity mapping.

What Hermes does not have without it:

- Current `MEMORY.md` and `USER.md` are curated and stable, but manual.
- Hermes has durable context, but not automatic pattern extraction from conversations.
- It does not maintain peer-specific learned models for Athena versus Argus versus Vulcan unless we manually encode the differences.

Why it can make Hermes better:

- Athena could learn Arijit's recurring preferences, risk posture, operating patterns, and decision history without every insight being manually compressed into `MEMORY.md`.
- Argus, Vulcan, and Athena could have cleaner peer separation if configured carefully.
- Session summaries and semantic conclusions could reduce repeat questions and reduce stale recap work.

Risks:

- Cloud or server-side memory can store sensitive operating details.
- Auto-injection can increase prompt size and degrade voice if low-quality conclusions accumulate.
- Gateway identity mapping can contaminate memories if runtime IDs are pinned or aliased incorrectly.
- Replacing `MEMORY.md` too quickly would remove the useful friction of human-approved durable memory.

Recommendation:

- Pilot, do not replace.
- Use a lab profile first, preferably `athena-memory-lab`, not Athena/default.
- Start with `recallMode: tools` or a strict `contextTokens` cap before auto-injection.
- Keep `memory.write_approval: true` and preserve `MEMORY.md` as the canonical curated layer.
- Evaluate against real tasks: identity continuity, project recall, Argus voice preservation, and token growth.

Implementation gate:

- No live Athena/default change until a 2-week pilot shows improved recall without prompt bloat, privacy leakage, or voice drift.

### 2. Hermes Skills System

Source: https://hermes-agent.nousresearch.com/docs/user-guide/features/skills

What it is:

- Hermes skills are progressive-disclosure instruction bundles.
- A skill lives in its own directory with `SKILL.md`; optional `references/`, `templates/`, `scripts/`, and `assets/` are installed with it.
- Hermes can install from official catalogs, `skills.sh`, `.well-known/skills`, GitHub repos/taps, ClawHub, Claude marketplace-style repos, and LobeHub.
- Community taps are treated as lower trust and receive scan/warning treatment.

What Hermes does not have without stronger skill governance:

- Skills can be installed, but Chowmes does not yet have a formal intake process that says: inspect, scan, sandbox, test, approve, install, document, verify.
- There is no single adoption ledger for external skills.
- There is no standard "skill changed Athena behavior, refresh session, run health check" playbook.

Why it can make Hermes better:

- Skills are the right extension mechanism for reusable workflows such as security review, research intake, CI report generation, artifact production, and operational runbooks.
- Progressive disclosure keeps the prompt smaller than dumping all instructions into `SOUL.md` or `AGENTS.md`.

Risks:

- Skills can carry hidden assumptions, tool expectations, external scripts, or instruction conflicts.
- Installing broad skillpacks can pollute Athena's behavior.
- Skill updates can drift unless pinned, tested, and documented.

Recommendation:

- Add a Chowmes Skill Intake and Promotion process before adding more external skills.
- Treat external skills as source material first, not automatically executable dependencies.
- Maintain a local skill registry with: source URL, license, owner, purpose, risks, scanned status, install status, tests, and rollback path.

Implementation gate:

- No new skill goes live until it passes static scan, manual review, bounded smoke test, and documentation update.

### 3. Pantheon Security Medusa

Source: https://github.com/Pantheon-Security/medusa

What it is:

- AI-first security scanner with AI/ML, LLM agent, MCP, RAG, traditional code, secrets, and AI editor config detection.
- It supports `medusa scan --git <URL>`, `medusa scan . --ai-only`, `medusa secrets scan`, JSON/HTML/Markdown/SARIF output, and project `.medusa.yml`.
- It explicitly scans agent instruction/config files including `AGENTS.md`, `CLAUDE.md`, `SKILL.md`, MCP configs, Codex config, and other AI tool files.
- License from GitHub API on 2026-07-10: AGPL-3.0.

What Hermes does not have without it:

- Current process depends on human caution and ad hoc inspection for external agent repos.
- There is no standard automated scan for repo poisoning, prompt injection, risky AI config, MCP config risk, or leaked secrets across agent histories.

Why it can make Hermes better:

- It gives Chowmes an explicit "scan before install" gate for external skillpacks, plugins, and agent repos.
- It can protect Athena/Argus from instruction poisoning and accidental secret exposure.
- SARIF/Markdown outputs can become durable security artifacts.

Risks:

- AGPL-3.0 means do not embed or vendor it into proprietary Chowmes/Hermes code without legal review.
- False positives are likely and need triage.
- Running secret scanners can touch sensitive local histories, so outputs must be private and redacted.

Recommendation:

- Adopt as an external CLI gate only.
- Do not vendor it.
- Do not run broad home-directory secret scans without explicit approval.
- Use it for local repo scans and external repo vetting before install.

Implementation gate:

- Add scripts that run Medusa in report-only mode against the current repo and candidate external repos.
- Store reports under a private, ignored artifacts path.
- Use failures as blockers for installing skills/plugins, not as automatic code changes.

### 4. Sentry Skills

Source: https://github.com/getsentry/skills

What it is:

- A public repository of agent skills used by Sentry's development team.
- It includes skills for AGENTS/CLAUDE maintenance, code review, code simplification, Django access review, Django performance review, GitHub Actions security review, bug finding, PR writing, prompt optimization, security review, skill scanning, and skill writing.
- License from GitHub API on 2026-07-10: Apache-2.0.

What Hermes does not have without it:

- Chowmes has strong operating rules, but not all of Sentry's targeted review workflows.
- We lack a mature borrowed pattern for "skill-scanner" and "agents-md" style maintenance.

Why it can make Hermes better:

- The `security-review`, `gha-security-review`, `find-bugs`, `skill-scanner`, and `agents-md` patterns are directly relevant to Hermes and Chowmes.
- Their skills can teach how a high-performing engineering team packages review workflows for agents.

Risks:

- Sentry's engineering practices are not Chowmes' operating constitution.
- Installing the whole pack would add irrelevant assumptions and extra triggers.
- Some skills are domain-specific, such as Django and Sentry API documentation, and should not become default Athena behavior.

Recommendation:

- Do not install the pack wholesale.
- Study and selectively port ideas into Chowmes-specific skills or runbooks.
- Candidate imports by idea, not raw install: `skill-scanner`, `security-review`, `gha-security-review`, `find-bugs`, and `agents-md`.

Implementation gate:

- Each candidate skill gets its own review: trigger fit, conflicts with AGENTS.md, tools expected, tests, and smoke examples.

### 5. Hermes Agent Self-Evolution

Source: https://github.com/NousResearch/hermes-agent-self-evolution

What it is:

- A Nous Research repository for evolving Hermes skills, tool descriptions, prompts, and eventually code using DSPy and GEPA.
- It optimizes by generating variants, evaluating against traces/datasets, enforcing gates, and producing PRs.
- Implemented phase is skill file optimization. Later phases are tool descriptions, prompt sections, tool implementation code, and continuous improvement.
- Repository license was not declared by GitHub API on 2026-07-10. README references MIT for DSPy/GEPA and AGPL for an external Darwinian Evolver engine.

What Hermes does not have without it:

- Hermes currently improves through manual edits, feedback, and testing.
- We do not yet have an automated loop that turns failed traces into scored prompt/skill improvements.

Why it can make Hermes better:

- Argus voice failures, CI report failures, and Athena operating-loop failures can become eval datasets.
- Skills can improve through measurable benchmarks instead of vibe-based editing.
- It can support the user's desire that Hermes compound rather than regress.

Risks:

- Without a benchmark suite, self-evolution optimizes the wrong thing.
- It can mutate voice, authority, security posture, or project boundaries.
- Continuous improvement against live Athena would be dangerous.
- License status needs review before operational embedding.

Recommendation:

- Use only after a Hermes evaluation harness exists.
- Start with one noncritical skill, not `SOUL.md`, live gateway code, or Argus production CI.
- Every evolved variant must land as a PR or patch proposal, with human review.

Implementation gate:

- Required first: tests for skill behavior, prompt-size limits, voice/style regression checks, security checks, and rollback.

### 6. Perplexity Bumblebee

Source: https://github.com/perplexityai/bumblebee

What it is:

- A read-only inventory collector for package, extension, developer-tool, MCP, and agent-skill metadata on macOS and Linux.
- It outputs structured NDJSON component records.
- It supports baseline/project/deep profiles.
- It reads lockfiles, install metadata, extension manifests, and supported MCP JSON configs. It does not run package managers or read source files.
- License from GitHub API on 2026-07-10: Apache-2.0.

What Hermes does not have without it:

- Chowmes lacks a fast inventory answer to: "Which packages, extensions, MCP servers, and agent skills are present right now?"
- Medusa can scan for risky patterns, but Bumblebee answers exposure inventory questions.

Why it can make Hermes better:

- It can identify what is installed across local and VPS contexts before a supply-chain advisory lands.
- It can produce a lightweight recurring security inventory without executing package managers.
- It complements Medusa: Bumblebee says what exists; Medusa says what looks risky.

Risks:

- It does parse config files that may contain environment values, even if it does not emit them.
- It does not parse all config types, such as Codex TOML and Continue YAML in v0.1.
- Deep scans may be too broad for Telegram-triggered work.

Recommendation:

- Adopt as a read-only inventory tool in local operator mode first.
- Consider a VPS cron only after verifying output privacy and runtime cost.
- Pair with Medusa reports for a security baseline.

Implementation gate:

- `bumblebee selftest` must pass.
- First real scans should run on the local repo and controlled directories only.
- Any recurring scan must write private artifacts and avoid dumping sensitive paths into Telegram.

### 7. GBrain

Source: https://github.com/garrytan/gbrain

What it is:

- An opinionated personal/team "brain" system for OpenClaw/Hermes-style agents.
- It stores knowledge in markdown git repos, syncs to a database, provides retrieval and graph/search, supports schema packs, ingestion workflows, skills, and a dream/enrichment cycle.
- It has commands for capture, file ingestion, webhook ingestion, schema detection, schema suggestions, and MCP connection.
- License from GitHub API on 2026-07-10: MIT.

What Hermes does not have without it:

- Current MyOS memory is split between `MEMORY.md`, local docs, the live VPS, and Obsidian source-of-truth notes.
- There is not yet a typed, schema-aware retrieval layer that understands projects, people, companies, meetings, ideas, sources, and analyses as first-class objects.

Why it can make Hermes better:

- The "brain repo is system of record" model maps well to Arijit's desire for durable operating memory.
- Schema packs could make MyOS less dependent on giant untyped markdown blobs.
- It could improve retrieval, routing, and cross-project continuity if integrated carefully with Obsidian.

Risks:

- It is a large opinionated system with many skills and conventions.
- Installing it wholesale could conflict with MyOS structure and Athena's existing operating model.
- It may overlap with Honcho, built-in memory, Obsidian, and current record-knowledge workflows.
- It adds database/runtime complexity.

Recommendation:

- Study as architecture, then pilot as a separate brain for one bounded domain.
- The best candidate pilot is "Hermes Improvement Research" or "Competitive Intelligence Knowledge", not all of MyOS.
- Do not replace Obsidian or `MEMORY.md` until a migration plan proves no loss of source-of-truth semantics.

Implementation gate:

- Define a mapping from current MyOS vault structures to GBrain schema packs before any import.
- Run duplicate/retrieval tests against known questions.
- Require export/rollback proof.

### 8. Turbovec

Source: https://github.com/RyanCodrai/turbovec

What it is:

- A Rust vector index with Python bindings based on TurboQuant.
- It targets local/private vector search with lower RAM usage, online ingest, SIMD search, filtered search, and no managed service.
- License from GitHub API on 2026-07-10: MIT.

What Hermes does not have without it:

- Hermes does not currently have a custom local compressed vector index for Obsidian or MyOS memory.
- Current retrieval relies on built-in memory/search, docs, web tools, and whatever underlying providers Hermes already supports.

Why it could make Hermes better:

- If MyOS grows into a very large private local corpus, turbovec could reduce memory cost and keep retrieval air-gapped.
- Filtered search is useful for tenant/profile/project isolation.

Risks:

- It is infrastructure, not an immediate product capability.
- Adding vector infra before measuring retrieval problems creates maintenance burden.
- It may duplicate what GBrain, Honcho, or Hermes native memory providers already solve.

Recommendation:

- Defer.
- Keep it on the watchlist for a measured private-RAG bottleneck.
- Do not add to live Hermes now.

Implementation gate:

- Only evaluate after a benchmark shows current retrieval fails on corpus size, latency, privacy, or cost.

### 9. Open Design

Source: https://github.com/nexu-io/open-design

What it is:

- A local-first desktop design/artifact app that uses coding agents as the design engine.
- It supports design systems via `DESIGN.md`, composable skills, plugins, prototypes, dashboards, decks, images, video, HTML/PDF/PPTX/MP4 export, and BYOK/OpenAI-compatible endpoints.
- It advertises support for Hermes and many other CLIs.
- License from GitHub API on 2026-07-10: Apache-2.0.

What Hermes does not have without it:

- Hermes can create artifacts through code and skills, but it does not have a polished local design studio loop for prototypes, dashboards, decks, and export workflows.
- Current Algolia and CI artifacts need strong design-system adherence and visual validation.

Why it can make Hermes better:

- It can give Athena/Argus a better artifact-production path for dashboards, executive decks, leave-behinds, and visual reports.
- It aligns with the existing rule that Algolia artifacts must use official design-system assets.
- Local-first operation is preferable to public hosted artifact generation.

Risks:

- Very large repo and large skill/plugin surface.
- Includes external model/provider and media workflows that may not fit Chowmes security posture.
- Could tempt product work into flashy artifacts before intelligence quality is proven.

Recommendation:

- Pilot locally only, not on VPS and not in Telegram.
- Use it for one artifact workflow: CI dashboard/report deck or Algolia-branded leave-behind.
- Scan before install, pin version, and keep generated artifacts separated from runtime code.

Implementation gate:

- Security scan, dependency review, local install smoke, one real artifact benchmark, and visual QA.

## Decision Matrix

| Resource | Decision | Why | Not having it means | Main risk | First gate |
|---|---|---|---|---|---|
| Honcho | Pilot | Automatic dialectic memory and peer separation | Manual-only durable memory | Privacy, prompt bloat, contamination | Isolated profile, capped context |
| Hermes skills docs | Adopt process | Native extension mechanism | No formal skill intake | Skill pollution | Skill intake checklist |
| Medusa | Adopt as external CLI | AI-agent security scan and repo poisoning detection | Manual-only security review | AGPL and false positives | Report-only local scan |
| Sentry skills | Selectively study/port | Mature review workflow examples | Reinventing review skills | Irrelevant assumptions | Per-skill review |
| Self-evolution | Defer until evals | Measurable prompt/skill improvement | Manual prompt iteration only | Optimizing wrong target | Benchmarks first |
| Bumblebee | Adopt read-only inventory | Installed component exposure view | Weak supply-chain inventory | Sensitive path/config handling | Selftest and scoped scan |
| GBrain | Architecture pilot | Schema-aware brain and retrieval | Untyped fragmented knowledge | System overlap and complexity | Bounded brain pilot |
| Turbovec | Defer | Private low-RAM vector index | No custom compressed vector layer | Premature infra | Retrieval benchmark |
| Open Design | Local artifact pilot | Better dashboards/decks/prototypes | Slower artifact/design loop | Huge dependency surface | Local-only scanned pilot |

## What To Throw Out Or Reject For Now

### Reject wholesale skillpack installs

Do not install all Sentry, GBrain, or Open Design skills. The value is in selected workflows. The cost is trigger pollution, conflicting standards, and new tool assumptions.

### Reject replacing `MEMORY.md` immediately

Honcho and GBrain are promising, but Athena's curated memory is currently a control surface. Replacing it now would trade known friction for unknown automatic memory behavior.

### Reject self-evolution against live production behavior

Self-evolution without evals is just automated prompt drift with nicer math. It should propose patches, not change Athena, Argus, or gateway behavior directly.

### Reject embedding Medusa

Medusa is useful as a CLI gate, but AGPL-3.0 makes embedding or vendoring a legal and architectural decision. Use it externally.

### Reject turbovec as a current live dependency

There is no measured local vector bottleneck yet. Keep the option warm, but do not add Rust/Python vector infrastructure before the retrieval problem is proven.

### Reject new public services for this adoption wave

No new public ports, no dashboard exposure, no memory server exposure, and no broad webhook endpoints without a separate security review.

## Implementation Plan

### Phase 0: Evidence freeze and adoption ledger

Deliverables:

- Create `hermes-core/resource-intake/docs/hermes-resource-adoption-plan.md`.
- Add `hermes-core/resource-intake/docs/hermes-external-resource-ledger.md` with each source, license, current version/commit, trust level, scan status, decision, and owner.
- Add private artifacts directory to `.gitignore` if missing, for example `.artifacts/security/`.

Acceptance:

- Each URL has a documented decision: adopt, pilot, study, defer, or reject.
- Each accepted/pilot resource has an explicit gate before live use.

### Phase 1: Security-first intake workflow

Status: completed locally on 2026-07-10.

Completion evidence:

- Medusa v2026.7.0 installed locally under `.tools/medusa-venv`.
- Bumblebee v0.1.2 installed locally under `.tools/bin/bumblebee`.
- Bumblebee checksum verification passed for `bumblebee_0.1.2_darwin_arm64.tar.gz`.
- `hermes-core/resource-intake/scripts/hermes-resource-scan . --run-medusa` completed with `medusa_status=ran`, `exit_code=0`.
- `hermes-core/resource-intake/scripts/hermes-inventory-scan . --run-bumblebee` completed with `bumblebee_status=ran`, `exit_code=0`.
- Focused tests passed: `python3 -m pytest hermes-core/resource-intake/tests/test_hermes_resource_intake.py -q` reported `5 passed`.
- No live Hermes/VPS/Athena/Argus/Telegram runtime changes were made.

Deliverables:

- Add `hermes-core/resource-intake/scripts/hermes-resource-scan` wrapper for candidate repos:
  - runs Medusa in report-only mode
  - records license and GitHub metadata
  - flags `.claude`, `AGENTS.md`, `CLAUDE.md`, `SKILL.md`, MCP configs, and install scripts
  - writes Markdown and JSON reports privately
- Add `hermes-core/resource-intake/scripts/hermes-inventory-scan` wrapper for Bumblebee:
  - runs `bumblebee selftest`
  - runs scoped project inventory
  - writes NDJSON privately
- Add a checklist in `hermes-core/resource-intake/docs/hermes-skill-intake-checklist.md`.

Acceptance:

- Running the wrappers does not print secrets.
- Reports are private and ignored by git unless intentionally promoted.
- Candidate external repos cannot be installed until the checklist is passed.

### Phase 2: Skill governance and selected workflow import

Deliverables:

- Build a Chowmes skill registry document.
- Review Sentry candidate skills:
  - `skill-scanner`
  - `security-review`
  - `gha-security-review`
  - `find-bugs`
  - `agents-md`
- Decide for each: install, port, rewrite, or reject.
- Create Chowmes-native versions when the workflow is valuable but Sentry assumptions are wrong.

Acceptance:

- Every installed/ported skill has a smoke test.
- No skill conflicts with AGENTS.md, SOUL.md, or the Telegram operator-mode restrictions.
- After any live skill change, run the required fresh-session and health-check scripts.

### Phase 3: Memory pilot

Deliverables:

- Create an isolated profile or lab environment for Honcho evaluation.
- Define recall evals using real Chowmes/MyOS prompts:
  - "Who owns CI delivery?"
  - "What must happen after SOUL.md changes?"
  - "What should Argus sound like?"
  - "Which systems are external to MyOS-Core?"
  - "What should Athena never enable without approval?"
- Compare built-in memory only, Honcho tools-only, Honcho capped context, and GBrain pilot retrieval.

Acceptance:

- Recall improves measurably without increasing prompt size beyond budget.
- No sensitive memory appears in inappropriate profile or peer context.
- Voice and identity tests pass.
- Rollback is documented.

### Phase 4: GBrain architecture pilot

Deliverables:

- Choose one bounded domain:
  - `Hermes Improvement Research`, or
  - `Competitive Intelligence Knowledge`.
- Map current Obsidian note types to GBrain schema types.
- Import a small corpus.
- Test capture, retrieval, schema detection, and export.

Acceptance:

- GBrain answers known retrieval questions better than current docs search.
- Obsidian remains source of truth or the new source-of-truth boundary is explicitly approved.
- Export/rollback works.

### Phase 5: Self-evolution only after eval harness

Deliverables:

- Build an eval corpus from prior failures:
  - Argus robotic voice drift
  - CI delivery readiness false positives
  - stale OpenRouter/Gemini routing memory
  - wrapper syntax errors
  - weak or industrial dashboard copy
- Add benchmark scripts for style, security, prompt size, skill trigger precision, and task success.
- Run self-evolution against one noncritical skill.

Acceptance:

- Candidate improvement beats baseline on held-out tests.
- No evolved patch lands without review.
- No production prompt or code is modified automatically.

### Phase 6: Design/artifact pilot

Deliverables:

- Scan Open Design.
- Install locally only if scan and dependency review pass.
- Create one artifact using real constraints:
  - CI dashboard review deck, or
  - Algolia-branded competitive intelligence leave-behind.
- Use the official Algolia design system when producing Algolia-facing artifacts.

Acceptance:

- HTML/PDF/PPTX export works locally.
- Visual output passes review.
- Generated files do not pollute runtime code.
- No new public service is exposed.

### Phase 7: Live rollout discipline

Deliverables:

- Only after a pilot passes, propose live Hermes changes.
- Back up config.
- Apply minimal config/skill changes.
- Refresh the relevant Telegram session.
- Run `scripts/chowmes-health-check --repair --send-test`.
- For Argus/CI, run `scripts/chowmes-ci-e2e-status --require-final-argus-only`.
- Record final decision and verification evidence.

Acceptance:

- Live behavior is verified from the real runtime, not inferred from files.
- Voice, delivery, memory, and security checks all pass.
- Rollback path is written before change.

## Verification Checklist For This Plan

- Source URLs opened and reviewed.
- GitHub metadata checked on 2026-07-10.
- Local Hermes docs and runbooks reviewed.
- Current Chowmes restrictions respected.
- No live runtime changes made.
- No external skills installed.
- No secrets printed.

## Source Metadata Snapshot

GitHub API metadata checked on 2026-07-10:

| Repo | Stars | Forks | Issues | License | Last push |
|---|---:|---:|---:|---|---|
| Pantheon-Security/medusa | 915 | 152 | 2 | AGPL-3.0 | 2026-06-24 |
| getsentry/skills | 850 | 45 | 26 | Apache-2.0 | 2026-06-30 |
| NousResearch/hermes-agent-self-evolution | 4604 | 524 | 95 | Not declared by API | 2026-06-17 |
| perplexityai/bumblebee | 4771 | 431 | 36 | Apache-2.0 | 2026-07-08 |
| garrytan/gbrain | 25764 | 3713 | 1277 | MIT | 2026-07-10 |
| RyanCodrai/turbovec | 12626 | 1116 | 12 | MIT | 2026-06-10 |
| nexu-io/open-design | 76874 | 8770 | 534 | Apache-2.0 | 2026-07-10 |

## Sources

- Hermes Honcho Memory: https://hermes-agent.nousresearch.com/docs/user-guide/features/honcho
- Hermes Skills System: https://hermes-agent.nousresearch.com/docs/user-guide/features/skills
- Medusa: https://github.com/Pantheon-Security/medusa
- Sentry Skills: https://github.com/getsentry/skills
- Hermes Agent Self-Evolution: https://github.com/NousResearch/hermes-agent-self-evolution
- Bumblebee: https://github.com/perplexityai/bumblebee
- GBrain: https://github.com/garrytan/gbrain
- Turbovec: https://github.com/RyanCodrai/turbovec
- Open Design: https://github.com/nexu-io/open-design
