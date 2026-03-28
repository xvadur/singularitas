# /save runbook

Purpose:
Turn the current conversation state into usable continuity.

Files:
- `memory/YYYY-MM-DD.md` -> distilled daily continuity
- `memory/logs/YYYY-MM-DD.md` -> richer daily progress log
- `MEMORY.md` -> durable truth only when something should persist beyond today

Rules:
- do not dump transcripts
- log = richer execution trace
- daily memory = distilled resume state
- durable memory = only stable truths, preferences, strategy, environment facts

Expected command behavior:
- `/save` should update today's log and today's memory
- it may update `MEMORY.md` only when justified
- response should confirm what was saved
