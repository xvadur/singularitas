#!/bin/bash
# pipeline-report.sh - Generate lightweight Xvadur pipeline reviews
# Usage: ./pipeline-report.sh [daily|weekly|list]

BD_DIR="${HOME}/.openclaw/workspace/business-development"
REPORTS_DIR="$BD_DIR/reports"
mkdir -p "$REPORTS_DIR"

generate_daily() {
    local date
    date=$(date +%Y-%m-%d)
    local report_file="${REPORTS_DIR}/daily-${date}.md"

    cat > "$report_file" << EOF
# Xvadur Daily Pipeline Review — ${date}

## Today's Focus
- Dominant segment:
- Dominant objective:

## Movement
- New leads researched:
- Messages sent:
- Replies:
- Calls booked:
- Pilots advanced:

## Live Opportunities
| Company | Stage | Signal | Blocker | Next Action |
|---------|-------|--------|---------|-------------|

## Messaging Learnings
- What worked:
- What did not:
- New objection:

## Tomorrow
1.
2.
3.
EOF

    echo "Created: $report_file"
}

generate_weekly() {
    local date
    date=$(date +%Y-%m-%d)
    local report_file="${REPORTS_DIR}/weekly-${date}.md"

    cat > "$report_file" << EOF
# Xvadur Weekly Pipeline Review — ${date}

## Summary
- Segment worked this week:
- Total prospects touched:
- Positive replies:
- Calls:
- Qualified prospects:
- Pilot proposals:
- Closed won:

## Best Signals
1.
2.
3.

## Friction
1.
2.
3.

## Pipeline Review
| Company | Stage | Buyer | Surface | Next Step |
|---------|-------|-------|---------|-----------|

## Priority for Next Week
1.
2.
3.
EOF

    echo "Created: $report_file"
}

case "$1" in
    daily)
        generate_daily
        ;;
    weekly)
        generate_weekly
        ;;
    list)
        ls "$REPORTS_DIR"/*.md 2>/dev/null || echo "No reports yet."
        ;;
    *)
        echo "Xvadur Pipeline Report Generator"
        echo "Commands:"
        echo "  daily   - Create daily pipeline review"
        echo "  weekly  - Create weekly pipeline review"
        echo "  list    - List reports"
        ;;
esac
