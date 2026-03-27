#!/usr/bin/env python3
import argparse
import collections
import datetime as dt
import html
import json
import os
import re
import urllib.request
from pathlib import Path
from urllib.parse import urlparse

API = "https://natural20.com/api/feed"
TZ = dt.timezone(dt.timedelta(hours=1), name="CET")
STOPWORDS = {
    "a", "an", "and", "are", "as", "at", "be", "but", "by", "for", "from", "has", "have", "how", "in", "into",
    "is", "it", "its", "new", "of", "on", "or", "s", "says", "that", "the", "their", "this", "to", "up", "via",
    "we", "what", "with", "will"
}
THEME_RULES = {
    "audio-model-race": ["audio", "voice", "speech", "transcription", "transcript", "live", "latency"],
    "data-center-politics": ["data", "center", "centers", "electricity", "grid", "power", "ban", "tax"],
    "ai-governance": ["ban", "rules", "policy", "safety", "regulation", "editorial", "guidelines", "nude", "nudify"],
    "consumer-ai-launches": ["video", "creator", "capcut", "flash", "localization", "comics", "product", "launches"],
    "capital-and-deals": ["raises", "funding", "acquires", "deal", "buy", "valuation"],
}


def fetch_feed():
    with urllib.request.urlopen(API, timeout=20) as r:
        return json.load(r)


def parse_dt(value):
    return dt.datetime.fromisoformat(value.replace("Z", "+00:00"))


def now_utc():
    return dt.datetime.now(dt.timezone.utc)


def fmt_local(ts):
    return ts.astimezone(TZ).strftime("%Y-%m-%d %H:%M CET")


def fmt_dual(ts):
    return f"{ts.astimezone(TZ).strftime('%Y-%m-%d %H:%M CET')} / {ts.astimezone(dt.timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}"


def date_slug(ts):
    return ts.astimezone(TZ).strftime("%Y-%m-%d")


def normalize_text(text):
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9]+", " ", (text or "").lower())).strip()


def title_tokens(text):
    tokens = [t for t in normalize_text(text).split() if len(t) > 2 and t not in STOPWORDS]
    return tokens


def token_set(text):
    return set(title_tokens(text))


def make_slug(tokens):
    seen = []
    for token in tokens:
        if token not in seen:
            seen.append(token)
    if not seen:
        return "story"
    return "-".join(seen[:5])


def classify_theme(title, summary):
    bag = token_set(title) | token_set(summary)
    scores = []
    for theme, words in THEME_RULES.items():
        overlap = len(bag & set(words))
        if overlap:
            scores.append((overlap, theme))
    scores.sort(reverse=True)
    return scores[0][1] if scores else "general-ai-signal"


def similarity(tokens_a, tokens_b):
    if not tokens_a or not tokens_b:
        return 0.0
    shared = tokens_a & tokens_b
    if len(shared) < 2:
        return 0.0
    return len(shared) / min(len(tokens_a), len(tokens_b))


def parse_existing_live(path):
    if not path.exists():
        return []
    rows = []
    pattern = re.compile(r"^\|\s*(\d+)\s*\|(?:\s*`([^`]*)`\s*\|)?\s*\[(.*?)\]\((.*?)\)\s*\|\s*(\d+)\s*\|\s*([^|]+?)\s*\|")
    for line in path.read_text().splitlines():
        match = pattern.match(line.strip())
        if not match:
            continue
        rank, event_key, title, url, score, published = match.groups()
        rows.append({
            "rank": int(rank),
            "event_key": event_key or None,
            "title": html.unescape(title.strip()),
            "score": int(score),
            "published": published.strip().replace("Z", "+00:00"),
            "url": url.strip(),
        })
    return rows


def load_state(path, live_path):
    if path.exists():
        return json.loads(path.read_text())
    seed_top10 = parse_existing_live(live_path)
    state = {"events": {}, "last_top10": seed_top10, "last_run_utc": None}
    for row in seed_top10:
        title = row["title"]
        summary = ""
        event_key = make_slug(title_tokens(title))
        state["events"][event_key] = {
            "event_key": event_key,
            "first_seen": row["published"],
            "last_seen": row["published"],
            "first_title": title,
            "latest_title": title,
            "latest_norm_title": normalize_text(title),
            "latest_url": row["url"],
            "latest_domain": urlparse(row["url"]).netloc.lower(),
            "theme": classify_theme(title, summary),
            "tokens": sorted(token_set(title)),
            "appearances": 1,
            "status": "active",
            "timeline": [{
                "run": row["published"],
                "rank": row["rank"],
                "score": row["score"],
                "title": title,
                "url": row["url"],
                "state": "seeded from prior live file",
            }],
        }
        row["event_key"] = event_key
    return state


