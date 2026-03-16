# TOOLS.md - Local Notes

This file is for environment-specific notes only.

Skills define procedures.
Doctrine lives in core files.
`TOOLS.md` is the local cheat sheet.

## What belongs here

Put only setup-specific details that help execution, such as:

- local file paths
- device nicknames
- SSH aliases / host labels
- preferred TTS voices
- camera names
- temp-file conventions
- local CLI quirks
- environment-specific workarounds

## What does not belong here

Do not turn this file into:
- a second `AGENTS.md`
- a policy file
- a strategy document
- a skill spec
- a memory dump
- a general tutorial

If the note is durable doctrine, put it in:
- `AGENTS.md`
- `IDENTITY.md`
- `SOUL.md`
- `USER.md`
- `docs/`
- `MEMORY.md`

## Use style

Keep entries:
- short
- practical
- local
- easy to scan

Prefer bullets over prose.

---

## Rescue notes

### Telegram + voice

- Preferred voice reply path: `/tmp/openclaw/voice-reply.mp3`
- Do not use plain `/tmp/voice-reply.mp3` for Telegram replies.
- `messages.tts` uses ElevenLabs in this profile.
- Audio transcription order in this profile:
  - `workspace/systems/local-scripts/elevenlabs-stt.sh`
  - fallback: `workspace/systems/local-scripts/whisper-stt.sh`

### Workspace reality

- Authoritative runtime workspace: `/Users/_xvadur/singularitas`
- Obsidian knowledge home: `/Users/_xvadur/singularitas_opus`

### Google Workspace accounts

- Personal account: `yksvadur.ja@gmail.com`
- Business account: `adam@xvadur.com`
- Personal auth root: `~/.config/gws`
- Business auth root: `~/.config/gws-xvadur`

### Skill hygiene

- Shared/global skills live under the npm-installed OpenClaw skill path.
- Workspace-specific skills live under `/Users/_xvadur/singularitas/skills`.
- Retired skills were moved out of the active system on 2026-03-14; do not assume old wrapper skills still exist.
