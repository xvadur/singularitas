#!/bin/bash
# partner-research.sh - Build a lightweight Xvadur prospect note
# Usage: ./partner-research.sh <company_name> [--profile]

BD_DIR="${HOME}/.openclaw/workspace/business-development"
LEADS_DIR="$BD_DIR/leads"

mkdir -p "$LEADS_DIR"

show_help() {
    echo "Xvadur Prospect Research Tool"
    echo "============================="
    echo ""
    echo "Usage:"
    echo "  $0 <company_name>           - Show research checklist"
    echo "  $0 <company_name> --profile - Create a prospect note"
}

research_checklist() {
    local company="$1"

    echo "Research Checklist for: $company"
    echo "================================"
    echo ""
    echo "1. Business model"
    echo "- What do they sell?"
    echo "- Who answers demand today?"
    echo "- Is phone or web intake important?"
    echo ""
    echo "2. Demand capture gaps"
    echo "- Are they hard to reach?"
    echo "- Do they invite calls, forms, or bookings?"
    echo "- Do reviews mention response speed or poor follow-up?"
    echo ""
    echo "3. Buyer and signal"
    echo "- Who likely owns growth or operations?"
    echo "- What specific signal can personalize outreach?"
    echo "- Why are they a fit for a pilot right now?"
    echo ""
    echo "4. Pilot hypothesis"
    echo "- Best surface: phone, widget, follow-up, reviews, or kit?"
    echo "- Smallest believable pilot?"
    echo "- Biggest scope risk?"
}

create_profile() {
    local company="$1"
    local filename
    filename=$(echo "$company" | tr '[:upper:]' '[:lower:]' | tr ' ' '-' | tr -cd 'a-z0-9-')
    local profile_file="$LEADS_DIR/${filename}.md"

    cat > "$profile_file" << EOF
# Prospect Note: $company

## Snapshot
- Company:
- Website:
- Segment:
- Location:
- Likely buyer:

## Why This Lead
- Fit reason:
- Personalization signal:
- Likely problem:

## Xvadur Angle
- Best surface:
- Pilot angle:
- Why now:

## Outreach Draft
- Opener:
- Main message:
- CTA:

## Qualification
- Clear pain:
- Reachable buyer:
- Scope manageable:
- Notes:

## Pipeline
- Stage: Research
- Last touch:
- Next action: Finish research and prepare outreach
EOF

    echo "Prospect note created: $profile_file"
}

if [ -z "$1" ]; then
    show_help
    exit 0
fi

COMPANY="$1"

if [ "$2" = "--profile" ]; then
    create_profile "$COMPANY"
else
    research_checklist "$COMPANY"
fi
