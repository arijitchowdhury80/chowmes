# aRRIe Phase 6 True 3D Prototype Contract

Date: 2026-07-28
Status: contract for review mockup

## Artifact

`docs/mockups/arrie/2026-07-28-market-field-true-3d.html`

## Required Behaviors

1. Render a WebGL canvas using Three.js.
2. Place nodes in real x/y/z space.
3. Draw edges as 3D lines between nodes.
4. Animate signal pulses along evidence-backed edges.
5. Allow click selection of hotspots and connected nodes.
6. Update the Selected Movement panel from the selected object.
7. Change movement language and pulse intensity when Today, 7D, 30D, or Custom is selected.
8. Reveal proof without replacing the market story.
9. Expose Evidence Lab and Admin as secondary routes only.
10. Provide mobile layout where the field remains visible and panels stack.

## Semantic Node Set

| Node | Type | Meaning |
|---|---|---|
| Agent Studio | theme | accepted market movement |
| Algolia product proof | capability | shipped product evidence |
| Audience demand | audience_demand | Looker-derived audience response |
| Narrative gap | confidence_limit | accepted action-grade gap |
| Product Marketing action | recommendation | named-team action |
| Google Vertex AI Search | competitor | competitive context |
| Bloomreach | competitor | competitive context |
| Coveo | competitor | competitive context |
| Unknown capability cells | unknown_boundary | confidence limit |

## Acceptance Questions

The review artifact should let Arijit answer:

1. What is the main market movement?
2. Which signals connect to it?
3. What changed across time?
4. Why does it matter to Algolia?
5. What should Product Marketing do next?
6. What evidence supports this?
7. What is confidence-limiting?
8. Where do raw proof and admin controls live?

