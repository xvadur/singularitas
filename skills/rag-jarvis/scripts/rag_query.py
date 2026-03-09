#!/usr/bin/env python3
import argparse, json, os, sys, requests

def embed(text, api_key):
    r = requests.post(
        'https://api.openai.com/v1/embeddings',
        headers={'Authorization': f'Bearer {api_key}', 'Content-Type': 'application/json'},
        json={'model': 'text-embedding-3-small', 'input': text},
        timeout=45,
    )
    r.raise_for_status()
    return r.json()['data'][0]['embedding']

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('query')
    ap.add_argument('--type', choices=['jarvis','obsidian','chronology'])
    ap.add_argument('--limit', type=int, default=5)
    ap.add_argument('--json', action='store_true')
    args = ap.parse_args()

    supabase_url = os.getenv('SUPABASE_URL')
    service_key = os.getenv('SUPABASE_SERVICE_KEY')
    openai_key = os.getenv('OPENAI_API_KEY')
    if not (supabase_url and service_key and openai_key):
        print(json.dumps({'used_rag': False, 'error': 'Missing SUPABASE_URL/SUPABASE_SERVICE_KEY/OPENAI_API_KEY'}))
        sys.exit(1)

    try:
        qemb = embed(args.query, openai_key)
        payload = {'query_embedding': qemb, 'match_count': args.limit}
        if args.type:
            payload['filter_type'] = args.type

        r = requests.post(
            supabase_url.rstrip('/') + '/rest/v1/rpc/match_documents',
            headers={
                'apikey': service_key,
                'Authorization': f'Bearer {service_key}',
                'Content-Type': 'application/json'
            },
            json=payload,
            timeout=60,
        )
        r.raise_for_status()
        rows = r.json()

        if not rows:
            out = {'used_rag': False, 'hits': 0, 'answer': '', 'sources': []}
        else:
            answer = '\n\n'.join([x.get('chunk','')[:900] for x in rows[:3]])
            sources = [{'source': x.get('source'), 'source_type': x.get('source_type')} for x in rows[:5]]
            out = {'used_rag': True, 'hits': len(rows), 'answer': answer, 'sources': sources}

        if args.json:
            print(json.dumps(out, ensure_ascii=False))
        else:
            print(out['answer'])

    except Exception as e:
        out = {'used_rag': False, 'error': str(e)}
        print(json.dumps(out, ensure_ascii=False))
        sys.exit(1)

if __name__ == '__main__':
    main()
