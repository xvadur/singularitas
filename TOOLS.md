# TOOLS.md - Local Cheat Sheet

Environment-specific execution notes only.

Skills define procedures.
Doctrine lives elsewhere.
This file is just the local cheat sheet.

## Path anchors

- Main runtime workspace: `/Users/_xvadur/singularitas`
- Obsidian knowledge/input layer: `/Users/_xvadur/singularitas_opus`
- Business workspace: `/Users/_xvadur/firma`

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
- Retired wrapper skills were removed on `2026-03-14`; do not assume old aliases still exist

## Known gotchas

- `singularitas` = runtime source of truth
- `singularitas_opus` = shared writable knowledge/input layer, not runtime doctrine
- `firma` = live business truth + output layer
- Do not let local notes here turn into policy, strategy, or memory
