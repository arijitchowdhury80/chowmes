# CI-OS Application User Hardening

Date: 2026-07-13
Status: service hardening applied, runner-boundary follow-up required
Phase: 1. Restore Hermes-owned execution
Source release: `40e171ce24ca4bae97d4f8db8f45debae232acf4`
Release archive SHA-256: `4798a29111280e4866863218674ecbfb04d4672ccb7ef146e57a10d72147ae1e`

## Reason

Arijit identified a bad practice: CI-OS execution paths were using the admin
user or root-adjacent ownership. The corrected boundary is:

- `chowmesadmin` is an access/admin identity only.
- `root` is not a CI-OS artifact producer.
- CI-OS host services run as dedicated application users.
- Hermes remains the scheduler/orchestrator and must not absorb CI-OS business
  logic.

## Source Contract Change

The CI-OS package contract now requires the local admin service to run as the
dedicated application user:

```text
User=cios
Group=cios
```

Verified locally before deployment:

```text
python3 -m pytest tests/scripts/test_verify_hermes_package_contract.py -q
52 passed in 4.24s

python3 -m pytest tests/deploy/test_cios_daily_wrapper.py tests/scripts/test_verify_hermes_package_contract.py -q
69 passed in 14.08s

python3 -m pytest
1186 passed, 1 skipped, 23 deselected in 24.36s
```

## Applied Server Changes

Backups:

```text
/root/.hermes/backups/cios-app-user-repair-20260713T220341Z/before-units-and-config.tgz
/root/.hermes/backups/cios-shim-user-repair-20260713T220604Z/before-shim.tgz
```

Created dedicated users:

```text
cios:x:997:986::/var/lib/cios:/usr/sbin/nologin
cios-shim:x:995:985::/var/lib/cios-shim:/usr/sbin/nologin
```

Changed `cios-admin.service`:

```text
User=cios
Group=cios
ActiveState=active
1268274 cios cios /root/.hermes/apps/cios/.venv/bin/python /root/.hermes/apps/cios/scripts/run_admin.py --env-file /root/.hermes/cios-env --host 127.0.0.1 --port 8765
```

Changed `cios-claude-shim.service`:

```text
User=cios-shim
Group=cios-shim
ActiveState=active
1270136 cios-shim cios-shim /root/.hermes/apps/cios/.venv/bin/python /opt/cios/claude-shim/.venv/bin/uvicorn shim:app --host 127.0.0.1 --port 8663
```

Moved the shim away from:

```text
/home/chowmesadmin/cios
```

and into:

```text
/opt/cios/claude-shim
```

The candidate `cios-shim` process was tested on `127.0.0.1:8664` before
replacing the live service on `127.0.0.1:8663`.

## Ownership And Permissions

Current checked owner distribution:

```text
/root/.hermes/apps/cios
/root/.hermes/apps/algolia-competitive-intelligence/apps/dashboard/public
322 cios:hermes
```

Key files:

```text
-rw-r----- 1 root cios-shim   127 /etc/cios-claude-shim.env
-rw-r----- 1 cios hermes      626 /root/.hermes/cios-env
-rwxr-x--- 1 cios hermes    24898 /root/.hermes/scripts/cios-daily.sh
```

Because `setfacl` is not installed on the VPS, `/root/.hermes` and
`/root/.hermes/apps` use execute-only traversal (`711`) rather than ACLs. This
allows `cios` and `hermes` to reach the app path without granting directory
listing.

## Verification

Package contract:

```text
sudo -u cios bash -lc "cd /root/.hermes/apps/cios && .venv/bin/python scripts/verify_hermes_package_contract.py --app-dir ."
PASS: CI-OS Hermes package contract satisfied

sudo -u hermes bash -lc "cd /root/.hermes/apps/cios && .venv/bin/python scripts/verify_hermes_package_contract.py --app-dir ."
PASS: CI-OS Hermes package contract satisfied
```

Local-only binds:

```text
127.0.0.1:8663 users:(("uvicorn",pid=1270136,fd=6))
127.0.0.1:8765 users:(("python",pid=1268274,fd=6))
```

Health:

```text
http://127.0.0.1:8765/health -> {"status":"ok"}
http://127.0.0.1:8663/health -> {"healthy":true,"checked_at":1783980376.2029722,"detail":null}
```

Owner-based process check:

```text
systemctl show cios-admin.service cios-claude-shim.service -p User -p Group -p ActiveState
User=cios
Group=cios
ActiveState=active

User=cios-shim
Group=cios-shim
ActiveState=active
```

The remaining `chowmesadmin` processes observed are unrelated Prism and Bible
services, not CI-OS admin or shim services.

## Remaining Boundary

This hardening fixes the live CI-OS admin service, shim service, source
contract, package ownership, and secrets readability. It does not yet make the
Hermes cron subprocess itself run as `cios`.

Reason: Hermes cron runs inside the `hermes` container as the `hermes` runtime
user. Simply `chown -R cios:cios` would break the scheduler again. The next
Phase 1 design slice should add an explicit runner handoff so Hermes can
schedule and record the job while the CI-OS daily subprocess executes as the
`cios` app user.

Do not treat the application-user hardening as a Phase 1 gate pass until that
runner boundary is resolved or explicitly accepted as `hermes`-scheduled with
`cios`-owned package state.
