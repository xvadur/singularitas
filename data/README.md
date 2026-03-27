# Operational Data

This tree isolates operational data from runtime doctrine.

- `connectors/` for raw pulls and connector-side machine state
- `imports/` for raw incoming data
- `normalized/` for machine-readable transformed state

Do not keep loose data files at the workspace root.
This tree is non-canonical support storage. It does not define business truth.
