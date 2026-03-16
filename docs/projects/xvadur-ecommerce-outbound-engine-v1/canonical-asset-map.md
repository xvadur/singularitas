# Xvadur E-commerce Outbound Engine v1 - Canonical Asset Map

Locked scope: autodiely / pneuservis / support-heavy e-commerce only. This doc names the source-of-truth file per asset category and marks the rest as supporting or legacy for v1.

Flow: `segment shortlist -> enriched lead base -> top-10 outreach packet -> shared demo asset -> reply/interest -> founder handoff`

## Asset map

| Asset category | Canonical file/path | Purpose | Status | Why chosen |
| --- | --- | --- | --- | --- |
| Segment + full lead base | `/Users/_xvadur/singularitas/agents/cso/sk-autodiely-pneu-enriched-v2.csv` | Upstream source for scoring, filtering, and future batch selection across the full 36-lead pool. | canonical | Most complete lead file. It keeps the original shortlist fields and adds web contact, FAQ, reklamacie, chat, platform, cart, and support-channel signals needed for v1 research. |
| Current send-ready outreach batch | `/Users/_xvadur/singularitas/agents/cso/sk-autodiely-pneu-top10-outreach.csv` | Downstream packet for the current v1 top 10 with personalization hooks and drafted outreach. | canonical | Final current-stage batch file. It already contains cleaned contact data, reklamacie observations, and outreach subject/body in one place. |
| Demo copy brief | `/Users/_xvadur/singularitas/agents/cso/ecommerce-support-agent-onepager.md` | Message source for the outbound demo page and angle consistency. | supporting | Strong messaging brief, but not the live asset source. Use it to understand positioning and copy intent. |
| Demo asset source | `/Users/_xvadur/singularitas/agents/cmo/ecommerce-support-onepager/src/pages/index.astro` | Canonical source for the demo page that gets referenced in outreach and demos. | canonical | Real implementation source, not just copy notes or generated output. This is the asset that should be updated if the shared demo changes. |
| Demo build output | `/Users/_xvadur/singularitas/agents/cmo/ecommerce-support-onepager/dist/index.html` | Generated snapshot of the onepager. | legacy | Useful for preview/export only. Never edit or treat as source-of-truth. |
| Runtime contract | `/Users/_xvadur/singularitas/business/segments/ecommerce-agent-tools-contracts.md` | Contract-level definition of the support agent tools and behavior. | canonical | Best doctrine-level source for what the support agent can do. More stable than prompt JSON or workflow stubs. |
| Active support-agent prompt | `/Users/_xvadur/singularitas/tmp/e-shop-assistant-prompt-v4.json` | Current prompt/runtime config for the support demo agent. | supporting | Active implementation config using `gpt-4o` plus the 4 tools, but still implementation-level, not doctrine-level. |
| Vapi tool pack | `/Users/_xvadur/singularitas/tmp/vapi-tool-get-order-status.json` | Vapi tool definition for order status. | supporting | Active tool config, but only one member of the implementation set. Keep aligned to the runtime contract. |
| Vapi tool pack | `/Users/_xvadur/singularitas/tmp/vapi-tool-create-support-ticket.json` | Vapi tool definition for support ticket creation. | supporting | Same reason as above. |
| Vapi tool pack | `/Users/_xvadur/singularitas/tmp/vapi-tool-handoff-to-human.json` | Vapi tool definition for human escalation. | supporting | Same reason as above. |
| Vapi tool pack | `/Users/_xvadur/singularitas/tmp/vapi-tool-log-customer-request.json` | Vapi tool definition for request logging. | supporting | Same reason as above. |
| n8n workflow pack | `/Users/_xvadur/singularitas/tmp/n8n-get_order_status.json` | n8n webhook stub for order-status lookup. | supporting | Implementation stub paired to the Vapi tool. Not the contract source. |
| n8n workflow pack | `/Users/_xvadur/singularitas/tmp/n8n-create_support_ticket.json` | n8n webhook stub for support ticket creation. | supporting | Implementation stub paired to the Vapi tool. Not the contract source. |
| n8n workflow pack | `/Users/_xvadur/singularitas/tmp/n8n-handoff_to_human.json` | n8n webhook stub for human handoff. | supporting | Implementation stub paired to the Vapi tool. Not the contract source. |
| n8n workflow pack | `/Users/_xvadur/singularitas/tmp/n8n-log_customer_request.json` | n8n webhook stub for request logging. | supporting | Implementation stub paired to the Vapi tool. Not the contract source. |

