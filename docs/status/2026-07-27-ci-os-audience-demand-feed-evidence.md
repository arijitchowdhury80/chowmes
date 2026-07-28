# CI-OS Audience Demand feed evidence

Date: 2026-07-27
Tenant: `algolia`
Runtime path: `/opt/cios/app`
Runtime user: `cios`

## Result

The manual Audience Demand feed path is verified on Chowmes production.

- Uploaded canonical Looker demand CSV:
  `/opt/cios/app/data/looker/algolia/algolia-looker-demand_2026-07-07_2026-07-13.csv`
- Remote ownership after upload: `cios:cios`
- Remote line count: `100` lines, meaning header plus 99 demand rows.
- Import command ran as `cios` with `/etc/cios-env` loaded.
- Import exit code: `0`
- Import status: `refreshed`
- Prepare summary:
  - `discovered_count`: 1
  - `ready_count`: 1
  - `normalized_row_count`: 99
  - `skipped_row_count`: 0
  - `error_count`: 0
- Current-demand gate after import: `pass`
- Current processed demand rows after import: `120`

## Verification Commands

```bash
sudo -u cios wc -l /opt/cios/app/data/looker/algolia/algolia-looker-demand_2026-07-07_2026-07-13.csv
```

```bash
cd /opt/cios/app
sudo -u cios bash -lc "set -a; . /etc/cios-env; set +a; .venv/bin/python scripts/import_demand_and_refresh.py --tenant algolia --queued --app-dir /opt/cios/app --work-root /tmp/cios-product-market --out-dir /opt/cios/app/out --own-company-name Algolia --output /tmp/cios-demand-import-result.json"
```

```bash
cd /opt/cios/app
sudo -u cios bash -lc "set -a; . /etc/cios-env; set +a; .venv/bin/python scripts/check_argus_demand_source_gate.py --tenant algolia --app-dir /opt/cios/app --work-root /tmp/cios-product-market --require-current-demand"
```

## Recurring Automation Status

The recurring GA4 Data API feed is not configured yet.

Remote `/etc/cios-env` is missing:

- `CIOS_GA4_EXPORT_ENABLED`
- `CIOS_GA4_PROPERTY_ID`
- `CIOS_GA4_CREDENTIALS_JSON`
- `GOOGLE_APPLICATION_CREDENTIALS`
- `CIOS_GA4_SOURCE_URL`
- `CIOS_GA4_ROLLING_DAYS`

Local ChowMes `.env.local` is also missing the same GA4 keys.

This means CI-OS can process queued manual Audience Demand exports today, but cannot yet pull fresh recurring demand from GA4 unattended. The next implementation step is to install a GA4 service-account credential readable by `cios`, set the GA4 property/env values in `/etc/cios-env`, and run the existing `scripts/run_argus_demand_intake.py` path in GA4 mode.

## Notes

- Do not run CI-OS commands through `/root/.hermes/apps/cios` as the application user. The correct app-user runtime path is `/opt/cios/app`.
- The old `/root/.hermes/apps/cios` path remains a package source location, but `/root/.hermes` traversal blocks direct `cios` execution.
- No Hermes core files, SSH settings, firewall settings, or Caddy configuration were changed.
