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
import argparse, json, math, os, re, sys, shlex

PROFILES = {  # súlyok: S=túlélés R=újjáépítés A=gyakorlatiasság U=pótolhatatlanság Q=megbízhatóság O=offline-kényelem
    "balanced":  {"S": .30, "R": .25, "A": .15, "U": .15, "Q": .10, "O": .05},
    "survival":  {"S": .45, "R": .10, "A": .20, "U": .10, "Q": .10, "O": .05},
    "rebuild":   {"S": .15, "R": .40, "A": .15, "U": .15, "Q": .10, "O": .05},
    "education": {"S": .10, "R": .35, "A": .10, "U": .15, "Q": .20, "O": .10},
    "computing": {"S": .05, "R": .40, "A": .20, "U": .15, "Q": .10, "O": .10},
}
MEM_CAP = {"T5": 10e9, "T4": 100e9, "T3": 220e9, "T2": 900e9, "T1": 1e18}  # alapértelmezett max. modellméret hardverszintenként
AUTO_METHODS = {"agent", "jigdo", "kiwix", "http", "wget-mirror", "rsync", "git", "hf", "ollama", "archive.org", "torrent"}
UNITS = {"B": 1, "KB": 1e3, "MB": 1e6, "GB": 1e9, "TB": 1e12, "PB": 1e15, "K": 1e3, "M": 1e6, "G": 1e9, "T": 1e12, "P": 1e15,
         "KIB": 2**10, "MIB": 2**20, "GIB": 2**30, "TIB": 2**40}
LANG_WORDS = {"hu": "hungarian", "en": "english"}


def lang_ok(lang, langs):
    l = (lang or "").lower()
    if l == "multi" or l in langs:
        return True
    toks = set(re.findall(r"[a-z]+", l))
    return bool(toks & langs) or any(LANG_WORDS.get(x, "\0") in l for x in langs)


def parse_size(s, default_unit="GB"):
    m = re.fullmatch(r"\s*(\d+(?:[.,]\d+)?)\s*([A-Za-z]*)\s*", s)
    u = (m.group(2) or default_unit).upper() if m else None
    if not m or u not in UNITS:
        sys.exit(f"Érvénytelen méret: {s!r} (pl. 512GB, 2TB, 1.5TiB)")
    return int(float(m.group(1).replace(",", ".")) * UNITS[u])


def human(b):
    if b is None:
        return "?"
    for u, f in (("TB", 1e12), ("GB", 1e9), ("MB", 1e6), ("KB", 1e3)):
        if b >= f:
            return f"{b / f:.2f} {u}".replace(".", ",")
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


class HuFormatter(argparse.RawDescriptionHelpFormatter):
    def add_usage(self, usage, actions, groups, prefix=None):
        return super().add_usage(usage, actions, groups, "Használat: ")


class HuParser(argparse.ArgumentParser):
    """argparse magyar keretszövegekkel (súgó és hibaüzenetek)."""
    TR = (("the following arguments are required", "hiányzó kötelező argumentum"), ("expected one argument", "egy értéket vár"),
          ("invalid choice", "érvénytelen választás"), ("choose from", "választható"), ("unrecognized arguments", "ismeretlen argumentum"),
          ("invalid float value", "érvénytelen szám"), ("invalid int value", "érvénytelen egész szám"), ("argument ", "argumentum: "))

    def __init__(self, **k):
        super().__init__(add_help=False, formatter_class=HuFormatter, **k)
        self._positionals.title, self._optionals.title = "kötelező argumentum", "kapcsolók"
        self.add_argument("-h", "--help", action="help", help="ez a súgó")

    def error(self, message):
        for a, b in self.TR:
            message = message.replace(a, b)
        self.print_usage(sys.stderr)
        self.exit(2, f"{self.prog}: hiba: {message}\n")


def run_cli(main):
    try:
        main()
    except BrokenPipeError:            # pl. --list | head
        os.dup2(os.open(os.devnull, os.O_WRONLY), sys.stdout.fileno()); sys.exit(1)