## Lead-data lineage

| File | Purpose | Status | Notes |
| --- | --- | --- | --- |
| `/Users/_xvadur/singularitas/agents/cso/sk-autodiely-pneu-shortlist.csv` | Initial 36-lead segment shortlist with first-pass pain hypotheses. | legacy | Good provenance, but too thin for v1 scoring and outreach decisions. |
| `/Users/_xvadur/singularitas/agents/cso/sk-autodiely-pneu-enriched.csv` | First enrichment pass with website/review context. | legacy | Superseded by `enriched-v2`, which adds the support-heavy website signals that matter operationally. |
| `/Users/_xvadur/singularitas/agents/cso/sk-autodiely-pneu-enriched-v2.csv` | Full enriched lead base. | canonical | Start all new scoring and top-10 selection from here. |
| `/Users/_xvadur/singularitas/agents/cso/sk-autodiely-pneu-top10-clean.csv` | Cleaned narrowed batch. | supporting | Useful intermediate reference for contact normalization, but no reklamacie analysis or outreach copy. |
| `/Users/_xvadur/singularitas/agents/cso/sk-autodiely-pneu-top10-reklamacie.csv` | Narrowed batch plus reklamacie friction analysis. | supporting | Useful bridge file for pain inference, but outreach packet supersedes it for current execution. |
| `/Users/_xvadur/singularitas/agents/cso/sk-autodiely-pneu-top10-outreach.csv` | Current send-ready batch. | canonical | This is the current v1 execution packet, not just an intermediate research file. |

## Demo/runtime lineage

| File | Purpose | Status | Notes |
| --- | --- | --- | --- |
| `/Users/_xvadur/singularitas/agents/cso/ecommerce-support-agent-onepager.md` | Source messaging brief. | supporting | Keep as copy/source material. Do not treat as the live demo asset. |
| `/Users/_xvadur/singularitas/agents/cmo/ecommerce-support-onepager/src/pages/index.astro` | Live onepager source. | canonical | Shared demo reference for outbound and demos. |
| `/Users/_xvadur/singularitas/business/segments/ecommerce-agent-tools-contracts.md` | Runtime/tool contract. | canonical | Doctrine-level source for support-agent behavior. |
| `/Users/_xvadur/singularitas/tmp/e-shop-assistant-prompt-v4.json` | Live prompt config. | supporting | Current active implementation. Verify against contract when changed. |
| `/Users/_xvadur/singularitas/tmp/vapi-tool-*.json` | Tool definitions for Vapi. | supporting | Keep in sync with the contract doc; do not promote above it. |
| `/Users/_xvadur/singularitas/tmp/n8n-*.json` | Matching n8n webhook stubs. | supporting | Implementation stubs only. |

## v1 operating decisions from this map

- Research and rescoring start from `/Users/_xvadur/singularitas/agents/cso/sk-autodiely-pneu-enriched-v2.csv`.
- Current outreach execution starts from `/Users/_xvadur/singularitas/agents/cso/sk-autodiely-pneu-top10-outreach.csv`.
- Demo references point to one shared asset: `/Users/_xvadur/singularitas/agents/cmo/ecommerce-support-onepager/src/pages/index.astro`.
- Runtime truth lives in `/Users/_xvadur/singularitas/business/segments/ecommerce-agent-tools-contracts.md`; prompt/Vapi/n8n files are active implementations underneath that contract.
- No CRM file is canonical in v1 because tracking is file-only by fixed decision.
