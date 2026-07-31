# Goal: Complete CI-OS Intelligence Spine, Distribution, And Product UX

Date: 2026-07-30
Status: ready for activation
Owner: Arijit Chowdhury
Runtime boundary: Hermes remains the runtime OS. CI-OS remains a separately versioned extension. This goal does not authorize Hermes core changes.
Required workflow: `development-loop`

## Objective

Complete CI-OS as a trusted Competitive Intelligence Operating System by first proving the canonical Argus intelligence spine, then making Telegram, the mobile dashboard, the 3D Market Field, Evidence Lab, Admin, daily delivery, and weekly synthesis consume that same intelligence contract.

The system is not complete because a controlled pilot artifact exists. It is complete only when the live operating loop produces one run-bound, evidence-backed, self-explaining intelligence packet that a business user can understand and act on from Telegram or the dashboard without builder explanation.

## Why This Goal Exists

The prior CI-OS completion goal reached a mechanically verified controlled pilot, but Arijit rejected the product experience as not self-explaining. The remaining risk is not merely UI polish or Telegram delivery. The deeper risk is semantic drift: different parts of CI-OS may be rendering fragments from product evidence, market conversation, audience demand, recommendations, and run diagnostics without one canonical intelligence spine.

This goal converts the open-ended "make it understandable" problem into binary gates. No phase may pass from confidence estimates, waived design authority, test counts alone, stale data, or a manually explained page. Each gate must produce artifacts, tests, live evidence, and a yes/no acceptance result.

## Source Material To Read Before Work

Start every resumed execution by reading these files, then update this list if a newer canonical artifact supersedes them:

- `docs/goals/2026-07-13-complete-ci-os-algolia-pilot.md`
- `docs/status/2026-07-19-ci-os-current-goal-freeze.md`
- `docs/status/2026-07-13-ci-os-project-dossier.md`
- `docs/plan/2026-07-28-ci-os-arrie-ux-ia-gate.md`
- `docs/plan/ci-os-product-architecture.md`
- `docs/plan/e2e-validation.md`
- `/Users/arijitchowdhury/Dropbox/AI-Development/CI-OS/docs/planning/Argus-product-market-intelligence-spine.md`
- `/Users/arijitchowdhury/Dropbox/AI-Development/CI-OS/docs/workspace/cios-intelligence-core/_status.md`
- `/Users/arijitchowdhury/Dropbox/AI-Development/CI-OS/docs/workspace/arrie-phase6-3d-field/_status.md`, if present in the active CI-OS checkout
- `/Users/arijitchowdhury/.agents/skills/development-loop/SKILL.md`

## Non-Negotiable Product Contract

CI-OS must produce a canonical Argus Intelligence Packet for every successful run.

The packet must include:

- run identity: run id, generated time, cadence, time window, release commit, package id
- evidence planes: product reality, market conversation, Audience Demand, source health
- market movement: hotspots, leading entities, leading capabilities, trend direction, velocity, cooling/rising state
- semantic read: facts, inferences, hypotheses, contradictions, rejected reads, unknowns
- strategic read: why the movement matters to Algolia, what market belief it implies, what may happen next
- attention state: what deserves attention now, what is monitored, what is quiet, what is blocked
- recommendations: named owner, action, urgency, why now, expected outcome, next review date
- proof graph: evidence refs, source URLs, source family, confidence, contradiction, missing-proof boundaries
- next monitoring actions: what Hermes / Argus should recheck, collect, or learn next
- delivery status: whether Telegram and public/dashboard publication actually consumed this same packet

No consumer may create an independent story from raw tables. Telegram, dashboard, 3D Market Field, weekly synthesis, Evidence Lab, Admin, and public status must render from the same packet or explicitly say they have no current packet.

## Autonomous Operating Rules

Use `development-loop` full path unless a stage artifact explicitly proves a light path is safe. This goal touches schema/API/external surfaces, Telegram delivery, production UI, security, and live deployment, so the default is full path.

Use subagent-driven execution when available. Before dispatching, verify that the named subagent or tool exists. If unavailable, execute the checklist inline and record that substitution in the phase artifact.

Run parallel work only inside a phase after the phase contract is known. Do not run later phases before predecessor gates pass.

Use TDD for all implementation. Every behavior change starts with mapped or failing tests.

Do not modify Hermes core. CI-OS may use Hermes scheduling, queueing, gateway, and runtime boundaries, but business logic belongs in the CI-OS package.

Do not discard or revert user changes without explicit approval. If the worktree contains cloud-sync conflicts, generated artifacts, or unrelated dirty files, inventory them and isolate the goal work in a clean branch or worktree.

