# aRRIe Option 1 Visual Mockup Brief

Date: 2026-07-28
Status: review brief for the next visual mockup, not approved, not implementation-ready
Direction: Option 1, Constellation-First Intelligence Field
Related:
- `docs/plan/2026-07-28-ci-os-arrie-ux-ia-gate.md`
- `docs/mockups/arrie/2026-07-28-market-field-low-fi.md`
- `docs/mockups/arrie/2026-07-28-market-field-visual-directions.md`

## Purpose

This brief defines the next visual mockup to create if the Constellation-First Intelligence Field remains the preferred direction.

It does not approve production implementation. It defines what the mockup must prove before any implementation plan can resume.

## Mockup Goal

Show that CI-OS can open with a spatial market story that is understandable without an admin guide.

The first screen must communicate:

1. The market has hotspots, not just rows.
2. Hotspots are formed by relationships between competitors, product capabilities, market conversation, and Audience Demand.
3. A user can click one hotspot and immediately understand what changed, why it matters, what to do, and what proof exists.
4. Unknowns are confidence boundaries, not broken UI.
5. Time is part of the read, not a decorative filter.

## Visual Tone

The mockup should feel:

- premium
- intelligence-grade
- spatial
- layered
- inspectable
- calm enough for business use
- distinct from generic SaaS analytics dashboards
- distinct from Algolia marketing pages

The mockup should not feel:

- corporate dashboard
- flat table-first BI
- decorative sci-fi
- generic network graph
- source-health admin console
- marketing landing page

## First View Composition

```text
┌──────────────────────────────────────────────────────────────────────────────┐
│ Argus / CI-OS                 Algolia                  Today | 7D | 30D | ▾ │
├──────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│                          MARKET FIELD                                        │
│                                                                              │
│          faint historical trail                                              │
│                    · · ·                                                     │
│                       ◉ AI commerce ownership                                │
│                    ╱  │  ╲                                                   │
│       Constructor ●   │   ● Coveo                                            │
│                  ╲    │    ╲                                                 │
│    Audience demand ●──● Product capability cluster                           │
│                       │                                                      │
│                       ◌ Unknown capability boundary                          │
│                                                                              │
│       Elastic ●────────◌ TCO / infra narrative                               │
│                                                                              │
│       Shopify ◌────────◌ Partner ecosystem watch                             │
│                                                                              │
│  Selection chip: AI commerce ownership                                       │
│  Movement: rising | Window: 7D | Confidence: medium-high | Proof: partial    │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

## Required First-Screen Elements

1. Top bar:
   - Argus / CI-OS identity
   - tenant selector fixed to Algolia for pilot
   - time controls: Today, 7D, 30D, custom
   - clear route to Evidence Lab and Admin without making them primary

2. Market field:
   - a dominant spatial area
   - no card-grid homepage
   - no raw source table
   - no generic scorecard row

3. Hotspots:
   - one primary selected hotspot
   - two or three secondary hotspots
   - quiet or weak areas visible but visually subordinate

4. Selection state:
   - selected hotspot name
   - movement direction
   - time window
   - confidence
   - proof completeness

5. Immediate reveal affordance:
   - Argus read
   - Actions
   - Proof
   - Unknowns

## Node Object Model

The first mockup should include these node classes.

| Node class | Example | Visual role |
|---|---|---|
| Competitor | Constructor, Coveo, Bloomreach, Elastic | named market actors |
| Partner | Shopify | ecosystem actor |
| Theme | AI commerce ownership, TCO narrative | market narrative |
| Capability | product capability cluster | shipped product proof |
| Audience Demand | agentic shopping demand | Algolia audience response |
| Unknown Boundary | unverified capability cells | confidence limit |

Recommendations should not be free-floating nodes in the first mockup. They should be revealed after selecting a hotspot. If recommendations appear in the field too early, the map will become conceptually crowded.

Source clusters should not be first-class nodes in the home mockup. Sources belong in the Proof Drawer and Evidence Lab.

## Edge Object Model

| Edge class | Meaning | Visual treatment |
|---|---|---|
| claims | competitor is talking about a theme | thin solid line |
| ships | competitor has product proof for capability | thicker solid line |
| overlaps demand | audience demand overlaps theme | luminous line |
| limits confidence | unknown weakens conclusion | dotted or warning line |
| influences action | selected pattern supports recommendation | only visible in Action layer |

## Time Behavior

The mockup should show at least two time states.

### Today

Purpose: operating read.

Expected behavior:

- only new or still-material movement pulses
- selected hotspot may be smaller but fresher
- actions emphasize immediate operating next step
- quiet areas stay visible but do not dominate

### 7D

Purpose: weekly pattern formation.

Expected behavior:

- trails show how the hotspot formed
- edge strength reflects repeated signals across the week
- Argus read explains formation, not just today's event
- actions can be stronger because pattern evidence has accumulated

### 30D

Purpose: strategic movement.

Expected behavior:

- clusters reveal whether a movement is durable or just noisy
- weak one-day bursts fade
- competitor positioning patterns become clearer
- actions become strategic rather than immediate

## Interaction Sequence

The visual mockup should demonstrate this path.

```text
Landing
-> select AI commerce ownership hotspot
-> Selected Movement panel opens
-> Show Actions
-> Open Proof Drawer
-> Change 7D to 30D
-> Market Field and Selected Movement update
```

## Selected Movement Panel

The selected panel should appear beside or below the field, depending on viewport.

It must include:

- selected hotspot name
- one-sentence Argus read
- what changed
- who drove it
- why it matters to Algolia
- confidence state
- proof completeness
- unknown / blocked areas

It must not include:

- raw rows
- full source-health logs
- a long essay
- decorative metrics with no implication

## Action Layer

Actions should appear only after the selected movement is known.

Each action needs:

- team owner
- priority
- action verb
- why now
- evidence basis
- confidence / limitation

Example actions:

```text
PMM      P1  sharpen AI commerce positioning
Sales    P1  prepare Constructor / Coveo objection talk track
Product  P2  review unknown capability cells before treating gaps as real
```

## Proof Drawer

The Proof Drawer should be an inspectable layer, not a page takeover.

It must show:

- recommendation
- evidence chain
- source references
- product proof
- conversation proof
- Audience Demand proof
- contradictions
- unknowns
- confidence limits

It should provide links to Evidence Lab for raw inspection.

## Mobile Fallback

The mobile mockup should not attempt to show the full constellation as a tiny tangled graph.

Recommended mobile behavior:

1. Show the selected primary hotspot as a focused mini-field.
2. Show secondary hotspots as a horizontal orbit / strip.
3. Reveal Selected Movement immediately below.
4. Actions and Proof Drawer become stacked disclosure sections.
5. Evidence Lab and Admin remain separate routes.

Mobile must still answer:

- what moved
- who drove it
- why it matters
- what to do
- what proof exists
- what is unknown

## Mockup Acceptance Criteria

The next visual mockup passes only if a reviewer can answer these from the screen:

1. What is the dominant hotspot?
2. Why is it a hotspot?
3. Which competitors or partners connect to it?
4. Which evidence planes support it?
5. What changed in the selected time window?
6. What does Argus think it means?
7. What should Algolia do next?
8. What is unknown or confidence-limiting?
9. Where is proof?
10. Where are admin controls?

If the reviewer has to ask what the map means, the mockup fails.

## Recommended Next Artifact

Create one visual mockup file for review:

- `docs/mockups/arrie/2026-07-28-market-field-option-1.html`

The file should be static or lightly interactive only. It should not connect to live data, CI-OS source, Hermes, or the production dashboard.

The goal of the next artifact is product interpretation, not engineering validation.

