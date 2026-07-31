# Draft Goal: aRRIe UX / IA Review And Redesign

Date: 2026-07-19
Status: draft only, not an active goal
Prepared because: the current CI-OS completion goal is blocked by failed product sense-making and user acceptance.

## Non-Activation Notice

This is not a new active goal.

Arijit has not approved execution yet. This draft exists so the goal can be reviewed, debated, revised, and activated later after the current CI-OS completion goal is cancelled or otherwise cleared.

## Working Name

aRRIe UX / IA Review And Redesign

Use the name `aRRIe` as the user-provided working label. Do not invent an expansion until Arijit defines or approves one.

## Problem Statement

The current Argus / CI-OS dashboard has data, evidence, and working mechanics, but the product does not yet explain itself. A user should not need an admin guide to understand what to read first, what matters, why Argus believes or withholds a conclusion, what action is recommended, and where to inspect proof.

If the interface cannot tell a clear visual and semantic story, additional CI-OS phase work will only add more unreadable material.

## Draft Objective

Define, prototype, validate, and document the intuitive information architecture and UX journey for Argus / CI-OS before continuing the broader CI-OS completion phases.

The output should be an approved UX / IA specification and mockup set that makes the product self-explaining for its primary operators and business users.

## Core Product Promise To Design Around

Within the first minute, the user should understand:

1. What changed in the competitive market.
2. Why it matters to Algolia.
3. Whether Argus trusts the read or is holding back.
4. What evidence supports or contradicts the read.
5. What team should do what next.
6. What remains unknown.
7. Where to inspect the underlying proof without drowning in it.

## Research And Brainstorming Sequence

1. Capture the current live UI failure modes from screenshots, live inspection, and Arijit's critique.
2. Define the primary audiences:
   - executive reader
   - PMM operator
   - Product owner
   - Sales / GTM user
   - evidence auditor / admin
3. Define each audience's first three questions.
4. Inventory all content objects currently shown or planned:
   - market movement
   - competitor activity
   - product reality
   - audience demand
   - recommendation
   - confidence
   - contradictions
   - unknowns
   - source health
   - evidence rows
   - admin controls
   - learning / feedback loop
5. Sort content into tiers:
   - Tier 1: decision story
   - Tier 2: rationale and alternatives
   - Tier 3: team action workflows
   - Tier 4: proof and audit
   - Tier 5: admin / diagnostics
6. Produce an IA map showing what belongs on the first screen, what belongs in the core journey, and what belongs behind audit or admin disclosure.
7. Produce low-fidelity mockups before implementation.
8. Debate the mockups with Arijit and revise.
9. Convert the accepted direction into a UX / IA spec.
10. Only after approval, plan frontend implementation using the required frontend-builder path and TDD.

## Candidate IA Hypothesis

The product should not be organized around available datasets. It should be organized around a decision journey:

1. Today
   - the competitive brief
   - one primary read
   - one trust state
   - one recommended next action
2. Why
   - evidence summary
   - confidence rubric
   - support and contradiction
   - unknowns
3. What To Do
   - PMM action
   - Product action
   - Sales action
   - Content / executive action if relevant
4. Market Map
   - themes
   - competitors
   - movement
   - time window
5. Product Reality
   - feature / capability comparison
   - shipped evidence
   - explicit unknowns
6. Audience Demand
   - Looker / GA4 evidence
   - demand overlap and contradiction
7. Evidence Lab
   - source rows
   - source health
   - raw ledgers
   - validation records
8. Admin
   - source onboarding
   - competitor registry
   - run controls
   - diagnostics

This hypothesis is intentionally provisional. It should be tested against Arijit's critique and actual user journeys before code is written.

## Draft Success Criteria

The future goal should pass only when:

- Arijit can look at the first screen and explain the main read, trust state, evidence basis, and next action without an admin guide.
- Every major section has a clear job and audience.
- Raw evidence and diagnostics are hidden behind proof / audit workflows rather than mixed into the executive story.
- Unknowns are explained as confidence boundaries, not blank or broken comparisons.
- The interface distinguishes:
  - fact
  - inference
  - recommendation
  - blocked recommendation
  - unknown
  - audit detail
- The product has at least one approved low-fidelity mockup before implementation.
- The product has at least one approved high-fidelity direction before implementation.
- The implementation plan includes UI journey validation, semantic validation, accessibility checks, responsive checks, and live-data E2E validation.
- The old CI-OS phase plan is updated only after this UX / IA gate is resolved.

## Non-Goals

- Do not build the production UI during brainstorming.
- Do not continue Scout, GA4 / Looker, Argus intelligence, or pilot phases during this UX / IA definition work.
- Do not create an admin guide as the substitute for clarity.
- Do not treat a passing Playwright click test as proof of usability.
- Do not use a design polish pass to compensate for broken information architecture.

## Expected Artifacts

- Current UI critique inventory.
- Audience / job-to-be-done map.
- Content object inventory.
- IA map.
- Low-fidelity wireframes.
- Revised visual story mockups.
- Accepted UX / IA spec.
- Implementation gate checklist.
- Validation plan covering UI journey, semantics, accessibility, responsive behavior, live data, and Hermes integration.

## Execution Boundary For Later

When this draft becomes an active goal, start with research and brainstorming. Do not write production code until Arijit approves the IA direction and mockups.

