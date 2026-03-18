# n8n

Canonical system note for Xvadur automation work.

## Purpose

Keep one clean note for the current `n8n` surface, access model, and workflow conventions.

## Current knowns

- Base URL: TODO
- Auth source: `N8N_BASE_URL` + `N8N_API_KEY`
- Primary role: webhook and automation workflow execution
- Related surfaces: Vapi, ElevenLabs, internal tool contracts

## Tomorrow's goals

- confirm instance access
- confirm naming conventions
- confirm test/validation path
- identify first workflow to set up or verify

## Workflow naming

Default pattern:
- `<surface>-<use-case>-<environment>`

Examples:
- `voice-realtor-intake-staging`
- `site-content-publish-staging`

## Validation

Every workflow should have:
- trigger description
- expected input
- expected output
- failure path
- owner
- test evidence

## Unknowns to resolve

- exact instance URL
- environment split
- current live workflows
- logging/monitoring expectations
