# Google Stack Reference for Scout

Use this reference when the task should run through the Google-based scouting stack.

## Stack roles

### `goplaces` = sourcing
Use for:
- text search by segment/city
- company lookup by name
- rating/review filtering
- details and review retrieval

Good fit for:
- local services
- hotels/accommodation
- real estate agencies/agents
- high-phone-volume small businesses

## `gog` = execution
Use for:
- writing leads into Google Sheets
- creating Gmail drafts
- exporting or reading Google Docs
- simple contact or document workflows inside Google Workspace

## Suggested pipeline

1. Search in `goplaces`
2. Shortlist high-signal leads
3. Check website and contact flow
4. Infer likely pain hypothesis
5. Create offer angle and personalization note
6. Write lead into Google Sheets via `gog sheets append`
7. Create outreach draft via `gog gmail drafts create`

## Suggested sheet columns

- created_at
- segment
- city
- company_name
- website
- phone
- google_rating
- google_review_count
- key_signal
- pain_hypothesis
- offer_angle
- buyer_guess
- personalization_note
- outreach_status
- draft_subject
- priority
- source

## Usage notes

- Use `goplaces --json` for structured batches.
- Keep review reading selective; only read enough to identify pattern signals.
- In Gmail, create drafts before sending.
- In Sheets, prefer append for lead capture and update only when tracking progress.
- Keep pain statements hypothesis-based unless directly evidenced.
