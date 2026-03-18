# 2026-03-18 Runtime Smoke Test

## Scope

Config-level smoke test for the `Obsidian -> singularitas -> firma` split.
This is a runtime check only.
It does not prove live Telegram transport, CRM health, SIP feasibility, or publish readiness.

## Checks run

1. Parse `~/.openclaw/openclaw.json`
2. Confirm Telegram `defaultAccount=default`
3. Confirm compatibility bridge routes:
   - `default -> main`
   - `cso -> research`
   - `cro -> revenue`
   - `cmo -> web`
   - `coo -> integration`
4. Confirm declared agent workspaces exist on disk for all specialist lanes

## Result

- `defaultAccount`: `default`
- route `default`: `main`
- route `cso`: `research`
- route `cro`: `revenue`
- route `cmo`: `web`
- route `coo`: `integration`
- workspace directories present: `13/13`

## Evidence commands

```bash
python3 - <<'PY'
import json
from pathlib import Path
p = Path('/Users/_xvadur/.openclaw/openclaw.json')
with p.open() as f:
    data = json.load(f)
print('defaultAccount', data['channels']['telegram']['defaultAccount'])
actual = {b['match']['accountId']: b['agentId'] for b in data['bindings'] if b.get('type') == 'route'}
for key in ['default','cso','cro','cmo','coo']:
    print('route', key, actual.get(key))
agent_map = {a['id']: Path(a['workspace']) for a in data['agents']['list'] if 'workspace' in a}
missing = [(agent_id, str(path)) for agent_id, path in agent_map.items() if not path.exists()]
print('workspace_dirs_ok', len(agent_map) - len(missing))
PY
```

## Blocked live checks

- Telegram ingress delivery was not exercised with a real inbound message
- CRM remains blocked until a live source replaces the missing DB
- Voice layer remains partial until SIP/vendor validation is complete
- Publishing remains business-partial until public-surface checks are run

## Verdict

Runtime routing is structurally operable.
The remaining gaps are live-system checks, not topology errors.
