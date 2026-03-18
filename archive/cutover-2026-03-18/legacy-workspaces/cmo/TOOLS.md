# TOOLS.md - Local Notes

Skills define _how_ tools work. This file is for _your_ specifics — the stuff that's unique to your setup.

## What Goes Here

Things like:

- Camera names and locations
- SSH hosts and aliases
- Preferred voices for TTS
- Speaker/room names
- Device nicknames
- Anything environment-specific

## Examples

```markdown
### Cameras

- living-room → Main area, 180° wide angle
- front-door → Entrance, motion-triggered

### SSH

- home-server → 192.168.1.100, user: admin

### TTS

- Preferred voice: "Nova" (warm, slightly British)
- Default speaker: Kitchen HomePod
```

## Why Separate?

Skills are shared. Your setup is yours. Keeping them apart means you can update skills without losing your notes, and share skills without leaking your infrastructure.

---

Add whatever helps you do your job. This is your cheat sheet.

## Rescue Notes

### Telegram + Voice

- Preferred voice reply path: `/tmp/openclaw/voice-reply.mp3`
- Do not use plain `/tmp/voice-reply.mp3` for Telegram replies.
- `messages.tts` uses ElevenLabs in this profile.
- Audio transcription order in this profile:
  - `workspace/systems/local-scripts/elevenlabs-stt.sh`
  - fallback: `workspace/systems/local-scripts/whisper-stt.sh`

### Cloudflare

- Preferred Cloudflare skill: `/Users/_xvadur/singularitas/skills/cloudflare-toolkit`
- Main script: `/Users/_xvadur/singularitas/skills/cloudflare-toolkit/scripts/cf.sh`
- Requires env: `CLOUDFLARE_API_TOKEN`
- Optional for tunnel ops: `CLOUDFLARE_ACCOUNT_ID`
- Managed domain context: `jozef.xvadur.com`
- Use this skill first for Cloudflare DNS / SSL / settings / tunnel checks before ad-hoc methods.
