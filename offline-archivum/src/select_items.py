#!/usr/bin/env python3
"""
ARCHIVUM kiválasztó + letöltési terv generátor (csak Python stdlib, 3.9+).

Bemenet: ARCHIVUM.md (a ```jsonl blokkokat olvassa ki) vagy egy .jsonl katalógus.
Kimenet: kiválasztási terv (táblázat a képernyőre, plan.json, opcionálisan download.sh).

Példák:
  python3 select_items.py ARCHIVUM.md --budget 256GB
  python3 select_items.py ARCHIVUM.md --budget 2TB --profile survival --langs hu,en --hw T3 --emit-sh dl.sh
  python3 select_items.py ARCHIVUM.md --budget 64GB --focus medicine=2,agriculture=1.5 --exclude kx-ted
  python3 select_items.py ARCHIVUM.md --list            # teljes katalógus pontszámokkal
"""
import argparse, json, re, sys, shlex

PROFILES = {  # súlyok: S=túlélés R=újjáépítés A=gyakorlatiasság U=pótolhatatlanság Q=megbízhatóság O=offline-kényelem
    "balanced":  {"S": .30, "R": .25, "A": .15, "U": .15, "Q": .10, "O": .05},
    "survival":  {"S": .45, "R": .10, "A": .20, "U": .10, "Q": .10, "O": .05},
    "rebuild":   {"S": .15, "R": .40, "A": .15, "U": .15, "Q": .10, "O": .05},
    "education": {"S": .10, "R": .35, "A": .10, "U": .15, "Q": .20, "O": .10},
    "computing": {"S": .05, "R": .40, "A": .20, "U": .15, "Q": .10, "O": .10},
}
MEM_CAP = {"T5": 10e9, "T4": 100e9, "T3": 220e9, "T2": 900e9, "T1": 1e18}  # alapértelmezett max. modellméret hardverszintenként
AUTO_METHODS = {"agent", "kiwix", "http", "wget-mirror", "rsync", "git", "hf", "ollama", "archive.org", "torrent", "jigdo", "s3"}
UNITS = {"B": 1, "KB": 1e3, "MB": 1e6, "GB": 1e9, "TB": 1e12, "PB": 1e15,
         "KIB": 2**10, "MIB": 2**20, "GIB": 2**30, "TIB": 2**40}


def parse_size(s):
    m = re.fullmatch(r"\s*([\d.]+)\s*([A-Za-z]*)\s*", s)
    if not m:
        sys.exit(f"Érvénytelen méret: {s}")
    return int(float(m.group(1)) * UNITS.get((m.group(2) or "B").upper(), 1))


def human(b):
    if b is None:
        return "?"
    for u, f in (("TB", 1e12), ("GB", 1e9), ("MB", 1e6), ("KB", 1e3)):
        if b >= f:
            return f"{b / f:.2f} {u}"
    return f"{b} B"


def load(path):
    text = open(path, encoding="utf-8").read()
    if path.endswith(".md"):
        blocks = re.findall(r"```jsonl\n(.*?)```", text, re.S)
        lines = [l for b in blocks for l in b.splitlines()]
    else:
        lines = text.splitlines()
    items, seen = [], set()
    for l in lines:
        l = l.strip()
        if not l or l.startswith("//"):
            continue
        it = json.loads(l)
        if it["id"] in seen:
            sys.exit(f"Duplikált id: {it['id']}")
        seen.add(it["id"])
        items.append(it)
    return items


def composite(it, w, focus):
    s = it.get("scores") or {}
    base = sum(w[k] * s.get(k, 0) for k in w)
    return round(base * focus.get(it.get("cat"), 1.0), 3)


