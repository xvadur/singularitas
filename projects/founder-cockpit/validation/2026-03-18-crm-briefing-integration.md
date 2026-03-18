# 2026-03-18 CRM Briefing Integration

## Goal

Close the CRM path contract and make the founder briefing consume live relationship-memory data instead of falling back to `NO_SIGNAL`.

## Current evidence

- CRM DB exists at `/Users/_xvadur/singularitas/data/crm/pcrm.sqlite`
- Tables present: `contacts`, `interactions`, `reminders`
- Record counts:
  - `contacts = 2`
  - `interactions = 2`
  - `reminders = 2`
- Representative data:
  - `Premedix Clinic lead` is a `prospect` with `open` status
  - `Inwhite clinic lead` is a `prospect` with `pilot_pending` status
  - both have open follow-up pressure in `reminders`

## Exact path contract

- Canonical relationship-memory source: `/Users/_xvadur/singularitas/data/crm/pcrm.sqlite`
- Canonical CRM tables for briefing synthesis: `contacts`, `interactions`, `reminders`
- Do not use an old or inferred path
- Do not treat the DB as missing when the file exists

## Required briefing fields

The founder briefing should project CRM data into these sections:

- `Leads needing action`
- `Callbacks at risk`
- `Best next move`

Each CRM-derived item should carry:

- `contact name`
- `company`
- `relationship_tier`
- `openclaw_status`
- `next due date`
- `source_ref` or provenance

If a reminder has no `due_at`, it stays visible as `manual due date needed` instead of disappearing.

## Why the briefing still shows `NO_SIGNAL`

The DB is present and populated, so `NO_SIGNAL` is not caused by missing CRM data.

The real blocker is contract wiring:

- the briefing surface is still not reading the CRM DB path as canonical runtime input
- the projection rules for `Leads needing action` and `Callbacks at risk` are not yet wired into the founder briefing generator
- until that happens, the briefing will keep behaving as if CRM is unavailable

## How to remove `NO_SIGNAL`

1. Repoint briefing generation to `/Users/_xvadur/singularitas/data/crm/pcrm.sqlite`
2. Read `contacts`, `interactions`, and `reminders` directly
3. Synthesize open prospect items into `Leads needing action`
4. Synthesize open reminders with due dates into `Callbacks at risk`
5. If a row is missing `due_at`, keep it in the briefing and mark it `manual due date needed`
6. Only print `NO_SIGNAL` when the DB path is actually unreadable or the table query fails

## Verification

Read-only DB evidence:

```bash
sqlite3 /Users/_xvadur/singularitas/data/crm/pcrm.sqlite ".tables"
sqlite3 -header -column /Users/_xvadur/singularitas/data/crm/pcrm.sqlite "select count(*) as contacts from contacts; select count(*) as interactions from interactions; select count(*) as reminders from reminders;"
sqlite3 -header -column /Users/_xvadur/singularitas/data/crm/pcrm.sqlite "select id, name, company, role, relationship_tier, openclaw_status, contact_info from contacts order by id;"
sqlite3 -header -column /Users/_xvadur/singularitas/data/crm/pcrm.sqlite "select id, contact_id, channel, direction, subject, at, source_ref from interactions order by id;"
sqlite3 -header -column /Users/_xvadur/singularitas/data/crm/pcrm.sqlite "select id, contact_id, title, due_at, status from reminders order by id;"
```

Briefing evidence:

- `/Users/_xvadur/firma/briefings/2026-03-18-founder-briefing.md`

## Verdict

CRM is not the missing piece.
The missing piece is the path contract and briefing projection from the real DB into the founder control surface.
