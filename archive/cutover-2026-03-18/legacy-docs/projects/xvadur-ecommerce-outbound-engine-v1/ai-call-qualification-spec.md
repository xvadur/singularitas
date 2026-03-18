# Xvadur E-commerce Outbound Engine v1 - AI Call Qualification Spec

Status: Optional branch  
Trigger: only for leads marked `ready_to_call`

## Trigger Rule

The call module may run only when all of these are true:
- lead state is `ready_to_call`
- the lead already showed enough signal to justify a call
- a usable phone number exists
- the call input packet is complete

If one is missing, the lead stays in manual email or founder routing.

## Call Input Packet

Required fields:

| Field | Notes |
| --- | --- |
| `run_id` | Parent run |
| `lead_id` | Lead key |
| `company_name` | Account identity |
| `website` | Main domain |
| `contact_name` | If known |
| `contact_phone` | Required for execution |
| `reply_summary` | Why a call is justified now |
| `primary_pain_angle` | Current working angle |
| `pain_hypothesis` | Working problem framing |
| `outbound_history` | What was already sent or discussed |
| `qualification_goal` | Why this call exists |

Recommended fields:
- `founder_priority`
- `preferred_founder_cta`
- `no_go_topics`

## Qualification Goals

The call should answer only these questions:
1. Is there a real support or sales-ops pain here?
2. Is the contact close enough to the decision path?
3. Is there timing or urgency?
4. Is a founder conversation justified now?

The call should not:
- scope a custom project deeply
- negotiate pricing
- promise delivery details Adam has not approved
- try to close the deal

## Output States / Outcomes

The call can end in exactly one of these outcomes:
- `qualified_for_founder`
- `nurture`
- `disqualified`
- `call_failed`

## Required Output Fields

| Field | Notes |
| --- | --- |
| `call_attempted_at` | Timestamp |
| `contact_reached` | `yes` or `no` |
| `decision_role_signal` | Best guess at role |
| `pain_confirmation` | `confirmed`, `partial`, or `weak` |
| `timeline_signal` | `near_term`, `later`, or `unknown` |
| `qualification_outcome` | One of the four outcomes |
| `summary` | Short narrative summary |
| `recommended_next_move` | `founder_call`, `nurture`, or `disqualify` |

## Founder Escalation Boundary

Escalate to Adam only when outcome is `qualified_for_founder`.

That escalation must include:
- the call summary
- the key pain confirmed
- the decision-path signal
- the recommended founder CTA
- the recommended timing

Do not escalate to Adam when the outcome is:
- `nurture`
- `disqualified`
- `call_failed`

Those stay inside the engine until Jarvis routes them otherwise.

## Attempt Budget

Minimal v1 budget:
- one primary attempt
- one follow-up attempt if justified

Do not let repeated calls become their own workflow.

## Failure Rule

If the phone number is missing, the packet is incomplete, or execution fails technically, the module must not proceed as qualified.

Route the lead to:
- `call_failed` if the call attempt happened and failed
- manual Jarvis routing if the packet was incomplete before the call
