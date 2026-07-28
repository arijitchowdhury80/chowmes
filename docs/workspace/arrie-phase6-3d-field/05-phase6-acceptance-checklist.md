# aRRIe Phase 6 Acceptance Checklist

Date: 2026-07-28
Status: human direction accepted; production implementation pending verification

## Human Direction Gate

- [x] Arijit accepts the true 3D constellation Market Field as the Product IA spine.
- [ ] Arijit rejects it and requests a revised direction.
- [ ] Arijit accepts it with amendments recorded in this workspace.

Only one of the above can be true. Acceptance recorded from Arijit's 2026-07-28 approval.

## Business-User Comprehension Gate

Five representative users must be able to answer without a builder explanation:

- [ ] What is the main market movement?
- [ ] Which competitors, partners, product proof, and demand signals connect to it?
- [ ] What changed in Today / 7D / 30D / Custom views?
- [ ] Why does this matter to Algolia?
- [ ] What does Argus recommend?
- [ ] Which named team owns the next action?
- [ ] What evidence supports the recommendation?
- [ ] What is unknown, stale, blocked, or confidence-limiting?
- [ ] Where do they inspect raw proof?
- [ ] Where do they manage sources, runs, and diagnostics?

## Navigation Gate

- [ ] Argus Read is the first screen.
- [ ] Product Muscle Matrix is inspectable by capability, product area, competitor, and evidence date.
- [ ] Conversation Heatmap shows theme intensity, movement, commonality, and competitor contribution.
- [ ] Demand Lens shows audience response and overlap/contradiction with market and product themes.
- [ ] Pattern Board explains support, contradiction, confidence, and disproof criteria.
- [ ] Actions are usable by PMM, Product, Sales, Content, and executives.
- [ ] Competitor Registry supports onboarding through first sweep.
- [ ] Evidence Lab owns raw proof, source health, failed checks, and rejected evidence.
- [ ] Argus Command/Admin owns runs, registry operations, publication health, and learning controls.

## Evidence And Semantics Gate

- [ ] Every visible number traces to a current-run field.
- [ ] Every visible claim traces to evidence.
- [ ] Unknown product evidence never renders as absence.
- [ ] Demand is labeled Audience Demand, not competitor proof.
- [ ] Confidence limits are visible in the selected read and proof drawer.
- [ ] Contradictions are visible when present.
- [ ] Blocked actions explain what Argus needs before recommending.

## Interaction Gate

- [x] Hotspot selection updates the read, actions, proof, and context.
- [x] Time-window selection updates bounded Market Field state.
- [x] Proof drawer opens without replacing the market story.
- [ ] Evidence and Admin routes are reachable but secondary.
- [ ] Selected competitor/partner context persists across dependent views.
- [ ] Repeated Argus commands update bounded state rather than appending endless chat.

## Accessibility And Responsive Gate

- [ ] Keyboard users can reach time controls, hotspot labels, proof, Evidence, and Admin.
- [ ] Focus states are visible.
- [ ] Controls have accessible names.
- [ ] Color is not the only state indicator.
- [ ] Reduced-motion mode keeps the field understandable.
- [x] 390px mobile layout has no clipped critical Market Field selectors in the reusable Agent Studio verifier artifact.
- [x] 768px tablet layout preserves the read and proof path in the reusable Agent Studio verifier artifact.
- [x] 1280px+ desktop layout preserves the market field as the primary visual in the reusable Agent Studio verifier artifact.

## Operational Gate

- [ ] CI-OS remains a separately versioned Hermes extension.
- [ ] Hermes core is not modified.
- [ ] Public production HTML/JS contains no external CDN dependency.
- [x] Any vendored 3D runtime has license and checksum recorded.
- [x] Package verifier checks required 3D/runtime assets and reusable Market Field validation scripts.
- [x] Public safety scan rejects secret, local path, private artifact leakage, and forbidden external runtime hosts for the reusable Agent Studio artifact.
- [x] Deployment mechanics use the CI-OS package path, stage before publish, redact internal filesystem references before scan, scan before publish, refresh public-store `served`, and preserve rollback pointers locally.
- [x] Public redaction gate removes private paths and `file://` references from staged public artifacts while still allowing the safety scanner to block secret-like values.
- [x] Live dashboard click validation passes.

## Gate Judgment

Phase 6 status remains `active` until every required item above is verified and recorded, or the remaining design-authority/comprehension gaps are explicitly narrowed or waived for the controlled pilot.
