# aRRIe Market Field Design Thinking

Date: 2026-07-28
Status: design checkpoint for review mockup, not production implementation

## 1. Mental Model

The user is not carrying a dashboard mental model anymore. The rejected live UI proved that cards, labels, and tables can show a lot of data while failing to communicate intelligence.

The intended mental model is a competitive-intelligence field: a spatial read of where the market is concentrating, which actors are connected, and which movement deserves attention.

What the user expects:

- an immediate sense of market shape
- visible hotspots
- click-to-reveal interpretation
- evidence behind claims
- confidence boundaries
- time movement

What would confuse them:

- raw data labels as primary navigation
- a heatmap that is secretly a text list
- 3D visuals with no semantic meaning
- source health or run diagnostics on the home screen
- actions that are not tied to a selected market movement

## 2. Information Architecture Tiers

| Element | Tier | Treatment |
|---|---|---|
| Market Field | Hero | Dominant spatial area, first thing the eye reads |
| Selected hotspot | Primary | Clear active state with name, movement, window, confidence |
| Time controls | Primary | Persistent controls because time changes meaning |
| Selected Movement panel | Primary | Appears immediately beside selected hotspot |
| Actions | Primary | Revealed from selected movement, not generic cards |
| Proof Drawer | Secondary | Always reachable, not first-screen clutter |
| Unknowns / confidence limits | Secondary | Visible in selected read and proof layer |
| Secondary hotspots | Secondary | Visible but lower emphasis |
| Evidence Lab route | Supporting | Available, not dominant |
| Admin route | Supporting | Available, not dominant |

Tier inflation risk: making every node look important. Mitigation: only one selected hotspot receives full brightness, pulse, and interpretation.

## 3. Interaction Flow

Common actions:

1. Select a market hotspot.
2. Open actions for the selected movement.
3. Open proof for the selected recommendation.

Happy path:

1. User lands on Market Field.
2. Primary hotspot is preselected.
3. User sees movement, confidence, and time window.
4. User opens Argus read.
5. User opens actions.
6. User opens proof drawer.
7. User changes from 7D to 30D and sees the read update.

Empty state:

- Show monitored market field with no material hotspots and explain what was checked.

Loading state:

- Show field skeleton and run timestamp, not fake insight.

Error state:

- Keep last verified read visible and show which evidence plane failed.

## 4. Cognitive Load Budget

Visible chunks on first screen:

1. Top rail and time controls.
2. Market Field.
3. Selected hotspot state.
4. Selected Movement preview.
5. Reveal controls.

Budget: 5 chunks.

Reduction strategy:

- proof rows hidden in drawer
- admin hidden in route
- source health hidden in Evidence Lab
- recommendations revealed from selected movement

## 5. Emotional Journey

Landing:

- feeling: orientation
- carried by: spatial field and visible hotspot

Selection:

- feeling: recognition
- carried by: selected node, pulse, and readable movement summary

Action:

- feeling: decision confidence
- carried by: team-specific action with why-now and confidence state

Proof:

- feeling: trust and control
- carried by: evidence chain and unknown boundaries

## 6. Design Pre-Mortem

Tigers:

- Looks like generic AI network graph.
  - Mitigation: strict node and edge semantics, restrained motion, no decorative particles.
- Information overload.
  - Mitigation: one selected hotspot, two or three secondary hotspots, proof hidden by default.
- 3D becomes unreadable.
  - Mitigation: this first artifact is static / lightly interactive 2.5D, not production 3D.
- Mobile graph becomes tangled.
  - Mitigation: focused mini-field plus stacked reveal sections.
- Users miss the action.
  - Mitigation: selected movement always has an action reveal.

Elephants:

- The direction might still be too abstract.
  - Mitigation: include concrete Algolia/competitor labels and plain-language Argus read.
- The reference inspiration may tempt imitation.
  - Mitigation: adapt the interaction idea only; competitive-intelligence semantics must drive every visual choice.

## Aesthetic Choice

Chosen aesthetic: custom intelligence-field direction.

Reason:

- `theme-dashboard` risks repeating the rejected dashboard failure.
- `report-designer` risks returning to a static brief.
- `theme-enterprise` risks feeling too corporate and flat.
- The product needs a distinctive spatial intelligence surface.

Token direction:

- Deep field background: `#090A0F`
- Signal ink: `#F4F0E6`
- Algolia blue: `#0A4CFF`
- Demand cyan: `#48D7E8`
- Product amber: `#D9A84E`
- Confidence warning: `#F26D5B`
- Quiet graphite: `#242833`

Typography direction:

- Display: Charter / Georgia style for Argus read only.
- UI/data: Inter / system sans.
- Data labels: IBM Plex Mono / SFMono where available.

Signature:

- A semantic constellation where edge treatment and pulsing encode evidence plane, time, and confidence.

## UIUX SOP Constraint Check

The configured SOP path did not resolve in this workspace:

`~/Library/CloudStorage/GoogleDrive-arijitchowdhury@algolia.com/My Drive/AI-Docs/Obsidian/ArijitOS-Brain/Standards/UIUXDesignSOP/index.md`

Applied local constraints instead:

- no production code
- no live-data connection
- no Hermes changes
- no raw proof rows on first screen
- mobile fallback required
- keyboard-visible controls in the static mockup
- text must fit at 375px, 768px, 1024px, and 1280px

