# aRRIe Market Field Candidate UX / IA Spec

Date: 2026-07-28
Status: approved by Arijit for implementation planning, not implementation-ready
Primary artifact: `docs/mockups/arrie/2026-07-28-market-field-option-1.html`

## Scope

This spec defines the approved UX / IA direction for the CI-OS / Argus first-read experience.

It does not authorize production UI implementation, CI-OS runtime changes, Hermes changes, live data wiring, or pilot release work without the next implementation plan and phase gates.

## Product Decision Being Proposed

Use **Market Field first** as the default CI-OS / Argus home experience.

The user should land on a spatial competitive-intelligence field, not a static report, dashboard grid, source ledger, or admin workbench.

The first screen should answer:

> Where is the competitive market concentrating, which hotspot matters now, and what does Argus think Algolia should do?

## Accepted If Approved

If Arijit approves this direction, the following become the implementation target for the next planning phase:

1. The home screen opens with a dominant Market Field.
2. The Market Field shows selected market movement through a constellation of competitors, themes, product proof, Audience Demand, and unknown boundaries.
3. The default interaction is click-to-reveal.
4. Selecting a hotspot reveals:
   - Argus read
   - movement direction
   - time window
   - confidence state
   - named team actions
   - proof drawer
   - unknowns / confidence limits
5. Evidence and Admin remain secondary routes, not first-screen content.
6. Mobile uses a focused mini-field plus stacked disclosure sections instead of a tiny full constellation.
7. Time controls are part of the semantic read: Today, 7D, 30D, and Custom must change the movement interpretation.

## Explicit Non-Decisions

Approval of this candidate spec would not decide:

1. Final visual design system.
2. Final 3D engine or whether production uses true 3D.
3. Final data schema changes.
4. Final recommendation-ranking logic.
5. Final Product Muscle completion strategy.
6. Pilot readiness.
7. Public deployment.

Those require separate implementation plans and phase gates.

## Required Screen Model

```text
Market Field
├── selected hotspot
│   ├── Selected Movement
│   ├── Action Layer
│   ├── Proof Drawer
│   └── Unknowns / Confidence Limits
├── Evidence Lab
└── Admin
```

## Required Object Semantics

Every visual object must map to a durable CI-OS object.

| Visual object | Required meaning |
|---|---|
| Competitor node | monitored competitor such as Constructor, Coveo, Bloomreach, Elastic |
| Partner node | monitored ecosystem actor such as Shopify |
| Theme node | market narrative or strategic pattern |
| Capability node | product proof / feature capability cluster |
| Audience Demand node | Algolia audience response signal |
| Unknown Boundary node | explicit confidence limit, not a product absence claim |
| Edge | evidence-backed relationship between two nodes |
| Pulse / trail | new or changing movement in selected time window |

## Required Interaction Semantics

| Interaction | Required behavior |
|---|---|
| Select hotspot | update Selected Movement read |
| Select time window | update movement language and urgency |
| Open actions | show named team actions tied to selected movement |
| Open proof drawer | reveal evidence chain without raw-row flood |
| Navigate Evidence | inspect raw evidence, source health, failed checks, confidence detail |
| Navigate Admin | inspect run controls, registry, publish health, operator diagnostics |

## Required Content Semantics

The UI must distinguish:

- fact
- inference
- recommendation
- blocked recommendation
- unknown
- confidence limit
- raw evidence
- admin / operational state

The UI must not show unknown product proof as either:

- confirmed absence
- broken comparison
- empty UI

## First Implementation Acceptance Questions

A future implemented version can pass the UX gate only if a user can answer these from the live UI without an admin guide:

1. What is the dominant market hotspot?
2. Which competitors or partners connect to it?
3. What changed in the selected window?
4. Why does this matter to Algolia?
5. What does Argus recommend?
6. Which team owns the next action?
7. What evidence supports the recommendation?
8. What evidence is missing or confidence-limiting?
9. How do I switch from Today to 7D, 30D, or Custom?
10. Where do I inspect raw proof?
11. Where do I manage sources, runs, and diagnostics?

## Validation Requirements For Future Build

The implementation plan must include:

1. Unit tests for Market Field view-model generation.
2. Semantic tests proving unknowns are not rendered as absences.
3. E2E tests for hotspot selection, time-window change, action reveal, proof drawer, Evidence route, and Admin route.
4. Responsive validation at 390px, 768px, 1024px, and 1280px.
5. Accessibility checks for keyboard selection, focus states, labels, contrast, and touch targets.
6. Live-data validation against a current CI-OS run.
7. Hermes integration validation proving CI-OS remains an extension and does not modify Hermes core.
8. Human acceptance against the first-read questions above.

## Current Review Evidence

Validated review artifacts:

- `docs/mockups/arrie/2026-07-28-market-field-option-1.html`
- `docs/mockups/arrie/screenshots/2026-07-28-market-field-option-1-desktop.png`
- `docs/mockups/arrie/screenshots/2026-07-28-market-field-option-1-mobile.png`
- `docs/workspace/arrie-market-field/02-visual-validation.md`

Current validation result:

- desktop and mobile screenshots render
- embedded JavaScript parses
- no live runtime hooks are present
- mockup remains standalone
- mobile route rail is tight at 390px and should be refined in high-fidelity design

## Approval Record

Arijit approved the Market Field-first UX / IA direction on 2026-07-28.

The next artifact is an implementation plan for the accepted UX / IA, not direct production coding.
