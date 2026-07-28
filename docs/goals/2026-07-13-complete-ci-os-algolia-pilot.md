# Goal: Complete The CI-OS Algolia Pilot

Date: 2026-07-13
Status: active
Source plan: `docs/plan/2026-07-13-ci-os-completion-plan.md`
Source dossier: `docs/status/2026-07-13-ci-os-project-dossier.md`
Codex task: `019f4976-1149-7531-8852-effeb8392a8a`

## Objective

Complete Phases 0 through 8 of the approved CI-OS completion plan and release a controlled, monitored Algolia pilot. The finished system must combine current product evidence, competitor conversation, Algolia audience demand, and Argus reasoning into source-backed, confidence-scored recommendations that named business teams can use.

Hermes remains the runtime OS. CI-OS remains a separately versioned extension. This goal does not authorize changes to Hermes core.

## Autonomous Operating Loop

For each phase, Codex will run this loop:

1. Restore current state from the plan, dossier, repository, vault, tracker, Bible, and live environment.
2. Inspect the affected code, tests, runtime path, and deployed state before deciding what to change.
3. Break the phase into the smallest testable execution slice.
4. Add or map failing tests before changing existing behavior.
5. Implement the slice within the CI-OS extension boundary.
6. Run code, security, architecture, data-semantic, and UX review appropriate to the slice.
7. Rectify every critical or important finding.
8. Verify locally, then verify through the real Hermes and production path when the phase requires it.
9. Record commands, outputs, run IDs, commit IDs, artifact paths, and unresolved risks.
10. Update the dossier, vault, project tracker, and Bible status after the phase gate.
11. Evaluate the documented exit gate. Advance automatically only when it passes.

An identical failed action must not be repeated without new evidence or a changed hypothesis. A failure starts a bounded debugging loop; it does not lower the gate.

## Phase Sequence

| Phase | Deliverable | Gate before advancing |
|---|---|---|
| 0. Contain and baseline | Auditable code, artifact, and deployed baseline | Clean reviewable branch with no unknown source files |
| 1. Restore Hermes execution | Hermes-owned scheduled operating loop | Two consecutive healthy scheduled Hermes runs |
| 2. Trustworthy publication | Atomic, fresh, run-bound public state | Planted defects fail and one fresh complete run passes |
| 3. Product Muscle | Scout-backed shipped-product comparison | Current evidence or explicit unknown for every active competitor |
| 4. Audience Demand | GA4 or Looker inward-demand evidence | Nonzero traceable seven-day demand signals |
| 5. Argus intelligence | Cross-plane patterns, recommendations, and learning | One accepted, non-obvious, usable recommendation and proven learning effect |
| 6. Product IA | Accepted business workflows and embedded Argus actions | Representative users understand priority, evidence, confidence, and action |
| 7. E2E validation | Backend, Hermes, semantic, frontend, UX, accessibility, security, and live proof | Corrected production launch gate and human acceptance pass |
| 8. Algolia pilot | Versioned release, monitoring, rollback, users, and feedback loop | Repeatable trusted decisions used in real work |

## Current Execution Boundary

Phase 0 passed on 2026-07-13 after the clean CI-OS branch and deployed runtime baseline were mapped. Phase 1 passed on 2026-07-14 after two consecutive real Hermes runs completed as `cios` with exit code 0, no permission errors, no timeout, no orphan work, no ownership drift, and fresh blocked diagnostics. Phase 2 passed on 2026-07-27 ET / 2026-07-28 UTC after a fresh Hermes-wrapper run published run-bound public status and semantic dashboard artifacts for `cios-20260728T032901Z-3409872`, with live click validation passing. Phase 3 Product Muscle, Phase 4 Audience Demand, and Phase 5 Argus Intelligence have passed for the controlled pilot, with Phase 4 and Phase 5 retaining limited-confidence caveats. Phase 6 Product IA passed for the controlled pilot on 2026-07-28 after CI-OS commit `760f03c` deployed to `/opt/cios/app`, public release `cios-20260728T122836Z-3951326` became current, public redaction and safety scans passed, live dashboard click validation passed on `https://ci.chowmes.com/`, and Arijit's approval was recorded as the temporary pilot design-authority waiver. Phase 7 technical E2E validation passed on 2026-07-28 after CI-OS commit `2f7385f4afdcdd2af771e34d8e92bdc629a990fa` deployed to `/opt/cios/app`, package contract passed, live operational safety passed, public redaction and safety scans passed, live dashboard click validation passed, and aggregate launch readiness passed with `42` active sources, `4` failed source fetches, and a controlled-pilot source failure ratio of `0.0952 <= 0.10`. Arijit accepted the Phase 7 human usefulness gate on 2026-07-28. Phase 8 controlled pilot release `cios-pilot-algolia-20260728-f8f8a3c` is now live from CI-OS commit `f8f8a3cfd5f39577ff224aabdc3c195e59ddc7a4`, with rollback preserved, release bundle `/opt/cios/releases/f8f8a3c.tar.gz`, pilot monitoring passed, and observation active. The live public status exposes one open PMM recommendation for pilot-window disposition, and CI-OS now generates `/opt/cios/app/out/phase8/argus-pmm-narrative-brief.json` as a Product Marketing draft work artifact. The formal exit artifact `/opt/cios/app/out/phase8/cios-phase8-exit.json` currently fails only on `named_team_disposition_final`. Recurring GA4 automation is deferred until credentials are provided.

## Human Decision Boundaries

Autonomous work pauses only when progress depends on a decision or external input that cannot be safely discovered or inferred, including:

- authorization and credentials for the chosen GA4 or Looker data path;
- approval of public versus internal product surfaces and admin access;
- acceptance, rejection, or amendment of the qualifying Argus recommendation;
- repository, branch, or release ownership when no authoritative record exists;
- destructive infrastructure, credential, firewall, or public-exposure changes.

Routine implementation choices, debugging, testing, review, documentation, and non-destructive verification do not require a pause.

## Definition Of Done

The goal is complete only when all nine phase gates pass and the evidence is current. At minimum:

- the retained implementation has a clean versioned baseline and reproducible release;
- Hermes owns scheduling and execution without root intervention, orphan processes, or ownership drift;
- every public artifact belongs to one verified run and publication is atomic;
- Product Muscle covers the accepted competitor set with evidence or explicit unknowns;
- Audience Demand contains nonzero, validated, traceable data;
- Argus produces an accepted cross-plane recommendation and an auditable learning effect;
- the accepted IA is implemented with contextual Argus actions and the official design system;
- exhaustive local and live E2E suites pass across all controls, entities, roles, states, and viewports;
- the controlled Algolia pilot is monitored, recoverable, and used for at least one real team decision;
- the vault, dossier, tracker, Bible page, release record, and live deployment all agree on status.

No completion claim may be based only on code presence, test counts, a manual root run, a stale dashboard, or an unverified mockup.
