# Routing v1 Reference

## Canonical routing defaults

- Timezone: `Europe/Bratislava`
- Default owner topic: `#command-center`
- Single owner per packet: `true`
- Claim window: `5 minutes`
- Ownership adjudication SLA: `20 minutes`

## Lane roles

### Talker lanes
- `agent_orchestrator`
- `agent_sales_outreach`
- `agent_content_media`

### Worker lanes
- `agent_client_delivery`
- `agent_ai_recepcia`
- `agent_system_devops`
- `agent_finance_ops`
- `agent_voice_builder`
- `agent_voice_ops`
- `agent_biz_admin`

### Read-only lane
- `agent_research_intel`

## Routing rules

1. Default owner is the topic-bound agent.
2. Ambiguous ownership escalates to `agent_orchestrator`.
3. Cross-topic movement requires explicit handoff.
4. Silent lane switching is forbidden.

## Priority and concurrency defaults

### P0
- Ack SLA: `5 minutes`
- Max active per lane: `1`

### P1
- Ack SLA: `15 minutes`
- Max active per lane: `2`

### P2
- Ack SLA: `60 minutes`
- Max active per lane: `2`

## Watchdog defaults

- Enabled: `true`
- Interval: `10 minutes`
- Blocker escalation: `30 minutes`
- Max auto retries: `2`
- After retries: human unblock required

## Summary cadence

1. Post summary on state change.
2. Post heartbeat every `15 minutes`.
