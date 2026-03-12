#!/usr/bin/env python3
import argparse, json, datetime as dt

TEMPLATE = {
  "project_name": "",
  "vertical": "",
  "business_name": "",
  "locale": "sk-SK",
  "timezone": "Europe/Bratislava",
  "channels": ["phone"],
  "hours": "",
  "primary_goal": "",
  "call_types": [],
  "required_fields": ["name", "phone"],
  "booking_target": "calendar_or_crm",
  "handoff_triggers": [
    "urgent request",
    "user asks for human",
    "assistant confidence low"
  ],
  "integrations": {
    "voice": "",
    "automation": "n8n",
    "crm": "",
    "calendar": ""
  },
  "qa_owner": "",
  "go_live_target": ""
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--vertical", choices=["dentist", "realtor"], required=True)
    args = ap.parse_args()

    brief = TEMPLATE.copy()
    brief["vertical"] = args.vertical
    if args.vertical == "dentist":
        brief["call_types"] = ["booking", "reschedule", "cancel", "faq"]
        brief["primary_goal"] = "maximize appointment booking completion"
    else:
        brief["call_types"] = ["buyer_lead", "seller_lead", "renter_lead", "callback"]
        brief["primary_goal"] = "maximize qualified lead capture"

    payload = {
      "created_at": dt.datetime.now().isoformat(),
      "brief": brief
    }
    print(json.dumps(payload, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
