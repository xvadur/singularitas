# Marek / realitky — Tools

## Purpose

This document explains the runtime action surface for Marek.
It exists so prompt work, review work, and backend work all refer to the same operational model.

## Two runtime shapes currently exist

### A. Current live/staged 5-tool surface
This is the currently evidenced live shape on `realitky`.
Attached tools:
- `log_lead_progress`
- `check_availability`
- `create_appointment`
- `handoff_urgent`
- `finalize_call`

This surface maps to the current production-compatible n8n gateway package in:
- `outputs/marek-n8n-backend-v2/`

### B. Cleaned target single-tool surface
This is the cleaner proposed target contract.
Public tool:
- `a10_control`

This surface uses one field, `action`, to express the needed backend behavior.

## Current canonical working rule

For project documentation and review work, keep both visible.
For live-runtime claims, do **not** pretend the single-tool contract is already the current live reality unless explicitly revalidated.

## 5-tool surface meaning

### `log_lead_progress`
Use when the caller is understood enough to store or update the lead record.

### `check_availability`
Use when the caller wants a callback or viewing in a concrete time window and the slot must be verified.

### `create_appointment`
Use only after the time is specific and should be written to the calendar/backend.

### `handoff_urgent`
Use when the lead is urgent, high-value, referral-based, or should be escalated quickly.

### `finalize_call`
Use at the end of the call to close the trace with the correct outcome.

## Single-tool target meaning

In the cleaned target model, the assistant should think in terms of one backend capability:
- `a10_control`

Allowed actions:
- `log_lead`
- `check_availability`
- `create_appointment`
- `handoff_urgent`
- `finalize_call`

This is founder-readable and easier to maintain.

## Core business rules currently associated with the backend

These belong in backend logic, not spoken improvisation:
- callback duration = `15 min`
- viewing duration = `60 min`
- working hours = `08:00–19:00`
- lunch block = `12:00–13:00`
- weekends allowed
- callbacks cannot overlap with viewings
- Bratislava logistics buffers apply
- when slot is unavailable, return `3 nearest alternatives`

## Project rule

Never describe Marek as having a clean single-tool runtime unless that is the currently locked deployment contract.
Until then, the safe description is:
- live/staged runtime evidence points to the 5-tool surface
- cleaned target direction points to `a10_control`