def main():
    ap = HuParser(description=__doc__)
    ap.add_argument("catalog", help="ARCHIVUM.md vagy .jsonl katalógus")
    ap.add_argument("--budget", help="pl. 64GB, 512GB, 2TB (decimális egység, mint a meghajtók címkéje)")
    ap.add_argument("--reserve", type=float, default=0.08, help="tartalék hányad a fájlrendszernek / checksumoknak (alap 0.08)")
    ap.add_argument("--profile", default="balanced", choices=PROFILES, help="súlyprofil (alap: %(default)s)")
    ap.add_argument("--langs", default="hu,en,multi", help="engedett nyelvek, vesszővel (alap: %(default)s)")
    ap.add_argument("--access", default="free,free-registration,donation",
                    help="engedett hozzáférés: free,free-registration,donation,paid,gray,physical")
    ap.add_argument("--hw", default=None, choices=["T1", "T2", "T3", "T4", "T5"], help="LLM hardverszint T1..T5 (T1 szerver, T2 munkaállomás, T3 gamer PC, T4 laptop, T5 telefon); nélküle nem kerül be LLM")
    ap.add_argument("--llm-max", type=float, default=0.35, help="a keret max. ennyi hányada mehet LLM-súlyokra (alap: %(default)s)")
    ap.add_argument("--platform", default="", help="LLM-formátumok a GGUF/Ollama mellé: mac (MLX), server (vLLM/SGLang: FP8/NVFP4/AWQ), android (LiteRT); vesszővel")
    ap.add_argument("--uncensored", choices=["no", "also", "only"], default="also", help="cenzúrázatlan LLM-változatok: no | also | only")
    ap.add_argument("--max-uncensored", type=int, default=None, help="legfeljebb ennyi cenzúrázatlan LLM-modell (alap: nincs külön korlát)")
    ap.add_argument("--llm-models", type=int, default=3, help="legfeljebb ennyi különböző LLM-modell (group) kerüljön be (alap: %(default)s)")
    ap.add_argument("--mem", default=None, help="LLM-re használható memória (RAM+VRAM vagy unified), pl. 48GB / 512GB; a modell max. 85%%-a lehet")
    ap.add_argument("--focus", default="", help="kategória-szorzók, pl. medicine=2,agriculture=1.5")
    ap.add_argument("--max-tier", type=int, default=5, help="legfeljebb ennyi tier (0–5) kerüljön be, alap 5")
    ap.add_argument("--include", default="", help="kötelezően beveendő id-k (vesszővel)")
    ap.add_argument("--exclude", default="", help="kizárt id-k vagy kategóriák (cat:NAME)")
    ap.add_argument("--list", action="store_true", help="katalógus listázása pontszám szerint")
    ap.add_argument("--out", default="plan.json", help="a terv JSON-fájlja (alap plan.json)")
    ap.add_argument("--emit-sh", default=None, help="letöltő bash szkript írása ide")
    ap.add_argument("--dest", default="/mnt/archivum", help="célkönyvtár a szkriptben (alap: %(default)s; futáskor DEST=... felülírja)")
    a = ap.parse_args()

    try:
        items = sorted(load(a.catalog), key=lambda i: i["id"])
    except (OSError, UnicodeDecodeError, ValueError, KeyError) as e:
        sys.exit(f"Nem olvasható katalógus: {a.catalog} ({e})")   # determinisztikus sorrend (holtversenynél is)
    w = PROFILES[a.profile]
    cats, ids = {it["cat"] for it in items}, {it["id"] for it in items}
    unk = sorted({p.split("=")[0] for p in a.focus.split(",") if p} - cats) + sorted(
        x for x in a.exclude.split(",") if x and (x[4:] not in cats if x.startswith("cat:") else x not in ids))
    if unk:
        print(f"FIGYELEM: ismeretlen kategória / azonosító (--focus / --exclude): {', '.join(unk)}", file=sys.stderr)
    try:
        focus = {k: float(v) for k, v in (p.split("=") for p in a.focus.split(",") if p)}
    except ValueError:
        ap.error("--focus formátuma: kategória=szorzó, pl. medicine=2,agriculture=1.5")
    if not 0 <= a.reserve < 1:
        ap.error("--reserve 0 és 1 közötti hányad (pl. 0.08)")
    if not 0 <= a.llm_max <= 1:
        ap.error("--llm-max 0 és 1 közötti hányad (alap 0.35)")
    if a.llm_models < 0 or not 0 <= a.max_tier <= 5:
        ap.error("--llm-models >= 0 és --max-tier 0–5 kell")
    if any(not (math.isfinite(v) and v >= 0) for v in focus.values()):
        ap.error("--focus szorzói véges, nemnegatív számok legyenek")
    bad = (set(x for x in a.access.split(",") if x) - {"free", "free-registration", "donation", "paid", "gray", "physical"}) | \
          (set(x for x in a.platform.split(",") if x) - {"mac", "server", "android"})
    if bad or not a.access.strip(",") or not a.langs.strip(","):
        ap.error(f"ismeretlen / üres --access, --platform vagy --langs érték: {', '.join(sorted(bad)) or '(üres)'}")
    if a.mem and parse_size(a.mem) <= 0:
        ap.error("--mem pozitív méret legyen (pl. 48GB)")
    if not a.hw and (a.mem or a.platform or a.uncensored != "also"):
        print("FIGYELEM: --hw nélkül nem kerül be LLM; a --mem / --platform / --uncensored hatástalan", file=sys.stderr)
    for it in items:
        it["_score"] = composite(it, w, focus)

    if a.list:
        for it in sorted(items, key=lambda x: (x["tier"], -x["_score"])):
            print(f"T{it['tier']} {it['_score']:5.2f} {human(size_of(it)):>10} {it['access']:<17} {it['cat']:<17} {it['id']}")
        return
    if not a.budget:
        sys.exit("--budget kötelező (vagy --list)")

    budget = int(parse_size(a.budget) * (1 - a.reserve))
    if budget <= 0:
        sys.exit("--budget pozitív méret legyen (pl. 64GB)")
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
        if not lang_ok(it.get("lang"), langs) and it["id"] not in incl:
            continue
        if it.get("access") not in access:
            continue
        if it["cat"] in ("ai_tools",) or it["id"] == "tool-ollama-installers":
            if not a.hw:
                continue
        if it["cat"].startswith("ai_models"):
            if it.get("moe") is False and (it.get("llm_bits") or 9) < 2.5:   # mint llm_calc.unusable_quant
                continue
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
        if method == "hf" and not it["download"].get("repo"):
            method = "manual"
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
    byid = {it["id"]: it for it in items}

    def missing_deps(v):
        have = {x["id"] for x in chosen.values()}
        return [byid[r] for r in (v.get("requires") or []) if r in byid and r not in have and r not in excl and f"cat:{byid[r]['cat']}" not in excl]

    def choose(k, v):
        nonlocal used
        for t in missing_deps(v):
            chosen[t.get("group") or t["id"]] = t; used += size_of(t) or 0
        chosen[k] = v; used += size_of(v)

    def llm_used():
        return sum(size_of(v) for v in chosen.values() if v["cat"].startswith("ai_models"))

    def fits(new, old=None):
        delta = size_of(new) - (size_of(old) if old else 0) + sum(size_of(t) or 0 for t in missing_deps(new))
        if used + delta > budget:
            return False
        if new["cat"].startswith("ai_models"):
            if llm_used() + delta > llm_cap:
                return False
            if old is None and sum(1 for v in chosen.values() if v["cat"].startswith("ai_models")) >= a.llm_models:
                return False
            if (old is None and new["cat"] == "ai_models_uncensored" and a.max_uncensored is not None
                    and sum(1 for v in chosen.values() if v["cat"] == "ai_models_uncensored") >= a.max_uncensored):
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
            forced = [x for x in g if x["id"] in incl]
            v = forced[0] if forced else min(g, key=size_of)
            if fits(v):
                choose(k, v)
        for k, g in sel:                       # 2) feljavítás az ajánlott változatig
            if k not in chosen or chosen[k]["id"] in incl:
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
            if v.get("moe") is False:   # mint llm_calc.qf(dense)
                q = 0.15 if b < 2 else 0.6 if b < 3 else 0.85 if b < 4 else 1.0 if b < 5 else 1.03 if b < 7 else 1.05
            else:
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
                    choose(k, v)
                    return v
        while take(lambda v: v["id"] in incl):
            pass
        take(lambda v: v["cat"] == "ai_models")
        if a.uncensored != "no":
            take(lambda v: v["cat"] == "ai_models_uncensored")
        take(lambda v: size_of(v) <= 20e9)
        while take(lambda v: True):
            pass

    def upgrade(maxtier=9):
        """luxus-feljavítások (pl. képes Wikipedia) pontszám szerint; maxtier: csak az ennél nem kisebb fontosságú csoportok"""
        nonlocal used
        for k, g in sorted(groups.items(), key=lambda kv: -max(v["_score"] for v in kv[1])):
            if k in chosen and not is_llm(g) and chosen[k]["id"] not in incl and tier_of(k, g) <= maxtier:
                for v in sorted(g, key=size_of, reverse=True):
                    if size_of(v) > size_of(chosen[k]) and fits(v, chosen[k]):
                        used += size_of(v) - size_of(chosen[k]); chosen[k] = v
                        break

    llm_done = False
    for t in tiers:
        if t >= 1 and not llm_done:
            llm_pass(); llm_done = True
        fill(lambda k, g, t=t: tier_of(k, g) == t and not is_llm(g))
        if t == 1:
            upgrade(1)      # a 0–1. szintű csoportok bővített változata a 2. szintű új tételek előtt jön
    # 3) luxus-feljavítások a maradék helyen
    upgrade()
    # 4) átfedések kiszűrése (pl. Wikipedia-orvosi részhalmaz, ha a teljes WP bent van), majd újratöltés
    for _ in range(10):
        ids = {v["id"] for v in chosen.values() if v["download"]["method"] != "agent"}   # AI-feladat nem helyettesít automatikus letöltést
        drop = [k for k, v in chosen.items() if set(v.get("subsumed_by") or []) & ids and v["id"] not in incl]
        if not drop:
            break
        for k in drop:
            used -= size_of(chosen[k]); del chosen[k]
        ids = {v["id"] for v in chosen.values() if v["download"]["method"] != "agent"}
        for t in tiers:
            fill(lambda k, g, t=t: tier_of(k, g) == t and not is_llm(g) and not any(set(v.get("subsumed_by") or []) & ids for v in g))

    plan = sorted(chosen.values(), key=lambda x: (x["tier"], -x["_score"]))
    # szükséges olvasó/futtató eszközök (requires) – ha a katalógusban szerepelnek, mindig kerüljenek be
    need = {r for v in plan for r in (v.get("requires") or [])}
    tools = []  # függőségek már a kiválasztáskor bekerültek (choose/missing_deps)
    for t in tools:
        if size_of(t):
            used += size_of(t)
    plan = tools + plan

    try:
        out = open(a.out, "w", encoding="utf-8")
    except OSError as e:
        sys.exit(f"Nem írható: {a.out} ({e})")
    json.dump({"budget_bytes": budget, "used_bytes": used, "profile": a.profile,
               "items": [{k: v[k] for k in v if not k.startswith("_")} | {"score": v["_score"]} for v in plan],
               "manual": [v["id"] for v in manual]}, out, ensure_ascii=False, indent=1)
    out.close()
    if a.emit_sh:
        try:
            write_sh(plan, a.emit_sh, a.dest)
        except OSError as e:
            sys.exit(f"Nem írható: {a.emit_sh} ({e})")
    print(f"Profil: {a.profile} | keret: {a.budget} (használható {human(budget)}) | felhasználva: {human(used)} "
          f"| elemek: {len(plan)} | LLM: {human(llm_used())} (max {human(llm_cap)})\n")
    print(f"{'#':>3} {'T':>2} {'pont':>5} {'méret':>10}  {'mód':<11} id")
    for i, v in enumerate(plan, 1):
        print(f"{i:>3} {v['tier']:>2} {v['_score']:5.2f} {human(size_of(v)):>10}  {v['download']['method']:<11} {v['id']}"
              + ("  (becsült méret)" if not v.get("bytes") else ""))
    ag = sum(size_of(v) or 0 for v in plan if v["download"]["method"] == "agent")
    if ag:
        print(f"Ebből AI-feladat (nem automatikus, a dl.sh TODO-ként jelzi): {human(ag)} – "
              f"{sum(1 for v in plan if v['download']['method'] == 'agent')} tétel (API/OAI-PMH-lista, S3, több fájlos készletek)")
    miss = sorted(x for x in incl if x not in {v["id"] for v in plan})
    if miss:
        known = {it["id"] for it in items}
        for x in miss:
            why = "ismeretlen azonosító" if x not in known else "nem fér el a keretben, ki van zárva (--exclude / nyelv / hozzáférés / hardver), vagy fizetős/kézi tétel"
            print(f"FIGYELEM: a kötelezőnek kért tétel nem került be: {x} – {why}")
    left = sorted([it for k, g in groups.items() if k not in chosen for it in g[:1]], key=lambda x: (x["tier"], -x["_score"]))
    if left:
        print(f"\nKimaradt – első 15 a fontosság szerint (ok: hely / átfedés / LLM-darabszám):")
        pids = {v["id"] for v in plan}
        nllm = len({v.get("group") for v in plan if v["cat"].startswith("ai_models")})
        for v in left[:15]:
            ov = set(v.get("subsumed_by") or []) & pids
            why = ("átfedés: " + ",".join(sorted(ov))) if ov else ("LLM-darabszám (--llm-models)" if v["cat"].startswith("ai_models") and nllm >= a.llm_models else "hely")
            print(f"     T{v['tier']} {v['_score']:5.2f} {human(size_of(v)):>10}  {v['id']}  [{why}]")
    if manual:
        print(f"\nKÉZI TEENDŐK (fizetős / regisztrációs / fizikai / kézi letöltés) – emberi döntés kell:")
        for v in sorted(manual, key=lambda x: (x["tier"], -x["_score"])):
            print(f"     T{v['tier']} {v['_score']:5.2f} {v['access']:<17} {v.get('price') or '':<14} {v['id']}  {v.get('info_url')}")
    if skipped_unknown:
        print("\nIsmeretlen méret miatt kihagyva (ellenőrizd kézzel):", ", ".join(v["id"] for v in skipped_unknown))

    print(f"\nTerv mentve: {a.out}")
    if a.emit_sh:
        print(f"Letöltő szkript: {a.emit_sh}  (futtatás előtt nézd át!)")


