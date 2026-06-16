# Obsidian Access Policy

Chowmes should treat Obsidian as a curated knowledge base, not as unrestricted personal-data access.

## Recommended Vault Shape

Create or sync a curated subset for Chowmes:

```text
Chowmes-Knowledge/
  Company-OS/
  Founder/
  Product-Ideas/
  Architecture/
  Projects/
  Research/
  Decisions/
  Meeting-Notes/
```

Do not connect the full personal vault by default.

## Safe To Include

- Product ideas.
- Project notes.
- Architecture notes.
- Research notes.
- Decision records.
- Meeting notes intended for work.
- Public or work-safe reference material.
- Operating principles for Chowmes.

## Keep Out Unless Explicitly Approved

- Financial accounts and tax records.
- Passwords, recovery codes, API keys, tokens, and private keys.
- Identity documents.
- Medical records.
- Family or relationship notes.
- Legal disputes or attorney-client material.
- Private journal entries.
- Anything that would be harmful if exposed to an API provider.

## Preferred Sync Pattern

Start with one-way sync of a curated folder to the VPS:

```text
Mac curated vault subset -> VPS /opt/data/knowledge/obsidian
```

Use Git or rsync. Avoid mounting broad cloud-drive folders directly on the VPS unless there is a specific reason.

## Access Rules

- Read-only by default.
- Write access only to a dedicated inbox or generated-notes folder.
- No secrets in synced notes.
- No automatic ingestion of the full vault.
- Summaries and extracted memory must be reviewed before being added to `MEMORY.md`.

## Future Integration Options

Good first step:

- Sync curated markdown files to `/opt/data/knowledge/obsidian`.
- Let Chowmes read/search them during deep work only.

Later options:

- Add an MCP filesystem server scoped only to the curated folder.
- Add a lightweight local index.
- Add an external memory provider only if built-in memory and curated docs are no longer enough.
