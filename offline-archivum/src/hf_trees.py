#!/usr/bin/env python3
"""HF repók fájllistájának letöltése és cache-elése (research/hf_trees.json) – a pontos include-mintákhoz és méretekhez."""
import json, os, sys, urllib.request, concurrent.futures as cf
HERE = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(HERE, "research", "hf_trees.json")
repos = set()
for f in ("items_llm.jsonl", "items_aitools.jsonl", "items_computing.jsonl"):
    for l in open(os.path.join(HERE, f), encoding="utf-8"):
        d = json.loads(l)["download"]
        if d.get("method") == "hf" and d.get("repo"):
            repos.add(d["repo"])
repos |= {"ggerganov/whisper.cpp", "rhasspy/piper-voices", "facebook/nllb-200-distilled-600M", "facebook/nllb-200-3.3B"}
cache = json.load(open(OUT)) if os.path.exists(OUT) else {}
def get(repo):
    files, url = [], f"https://huggingface.co/api/models/{repo}/tree/main?recursive=true&expand=false"
    try:
        with urllib.request.urlopen(url, timeout=60) as r:
            data = json.load(r)
        files = [(x["path"], (x.get("lfs") or {}).get("size") or x.get("size") or 0) for x in data if x.get("type") == "file"]
    except Exception as e:
        return repo, {"error": str(e)}
    return repo, {"files": files}
todo = [r for r in sorted(repos) if r not in cache or "error" in cache[r]]
with cf.ThreadPoolExecutor(8) as ex:
    for repo, res in ex.map(get, todo):
        cache[repo] = res
json.dump(cache, open(OUT, "w"), ensure_ascii=False)
print(len(repos), "repo;", sum(1 for r in repos if "error" in cache.get(r, {})), "hiba")
