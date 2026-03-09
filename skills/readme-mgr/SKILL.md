---
name: readme-mgr
description: Manage Singularitas README generation/maintenance and optional integration with readme-md-generator.
user-invocable: true
metadata:
  {
    "openclaw": {
      "requires": {
        "bins": ["bash", "npx"]
      },
      "emoji": "🧾"
    }
  }
---

# README manager

Primary goal: keep `README.md` coherent, branded, and commit-friendly.

## Usage
- `/readme` or `/readme refresh` → run generator candidate flow (non-destructive)
- `/readme status` → show current file summary and quick diff against generated candidate if present

## Behavior
1. Prefer manual branding sections in `README.md` as source of truth.
2. Do not overwrite creative sections unless explicitly asked.
3. For generator flow, use local script:
   - `./scripts/readme-refresh.sh`
4. If `README.generated.md` is created, inspect it first and merge manually.

## Constraints
- Never remove core blocks like identity/discipline/commit workflow unless explicitly approved.
- Keep `.md` image assets and branding intentionally visible.
