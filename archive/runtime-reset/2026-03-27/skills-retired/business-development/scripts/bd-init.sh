#!/bin/bash
# bd-init.sh - Initialize Xvadur BD workspace
# Usage: ./bd-init.sh

BD_DIR="${HOME}/.openclaw/workspace/business-development"

echo "Initializing Xvadur Business Development Workspace"
echo "================================================="

mkdir -p "$BD_DIR"/{segments,leads,outreach,pipeline,templates,reports}

cat > "$BD_DIR/templates/segment-brief.md" << 'EOF'
# Segment Brief: [Segment]

## Buyer
- Primary buyer:
- Secondary buyer:

## Pain Pattern
- What breaks today:
- What gets lost:
- Why it matters now:

## Xvadur Fit
- Recommended surface: [phone voice agent / widget agent / follow-up / review engine / kit]
- Pilot angle:
- Fastest believable promise:

## Risks
- Sales risk:
- Delivery risk:
- Proof gap:

## Next Actions
1.
2.
EOF

cat > "$BD_DIR/templates/lead-sheet.md" << 'EOF'
# Lead Sheet: [Segment Batch]

| Company | Contact | Fit Reason | Signal | Angle | Stage | Next Action |
|---------|---------|------------|--------|-------|-------|-------------|
EOF

cat > "$BD_DIR/templates/qualification-note.md" << 'EOF'
# Qualification Note: [Company]

## Problem
- What is happening now:
- Evidence:

## Proposed Pilot
- Surface:
- Scope:
- Expected outcome:

## Client Inputs Needed
- Phone/web access:
- FAQ or process source:
- Escalation path:

## Risks
- Scope risk:
- Integration risk:
- Buyer risk:

## Next Step
- Owner:
- Date:
- Action:
EOF

cat > "$BD_DIR/pipeline/current.md" << 'EOF'
# Xvadur Pipeline

## Summary
- Research:
- Ready:
- Sent:
- Replied:
- Call:
- Qualified:
- Pilot Proposed:
- Closed Won:
- Closed Lost:

## Active Opportunities
| Company | Segment | Surface | Stage | Last Touch | Blocker | Next Action |
|---------|---------|---------|-------|------------|---------|-------------|
EOF

echo "Workspace ready at: $BD_DIR"
echo "Templates created:"
echo "  - templates/segment-brief.md"
echo "  - templates/lead-sheet.md"
echo "  - templates/qualification-note.md"
echo "  - pipeline/current.md"
