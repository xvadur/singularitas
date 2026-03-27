---
name: youtube-transcript
description: Extract YouTube transcript and convert it into summary/tasks/notes with deterministic output files.
---

# YouTube Transcript

## Run

```bash
python3 scripts/youtube_transcript.py "<youtube-url>" --lang sk,en --out /tmp/transcript.md
```

## Default post-processing outputs

- concise summary
- action items
- publish notes (if content workflow)

Preferred long-term save path:
- `/Users/_xvadur/singularitas/projects/singularity/content/`
