#!/usr/bin/env python3
"""ALGOTRADING-archívum build: research/*.jsonl → ALGOTRADING.md, -kompakt.md, -chat.md, katalogus.jsonl, letolto.sh, FEJLESZTOI-SPEC.md.
Független az ARCHIVUM (blackout) kiadástól. Futtatás: python3 -I build.py"""
import json, os, re, sys, glob, hashlib
from collections import defaultdict, Counter

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
RES = os.path.join(HERE, "research")
DATE = os.environ.get("BUILD_DATE", "2026-11-15")

ACCESS = {"free": "ingyenes", "registration": "regisztrációs", "freemium": "freemium", "paid": "fizetős", "institutional": "intézményi"}
SCORE_KEYS = "REQCLFZ"
SCORE_HU = {"R": "relevancia", "E": "edge-potenciál", "Q": "minőség", "C": "költséghatékonyság", "L": "késleltetés/frissesség",
            "F": "karbantartottság", "Z": "jogi/ÁSZF-biztonság"}
PROFILES = {   # súlyok összege 1
    "gyors_mt5":  {"E": .30, "L": .20, "R": .15, "Q": .10, "Z": .10, "C": .10, "F": .05},
    "kockazat":   {"Q": .30, "R": .25, "F": .15, "C": .10, "Z": .10, "E": .05, "L": .05},
    "kutatas":    {"R": .25, "Q": .25, "E": .20, "F": .15, "C": .10, "Z": .05, "L": .00},
    "predikcio":  {"E": .30, "Z": .20, "R": .15, "Q": .15, "L": .10, "C": .10, "F": .00},
    "kiegyensulyozott": {"R": .20, "E": .20, "Q": .20, "C": .10, "L": .10, "F": .10, "Z": .10},
}
PROFILE_HU = {"gyors_mt5": "Gyors pénz – aktív automatizált kereskedés", "kockazat": "Aladdin-szerű kockázat", "kutatas": "Kutatás",
              "predikcio": "Predikciós piacok és sport", "kiegyensulyozott": "Kiegyensúlyozott"}
# kutatási fájl → fejezet (sorrend = fejezetsorrend)
SOURCES = [
    ("a1_market_exec", "Piaci adat (FX, CFD, részvény, opció, határidős) és végrehajtás, brókerek, MetaTrader"),
    ("a2_crypto", "Kripto: tőzsdék, adatok, on-chain, DeFi"),
    ("a3_predict_sports", "Predikciós piacok és sportfogadás"),
    ("a4_macro_news_alt", "Makró, statisztika, fundamentumok, hírek, alternatív adat, magyar források"),
    ("a5_oss", "Nyílt forráskódú szoftverek: backtest, végrehajtás, adatbázis, ML, idősor-alapmodellek"),
    ("a6_ai_research", "AI-kereskedés kutatása, LLM-ágensek, súlyozás, validálás, irodalom, benchmark-platformok"),
    ("a8_infra_legal", "Infrastruktúra, szerverhelyek, hardver, költözés, adó, szabályozás"),
    ("a9_platform", "Platform-architektúra és AI-fejlesztési eszközök"),
    ("a11_platforms", "Platform- és bróker-összehasonlítás: van-e jobb, mint a jelenlegi (MT5/Vantage)"),
    ("a10_methods", "Bevált módszerek: statisztikai összefüggésekből értelem és eredmény (esettanulmányok, módszertár)"),
]


