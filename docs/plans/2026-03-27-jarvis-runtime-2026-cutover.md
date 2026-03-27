# Jarvis Runtime 2026 Cutover

This cutover establishes:

- `singularitas` as canonical truth
- `control/` as founder cockpit
- `personal/` and `business/` as canonical operational layers
- `projects/` as initiative-only execution space
- `firma` as legacy import source
- `singularitas_opus` as raw capture only

Primary migration buckets:

- extract `studio/*` into `docs/playbooks/`, `systems/`, `outputs/`
- extract `docs/voice/*` into `business/voice/`
- retire `projects/founder-cockpit` as the default founder entrypoint
- reduce live `skills/` to the curated runtime set
