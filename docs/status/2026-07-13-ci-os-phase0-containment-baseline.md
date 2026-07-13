# CI-OS Phase 0 Containment Baseline

Date: 2026-07-13
Status: Phase 0 active, source-control blocker cleared, deployed-release mapping still incomplete
Goal: Complete the CI-OS Algolia pilot through the approved phase-gated plan.

## Boundary

This artifact records the current Phase 0 baseline only. No CI-OS business
logic was changed, no generated files were deleted, no user changes were
reverted, and no server state was modified. The CI-OS package repo changes made
during this continuation were source-control hygiene, commit separation,
development-loop bootstrap, and publication of the Phase 0 branch/tags to the
user-confirmed package remote.

Hermes remains the runtime OS. CI-OS remains a separately versioned extension.
This baseline does not authorize Hermes core changes.

## Local Repositories

### ChowMes coordination repo

- Path: `/Users/arijitchowdhury/Dropbox/AI-Development/Personal/ChowMes`
- Branch: `codex/hermes-resource-intake`
- HEAD: `1951342c6509fd724584565447e9e61f5a919efa`
- Upstream: `origin/codex/hermes-resource-intake`
- Ahead/behind: `+1 -0`
- Tracked changes outside this artifact before this update: 2 files,
  `CHOW_TRACKING.md` and `README.md`
- Untracked source-control candidates: 62, pre-existing coordination/mockup
  artifacts

ChowMes currently holds the coordination artifacts, public status docs, mockup
lock, and CI-OS extension-boundary manifest. It is not the package source.

### CI-OS package repo

- Path: `/Users/arijitchowdhury/Dropbox/AI-Development/CI-OS`
- Branch: `codex/ci-os-phase0-baseline`
- HEAD: `13731acc5d875a09ba736adcf411ca3c604e4f69`
- Base before Phase 0 hygiene: `453849cb0bd4a7d59799e8deb3f76e41173d1fe6`
- Git remote: `origin`
  `https://github.com/arijitchowdhury80/algolia-competitive-intelligence.git`
- Authoritative Phase 0 source branch:
  `origin/codex/ci-os-phase0-baseline` ->
  `13731acc5d875a09ba736adcf411ca3c604e4f69`
- Phase 0 local commit series:
  - `b5787b1 chore: quarantine generated artifacts`
  - `a87b4e0 chore: bootstrap development-loop state`
  - `9da3fa1 feat(db): add CI-OS evidence repositories`
  - `eb2c601 feat(intelligence): add product muscle extraction`
  - `e0e56ff feat(intelligence): add audience demand intake`
  - `da7d1d2 feat(intelligence): add Argus reasoning loop`
  - `533ed03 feat(admin): add CI-OS operator dashboard`
  - `7091273 feat(deploy): add Hermes CI-OS runtime gates`
  - `13731ac docs: record CI-OS recovery plan`
- Local tags:
  - `ci-os-pre-phase0-recovery-2026-07-13` -> `453849c`
  - `ci-os-phase0-clean-baseline-2026-07-13` -> `13731ac`
- Published tags:
  - `ci-os-pre-phase0-recovery-2026-07-13` ->
    `453849cb0bd4a7d59799e8deb3f76e41173d1fe6`
  - `ci-os-phase0-clean-baseline-2026-07-13` ->
    `13731acc5d875a09ba736adcf411ca3c604e4f69`
- Remaining tracked changes after commit series: 0
- Untracked source-control candidates after commit series: 0
- Clean source archive checksum from `git archive --format=tar HEAD`:
  `77621f7a81bc0f77c263e23a7e06cc06126ba5149741383fc57baa1202f9dd5d`
- Tracked file count: 474

The CI-OS repo now has a clean published review branch and reviewable commit
series. The repository ownership blocker is resolved by the user-confirmed
GitHub repository. The remaining Phase 0 question is narrower: whether the
currently deployed `/root/.hermes/apps/cios` package can be mapped to this
commit or to a reproducible release bundle beyond sampled checksum parity.

Development-loop project state now exists under `.development-loop/project/`
and points back to the approved CI-OS completion plan rather than creating a
parallel roadmap.

## CI-OS Dirty Tree Inventory

### Retained work by committed domain

- Source-control hygiene and development-loop bootstrap.
- Schema and repositories.
- Product Muscle and Scout-backed product-surface extraction.
- Audience demand intake and GA4/manual import readiness.
- Argus reasoning, product-market synthesis, and learning loop.
- Local-only admin and public dashboard state/render/publish surfaces.
- Hermes runtime wrapper, package contract, and launch readiness gates.
- Recovery plan, dossier, workspace status, and validation documentation.

### Original tracked modified files by domain

