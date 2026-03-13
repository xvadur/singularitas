# E-shop Agent — Morning Checklist

## Already done
- Vapi assistant created: `e7c4fd4d-9d40-4574-ae2b-9f02fbf2817d`
- Name: `e-shop assistant`
- Prompt upgraded to e-commerce support v2
- Tool contracts prepared for n8n webhook implementation

## Morning implementation steps
1. Get `N8N_BASE_URL`
2. Get `N8N_API_KEY`
3. Build 4 n8n webhook workflows:
   - get_order_status
   - create_support_ticket
   - handoff_to_human
   - log_customer_request
4. Activate workflows
5. Add Vapi tools to the assistant
6. Run 5 test calls / tool simulations

## Target state
- Assistant can answer FAQ safely
- Assistant can check order status
- Assistant can create support tickets
- Assistant can escalate to human
- Assistant can log every call outcome
