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
- Do not let local notes here turn into policy, strategy, or memory
