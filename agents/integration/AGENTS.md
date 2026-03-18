# AGENTS.md - Integration Workspace

This workspace is home for the `integration` agent.

Use it for:
- n8n
- CRM writes
- booking flows
- SIP/carrier glue
- MCP/connectors
- webhooks

Startup discipline:
1. Read `SOUL.md`.
2. Read `IDENTITY.md`.
3. Read `USER.md`.
4. Read `HEARTBEAT.md`.
5. Read `MEMORY.md`.
6. Read the relevant contracts, workflow specs, and project files.

Rules:
- Prefer explicit contracts and runbooks over hidden glue.
- Keep risky external writes gated behind approval.
- Do not let connector work cannibalize the primary revenue engine.
