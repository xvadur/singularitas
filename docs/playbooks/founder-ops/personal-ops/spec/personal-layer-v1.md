# Personal Layer v1

Purpose: make `personal-ops` a real founder continuity layer rather than only a one-off refresh.

## Mission

`personal-ops` exists to reduce cognitive drag for Adam by keeping four surfaces legible:
- time
- inbox attention
- commitments
- personal follow-up debt

It does not own pipeline, delivery, publishing, or web execution.
It owns founder continuity.

## What the layer must answer

In founder language, `personal-ops` should be able to answer:
- what is on my calendar
- what in my inbox actually needs me
- what commitments are drifting
- what is the next personal cleanup move
- where are we still blind

## V1 source hierarchy

### 1. Calendar truth
Primary source:
- Google Calendar via `gog`
- current trusted account: `adam@xvadur.com`

Meaning:
- meetings
- time commitments
- visible scheduling load

### 2. Inbox truth
Primary source:
- Gmail via `gog`
- current trusted account: `adam@xvadur.com`

Meaning:
- operational asks waiting on the founder
- account, payment, legal, or admin notices
- direct replies that create follow-up pressure

### 3. Commitment truth
Primary source in v1:
- Apple Reminders via `remindctl`
- trusted list: `XVADUR`

Meaning:
- active follow-ups
- unfinished founder commitments
- reminder drift

### 4. Context memory
Context source only:
- Obsidian at `/Users/_xvadur/singularitas_opus`

Meaning:
- notes
- capture
- context lookup

Rule:
Obsidian is not the default live truth source for calendar, inbox, or commitments in v1.
It supports the layer, but does not replace the live surfaces.

## Core objects

### Calendar event
A time-bound commitment visible on the trusted calendar surface.

### Inbox action
A message that requires founder attention because it affects:
- money
- access
- legal/admin status
- a live conversation
- a real decision

### Commitment item
A reminder or follow-up that represents a promise, dependency, or personal task that can drift.

### Noise
Anything visible but not founder-relevant by default:
- social notifications
- routine newsletters
- passive promo mail

Noise may stay visible in tooling, but should not dominate the founder-facing summary.

## Standard outputs

### 1. Daily founder ops snapshot
File:
- `daily/YYYY-MM-DD-founder-ops.md`

Purpose:
- state read
- risk read
- next move

### 2. Personal action queue
File:
- `daily/YYYY-MM-DD-personal-action-queue.md`

Purpose:
- the concrete founder-facing queue after the refresh
- small, ordered, actionable

### 3. Interrupt packet
Only when required.

Trigger classes:
- deadline risk
- same-day conflict
- blocked access/payment risk
- real message waiting that will decay if ignored

## Interpretation rules

### Calendar
- no event means no visible event
- do not infer hidden meetings from vague context

### Inbox
- distinguish actionable from merely unread
- surface only the operational residue that actually matters

### Commitments
- overdue reminders count as active founder risk
- duplicate reminders count as clarity debt

## Refresh rule

A real refresh means:
1. check trusted calendar source
2. check trusted inbox source
3. check trusted commitment source
4. write snapshot
5. write action queue if actionable residue exists
6. update founder brief when the result changes top-level truth

## Promotion rule

Promote from `personal-ops` into founder-facing `main` when:
- founder attention is needed now
- a blocker or approval exists
- a dominant next move becomes obvious

Otherwise, keep the layer quiet and legible.

## Current v1 status

As of `2026-03-24`:
- first live refresh exists
- calendar and inbox are verified on one trusted account
- Apple Reminders is pinned as provisional commitment truth
- the main visible risk is follow-up drift, not calendar overload
