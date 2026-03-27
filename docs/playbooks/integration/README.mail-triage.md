# Mail triage worker (local, code-based)

A small local worker for Gmail triage built in explicit Node.js code around the already-installed `gog` CLI.

## What it does in v1

- fetches candidate emails from `adam@xvadur.com`
- normalizes Gmail thread/message data into a simpler local shape
- classifies messages into configurable categories:
  - `lead`
  - `provider`
  - `finance`
  - `legal`
  - `newsletter`
  - `ignore`
  - `other`
- decides labels/actions
- can create **draft replies only** for selected categories
- defaults to **dry-run** behavior
- is structured so another mailbox can be added later in config

## Why this exists

The old n8n flow is gone. This worker keeps the logic:

- local
- legible
- reversible
- not hidden inside workflow nodes

## Files

- `package.json` – simple runner scripts
- `config/mail-triage.sample.json` – sample config without secrets
- `src/mail-triage/cli.js` – one-shot runner CLI
- `src/mail-triage/run.js` – orchestration for one mailbox run
- `src/mail-triage/providers/gmail-gog.js` – Gmail provider using `gog`
- `src/mail-triage/lib/normalize.js` – message normalization
- `src/mail-triage/lib/classifier.js` – AI classification with heuristic fallback
- `src/mail-triage/lib/planner.js` – label/action planning
- `src/mail-triage/lib/draft-reply.js` – draft generation for human review
- `runs/mail-triage/*.json` – run reports
- `MAIL_TRIAGE_IMPLEMENTATION_NOTE.md` – concise implementation note

## Requirements

- `node` installed
- `gog` installed and already authenticated for `adam@xvadur.com`
- optional: `OPENAI_API_KEY` (or whichever env var you set in config) for AI classification and draft generation

## Usage

### 1. Review the sample config

Start from:

```bash
config/mail-triage.sample.json
```

If you want a real config file:

```bash
cp config/mail-triage.sample.json config/mail-triage.local.json
```

### 2. Dry-run first

```bash
npm run triage -- --config config/mail-triage.sample.json --mailbox business --mode dry-run
```

or:

```bash
node src/mail-triage/cli.js --config config/mail-triage.sample.json --mailbox business --mode dry-run
```

This will:

- fetch threads
- normalize them
- classify them
- compute planned labels/actions
- optionally generate proposed draft text
- write a JSON report into `runs/mail-triage/`

It will **not** change Gmail state.

### 3. Apply mode

```bash
npm run triage -- --config config/mail-triage.sample.json --mailbox business --mode apply
```

Apply mode will:

- ensure configured labels exist
- apply planned labels to matching threads
- create Gmail drafts for selected categories

It will **not send** anything.

## Current action policy

In apply mode the worker may:

- add `triage/*` labels
- remove `UNREAD` for `newsletter` and `ignore`
- create a Gmail draft reply for configured categories

It does **not**:

- send emails
- archive messages
- delete messages
- unsubscribe

## AI behavior

The classifier prefers an OpenAI-compatible API when configured, but falls back to simple heuristics if the API key is missing or the request fails.

That means the worker remains runnable even without AI credentials, while still preserving the classification step in code.

## Extending to a second mailbox later

Add another mailbox entry under `mailboxes` in config with its own:

- account
- fetch query
- labels
- classification rules
- drafting settings

The current runner already selects a mailbox by name:

```bash
node src/mail-triage/cli.js --config config/mail-triage.local.json --mailbox business --mode dry-run
```

## Notes

- Search currently uses Gmail query syntax through `gog gmail search`.
- Thread details come from `gog gmail thread get`.
- Drafts are created with `gog gmail drafts create`.
- The worker is intentionally plain and direct over clever.
