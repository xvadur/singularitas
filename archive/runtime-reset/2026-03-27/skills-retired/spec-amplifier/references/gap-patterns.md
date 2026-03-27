# Gap Patterns

Use this file to spot likely missing dimensions by task type.
Use only the relevant subset.
Do not dump the whole checklist into the reply.

## App / Web App

Check for:
- target user
- core action / success event
- auth or no auth
- roles / permissions
- key entities and data model
- empty states
- failure states
- mobile vs desktop priority
- admin needs
- analytics / tracking
- deployment target
- MVP boundary

## Automation / Workflow / API Integration

Check for:
- source trigger
- destination system
- required fields
- idempotency / duplicate handling
- retries / failure handling
- auth and secret storage
- logging / observability
- manual fallback
- rate limits
- ownership of errors

## Agent / Skill / Assistant

Check for:
- primary job to be done
- allowed vs forbidden actions
- channel / runtime
- escalation path
- tool availability
- memory / state expectations
- output contract
- QA or acceptance examples
- tone / audience if externally facing

## Offer / Service / Sales Asset

Check for:
- buyer / segment
- pain being solved
- promised outcome
- proof level
- risk reversal
- CTA
- what is intentionally out of scope
- delivery shape

## Content / Document / Brief

Check for:
- audience
- objective
- tone
- length / depth
- source material
- must-include points
- must-avoid points
- final format
- review standard

## Infra / Deployment / Production Change

Check for:
- environment
- rollback shape
- secrets
- data persistence
- monitoring
- downtime tolerance
- backup / restore
- access control
- blast radius
- verification method

## Data / Research / Analysis

Check for:
- question being answered
- source of truth
- freshness needs
- output format
- confidence bar
- exclusions
- success threshold
- next decision enabled by the analysis