- Source: `src/cios/brain`, `src/cios/collect`, `src/cios/dashboard`,
  `src/cios/db`, `src/cios/learn`, and
  `src/cios/platform/models/providers/claude_cli.py`.
- Scripts: `scripts/daily_production_run.py`,
  `scripts/rerender_dashboard.py`.
- Config and packaging: `config/tenants-sources.yaml`, `pyproject.toml`,
  `deploy/claude-shim/shim.py`, `AGENTS.md`.
- Docs: `docs/planning/CI-OS-data-model-spec.md`,
  `docs/workspace/ci-os-dashboard-app/_status.md`.
- Tests: modified tests across brain, collect, dashboard, db, integration,
  learn, platform, and daily-run scripts.
- Machine metadata: tracked `.DS_Store` files under `tests/`,
  `tests/brain/`, and `tests/dashboard/` were removed from Git's tracked source
  set in commit `b5787b1`; the local files remain on disk and are ignored.

### Untracked candidates by top-level domain

```text
deploy 2
docs 30
scripts 34
src 42
tests 73
```

### Untracked candidates by extension

```text
py 148
md 30
sh 1
service 1
[none] 1
```

Generated local runtime artifacts under `out/` and the empty
`product_market_summary` file are now ignored. They remain on disk for evidence
if needed, but no longer appear as source-control candidates.

## Retain Versus Quarantine

### Retain as likely source or review evidence

- Extension/runtime boundary: `deploy/cios-daily.sh`,
  `deploy/cios-admin.service`, package contract scripts, daily wrapper tests.
- Schema and repositories: product-market, product-surface, run-stage repos,
  schema changes, and related db tests.
- Collection and Product Muscle: Scout adapter/exporter, product-surface
  planner/runner, gap discovery, capability and feature-matrix modules,
  product-muscle scripts and tests.
- Audience demand plumbing: GA4 exporter, demand imports, demand sources,
  demand intake, demand quality, import/refresh scripts, work-order export
  scripts, and tests.
- Intelligence and learning: market movement, decision read, product-market
  synthesis, recommendation challenge, learning apply/audit modules, and
  tests.
- Admin and dashboard: local-only admin app, dashboard refresh, operator
  handoff, data-plane manifest, feature comparison, cockpit/state/publisher
  changes, click validation, launch readiness, and tests.
- Planning records that explain accepted recovery direction:
  `docs/plan/2026-07-13-ci-os-completion-plan.md`,
  `docs/plan/e2e-validation.md`,
  `docs/workspace/2026-07-13-ci-os-project-dossier.md`, and current workspace
  status files.

### Quarantine from source commits unless intentionally preserved

- Generated status artifacts under `out/status-check/`.
- Empty generated file `product_market_summary`.
- Local and server `.DS_Store` files.
- Pytest caches, virtualenv contents, AppleDouble `._*` files, and other local
  machine metadata.
- Old run logs should be preserved only as evidence attachments, not mixed into
  source commits.

### UI iteration status

The accepted screen direction is the locked Argus mockup recorded in ChowMes:

- `docs/mockups/LOCKED.md`
- `docs/mockups/locked/ci-os-argus-locked-2026-07-10.html`
- `docs/mockups/locked/ci-os-argus-locked-2026-07-10.png`

Other dashboard/admin design notes in the CI-OS repo are useful as rationale
and status history, but they are not proof that the accepted IA is implemented.
They should not unlock Phase 6 or UI build work.

## Verification Run

### Local CI-OS checks

Command:

```bash
git diff --check
```

Result: passed with no output.

Command:

```bash
python3 -m pytest
```

Result:

```text
1180 passed, 1 skipped, 23 deselected in 21.70s
```

The local suite is green against the clean branch. This does not prove the live
Hermes path, publication contract, product evidence freshness, or UI acceptance.

### Local checksum anchors

```text
c220ff66286f8c5dba3c40145bd01d1f8e87255c1cd48757060976af25ea869d  pyproject.toml
93caf18b790f9c67789237a5a93443f69700a947ef6822babd1f15d10ea55ed9  scripts/daily_production_run.py
e381f3cb10adc1b8e1861f7cabc5c8ab752307f74836d4f17e8b45b1e66f4d4b  scripts/check_e2e_launch_readiness.py
1202f3365c5ad50bd0c6030986809801c408de2f55ce641543fad2e2f27d5984  src/cios/dashboard/state_builder.py
810ba4929433d818d8d14273340a9c60718cf9c354c2e7084ee5821bc3406f6a  src/cios/db/schema.sql
```

## Deployed Baseline

Read-only VPS inspection through the ChowMes SSH helper connected to host
`chowmes` at `2026-07-13T12:17:57Z`.

