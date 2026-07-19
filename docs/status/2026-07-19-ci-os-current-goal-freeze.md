# CI-OS Current Goal Freeze

Date: 2026-07-19
Status: frozen for cancellation and later resume
Owner: Arijit Chowdhury
Runtime boundary: Hermes remains the runtime OS; CI-OS remains a separately versioned extension; Hermes core is not authorized for modification.

## Why This Freeze Exists

The active CI-OS completion goal is being paused and recorded because the current Argus / CI-OS dashboard is not self-explaining enough for real use. The visible product does not yet tell a coherent story without training, an admin guide, or prior knowledge of the data model.

Arijit's decision on 2026-07-19:

- Do not create a new goal yet.
- First research, brainstorm, debate, and define the right UX / IA goal.
- Record the current goal state to disk so the active goal can be cancelled without losing context.
- Later create a new aRRIe UX / IA goal from the draft plan.
- Do not continue normal CI-OS phases until the UX / IA problem is explicitly addressed.

This file is the resume handoff for the current goal.

## Active Goal Being Frozen

Tool-reported objective:

> Complete Phases 0 through 8 of the approved CI-OS completion plan and release a controlled, monitored Algolia pilot. The finished system must combine current product evidence, competitor conversation, Algolia audience demand, and Argus reasoning into source-backed, confidence-scored recommendations that named business teams can use. Hermes remains the runtime OS. CI-OS remains a separately versioned extension. This goal does not authorize changes to Hermes core.

Tool-reported status at freeze time: `blocked`

Source charter:

- `docs/goals/2026-07-13-complete-ci-os-algolia-pilot.md`
- `docs/plan/2026-07-13-ci-os-completion-plan.md`
- `docs/status/2026-07-13-ci-os-project-dossier.md`

The original goal's definition of done still requires all phase gates, accepted IA, exhaustive E2E validation, a versioned release, monitoring, rollback, and evidence that real users can make repeatable trusted decisions.

## Current Repository State

Local CI-OS worktree:

- Path: `/Users/arijitchowdhury/Dropbox/AI-Development/Personal/ChowMes/.worktrees/ci-os-phase1-runtime`
- Branch: `codex/ci-os-phase1-runtime`
- Remote branch: `origin/codex/ci-os-phase1-runtime`
- Remote repository: `arijitchowdhury80/algolia-competitive-intelligence`
- Current pushed head: `72294bc Fix Argus cockpit semantic read`

Dirty local files initially observed at freeze time:

- `scripts/validate_dashboard_clicks.py`
- `src/cios/dashboard/cockpit_renderer.py`
- `tests/dashboard/test_cockpit_renderer.py`

Dirty diff size at freeze time:

- 3 files changed
- 260 insertions
- 31 deletions

These local modifications are the uncommitted interim IA patch that tried to make the live page more story-led. They have not been committed or pushed after `72294bc`.

Verification correction during freeze:

The CI-OS worktree then presented those same files as deleted, with Dropbox-style conflicted copies beside them:

- `scripts/validate_dashboard_clicks (ATL-M3P-AC2's conflicted copy 2026-07-19).py`
- `src/cios/dashboard/cockpit_renderer (ATL-M3P-AC2's conflicted copy 2026-07-19).py`
- `tests/dashboard/test_cockpit_renderer (ATL-M3P-AC2's conflicted copy 2026-07-19).py`

`git diff --stat` in the CI-OS worktree showed:

- 3 tracked files deleted
- 8,115 deletions

This looks like a cloud-sync conflict, not a deliberate source-control decision. Before any future coding resumes, the next operator must reconcile this worktree state or create a clean replacement worktree from `origin/codex/ci-os-phase1-runtime`. Do not treat the conflicted filenames as normal source paths.

## What Has Been Done

Phase 0 baseline work established a controlled source and runtime direction:

- CI-OS source-of-truth directory was identified as `/Users/arijitchowdhury/Dropbox/AI-Development/CI-OS`.
- GitHub source-of-truth was identified as `arijitchowdhury80/algolia-competitive-intelligence`.
- CI-OS remained separate from Hermes core.
- The working branch and remote were reconciled for auditable work.

Phase 1 runtime ownership work established dedicated production execution:

