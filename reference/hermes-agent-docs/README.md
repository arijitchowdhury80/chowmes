# Local Hermes Agent Documentation

Downloaded on 2026-06-15 from the official Hermes Agent docs:

- Source: https://hermes-agent.nousresearch.com/docs/
- Skills Hub: https://hermes-agent.nousresearch.com/docs/skills/

## Files

- `llms.txt`: concise machine-readable index of the docs.
- `llms-full.txt`: full concatenated Hermes Agent documentation for local search and LLM ingestion.
- `skills-catalogs.md`: extracted bundled and optional skills catalogs from `llms-full.txt`.
- `skills-hub.html`: saved rendered Skills Hub shell. The live catalog is dynamic, so use `skills-catalogs.md` for local skill lookup first.
- `site-main.js`: saved Docusaurus app bundle. Useful only when checking route/catalog metadata.

## Lookup Policy

For Hermes Agent questions, search this folder first:

```sh
rg -n "search terms" reference/hermes-agent-docs
```

If the answer is not present locally, or if the question depends on a newer version of Hermes than this snapshot, check the official docs online before using other sources.

Do not install, enable, or modify Hermes skills based only on this reference. Treat skills as documentation until Arijit explicitly asks to install or activate one.

## Refresh

To refresh the local snapshot:

```sh
curl -L --fail --silent --show-error https://hermes-agent.nousresearch.com/docs/llms.txt -o reference/hermes-agent-docs/llms.txt
curl -L --fail --silent --show-error https://hermes-agent.nousresearch.com/docs/llms-full.txt -o reference/hermes-agent-docs/llms-full.txt
curl -L --fail --silent --show-error https://hermes-agent.nousresearch.com/docs/skills/ -o reference/hermes-agent-docs/skills-hub.html
curl -L --fail --silent --show-error https://hermes-agent.nousresearch.com/docs/assets/js/main.ffe088f1.js -o reference/hermes-agent-docs/site-main.js
awk 'BEGIN{copy=0} /^<!-- source: website\/docs\/reference\/skills-catalog.md -->/{copy=1} /^<!-- source: / && copy==1 && $0 !~ /skills-catalog.md|optional-skills-catalog.md/{exit} {if(copy) print}' reference/hermes-agent-docs/llms-full.txt > reference/hermes-agent-docs/skills-catalogs.md
```
