# Xvadur E-commerce Outbound Engine v1 - Pain Scoring And Personalization Rules

Locked scope: autodiely / pneuservis / support-heavy e-commerce only. These rules are for lightweight v1 research and outreach selection, not for building a heavy scoring system.

## Canonical inputs

- Upstream scoring source: `/Users/_xvadur/singularitas/agents/cso/sk-autodiely-pneu-enriched-v2.csv`
- Current batch reference: `/Users/_xvadur/singularitas/agents/cso/sk-autodiely-pneu-top10-outreach.csv`

Use these fields first:

- `segment`
- `mode`
- `pain_hypothesis`
- `notes`
- `review_snippet_1`
- `review_snippet_2`
- `chat_signal`
- `platform_guess`
- `has_faq`
- `has_reklamacie`
- `support_channel_count`
- `contact_page_url`
- `faq_url`
- `reklamacie_url`
- `personalization_hook`
- `reklamacie_support_pain`
- `reklamacie_complexity`

## Pain categories

### 1. Compatibility / pre-sale repetition

Use when the lead visibly sits in autodiely or pneuservis and signals repeated questions about:

- compatibility or fitment
- stock / availability
- delivery timing
- basic product choice or next step

Typical evidence:

- `segment = autodiely`
- `mode = phone-heavy` or `mixed`
- `pain_hypothesis` mentions compatibility, availability, or order questions
- reviews or notes describe staff repeatedly helping customers choose or verify parts

### 2. Reklamacie / returns friction

Use when the visible support burden is around complaint or return handling.

Typical evidence:

- `reklamacie_url` exists
- `reklamacie_support_pain` mentions PDF, form, attachments, email back-and-forth, or process friction
- `reklamacie_summary` describes a multi-step complaint flow
- `reklamacie_complexity` is `high`

### 3. Multi-channel support chaos

Use when the store clearly routes support through several places and likely creates intake fragmentation.

Typical evidence:

- `support_channel_count >= 4`
- visible phone + email + contact page + reklamacie page
- `mode = mixed`
- no single structured support intake signal

### 4. Chat gap on top of visible support load

Use as a modifier, not the primary pain, when the lead has visible support channels but no chat.

Typical evidence:

- `chat_signal = no`
- phone or email present
- support-heavy signals already exist elsewhere

## Lightweight scoring logic

Score each lead on a `0-8` scale.

### A. Support-load evidence: `0-2`

- `support_channel_count >= 4` -> `+2`
- `support_channel_count = 3` -> `+1`
- `support_channel_count <= 2` or missing -> `+0`

### B. Reklamacie friction: `0-2`

- `reklamacie_complexity = high` -> `+2`
- `reklamacie_support_pain` present or `reklamacie_summary` clearly describes friction -> `+1`
- only `has_reklamacie = yes` with no friction signal -> `+0`

### C. Repetitive pre-sale pressure: `0-2`

- `pain_hypothesis` or `personalization_hook` clearly mentions compatibility / availability / delivery questions -> `+2`
- segment implies the pattern but signal is weaker -> `+1`
- no evidence -> `+0`

### D. Chat gap / implementation-fit bonus: `0-2`

- `chat_signal = no` and visible support channels exist -> `+1`
- `platform_guess = woocommerce` -> `+1`
- otherwise -> `+0`

## Score bands

- `6-8` -> prioritize for v1 outbound now
- `4-5` -> valid v1 lead, but secondary batch
- `0-3` -> keep in research pool, not in the first-send batch

## Primary angle selection rules

Assign exactly one primary angle.

### Choose `Reklamacie friction` when:

- `reklamacie_complexity = high`, or
- `reklamacie_support_pain` explicitly shows manual complaint/return load

Promise:
- explain process
- collect missing inputs
- prepare a cleaner case for the human team

### Choose `Multi-channel chaos` when:

- `support_channel_count >= 4`, and
- reklamacie friction is not the strongest signal

Promise:
- one intake layer across web/email/phone
- cleaner handoff instead of fragmented support threads

### Choose `Compatibility / pre-sale repetition` in all other strong v1 cases when:

- the lead is autodiely / pneuservis / technical e-commerce, and
- the strongest visible signal is repeated product or order-adjacent questions

Promise:
- catch routine questions faster
- reduce repeated manual explanations
- let humans step in only when needed

## Personalization rules

### Rule 1

Open with one visible observation only.

Allowed:

- complaint/returns flow
- support channel mix
- compatibility / delivery / stock question pattern

Not allowed:

- stacking two or three different pain narratives in the opener

### Rule 2

Convert the observation into one operational pain sentence.

Examples:

- repeated part-fit questions steal human time
- reklamacie flow creates manual back-and-forth
- too many channels create messy intake

### Rule 3

Attach one demo promise only.

- Compatibility / pre-sale repetition -> support chat/front-door for repeated questions
- Reklamacie friction -> complaint intake + missing-data capture
- Multi-channel chaos -> shared intake + cleaner human handoff

### Rule 4

Stay inside the proven v1 offer:

- routine capture
- faster first response
- missing-data collection
- prepared handoff to a human

Do not sell full automation, CRM replacement, or broad AI transformation.

### Rule 5

Use only evidence visible in the current artifacts. Do not invent:

- ticket volume
- staffing pressure
- conversion uplift
- revenue impact

## Ready-to-call boundary

Research can set `ready_to_call = yes` only when all of these are true:

- score is `6+`
- a primary angle is assigned cleanly
- `main_phone` exists
- a usable personalization hook exists from visible evidence
- the lead already has send-ready outreach or has shown interest / reply

Research should keep `ready_to_call = no` when:

- score is below `6`
- no phone exists
- the pain angle is ambiguous
- personalization depends on guesswork
- the record is only enriched but not packaged for outreach

Boundary rule:

- research flags potential call-worthiness
- call qualification is only triggered later for leads already marked `ready_to_call`
- no broad AI calling across the whole list in v1

## Default v1 judgments

- Default upstream scoring file: `/Users/_xvadur/singularitas/agents/cso/sk-autodiely-pneu-enriched-v2.csv`
- Default execution packet: `/Users/_xvadur/singularitas/agents/cso/sk-autodiely-pneu-top10-outreach.csv`
- Default angle for most autodiely leads: `Compatibility / pre-sale repetition`
- Strongest differentiator when present: `Reklamacie friction`
