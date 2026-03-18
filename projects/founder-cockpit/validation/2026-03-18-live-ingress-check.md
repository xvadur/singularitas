# 2026-03-18 Live Ingress Check

## Scope

Gate 1 only: prove that founder traffic can reach `Jarvis (main)` through the live Telegram ingress path.

This file does not claim live proof. It records the current evidence, the exact test to run, and the blocker if live transport cannot be exercised from this workspace.

## Current evidence

Config-level evidence already supports the intended route:

- `~/.openclaw/openclaw.json` reports `defaultAccount=default`
- route bindings in that file map:
  - `default -> main` (canonical)
  - `cso -> research` (compat legacy)
  - `cro -> revenue` (compat legacy)
  - `cmo -> web` (compat legacy)
  - `coo -> integration` (compat legacy)
- the same config reports `agents with workspaces=13`

Supporting repo evidence:

- [Runtime route bridge](/Users/_xvadur/singularitas/projects/founder-cockpit/spec/runtime-route-bridge.md)
- [Current system contracts](/Users/_xvadur/singularitas/projects/founder-cockpit/spec/current-system-contracts.md)
- [Startup contract](/Users/_xvadur/singularitas/projects/founder-cockpit/spec/startup-contract.md)
- [Jarvis usability checklist v1](/Users/_xvadur/singularitas/projects/founder-cockpit/validation/2026-03-18-jarvis-usability-checklist-v1.md)
- [Runtime smoke test](/Users/_xvadur/singularitas/projects/founder-cockpit/validation/2026-03-18-runtime-smoke-test.md)

## Exact live test steps

Run these steps in a real Telegram session from the default founder ingress surface:

1. Send: `ping jarvis live ingress 2026-03-18`
2. Confirm the message lands in `Jarvis` via `OpenClaw`
3. Confirm the reply is short, verdict-first, and uses current founder-cockpit context
4. Confirm the reply does not fall back to legacy C-level framing
5. Record the reply timestamp, agent name, and the exact wording of the response

If the live session is available, the reply should also be checked against the startup contract:

- startup reads are loaded in the documented order
- the default founder briefing surface is named correctly
- output routing matches object type

## Pass criteria

- A real Telegram message reaches `Jarvis (main)` through OpenClaw
- The reply is generated in the new Jarvis posture
- The reply references the active founder-cockpit context instead of generic filler
- The session can be traced back to the config route `default -> main`

## Fail criteria

- No reply arrives
- The wrong agent answers
- The reply ignores founder-cockpit context
- The message can only be proven at config level, not as a live Telegram delivery

## Blocker notes

Live transport is still blocked from this workspace because I do not have a documented, safe local mechanism to emit a real Telegram message from here.

That means the current state is:

- route bridge: proven in config
- startup contract: written
- live ingress: not yet exercised

## Recommended next move

Use a real founder Telegram DM or the existing OpenClaw-supported ingress surface to send the exact test message above, then capture the reply as a live session record.

If the live path still cannot be triggered, the next verification step is to identify the documented Telegram send surface in the OpenClaw runtime and test only that path, not an ad hoc workaround.
