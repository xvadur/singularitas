# Google Workspace CLI Phase 1 Validation — 2026-03-12

## Result

**Partial pass / blocked on auth bootstrap**

`gws` is now installed and usable locally, but real API validation is currently blocked because no `gws` auth has been configured yet.

## What was validated successfully

### Installation
- `gws` installed successfully via:
  - `npm install -g @googleworkspace/cli`
- binary location:
  - `/Users/_xvadur/.npm-global/bin/gws`

### CLI surface
`gws` is available and exposes Workspace services including:
- drive
- sheets
- gmail
- calendar
- docs
- people
- chat
- tasks
- forms
- meet
- classroom

### Auth model
`gws auth --help` confirms supported flows:
- `gws auth login`
- `gws auth setup` (requires `gcloud`)
- `gws auth status`
- `gws auth export`
- `gws auth logout`

### Current auth state
`gws auth status` shows:
- no credentials configured
- no client secret present
- no token cache present

Meaning:
- `gws` is installed
- but it is not yet connected to any Google account

### Local environment blockers
- `gcloud` is **not installed**
- `gws auth setup` therefore is not currently available as the easy bootstrap path
- `~/.config/gws/client_secret.json` does **not** exist

### Command/schema validation
Without auth, we still confirmed that `gws` can introspect real method schemas.
Validated examples:
- `gws schema gmail.users.messages.list`
- `gws schema calendar.events.list`

This confirms:
- Gmail and Calendar surface is real
- parameters/scopes are discoverable
- JSON-first agent workflow is viable

## Current comparison vs existing setup

### Existing backend
- `gog` is installed and available
- current Google skills in workspace are written against `gog`

### Important note
Current `gog auth status` output does not show an active account either, at least in the current shell context.
That means this Phase 1 run did **not** verify a reusable auth bridge from `gog` into `gws`.

## What remains unvalidated

Still blocked until auth exists:
- Gmail inbox read
- Gmail thread fetch
- Gmail draft create
- Calendar event list
- Calendar event create
- business vs personal account switching

## What is needed next

There are 3 viable next paths.

### Path A — manual OAuth for `gws` (recommended)
Create a Google Cloud OAuth Desktop client and save the downloaded JSON to:
- `~/.config/gws/client_secret.json`

Then run:
```bash
gws auth login -s gmail,calendar,drive,sheets
```

This is the cleanest path for testing.

### Path B — install `gcloud`
Install Google Cloud CLI, then run:
```bash
gws auth setup --login
```

This is the easiest guided bootstrap, but requires `gcloud`.

### Path C — inject existing token/credentials
If you already have usable OAuth credentials or a service-account JSON:
- set `GOOGLE_WORKSPACE_CLI_CREDENTIALS_FILE`
- or set `GOOGLE_WORKSPACE_CLI_TOKEN`

Useful for automation, but not the best first-time path unless credentials already exist.

## Recommended next action

Recommended immediate next step:
1. create manual OAuth Desktop credentials for `gws`
2. store them at `~/.config/gws/client_secret.json`
3. run `gws auth login -s gmail,calendar,drive,sheets`
4. then re-run validation with real read/write-safe commands

## Decision update

Migration remains viable.
But today it is still at:
- **tool installed** ✅
- **auth bootstrapped** ❌
- **real workflow parity validated** ❌

So we are ready for auth bootstrap, not for backend switch yet.
