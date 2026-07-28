# aRRIe Market Field Visual Validation

Date: 2026-07-28
Status: review mockup visually rendered, not approved

## Artifact Validated

- `docs/mockups/arrie/2026-07-28-market-field-option-1.html`

## Render Evidence

Rendered with local Chrome headless from the standalone file URL.

Desktop screenshot:

- `docs/mockups/arrie/screenshots/2026-07-28-market-field-option-1-desktop.png`
- Size: 1440 x 1100

Mobile screenshot:

- `docs/mockups/arrie/screenshots/2026-07-28-market-field-option-1-mobile.png`
- Size: 390 x 1100

## Mechanical Checks

- HTML parsed with Python `HTMLParser`.
- Embedded JavaScript extracted and checked with `node --check`.
- Search found no `fetch`, `XMLHttpRequest`, `/api/`, `ci.chowmes.com`, or other live runtime hooks.
- The artifact remains standalone review HTML.

## Visual Findings

Desktop:

- Market Field is visible as the dominant first-screen surface.
- Selected Movement, actions, and proof drawer affordance are visible without opening raw evidence rows.
- Secondary Evidence and Admin routes are present but subordinate.
- The headline no longer directly collides with the selected hotspot.

Mobile:

- The mobile view now behaves as a focused mini-field rather than a cropped desktop constellation.
- The selected movement title wraps correctly.
- Secondary nodes are reduced in mobile to keep the first viewport legible.
- Admin remains available, but the route rail is tight at 390px and should be refined in the next higher-fidelity pass.

## Gate Judgment

This passes as a review mockup artifact.

It does not pass the UX / IA gate by itself. Arijit still needs to accept, reject, or revise the Market Field-first direction before production UI implementation resumes.