CAT_HU = {
    "broker": "Brókerek", "community": "Közösségek", "data": "Piaci adatforrások", "execution": "Végrehajtás, MetaTrader, API-k",
    "execution-quality": "Végrehajtási minőség mérése", "infra": "Infrastruktúra", "reference": "Referenciaadat", "research": "Kutatási források",
    "kripto-cex-api": "Központosított tőzsdék API-i", "kripto-derivativ-adat": "Derivatív adat (funding, OI, likvidáció)", "kripto-dex-adat": "DEX-adat",
    "kripto-infrastruktura": "Infrastruktúra, node, colocation", "kripto-irodalom": "Kutatás és irodalom", "kripto-jog-ado": "Jog és adó (HU/EU)",
    "kripto-mev-mempool": "MEV és mempool", "kripto-onchain-adat": "On-chain adat", "kripto-oss-eszkoz": "Nyílt forráskódú eszközök",
    "kripto-piaci-adat": "Piaci adat (tick, L2)", "kripto-strategia": "Stratégiák",
    "M1-adateszkoz": "Adateszközök", "M13-meta-index": "Gyűjtőlisták, meta-indexek", "M14-fejlesztes-biztonsag": "Fejlesztés és biztonság",
    "M14-infra": "Infrastruktúra-szoftver", "M14-mlops": "MLOps", "M14-vizualizacio": "Vizualizáció, terminál", "M6-mt5-hid": "MetaTrader-hidak",
    "M6-vegrehajtas": "Végrehajtás", "M7-adattarolo": "Adattárolók (tick, idősor)", "M7-backtest": "Backtest- és élő motorok", "M7-validalas": "Validálás",
    "M8-idosor": "Idősor-elemzés", "M8-kvant-konyvtar": "Kvant-könyvtárak", "M8-ts-alapmodell": "Idősor-alapmodellek", "M9-penzugyi-llm": "Pénzügyi LLM-ek",
    "broker-regulation": "Bróker-szabályozás", "infra-hardware": "Hardver", "infra-latency": "Késleltetés", "infra-server-location": "Szerverhelyek",
    "infra-vps-colo": "VPS és colocation", "legal-tax-hu": "Magyar adó és jog", "regulation": "Szabályozás", "relocation": "Költözés, adórezidencia",
    "case_study": "Esettanulmányok", "method": "Módszertár",
}


def cat_label(o, big):
    c = o.get("cat") or "egyéb"
    lab = CAT_HU.get(c, re.sub(r"^M\d+[ -]", "", c))
    if c in big and o.get("sub"):
        part = re.split(r" / | – |: ", str(o["sub"]))[0].strip()
        return f"{lab} – {part[:1].upper() + part[1:]}"
    return lab


def slug(s):
    s = s.lower()
    for a, b in zip("áéíóöőúüű", "aeiooouuu"):
        s = s.replace(a, b)
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")


def hunum(x, d=1):
    if x is None:
        return "?"
    if isinstance(x, (int,)) or float(x).is_integer():
        return f"{int(x):,}".replace(",", " ")
    return f"{x:,.{d}f}".replace(",", " ").replace(".", ",")


def load(name):
    p = os.path.join(RES, name + ".jsonl")
    out, bad = [], 0
    if not os.path.exists(p):
        return out, 0
    for ln, line in enumerate(open(p, encoding="utf-8"), 1):
        line = line.strip()
        if not line:
            continue
        try:
            o = json.loads(line)
        except ValueError:
            bad += 1
            continue
        if isinstance(o, dict):
            o["_src"] = name
            out.append(o)
    return out, bad


def norm_url(u):
    u = (u or "").strip().lower()
    u = re.sub(r"^https?://(www\.)?", "", u).rstrip("/")
    return u


def clean_scores(o):
    sc = o.get("scores") or {}
    out = {}
    for k in SCORE_KEYS:
        v = sc.get(k)
        try:
            v = float(v)
        except (TypeError, ValueError):
            v = None
        out[k] = None if v is None else max(0.0, min(10.0, v))
    return out


def prof_score(sc, w):
    num = sum(w[k] * sc[k] for k in w if sc.get(k) is not None)
    den = sum(w[k] for k in w if sc.get(k) is not None)
    return round(num / den * 10, 1) if den else 0.0     # 0–100


def collect():
    items, stats, seen_id, seen_url = [], {}, {}, {}
    for name, _ in SOURCES:
        L, bad = load(name)
        stats[name] = {"raw": len(L), "bad_json": bad, "dup": 0, "no_url": 0}
        for o in L:
            iid = slug(str(o.get("id") or o.get("name") or ""))
            if not iid or not o.get("name"):
                continue
            url = o.get("url") or o.get("docs_url") or o.get("info_url")
            if not url:
                stats[name]["no_url"] += 1
            nu = norm_url(url)
            if iid in seen_id or (nu and nu in seen_url and len(nu) > 12):
                stats[name]["dup"] += 1
                prev = seen_id.get(iid) or seen_url.get(nu)
                for k in ("notes_hu", "pitfalls_hu"):   # összefésülés: a hosszabb leírás marad
                    if len(str(o.get(k) or "")) > len(str(prev.get(k) or "")):
                        prev[k] = o.get(k)
                continue
            o["id"] = iid
            o["url"] = url
            o["access"] = o.get("access") if o.get("access") in ACCESS else "paid" if o.get("price") else "free"
            o["scores"] = clean_scores(o)
            o["prof"] = {p: prof_score(o["scores"], w) for p, w in PROFILES.items()}
            try:
                o["tier"] = int(o.get("tier"))
            except (TypeError, ValueError):
                o["tier"] = 2
            o["tier"] = max(0, min(3, o["tier"]))
            if o.get("verified") not in ("mért", "becsült", "nem ellenőrzött"):
                o["verified"] = "nem ellenőrzött"
            seen_id[iid] = o
            if nu:
                seen_url[nu] = o
            items.append(o)
    return items, stats