Do not claim done without live verification. A passing local test suite is necessary but not sufficient.

## Agent Workstreams

The goal is designed for multi-agent execution after Phase 0 establishes the real source and runtime baseline.

### Workstream A: Forensic State Mapper

Purpose: discover current truth before architecture or implementation.

Outputs:

- current branch, commit, remote, dirty tree, generated artifacts, conflict files
- deployed package commit and release bundle
- latest Hermes cron status and queue permissions
- latest CI-OS run id, dashboard JSON, public status, Telegram delivery rows, weekly synthesis rows
- gap matrix from required product questions to existing code/tests/live evidence

### Workstream B: Intelligence Contract Architect

Purpose: design the canonical Argus Intelligence Packet and map current objects into it.

Outputs:

- packet schema and versioning policy
- source mapping from existing objects such as `ProductMarketIntelligenceBrief`, `IntelligenceSpine`, `decision_read`, `movement_map`, `pattern_observations`, and `argus_recommendations`
- migration or adapter plan if current objects are retained
- consumer contract for Telegram, dashboard, 3D Market Field, Evidence Lab, Admin, and public status

### Workstream C: Evaluation And Test Designer

Purpose: make product understanding testable.

Outputs:

- golden scenario fixtures: actionable day, quiet verified day, degraded day, contradiction day, stale evidence day, missing demand day, weekly trend day, noisy duplicate day
- machine assertions for every required packet field
- semantic assertions that consumers answer the required business questions
- live validation checklist for Telegram, dashboard, mobile, 3D, weekly, public status, and run identity

### Workstream D: Engine Implementer

Purpose: make the CI-OS engine produce the packet from evidence.

Outputs:

- packet builder
- persistence and publication path
- current-run and historical-window logic
- confidence, contradiction, blocked-action, unknown, and next-monitoring logic
- learning-loop integration

### Workstream E: Consumer Implementer

Purpose: make every product surface consume the packet.

Outputs:

- daily Telegram command brief
- weekly synthesis brief
- mobile dashboard command surface
- 3D Market Field packet graph
- proof drawer and Evidence Lab packet graph inspection
- Admin operator surface for run, source, delivery, and packet health

### Workstream F: Verification, Security, And Release Reviewer

Purpose: block false completion.

Outputs:

- code review
- security review
- public artifact redaction and safety scan
- run-bound publication verification
- live Playwright desktop/tablet/mobile evidence
- live Telegram delivery evidence
- release record, rollback evidence, and monitoring verdict

## Phase Gates

### Phase 0: Truth Freeze And Baseline

Objective: establish the real current state before changing anything.

Work:

1. Inspect ChowMes repo and CI-OS repo status, branch, remote, dirty files, ignored/generated files, and conflict files.
2. Identify authoritative source directory and GitHub remote.
3. Identify deployed CI-OS commit, release bundle, SHA, package path, and public site artifact.
4. Inspect Hermes cron, CI-OS queue, `cios` user ownership, run-queue permissions, delivery rows, and weekly/daily status.
5. Export current live dashboard JSON, public status JSON, latest Telegram delivery records, latest weekly reports, and latest `product_market_run_intelligence`.
6. Write a gap matrix showing every product question and whether it is answered by current engine, current dashboard, current Telegram, current tests, and live evidence.

Exit gate:

- No unknown source-of-truth ambiguity.
- No unclassified dirty source files.
- No deployed-state mystery.
- Current live status is documented with run ids and evidence.
- The gap matrix exists and marks each item pass, fail, or blocked.

Auto-advance: yes, if the exit gate passes.

### Phase 1: Intelligence Packet Contract

Objective: define the canonical packet that all consumers must use.

Work:

1. Decide whether the packet is a new `ArgusIntelligencePacket` type or a versioned evolution of `ProductMarketIntelligenceBrief`.
2. Define packet schema, required fields, optional fields, version, cadence, time-window, and evidence refs.
3. Define how packet status maps to actionable, watch, quiet, degraded, blocked, and failed states.
4. Define how facts, inferences, hypotheses, contradictions, rejected reads, confidence limits, and unknowns are represented.
5. Define exact consumer rules: no dashboard, Telegram, weekly, or public status surface may synthesize its own business read outside the packet.
6. Write schema and contract tests before implementation.

Exit gate:

- The packet contract answers all required product questions on paper.
- Contract tests fail before implementation or prove equivalent existing behavior.
- Arijit approves the packet contract if it changes product semantics.

Human gate: yes.

### Phase 2: Intelligence Scenario Harness

