# Approval Schema v1

## Purpose

Gate 2 actions remain locked until Adam provides an explicit approval payload.

## Gate 2 scopes

- `outbound_send`
- `production_change`
- `financial_commitment`
- `legal_or_public_claim`
- `destructive_action`

## Required fields

- `TYPE:approval`
- `ACTION_ID:<action-id>`
- `APPROVED_BY:Adam`
- `APPROVAL_TOKEN:<token>`
- `AT:<ISO-8601 timestamp>`
- `SCOPE:<scope>`

## Token format

- Pattern: `APR-YYYYMMDD-<ACTION_ID>-<HEX6_12>`
- Regex: `^APR-[0-9]{8}-[a-z0-9\\-]+-[a-f0-9]{6,12}$`

## Example

```text
[TYPE:approval] ACTION_ID:deploy-2026-03-06-01 APPROVED_BY:Adam
APPROVAL_TOKEN:APR-20260306-deploy-2026-03-06-01-a1b2c3d4
AT:2026-03-06T09:14:00+01:00
SCOPE:production_change
```

## Validation rules

1. Missing or invalid token means approval rejected.
2. `APPROVED_BY` must be exactly `Adam`.
3. `ACTION_ID` must map to one pending action or packet.
4. The approval token is single-use for that action.
