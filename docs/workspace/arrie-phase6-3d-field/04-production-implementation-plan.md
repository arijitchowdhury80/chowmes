# aRRIe Phase 6 Production Implementation Plan

Date: 2026-07-28
Status: human direction accepted; production implementation may begin with TDD guardrails
Scope: CI-OS Product IA only. Hermes core remains untouched.

## Gate Position

Phase 6 is active, but not passed.

The true 3D prototype proved a viable direction for review. Arijit accepted the true 3D constellation direction on 2026-07-28.

Production work must begin with the dependency/package guardrail slice before renderer changes.

## Implementation Thesis

The live CI-OS product should open with Argus Read as a 3D Market Field:

1. The user sees the market movement first.
2. The selected hotspot reveals one Argus read.
3. The read exposes action, confidence, proof, and unknowns.
4. The rest of the product is organized around drilldown workflows, not raw data sections.

The accepted Phase 5 Agent Studio recommendation is the first production story:

> Turn the shipped Agent Studio capability into an evidence-backed market narrative before the demand window cools.

## Production Navigation Contract

| Route | Job | First production requirement |
|---|---|---|
| Argus Read | Start with the selected 3D Market Field hotspot and one decision. | Show Agent Studio movement with product proof, Audience Demand, narrative gap, confidence limits, and Product Marketing action. |
| Product Muscle Matrix | Inspect product reality behind the selected hotspot. | Filter by selected capability/theme and preserve unknown cells as confidence boundaries. |
| Conversation Heatmap | Show market narrative intensity and movement. | Show theme intensity, competitor contribution, freshness, and whether conversation supports or contradicts the hotspot. |
| Demand Lens | Show Algolia audience response. | Show Agent Studio demand, time window, export provenance, overlap with product/conversation evidence, and coverage limits. |
| Pattern Board | Explain why Argus believes the pattern exists. | Show support, contradiction, disproof criteria, and confidence scoring. |
| Actions | Make recommendations usable by named teams. | Show PMM, Product, Sales, Content, and Exec action rows tied to selected movement and proof. |
| Competitor Registry | Keep market actors inspectable and onboardable. | Preserve selected competitor/partner context across drilldowns and expose first-sweep status. |
| Evidence Lab | Audit proof, raw rows, failed checks, and rejected evidence. | Keep raw evidence subordinate to proof drawers and audits. |
| Argus Command / Admin | Run controls, source health, publish health, and learning controls. | Separate operator state from the business read. |

## Technical Architecture

Implementation lives in `/Users/arijitchowdhury/Dropbox/AI-Development/CI-OS`.

### 1. Market Field State

Add or extend dashboard view-model objects:

- `MarketFieldState`
- `MarketFieldNode`
- `MarketFieldEdge`
- `MarketFieldHotspot`
- `MarketFieldAction`
- `MarketFieldProofItem`
- `MarketFieldTimeWindow`

State must be generated from existing backend evidence:

- `product_market_run_intelligence`
- `argus_recommendations`
- `pattern_observations`
- `product_events`
- `conversation_themes`
- `demand_signals`
- feature comparison rows
- source/evidence references
- learning-policy and recommendation acceptance artifacts

No UI-only claims are allowed.

### 2. 3D Runtime

The review mockup uses Three.js from a CDN. Production must not.

Production options:

1. **Preferred:** vendor an audited, pinned Three.js module inside the CI-OS package, for example `src/cios/dashboard/static/vendor/three.module.min.js`, and include its license and checksum.
2. **Fallback:** implement a smaller package-owned WebGL renderer if dependency review rejects Three.js.

No external CDN dependency is acceptable for the controlled pilot.

### 3. Renderer

Modify `src/cios/dashboard/cockpit_renderer.py` to render:

- local 3D runtime asset
- serialized Market Field state JSON
- canvas + label layer
- selected movement panel
- time controls
- action layer
- proof drawer
- Evidence Lab / Admin route boundaries
- reduced-motion fallback
- mobile focused-field layout

The renderer must preserve the current self-contained publication model and public safety scanning.

### 4. Route / Workflow Composition

