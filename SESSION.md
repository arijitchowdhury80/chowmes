# SESSION — ChowMes / CI-OS Argus Telegram Repair

_Last updated: 2026-07-31. Resume artifact — read this section first. The older June PRISM section remains below for historical continuity, but it is not the current active work._

---

## CURRENT ACTIVE HANDOFF — CI-OS Intelligence Spine Phase 4

Active goal:

- `docs/goals/2026-07-30-ci-os-intelligence-spine-autonomous-goal.md`
- Goal status in Codex: blocked
- Blocked gate: Phase 4 Telegram human usefulness plus dashboard same-run parity

Primary handoff:

- `for-handoff/ci-os-argus-telegram-2026-07-31/START-HERE.md`

Current truth:

- Arijit rejected the live Telegram messages as repetitive and nonsensical.
- The rejection is valid. Treat it as a product/human-usefulness gate failure.
- Telegram transport passed before the rejection, but content did not pass.
- No new Telegram message was sent after the corrective deployment.

CI-OS source:

- Path: `/Users/arijitchowdhury/Dropbox/AI-Development/CI-OS`
- Branch: `codex/ci-os-phase0-baseline`
- Remote: `https://github.com/arijitchowdhury80/algolia-competitive-intelligence.git`
- Latest pushed commits:
  - `3188c81` - Align weekly unavailable Telegram next check.
  - `36d3326` - Fix Argus Telegram watch brief semantics.

ChowMes status:

- Status artifact: `docs/status/2026-07-30-ci-os-intelligence-spine-phase4-local-delivery.md`
- Latest pushed commit: `405d47f` - Record deployed CI-OS Telegram preview repair.

VPS deployment:

- Active CI-OS package marker: `3188c81db5f3e393c920f2ea69147f61e35e2bf6`
- Rollback bundle: `/opt/cios/releases/rollback-before-weekly-unavailable-next-check-20260731T061153Z.tar.gz`
- Remote package contract after deploy: `PASS: CI-OS Hermes package contract satisfied`

Deployed no-send preview artifacts:

- `/opt/cios/app/out/argus-phase4-deployed-daily-preview.txt`
- `/opt/cios/app/out/argus-phase4-deployed-weekly-preview.txt`

Corrected daily preview:

```text
Argus read: Watch, no owner action
Run: product-market-local-tenant-1-20260730T204949Z
Window: today

Market movement: Shopping Assistant
Shopping Assistant is heating up across Luigi's Box, Constructor, and Bloomreach.

Why it matters: Product and market-conversation proof exist, but no tenant-side demand evidence was captured, so Argus is watching instead of promoting an owner action.

Next check: Collect GA / Looker demand evidence for Shopping Assistant before promoting it into a recommendation.

Proof: Product Reality present (524); Market Conversation present (80); Audience Demand missing
```

Resume rules:

- Use `development-loop`, not the retired predecessor.
- Do not proceed to Phase 5.
- Do not send Telegram again unless Arijit explicitly approves.
- If approved, send only the corrected daily brief.
- Do not send a weekly synthesis from a daily packet.
- Dashboard/public same-run parity remains pending unless explicitly moved to Phase 5.
- Do not modify Hermes core. CI-OS is a separately versioned extension.
- Do not discard or revert user changes.

---

# Historical Session — ChowMes / My OS · PRISM-engine direction + PetSmart audit

_Last updated: 2026-06-19. Resume artifact — read this first, then MEMORY.md index at `~/.claude/projects/-Users-arijitchowdhury-Dropbox-AI-Development-Personal-ChowMes/memory/`._

---

## 🎯 NEXT SESSION = brainstorm the MECHANICS of the autonomous audit engine (clean context, step by step)
Arijit gets the **direction** but not the **mechanics** yet. **Do NOT jump to building.** Walk it concretely.

**Resume action:**
1. Read this file + memory `prism-engine-direction.md` (the full strategic direction) + `verify-rendered-output-vs-reference.md` (the key lesson).
2. Read the Discovery-OS doc: `~/Dropbox/AI-Development/Discovery/Discovery-OS-v1.md` (§9 "PRISM Translation Ruleset" is the build spec for the synthesis layer).
3. Then brainstorm, step by step: **how does one Telegram line from a rep — "Hey Hermes, run an Algolia Search Audit for Costco.com" — become a gated, executed, data-validated, delivered audit + a Discovery-OS call plan?** Explain mechanics, not just direction.

