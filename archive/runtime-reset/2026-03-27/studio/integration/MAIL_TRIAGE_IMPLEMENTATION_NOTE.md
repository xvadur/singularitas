# Mail triage implementation note

## Implementation choices

- Built as plain Node.js modules with no npm dependencies.
- Uses the installed `gog` CLI for Gmail reads/writes instead of n8n.
- Keeps risky behavior gated behind `--mode apply`.
- Keeps email sending out of scope entirely.
- Stores a JSON report for every run in `runs/mail-triage/` for traceability and reversibility.

## Reversibility

This worker is reversible because:

- logic is explicit in files
- apply mode is separate from dry-run mode
- labels are additive and named under `triage/*`
- no message send/delete/archive behavior exists
- every run writes a local report

## Known limitations in v1

- classification quality depends on either the AI model or basic keyword heuristics
- HTML-to-text normalization is intentionally simple, not perfect
- there is no stateful dedupe yet beyond Gmail queries/labels
- label removal policy is intentionally conservative
- draft tone still needs human review before use

## Intended next steps

- add a local reviewed-state file to skip already-triaged thread IDs
- tune category-specific prompts and draft templates
- add mailbox-specific config for second and third inboxes
- optionally add a daily review summary output
