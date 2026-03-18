# Operability Checklist

- [x] `openclaw.json` routes the default Telegram account to Jarvis (`main`)
- [x] `openclaw.json` routes legacy bridge bots to canonical owners (`research`, `revenue`, `web`, `integration`)
- [x] founder briefing can be produced from project files without chat reconstruction
- [x] missing source data is explicitly marked
- [x] one approval packet exists
- [x] one phone-engine packet exists
- [x] one web/proof packet exists

## Verification note

These checks are currently satisfied at the file/config level.
They do not prove live Telegram transport delivery, SIP feasibility, CRM health, or publishing readiness.

If all items are true, the cockpit is operable enough for tomorrow.
