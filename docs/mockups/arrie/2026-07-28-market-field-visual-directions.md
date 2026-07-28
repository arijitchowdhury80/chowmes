# aRRIe Market Field Visual / IA Directions

Date: 2026-07-28
Status: candidate comparison for review, not approved, not implementation-ready
Related:
- `docs/plan/2026-07-28-ci-os-arrie-ux-ia-gate.md`
- `docs/mockups/arrie/2026-07-28-market-field-low-fi.md`

## Purpose

The UX gate now needs a direction decision. The old dashboard failed because it exposed data objects without a clear market story. The next direction must prove that CI-OS can reveal competitive intelligence in layers:

1. market movement
2. selected hotspot
3. Argus read
4. recommended action
5. evidence chain
6. unknowns and confidence limits

This document compares three candidate visual / IA directions before any implementation work resumes.

## Option 1: Constellation-First Intelligence Field

### Concept

The home screen is a spatial signal field. Competitors, themes, product capabilities, audience demand, recommendations, and source clusters appear as connected nodes. Hotspots form where multiple evidence planes overlap.

The user starts with the market shape, selects a hotspot, then Argus reveals the read, actions, proof, and unknowns.

### First View

```text
┌──────────────────────────────────────────────────────────────────────────────┐
│ ARGUS / CI-OS                         Algolia        Today | 7D | 30D | ▾   │
├──────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│                    MARKET FIELD                                              │
│                                                                              │
│                         ◉ AI commerce ownership                              │
│                      ╱  │  ╲                                                 │
│        Constructor ●    │    ● Coveo                                         │
│                    ╲    │   ╱                                                │
│       Audience demand ●─● Product capability                                 │
│                         │                                                    │
│       Elastic ●─────────◌ TCO / infra narrative                              │
│                                                                              │
│       Selected: AI commerce ownership                                        │
│       Movement rising | Confidence medium-high | 7D window                   │
│                                                                              │
│       Reveal: Argus read | Actions | Proof | Unknowns                        │
└──────────────────────────────────────────────────────────────────────────────┘
```

### Strengths

- Most aligned with the desired intelligence-grade, map-like, layered experience.
- Makes relationships visible before the user reads prose.
- Supports time movement through pulses, trails, and changing edge strength.
- Naturally supports click-to-reveal.
- Can become true 3D after the object model is accepted.

### Risks

- If semantics are weak, it becomes decorative.
- If too many objects are shown, it becomes unreadable.
- If the editorial read is hidden too deeply, business users may not know what to do first.

### Guardrails

- Every node type and edge type must have exactly one meaning.
- Default field shows only material hotspots, not every captured source.
- Argus read appears immediately after selecting a hotspot.
- No animation unless it explains time, movement, confidence, or evidence relationship.

### Best Use

Use this if the product should feel like a premium competitive-intelligence operating system, not a dashboard.

## Option 2: Analyst Lens With Embedded Map

### Concept

The home screen opens with an Argus editorial read on the left and a smaller market map on the right. The user gets a plain-language answer first, then uses the map to inspect why.

### First View

```text
┌──────────────────────────────────────────────────────────────────────────────┐
│ ARGUS / CI-OS                         Algolia        Today | 7D | 30D | ▾   │
├──────────────────────────────────────────┬───────────────────────────────────┤
│ TODAY'S READ                             │ MARKET FIELD                      │
│                                          │                                   │
│ AI commerce ownership is the active      │       ◉ AI commerce               │
│ competitive frame this week.             │    Constructor ●──● Coveo         │
│                                          │          ╲    │   ╱               │
│ Why it matters                           │       Demand ●─● Capability       │
│ Algolia needs sharper market language    │                                   │
│ before competitors define the category.  │ Selected hotspot updates the read │
│                                          │                                   │
│ [Actions] [Proof] [Unknowns]             │                                   │
└──────────────────────────────────────────┴───────────────────────────────────┘
```

### Strengths

- Easier for executive users to understand immediately.
- Keeps the business read visible without requiring exploration.
- Lower risk than a full-field first screen.
- Still supports map-driven inspection.

### Risks

- Can drift back into a report with a decorative side graphic.
- Less visually distinctive.
- The market map may become secondary, weakening the product's spatial intelligence idea.

### Guardrails

- The map must drive the read, not decorate it.
- Clicking any hotspot must update the editorial read, actions, and proof.
- The first read must show what changed over time, not only a static conclusion.

### Best Use

Use this if clarity beats immersion for the first release.

## Option 3: Mission Control Workbench

### Concept

The home screen is an analyst command surface with market map, recommendations, source health, queue status, and run controls visible together.

### First View

```text
┌──────────────────────────────────────────────────────────────────────────────┐
│ ARGUS / CI-OS                         Algolia        Today | 7D | 30D | ▾   │
├─────────────────────────────┬────────────────────────┬───────────────────────┤
│ MARKET MAP                  │ ACTION QUEUE           │ RUN / SOURCE HEALTH   │
│                             │                        │                       │
│ AI commerce cluster         │ PMM: sharpen narrative │ Last run published    │
│ TCO cluster                 │ Sales: update talk     │ Failed sources: 3     │
│ Product unknowns            │ Product: review gaps   │ Queue limits: 39      │
│                             │                        │                       │
├─────────────────────────────┴────────────────────────┴───────────────────────┤
│ Evidence and operator detail                                                  │
└──────────────────────────────────────────────────────────────────────────────┘
```

### Strengths

- Operator-friendly.
- Makes system health and work queue visible.
- Useful for the internal builder/admin workflow.

### Risks

- Too close to the failed dashboard mental model.
- Too much admin surface on the first screen.
- Weak for the primary business-user story.
- Likely to require training.

### Guardrails

- Should not be the default home screen.
- Belongs under Admin or Evidence Lab, not the executive/business read.

### Best Use

Use this as the operator/admin surface, not as the primary product experience.

## Recommendation

Choose **Option 1: Constellation-First Intelligence Field** as the target direction, but prototype it in two steps:

1. Low-fidelity static / 2.5D mockup to prove IA, object model, time controls, and click-to-reveal sequence.
2. High-fidelity true 3D prototype only after the IA reads clearly without motion.

This gives the product the intelligence-grade shape Arijit is asking for while avoiding the trap of building a pretty 3D visual that does not explain anything.

## What Approval Means

Approving Option 1 does not approve production implementation.

It approves the next design artifact:

- a visual low-fidelity screen mockup of the Market Field home screen
- selected hotspot state
- action layer
- proof drawer
- daily / 7D / 30D time behavior
- mobile fallback concept

After that, the high-fidelity 3D direction can be designed and reviewed.

## What Rejection Means

If Option 1 is rejected, the next step should be either:

- revise Option 1's object model and first-screen reveal behavior, or
- choose Option 2 if the first view needs to keep the editorial read visible beside the map.

Option 3 should not be chosen as the primary product home screen unless the product is being reframed as an internal operator console.

## Decision Needed

The next decision is:

> Should aRRIe proceed with Option 1, the Constellation-First Intelligence Field, as the candidate direction for the next visual mockup?

