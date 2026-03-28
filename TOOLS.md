# TOOLS.md - Local Cheat Sheet

Environment-specific execution notes only.

Skills define procedures.
Doctrine lives elsewhere.
This file is just the local cheat sheet.

## Path anchors

- Main runtime workspace: `/Users/_xvadur/singularitas`
- Founder raw capture layer: `/Users/_xvadur/singularitas_opus`
- Legacy business archive/import source: `/Users/_xvadur/firma`

## Runtime anchors

- Founder cockpit: `/Users/_xvadur/singularitas/control/cockpit`
- Daily control surface: `/Users/_xvadur/singularitas/control/daily`
- Canonical tasks: `/Users/_xvadur/singularitas/control/tasks`
- Canonical roadmaps: `/Users/_xvadur/singularitas/control/roadmaps`
- Canonical CRM: `/Users/_xvadur/singularitas/business/crm`

## Nerve ops

- Nerve project root: `/Users/_xvadur/openclaw-nerve`
- Nerve config file: `/Users/_xvadur/openclaw-nerve/.env`
- Nerve runtime data dir: `~/.nerve`
- Nerve kanban source of truth: `~/.nerve/kanban/tasks.json`
- Nerve device identity: `~/.nerve/device-identity.json`

Current local Nerve shape:
- `PORT=3080`
- `HOST=127.0.0.1`
- `GATEWAY_URL=http://127.0.0.1:19789`
- `NERVE_AUTH=false`
- `AGENT_NAME=Jarvis`

Operational rules:
- If a task should appear in the live Nerve board, write it to `~/.nerve/kanban/tasks.json`.
- Workspace markdown backlog files help planning, but do not auto-populate the live Nerve kanban.
- Treat Nerve as the cockpit in front of OpenClaw Gateway, not as the gateway itself.
- Keep the gateway on loopback when possible; Nerve proxies the browser connection.
- Do not expose Nerve to the network without intentionally configuring auth.

Useful Nerve commands:
- `cd /Users/_xvadur/openclaw-nerve && npm run setup`
- `cd /Users/_xvadur/openclaw-nerve && npm run setup -- --check`
- `cd /Users/_xvadur/openclaw-nerve && npm start`
- `cd /Users/_xvadur/openclaw-nerve && npm run dev`

Useful operating checks:
- first-time / broken-scope suspicion: verify `~/.nerve/device-identity.json` exists and re-approve device if needed
- if board items do not appear: check `~/.nerve/kanban/tasks.json` first, then refresh Nerve UI
- if auth/login behaves strangely: inspect `NERVE_AUTH` and related `.env` state before debugging the UI
- if connection fails: verify Nerve `.env`, then gateway reachability on `GATEWAY_URL`

Kanban / API note:
- board config is managed via Nerve REST API; docs mention `GET /api/kanban/config` and `PUT /api/kanban/config`
- task persistence itself lives in `~/.nerve/kanban/tasks.json`

## Telegram + voice

- Preferred voice reply path: `/tmp/openclaw/voice-reply.mp3`
- Do not use plain `/tmp/voice-reply.mp3` for Telegram replies
- `messages.tts` uses ElevenLabs in this profile
- Audio transcription order:
  - `workspace/systems/local-scripts/elevenlabs-stt.sh`
  - fallback: `workspace/systems/local-scripts/whisper-stt.sh`

## Google Workspace

- Personal account: `yksvadur.ja@gmail.com`
- Business account: `adam@xvadur.com`
- Personal auth root: `~/.config/gws`
- Business auth root: `~/.config/gws-xvadur`

## Skill paths

- Shared/global skills: npm-installed OpenClaw skill path
- Workspace-specific skills: `/Users/_xvadur/singularitas/skills`

## Known gotchas

- `singularitas` is now the canonical operational truth
- `singularitas_opus` is raw capture, journaling, and thinking, not runtime doctrine
- `firma` is no longer canonical truth for Jarvis; use it only as legacy source or archive input
- `agents/` is intentionally empty until a future isolated agent workspace is created
- Nerve kanban source of truth lives in `~/.nerve/kanban/tasks.json`
- If a task is supposed to appear in the Nerve board, write it to `~/.nerve/kanban/tasks.json`, not only to workspace markdown backlog files
- Do not let local notes here turn into policy, strategy, or memory
