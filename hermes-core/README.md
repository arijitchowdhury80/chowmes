# Hermes Core Boundary

This directory is the repository boundary for Hermes core.

CI-OS business logic must not live here. CI-OS must integrate with Hermes
through stable extension seams: cron scripts, skills, agent profiles, channel
delivery, model routing, configuration, and package entrypoints.

Rules:

- No CI-OS competitors, sources, dashboard, report, or intelligence logic in
  Hermes core.
- No one-off patches to Hermes core to make CI-OS work.
- If Hermes core needs a new generic capability, open a separate Hermes-core
  workstream with its own spec, tests, release notes, and validation.
- Core changes must be generic to Hermes, not specific to Algolia, Argus, or
  CI-OS.
- CI-OS can depend on documented Hermes interfaces, not private implementation
  details.

Current state:

- This ChowMes repository is not vendoring Hermes core source code here.
- Runtime configuration changes, such as cron timeout values, are operational
  configuration and must be documented separately from CI-OS package logic.
- The CI-OS package boundary lives in `../ci-os/`.