### The direction (decided 2026-06-19)
- **Build the ENGINE + a Telegram/Hermes control plane. Do NOT build a PRISM web app.** "PRISM" = the intelligence engine + outputs (how Discovery-OS uses the word), not a UI. Telegram is the interface + chat.
- **Internal now; possibly productise/sell externally later.** Fine because the engine is durable and the interface is a swappable skin.
- **Target UX:** each rep has their own Telegram bot → Hermes (a dedicated Algolia-research orchestrator agent with all the skills) → "research Costco", interactive follow-ups, "email me the report/pitch" → full audit runs + returns. Mobile/anywhere.

### Architecture — 3 planes (refine "Hermes spawns Claude" → queue + workers; don't block Hermes)
- **CONTROL** = Hermes: per-rep identity, intent parse, job queue, progress msgs, gating verdicts, delivery.
- **EXECUTION** = headless Claude (`claude` CLI / Agent SDK) + 22 algolia skills + MCP, as disposable context-isolated workers (← also the fix for context-clearing).
- **DATA** = persisted **deal-intelligence object** (findings + call plans + cached prospect data, reused across reps/roles). Discovery-OS §7.3/§9.2.5 needs this too.

### The convergence (why these aren't separate streams)
Autonomy + context-economy + Discovery-OS + persona report-IA = ONE build:
- Discovery-OS §9 is the spec. `audit-data.json` already produces its `finding` categories. **Missing piece = the translation layer (§9.2.3) + single-page call-plan generator (§9.4)** → a new Wave-5 synthesis module.
- **Gating system = Discovery-OS's hard precondition** (confidence scoring, evidence URLs, reviewer gate for High-risk×Low-confidence, **design-verify gate**). The wrong-template incident below is exactly the failure Discovery-OS calls "nearly unrecoverable." Build gates once, serve both.
- **Report-IA fix** ("too much info, people get lost") = adopt §9.4 single-page compression + persona_fit (Merch/Product/Eng/Exec) + 6 archetypes.

### Top holes / open design Qs (stress-tested)
1. **Browser wave from a datacenter IP gets blocked** (Akamai/Cloudflare) — stealth only worked from Arijit's residential Mac. **#1 risk.** Need a residential-IP runner / proxies / degraded-and-flagged.
2. Gates HARD-fail → human review queue; never auto-deliver unverified output to a prospect.
3. Secrets (Algolia Usage/Analytics keys) can't flow through Telegram — vault + non-chat path. Golden telemetry only exists for EXISTING customers; net-new = displacement (thin data → SPIN fallback).
4. Async-over-chat; 5. cost/queue/caching (dedup repeat prospects); 6. headless MCP (Crossbeam OAuth degrades).

### Build order
(1) engine → finding-object + gates · (2) Discovery synthesis module · (3) execution/queue/worker + data store · (4) Telegram/Hermes control plane · (5) persona report-IA.

### 3 questions to answer before formalizing
(a) always-on residential-IP machine for the browser wave, or budget proxies? (b) #reps / all Algolia AEs? (c) targets mostly existing Algolia customers (golden-data expansion) or net-new prospects (displacement)?

> When ready to formalize (after brainstorming mechanics): a strategy canvas (internal→external) + an architecture ADR + a build plan for steps 1–2. Also owed: convert captured lessons into ENFORCED gates (notes ≠ prevention).

---

