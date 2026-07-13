# CI-OS Phase 1 Runtime Owner Repair

Date: 2026-07-13
Status: repair applied, phase gate not passed
Phase: 1. Restore Hermes-owned execution
Source release: `eddbde3902d68dd70b9ac42946f6e331f6979c75`
Release archive SHA-256: `617bda2ad91faf53e322e1476ad5a9a903263a147f9ebd162be863eb1ea74c7b`

## Boundary

This repair changed only the CI-OS extension deployment on Chowmes. It did not
modify Hermes core, firewall rules, SSH configuration, secrets, public ports, or
credential policy.

Phase 1 is still active. Product Muscle, GA4/Looker, Argus intelligence, product
IA, and pilot work remain locked until their predecessor gates pass.

## Applied Changes

- Created a named `hermes` runtime identity mapped to UID/GID `10000:10000`.
- Deployed the reviewed CI-OS source bundle from commit `eddbde3` to
  `/root/.hermes/apps/cios`.
- Installed the updated CI-OS daily wrapper at
  `/root/.hermes/scripts/cios-daily.sh`.
- Installed the updated admin service unit at
  `/etc/systemd/system/cios-admin.service`.
- Changed `cios-admin.service` to run as `hermes:hermes`.
- Repaired CI-OS app, output, and public dashboard ownership to
  `hermes:hermes`.
- Added the `.cios-output-dir` marker required by the safer wrapper cleanup.
- Preserved a server-side backup before mutation:
  `/root/.hermes/backups/cios-phase1-runtime-owner-20260713T164357Z/before-config.tgz`.

## Verification Evidence

Initial post-repair service and contract verification:

```text
uid=10000(hermes) gid=10000(hermes) groups=10000(hermes)
ExecMainStatus=0
User=hermes
Group=hermes
ActiveState=active
1045729 hermes hermes /root/.hermes/apps/cios/.venv/bin/python /root/.hermes/apps/cios/scripts/run_admin.py --env-file /root/.hermes/cios-env --host 127.0.0.1 --port 8765
PASS: CI-OS Hermes package contract satisfied
{"status":"ok"}
```

Independent ownership and contract verification:

```text
hermes:x:10000:10000::/root/.hermes:/usr/sbin/nologin
hermes:x:10000:
ExecMainStatus=0
User=hermes
Group=hermes
ActiveState=active
62 hermes:hermes
-rw-r--r-- 1 hermes hermes 0 Jul 13 12:43 /root/.hermes/apps/cios/out/.cios-output-dir
PASS: CI-OS Hermes package contract satisfied
{"status":"ok"}
```

Focused deployed regression tests run as `hermes`:

```text
.....................................................................    [100%]
69 passed in 12.66s
```

Bounded Hermes-owned manual smoke using private output/public directories:

```text
MANUAL_OUT=/root/.hermes/apps/cios/out/manual-phase1-20260713T164953Z
MANUAL_PUBLIC=/root/.hermes/apps/cios/out/manual-phase1-public-20260713T164953Z
MANUAL_EXIT=124
daily production runner timed out after 90s
MANUAL_OWNER_COUNTS
      9 hermes:hermes
status=blocked_runtime_timeout
next_hermes_action=inspect_daily_run_stage_ledger_and_rerun_after_timeout_fix
```

Post-timeout cleanup verification:

```text
PROCESSES
OWNER_COUNTS_APP
     62 hermes:hermes
OWNER_COUNTS_PUBLIC
     75 hermes:hermes
ExecMainStatus=0
User=hermes
Group=hermes
ActiveState=active
{"status":"ok"}
```

The manual smoke proves the repaired wrapper can execute live source collection
as `hermes`, preserve Hermes-owned output, time out into a structured blocked
state, and leave no orphan CI-OS worker processes. It does not satisfy the Phase
1 scheduled-run gate.

## Current Cron State

The Hermes cron job remains:

```text
id=107e64d347d9
name=cios-v2-daily
schedule_display=0 9 * * *
state=scheduled
script=cios-daily.sh
```

The last recorded cron error is still the pre-repair 2026-07-13 09:00 ET
permission failure against old root-owned output. The next scheduled run must
replace that evidence.

## Remaining Phase 1 Work

- Let the next real scheduled Hermes run execute with the repaired runtime owner.
- Investigate the 90-second smoke timeout using the stage ledger rather than
  lowering the gate.
- Prove two consecutive scheduled Hermes runs complete without root
  intervention, permission errors, timeout, orphan work, or stale-public
  fallback.

Phase 1 cannot pass until those scheduled-run requirements are met.