### Paths

- Present: `/root/.hermes/apps/cios`
- Missing: `/opt/data/apps/cios`
- Present: `/root/.hermes/scripts/cios-daily.sh`
- Missing: `/opt/data/scripts/cios-daily.sh`
- Present: `/root/.hermes/apps/algolia-competitive-intelligence/apps/dashboard/public`
- Missing: `/opt/data/apps/algolia-competitive-intelligence/apps/dashboard/public`

### Package identity

- Live app path: `/root/.hermes/apps/cios`
- Live package version in `pyproject.toml`: `0.1.0`
- Live app Git metadata: none found
- Latest visible backup markers:
  - `cios-app-20260712T040534Z-data-plane-manifest`
  - `cios-app-20260712T041926Z-admin-data-plane`
  - `cios-app-20260712T043044Z-ga4-fast-lane`
  - `cios-app-20260712T043815Z-ga4-rolling-window`

Sampled live checksums match the clean local branch checksums for:

- `pyproject.toml`
- `scripts/daily_production_run.py`
- `scripts/check_e2e_launch_readiness.py`
- `scripts/verify_hermes_package_contract.py`
- `src/cios/dashboard/state_builder.py`
- `src/cios/db/schema.sql`
- `src/cios/intelligence/runner.py`
- `src/cios/admin/app.py`
- `deploy/cios-daily.sh`

This proves sampled file parity, not a complete reproducible release. The
deployed package still cannot be fully mapped to a commit because the app
directory has no Git metadata and no release manifest on the host. The package
source of truth is now authoritative, but the deployed directory itself is not
yet a clean release bundle.

### Ownership and metadata concerns

The deployed tree contains root-owned files and local machine metadata:

- `/root/.hermes/apps/cios` reported `UNKNOWN:root`.
- `/root/.hermes/apps/algolia-competitive-intelligence/.../argus-latest-run-status.json`
  reported `root:root`.
- The app root contains `.DS_Store` and AppleDouble `._*` files owned by UID
  `501`, plus mixed ownership across app files and directories.

This confirms Phase 1's ownership problem remains relevant. It also means the
deployed package is not yet a clean release bundle.

### Public status

Current deployed public status fields:

```text
status='blocked_on_evidence'
publish_status='blocked'
generated_at='2026-07-13T01:51:21.937836Z'
public_dashboard_updated=False
next_hermes_action='configure_ga4_or_upload_demand_export'
```

Current deployed semantic dashboard fields:

```text
generated_at='2026-07-13T01:51:16.684183Z'
demand_signals=[]
```

The system is correctly blocked on inward demand, but publication remains
non-final because the release and ownership baseline are not clean.

## Phase 0 Gate Evaluation

Gate: one clean, reviewable branch represents the retained CI-OS
implementation, and no unknown untracked source files remain.

Result: not passed yet.

Source-control subgate: passed.

- The retained CI-OS implementation is clean locally.
- The retained branch is published to the user-confirmed authoritative remote.
- The pre-recovery and clean-baseline tags are published to the same remote.
- Remote ref verification on 2026-07-13 returned the expected commit IDs:
  - `refs/heads/codex/ci-os-phase0-baseline` ->
    `13731acc5d875a09ba736adcf411ca3c604e4f69`
  - `refs/tags/ci-os-phase0-clean-baseline-2026-07-13` ->
    `13731acc5d875a09ba736adcf411ca3c604e4f69`
  - `refs/tags/ci-os-pre-phase0-recovery-2026-07-13` ->
    `453849cb0bd4a7d59799e8deb3f76e41173d1fe6`

Blocking facts:

1. The deployed app has no Git metadata, mixed ownership, local machine
   metadata, and only sampled checksum parity with the clean published branch.
2. No release manifest currently exists on the host that maps
   `/root/.hermes/apps/cios` to the published branch, tag, or source archive
   checksum.
3. Generated output and local metadata are ignored and no longer pollute Git
   status.

### Latest release-record attempt

At `2026-07-13T13:36:05Z`, a read-only attempt to inspect the VPS app tree for
full tracked-file parity did not reach the host:

```text
ssh: connect to host 72.61.72.147 port 22: Operation timed out
ssh_diagnose_tcp_status=timeout
ssh_diagnose_tcp_errno=EAGAIN
```

No server state was changed. Phase 0 remains blocked on creating or verifying a
deployed release record once SSH reachability returns.

## Next Phase 0 Work Only

Do not begin Phase 1 yet.

Next containment slice:

1. Create a deployed release record that maps `/root/.hermes/apps/cios` to the
   authoritative commit/tag/archive checksum.
2. Only then re-evaluate the Phase 0 gate for advancement to Phase 1.
