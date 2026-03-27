# Agents Folder

This folder stays in the workspace root on purpose.

## What it is

`agents/` is a parent directory reserved for future isolated agent workspaces.

If multi-agent routing is reintroduced later, each subfolder here should be a real OpenClaw workspace for that agent, with its own bootstrap files such as:

- `AGENTS.md`
- `SOUL.md`
- `IDENTITY.md`
- `USER.md`
- `TOOLS.md`
- `HEARTBEAT.md`
- `memory/`

## What it is not

- not the bootstrap source for `main`
- not a shared-doc bucket
- not a place for live project artifacts
- not a fake internal lane fleet

## Current state

Right now the runtime is single-agent.

- live agent = workspace root `/Users/_xvadur/singularitas`
- founder-facing bootstrap files = root workspace files
- this folder is intentionally minimal until a real second isolated agent exists
