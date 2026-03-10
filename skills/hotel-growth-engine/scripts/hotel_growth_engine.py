#!/usr/bin/env python3
import argparse
import csv
import glob
import json
import os
import re
import subprocess
from collections import Counter
from datetime import date
from pathlib import Path
from urllib.parse import urlparse

WORKSPACE = Path('/Users/_xvadur/.openclaw/workspace')
RUNS = WORKSPACE / 'systems' / 'research-pipeline' / 'runs'
GOPLACES = Path('/Users/_xvadur/.openclaw/skills/goplaces/scripts/places_search.py')


def latest(pattern: str) -> str | None:
    items = sorted(glob.glob(str(RUNS / pattern)))
    return items[-1] if items else None


def domain_of(url: str | None) -> str:
    if not url:
        return ''
    u = url.strip()
    if not u:
        return ''
    if not u.startswith('http'):
        u = 'https://' + u
    try:
        return (urlparse(u).netloc or '').lower().replace('www.', '')
    except Exception:
        return ''


def run_places_search(query: str) -> dict:
    out = subprocess.check_output(
        ['python3', str(GOPLACES), query],
        text=True,
        stderr=subprocess.STDOUT,
        timeout=30,
    )
    return json.loads(out)


def choose_best_result(results: list, website: str | None) -> dict | None:
    if not results:
        return None
    if website:
        wanted = domain_of(website)
        if wanted:
            for r in results:
                rd = domain_of(r.get('website') or r.get('url') or '')
                if rd and rd == wanted:
                    return r
    return results[0]


def places_enrich(company: str, city: str, website: str | None) -> dict:
    query = f"{company} {city} hotel"
    data = run_places_search(query)
    results = data.get('results') or []
    best = choose_best_result(results, website)
    if not best:
        return {
            'places_found': False,
            'google_rating': None,
            'google_reviews': None,
            'google_place_id': None,
            'google_name': None,
        }
    return {
        'places_found': True,
        'google_rating': best.get('rating'),
        'google_reviews': best.get('user_ratings_total'),
        'google_place_id': best.get('place_id'),
        'google_name': best.get('name'),
    }


def route_offer(lead: dict) -> tuple[str, str]:
    rating = lead.get('google_rating')
    reviews = lead.get('google_reviews')
    pain = int(lead.get('pain_score') or 0)
    value = int(lead.get('value_score') or 0)
    website = lead.get('website')

    if rating is not None and rating < 4.2:
        return 'review-agent', 'Low Google rating signal.'
    if reviews is not None and reviews < 60:
        return 'review-agent', 'Low Google review volume signal.'
    if (not website) or pain < 55:
        return 'web-refresh', 'Weak website/conversion or lower ops pain.'
    if pain >= 60 and value >= 75:
        return 'ai-recepcia', 'Strong ops pain + value fit.'
    return 'web-refresh', 'Default conversion uplift offer.'


def priority_band(priority_score: int) -> str:
    if priority_score >= 70:
        return 'A'
    if priority_score >= 60:
        return 'B'
    return 'C'


def sequence_for_offer(offer_type: str) -> dict:
    if offer_type == 'review-agent':
        return {
            'd0': 'Quick audit + review recovery angle',
            'd2': 'Follow-up with 2 review response examples',
            'd5': 'Pilot proposal: review agent + response automation',
        }
    if offer_type == 'ai-recepcia':
        return {
            'd0': 'Ops pain opener + KPI pilot proposal',
            'd2': 'Follow-up with workflow map (inbound -> booking)',
            'd5': 'Pilot offer with response-time/no-show KPIs',
        }
    return {
        'd0': 'Homepage/CTA conversion audit opener',
        'd2': 'Follow-up with before/after page outline',
        'd5': '72h web-refresh pilot offer',
    }


def load_phase2(path: str) -> list[dict]:
    data = json.loads(Path(path).read_text(encoding='utf-8'))
    return data.get('items', [])


def to_slug(s: str) -> str:
    return re.sub(r'[^a-z0-9]+', '-', s.lower()).strip('-')


