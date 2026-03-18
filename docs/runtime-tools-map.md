# Tools Map

## Purpose

Map the core tool and integration families that the runtime must understand and reference.

## Operating assumptions

- file-first truth
- propose-first autonomy
- no silent live mutations
- degrade to internal artifact when a tool is unavailable

## Core tool families

| Family | Role | Primary Lane | Primary Source | Notes |
| --- | --- | --- | --- | --- |
| Artifact + project-home layer | File-backed operating truth | Jarvis / all | `singularitas/docs/workspace-overview.md` | Foundation for status, handoffs, specs |
| OpenClaw orchestration | Routing and execution discipline | Jarvis / ops | `singularitas/AGENTS.md` | Supervisory control plane |
| Telegram + ACP ingress | Persistent operator chat surface | Jarvis / ops | `singularitas/TOOLS.md` | Includes voice-path conventions |
| Linear | Execution visibility | Jarvis / growth / ops | `singularitas/skills/linear/SKILL.md` | Work tracking layer |
| Google Workspace | Mail, calendar, docs, sheets | Jarvis / growth | `singularitas/skills/google-workspace/SKILL.md` | Two-account model already exists |
| Research stack | Lead and business intelligence | research / growth | `singularitas/skills/lead-researcher/SKILL.md` | Discovery and qualification layer |
| Voice runtime | Voice deployments | voice / integration | `singularitas/skills/voice-factory/SKILL.md` | Vapi / ElevenLabs deployment subsystem |
| CRM memory | Contact state and follow-up memory | revenue / growth | `singularitas/skills/crm/SKILL.md` | Local CRM operating surface |
| n8n automation | Webhook and workflow layer | integration / ops | `singularitas/skills/n8n/SKILL.md` | Converts tool contracts into executable flows |
| Cloudflare | Domain / DNS / public edge | build / ops | `singularitas/skills/cloudflare-toolkit/SKILL.md` | Optional unless public web changes happen |

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

- `singularitas/projects/phone-first-engine/spec/pilot-workflow.md`
- `singularitas/projects/web-proof-engine/spec/site-engine-ia.md`
- `singularitas/projects/founder-cockpit/spec/current-system-contracts.md`
- `singularitas/systems/n8n.md`

## Cut line

Definitely in:
- tool family inventory
- source-of-truth pointers
- auth / env note surface
- runtime-ready references for phone-first, web-proof, and founder cockpit

Not here:
- archived legacy paths
- stale implementation scratch
- canonical business truth that belongs in `firma`
