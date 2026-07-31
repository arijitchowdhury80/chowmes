# CI-OS Phase 1 Read-Only Preflight

Date: 2026-07-13
Status: evidence captured, no server changes made
Phase: 1. Restore Hermes-owned execution

## Boundary

This preflight inspected the Chowmes VPS through the approved SSH helper after
Phase 0 passed. No ownership, service, cron, wrapper, firewall, SSH, data, or
public artifact changes were made.

Hermes remains the runtime OS. CI-OS remains a separately versioned extension.
This preflight does not authorize Hermes core changes.

## Confirmed Access

- SSH diagnostic: TCP/22 open.
- SSH login: `chowmesadmin` key login succeeded.
- Host: `chowmes`
- OS: Ubuntu 24.04.4 LTS
- Kernel: Linux 6.8.0-134-generic

## Phase 0 Carry-Forward

- Current source branch:
  `arijitchowdhury80/algolia-competitive-intelligence`,
  `codex/ci-os-phase0-baseline`, commit
  `149e63c717c7d3853624c302473af2ba295ded89`.
- Deployed executable package maps to `13731ac` with non-executable
  workspace status-note drift.
- Deployed package contract currently passes:
  `PASS: CI-OS Hermes package contract satisfied`.

## Runtime Ownership Findings

### Users

`getent passwd` returned only `root` for the checked runtime IDs:

```text
root:x:0:0:root:/root:/bin/bash
```

The UID/GID values that own most Hermes/CI-OS paths, especially `10000:10000`
and `501:*`, are not named users on the host. This makes the runtime ownership
contract implicit and brittle.

### Services

```text
cios-admin.service:
  User=
  Group=
  DynamicUser=no
  ExecStart=/root/.hermes/apps/cios/.venv/bin/python /root/.hermes/apps/cios/scripts/run_admin.py --env-file /root/.hermes/cios-env --host 127.0.0.1 --port 8765

cios-claude-shim.service:
  User=chowmesadmin
  Group=
  DynamicUser=no
  ExecStart=/home/chowmesadmin/cios/.venv/bin/uvicorn deploy.claude-shim.shim:app --app-dir /home/chowmesadmin/cios --host 127.0.0.1 --port 8663
```

Implications:

- `cios-admin.service` runs as root.
- `cios-claude-shim.service` runs from a separate `/home/chowmesadmin/cios`
  copy, not the canonical `/root/.hermes/apps/cios` package path.
- The admin service can create root-owned runtime output, which directly
  conflicts with Hermes cron cleanup and publication.

### Path Ownership

```text
/root/.hermes/apps/cios                                      UNKNOWN:root 755
/root/.hermes/apps/cios/out                                  UNKNOWN:root 755
/root/.hermes/apps/cios/data                                 UNKNOWN:root 755
/root/.hermes/scripts/cios-daily.sh                          UNKNOWN:UNKNOWN 755
/root/.hermes/apps/algolia-competitive-intelligence/.../public          UNKNOWN:UNKNOWN 755
/root/.hermes/apps/algolia-competitive-intelligence/.../public/data     UNKNOWN:UNKNOWN 755
/root/.hermes/apps/algolia-competitive-intelligence/.../public/v2/data  UNKNOWN:UNKNOWN 755
```

Owner counts:

```text
/root/.hermes/apps/cios:
  10699 501:root
     82 root:root
     68 501:staff

/root/.hermes/apps/algolia-competitive-intelligence/apps/dashboard/public:
     66 root:root
     36 10000:10000
```

Recent CI-OS output files show the same split:

```text
501:root  /root/.hermes/apps/cios/out/argus-public-run-status.json
501:root  /root/.hermes/apps/cios/out/argus-data-plane-manifest.json
root:root /root/.hermes/apps/cios/out/argus-dashboard.json
root:root /root/.hermes/apps/cios/out/argus-dashboard.html
root:root /root/.hermes/apps/cios/out/argus-demand-work-order-guide.json
```