def stable_event_key(item, state_events):
    url = item["url"]
    norm_title = normalize_text(item["title"])
    tokens = item["tokens"]
    domain = urlparse(url).netloc.lower()

    for key, event in state_events.items():
        if url and url == event.get("latest_url"):
            return key, "exact-url"
        if norm_title and norm_title == event.get("latest_norm_title"):
            return key, "exact-title"

    best_key = None
    best_reason = None
    best_score = 0.0
    for key, event in state_events.items():
        prior_tokens = set(event.get("tokens", []))
        score = similarity(tokens, prior_tokens)
        if score < 0.6:
            continue
        shared = sorted(tokens & prior_tokens)
        domain_match = domain and domain == event.get("latest_domain")
        if domain_match:
            score += 0.05
        if score > best_score:
            best_score = score
            best_key = key
            best_reason = f"token-overlap {','.join(shared[:4])}"

    if best_key:
        return best_key, best_reason

    base = make_slug(list(tokens) or title_tokens(item["title"]))
    key = base
    i = 2
    while key in state_events:
        key = f"{base}-{i}"
        i += 1
    return key, "new-key"


def build_items(raw_items):
    rows = []
    for raw in raw_items:
        published = raw.get("published")
        title = html.unescape((raw.get("title") or "").strip())
        url = (raw.get("url") or "").strip()
        if not (published and title and url):
            continue
        try:
            when = parse_dt(published)
        except Exception:
            continue
        rows.append({
            "title": title,
            "summary": (raw.get("summary") or "").strip(),
            "url": url,
            "score": int(raw.get("score", 0) or 0),
            "published": when,
            "source": (raw.get("source") or "").strip(),
            "source_type": (raw.get("sourceType") or "").strip(),
            "tokens": token_set(title),
            "norm_title": normalize_text(title),
            "domain": urlparse(url).netloc.lower(),
        })
    rows.sort(key=lambda r: (r["score"], r["published"]), reverse=True)

    dedup = []
    seen = set()
    for row in rows:
        key = (row["norm_title"], row["url"])
        if key in seen:
            continue
        seen.add(key)
        dedup.append(row)
    return dedup[:10]


def update_state(state, top10, run_ts):
    previous = {row["event_key"]: row for row in state.get("last_top10", [])}
    previous_keys = set(previous)
    current_keys = set()

    for rank, item in enumerate(top10, start=1):
        event_key, match_reason = stable_event_key(item, state["events"])
        item["event_key"] = event_key
        item["match_reason"] = match_reason
        current_keys.add(event_key)

        event = state["events"].get(event_key)
        if not event:
            event = {
                "event_key": event_key,
                "first_seen": run_ts.isoformat(),
                "last_seen": run_ts.isoformat(),
                "first_title": item["title"],
                "latest_title": item["title"],
                "latest_norm_title": item["norm_title"],
                "latest_url": item["url"],
                "latest_domain": item["domain"],
                "theme": classify_theme(item["title"], item["summary"]),
                "tokens": sorted(item["tokens"]),
                "appearances": 0,
                "status": "active",
                "timeline": [],
            }
            state["events"][event_key] = event

        event["last_seen"] = run_ts.isoformat()
        event["latest_title"] = item["title"]
        event["latest_norm_title"] = item["norm_title"]
        event["latest_url"] = item["url"]
        event["latest_domain"] = item["domain"]
        event["tokens"] = sorted(item["tokens"])
        event["theme"] = classify_theme(item["title"], item["summary"])
        event["appearances"] += 1
        event["status"] = "active"

        prior_rank = previous.get(event_key, {}).get("rank")
        if prior_rank is None:
            state_label = "new story"
        elif prior_rank == rank:
            state_label = f"continuation; holds #{rank}"
        elif prior_rank > rank:
            state_label = f"continuation; rank up #{prior_rank} → #{rank}"
        else:
            state_label = f"continuation; rank down #{prior_rank} → #{rank}"
        item["state_label"] = state_label
        item["prior_rank"] = prior_rank

        event["timeline"].append({
            "run": run_ts.isoformat(),
            "rank": rank,
            "score": item["score"],
            "title": item["title"],
            "url": item["url"],
            "state": state_label,
        })
        event["timeline"] = event["timeline"][-12:]

    dropped = sorted(previous_keys - current_keys)
    for key in dropped:
        event = state["events"].get(key)
        if event:
            event["status"] = "inactive"

    state["last_top10"] = [
        {
            "rank": idx,
            "event_key": item["event_key"],
            "title": item["title"],
            "score": item["score"],
            "published": item["published"].isoformat(),
            "url": item["url"],
        }
        for idx, item in enumerate(top10, start=1)
    ]
    state["last_run_utc"] = run_ts.isoformat()
    return previous, dropped