def load_plain(name):
    L, _ = load(name)
    return L


def read(name):
    p = os.path.join(RES, name)
    return open(p, encoding="utf-8").read().strip() if os.path.exists(p) else ""


def esc(s):
    return str(s or "").replace("|", "\\|").replace("\n", " ").strip()


def link(o):
    u = o.get("url") or ""
    return f"[{esc(o['name'])}]({u})" if u.startswith("http") else esc(o["name"])


def price(o):
    e = o.get("price_eur_month")
    p = esc(o.get("price"))
    if isinstance(e, (int, float)) and e > 0:
        return f"{p} (~{hunum(e, 0)} €/hó)" if p else f"~{hunum(e, 0)} €/hó"
    return p or ("0" if o["access"] in ("free",) else "?")


def table(rows, prof="kiegyensulyozott"):
    md = ["| Szint | Név | Hozzáférés | Ár | Pont | Mire jó | Buktató | Ellenőrzés |", "|---|---|---|---|---|---|---|---|"]
    for o in rows:
        md.append(f"| {o['tier']} | {link(o)} | {ACCESS[o['access']]} | {price(o)} | {o['prof'][prof]:.0f} | "
                  f"{esc(o.get('notes_hu'))[:400]} | {esc(o.get('pitfalls_hu'))[:250]} | {o['verified']} |")
    return md


def m16_table(rows):
    """M16: esettanulmány / módszer – saját mezőkkel (ki, adat, módszer, eredmény + ellenőrzés, miért működött, mikor halt meg, jobb változat, platform)"""
    if rows and rows[0].get("cat") == "method":
        md = ["| Módszer | Mikor jó / mire | Mikor csal (buktató) | Könyvtár, cikk | Platform-felhasználás |", "|---|---|---|---|---|"]
        for o in rows:
            cu = o.get("code_urls") or []
            cu = cu if isinstance(cu, list) else [cu]
            refs = " · ".join(f"[{k + 1}]({u})" for k, u in enumerate(cu[:4]) if isinstance(u, str) and u.startswith("http"))
            md.append(f"| {link(o)} | {esc(o.get('method_hu') or o.get('notes_hu'))[:350]} | {esc(o.get('pitfalls_hu'))[:250]} | {refs} | {esc(o.get('platform_use_hu'))[:250]} |")
        return md
    md = ["| Eset | Ki, adat | Módszer | Eredmény (ellenőrzés) | Miért működött / mikor halt meg | Hogyan jobban | Platform | Kód, cikk |", "|---|---|---|---|---|---|---|---|"]
    for o in rows:
        cu = o.get("code_urls") or []
        cu = cu if isinstance(cu, list) else [cu]
        refs = " · ".join(f"[{k + 1}]({u})" for k, u in enumerate(cu[:4]) if isinstance(u, str) and u.startswith("http"))
        md.append(f"| {link(o)} | {esc(o.get('who'))[:80]}; {esc(o.get('data_hu'))[:160]} | {esc(o.get('method_hu'))[:260]} | "
                  f"{esc(o.get('result_hu'))[:220]} ({esc(o.get('result_verified') or o['verified'])}) | {esc(o.get('why_worked_hu'))[:180]} / {esc(o.get('died_hu'))[:160]} | "
                  f"{esc(o.get('improve_hu'))[:220]} | {esc(o.get('platform_use_hu'))[:200]} | {refs} |")
    return md


