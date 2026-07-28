# aRRIe Phase 6 3D Runtime Dependency Review

Date: 2026-07-28
Status: reviewed and accepted as the first production guardrail slice
Scope: CI-OS Product IA only. Hermes core remains untouched.

## Purpose

This note records the runtime and package constraints for turning the validated true 3D Market Field prototype into production CI-OS UI after the human IA direction gate passes.

The prototype proved the interaction model locally, but it used a CDN import for Three.js. That is acceptable for a throwaway review artifact only. The controlled Algolia pilot cannot rely on public CDN JavaScript.

## Current CI-OS State

Audited local package: `/Users/arijitchowdhury/Dropbox/AI-Development/CI-OS`
Branch: `codex/ci-os-phase0-baseline`

Findings:

- The current public cockpit renderer is intentionally self-contained. `src/cios/dashboard/cockpit_renderer.py` documents that no external JS is loaded.
- Existing dashboard tests already assert no external script or stylesheet for the HTML renderer.
- The current production Market Field is semantic HTML with positioned nodes, not a WebGL or Three.js scene.
- The dashboard view model already has the core graph contract: nodes, edges, hotspots, actions, proof items, selected hotspot, and time windows.
- `scripts/validate_dashboard_clicks.py` already checks Market Field sections, hotspot selection, time controls, proof drawer, Evidence Lab, and Admin route boundaries.
- `scripts/verify_hermes_package_contract.py` does not yet require a 3D runtime asset or reject CDN references as a package invariant.
- No existing Three.js, WebGL runtime, or vendored 3D dependency was found in the CI-OS package surface inspected for Phase 6.

Conclusion: the semantic data layer is ahead of the rendering layer. Production work should extend rendering and verification without changing Hermes core.

## Reviewed Candidate

Package: `three`
Prototype version: `0.160.0`
Latest npm version checked on 2026-07-28: `0.185.1`

Review command:

```bash
npm view three@0.160.0 version license dist.integrity dist.tarball --json
npm view three version license dist.integrity dist.tarball --json
npm pack three@0.160.0 --pack-destination /tmp/cios-three-review
```

Reviewed metadata for `three@0.160.0`:

- license: `MIT`
- npm integrity: `sha512-DLU8lc0zNIPkM7rH5/e1Ks1Z8tWCGRq6g8mPowdDJpw1CFBJMU7UoJjC6PefXW7z//SSl0b2+GCw14LB+uDhng==`
- npm tarball: `https://registry.npmjs.org/three/-/three-0.160.0.tgz`
- tarball sha256: `1ee2f935c4f555814b388e87b5ef78a44856bd2e9d0feb88643a6e193fb42856`
- tarball license file size: `1081` bytes
- `package/build/three.module.min.js` size: `670681` bytes
- `package/build/three.module.min.js` sha256: `3e690ac7d180b0aadf0891bea39eec643e29e2d3e75c99b18689518665f69ba6`

## Dependency Decision

Preferred pilot strategy:

1. Do not float to latest for the pilot.
2. Pin the production pilot to the same reviewed version used by the prototype unless a separate upgrade review is approved.
3. Vendor only the minimum required runtime asset, likely `three.module.min.js`, inside the CI-OS package.
4. Store the MIT license and checksum beside the vendored asset.
5. Load the runtime from the CI-OS package/public artifact path only.

Suggested production paths:

- `src/cios/dashboard/static/vendor/three/0.160.0/three.module.min.js`
- `src/cios/dashboard/static/vendor/three/0.160.0/LICENSE`
- `src/cios/dashboard/static/vendor/three/0.160.0/CHECKSUMS.txt`

Rejected for the controlled pilot:

- `https://unpkg.com/three/...`
- `https://cdn.jsdelivr.net/...`
- `https://esm.sh/...`
- any public CDN or dynamic module resolver
- a floating `latest` dependency

Fallback if the dependency is rejected:

- Build a smaller package-owned WebGL renderer for nodes, edges, pulses, labels, and click hit zones.
- Keep the same Market Field state contract so the IA and evidence model remain stable.

## Required Production Guardrails

Before production implementation can pass Phase 6:

- `verify_hermes_package_contract.py` must require the vendored 3D runtime, license, and checksum when the 3D Market Field is enabled.
- A public safety scan must fail on external JavaScript hosts including `unpkg.com`, `cdn.jsdelivr.net`, `esm.sh`, `skypack.dev`, and raw GitHub asset hosts.
- Renderer tests must assert no `<script src="https://...">` or dynamic remote import.
- Playwright validation must include a canvas pixel check, label clipping check, hotspot click check, time-window check, proof-drawer check, and reduced-motion fallback check.
- Live validation must run against `https://ci.chowmes.com/` after deployment.
- Rollback must preserve the previous self-contained HTML Market Field.

## Phase 6 Position

This review does not pass Phase 6 by itself.

Arijit accepted the true 3D constellation Market Field as the Product IA spine on 2026-07-28.

The first production slice is now a TDD implementation of the vendored runtime contract and the 3D Market Field shell, followed by live browser validation before any broader UI routes are rewritten.
