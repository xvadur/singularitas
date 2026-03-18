# Operational Data

This tree isolates operational data from runtime doctrine.

- `crm/` for active CRM databases and exports
- `imports/` for raw incoming data
- `runs/` for generated run artifacts and reports
- `tmp/` for disposable working files
- `archive/` for superseded data worth keeping

Do not keep loose data files at the workspace root.
This tree is non-canonical support storage. It does not define business truth.