This confirms Phase 1's core failure: one runtime path is being written by
multiple identities.

## Cron Evidence

Hermes cron storage:

```text
/root/.hermes/cron/jobs.json
mode=0600 uid=10000 gid=10000
```

Relevant job:

```text
id=107e64d347d9
name=cios-v2-daily
schedule=0 9 * * *
state=scheduled
script=cios-daily.sh
deliver=local
```

Last recorded error:

```text
Script exited with code 1
rm: cannot remove '/opt/data/apps/cios/out/argus-demand-plan-template.csv': Permission denied
rm: cannot remove '/opt/data/apps/cios/out/brief.html': Permission denied
rm: cannot remove '/opt/data/apps/cios/out/argus-public-run-status.json': Permission denied
rm: cannot remove '/opt/data/apps/cios/out/argus-dashboard.json': Permission denied
rm: cannot remove '/opt/data/apps/cios/out/argus-dashboard.html': Permission denied
```

The error contains many additional files under
`/opt/data/apps/cios/out/briefs/algolia/`. The current `/opt/data/apps/cios`
path no longer exists, so this error records the previous failed scheduled
cycle, not the current filesystem path.

## Wrapper Findings

Live wrapper:

```text
/root/.hermes/scripts/cios-daily.sh
```

Package wrapper:

```text
/root/.hermes/apps/cios/deploy/cios-daily.sh
```

Both wrappers currently:

- default `APP` to `/opt/data/apps/cios`, then fall back to
  `/root/.hermes/apps/cios` if `/opt/data/apps/cios` is absent;
- default `PUB` to `/opt/data/apps/algolia-competitive-intelligence/.../public`,
  then fall back to `/root/.hermes/apps/algolia-competitive-intelligence/.../public`;
- set `OUT="${CIOS_OUTPUT_DIR:-$APP/out}"`;
- reject only empty `OUT` and `/`;
- run `rm -rf "$OUT"` before recreating output;
- publish public status and demand artifacts with plain `cp`.

This confirms the planned Phase 1 scope:

1. The wrapper still uses broad output deletion.
2. The output path validation is too weak for a production wrapper.
3. The publication path can inherit whichever user ran the wrapper or sidecar.
4. The next repair must define the runtime owner and make every app/output/public
   path writable by that owner before a scheduled run.

## Current Public Status

```text
status=blocked_on_evidence
publish_status=blocked
generated_at=2026-07-13T01:51:21.937836Z
next_hermes_action=configure_ga4_or_upload_demand_export
```

This is expected. Phase 1 is about execution ownership and scheduled reliability,
not demand evidence or launch readiness.

## Repair Direction

Do not begin Product Muscle, GA4/Looker, Argus intelligence, UI, or pilot work.

Smallest credible Phase 1 repair plan:

1. Define the canonical runtime owner for CI-OS cron, app, output, and public
   artifacts. Current evidence suggests UID/GID `10000:10000` is Hermes cron's
   owner, but it lacks a named passwd entry and must be handled carefully.
2. Stop root-owned output creation by changing `cios-admin.service` away from
   root or isolating admin-generated output from cron-owned output.
3. Remove or retire the separate `/home/chowmesadmin/cios` shim copy, or make
   it explicitly non-production, after confirming no required route depends on it.
4. Replace `rm -rf "$OUT"` with a validated, marked staging-output rotation.
5. Make publication atomic and owner-consistent only after ownership is fixed.
6. Prove with tests first, then one manual Hermes-owned dry run, then two
   scheduled Hermes runs.

## Open Question Before Mutation

The main decision before changing server state is the canonical runtime owner:

- Use the existing numeric Hermes owner `10000:10000`, even without a named
  passwd user.
- Create or map a named `hermes` user to the existing runtime ownership.
- Run CI-OS under `chowmesadmin`, which would be simpler operationally but less
  aligned with the current Hermes cron file ownership.

No ownership or service change should happen until this choice is explicit.