def render_live(run_ts, top10, previous, dropped, daily_rel, continuity_rel):
    prev_titles = {v["event_key"]: v["title"] for v in previous.values()}
    entrants = [item for item in top10 if item["prior_rank"] is None]
    rank_moves = [item for item in top10 if item["prior_rank"] is not None and item["prior_rank"] != item["rank"]]
    dropped_items = [previous[key] for key in dropped if key in previous]
    themes = collections.Counter(classify_theme(item["title"], item["summary"]) for item in top10)

    lines = [
        "# Natural20 Live Top 10",
        "",
        "- Surface: `natural20-live-top10`",
        "- Owner: `research`",
        "- State: `live`",
        f"- Last updated: `{fmt_dual(run_ts)}`",
        "- Source: `https://natural20.com/api/feed`",
        "- Contract: script-written by `skills/natural20-api-brief/scripts/n20_ingest.py`",
        "- Purpose: maintain a rolling top-10 world-state layer from Natural20 so Jarvis can answer current-event questions from stored state instead of reconstructing from scratch.",
        "",
        "## Current top 10",
        "",
        "| Rank | Event key | Story | Score | Published | State |",
        "|---|---|---|---:|---|---|",
    ]
    for item in top10:
        lines.append(
            f"| {item['rank']} | `{item['event_key']}` | [{item['title']}]({item['url']}) | {item['score']} | {item['published'].isoformat().replace('+00:00', 'Z')} | {item['state_label']} |"
        )

    lines += ["", "## Entrants / drops / notable rank changes", ""]
    lines.append("### New in top 10 this run")
    if entrants:
        for item in entrants:
            lines.append(f"- #{item['rank']} `{item['event_key']}` — {item['title']}")
    else:
        lines.append("- None")

    lines.append("")
    lines.append("### Dropped from top 10 this run")
    if dropped_items:
        for item in dropped_items:
            lines.append(f"- `{item['event_key']}` — {item['title']} (was #{item['rank']})")
    else:
        lines.append("- None")

    lines.append("")
    lines.append("### Notable rank changes")
    if rank_moves:
        for item in rank_moves:
            arrow = "↑" if item["prior_rank"] > item["rank"] else "↓"
            lines.append(f"- `{item['event_key']}` {arrow} #{item['prior_rank']} → #{item['rank']} — {item['title']}")
    else:
        lines.append("- None")

    lines += ["", "## Dominant themes", ""]
    for theme, count in themes.most_common(4):
        lines.append(f"- `{theme}` — {count} of current top-10 stories")

    lines += [
        "",
        "## Query hints",
        "",
        f"- For **what changed in the last X hours**, use today’s append-only log at `{daily_rel}`.",
        f"- For **what is happening with a specific story**, use `{continuity_rel}` and the event key column above.",
        "- This file is the rolling state layer, not an archive.",
    ]
    return "\n".join(lines) + "\n"


def render_daily(run_ts, top10, previous, dropped, path):
    theme_counts = collections.Counter(classify_theme(item["title"], item["summary"]) for item in top10)
    entrants = [item for item in top10 if item["prior_rank"] is None]
    rank_moves = [item for item in top10 if item["prior_rank"] is not None and item["prior_rank"] != item["rank"]]
    dropped_items = [previous[key] for key in dropped if key in previous]
    current_lead = top10[0]

    header = [
        "# Natural20 Hourly Brief Log",
        "",
        f"- Date: `{date_slug(run_ts)}`",
        "- Owner: `research`",
        "- Surface: `natural20-hourly-monitor`",
        "- Purpose: append hourly Natural20 monitoring snapshots so Jarvis can answer what changed over the last X hours.",
        "- Contract: script-written by `skills/natural20-api-brief/scripts/n20_ingest.py`",
        "",
        "## Run log",
        "",
    ]
    if not path.exists():
        text = "\n".join(header)
    else:
        text = path.read_text().rstrip() + "\n\n"

    block = [
        f"## Run {run_ts.astimezone(TZ).strftime('%H:%M CET')} / {run_ts.astimezone(dt.timezone.utc).strftime('%H:%M UTC')}",
        "",
        "### Top changes this hour",
    ]
    if entrants:
        block.append("- New in top 10: " + "; ".join(f"#{item['rank']} `{item['event_key']}` — {item['title']}" for item in entrants))
    else:
        block.append("- New in top 10: none")
    if dropped_items:
        block.append("- Dropped from top 10: " + "; ".join(f"`{item['event_key']}` — {item['title']} (was #{item['rank']})" for item in dropped_items))
    else:
        block.append("- Dropped from top 10: none")
    if rank_moves:
        block.append("- Rank changes: " + "; ".join(f"`{item['event_key']}` #{item['prior_rank']} → #{item['rank']}" for item in rank_moves))
    else:
        block.append("- Rank changes: none")

    block += ["", "### Current dominant themes"]
    for theme, count in theme_counts.most_common(4):
        block.append(f"- `{theme}` ({count}/10)")

    block += [
        "",
        "### Continuity notes",
        f"- Current #1: `{current_lead['event_key']}` — {current_lead['title']} (score {current_lead['score']}).",
        f"- Top-10 turnover this run: {len(entrants)} entrant(s), {len(dropped_items)} drop(s).",
        "- Matching is deterministic: exact URL, then exact normalized title, then ≥0.60 token-overlap on informative title tokens.",
    ]
    return text + "\n".join(block).rstrip() + "\n"


