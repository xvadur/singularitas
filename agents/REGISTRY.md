# Runtime Registry

Founder-readable map of the active runtime.

## Main Workspace

- `jarvis` → `/Users/_xvadur/singularitas`
- Role: chief of staff, approval surface, priority arbitration, layer routing, founder briefing
- Main duties:
  - reconcile personal and business priorities
  - identify the single best next move
  - escalate decisions that carry commercial, publishing, or production risk
- Allowed outputs: priorities, approvals, handoffs, reviews, founder-facing synthesis

## Personal Layer

### `personal-ops`

- Path: `/Users/_xvadur/singularitas/agents/personal-ops`
- Mission: Adam's commitments, inbox triage, personal capture normalization, reminders, personal queue hygiene
- Inputs: calendar state, inbox state, personal tasks, Obsidian capture, daily notes
- Allowed outputs: daily agenda packets, reminders, task queues, capture normalization notes

### `personal-web`

- Path: `/Users/_xvadur/singularitas/agents/personal-web`
- Mission: personal website stewardship, drift detection, maintenance packets, upgrade proposals
- Inputs: site issues, stale copy, analytics signal, publishing backlog, maintenance requests
- Allowed outputs: patch packets, content drafts, maintenance checklists, approval-ready change proposals

## Business Layer

### `revenue`

- Path: `/Users/_xvadur/singularitas/agents/revenue`
- Mission: lead generation, outreach, follow-up, call prep, pipeline movement, pilot proposals
- Inputs: pipeline state, reply rate, lead batches, call outcomes, proof assets
- Allowed outputs: lead queues, outreach drafts, follow-up packets, pilot proposals, revenue reviews

### `voice`

- Path: `/Users/_xvadur/singularitas/agents/voice`
- Mission: phone-first assistant design, runtime tuning, call flows, QA, callback logic
- Inputs: deployment specs, call transcripts, call outcomes, objection logs, carrier constraints
- Allowed outputs: voice specs, prompt packets, QA findings, callback-flow updates, deployment recommendations

### `integration`

- Path: `/Users/_xvadur/singularitas/agents/integration`
- Mission: n8n, CRM writes, booking flows, SIP/carrier glue, MCP/connectors, webhooks
- Inputs: system contracts, workflow failures, connector opportunities, deployment requirements
- Allowed outputs: integration packets, runbooks, connector specs, workflow repair queues, partner feasibility notes

### `delivery`

- Path: `/Users/_xvadur/singularitas/agents/delivery`
- Mission: onboarding, scope enforcement, rollout tracking, validation, weekly status
- Inputs: won deals, deployment packets, project status, blockers, validation criteria
- Allowed outputs: onboarding packets, rollout plans, validation packets, weekly status summaries, delivery escalations

### `proof`

- Path: `/Users/_xvadur/singularitas/agents/proof`
- Mission: before/after, case notes, objections learned, proof extraction, sales artifacts
- Inputs: call outcomes, delivery learnings, wins, objections, screenshots, transcripts
- Allowed outputs: proof packets, case notes, objection updates, proof blocks, content-ready shards

### `web`

- Path: `/Users/_xvadur/singularitas/agents/web`
- Mission: Xvadur public web surfaces, proof pages, content packaging, website ops
- Inputs: proof assets, landing requirements, content backlog, site analytics, web maintenance requests
- Allowed outputs: page change packets, content drafts, publish queues, site ops checklists, CTA improvement proposals

## Support Execution Lanes

### `research`

- Path: `/Users/_xvadur/singularitas/agents/research`
- Mission: market research, prospect intelligence, general knowledge gathering

### `growth`

- Path: `/Users/_xvadur/singularitas/agents/growth`
- Mission: message shaping, outreach support, CRM hygiene, offer and website refresh proposals

### `build`

- Path: `/Users/_xvadur/singularitas/agents/build`
- Mission: frontend, backend, product implementation, technical polish

### `ops`

- Path: `/Users/_xvadur/singularitas/agents/ops`
- Mission: delivery systems, automations, runtime operations, operational runbooks

### `janitor`

- Path: `/Users/_xvadur/singularitas/agents/janitor`
- Mission: hygiene, drift detection, missing-record alerts, cleanup coverage

## Operating Rules

- Personal layer owns Adam-facing commitments, personal web stewardship, and personal capture normalization.
- Business layer owns pipeline, deployments, proof, business web/content, and client systems.
- Shared objects are readable across the runtime, but write ownership must stay explicit.
- Canonical ingress model: `default -> jarvis`.
- Compatibility bridge (legacy Telegram aliases) may remain active only for migration continuity: `cso -> research`, `cro -> revenue`, `cmo -> web`, `coo -> integration`.
- Canonical owners are always reached through Jarvis dispatch unless a legacy bridge alias is explicitly configured for temporary compatibility.
- The primary revenue engine is phone-first deployments.
- The parallel engine is web/content/proof systems.
- Vendor/MCP/connectors are opportunistic and should not silently cannibalize phone-first revenue execution.
- No lane performs risky outbound, publishing, or production changes by default; lanes prepare packets, tasks, and patches for review.
