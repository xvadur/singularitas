# Integration Runtime Surfaces Inventory

Use this file as the durable inventory for the major integration surfaces owned by `integration`.

## Fields to maintain per surface
- surface name
- purpose
- platform
- current stage (`design` | `staged` | `partial-validation` | `live` | `stale`)
- current truth
- known blockers
- last validation state
- next move
- canonical sources

---

## Surface: Marek / realitky webhook gateway
- purpose: receive ElevenLabs webhook tool calls and bridge them into scheduling, logging, and handoff actions
- platform: n8n cloud
- current stage: `partial-validation`
- current truth:
  - n8n cloud root is reachable
  - health endpoint responds
  - public webhook paths are reachable at the platform surface
  - end-to-end POST behavior is not yet founder-readably confirmed
- known blockers:
  - workflow activation state not yet explicitly inventoried here
  - live write behavior still partially unverified
- last validation state: `safe read-only probe`
- next move:
  - inspect workflow activation state directly
  - run one bounded safe POST validation once write behavior is agreed
- canonical sources:
  - `studio/integration/daily/2026-03-25-integration-snapshot.md`
  - `studio/voice-factory/daily/2026-03-25-marek-runtime-validation-result.md`
  - `outputs/runtime-handoffs/2026-03-22-marek-elevenlabs-to-n8n.md`
