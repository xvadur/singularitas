# Research Surfaces Inventory

Use this file as the durable inventory for the major surfaces owned by `research`.

## Fields to maintain per surface
- surface name
- purpose
- current stage
- current truth
- known blockers
- validation state
- next move
- canonical sources

## Surfaces

### `natural20-live-top10`
- purpose: rolling top-10 Natural20 intelligence view for hourly monitoring and rapid founder queries about recent changes
- current stage: `bootstrap-installed`
- current truth: file contract exists; first live monitor run still needs to populate it
- known blockers: diff/update logic still lives in the scheduled run prompt rather than a dedicated script
- validation state: `PARTIAL`
- next move: run a first live update and verify the rolling state plus daily log output
- canonical sources:
  - `/Users/_xvadur/singularitas/studio/research/inventory/natural20-live-top10.md`
  - `/Users/_xvadur/singularitas/studio/research/daily/2026-03-26-natural20-brief.md`
  - `https://natural20.com/api/feed`