GH_RELEASE_SH = [
    'gh_release(){ # owner/repo tag célkönyvtár [tételkeret MB] – GitHub-kiadás fő telepítői platformonként (alap: Linux x86-64, Windows x64, Android APK), a terv szerinti méretkerettel',
    '  local a list="" u r=0 cap="${4:-4000}" alt="" used',
    '  if [ -f "$3/.ok" ] && [ -z "${REFRESH:-}" ]; then return 0; fi   # már teljesen letöltve (REFRESH=1: újra)',
    '  used=$(du -smc "$(dirname "$3")"/*.git 2>/dev/null | tail -1 | cut -f1); cap=$(( cap - ${used:-0} ))   # a keretből csak a git-tükör jön le',
    '  [ "$cap" -gt 0 ] || { echo "FIGYELEM: $1 – a tétel kerete elfogyott a forráskódra, telepítő nem fér" >&2; return 1; }',
    '  [ -n "$2" ] && [ "${2#v}" = "$2" ] && alt="tags/v$2"   # v-előtagos tagnél nincs dupla API-hívás',
    '  have python3 || return 1',
    '  [ -n "${GITHUB_TOKEN:-}" ] || [ -n "${_GHWARN:-}" ] || { _GHWARN=1; echo "FIGYELEM: GITHUB_TOKEN nélkül a GitHub API óránként 60 kérést enged; a többi telepítő TODO lesz (export GITHUB_TOKEN=...)" >&2; }',
    '  for a in ${2:+"tags/$2"} ${alt:+"$alt"} latest; do   # a katalógus-verzió tagje (v-vel / nélküle), különben a legutóbbi kiadás',
    '  list=$(curl -fsSL ${GITHUB_TOKEN:+-H "Authorization: Bearer $GITHUB_TOKEN"} "https://api.github.com/repos/$1/releases/$a" 2>/dev/null | GH_ITEM_MB="$cap" python3 -c \'import sys, json, re, os',
    'd = json.load(sys.stdin); mx = float(os.environ.get("GH_ASSET_MAX_MB", "1500")) * 1e6; tot = min(float(os.environ.get("GH_RELEASE_MAX_MB", "4000")), float(os.environ.get("GH_ITEM_MB", "4000"))) * 1e6',
    'ok = re.compile(os.environ.get("GH_ASSET_RE", r"((linux|appimage).*(x86_64|amd64|x64)|(x86_64|amd64|x64).*(linux|appimage|\\.deb$|\\.tar\\.(gz|xz|zst)$)|win(dows)?[-_.]?(x64|x86_64|amd64|64)|(x64|x86_64|amd64).*\\.(exe|msi|zip)$|\\.msi$|win64|\\.apk$|darwin|macos|osx|\\.dmg$|\\.pkg$)"), re.I)',
    'bad = re.compile(r"(debug|symbols|dbgsym|pdbs?\\b|[-_.]reh[-_.]|server|[-_.]web[-_.]|sha\\d+|checksum|\\.sig$|\\.asc$|\\.txt$|\\.md5$|\\.blockmap$|\\.ya?ml$|\\.json$|\\.zsync$)", re.I)',
    'arch = re.compile(os.environ.get("GH_ASSET_EXCL", r"(darwin|macos|apple|osx|freebsd|openbsd|netbsd|aarch64|arm64|armv\\d|armhf|riscv|s390|ppc|mips|i[3-6]86)"), re.I)   # más platform (APK kivétel)',
    'def plat(n):',
    '    n = n.lower()',
    '    return "apk" if n.endswith(".apk") else "mac" if re.search(r"darwin|macos|osx|\\.dmg$|\\.pkg$", n) else "win" if re.search(r"win|\\.exe$|\\.msi$", n) else "linux"',
    'def prio(n):   # platformon belül a fő telepítő: Windows setup.exe > msi > zip/7z; Linux AppImage > tar > deb',
    '    n = n.lower()',
    '    return 3 if re.search(r"(setup|install).*\\.exe$|\\.appimage$", n) else 2 if re.search(r"\\.exe$|\\.msi$|\\.tar\\.(gz|xz|zst)$|universal.*\\.apk$", n) else 1',
    'P = os.environ.get("GH_PLATFORMS", "linux,win,apk").split(",")',
    'c = [a for a in d.get("assets", []) if ok.search(a["name"]) and not bad.search(a["name"]) and (a["name"].lower().endswith(".apk") or (plat(a["name"]) == "mac" and "mac" in P) or not arch.search(a["name"])) and a.get("size", 0) <= mx]',
    'for p in P:   # platformonként egy fő telepítő, ami még belefér a keretbe (macOS: GH_PLATFORMS=linux,win,apk,mac)',
    '    for a in sorted([a for a in c if plat(a["name"]) == p], key=lambda a: (-prio(a["name"]), -a.get("size", 0))):',
    '        if a.get("size", 0) <= tot: tot -= a.get("size", 0); print(a["browser_download_url"]); break\' 2>/dev/null) && [ -n "$list" ] && break',
    '  done; [ -n "$list" ] || return 1',
    '  mkdir -p "$3"; for u in $list; do fetch "$u" "$3" || r=1; done; [ $r = 0 ] && touch "$3/.ok"; return $r; }',
]


