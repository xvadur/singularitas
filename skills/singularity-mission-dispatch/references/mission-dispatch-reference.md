# Mission Dispatch Reference

## Minimal payload template
```json
{
  "mission_id": "voice-agent-delivery-20260306-02",
  "objective": "Ship voice agent readiness for Monday pilot",
  "priority": "P1",
  "deadline": "2026-03-06T17:00:00+01:00",
  "mission_type": "voice_delivery",
  "success_criteria": [
    "Voice flow stable",
    "No P0 blockers",
    "Linear packets created"
  ],
  "constraints": [
    "No production/destructive action without approval token"
  ],
  "requested_by": "Adam"
}
```

## Packet contract summary

Required packet fields:

- `packet_id`
- `mission_id`
- `owner_lane`
- `objective`
- `scope_in`
- `scope_out`
- `deadline`
- `priority`
- `dod`
- `constraints`
- `idempotency_key`

Required result block:

- `Done`
- `Evidence`
- `Blocked`
- `Next`
- `Risks/assumptions`
- `Rollback note`

## Handoff rules

1. Cross-lane work requires explicit handoff.
2. Receiver must ACK the handoff.
3. Same `idempotency_key` updates the existing packet, not a new one.
4. Ownership conflict after `5 minutes` escalates to `agent_orchestrator`.

## Health checks
```bash
cd /Users/_xvadur/singularitas/projects/singularity/runtime
npm test
npm run dispatch -- ./examples/mission.voice.json
npm run watchdog -- ./examples/packets.blocked.json
```

## Typical outcomes
- `linearSync.mode = dry` -> missing Linear env
- `recap skipped` -> missing `SINGULARITY_TELEGRAM_TARGET`
- packet `approval_pending` -> needs Gate 2 approval
