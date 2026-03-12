# Active Tasks

## [2026-03-12-google-places-setup] Enable Google Places data pulling
- **Status**: ✅ 完成
- **Requested**: 2026-03-12 07:28
- **Updated**: 2026-03-12 08:02
- **Notes**: New API key from Obsidian note was live-tested successfully against Google Places Text Search. Updated OpenClaw config so `goplaces` uses the working backend key. Also updated the workspace `goplaces` skill docs to point at the real script path and document that the key is injected from `skills.entries.goplaces.apiKey` into `GOOGLE_PLACES_API_KEY`.
- **Result**: Google Places is configured into both runtime and skill-layer docs; ready for real lead pulls.

# Completed (recent)
- [2026-03-12-google-skill-audit] `gws` backend works for Gmail+Calendar; current Google Workspace skill docs still need migration from `gog` to `gws`; wrappers are acceptable as thin shorthands.
- [2026-03-12-google-cli-assessment] `gws` viability confirmed; Gmail/Calendar/Drive/Sheets usable, full parity still pending.
- [2026-03-12-telegram-pairing] Approved Telegram pairing codes for the new bots; CMO now uses Judge bot.
- [2026-03-12-runtime-audit] main+cso+cro+cmo+coo confirmed; subagents now use per-agent workspaces under ~/agents.