def render_continuity(run_ts, state):
    events = []
    for event in state["events"].values():
        if event.get("appearances", 0) >= 2 or event.get("status") == "active":
            events.append(event)
    events.sort(key=lambda e: (e["status"] != "active", e["last_seen"]), reverse=False)
    events.sort(key=lambda e: parse_dt(e["last_seen"]), reverse=True)

    lines = [
        "# Natural20 Event Continuity",
        "",
        "- Surface: `natural20-event-continuity`",
        "- Owner: `research`",
        "- State: `durable`",
        f"- Last updated: `{fmt_dual(run_ts)}`",
        "- Source of updates: Natural20 feed + script state",
        "- Contract: script-written by `skills/natural20-api-brief/scripts/n20_ingest.py`",
        "- Purpose: preserve major recurring story continuity across the day so Jarvis can answer event-specific questions from stored state.",
        "",
        "## Matching contract",
        "",
        "1. exact URL match keeps the prior event key",
        "2. else exact normalized title keeps the prior event key",
        "3. else informative-title token overlap ≥ 0.60 with at least 2 shared tokens keeps the prior event key",
        "4. else a new event key is created from the title-token slug",
        "",
        "## Tracked events",
        "",
    ]

    if not events:
        lines.append("- None yet")
        return "\n".join(lines) + "\n"

    for idx, event in enumerate(events, start=1):
        latest = event["timeline"][-1] if event.get("timeline") else None
        lines += [
            f"### {idx}) `{event['event_key']}`",
            f"- Status: `{event['status']}`",
            f"- Theme: `{event.get('theme', 'general-ai-signal')}`",
            f"- First seen: `{fmt_local(parse_dt(event['first_seen']))}`",
            f"- Last seen: `{fmt_local(parse_dt(event['last_seen']))}`",
            f"- Appearances in top 10: `{event.get('appearances', 0)}`",
            f"- Latest title: {event.get('latest_title', '')}",
        ]
        if latest:
            lines.append(f"- Latest known position: `#{latest['rank']}` at `{fmt_local(parse_dt(latest['run']))}`")
        lines.append("- Timeline:")
        for point in event.get("timeline", [])[-8:]:
            lines.append(
                f"  - `{fmt_local(parse_dt(point['run']))}` — #{point['rank']} — {point['state']}"
            )
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default="/Users/_xvadur/singularitas")
    args = ap.parse_args()

    root = Path(args.root)
    inventory_dir = root / "studio/research/inventory"
    daily_dir = root / "studio/research/daily"
    state_path = inventory_dir / "natural20-state.json"
    live_path = inventory_dir / "natural20-live-top10.md"
    continuity_path = inventory_dir / "natural20-event-continuity.md"

    run_ts = now_utc().replace(second=0, microsecond=0)
    daily_path = daily_dir / f"{date_slug(run_ts)}-natural20-brief.md"
    daily_rel = os.path.relpath(daily_path, root)
    continuity_rel = os.path.relpath(continuity_path, root)

    state = load_state(state_path, live_path)
    raw = fetch_feed()
    top10 = build_items(raw.get("items", []))
    if not top10:
        raise SystemExit("Natural20 feed returned no usable items")

    previous, dropped = update_state(state, top10, run_ts)
    for rank, item in enumerate(top10, start=1):
        item["rank"] = rank

    inventory_dir.mkdir(parents=True, exist_ok=True)
    daily_dir.mkdir(parents=True, exist_ok=True)

    live_path.write_text(render_live(run_ts, top10, previous, dropped, daily_rel, continuity_rel))
    continuity_path.write_text(render_continuity(run_ts, state))
    daily_path.write_text(render_daily(run_ts, top10, previous, dropped, daily_path))
    state_path.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n")

    print(json.dumps({
        "run_utc": run_ts.isoformat(),
        "top10_count": len(top10),
        "daily_path": str(daily_path),
        "live_path": str(live_path),
        "continuity_path": str(continuity_path),
        "state_path": str(state_path),
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