## ✅ DONE THIS RUN — PetSmart Algolia Search Audit: COMPLETE & PUBLISHED (rich design)
Live: `https://algolia-arian-v2.vercel.app/petsmart/`. Score **5.8** "Strong Foundation, Unactivated Upside"; factcheck **PROCEED 9.2/HIGH** (0 fabrications); eval **10.0/10**. EXISTING-customer EXPANSION audit (App ID `97P6EWKR25`). ROI aligned across deck + business case (Arijit's call): **$60–71M conservative / $146–173M moderate, 76–177×, payback <1 quarter**, sized on PetSmart's own telemetry (15.98% no-results ≈100M dead-end searches/yr, CTR 10.98%, click pos 13.1, CVR 4.41%, ~45% Mar-2026 volume step-down). Athena (Hermes `default`) closed the board + gave the exec verdict (`deliverables/athena-executive-verdict.md`).

### ⚠️ The big lesson from this run (do not repeat)
The deck was FIRST rendered + published from the skill's **simplified `index-template.html`** (role-tab, ~170KB) — NOT the rich `renderSections` design every other audit uses. Token-marker checks (brand CSS present, 0 unreplaced tokens) **passed on the wrong template**, so it was wrongly marked "contract held." Arijit caught it. **Fixed:** rebuilt PetSmart's deck rich + re-rendered via the official pipeline (reproducible, verified headless across all 5 tabs — 0 JS errors, 0 donor leakage); **restored the skill's rich `index-template.html`** (reconstructed from a shipped audit; the rich source had been overwritten by a simple stub and is not git-tracked; simple stub backed up to `templates/index-template.simple.bak.html`). Lesson → memory `verify-rendered-output-vs-reference`: **token checks ≠ design correctness; diff against a reference / screenshot it; never trust a prior "verified" note for presentation.**

### Open PetSmart follow-ups (flagged, non-blocking)
- **Chewy head-to-head** still HTTP-429 blocked → needs residential-proxy/manual run before the AE call.
- **Hub gallery** (`~/algolia-arian-v2/index.html`) not regenerated — deck live at the direct `/petsmart/` route, not listed on the landing page (regenerating risks pulling in other companies' untracked WIP → do surgically).
- **Logo** is a clearbit URL (loads live) — could embed as data URI for offline robustness.
- Schema additions this run (`search_analytics` in `audit_data_schema.py` + `audit-data.schema.json`) are Optional/harmless; the rich template shows analytics via findings, not that block.

---

## REFERENCE FILES / COMMANDS
- **Discovery-OS (methodology + build spec):** `~/Dropbox/AI-Development/Discovery/Discovery-OS-v1.md` (§9 = PRISM Translation Ruleset).
- **PetSmart codification log (full pipeline build-spec + every gotcha + the wrong-template correction):** `~/Dropbox/AI-Development/Personal/Obsidian-Vault/MyOS/Projects/PRISM/Sessions/2026-06-19-petsmart-pipeline-codification-log.md`.
- **PetSmart workspace:** `~/AI-Development/Algolia Search Audit/PetSmart/deliverables/` (index.html SPA, petsmart-audit-data.json, petsmart/ae-report+battle-card+leave-behind.html, business-case.md, playbook.md, abx-campaign/, strategic-signal-brief.md, athena-executive-verdict.md, factcheck-report.md, screenshots/; eval at PetSmart/eval/).
- **Skill:** `~/.claude/skills/algolia-search-audit/` — AGENT-CONTEXT.md (contract), `scripts/render-audit.ts` (site→`index-template.html`, RESTORED rich), `scripts/audit_data_schema.py` (pydantic gate). Render from the deliverables dir: `cd <deliverables> && deno run -A ~/.claude/skills/algolia-search-audit/scripts/render-audit.ts petsmart site` (reads/writes cwd). NOTE: render's style+schema gates fail-open from the deliverables cwd — run them manually or render from scripts/.
- **Hub:** `~/algolia-arian-v2` (GitHub arijitchowdhury80/algolia-arian-v2; Vercel auto-deploy on push to main). Has untracked WIP for ~8 other companies — NEVER `git add -A`; stage only target paths.
- **Hermes/Athena:** `ssh -i ~/.ssh/chowmes_ed25519 chowmesadmin@72.61.72.147` → `sudo docker exec -u 10000 -i hermes hermes -p default -z "..."` (avoid apostrophes/`$`/`"` in the prompt; SSH single-quote wrapping; macOS has no `timeout`). Bash heredocs with `$` in code → use `<<'PY'` (quoted) or the shell mangles `$110`/`$9.6B`.

## WHAT HAS NOT BEEN DONE
- The engine/gates/Discovery-module/Telegram architecture is DESIGN-ONLY (brainstorm). Nothing built. The 3 open questions are unanswered. Lessons are notes, not enforced gates yet.