- Production execution was moved toward the `cios` application user rather than root or admin-user execution.
- Hermes remained the scheduler / queue owner.
- CI-OS application execution was bounded through the cgroup-safe runner.
- Earlier evidence recorded two consecutive healthy scheduled runs as required by the Phase 1 gate.

Phase 2 publication and run-bound work advanced substantially:

- Run-bound publication machinery exists.
- Package and publication integrity checks are part of the deploy path.
- Cgroup-safe deployment through `/opt/cios/app/deploy/cios-daily.sh` has completed successfully.
- Latest recorded package / publish run from the interim IA patch:
  - Run id: `cios-20260719T070800Z-2705150`
  - Queue result: `0`
  - Package verdict: `pass`
  - Publication integrity: `pass`
  - Public HTML fetch confirmed the interim story labels existed.

UX / IA emergency patch, not accepted as final product design:

- Previous raw labels such as `Product-market memory`, `Argus run reads`, `Theme heat map`, `Window deltas`, `Entity velocity`, and `Holistic daily coverage` were removed or reframed.
- The dashboard gained story-oriented concepts such as:
  - `What to do with this brief`
  - `Action gate`
  - `Why Argus is holding back`
  - `Open proof detail`
- The patch was mechanically verified and deployed, but it does not have human acceptance.

## Verified Evidence Captured Before Freeze

Local tests after the interim IA patch:

- Command: `python3 -m pytest tests/dashboard/test_cockpit_renderer.py tests/scripts/test_validate_dashboard_clicks_dependencies.py -q`
- Result: `38 passed`

Local Playwright / dashboard validation after the interim IA patch:

- Structure passed.
- Navigation targets passed.
- Timeline checks passed.
- Semantic layer checks passed.
- Priority selection checks passed.
- Brief routing checks passed.
- Appendices checks passed.
- Responsive viewport checks passed for 390, 768, and 1280 widths.

Live deploy after the interim IA patch:

- Cgroup-safe deploy completed with run id `cios-20260719T070800Z-2705150`.
- Publication integrity passed.
- Live HTML fetch confirmed the interim story labels.

Important limitation:

These checks prove rendering mechanics, deploy mechanics, and selected click paths. They do not prove that the product is understandable, useful, or accepted by Arijit. The actual user acceptance result is failed / blocked.

## Where The Goal Is Stuck

The blocker is not SSH, runtime ownership, deploy plumbing, or test count.

The blocker is product sense-making:

- The page still reads as data and diagnostics rather than a guided competitive intelligence story.
- The user cannot tell what to pay attention to first.
- Section labels and ordering do not yet express a clear mental model.
- Raw evidence, diagnostics, market data, recommendations, confidence, and audit material are not tiered correctly.
- The product still risks requiring an admin guide, which fails the intended standard.
- The semantic layer is incomplete or at least not visible enough in the interface.

Proceeding into later CI-OS phases before fixing this would compound the wrong product shape.

## Do Not Do Next

Do not resume feature work as if the active phase plan is healthy.

Specifically, do not start or continue:

- Scout / Product Muscle expansion
- GA4 / Looker demand expansion
- Argus intelligence recommendation expansion
- Production UI feature buildout
- Pilot launch validation
- Release / pilot packaging

Those should remain blocked until the aRRIe UX / IA goal is drafted, approved, and executed.

Do not revert or discard the uncommitted interim IA patch unless Arijit explicitly asks. It is deployed live and dirty locally, so it must be treated as a known interim state.

## Resume Plan For The Old Goal

If this original CI-OS completion goal is resumed later:

1. Start from this freeze file.
2. Inspect the CI-OS worktree before editing.
3. Resolve the deleted-file / conflicted-copy state or create a clean replacement worktree.
4. Decide explicitly whether to keep, replace, or revert the uncommitted interim IA patch.
5. Reconcile live deployed state against branch `codex/ci-os-phase1-runtime`.
6. Confirm the current public page at `https://ci.chowmes.com/`.
7. Confirm the current package / publication run state on Chowmes.
8. Resume only after the UX / IA acceptance gate is no longer blocking.
9. Continue with the documented phase gates from the original goal.

## Draft Replacement Goal Pointer

The proposed future goal is not active yet.

Draft artifact:

- `docs/goals/drafts/2026-07-19-ci-os-arrie-ux-ia-goal-draft.md`

Purpose:

- Research, debate, and design the self-explaining aRRIe UX / IA before any further CI-OS phase work.
