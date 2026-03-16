---
name: google-workspace
description: Unified Google Workspace skill for Gmail and Calendar across business and personal accounts. Use for inbox triage, thread review, draft-first replies, scheduling, availability checks, event creation, cross-account conflict checks, and any request involving Adam's Google mail/calendar. Choose the account by intent: business for adam@xvadur.com, personal for yksvadur.ja@gmail.com.
---

# Google Workspace

Use this as the single Google mail + calendar skill.

## Accounts

- Business: `adam@xvadur.com`
- Personal: `yksvadur.ja@gmail.com`

## Account routing

Choose account by real-world context, not by tool name.

### Use business account when the task is about:
- Xvadur
- clients, leads, pilots, sales, partnerships
- work meetings
- company operations
- anything explicitly tied to `adam@xvadur.com`

### Use personal account when the task is about:
- private life
- family, friends, personal admin
- non-work appointments
- anything explicitly tied to `yksvadur.ja@gmail.com`

If ambiguous, ask one short question before writing.

## Rule

Always pass the account explicitly. Do not rely on defaults.

## Gmail operations

### Search inbox
```bash
gog gmail search "in:inbox newer_than:7d" --max=20 --json --no-input --account <EMAIL>
```

### Get thread
```bash
gog gmail thread get <threadId> --json --no-input --account <EMAIL>
```

### Create draft
```bash
gog gmail drafts create --to "x@y.com" --subject "..." --body "..." --no-input --account <EMAIL>
```

## Calendar operations

### List events
```bash
gog calendar list --days 1 --json --no-input --account <EMAIL>
```

### Create event
```bash
gog calendar create primary --summary "..." --from "<ISO>" --to "<ISO>" --json --no-input --account <EMAIL>
```

## Standard workflows

### Inbox triage
1. Pick business or personal account.
2. Search inbox.
3. Open important threads.
4. Summarize what matters.
5. Draft replies instead of sending unless explicitly approved.

### Scheduling from email
1. Read the thread.
2. Identify which account the meeting belongs to.
3. Check that account calendar.
4. If useful, also check the other account for conflicts.
5. Propose slots or create draft reply.
6. Create event only when timing is confirmed.

### Calendar management
1. Pick the correct account.
2. List upcoming events or search the target date range.
3. Create/update/delete only on explicit user intent.
4. Confirm timezone and attendees before external invites.

## Safety

- Draft-first for email by default.
- Sending email requires explicit approval.
- Sending invites to external recipients requires explicit approval.
- Confirm timezone for event writes when timing could be ambiguous.
- Keep business and personal actions separated unless the task explicitly needs both.

## Useful mental model

This is not six skills. It is one operating surface with two accounts.
