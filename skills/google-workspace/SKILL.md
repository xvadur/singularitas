---
name: google-workspace
description: Unified Gmail + Calendar operations across business and personal accounts via gog CLI. Use for inbox triage, drafting, scheduling, and conflict checks in one workflow.
---

# Google Workspace

Unified skill for both email and calendar.

## Accounts

- Business: `adam@xvadur.com`
- Personal: `yksvadur.ja@gmail.com`

## Core principle

Always pick account explicitly with `--account` and keep business/personal intent separated.

## Gmail commands

- Search:
`gog gmail search "in:inbox newer_than:7d" --max=20 --json --no-input --account <EMAIL>`
- Thread:
`gog gmail thread get <threadId> --json --no-input --account <EMAIL>`
- Draft:
`gog gmail drafts create --to "x@y.com" --subject "..." --body "..." --no-input --account <EMAIL>`

## Calendar commands

- List today:
`gog calendar list --days 1 --json --no-input --account <EMAIL>`
- Create:
`gog calendar create primary --summary "..." --from "<ISO>" --to "<ISO>" --json --no-input --account <EMAIL>`

## Combined workflow (mail + calendar)

1. Triage inbox (urgent first).
2. If email requires meeting -> propose slot.
3. Check account calendar availability.
4. Draft response and/or create event.
5. Summarize actions: drafted / scheduled / pending.

## Safety

- Draft-first unless user says send.
- Confirm timezone and account before event writes.


## Send policy

- Default: create drafts only.
- Sending email or sending invites to external recipients requires explicit user confirmation.
- If intent is ambiguous, keep in draft mode and ask for confirmation.
