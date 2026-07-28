# CI-OS aRRIe UX / IA Gate

Date: 2026-07-28
Status: active blocker definition, not approved implementation
Scope: CI-OS / Argus product experience only. Hermes remains the runtime OS and is not modified by this gate.

## Why This Gate Exists

The current CI-OS completion goal cannot honestly advance to later Product Muscle, Argus intelligence, production UI, pilot, or release phases while the user-facing product still fails the self-explaining UX / IA standard.

The dashboard has working data paths and verified click mechanics, but that is not enough. The product must tell a coherent competitive-intelligence story without an admin guide.

This artifact supersedes the assumption that the 2026-07-10 locked mockup is still accepted as the final implementation reference. That mockup remains historical evidence, not the current acceptance target.

## Current Gate Judgment

The UX / IA is not finalized.

The mockup set is not approved.

The production dashboard is not accepted as the final CI-OS product experience.

Normal CI-OS phase execution remains gated until this artifact produces an approved IA contract and mockup direction.

## Decisions Already Made

These points are treated as accepted direction unless Arijit revises them.

1. The product must be organized around a user decision journey, not around backend datasets.
2. The primary product spine should follow option A from the brainstorm: the business-user read and product sense-making journey.
3. Admin, run controls, cgroup/runtime details, source-health operations, and registry maintenance belong in a secondary operator surface.
4. Raw rows, citations, evidence chains, failed checks, and audit material belong inside proof drawers or an Evidence Lab, not in the first-read experience.
5. The interaction model should be click-to-reveal: the user starts from a high-level market read and drills into why, evidence, confidence, and action.
6. The experience needs a time dimension. The user must be able to understand daily, weekly, monthly, and custom-window movement, not only a static today page.
7. Audience Demand is the correct renamed frame for Looker / GA data. It is audience response, not competitor proof.
8. Unknown product capabilities must be shown as confidence boundaries, not as broken comparisons or quiet claims.
9. The visual language should not feel like a generic SaaS dashboard, an Algolia marketing page, or a flat table-first analytics screen.
10. The product needs to feel intelligence-grade: spatial, layered, premium, inspectable, and opinionated.

## Decisions Not Yet Finalized

These are still open and must be resolved before implementation resumes.

1. First screen sequence:
   - Option 1: Brief first, then Market Map.
   - Option 2: Market Map first, then Action / Editorial Read.
   - Current leaning: the experience may open with the market map if it can immediately tell the high-level story instead of becoming another visual data dump.
2. Market Map form:
   - It must not collapse into a text list.
   - It should probably become a spatial intelligence map or constellation-style signal graph, inspired by the referenced 3D second-brain interaction, but adapted for competitive movement rather than copied blindly.
3. 3D versus 2.5D:
   - True 3D may create a premium intelligence feel and reveal relationships.
   - It also risks becoming decorative or hard to read unless every node, edge, pulse, cluster, and camera move has semantic meaning.
4. Default time grain:
   - Daily view is needed for operating rhythm.
   - Weekly and monthly views are needed for pattern recognition.
   - The default should likely be "current market movement" with toggles for Today, 7D, 30D, and custom.
5. Editorial read placement:
   - It may sit beside the selected market pattern.
   - It may come after the map as the "Argus interpretation" layer.
   - It must not become a long static article before the user sees the market shape.
6. Action placement:
   - Actions should be revealed from the selected pattern or read.
   - They should not appear as generic PMM / Sales / Product cards unless they are tied to a named market movement and evidence chain.
7. Evidence density:
   - The first screen needs proof signals and trust state.
   - It should not show raw source rows until the user asks to inspect proof.

## Proposed Product Story Spine

The next mockup should test this sequence.

1. Market Field
   - A spatial view of competitors, partners, themes, capabilities, and demand signals.
   - Hotspots show where attention, product movement, and demand overlap.
   - Color and intensity encode confidence, movement, and urgency.
   - Pulses or trails encode time movement.
   - Clicking a hotspot selects the story.

2. Selected Movement
   - Plain-language Argus read for the selected hotspot.
   - What changed, who moved, why it matters, and whether Argus trusts the read.
   - Shows the time window and change direction.

3. Decision Layer
   - Recommended action by named team: PMM, Product, Sales, Content, Exec.
   - Each action has owner, urgency, why now, evidence basis, and confidence.
   - Blocked actions explain what Argus needs before recommending.

4. Proof Drawer
   - Evidence chain from recommendation back to claims, source events, product proof, conversation proof, and audience demand.
   - Contradictions and unknowns are visible here.
   - Raw rows stay inspectable but subordinate.

5. Evidence Lab / Admin
   - Source health, failed extraction, registry, run controls, publish checks, and operator diagnostics.
   - This is not the executive story.

## Market Field Semantic Contract

The market visualization is allowed to be visually ambitious only if the semantics are strict.

Each node must represent exactly one durable object type:

- competitor
- partner
- market theme
- product capability
- audience demand topic
- recommendation
- source cluster

Each edge must represent exactly one relationship type:

- competitor claims theme
- competitor ships capability
- Algolia has matching / missing / unknown capability
- audience demand overlaps theme
- recommendation depends on evidence
- confidence limited by missing proof

Each visual treatment must have one meaning:

- size: materiality or total signal weight
- brightness: freshness
- color: lens or status
- pulse: new movement in selected time window
- edge thickness: strength of evidence-backed relationship
- dotted edge: inferred or weak relationship
- warning ring: confidence limitation
- halo / cluster: market hotspot

No animation is allowed unless it clarifies time, flow, selection, confidence, or evidence relationship.

## Required Mockups Before Build Resumes

1. Low-fidelity IA map:
   - screens
   - primary flow
   - drilldown layers
   - what is hidden by default
2. Market Field interaction mockup:
   - static first, then interactive
   - must show nodes, edges, hotspots, selected state, and time controls
3. Selected Movement panel:
   - shows the editorial read generated from a selected hotspot
   - must distinguish fact, inference, recommendation, unknown, and blocked action
4. Proof Drawer:
   - shows the evidence chain without overwhelming the first view
5. Evidence Lab / Admin split:
   - confirms diagnostics and source controls are not polluting the business read
6. Mobile state:
   - the market view cannot become unusable on mobile

## Acceptance Test

Arijit should be able to open the first screen and answer these without builder explanation:

1. What is the main market movement?
2. Which competitors or partners are driving it?
3. What changed over the selected time window?
4. Why does it matter to Algolia?
5. What should a named team do next?
6. What evidence supports the read?
7. What is unknown or confidence-limiting?
8. How do I drill into proof without losing the story?
9. How do I change from today to 7D, 30D, or custom?
10. Where do admin / source-health controls live?

If these cannot be answered from the mockup, the UX / IA gate fails.

## Immediate Next Work

The next safe work item is not backend phase execution. It is a mockup sequence:

1. Produce a low-fidelity IA flow for the Market Field -> Selected Movement -> Action -> Proof Drawer journey.
2. Produce a static high-fidelity direction for the 3D / constellation-inspired Market Field.
3. Validate with Arijit whether the direction feels like intelligence-grade market sense-making rather than a dashboard.
4. Only after approval, convert the accepted direction into an implementation plan and frontend validation contract.