def write_sh(plan, path, dest):
    q = shlex.quote
    c = lambda x: str(x or "").replace("\r", " ").replace("\n", " ")       # kommentbe biztonságos
    safe = lambda x: re.sub(r"[^A-Za-z0-9._+-]", "_", str(x))            # "..."-be ágyazott útvonalelemekhez
    methods = {v["download"]["method"] for v in plan}
    plan_ids = {v["id"] for v in plan}
    need_tools = sorted({"curl"} | {t for m, ts in {"kiwix": ["curl"], "http": ["aria2c|wget"], "wget-mirror": ["wget"], "rsync": ["rsync"],
                         "git": ["git", "python3"], "jigdo": ["jigdo-lite"], "hf": ["hf|huggingface-cli"], "ollama": ["ollama"], "archive.org": ["ia"],
                         "torrent": ["aria2c"], "agent": ["python3"]}.items() if m in methods for t in ts})
    L = ["#!/usr/bin/env bash", "# ARCHIVUM letöltő – generálva select_items.py által. Újraindítható (resume).",
         "set -uo pipefail", f"DEST=${{DEST:-{q(dest)}}}", 'case "$DEST" in /*) ;; *) echo "DEST abszolút útvonal legyen (pl. /media/archivum)" >&2; exit 2;; esac',
         'DEST=$(realpath -m -- "$DEST" 2>/dev/null || python3 -c "import os,sys; print(os.path.realpath(sys.argv[1]))" "$DEST")   # ../ és szimlinkek feloldva',
         '_d=$(printf "%s" "$DEST" | tr -s / | sed -e "s#/\\./#/#g" -e "s#/\\.\\$##" -e "s#\\(.\\)/\\$#\\1#")   # //etc, /etc/, /./ → /etc, /',
         'case "$_d" in ""|/|/bin|/bin/*|/sbin|/sbin/*|/boot|/boot/*|/etc|/etc/*|/usr|/usr/*|/proc|/proc/*|/sys|/sys/*|/dev|/dev/*|/root|/var|/var/*|/lib|/lib/*|/lib64|/lib64/*|/opt|/home|/tmp|/Users|/System|/System/*|/Library|/Applications|/private|/private/etc|/private/etc/*|/private/var|/private/var/*|/private/tmp|"${HOME:-/nonexistent}")',
         '  echo "Hibás célkönyvtár: DEST=\\"$DEST\\" – adj meg egy külön meghajtót/mappát, pl. DEST=/media/archivum" >&2; exit 2;; esac',
         '_p=$DEST; while [ ! -d "$_p" ]; do _p=$(dirname "$_p"); done; if [ "$(df -P "$_p" 2>/dev/null | awk \'NR==2{print $6}\')" = / ]; then echo "FIGYELEM: $DEST nem külön csatolt meghajtón van – ellenőrizd, hogy nem a rendszerlemezt töltöd-e tele (Ctrl+C 10 mp-en belül)." >&2; sleep 10; fi', 'mkdir -p "$DEST"; LOG="$DEST/_log.txt"; RUNLOG="$DEST/_log_$(date +%Y%m%d-%H%M%S).txt"',
         'have(){ command -v "$1" >/dev/null 2>&1; }',
         'anyhave(){ local t; for t in ${1//|/ }; do have "$t" && return 0; done; return 1; }',
         "for t in " + " ".join(q(t) for t in need_tools) + '; do anyhave "$t" || echo "FIGYELEM: hiányzó eszköz: $t – az ezt igénylő tételek FAIL-lel végződnek"; done',
         'sha256c(){ if have sha256sum; then sha256sum -c -; else shasum -a 256 -c -; fi; }',
         'fetch(){ # url outdir',
         '  local ua=${UA:-Mozilla/5.0 (X11; Linux x86_64; rv:140.0) Gecko/20100101 Firefox/140.0}',
         '  if have aria2c; then aria2c -c -x8 -s8 --auto-file-renaming=false -U "$ua" -d "$2" "$1"; else (cd "$2" && wget -c --content-disposition --trust-server-names -U "$ua" "$1"); fi; }',
         'ollama_pull(){ # tag célkönyvtár: külön portú ideiglenes szerver, hogy a modell a meghajtóra kerüljön',
         '  local h=127.0.0.1:11499 r',
         '  if OLLAMA_HOST=$h ollama list >/dev/null 2>&1; then echo "FIGYELEM: a $h porton már fut egy ollama-szerver (régi futás?) – állítsd le"; return 1; fi',
         '  OLLAMA_MODELS="$2" OLLAMA_HOST=$h ollama serve >/dev/null 2>&1 & _OP=$!',
         "  trap 'kill $_OP 2>/dev/null' EXIT; trap 'kill $_OP 2>/dev/null; exit 130' INT; trap 'kill $_OP 2>/dev/null; exit 143' TERM",
         '  for _ in $(seq 1 60); do OLLAMA_HOST=$h ollama list >/dev/null 2>&1 && break; kill -0 $_OP 2>/dev/null || break; sleep 1; done',
         '  kill -0 $_OP 2>/dev/null && OLLAMA_HOST=$h ollama pull "$1"; r=$?',
         '  kill $_OP 2>/dev/null; wait $_OP 2>/dev/null; trap - EXIT INT TERM; return $r; }',
         'git_mirror(){ # url bare-könyvtár [tag]: csak ágak+tagek; sekély (tag vagy HEAD), GIT_FULL=1: teljes történet; mindig klónozható HEAD',
         '  local u=$1 g=$2 t=${3:-} h',
         '  if git -C "$g" remote get-url origin >/dev/null 2>&1; then git -C "$g" remote set-url origin "$u"; else git init -q --bare "$g" && git -C "$g" remote add origin "$u"; fi || return 1',
         '  git -C "$g" config --replace-all remote.origin.fetch "+refs/heads/*:refs/heads/*" && git -C "$g" config --add remote.origin.fetch "+refs/tags/*:refs/tags/*" || return 1',
         '  if [ -n "${GIT_FULL:-}" ] || { [ ! -f "$g/shallow" ] && git -C "$g" rev-parse -q --verify HEAD >/dev/null; }; then   # egyszer teljes → teljes marad',
         '    if [ -f "$g/shallow" ]; then git -C "$g" fetch -q --tags --unshallow origin; else git -C "$g" fetch -q --tags origin; fi || return 1',
         '    h=$(git -C "$g" ls-remote --symref origin HEAD 2>/dev/null | awk \'$1=="ref:"{print $2; exit}\'); [ -n "$h" ] && git -C "$g" symbolic-ref HEAD "$h"',
         '  else',
         '    { [ -n "$t" ] && git -C "$g" fetch -q --depth 1 origin "refs/tags/$t:refs/tags/$t" && git -C "$g" update-ref refs/heads/snapshot "refs/tags/$t^{commit}"; } \\',
         '      || git -C "$g" fetch -q --depth 1 origin "+HEAD:refs/heads/snapshot" || return 1',
         '    git -C "$g" symbolic-ref HEAD refs/heads/snapshot',
         '  fi',
         '  if [ -n "${BUNDLE:-}" ]; then   # BUNDLE=1: +1x hely; sekély tükörből nem klónozható bundle lenne',
         '    if [ -f "$g/shallow" ]; then echo "FIGYELEM: $g sekély – a BUNDLE-höz GIT_FULL=1 kell"; else git -C "$g" bundle create "${g%.git}.bundle" --all; fi',
         '  fi; }',
         *GH_RELEASE_SH,
         'hfdl(){ if have hf; then hf download "$@"; elif have huggingface-cli; then huggingface-cli download "$@"; else return 127; fi; }',
         'kiwix_latest(){ # book flavour fallback_url -> legfrissebb URL az OPDS katalógusból (GNU és BSD sed-del is)',
         '  local u; u=$(curl -fsSL "https://library.kiwix.org/catalog/v2/entries?name=$1&count=50" 2>/dev/null \\',
         "    | tr '\\n' ' ' | sed $'s#<entry>#\\\\\\n#g' | grep \"<name>$1</name>\" \\",
         '    | { if [ -n "$2" ]; then grep "<flavour>$2</flavour>"; else grep -v "<flavour>[^<]"; fi; } \\',
         '    | grep -o "https://[^\\"]*\\.zim\\.meta4" | sed "s/\\.meta4$//" | sort | tail -1)',
         '  echo "${u:-$3}"; }',
         'ok(){ echo "OK   $1" | tee -a "$LOG" "$RUNLOG"; }; fail(){ echo "FAIL $1" | tee -a "$LOG" "$RUNLOG"; }', ""]
    for v in plan:
        d = v["download"]; m = d["method"]; sub = f'$DEST/{safe(v["cat"])}/{safe(v["id"])}'; vid = q(v["id"])
        L.append(f"# --- {v['id']}  ({human(size_of(v))})  {c(v.get('name'))}")
        if v.get("notes") and (v["download"]["method"] in ("agent", "manual", "wget-mirror") or v["download"].get("todo_note")):
            L.append(f"# Megjegyzés: {c(v.get('notes'))[:600]}  (teljes rekord: plan.json → items[id={v['id']}])")
        if v.get("download", {}).get("todo_note"):
            L.append(f'[ -f "{sub}/.done" ] || echo {q("TODO " + v["id"] + " – " + c(v["download"]["todo_note"]) + " (kész után: touch " + sub + "/.done)")} | tee -a "$LOG" "$RUNLOG"')
        L.append(f'mkdir -p "{sub}"')
        if m == "kiwix":
            fl = d.get("flavour") or ""
            fl = "" if fl == "null" else fl
            L.append(f'if [ -z "${{REFRESH:-}}" ] && [ -f "{sub}/.ok" ]; then ok {vid}; else')
            L.append(f'U=$(kiwix_latest {q(d["book"])} {q(fl)} {q(d.get("url") or "")})')
            L.append(f'if have aria2c; then aria2c -c --auto-file-renaming=false --follow-metalink=mem -d "{sub}" "$U.meta4" || fetch "$U" "{sub}"; else fetch "$U" "{sub}"; fi')
            L.append(f'(cd "{sub}" && curl -fsSL "$U.sha256" | sha256c) && {{ if [ -n "${{PRUNE:-}}" ]; then find "{sub}" -maxdepth 1 -name "*.zim" ! -name "${{U##*/}}" -delete; elif ls "{sub}"/*.zim 2>/dev/null | grep -qv "${{U##*/}}"; then mkdir -p "{sub}/_old"; find "{sub}" -maxdepth 1 -name "*.zim" ! -name "${{U##*/}}" -exec mv -n {{}} "{sub}/_old/" ";"; echo "FIGYELEM: régi ZIM → {sub}/_old ($(du -sh "{sub}/_old" | cut -f1)); jóváhagyás után PRUNE=1 törli" | tee -a "$LOG" "$RUNLOG"; fi; touch "{sub}/.ok"; ok {vid}; }} || fail {vid}')
            L.append('fi')
        elif m == "http":
            us = [u for u in (d.get("urls") or [d.get("url")]) if u]
            share = 10 if d.get("todo_note") else 2          # a tervezett méret legalább 50%-a (todo_note-os készletnél 10%-a) legyen meg
            minh = max(1, int((size_of(v) or 0) / 1000 / share))
            guard = f'[ "$(du -sk "{sub}" | cut -f1)" -ge {minh} ]'
            if len(us) == 1:
                L.append(f'fetch {q(us[0])} "{sub}" && {guard} && ok {vid} || fail {vid}')
            elif us:      # több fájl: mind letöltődik, tételenként egy ítélet (részleges hiba = FAIL)
                L.append(f'_r=0; for _u in {" ".join(q(u) for u in us)}; do fetch "$_u" "{sub}" || _r=1; done; [ $_r = 0 ] && {guard} && ok {vid} || fail {vid}')
        elif m == "jigdo":    # Debian BD/DVD-képek .jigdo leírókból (jigdo-file csomag), nem interaktívan
            base = d["url"].rstrip("/") + "/"
            L.append(f'if have jigdo-lite; then _r=0; _n=0; for _j in $(curl -fsSL {q(base)} | grep -o \'href="{d.get("match") or "debian-[0-9]"}[^"]*\\.jigdo"\' | sed \'s/^href="//;s/"$//\' | sort -u); do '
                     f'_n=$((_n+1)); (cd "{sub}" && jigdo-lite --noask {q(base)}"$_j") || _r=1; done; [ $_r = 0 ] && [ $_n -gt 0 ] && ok {vid} || fail {vid}; '
                     f'else echo {q("TODO " + v["id"] + " – jigdo-lite kell (apt install jigdo-file)")} | tee -a "$LOG" "$RUNLOG"; fi')
        elif m == "wget-mirror":
            mink = max(1, int((size_of(v) or 0) / 1000 / 20))   # legalább a tervezett méret ~5%-a jöjjön le, különben részleges tükör
            L.append(f'(cd "{sub}" && wget -m -np -k -K -E -e robots=off --wait=1 --random-wait -U "Mozilla/5.0 (X11; Linux x86_64; rv:140.0) Gecko/20100101 Firefox/140.0" {d.get("wget_args","")} {q(d["url"])}); '
                     f'_k=$(du -sk "{sub}" | cut -f1); if [ "$_k" -ge {mink * 10} ]; then ok {vid}; elif [ "$_k" -ge {mink} ]; then echo "TODO {v["id"]} – részleges tükör (${{_k}} KB, a terv 5–50%-a): pótold célzottan" | tee -a "$LOG" "$RUNLOG"; else fail {vid}; fi')
        elif m == "rsync":
            L.append(f'rsync -avP --partial {d.get("rsync_args","")} {q(d["url"])} "{sub}/" && ok {vid} || fail {vid}')
        elif m == "git":
            calls = []
            for k_, u in enumerate([u for u in (d.get("repos") or [d.get("url")]) if u]):
                n = u.rstrip("/").split("/")[-1]
                n = safe(n[:-4] if n.endswith(".git") else n)
                g, tag = f'"{sub}/{n}.git"', (d.get("tag") or v.get("latest_version") or "") if k_ == 0 else ""
                tag = tag if re.fullmatch(r"[\w.+-]{1,60}", tag or "") else ""
                calls.append(f'git_mirror {q(u)} {g} {q(tag)}')
            if len(calls) == 1:
                L.append(f'{calls[0]} && ok {vid} || fail {vid}')
            elif calls:   # több repó: tételenként egy ítélet
                L.append("_r=0; " + "; ".join(f"{c_} || _r=1" for c_ in calls) + f"; [ $_r = 0 ] && ok {vid} || fail {vid}")
            if d.get("release_url"):
                gh = re.match(r"https://github\.com/([\w.-]+/[\w.-]+?)(?:\.git)?/?$", (d.get("repos") or [""])[0] or "")
                rtag = d.get("tag") or v.get("latest_version") or ""
                rtag = rtag if re.fullmatch(r"[\w.+-]{1,60}", rtag) else ""
                cap_mb = max(50, int(((v.get("bytes") or v.get("bytes_est") or 0) * 1.2) / 1e6))   # a tétel tervbe számolt méretén belül
                todo_txt = ("TODO " + v["id"] + " – telepítők: " + c(d["release_url"]) + " (keret ≈" + str(cap_mb) + " MB; platformok: GH_PLATFORMS szerint, alap linux-x64, win-x64, apk; kész után: touch "
                            + sub + "/release/.ok)")
                todo = f'{{ [ -f "{sub}/release/.ok" ] || echo {q(todo_txt)} | tee -a "$LOG" "$RUNLOG"; }}'
                bi = v.get("binaries_item")
                if bi and bi in plan_ids:
                    L.append(f'# telepítők: a(z) {c(bi)} tétel már letölti – itt nem ismételjük')
                elif gh:    # GitHub: a kiadás telepítői automatikusan (GH_ASSET_RE / GH_ASSET_MAX_MB állítható); ha nem sikerül: AI-feladat
                    L.append(f'gh_release {q(gh.group(1))} {q(rtag)} "{sub}/release" {cap_mb} || {todo}')
                else:
                    L.append(f'# Telepítők/binárisok (AI-feladat): a {c(d["release_url"])} oldalról a célplatformokhoz illő kiadások ide: "{sub}/release/"')
                    L.append(todo)
        elif m == "hf":
            rt = " --repo-type dataset" if d.get("repo_type") == "dataset" else ""
            # hf/huggingface-cli < 1.0: ismételt --include esetén csak az utolsó minta marad → mintánként külön hívás
            calls = [f'hfdl {q(d["repo"])}{rt}' + (f" --include {q(p)}" if p else "") + f' --local-dir "{sub}"' for p in (d.get("include") or [None])]
            hfmin = max(1, int((size_of(v) or 0) / 1000 / 2))   # legalább a tervezett méret fele legyen a mappában (üres minta → nem hamis OK)
            L.append("{ " + " && ".join(calls) + f'; }} && [ "$(du -sk "{sub}" | cut -f1)" -ge {hfmin} ] && ok {vid} || fail {vid}')
        elif m == "ollama":
            tag = d["tag"].split(" / ")[0].split()[0]
            L.append(f'ollama_pull {q(tag)} "{sub}" && ok {vid} || fail {vid}   # ideiglenes ollama-szerver, a modell a $DEST alá kerül')
        elif m == "archive.org":
            glob = f' --glob={q(d["glob"])}' if d.get("glob") else ""
            ids = [x for x in (d.get("ids") or [d.get("id")]) if x]
            if len(ids) == 1:
                L.append(f'ia download {q(ids[0])}{glob} --checksum --destdir "{sub}" && ok {vid} || fail {vid}')
            elif ids:
                L.append("_r=0; " + "; ".join(f'ia download {q(x)}{glob} --checksum --destdir "{sub}" || _r=1' for x in ids) + f"; [ $_r = 0 ] && ok {vid} || fail {vid}")
        elif m == "torrent":
            u = d.get("url") or d.get("magnet")
            if u:
                L.append(f'have aria2c && aria2c -c --seed-time=0 -d "{sub}" {q(u)} && ok {vid} || fail {vid}')
        elif m == "agent":
            L.append('# AGENT-FELADAT: ezt az AI-nak kell egyedileg megoldania (lista összegyűjtése API/OAI-PMH/oldal alapján, majd fetch).')
            L.append(f'# Leírás: {c(d.get("note"))}')
            for u in d.get("seed_urls") or []:
                L.append(f'#   kiinduló URL: {c(u)}')
            L.append(f'[ -f "{sub}/.done" ] || echo "TODO {v["id"]} (kész után: touch {sub}/.done)" | tee -a "$LOG" "$RUNLOG"')
        else:   # s3, jigdo, …: nincs megbízható automatikus parancs
            L.append(f'# KÉZI ({m}): {c(d.get("note"))} {c(d.get("url"))}')
            L.append(f'echo "TODO {v["id"]} ({m})" | tee -a "$LOG" "$RUNLOG"')
        L.append("")
    L.append('echo "Kész. Napló: $RUNLOG"; echo "FAIL ebben a futásban: $(grep -c "^FAIL" "$RUNLOG") | kézi/AI-teendő (TODO): $(grep -c "^TODO" "$RUNLOG")"')
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")


if __name__ == "__main__":
    run_cli(main)
