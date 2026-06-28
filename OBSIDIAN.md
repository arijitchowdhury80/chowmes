# Obsidian Access Policy

Chowmes should treat Obsidian as Arijit's central source of truth for work knowledge, projects, decisions, raw captures, synthesized notes, and operating memory.

## Current Approved Vault

As of June 16, 2026, Arijit has approved connecting the local Obsidian vault for Chowmes/Athena work.

```text
Mac vault container: /Users/arijitchowdhury/Dropbox/AI-Development/Personal/Obsidian-Vault
Mac active vault root: /Users/arijitchowdhury/Dropbox/AI-Development/Personal/Obsidian-Vault/MyOS
Hermes VPS mirror: /opt/data/knowledge/obsidian/MyOS
Default Hermes write inbox: /opt/data/knowledge/obsidian/MyOS/Chowmes-Inbox
```

The active vault root is `MyOS` because it contains `.obsidian/`.

The VPS mirror is not Obsidian Sync itself. It is a filesystem mirror used by live Hermes. Use `scripts/sync-obsidian-to-hermes` to push the local vault mirror to Hermes and `scripts/sync-obsidian-inbox-from-hermes` to pull Hermes-generated inbox notes back to the Mac vault.

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

Do not expand beyond the `MyOS` vault root without a separate approval.

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

Current sync path:

```text
Mac MyOS vault -> VPS /opt/data/knowledge/obsidian/MyOS
VPS /opt/data/knowledge/obsidian/MyOS/Chowmes-Inbox -> Mac MyOS/Chowmes-Inbox
```

Use the checked-in sync scripts. Avoid mounting broad cloud-drive folders directly on the VPS unless there is a specific reason.

## Access Rules

- Read and search the vault when it is relevant to work.
- Write generated notes to `Chowmes-Inbox/` by default unless Arijit names a specific project, decision, research, or knowledge note.
- No secrets in synced notes.
- Summaries and extracted memory must be reviewed before being added to `MEMORY.md`.

## Future Integration Options

Good next step:

- Migrate `/opt/data/workspace/Knowledge` into the Obsidian vault structure.
- Add scheduled or explicit sync cadence once the inbox workflow proves safe.

Later options:

- Add an MCP filesystem server scoped only to the curated folder.
- Add a lightweight local index.
- Add an external memory provider only if built-in memory and curated docs are no longer enough.