The 3D Market Field is the first screen, but Phase 6 cannot stop there.

Each production navigation item must have a route or section with:

- selected-context handoff
- empty/degraded state
- evidence/proof route
- keyboard-accessible controls
- no dead buttons
- no unexplained metrics

### 5. Persistence And Context

Selection state should be represented in URL hash or query state:

- selected hotspot
- selected competitor or partner
- selected time window
- selected proof drawer state

Repeated Argus commands update bounded state; they must not append an endless transcript.

## TDD Plan

### Slice 1: State Contract

Red tests:

- `tests/dashboard/test_market_field_view_model.py`
- unknown cells render as `unknown_boundary`, never absence
- Agent Studio accepted recommendation becomes the selected default hotspot
- evidence URLs and confidence limits attach to proof items
- time windows exist and have semantic labels

Green work:

- add Pydantic state models
- build Market Field state from dashboard state inputs

### Slice 2: Renderer Contract

Red tests:

- `tests/dashboard/test_cockpit_renderer.py`
- first screen contains `#market-field-3d`
- selected movement panel carries Agent Studio action
- proof drawer contains product proof, Audience Demand, Argus inference, confidence limit
- Evidence Lab and Admin are secondary routes
- unknown boundary copy is visible

Green work:

- render canvas, serialized state, panels, controls, proof drawer
- include local 3D runtime asset only after dependency decision

### Slice 3: Interaction Contract

Red tests:

- extend `scripts/validate_dashboard_clicks.py`
- canvas renders nonblank
- hotspot or label selection updates panel
- Today / 7D / 30D / Custom updates movement text
- proof drawer opens
- Evidence/Admin boundaries work
- mobile has no clipped labels

Green work:

- add browser automation for local and live routes
- add reduced-motion and mobile state handling

### Slice 4: Workflow Routes

Red tests:

- PMM journey reaches recommendation, proof, and action
- Product journey reaches Product Muscle Matrix and unknown cells
- Sales journey reaches competitor context and talk-track action
- Evidence Auditor journey reaches proof chain and raw source references
- Admin journey reaches source/run controls without polluting Argus Read

Green work:

- implement route/section handoffs
- keep selected context persistent

### Slice 5: Live Package Validation

Red tests:

- package contract fails if 3D asset missing
- public safety fails on external CDN references
- launch validation fails if visible numbers lack source fields
- live click validation fails if public dashboard drops proof/action/context

Green work:

- update package verifier
- update public safety scan
- deploy through CI-OS package path
- verify live public state

## Security And Reliability Checks

Required before deployment:

- no Hermes core edits
- no public CDN runtime dependency
- vendored dependency checksum recorded
- no secret/path leakage in public JSON/HTML
- no admin controls exposed as primary business UI
- accessibility labels for all controls
- reduced-motion path
- mobile layout tested at 390px
- rollback bundle preserved

## Phase 6 Acceptance Checklist

Phase 6 can pass only when:

1. Arijit accepts the true 3D constellation direction.
2. Production CI-OS implements all nine navigation jobs above.
3. The live UI answers the Phase 6 acceptance questions without explanation.
4. PMM, Product, Sales, Admin, and Evidence Auditor journeys pass against live data.
5. Product Muscle, Conversation, Demand, Pattern, Action, Registry, Evidence, and Admin routes all preserve selected context.
6. Every visible number and claim traces to current evidence.
7. Unknown, stale, blocked, failed, quiet, and confidence-limited states are visibly distinct.
8. Live validation passes on desktop, tablet, and mobile.
9. Status docs, tracker, and dossier are updated only after verified gate evidence.

## Explicit Non-Goals

- Do not start Phase 7 E2E certification before Phase 6 passes.
- Do not release the Algolia pilot before Phase 7 passes.
- Do not modify Hermes core.
- Do not make recurring GA4 automation a Phase 6 blocker.
- Do not let production UI fabricate missing competitor, demand, or product evidence.

## Review Decision Needed

Arijit needs to decide whether the validated true 3D Market Field prototype is the accepted Product IA direction.

If accepted, the next implementation slice is Slice 1: state contract and tests in the CI-OS package.
