#!/usr/bin/env python3
import argparse
import glob
import json
import subprocess
from pathlib import Path

WORKSPACE = Path('/Users/_xvadur/.openclaw/workspace')
PIPE = WORKSPACE / 'systems' / 'research-pipeline'
SCRIPTS = PIPE / 'scripts'
RUNS = PIPE / 'runs'

PHASE1 = SCRIPTS / 'phase1_hygiene_scoring.py'
PHASE2 = SCRIPTS / 'phase2_pain_value_intel.py'
PHASE3 = SCRIPTS / 'phase3_outreach_pack.py'
PHASE4 = SCRIPTS / 'phase4_sequence_engine.py'


def run(cmd):
    p = subprocess.run(cmd, shell=True, text=True, capture_output=True)
    if p.returncode != 0:
        raise RuntimeError((p.stderr or p.stdout).strip())
    return p.stdout.strip()


def cmd_phase1(_):
    print(run(f'python3 {PHASE1}'))


def cmd_phase2(_):
    print(run(f'python3 {PHASE2}'))


def cmd_phase3(_):
    print(run(f'python3 {PHASE3}'))


def cmd_phase4(_):
    print(run(f'python3 {PHASE4}'))


def cmd_run_all(_):
    print('== phase1 ==')
    print(run(f'python3 {PHASE1}'))
    print('== phase2 ==')
    print(run(f'python3 {PHASE2}'))
    print('== phase3 ==')
    print(run(f'python3 {PHASE3}'))
    print('== phase4 ==')
    print(run(f'python3 {PHASE4}'))


def latest(pattern):
    items = sorted(glob.glob(str(RUNS / pattern)))
    return items[-1] if items else None


def top5_from_json(path):
    if not path:
        return []
    data = json.loads(Path(path).read_text(encoding='utf-8'))
    items = data.get('items', [])
    return [x.get('company', '') for x in items[:5]]


def cmd_summary(_):
    p1j = latest('phase1_clean_top20_*.json')
    p1c = latest('phase1_clean_top20_*.csv')
    p2j = latest('phase2_pain_value_interpreted_*.json')
    p2c = latest('phase2_pain_value_interpreted_*.csv')
    p3j = latest('phase3_top5_outreach_pack_*.json')
    p3c = latest('phase3_top5_outreach_pack_*.csv')
    p3m = latest('phase3_top5_outreach_pack_*.md')
    p4j = latest('phase4_sequence_engine_top5_*.json')
    p4m = latest('phase4_sequence_engine_top5_*.md')

    out = {
        'phase1_json': p1j,
        'phase1_csv': p1c,
        'phase2_json': p2j,
        'phase2_csv': p2c,
        'phase3_json': p3j,
        'phase3_csv': p3c,
        'phase3_md': p3m,
        'phase4_json': p4j,
        'phase4_md': p4m,
        'top5_phase2': top5_from_json(p2j),
    }
    print(json.dumps(out, ensure_ascii=False, indent=2))


def main():
    ap = argparse.ArgumentParser(description='Hotel Intel pipeline wrapper')
    sub = ap.add_subparsers(dest='cmd', required=True)

    sub.add_parser('phase1').set_defaults(func=cmd_phase1)
    sub.add_parser('phase2').set_defaults(func=cmd_phase2)
    sub.add_parser('phase3').set_defaults(func=cmd_phase3)
    sub.add_parser('phase4').set_defaults(func=cmd_phase4)
    sub.add_parser('run-all').set_defaults(func=cmd_run_all)
    sub.add_parser('summary').set_defaults(func=cmd_summary)

    args = ap.parse_args()
    args.func(args)


if __name__ == '__main__':
    main()