def budget_section(items):
    tiers = [("Ingyenes indulócsomag (0 €/hó)", lambda o: o["access"] in ("free", "registration")),
             ("Kis költségvetés (≤ 100 €/hó tételenként)", lambda o: isinstance(o.get("price_eur_month"), (int, float)) and 0 < o["price_eur_month"] <= 100),
             ("Profi (100–1000 €/hó tételenként)", lambda o: isinstance(o.get("price_eur_month"), (int, float)) and 100 < o["price_eur_month"] <= 1000),
             ("Intézményi (> 1000 €/hó vagy egyedi ár)", lambda o: o["access"] == "institutional" or (isinstance(o.get("price_eur_month"), (int, float)) and o["price_eur_month"] > 1000))]
    md = ["## 3. Költségvetés szerinti válogatás – a „gyors pénz – aktív automatizált kereskedés” profil sorrendjében", "",
          "Tételenkénti ár; a csomag ára a kiválasztott tételek összege. Az árak a kutatás napján érvényesek (mért = az oldalon látott, becsült = számított vagy közvetett).", ""]
    for title, f in tiers:
        sel = sorted([o for o in items if f(o)], key=lambda o: -o["prof"]["gyors_mt5"])[:40]
        tot = sum(o.get("price_eur_month") or 0 for o in sel if isinstance(o.get("price_eur_month"), (int, float)))
        md += [f"### {title} – {len(sel)} tétel" + (f", összesen ~{hunum(tot, 0)} €/hó" if tot else ""), ""] + table(sel, "gyors_mt5") + [""]
    return md


