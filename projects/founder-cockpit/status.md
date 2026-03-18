# Status

Runtime scope only. Canonical founder-facing business state lives in `/Users/_xvadur/firma/briefings/founder-cockpit.md`.

- Owner: `jarvis`
- State: `partial`
- Operability target: `workbench live by evening`

## Currently wired

- runtime doctrine and agent model exist in the repo
- canonical agent registry exists
- OpenClaw routing bridge can now be updated from C-level accounts into the new model
- project-home template exists with approvals, validation, and content subfolders
- startup contract is now formalized in `/Users/_xvadur/singularitas/projects/founder-cockpit/spec/startup-contract.md`

## Currently blocked or incomplete

- local CRM exists at `/Users/_xvadur/singularitas/data/crm/pcrm.sqlite`, but runtime docs still point at the old path and need contract cleanup
- no verified n8n execution state is visible from the current shell session
- no verified Vapi API key is visible in current runtime config
- founder briefing is not yet generated automatically
- website/proof queue is now promoted into `firma`, but runtime signals still need to feed it reliably

## Manual fallbacks allowed for tomorrow

- manual founder queue may stand in for missing CRM signal
- manual briefing assembly is allowed
- project-home watchlists are allowed to hold blocked system state until contracts are wired

## Next move

Keep the briefing contract fed by runtime signals and continue replacing `NO_SIGNAL` sections with live business inputs where possible.
