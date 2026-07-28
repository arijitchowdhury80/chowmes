# aRRIe Phase 6 True 3D Market Field Design Thinking

Date: 2026-07-28
Status: design record for review prototype

## 1. Mental Model

The intended mental model is a competitive-intelligence constellation: a 3D knowledge graph where market movement is seen before it is explained. The user starts with a signal concentration, selects it, then reveals the Argus read, action, proof, and confidence limits.

The earlier flat graph direction was not enough. The user explicitly asked for a 3D constellation linked knowledge graph inspired by a second-brain build, adapted to competitive intelligence rather than copied.

## 2. Information Architecture Tiers

| Element | Tier | Treatment |
|---|---|---|
| 3D Market Field canvas | Hero | Full-height, primary spatial object |
| Selected Agent Studio hotspot | Primary | Bright selected cluster with connected planes |
| Selected Movement read | Primary | Compact panel tied to the selected hotspot |
| Named-team action | Primary | One immediate Product Marketing action |
| Time controls | Primary | Today, 7D, 30D, Custom alter motion and read |
| Proof drawer | Secondary | Reveals evidence chain and limits on demand |
| Secondary nodes | Secondary | Competitors, capabilities, demand, unknowns around the hotspot |
| Evidence Lab / Admin routes | Supporting | Present but not dominant |

## 3. Interaction Flow

Common actions:

1. Select a hotspot or connected node.
2. Switch the time window.
3. Open proof.

Happy path:

1. User lands on the 3D Market Field.
2. Agent Studio hotspot is selected by default.
3. Pulses travel between product proof, Audience Demand, market conversation, and the recommendation.
4. User changes from 7D to 30D and sees the story become more strategic.
5. User opens proof and sees evidence, unknowns, and confidence limits.

Empty state:

- No material hotspot: render a quiet field with checked planes and blocked-action explanation.

Loading state:

- Render a stable field shell with no fake insight.

Error state:

- Preserve the last verified read and mark the failed plane.

## 4. Cognitive Load Budget

Visible chunks:

1. Top rail / time controls.
2. 3D field.
3. Selected Movement panel.
4. Action strip.
5. Proof drawer toggle.

Budget: 5 chunks. Raw evidence remains hidden until proof is opened.

## 5. Emotional Journey

Landing should feel like orientation, not inspection.

Selection should feel like understanding: the constellation has a center and the center has a read.

Action should feel usable: one named team can act without reading the whole evidence store.

Proof should feel controlled: the user can audit the chain without drowning in rows.

## 6. Design Pre-Mortem

Risk: 3D becomes decorative.
Mitigation: every node, edge, color, pulse, and ring has a defined semantic meaning.

Risk: the first screen becomes another data dump.
Mitigation: show one selected hotspot and subordinate surrounding context.

Risk: motion confuses.
Mitigation: pulse only along evidence-backed relationships; reduce motion freezes animation.

Risk: mobile graph becomes unusable.
Mitigation: camera zooms toward selected hotspot and panels stack below.

## Aesthetic Choice

Chosen aesthetic: custom intelligence field.

Palette:

- Deep graphite: `#07080C`
- Iron plane: `#141820`
- Bone text: `#F3EFE4`
- Algolia blue: `#0A4CFF`
- Demand cyan: `#37D8E8`
- Product amber: `#D8A642`
- Confidence red: `#F06449`
- Proof green: `#77D489`

Typography:

- Display: Georgia for the Argus read only.
- UI: Inter / system sans.
- Data labels: SFMono / IBM Plex Mono fallback.

Signature:

- A true WebGL constellation where evidence pulses travel through the selected market story.

## UIUX SOP Constraint Check

The configured SOP path was unavailable locally:

`~/Library/CloudStorage/GoogleDrive-arijitchowdhury@algolia.com/My Drive/AI-Docs/Obsidian/ArijitOS-Brain/Standards/UIUXDesignSOP/index.md`

Fallback constraints applied from project rules and the prior aRRIe gate:

- no production code
- no Hermes core changes
- no raw proof rows on first screen
- true 3D canvas for the primary visual
- click-to-reveal as the main interaction
- time controls are semantic, not decorative
- keyboard-accessible controls
- responsive checks at desktop and mobile widths
- text must not overlap controls or panels
- unknowns remain confidence limits, not absent capabilities

