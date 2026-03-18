# E-shop Agent — n8n-ready Tool Contracts

## Goal
Prepare the Vapi e-shop assistant for later n8n webhook integration.

## Minimum tool set

### 1. get_order_status
Purpose:
- Return the current order state after customer verification.

Input:
```json
{
  "order_number": "string",
  "email": "string",
  "phone": "string"
}
```

Output:
```json
{
  "found": true,
  "order_number": "string",
  "status": "processing|paid|shipped|delivered|returned|cancelled|unknown",
  "status_human": "string",
  "carrier": "string",
  "tracking_number": "string",
  "estimated_delivery": "string",
  "notes": "string"
}
```

Failure output:
```json
{
  "found": false,
  "reason": "not_found|not_verified|system_error"
}
```

### 2. create_support_ticket
Purpose:
- Create support or complaint intake from a phone call.

Input:
```json
{
  "customer_name": "string",
  "email": "string",
  "phone": "string",
  "order_number": "string",
  "issue_type": "delivery|payment|return|complaint|product_question|other",
  "issue_summary": "string",
  "priority": "low|medium|high",
  "requested_action": "string"
}
```

Output:
```json
{
  "created": true,
  "ticket_id": "string",
  "next_step": "string"
}
```

### 3. handoff_to_human
Purpose:
- Escalate the case to a person or create callback follow-up.

Input:
```json
{
  "customer_name": "string",
  "email": "string",
  "phone": "string",
  "reason": "string",
  "urgency": "low|medium|high",
  "preferred_callback_time": "string"
}
```

Output:
```json
{
  "accepted": true,
  "handoff_type": "callback|support_queue|live_transfer",
  "reference_id": "string",
  "next_step": "string"
}
```

### 4. log_customer_request
Purpose:
- Save a clean call summary for CRM, helpdesk, sheet, or database.

Input:
```json
{
  "customer_name": "string",
  "email": "string",
  "phone": "string",
  "order_number": "string",
  "intent": "faq|order_status|complaint|return|product_question|handoff|other",
  "summary": "string",
  "outcome": "resolved|handoff|followup_needed|unresolved",
  "agent_name": "e-shop assistant"
}
```

Output:
```json
{
  "logged": true,
  "record_id": "string"
}
```

## Recommended webhook routes in n8n
- `POST /webhook/ecommerce/get-order-status`
- `POST /webhook/ecommerce/create-support-ticket`
- `POST /webhook/ecommerce/handoff-to-human`
- `POST /webhook/ecommerce/log-customer-request`

## Behaviour rules for the assistant
- Never call `get_order_status` without at least one usable identifier.
- Prefer order number first; email or phone as fallback.
- When ticket is created, repeat the next step in plain language.
- If a tool fails, apologize, capture contact details, and use `handoff_to_human` or `log_customer_request`.
- Do not promise refunds, delivery times, or complaint outcomes unless returned by a tool.
