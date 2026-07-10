# Hermes Resource Intake

This folder versions the first layer of the Hermes enhancement program for
Chowmes: the security and inventory gate for external Hermes resources.

It does not install or modify live Hermes runtime behavior. It provides the
local operator controls that must run before external skills, memory providers,
MCP integrations, self-evolution systems, or artifact tools are allowed to
touch Athena, Argus, Telegram, gateway config, or runtime memory.

## Contents

- `docs/hermes-resource-adoption-plan.md`: seven-phase adoption plan.
- `docs/hermes-external-resource-ledger.md`: source, license, decision, and gate ledger.
- `docs/hermes-resource-threat-model.md`: trust boundary and hard stops.
- `docs/hermes-skill-intake-checklist.md`: approval checklist for skills/plugins.
- `scripts/hermes-resource-scan`: Medusa-oriented resource scan wrapper.
- `scripts/hermes-inventory-scan`: Bumblebee-oriented inventory scan wrapper.
- `tests/test_hermes_resource_intake.py`: regression tests for the first-layer gate.

## Local Tooling

Scanner binaries are intentionally local and ignored by git:

- `.tools/medusa-venv`
- `.tools/bin/bumblebee`

Private reports are ignored by git:

- `.artifacts/hermes-resource-intake/`
- `.medusa/`

## Verification

```sh
python3 -m py_compile \
  hermes-core/resource-intake/scripts/hermes-resource-scan \
  hermes-core/resource-intake/scripts/hermes-inventory-scan \
  hermes-core/resource-intake/tests/test_hermes_resource_intake.py

python3 -m pytest hermes-core/resource-intake/tests/test_hermes_resource_intake.py -q
```