Objective: prove the brain against scenario fixtures before UI work.

Work:

1. Build deterministic fixtures for actionable, quiet, degraded, contradiction, stale, missing-demand, weekly-trend, and noisy-duplicate scenarios.
2. Assert each fixture produces correct movement, hotspot, pattern, strategic read, action, blocked action, proof, and confidence state.
3. Assert no recommendation is promoted without required evidence and confidence.
4. Assert quiet means verified quiet, not missing collection.
5. Assert Audience Demand is audience response, not competitor proof.
6. Assert weekly synthesis identifies change over time, not a daily recap with a weekly title.

Exit gate:

- All scenario tests pass.
- At least one fixture proves action promotion.
- At least one fixture proves action blocking.
- At least one fixture proves weekly pattern formation.
- No fixture requires a UI or Telegram renderer to invent meaning.

Auto-advance: yes.

### Phase 3: Engine Implementation And Persistence

Objective: produce and persist the canonical packet from real CI-OS evidence.

Work:

1. Implement or adapt the packet builder.
2. Persist packet output with run id, commit, cadence, time window, and evidence refs.
3. Bind packet to `product_market_run_intelligence`, dashboard state, public status, and delivery records.
4. Add current-run and historical-window logic for Today, 7D, 30D, and custom.
5. Add contradiction and rejected-read handling where evidence conflicts.
6. Add next-monitoring actions that feed future runs without modifying Hermes core.
7. Add export and inspection tooling for the latest packet.

Exit gate:

- A fresh local run produces a packet.
- The packet has one run id across persistence, dashboard state, public status, and delivery plan.
- Packet output passes scenario and integration tests.
- No consumer-specific story is required to understand packet content.

Auto-advance: yes, after tests and local integration pass.

### Phase 4: Telegram Daily And Weekly Gateway

Objective: make Telegram the mobile gateway into CI-OS, not an error stream.

Work:

1. Render daily Telegram command brief from the packet.
2. Render weekly synthesis from weekly packet or weekly packet view.
3. Add quiet verified, degraded, blocked, and failure message formats.
4. Include dashboard deep links and proof links.
5. Record every send attempt in CI-OS delivery tables with true sent, failed, blocked, or skipped status.
6. Add forced weekly validation mode so weekly delivery can be tested without waiting for Sunday.
7. Leave old paused Argus V0 cron paths disabled unless explicitly reactivated by a new architecture decision.

Exit gate:

- One forced daily Telegram brief is sent from a fresh packet.
- One forced weekly Telegram brief is sent from a fresh packet or weekly packet view.
- Delivery rows show true send status.
- Telegram and dashboard point to the same run id and same core read.
- Failure messages never pretend to be intelligence.

Auto-advance: no. Human must confirm Telegram usefulness.

### Phase 5: Dashboard, Mobile, And 3D Market Field Consumers

Objective: make the dashboard and 3D Market Field self-explaining packet consumers.

Work:

1. Make the first screen answer: what is hot, what changed, why it matters, and what to do.
2. Render Market Field from packet graph nodes and edges, not ad hoc state.
3. Keep true 3D only where semantics are strict: node type, edge type, pulse, halo, brightness, color, warning ring, and time trails must each mean one thing.
4. Add click-to-reveal flow: Market Field -> Selected Movement -> Decision Layer -> Proof Drawer.
5. Make Today, 7D, 30D, and custom change the actual packet view or packet query, not only CSS state.
6. Build mobile command layout: hotspot/story summary, selected movement, action, proof, evidence, admin split.
7. Move raw rows, diagnostics, failed checks, source walls, and admin operations out of the first-read experience.

Exit gate:

- Playwright validates desktop, tablet, and mobile.
- Canvas is nonblank and interactive where 3D is enabled.
- Critical controls are keyboard reachable.
- No text overlap or clipped critical selectors.
- A reader can answer the acceptance questions without an admin guide.

Auto-advance: no. Human usefulness gate required.

### Phase 6: Evidence Lab And Admin Separation

Objective: make proof and operations inspectable without polluting the business read.

Work:

1. Evidence Lab exposes claims, evidence refs, source URLs, source health, contradictions, unknowns, and rejected reads from the packet proof graph.
2. Admin exposes cron/run status, packet freshness, delivery health, source registry, ingestion state, public artifact safety, and release status.
3. Admin write paths require proper auth/token behavior and tenant ownership checks.
4. Evidence reached from any promoted claim must trace back to source.
5. Failed sources must reduce confidence visibly.

Exit gate:

