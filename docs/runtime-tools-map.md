# Tools Map

## Purpose

Map the core tool and integration families that the runtime must understand and reference.

## Operating assumptions

- file-first truth
- propose-first autonomy
- no silent live mutations
- degrade to internal artifact when a tool is unavailable

## Tonight tool families

| Family | Role Tonight | Primary Lane | Primary Source | Notes |
| --- | --- | --- | --- | --- |
| Artifact + project-home layer | File-backed operating truth | Jarvis / all | `singularitas/docs/workspace-overview.md` | Foundation for status, handoffs, specs |
| OpenClaw orchestration | Routing and execution discipline | Jarvis / ops | `singularitas/business/operations/openclaw-operating-runbook.md` | Supervisory control plane |
| Telegram + ACP ingress | Persistent operator chat surface | Jarvis / ops | `singularitas/TOOLS.md` | Includes voice-path conventions |
| Linear | Execution visibility | Jarvis / growth / ops | `singularitas/skills/linear/SKILL.md` | Work tracking layer |
| Google Workspace | Mail, calendar, docs, sheets | Jarvis / growth | `singularitas/skills/google-workspace/SKILL.md` | Two-account model already exists |
| Scout / research stack | Lead and business intelligence | research / growth | `singularitas/agents/cso/skills/scout/SKILL.md` | Strong enrichment and outreach support pattern |
| Voice runtime | Voice deployments | build / ops | `singularitas/skills/voice-factory/SKILL.md` | Vapi/ElevenLabs deployment subsystem |
| n8n automation | Webhook and workflow layer | ops | `singularitas/skills/n8n/SKILL.md` | Converts tool contracts into executable flows |
| Cloudflare | Domain/DNS/public edge | build / ops | `singularitas/skills/cloudflare-toolkit/SKILL.md` | Optional unless public web changes happen |

## Family details

### Artifact + mission-home layer
- What it does: stores runtime mission status, specs, staging, and handoffs
- Runtime usage: keep `singularitas` file-first from day one
- Later: promote action-bearing records into `firma`

### OpenClaw orchestration
- What it does: controls routing, review, and bounded execution
- Tonight usage: define behavior expectations, not a full app layer
- Later: connect more deeply to workflow graphs

### Telegram + ACP ingress
- What it does: persistent operator chat entry
- Tonight usage: note it as a core ingress surface
- Later: formal deep-linking and approval actions

### Linear
- What it does: visible execution tracking
- Tonight usage: map as a tool family, not as the only source of truth
- Later: define exact object sync policy

### Google Workspace
- What it does: email, calendar, docs, sheets
- Tonight usage: capture auth roots and role in business OS
- Later: formalize approval and automation flows

### Scout / research stack
- What it does: prospecting, enrichment, pain inference
- Tonight usage: mark as a reusable reference subsystem
- Later: extract canonical research pack contracts

### Voice runtime
- What it does: phone/voice deploys with testing patterns
- Tonight usage: mark as one of the strongest mature deploy surfaces
- Later: anchor seed voice workflow here

### n8n automation
- What it does: webhook and backend workflow execution
- Tonight usage: prepare tomorrow's setup and naming discipline
- Later: formalize live/staging boundary

### Cloudflare
- What it does: domain, DNS, tunnel, and public edge work
- Tonight usage: optional family only
- Later: activate when site/domain work enters scope

## Credentials and environment

- `N8N_BASE_URL`
- `N8N_API_KEY`
- `VAPI_API_KEY`
- `ELEVENLABS_API_KEY`
- `CLOUDFLARE_API_TOKEN`
- Google auth roots:
  - `~/.config/gws`
  - `~/.config/gws-xvadur`

## Strong contract references

- `singularitas/business/segments/ecommerce-agent-tools-contracts.md`
- `singularitas/business/segments/ecommerce-agent-n8n-ready-checklist.md`
- `singularitas/skills/voice-factory/references/vapi-build-system.md`

## Tonight cut line

Definitely in:
- tool family inventory
- source-of-truth pointers
- auth/env note surface
- readiness for `jozef.xvadur.com` and `n8n`

Optional:
- Cloudflare if web edge changes are needed tomorrow

Not tonight:
- full capability matrix
- live integration mutation
- secrets migration