def main():
    items, stats = collect()
    strategies = load_plain("a7_strategies")
    ideas = load_plain("a7_ideas")
    by_src = defaultdict(list)
    for o in items:
        by_src[o["_src"]].append(o)
    cnt_access = Counter(o["access"] for o in items)
    toc, body = [], []
    n = 4
    for name, title in SOURCES:
        L = by_src.get(name) or []
        if not L:
            continue
        a = f"{n}-{slug(title)}"
        toc.append(f"- [{n}. {title}](#{a}) – {len(L)} tétel")
        body += ["", "---", "", f"## {n}. {title}", ""]
        summ = read(name.split("_")[0] + "_summary.md")
        if summ:
            body += [f"### {n}.0. Összefoglaló – {title.split(':')[0].split(',')[0]}", "", re.sub(r"(?m)^#{1,3} (.*)$", lambda m: f"#### {m.group(1)} ({name.split('_')[0].upper()})", summ), ""]
        cc = Counter(o.get("cat") for o in L)
        big = {c for c, k in cc.items() if k > 40}
        cats = defaultdict(list)
        for o in L:
            cats[cat_label(o, big)].append(o)
        small = [k for k, v in cats.items() if len(v) < 3 and " – " in k]
        for k in small:      # 3 tételnél kisebb alcsoport → a fő kategória „egyéb” csoportja
            cats[k.split(" – ")[0] + " – egyéb"] += cats.pop(k)
        for j, (c, CL) in enumerate(sorted(cats.items(), key=lambda kv: (-len(kv[1]), kv[0])), 1):
            CL.sort(key=lambda o: (o["tier"], -o["prof"]["kiegyensulyozott"]))
            body += [f"### {n}.{j}. {c} ({len(CL)})", ""] + (m16_table(CL) if name == "a10_methods" else table(CL)) + [""]
        n += 1
    # stratégiák
    if strategies:
        toc.append(f"- [{n}. Stratégia-könyvtár](#{n}-strategia-konyvtar) – {len(strategies)} stratégia")
        body += ["", "---", "", f"## {n}. Stratégia-könyvtár", "",
                 "| Név | Képlet / lényeg | Mikor működik | Mikor hal meg | Lecsengés | MT5-alkalmasság | Bizonyíték |", "|---|---|---|---|---|---|---|"]
        for s in sorted(strategies, key=lambda s: -(s.get("mt5_fit") or 0)):
            ev = s.get("evidence")
            ev = ev if isinstance(ev, list) else [ev] if ev else []
            evs = " · ".join(f"[forrás]({e})" if isinstance(e, str) and e.startswith("http") else esc(e if isinstance(e, str) else json.dumps(e, ensure_ascii=False))[:120] for e in ev[:4])
            body.append(f"| {link(s) if s.get('url') else esc(s.get('name'))} | {esc(s.get('formula_hu'))[:300]} | {esc(s.get('works_when_hu'))[:200]} | "
                        f"{esc(s.get('dies_when_hu'))[:200]} | {esc(s.get('decay_hu'))[:150]} | {s.get('mt5_fit', '?')}/10 | {evs} |")
        n += 1
    risk = read("a7_risk.md")
    if risk:
        toc.append(f"- [{n}. Kockázati matematika (1:500, grid, martingale, Kelly)](#{n}-kockazati-matematika)")
        body += ["", "---", "", f"## {n}. Kockázati matematika", "", re.sub(r"(?m)^# ", "### ", re.sub(r"(?m)^## ", "### ", risk)), ""]
        n += 1
    if ideas:
        toc.append(f"- [{n}. Hipotézisgyár – új ötletek](#{n}-hipotezisgyar) – {len(ideas)} ötlet")
        body += ["", "---", "", f"## {n}. Hipotézisgyár", "",
                 "Az újszerűség becsült (0–10); a publikált ötletnél forrás és alacsonyabb pont. Minden ötlet cáfolható teszttel.", "",
                 "| # | Ötlet | Mechanizmus | Adat | Cáfoló teszt | Újszerűség | MT5 | Kockázat |", "|---|---|---|---|---|---|---|---|"]
        for k, s in enumerate(sorted(ideas, key=lambda s: -((s.get("novelty") or 0) + (s.get("mt5_fit") or 0))), 1):
            ds = s.get("data_sources")
            ds = ", ".join(map(str, ds[:5])) if isinstance(ds, list) else esc(ds)
            body.append(f"| {k} | **{esc(s.get('title_hu'))}** | {esc(s.get('mechanism_hu'))[:300]} | {esc(ds)[:200]} | {esc(s.get('test_hu'))[:250]} | "
                        f"{s.get('novelty', '?')}/10 | {s.get('mt5_fit', '?')}/10 | {esc(s.get('risk_hu'))[:150]} |")
        n += 1
    tab = read("a8_tables.md")
    if tab:
        toc.append(f"- [{n}. Szerverhelyek, VPS, hardver, költözési mátrix, magyar adó](#{n}-szerverhelyek-vps-hardver-koltozes-ado)")
        body += ["", "---", "", f"## {n}. Szerverhelyek, VPS, hardver, költözés, adó", "", re.sub(r"(?m)^# ", "### ", re.sub(r"(?m)^## ", "### ", tab)), ""]
        n += 1
    spec = read("a9_spec.md")
    pf = os.path.join(HERE, "sections", "platformfuggetlenseg.md")
    if spec and os.path.exists(pf):     # kötelező tervezési elv: a specifikáció végére, minden mást felülír
        spec += "\n\n" + open(pf, encoding="utf-8").read().strip()
    if spec:
        toc.append(f"- [{n}. Fejlesztői specifikáció (összefoglaló; teljes: FEJLESZTOI-SPEC.md)](#{n}-fejlesztoi-specifikacio)")
        body += ["", "---", "", f"## {n}. Fejlesztői specifikáció", "", "A teljes szöveg külön fájlban: `FEJLESZTOI-SPEC.md`.", "",
                 re.sub(r"(?m)^# ", "### ", re.sub(r"(?m)^## ", "### ", spec)), ""]
        n += 1

    pp = [os.path.join(ROOT, ".allapot", "MESTERPROMPT.md"), os.path.join(HERE, "allapot", "MESTERPROMPT.md")]   # repó / kicsomagolt ZIP
    prompt = open(next((x for x in pp if os.path.exists(x)), pp[0]), encoding="utf-8").read()
    head = [f"# ALGOTRADING – kvant-, algo- és AI-kereskedési archívum (kutatás: {DATE})", "",
            f"**{len(items)} katalógustétel**, {len(strategies)} stratégia, {len(ideas)} új ötlet. Hozzáférés: "
            + ", ".join(f"{ACCESS[k]} {v}" for k, v in cnt_access.most_common()) + ".", "",
            "> Egy fejlesztőcsapatnak szóló alapanyag egy pénzügyi meta-platformhoz (MetaTrader-alapú végrehajtás, többmodelles súlyozott AI-döntés ördögügyvéddel, "
            "predikciós piacok, kripto, makró, hírek, kockázati motor). Minden link a kutatás napján ellenőrzött, kivéve a „nem ellenőrzött” jelölésűeket. "
            "Nem befektetési tanácsadás.", "",
            "## Tartalom", "", "- [1. Mesterprompt (a kutatás és az építés specifikációja)](#1-mesterprompt)",
            "- [2. Pontozás és profilok](#2-pontozas-es-profilok)", "- [3. Költségvetés szerinti válogatás](#3-koltsegvetes-szerinti-valogatas--a-gyors-penz-mt5-on-profil-sorrendjeben)"] + toc
    scoring = ["## 2. Pontozás és profilok", "",
               "Tételpontok 0–10 skálán: " + ", ".join(f"**{k}** = {v}" for k, v in SCORE_HU.items()) + ". A profilpont 0–100 (súlyozott átlag × 10).", "",
               "| Profil | " + " | ".join(SCORE_KEYS) + " |", "|---|" + "---|" * len(SCORE_KEYS)]
    for p, w in PROFILES.items():
        scoring.append(f"| {PROFILE_HU[p]} | " + " | ".join(f"{w.get(k, 0):.2f}".replace(".", ",") for k in SCORE_KEYS) + " |")
    scoring += ["", "**Szint:** 0 = nélkülözhetetlen mag · 1 = erősen ajánlott · 2 = bővítés · 3 = luxus vagy intézményi.", ""]
    md = head + ["", "---", "", "## 1. Mesterprompt", "", re.sub(r"(?m)^(#{1,3}) ", lambda m: "#" * (len(m.group(1)) + 2) + " ", prompt), "", "---", ""] \
        + scoring + budget_section(items) + body
    # tartalomjegyzék-horgonyok a tényleges ## címsorokból, GitHub-szabály szerint (ékezet marad, írásjel törlődik, szóköz → kötőjel)
    gh = lambda h: re.sub(r"\s", "-", re.sub(r"[^\w\- ]", "", re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", h).strip().lower()))
    heads = {}
    for line in md:
        m = re.match(r"^## (\d+)\. (.*)$", line)
        if m and m.group(1) not in heads:
            heads[m.group(1)] = gh(f"{m.group(1)}. {m.group(2)}")
    md = [re.sub(r"\]\(#(\d+)-[^)]*\)", lambda m: f"](#{heads.get(m.group(1), m.group(0))})", l) if l.startswith("- [") else l for l in md]
    out = os.path.join(ROOT, "ALGOTRADING.md")
    open(out, "w", encoding="utf-8").write("\n".join(md) + "\n")

    # kompakt: szintenként a legjobb tételek, rövid sorokkal
    km = [f"# ALGOTRADING – kompakt ({len(items)} tételből a 0–1. szint)", ""]
    for name, title in SOURCES:
        L = sorted([o for o in by_src.get(name, []) if o["tier"] <= 1], key=lambda o: -o["prof"]["kiegyensulyozott"])
        if L:
            km += [f"## {title}", ""] + [f"- {link(o)} – {ACCESS[o['access']]}, {price(o)}; {esc(o.get('notes_hu'))[:180]}" for o in L] + [""]
    open(os.path.join(ROOT, "ALGOTRADING-kompakt.md"), "w", encoding="utf-8").write("\n".join(km) + "\n")
    # chat: LLM-be tölthető tömör változat
    ch = [f"# ALGOTRADING – chat-változat (LLM-kontextusba). Kutatás: {DATE}", "", "Formátum: id | név | hozzáférés | ár | profilpontok gyors/kockázat/kutatás/predikció | url", ""]
    for name, title in SOURCES:
        L = sorted(by_src.get(name, []), key=lambda o: (o["tier"], -o["prof"]["kiegyensulyozott"]))
        if L:
            ch += [f"## {title}"] + [f"{o['id']} | {esc(o['name'])[:70]} | {o['access']} | {price(o)[:40]} | "
                                      f"{o['prof']['gyors_mt5']:.0f}/{o['prof']['kockazat']:.0f}/{o['prof']['kutatas']:.0f}/{o['prof']['predikcio']:.0f} | {o.get('url')}" for o in L] + [""]
    if strategies:
        ch += ["## Stratégiák"] + [f"{esc(s.get('name'))} | MT5 {s.get('mt5_fit', '?')}/10 | {esc(s.get('formula_hu'))[:160]}" for s in strategies] + [""]
    if ideas:
        ch += ["## Ötletek"] + [f"{esc(s.get('title_hu'))} | új {s.get('novelty', '?')}/10 | {esc(s.get('test_hu'))[:160]}" for s in ideas] + [""]
    open(os.path.join(ROOT, "ALGOTRADING-chat.md"), "w", encoding="utf-8").write("\n".join(ch) + "\n")
    # gépi katalógus
    with open(os.path.join(ROOT, "katalogus.jsonl"), "w", encoding="utf-8") as f:
        for o in items:
            f.write(json.dumps({k: v for k, v in o.items() if not k.startswith("_")} | {"src": o["_src"]}, ensure_ascii=False) + "\n")
    if spec:
        open(os.path.join(ROOT, "FEJLESZTOI-SPEC.md"), "w", encoding="utf-8").write(spec + "\n")
    write_dl(items)
    json.dump({"items": len(items), "strategies": len(strategies), "ideas": len(ideas), "stats": stats},
              open(os.path.join(HERE, "build_stats.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"OK: {len(items)} tétel, {len(strategies)} stratégia, {len(ideas)} ötlet; " +
          "; ".join(f"{k}: {v['raw']} nyers, {v['dup']} dup, {v['bad_json']} hibás JSON" for k, v in stats.items() if v["raw"]))


def write_dl(items):
    """Letöltő szkript: csak ingyenes/regisztráció nélküli, automatikusan letölthető tételek (git klón, http fájl, HF)."""
    L = ["#!/usr/bin/env bash", "# ALGOTRADING – ingyenes források letöltése. Használat: DEST=/abszolut/ut bash letolto.sh",
         "set -u", 'DEST=${DEST:-}', 'case "$DEST" in /*) ;; *) echo "DEST abszolút út kell (pl. DEST=/mnt/algo)" >&2; exit 2;; esac',
         'DEST=$(realpath -m -- "$DEST")', 'case "$DEST" in /|/bin|/boot|/dev|/etc|/home|/lib*|/proc|/root|/run|/sbin|/sys|/usr|/var|/private|/System) echo "Tiltott DEST: $DEST" >&2; exit 2;; esac',
         'mkdir -p "$DEST" && LOG="$DEST/_letoltes.log"', 'ok(){ echo "OK   $1" | tee -a "$LOG"; }; fail(){ echo "FAIL $1" | tee -a "$LOG"; }', ""]
    n = 0
    for o in sorted(items, key=lambda o: (o["tier"], o["id"])):
        if o["access"] != "free":
            continue
        d = o.get("download") or {}
        gh = (o.get("github") or {}).get("repo")
        sub = f'"$DEST/{o["_src"]}/{o["id"]}"'
        q = lambda s: "'" + str(s).replace("'", "'\\''") + "'"
        if d.get("method") == "git" or (gh and re.match(r"^[\w.-]+/[\w.-]+$", gh)):
            url = d.get("url") if d.get("method") == "git" and d.get("url") else f"https://github.com/{gh}.git"
            L.append(f'[ -d {sub}/.git ] && git -C {sub} pull -q --ff-only || git clone -q --depth 1 {q(url)} {sub} && ok {o["id"]} || fail {o["id"]}')
            n += 1
        elif d.get("method") == "http" and str(d.get("url", "")).startswith("http"):
            L.append(f'mkdir -p {sub} && curl -fsSL --retry 3 -C - -o {sub}/{q(os.path.basename(d["url"].split("?")[0]) or "file")} {q(d["url"])} && ok {o["id"]} || fail {o["id"]}')
            n += 1
        elif d.get("method") == "hf" and d.get("url"):
            L.append(f'if command -v hf >/dev/null; then hf download {q(d["url"])} --local-dir {sub} && ok {o["id"]} || fail {o["id"]}; else echo "TODO hf: {o["id"]}"; fi')
            n += 1
    L += ["", 'echo "Kész. Napló: $LOG"']
    p = os.path.join(ROOT, "letolto.sh")
    open(p, "w", encoding="utf-8").write("\n".join(L) + "\n")
    os.chmod(p, 0o755)
    return n


if __name__ == "__main__":
    main()
