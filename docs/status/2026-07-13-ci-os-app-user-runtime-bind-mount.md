# CI-OS app-user runtime bind-mount repair

Date: 2026-07-13

## Decision

CI-OS host execution must not run as `root` or `chowmesadmin`.

Hermes remains the scheduler/runtime OS. CI-OS now runs from host-side app-user paths:

- Hermes cron wrapper: `/root/.hermes/scripts/cios-daily.sh`, owned `cios:hermes`, mode `750`.
- CI-OS app runtime mount: `/opt/cios/app`, bind-mounted from `/root/.hermes/apps/cios`.
- CI-OS public runtime mount: `/opt/cios/public`, bind-mounted from `/root/.hermes/apps/algolia-competitive-intelligence/apps/dashboard/public`.
- Host-readable CI-OS env copy: `/etc/cios-env`, owned `cios:hermes`, mode `640`.
- CI-OS admin service: `cios:cios`.
- CI-OS runner service: `cios:cios`, supplementary group `hermes`.
- CI-OS Claude shim: `cios-shim:cios-shim`, supplementary group `hermes`.

This avoids depending on `/root/.hermes` traversal for app-user execution. Hermes may keep or restore its private home permissions without breaking CI-OS.

## Source commits

Repository: `arijitchowdhury80/algolia-competitive-intelligence`

- `02598f6` - Add CI-OS host ownership preflight.
- `18d8862` - Use app-owned CI-OS product workdir.
- `efd89d0` - Fix CI-OS cron wrapper ownership.
- `8876fff` - Use ACL traversal for CI-OS app user.
- `1d19dd2` - Grant shim app user Hermes traversal.
- `5776891` - Run CI-OS services from opt bind mounts.
- `12b97ae` - Use host-readable CI-OS env for services.

Current deployed source archive checksum:

```text
d622742058c6960a8c5e82462f76302cb9d47bebe9ac8c00ba53f1eb81f17e15  /private/tmp/cios-12b97ae-source.tar
```

Remote deployment backup:

```text
/root/.hermes/backups/cios-opt-bind-20260713T234117Z
```

## Verification

Local source verification:

```text
python3 -m pytest tests/scripts/test_verify_hermes_package_contract.py tests/deploy/test_cios_daily_wrapper.py -q
79 passed

python3 -m pytest -q
1196 passed, 1 skipped, 23 deselected

python3 scripts/verify_hermes_package_contract.py --app-dir . --skip-python-imports
PASS: CI-OS Hermes package contract satisfied
```

Live host verification:

```text
/opt/cios/app     bind mount from /root/.hermes/apps/cios
/opt/cios/public  bind mount from /root/.hermes/apps/algolia-competitive-intelligence/apps/dashboard/public
/etc/cios-env     640 cios:hermes
/opt/cios/app     2775 cios:hermes
/opt/cios/app/out 2775 cios:hermes
/opt/cios/app/tmp/product-market 2775 cios:hermes
/opt/cios/public  2775 cios:hermes
/root/.hermes/scripts/cios-daily.sh 750 cios:hermes
```

Live services:

```text
cios-admin.service        active, User=cios, Group=cios
cios-claude-shim.service  active, User=cios-shim, Group=cios-shim, SupplementaryGroups=hermes
cios-runner.service       inactive/dead after run, User=cios, Group=cios, SupplementaryGroups=hermes
cios-runner.path          active/waiting
```

Health:

```text
http://127.0.0.1:8765/health -> {"status":"ok"}
http://127.0.0.1:8663/health -> {"healthy":true, ...}
```

Final Hermes cron smoke:

```text
Hermes wrapper process: /opt/data/scripts/cios-daily.sh as hermes
Host runner process: /opt/cios/app/deploy/cios-host-runner.sh as cios
Daily process: .venv/bin/python scripts/daily_production_run.py as cios
Request/result/log files: cios:hermes
```

The final smoke no longer fails because of root/chowmesadmin ownership, `.hermes` traversal, missing host env, shim startup, or app output permissions.

## Remaining blockers

The final daily run exits `2` for product gates, not Unix ownership:

- `product_surface_export` timed out after 240 seconds.
- Dashboard publish remained blocked because product-market status failed.
- Demand source remains blocked: GA4 is disabled and no manual GA / Looker demand export is uploaded.

These are Phase 1/next-gate product/runtime issues. The app-user ownership repair is verified.