def size_of(it):
    return it.get("bytes") or it.get("bytes_est")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("catalog")
    ap.add_argument("--budget", help="pl. 64GB, 512GB, 2TB (decimális egység, mint a meghajtók címkéje)")
    ap.add_argument("--reserve", type=float, default=0.08, help="tartalék hányad a fájlrendszernek / checksumoknak (alap 0.08)")
    ap.add_argument("--profile", default="balanced", choices=PROFILES)
    ap.add_argument("--langs", default="hu,en,multi", help="engedett nyelvek, vesszővel")
    ap.add_argument("--access", default="free,free-registration,donation",
                    help="engedett hozzáférés: free,free-registration,donation,paid,gray,physical")
    ap.add_argument("--hw", default=None, help="LLM hardverszint: T1..T5 (ha nincs megadva: nincs LLM, csak ha --llm-max>0 és --hw adott)")
    ap.add_argument("--llm-max", type=float, default=0.35, help="a keret max. ennyi hányada mehet LLM-súlyokra")
    ap.add_argument("--platform", default="", help="LLM-formátumok a GGUF/Ollama mellé: mac (MLX), server (vLLM/SGLang: FP8/NVFP4/AWQ), android (LiteRT); vesszővel")
    ap.add_argument("--uncensored", choices=["no", "also", "only"], default="also", help="cenzúrázatlan LLM-változatok: no | also | only")
    ap.add_argument("--llm-models", type=int, default=3, help="legfeljebb ennyi különböző LLM-modell (group) kerüljön be")
    ap.add_argument("--mem", default=None, help="LLM-re használható memória (RAM+VRAM vagy unified), pl. 48GB / 512GB; a modell max. 85%%-a lehet")
    ap.add_argument("--focus", default="", help="kategória-szorzók, pl. medicine=2,agriculture=1.5")
    ap.add_argument("--max-tier", type=int, default=5)
    ap.add_argument("--include", default="", help="kötelezően beveendő id-k (vesszővel)")
    ap.add_argument("--exclude", default="", help="kizárt id-k vagy kategóriák (cat:NAME)")
    ap.add_argument("--list", action="store_true", help="katalógus listázása pontszám szerint")
    ap.add_argument("--out", default="plan.json")
    ap.add_argument("--emit-sh", default=None, help="letöltő bash szkript írása ide")
    ap.add_argument("--dest", default="/mnt/archivum", help="célkönyvtár a szkriptben")
    a = ap.parse_args()

    items = load(a.catalog)
    w = PROFILES[a.profile]
    focus = {k: float(v) for k, v in (p.split("=") for p in a.focus.split(",") if p)}
    for it in items:
        it["_score"] = composite(it, w, focus)

    if a.list:
        for it in sorted(items, key=lambda x: (x["tier"], -x["_score"])):
            print(f"T{it['tier']} {it['_score']:5.2f} {human(size_of(it)):>10} {it['access']:<17} {it['cat']:<17} {it['id']}")
        return
    if not a.budget:
        sys.exit("--budget kötelező (vagy --list)")

    budget = int(parse_size(a.budget) * (1 - a.reserve))
    langs = set(a.langs.split(","))
    access = set(a.access.split(","))
    excl = set(x for x in a.exclude.split(",") if x)
    incl = set(x for x in a.include.split(",") if x)

    manual, skipped_unknown, eligible = [], [], []
    for it in items:
        if it["id"] in excl or f"cat:{it['cat']}" in excl:
            continue
        if it["tier"] > a.max_tier and it["id"] not in incl:
            continue
        if it.get("lang") not in langs and it["id"] not in incl:
            continue
        if it.get("access") not in access:
            continue
        if it["cat"] in ("ai_tools",) or it["id"] == "tool-ollama-installers":
            if not a.hw:
                continue
        if it["cat"].startswith("ai_models"):
            if not a.hw or a.hw not in (it.get("hw_tiers") or []):
                continue
            if it.get("platform", "any") not in ({"any"} | set(p for p in a.platform.split(",") if p)):
                continue
            memcap = parse_size(a.mem) * 0.85 if a.mem else MEM_CAP.get(a.hw, 1e18)
            if size_of(it) and size_of(it) > memcap:
                continue
            unc = it["cat"] == "ai_models_uncensored"
            if (a.uncensored == "no" and unc) or (a.uncensored == "only" and not unc):
                continue
        method = (it.get("download") or {}).get("method")
        if method not in AUTO_METHODS or it.get("access") in ("paid", "physical"):
            manual.append(it)
            continue
        if size_of(it) is None:
            skipped_unknown.append(it)
            continue
        eligible.append(it)

    groups = {}
    for it in eligible:
        groups.setdefault(it.get("group") or it["id"], []).append(it)
    for g in groups.values():
        g.sort(key=lambda x: (x.get("variant_rank") or 0, size_of(x)))

    chosen, used = {}, 0
    llm_cap = int(budget * a.llm_max)

    def llm_used():
        return sum(size_of(v) for v in chosen.values() if v["cat"].startswith("ai_models"))

    def fits(new, old=None):
        delta = size_of(new) - (size_of(old) if old else 0)
        if used + delta > budget:
            return False
        if new["cat"].startswith("ai_models"):
            if llm_used() + delta > llm_cap:
                return False
            if old is None and sum(1 for v in chosen.values() if v["cat"].startswith("ai_models")) >= a.llm_models:
                return False
        return True

    def pref_rank(g):
        for v in g:
            if v.get("variant_role") == "pref":
                return v.get("variant_rank") or 0
        return max((v.get("variant_rank") or 0) for v in g)

    order = sorted(groups.items(), key=lambda kv: (min(v["tier"] for v in kv[1]) if kv[0] not in
                                                   {v.get("group") or v["id"] for v in eligible if v["id"] in incl} else -1,
                                                   -max(v["_score"] for v in kv[1])))
    tiers = sorted({min(v["tier"] for v in g) for _, g in order} | {-1})

    def fill(tier_filter):
        nonlocal used
        sel = [(k, g) for k, g in order if tier_filter(k, g)]
        for k, g in sel:                       # 1) legkisebb változat
            if k in chosen:
                continue
            v = min(g, key=size_of)
            if fits(v):
                chosen[k] = v; used += size_of(v)
        for k, g in sel:                       # 2) feljavítás az ajánlott változatig
            if k not in chosen:
                continue
            pr = pref_rank(g)
            for v in sorted([x for x in g if (x.get("variant_rank") or 0) <= pr], key=size_of, reverse=True):
                if size_of(v) > size_of(chosen[k]) and fits(v, chosen[k]):
                    used += size_of(v) - size_of(chosen[k]); chosen[k] = v
                    break

    def tier_of(k, g):
        return -1 if any(v["id"] in incl for v in g) else min(v["tier"] for v in g)

    def is_llm(g):
        return g[0]["cat"].startswith("ai_models")

    def llm_pass():
        """LLM: modellenként a legjobb (intelligencia x kvant-minőség) beférő változat; 1 fő + 1 cenzúrázatlan + 1 kicsi tartalék + töltés."""
        nonlocal used
        def eff(v):
            b = v.get("llm_bits") or 4.5
            q = 0.55 if b < 2 else 0.75 if b < 3 else 0.9 if b < 4 else 1.0 if b < 5 else 1.03 if b < 7 else 1.05
            return (v.get("llm_aa") or 5) * q
        cands = sorted([v for k, g in groups.items() if is_llm(g) for v in g], key=lambda v: (-eff(v), size_of(v)))
        def take(pred):
            nonlocal used
            for v in cands:
                k = v.get("group") or v["id"]
                if k in chosen or not pred(v):
                    continue
                if fits(v):
                    chosen[k] = v; used += size_of(v)
                    return v
        take(lambda v: v["cat"] == "ai_models")
        if a.uncensored != "no":
            take(lambda v: v["cat"] == "ai_models_uncensored")
        take(lambda v: size_of(v) <= 20e9)
        while take(lambda v: True):
            pass

    for t in tiers:
        if t == 1:
            llm_pass()
        fill(lambda k, g, t=t: tier_of(k, g) == t and not is_llm(g))
    # 3) luxus-feljavítások (pl. képes Wikipedia) pontszám szerint
    for k, g in sorted(groups.items(), key=lambda kv: -max(v["_score"] for v in kv[1])):
        if k in chosen and not is_llm(g):
            for v in sorted(g, key=size_of, reverse=True):
                if size_of(v) > size_of(chosen[k]) and fits(v, chosen[k]):
                    used += size_of(v) - size_of(chosen[k]); chosen[k] = v
                    break
    # 4) átfedések kiszűrése (pl. Wikipedia-orvosi részhalmaz, ha a teljes WP bent van), majd újratöltés
    ids = {v["id"] for v in chosen.values()}
    for k in [k for k, v in chosen.items() if set(v.get("subsumed_by") or []) & ids]:
        used -= size_of(chosen[k]); del chosen[k]
    ids = {v["id"] for v in chosen.values()}
    for t in tiers:
        fill(lambda k, g, t=t: tier_of(k, g) == t and not is_llm(g) and not any(set(v.get("subsumed_by") or []) & ids for v in g))

    plan = sorted(chosen.values(), key=lambda x: (x["tier"], -x["_score"]))
    # szükséges olvasó/futtató eszközök (requires) – ha a katalógusban szerepelnek, mindig kerüljenek be
    need = {r for v in plan for r in (v.get("requires") or [])}
    byid = {it["id"]: it for it in items}
    tools = [byid[r] for r in sorted(need) if r in byid and r not in {v["id"] for v in plan}]
    for t in tools:
        if size_of(t):
            used += size_of(t)
    plan = tools + plan

    print(f"Profil: {a.profile} | keret: {a.budget} (használható {human(budget)}) | felhasználva: {human(used)} "
          f"| elemek: {len(plan)} | LLM: {human(llm_used())} (max {human(llm_cap)})\n")
    print(f"{'#':>3} {'T':>2} {'pont':>5} {'méret':>10}  {'mód':<11} id")
    for i, v in enumerate(plan, 1):
        print(f"{i:>3} {v['tier']:>2} {v['_score']:5.2f} {human(size_of(v)):>10}  {v['download']['method']:<11} {v['id']}"
              + ("  (becsült méret)" if not v.get("bytes") else ""))
    left = sorted([it for k, g in groups.items() if k not in chosen for it in g[:1]], key=lambda x: (x["tier"], -x["_score"]))
    if left:
        print(f"\nKimaradt (nem fért be) – első 15 a fontosság szerint:")
        for v in left[:15]:
            print(f"     T{v['tier']} {v['_score']:5.2f} {human(size_of(v)):>10}  {v['id']}")
    if manual:
        print(f"\nKÉZI TEENDŐK (fizetős / regisztrációs / fizikai / kézi letöltés) – emberi döntés kell:")
        for v in sorted(manual, key=lambda x: (x["tier"], -x["_score"])):
            print(f"     T{v['tier']} {v['_score']:5.2f} {v['access']:<17} {v.get('price') or '':<14} {v['id']}  {v.get('info_url')}")
    if skipped_unknown:
        print("\nIsmeretlen méret miatt kihagyva (ellenőrizd kézzel):", ", ".join(v["id"] for v in skipped_unknown))

    json.dump({"budget_bytes": budget, "used_bytes": used, "profile": a.profile,
               "items": [{k: v[k] for k in v if not k.startswith("_")} | {"score": v["_score"]} for v in plan],
               "manual": [v["id"] for v in manual]}, open(a.out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"\nTerv mentve: {a.out}")
    if a.emit_sh:
        write_sh(plan, a.emit_sh, a.dest)
        print(f"Letöltő szkript: {a.emit_sh}  (futtatás előtt nézd át!)")


def write_sh(plan, path, dest):
    q = shlex.quote
    L = ["#!/usr/bin/env bash", "# ARCHIVUM letöltő – generálva select_items.py által. Újraindítható (resume).",
         "set -uo pipefail", f"DEST=${{DEST:-{q(dest)}}}", 'LOG="$DEST/_log.txt"; mkdir -p "$DEST"',
         'have(){ command -v "$1" >/dev/null 2>&1; }',
         'fetch(){ # url outdir',
         '  local ua=${UA:-Mozilla/5.0 (X11; Linux x86_64; rv:140.0) Gecko/20100101 Firefox/140.0}',
         '  if have aria2c; then aria2c -c -x8 -s8 --auto-file-renaming=false -U "$ua" -d "$2" "$1"; else (cd "$2" && wget -c -U "$ua" "$1"); fi; }',
         'kiwix_latest(){ # book flavour fallback_url -> legfrissebb URL az OPDS katalógusból',
         '  local u; u=$(curl -fsSL "https://library.kiwix.org/catalog/v2/entries?name=$1&count=50" 2>/dev/null \\',
         '    | tr "\\n" " " | sed "s#<entry>#\\n#g" | { if [ -n "$2" ]; then grep "<flavour>$2</flavour>"; else cat; fi; } \\',
         '    | grep -o "https://[^\\"]*\\.zim\\.meta4" | sed "s/\\.meta4$//" | sort | tail -1)',
         '  echo "${u:-$3}"; }',
         'ok(){ echo "OK   $1" | tee -a "$LOG"; }; fail(){ echo "FAIL $1" | tee -a "$LOG"; }', ""]
    for v in plan:
        d = v["download"]; m = d["method"]; sub = f'$DEST/{v["cat"]}/{v["id"]}'
        L.append(f"# --- {v['id']}  ({human(size_of(v))})  {v.get('name','')}")
        L.append(f'mkdir -p "{sub}"')
        if m == "kiwix":
            L.append(f'U=$(kiwix_latest {q(d["book"])} {q(d.get("flavour") or "")} {q(d.get("url") or "")}); F="{sub}/${{U##*/}}"')
            L.append(f'if have aria2c; then aria2c -c --auto-file-renaming=false --seed-time=0 -d "{sub}" "$U.meta4" || fetch "$U" "{sub}"; else fetch "$U" "{sub}"; fi')
            L.append(f'(cd "{sub}" && curl -fsSL "$U.sha256" | sha256sum -c -) && ok {q(v["id"])} || fail {q(v["id"])}')
        elif m in ("http", "jigdo"):
            for u in (d.get("urls") or [d.get("url")]):
                if u:
                    L.append(f'fetch {q(u)} "{sub}" && ok {q(v["id"])} || fail {q(v["id"])}')
        elif m == "wget-mirror":
            L.append(f'(cd "{sub}" && wget -m -np -k -E -c -e robots=off --wait=1 --random-wait -U "Mozilla/5.0 (X11; Linux x86_64; rv:140.0) Gecko/20100101 Firefox/140.0" {d.get("wget_args","")} {q(d["url"])}) && ok {q(v["id"])} || fail {q(v["id"])}')
        elif m == "rsync":
            L.append(f'rsync -avP --partial {d.get("rsync_args","")} {q(d["url"])} "{sub}/" && ok {q(v["id"])} || fail {q(v["id"])}')
        elif m == "git":
            for u in (d.get("repos") or [d.get("url")]):
                n = u.rstrip("/").split("/")[-1]
                L.append(f'[ -d "{sub}/{n}.git" ] || git clone --mirror {q(u)} "{sub}/{n}.git"; '
                         f'git -C "{sub}/{n}.git" remote update && git -C "{sub}/{n}.git" bundle create "{sub}/{n}.bundle" --all && ok {q(v["id"])} || fail {q(v["id"])}')
        elif m == "hf":
            inc = " ".join(f"--include {q(p)}" for p in (d.get("include") or []))
            L.append(f'hf download {q(d["repo"])} {inc} --local-dir "{sub}" && ok {q(v["id"])} || fail {q(v["id"])}')
        elif m == "ollama":
            L.append(f'ollama pull {q(d["tag"])} && ok {q(v["id"])} || fail {q(v["id"])}   # tárolás: ~/.ollama/models (vagy $OLLAMA_MODELS)')
        elif m == "archive.org":
            for ident in (d.get("ids") or [d.get("id")]):
                glob = f' --glob={q(d["glob"])}' if d.get("glob") else ""
                L.append(f'ia download {q(ident)}{glob} --destdir "{sub}" && ok {q(v["id"])} || fail {q(v["id"])}')
        elif m == "torrent":
            L.append(f'aria2c -c --seed-time=0 -d "{sub}" {q(d.get("url") or d.get("magnet"))} && ok {q(v["id"])} || fail {q(v["id"])}')
        elif m == "agent":
            L.append(f'# AGENT-FELADAT: ezt az AI-nak kell egyedileg megoldania (lista összegyűjtése API/OAI-PMH/oldal alapján, majd fetch).')
            L.append(f'# Leírás: {d.get("note","")}'.replace("\n", " "))
            for u in d.get("seed_urls") or []:
                L.append(f'#   kiinduló URL: {u}')
            L.append(f'echo "TODO {v["id"]}" | tee -a "$LOG"')
        elif m == "s3":
            L.append(f'# S3: {d.get("note","")}\n# aws s3 sync {d.get("url")} "{sub}" {d.get("s3_args","")}')
        L.append("")
    L.append('echo "Kész. Napló: $LOG"; grep -c FAIL "$LOG" || true')
    open(path, "w").write("\n".join(L) + "\n")


if __name__ == "__main__":
    main()