- Every promoted claim, movement, hotspot, recommendation, and weekly pattern has reachable proof.
- Admin and Evidence Lab no longer appear as first-read business narrative.
- Security tests pass for write auth, tenant ownership, and public redaction.

Auto-advance: yes, unless security review finds critical issues.

### Phase 7: Runtime, Release, And Live E2E

Objective: prove the full live operating loop from Hermes cron through CI-OS packet through consumers.

Work:

1. Verify Hermes schedules and enqueues; CI-OS runs as `cios`; root/admin user execution is not part of normal operation.
2. Repair queue permissions or ownership drift if discovered.
3. Run fresh daily packet generation through the production path.
4. Run forced weekly synthesis through the production path.
5. Verify atomic publication and one run id across public status, dashboard JSON, HTML, Telegram, delivery rows, and release record.
6. Run public artifact redaction and safety scans.
7. Run dashboard Playwright validation on `https://ci.chowmes.com/`.
8. Run live Telegram delivery validation.
9. Record rollback path and verify previous release can be restored.

Exit gate:

- `ci_canonical_intelligence_ready=yes`
- `ci_canonical_delivery_ready=yes`
- latest daily status is ok
- latest weekly validation status is ok
- delivery ledger has sent rows
- public status and dashboard share the same run id
- rollback is documented and tested

Auto-advance: no. Human staging / live acceptance gate required.

### Phase 8: Monitoring And Completion Verdict

Objective: prove the operating system remains useful after launch, not only during a forced run.

Work:

1. Observe at least 48 hours or two scheduled daily cycles, whichever is stronger for current scheduling reality.
2. Capture daily Telegram usefulness and delivery status.
3. Capture dashboard packet freshness and public status.
4. Capture weekly synthesis validation if a weekly window is due; otherwise keep forced weekly proof as the acceptance substitute.
5. Track false quiet, source failure, stale data, permission drift, delivery failure, UI regression, and packet inconsistency.
6. Update dossier, goal status, release record, tracker, and any required vault/Bible pointers only after verified gates pass.

Exit gate:

- Two scheduled daily cycles pass or an explicit human waiver states why forced live validation substitutes for schedule time.
- No packet/consumer drift is found.
- No critical source, security, or delivery blockers remain.
- Arijit accepts the system as usable from Telegram and dashboard.
- Final status file records evidence, commands, run ids, commits, delivery ids, screenshots, and residual risks.

Human gate: yes.

## Required Acceptance Questions

The final product fails if Arijit cannot answer these from the live product without explanation:

1. What is the main market movement?
2. Which competitors or partners are driving it?
3. What changed over the selected time window?
4. Is this daily noise, weekly pattern, monthly trend, or custom-window movement?
5. Why does it matter to Algolia?
6. What should a named team do next?
7. Why is that team/action prioritized over another?
8. What evidence supports the read?
9. What evidence contradicts or weakens the read?
10. What is unknown or confidence-limiting?
11. What sources failed, and how does that reduce trust?
12. What should Argus monitor next?
13. How do I drill into proof without losing the story?
14. How do I switch from Telegram to dashboard and see the same run?
15. How do I know Hermes executed the run and CI-OS produced the intelligence?

## Validation Matrix

| Layer | Required proof |
|---|---|
| Contract | Packet schema tests and fixture validation |
| Engine | Evidence-to-packet integration tests |
| Semantics | Scenario harness for action, quiet, degraded, contradiction, stale, missing-demand, weekly, noisy duplicate |
| Consumers | Telegram, dashboard, 3D, Evidence Lab, Admin render from packet |
| Runtime | Hermes cron / queue / `cios` runner live verification |
| Release | One run id across release, public status, dashboard, Telegram, delivery rows |
| Security | Public redaction, auth/write checks, tenant boundary checks |
| UX | Playwright desktop/tablet/mobile plus human usefulness acceptance |
| Monitoring | 48-hour or two-cycle observation with delivery and freshness checks |

## Completion Definition

This goal is complete only when all phase gates pass and the final status artifact proves:

- one canonical Argus Intelligence Packet exists for fresh successful runs;
- every consumer renders from that packet;
- daily Telegram works as a mobile command brief;
- weekly synthesis works as a pattern brief;
- dashboard and 3D Market Field are self-explaining packet consumers;
- Evidence Lab and Admin are separated from the business read;
- live production path runs through Hermes and `cios`, not root/manual operation;
- public artifacts are safe, atomic, and run-bound;
- tests, live validation, and human acceptance all pass;
- documented residual risks are non-critical and explicitly accepted.

No completion claim may use phrases like "mostly ready," "pilot-complete," "controlled waiver," or "confidence is high" as a substitute for the binary gates above.
