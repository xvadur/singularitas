#!/usr/bin/env python3
import argparse, collections, datetime as dt, json, re, urllib.request

API = "https://natural20.com/api/feed"

TOPIC_MAP = {
    "policy": ["pentagon", "defense", "department of defense", "dod", "military", "ban", "safety"],
    "models": ["model", "claude", "chatgpt", "openai", "gemini", "deepmind", "llm"],
    "agents": ["agent", "mcp", "multi-model", "orchestr", "autonomous"],
    "infra": ["nvidia", "data center", "gpu", "infrastructure", "chip"],
    "open_source": ["qwen", "llama", "localllama", "open source"]
}

def parse_dt(s):
    return dt.datetime.fromisoformat(s.replace("Z", "+00:00"))

def fetch():
    with urllib.request.urlopen(API, timeout=20) as r:
        return json.load(r)

def classify(text):
    t = text.lower()
    tags = []
    for k, words in TOPIC_MAP.items():
        if any(w in t for w in words):
            tags.append(k)
    return tags or ["other"]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--hours", type=int, default=24)
    ap.add_argument("--top", type=int, default=10)
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    data = fetch()
    cutoff = dt.datetime.now(dt.timezone.utc) - dt.timedelta(hours=args.hours)

    rows = []
    for it in data.get("items", []):
        p = it.get("published")
        if not p:
            continue
        try:
            when = parse_dt(p)
        except Exception:
            continue
        if when < cutoff:
            continue
        title = it.get("title", "").strip()
        summary = (it.get("summary") or "").strip()
        score = int(it.get("score", 0) or 0)
        source = it.get("source", "")
        stype = it.get("sourceType", "")
        url = it.get("url", "")
        text = f"{title}. {summary}"
        tags = classify(text)
        rows.append({
            "published": when.isoformat(),
            "title": title,
            "summary": summary,
            "score": score,
            "source": source,
            "sourceType": stype,
            "url": url,
            "tags": tags,
        })

    rows.sort(key=lambda x: (x["score"], x["published"]), reverse=True)

    # dedupe by normalized title prefix
    seen = set()
    dedup = []
    for r in rows:
        key = re.sub(r"\W+", " ", r["title"].lower()).strip()[:90]
        if key in seen:
            continue
        seen.add(key)
        dedup.append(r)

    top = dedup[: args.top]
    source_counts = collections.Counter(r["sourceType"] for r in dedup)
    tag_counts = collections.Counter(t for r in dedup for t in r["tags"])

    out = {
        "generated": dt.datetime.now(dt.timezone.utc).isoformat(),
        "windowHours": args.hours,
        "itemsInWindow": len(rows),
        "itemsAfterDedupe": len(dedup),
        "sourceTypes": dict(source_counts),
        "themes": dict(tag_counts),
        "top": top,
    }

    if args.json:
        print(json.dumps(out, ensure_ascii=False, indent=2))
        return

    print(f"Natural20 brief | last {args.hours}h")
    print(f"Items: {len(rows)} (dedupe {len(dedup)})")
    print("Source types:", dict(source_counts))
    print("Themes:", dict(tag_counts))
    print("\nTop signals:")
    for i, r in enumerate(top, 1):
        print(f"{i}. [{r['score']}] {r['title']}")
        print(f"   - {r['source']} / {r['sourceType']} / {r['published']}")
        print(f"   - tags: {', '.join(r['tags'])}")
        print(f"   - {r['url']}")

if __name__ == "__main__":
    main()
