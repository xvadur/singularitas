---
name: scout
description: "Find and qualify business leads for outbound sales using segment search, company lookup, Google Places, website enrichment, review signals, pain inference, offer-angle selection, and personalized outreach drafting. Use when the user wants to: (1) find companies in a segment or city, (2) look up a company by name, (3) enrich a lead from public data, (4) identify likely commercial pain points from reviews, websites, or contact flows, (5) prepare CRM-ready lead records, or (6) write personalized cold emails or messages based on observable gaps."
---

# Scout

## Overview

Use this skill to work like a commercial scout: source leads, enrich them from public signals, infer likely pains, choose the most credible offer angle, and prepare structured CRM-ready output plus personalized outreach.

Optimize for practical outbound motion, not research theater. Prefer a smaller set of high-signal leads with clear pain hypotheses over large noisy lists.

## Core workflow

### 1. Define the search brief

First force the request into a usable brief:
- segment or business type
- geography
- count target
- filters
- exclusion rules
- desired output format

If the user is vague, infer a practical default and say so briefly.

Good filters include:
- low rating
- low review count
- missing website
- weak contact flow
- solo owner or small team
- poor responsiveness signals
- no booking path
- outdated positioning

### 2. Source leads

Use the most direct source available.

Preferred source order:
1. Google Places / business listings
2. firm website
3. public directory pages
4. social/business profiles

For each lead, capture at minimum:
- company name
- location
- website
- phone
- category
- source URL or lookup basis

When the user gives a company name, treat the task as lookup + qualification:
- confirm the entity
- find website/contact details
- identify what they sell
- extract commercial signals relevant to outreach

### 3. Enrich the lead

Collect only data that helps sales judgment.

High-value enrichment fields:
- rating and review count
- review themes
- whether website exists
- whether website is modern or weak
- clear CTA present or absent
- booking/contact path quality
- phone visibility
- lead capture form quality
- opening hours / availability clues
- service scope
- likely buyer type
- signs of operator overload

Do not pretend certainty. Distinguish:
- observed fact
- plausible inference
- speculation

### 4. Infer the likely pain

Translate public signals into commercial pain hypotheses.

Common signal -> pain mappings:
- low rating + complaint themes -> reputation drag, lost trust, lower conversion
- many reviews mentioning slow callbacks / unreachability -> missed leads, revenue leakage
- no clear booking/contact path -> drop-off before contact
- poor or outdated website -> low trust, weak conversion, owner neglecting funnel
- solo operator / small team -> calls missed during delivery work
- many listings / inventory + weak responsiveness -> follow-up gap, lead decay
- no structured follow-up visible -> warm leads cooling off

For Xvadur-style offers, bias toward pains tied to:
- missed calls
- slow lead response
- booking loss
- follow-up failure
- dependence on one person answering the phone

### 5. Choose the offer angle

Match the angle to the gap.

Examples:
- missed-call risk -> “Every unanswered call is a lead leak.”
- slow response -> “You are paying acquisition cost for leads that cool off before contact.”
- weak booking flow -> “Make contact immediate instead of hoping people try again.”
- overload on owner -> “The phone should not depend on whether you are free right now.”
- poor review/reachability signals -> “Fix the operational problem behind the reputation issue.”

Do not oversell product scope. Default to a simple pilot framing unless the user asks otherwise.

### 6. Draft outreach

Write outreach from evidence, not generic flattery.

Rules:
- reference one specific observable signal
- connect it to one likely business consequence
- make one concrete offer
- keep it short
- avoid AI buzzwords unless the user explicitly wants them

Useful structure:
1. personalization from an observed signal
2. pain hypothesis
3. simple offer
4. low-friction CTA

### 7. Prepare CRM-ready output

Always structure the result so it can be copied into a CRM or sheet.

Default columns:
- company_name
- segment
- city
- website
- phone
- source
- rating
- review_count
- key_signal
- pain_hypothesis
- offer_angle
- buyer_guess
- priority
- personalization_note
- outreach_draft

If the user asks for “write to CRM,” prepare the data in a compact table-like bullet list or CSV-style block unless a specific CRM format is provided.

## Output standard

For each lead, prefer this compact structure:
- Lead: company + location
- Facts: website / phone / rating / review count / notable public signals
- Likely pain: short hypothesis
- Why this matters: commercial consequence
- Offer angle: what to pitch
- Personalization: sentence fragment usable in outreach
- Outreach draft: 4-7 sentence version or shorter if volume matters
- CRM fields: structured row

For larger batches:
- summarize top patterns first
- then list leads
- keep outreach concise
- avoid long prose per lead unless the user asked for depth

## Quality bar

A good scout output should help the user decide who to contact next.

Prioritize:
- closability over curiosity
- observable evidence over cleverness
- pain tied to money over vague “optimization”
- narrow, usable personalization over generic templates

## Guardrails

- Do not invent facts that were not observed.
- Mark inferred pain as a hypothesis.
- Do not claim a company is losing money in a quantified way unless the data supports it.
- Do not scrape aggressively when a few high-signal examples are enough.
- Prefer fewer, better leads to bulk noise.

## Tool stack integration

Use this skill as the orchestration layer above Google tools.

### Google Places (`goplaces`)

Use `goplaces` as the default sourcing and lookup layer when the task involves:
- finding businesses by segment and city
- filtering by rating or review count
- checking place details and reviews
- resolving a company name into a concrete business entity

Preferred usage pattern:
1. search by segment + city
2. filter for signal quality (rating, review count, obvious fit)
3. fetch details for shortlisted leads
4. inspect reviews only when they help infer pain or personalization

Use JSON output when the task is batch-oriented or needs structured extraction.

Typical use cases:
- “Find 10 real estate agents in Bratislava with low ratings.”
- “Look up this company name and tell me if it is a fit.”
- “Find hotels in Brno with weak reviews and websites worth checking.”

### Google Workspace (`gog`)

Use `gog` as the execution layer after sourcing/enrichment.

Primary uses:
- Google Sheets for CRM-style lead storage
- Gmail for draft creation and approved sending
- Docs/Drive for shared notes, templates, or exports

Preferred workflow:
1. source and qualify leads
2. enrich from web / reviews / website
3. prepare structured fields
4. write rows into Sheets
5. draft personalized Gmail outreach
6. send only after explicit user confirmation

Default rule: draft freely, send only with confirmation.

## Xvadur scout workflow

For Xvadur-style outbound, follow this operational order:
1. source from Google Places
2. shortlist by fit and pain signals
3. inspect website/contact flow
4. infer likely pain tied to calls, lead response, booking loss, or follow-up failure
5. select offer angle
6. prepare CRM row for Google Sheets
7. prepare Gmail draft

When multiple leads are requested, keep a tight loop:
- search in batches
- enrich only the best candidates
- avoid deep research on weak-fit leads
- optimize for next-action readiness

## References

If needed, read `references/output-template.md` for a reusable lead record template and batch output shape.
