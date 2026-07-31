# aRRIe Phase 6 UI/UX Constraints Checkpoint

Date: 2026-07-28
Status: blocked on missing local standards source before production UI rendering changes
Scope: CI-OS Product IA and cockpit UI. Hermes core remains untouched.

## Required Source Check

The `frontend-builder` workflow requires reading:

`~/Library/CloudStorage/GoogleDrive-arijit.chowdhury@algolia.com/My Drive/AI-Docs/Obsidian/ArijitOS-Brain/Standards/UIUXDesignSOP/index.md`

Current result:

- The required file path does not exist on this machine.
- A quick search under `/Users/arijitchowdhury/Library/CloudStorage` found no `UIUXDesignSOP/index.md`.
- The Algolia design-system path referenced by workspace instructions also did not exist at:
  `/Users/arijitchowdhury/Library/CloudStorage/GoogleDrive-arijit.chowdhury@gmail.com/My Drive/AI-Projects/Algolia-Design-System`

## Constraints Already Known From Approved Phase 6 Direction

These constraints are approved enough to guide tests and implementation planning, but not enough to claim formal UI/UX SOP compliance:

- The first screen must be the true 3D Market Field, not a flat text list.
- The Market Field must reveal in layers: movement, selected read, action, proof, confidence limits, and raw evidence.
- The map must be clickable, not only ambient animation.
- Pulses and links must indicate movement and concentration.
- Audience Demand is a first-class evidence plane, not competitor proof.
- Unknown product evidence must render as a confidence boundary, not absence.
- Evidence Lab and Admin remain secondary routes.
- No external CDN JavaScript is allowed in production.
- Reduced motion and mobile fallback are required.

## Production Implication

The Phase 6 guardrail slice can proceed because it is package/security validation, not visual rendering.

Production UI rendering changes should not claim final design compliance until one of these happens:

1. The missing UI/UX SOP path is restored.
2. Arijit provides the current standards source path.
3. Arijit explicitly authorizes using the Phase 6 workspace constraints as the temporary UI/UX authority for the pilot.

## Next Safe Work

Allowed without the missing SOP:

- package runtime vendoring
- package verifier checks
- CDN rejection tests
- renderer red tests that assert structure and evidence semantics
- data-contract improvements that do not alter visual styling

Hold before claiming visual/UI completion:

- final production 3D styling
- brand compliance
- live UI acceptance
- Phase 6 pass judgment