def build_plan(args):
    phase2_path = args.phase2 or latest('phase2_pain_value_interpreted_*.json')
    if not phase2_path:
        raise SystemExit('No phase2 file found. Run hotel-intel phase1+phase2 first.')

    leads = load_phase2(phase2_path)
    if args.limit:
        leads = leads[: args.limit]

    rows = []
    places_enabled = (not args.no_places) and bool(os.environ.get('GOOGLE_PLACES_API_KEY'))

    for lead in leads:
        rec = {
            'company': lead.get('company'),
            'website': lead.get('website'),
            'email': lead.get('email'),
            'phone': lead.get('phone'),
            'contact_id': lead.get('contact_id'),
            'pain_score': int(lead.get('pain_score') or 0),
            'value_score': int(lead.get('value_score') or 0),
            'priority_score': int(lead.get('priority_score') or 0),
        }

        if places_enabled:
            try:
                rec.update(places_enrich(rec['company'] or '', args.city, rec.get('website')))
            except Exception:
                rec.update({
                    'places_found': False,
                    'google_rating': None,
                    'google_reviews': None,
                    'google_place_id': None,
                    'google_name': None,
                })
        else:
            rec.update({
                'places_found': False,
                'google_rating': None,
                'google_reviews': None,
                'google_place_id': None,
                'google_name': None,
            })

        offer_type, offer_reason = route_offer(rec)
        band = priority_band(rec['priority_score'])
        seq = sequence_for_offer(offer_type)

        rec.update({
            'offer_type': offer_type,
            'offer_reason': offer_reason,
            'priority_band': band,
            'tag_segment': 'segment:hotel',
            'tag_offer': f'offer:{offer_type}',
            'tag_priority': f'priority:{band}',
            'tag_status': 'status:outreach_1',
            'sequence_d0': seq['d0'],
            'sequence_d2': seq['d2'],
            'sequence_d5': seq['d5'],
            'next_action': 'email_first_then_call_24h' if rec.get('phone') else 'email_first',
        })
        rows.append(rec)

    rows.sort(key=lambda x: (x['priority_band'], -x['priority_score']))

    today = date.today().isoformat()
    out_base = RUNS / f'hotel_growth_plan_{today}'
    out_json = Path(str(out_base) + '.json')
    out_csv = Path(str(out_base) + '.csv')
    out_md = Path(str(out_base) + '.md')

    summary = {
        'count': len(rows),
        'phase2_source': phase2_path,
        'places_enrichment': places_enabled,
        'offer_counts': dict(Counter(r['offer_type'] for r in rows)),
        'priority_counts': dict(Counter(r['priority_band'] for r in rows)),
    }

    out_json.write_text(json.dumps({'summary': summary, 'items': rows}, ensure_ascii=False, indent=2), encoding='utf-8')

    if rows:
        fields = list(rows[0].keys())
        with out_csv.open('w', newline='', encoding='utf-8') as f:
            w = csv.DictWriter(f, fieldnames=fields)
            w.writeheader()
            w.writerows(rows)

    md = [
        '# Hotel Growth Plan',
        '',
        f"Source: {phase2_path}",
        f"Count: {summary['count']}",
        f"Places enrichment: {summary['places_enrichment']}",
        '',
        '## Offer mix',
    ]
    for k, v in summary['offer_counts'].items():
        md.append(f'- {k}: {v}')
    md += ['', '## Priority mix']
    for k, v in summary['priority_counts'].items():
        md.append(f'- {k}: {v}')
    md += ['', '## Top 10 queue']

    for i, r in enumerate(rows[:10], 1):
        md.append(f"{i}. {r['company']} | {r['offer_type']} | P{r['priority_band']} | score {r['priority_score']}")

    out_md.write_text('\n'.join(md) + '\n', encoding='utf-8')

    print(json.dumps({
        'summary': summary,
        'json': str(out_json),
        'csv': str(out_csv),
        'md': str(out_md),
        'top5': [r['company'] for r in rows[:5]],
    }, ensure_ascii=False, indent=2))


def main():
    ap = argparse.ArgumentParser(description='Hotel Growth Engine')
    sub = ap.add_subparsers(dest='cmd', required=True)

    b = sub.add_parser('build-plan')
    b.add_argument('--phase2', help='Absolute path to phase2 json')
    b.add_argument('--limit', type=int, default=0)
    b.add_argument('--city', default='Bratislava')
    b.add_argument('--no-places', action='store_true')
    b.set_defaults(func=build_plan)

    args = ap.parse_args()
    args.func(args)


if __name__ == '__main__':
    main()
