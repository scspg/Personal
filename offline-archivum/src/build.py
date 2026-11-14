#!/usr/bin/env python3
"""ARCHIVUM.md összeállítása: sections/*.md + items_*.jsonl + select_items.py -> ../ARCHIVUM.md"""
import json, glob, os, subprocess, sys, tempfile, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "ARCHIVUM.md")
W = {"S": .30, "R": .25, "A": .15, "U": .15, "Q": .10, "O": .05}
CAT_HU = {
 "medicine": "Orvoslás", "water_sanitation": "Víz és higiénia", "food": "Élelmiszer, tartósítás", "agriculture": "Mezőgazdaság",
 "veterinary": "Állatorvoslás", "survival": "Túlélés, katasztrófa", "appropriate_tech": "Megfelelő technológia",
 "repair": "Javítás", "construction": "Építés", "energy": "Energia", "engineering": "Mérnöki tudás",
 "manufacturing": "Gyártás, megmunkálás", "chemistry": "Kémia", "electronics": "Elektronika",
 "communications": "Kommunikáció, rádió", "navigation": "Navigáció", "open_hardware": "Nyílt hardver",
 "science": "Tudomány", "reference": "Lexikonok, szótárak", "education": "Oktatás", "library": "Könyvtárak",
 "hungarian": "Magyar források", "humanities": "Bölcsészet", "computing": "Számítástechnika",
 "os_mirror": "Operációs rendszerek, csomagtükrök", "source_code": "Forráskód", "ai_models": "LLM / AI modellek",
 "ai_tools": "AI futtatók és eszközök", "maps_geo": "Térképek, geoadatok", "knowledge_dump": "Nagy adathalmazok",
 "server_bundle": "Offline szerver-csomagok", "gpu_unlock": "GPU-feloldás és -hangolás (GeForce)", "tools": "Olvasók, futtatók (kötelező)", "bundle": "Kész csomagok (kereskedelmi)",
 "reference_book": "Kézikönyvek (könyv)", "gray_library": "Szürke zónás könyvtárak",
}
PRESETS = [("32GB", None, "pendrive / telefon"), ("128GB", "T5", "telefon + kis SSD"), ("512GB", "T4", "laptop SSD"),
           ("1TB", "T3", "gamer PC"), ("2TB", "T3", "gamer PC + nagy SSD"), ("4TB", "T2", "AI workstation"),
           ("8TB", "T2", "workstation + HDD"), ("20TB", "T1", "szerver / NAS")]


def human(b):
    if not b:
        return "?"
    for u, f in (("TB", 1e12), ("GB", 1e9), ("MB", 1e6), ("KB", 1e3)):
        if b >= f:
            return f"{b / f:.2f} {u}".replace(".00 ", " ")
    return f"{b} B"


def score(it):
    s = it.get("scores") or {}
    return round(sum(W[k] * s.get(k, 0) for k in W), 2)


def link(it):
    u = it.get("info_url")
    d = it.get("download") or {}
    if not u and d.get("method") == "kiwix":
        u = d.get("url")
    u = u or d.get("url") or (d.get("urls") or [None])[0] or (f"https://huggingface.co/{d['repo']}" if d.get("repo") else None)
    return f"[link]({u})" if u else "—"


def esc(s):
    return (s or "").replace("|", "\\|").replace("\n", " ")


SSD_SIZES = ["1TB", "2TB", "4TB", "8TB", "16TB", "32TB"]
CAT_GROUP = {  # kategória → összevont csoport az SSD-bontáshoz
 "medicine": "Életmentő: orvoslás, víz, élelem, túlélés", "water_sanitation": "Életmentő: orvoslás, víz, élelem, túlélés",
 "food": "Életmentő: orvoslás, víz, élelem, túlélés", "survival": "Életmentő: orvoslás, víz, élelem, túlélés", "veterinary": "Életmentő: orvoslás, víz, élelem, túlélés",
 "civil_defense": "Életmentő: orvoslás, víz, élelem, túlélés",
 "agriculture": "Mezőgazdaság, megfelelő technológia, energia", "appropriate_tech": "Mezőgazdaság, megfelelő technológia, energia", "energy": "Mezőgazdaság, megfelelő technológia, energia",
 "reference": "Lexikonok, szótárak", "hungarian": "Magyar források",
 "engineering": "Mérnöki tudás, gyártás, kémia, elektronika", "manufacturing": "Mérnöki tudás, gyártás, kémia, elektronika", "chemistry": "Mérnöki tudás, gyártás, kémia, elektronika",
 "electronics": "Mérnöki tudás, gyártás, kémia, elektronika", "construction": "Mérnöki tudás, gyártás, kémia, elektronika", "repair": "Mérnöki tudás, gyártás, kémia, elektronika",
 "open_hardware": "Mérnöki tudás, gyártás, kémia, elektronika", "communications": "Mérnöki tudás, gyártás, kémia, elektronika", "navigation": "Mérnöki tudás, gyártás, kémia, elektronika",
 "science": "Tudomány, oktatás, könyvtárak", "education": "Tudomány, oktatás, könyvtárak", "library": "Tudomány, oktatás, könyvtárak", "humanities": "Tudomány, oktatás, könyvtárak",
 "maps_geo": "Térképek, geoadatok", "os_mirror": "Szoftver, OS, forráskód", "source_code": "Szoftver, OS, forráskód", "computing": "Szoftver, OS, forráskód",
 "knowledge_dump": "Szoftver, OS, forráskód", "server_bundle": "Szoftver, OS, forráskód", "tools": "Olvasók, futtatók", "ai_tools": "Olvasók, futtatók", "gpu_unlock": "Olvasók, futtatók",
 "ai_models": "LLM-ek (alap)", "ai_models_uncensored": "LLM-ek (cenzúrázatlan)",
}


def ssd_plans(cat_path, tmp):
    """SSD-méretenként: select_items terv (T2-es gép, ~300 GB LLM-memória, alap + cenzúrázatlan LLM, max 4 modell)."""
    out = []
    for b in SSD_SIZES:
        outp = os.path.join(tmp, f"ssd{b}.json")
        subprocess.run([sys.executable, "-I", os.path.join(HERE, "select_items.py"), cat_path, "--budget", b, "--hw", "T2", "--mem", "300GB",
                        "--platform", "server", "--llm-models", "4", "--out", outp], check=True, capture_output=True)
        p = json.load(open(outp, encoding="utf-8"))
        out.append((b, p))
    return out


def ssd_section(plans):
    md = ["---", "", "## 4b. Hány TB-os SSD kell? – csomagok 1, 2, 4, 8, 16 és 32 TB-ra", "",
          "A `select_items.py` az alábbi beállítással számolt minden méretre: **balanced** profil, magyar + angol + többnyelvű anyag, ingyenes és regisztrációs források. "
          "LLM-ek: **T2-es gép, ~300 GB LLM-memória** (2× MS-S1, vagy RTX 6090 + RTX Pro). Legfeljebb 4 modell kerül be, alap és cenzúrázatlan is; az LLM legfeljebb a keret 35%-át foglalhatja. "
          "A címkén szereplő TB decimális (10¹² bájt), és 8% tartalék marad a fájlrendszernek.", "",
          "### Összefoglaló", "",
          "| SSD | Felhasználva | Elemek | LLM | Életmentő | Lexikon | Mérnöki | Tudomány/oktatás | Magyar | Térkép | Szoftver/OS |",
          "|---|---|---|---|---|---|---|---|---|---|---|"]
    def grp(items):
        g = {}
        for i in items:
            k = CAT_GROUP.get(i["cat"], "Egyéb")
            g[k] = g.get(k, 0) + (i.get("bytes") or i.get("bytes_est") or 0)
        return g
    for b, p in plans:
        g = grp(p["items"])
        llm = g.get("LLM-ek (alap)", 0) + g.get("LLM-ek (cenzúrázatlan)", 0)
        cols = ["Életmentő: orvoslás, víz, élelem, túlélés", "Lexikonok, szótárak", "Mérnöki tudás, gyártás, kémia, elektronika", "Tudomány, oktatás, könyvtárak",
                "Magyar források", "Térképek, geoadatok", "Szoftver, OS, forráskód"]
        md.append(f"| **{b}** | {human(p['used_bytes'])} | {len(p['items'])} | {human(llm)} | " + " | ".join(human(g.get(c, 0)) for c in cols) + " |")
    md += ["", "### Melyik méret mire elég – mi jön be az előző mérethez képest", ""]
    prev = set()
    for b, p in plans:
        new_items = [i for i in p["items"] if i["id"] not in prev]
        new_items.sort(key=lambda i: (i["tier"], -(i.get("bytes") or i.get("bytes_est") or 0)))
        big = sorted(new_items, key=lambda i: -(i.get("bytes") or i.get("bytes_est") or 0))[:8]
        t0 = [i for i in new_items if i["tier"] == 0]
        line = f"- **{b}** (+{len(new_items)} elem): " + "; ".join(f"{esc(i.get('name') or i['id'])[:60]} ({human(i.get('bytes') or i.get('bytes_est'))})" for i in big)
        if t0:
            line += f". Életmentő anyag: mind a {len(t0)} tétel bent van."
        md.append(line)
        prev = {i["id"] for i in p["items"]}
    md += ["",
           "**Ajánlás:**",
           "- **1 TB** a minimum: minden életmentő és gyakorlati anyag, a lexikonok, a Survivor Library és egy erős LLM-páros.",
           "- **2–4 TB** a teljes tudásanyaghoz.",
           "- **8 TB fölött** főleg nagy nyers adathalmazok és tükrök jönnek, ezeket HDD-n vagy NAS-on érdemes tárolni.", "",
           "### Melyik meghajtót vedd", "",
           "- **Munkameghajtó (a gépben):** NVMe SSD, TLC NAND, DRAM-cache-sel, magas TBW-értékkel. A gyors SSD a modellek **betöltését** gyorsítja, a futásukat nem.",
           "- **Archív példány (fiókban):** az SSD áram nélkül 1–3 évig tartja megbízhatóan az adatot (gyártófüggő, becslés). **Hosszú távra HDD** (CMR, nem SMR) vagy **M-DISC** kell. A HDD-t évente egyszer érdemes bekapcsolni és ellenőrizni.",
           "- **3-2-1 szabály:** 3 példány, 2 különböző adathordozón, 1 máshol tárolva. Javasolt összeállítás:\n"
           "  - 1 NVMe a gépben;\n"
           "  - 1 külső SSD vagy HDD otthon, fémdobozban (EMP és villám ellen);\n"
           "  - 1 HDD máshol;\n"
           "  - a 0. szint kinyomtatva.",
           "- **Fájlrendszer:** exFAT (minden gép olvassa) vagy ext4. **FAT32-t ne használj**, mert 4 GB fölötti fájlt nem kezel.",
           "- **Ellenőrzés:** minden fájl SHA-256 összegét mentsd egy `manifest`-be. Évente futtasd le a `sha256sum -c` ellenőrzést, és cseréld ki a hibás példányt.", ""]
    for b, p in plans:
        g = {}
        for i in p["items"]:
            g.setdefault(CAT_GROUP.get(i["cat"], "Egyéb"), []).append(i)
        md.append(f"<details><summary><b>{b} SSD</b> – {len(p['items'])} elem, {human(p['used_bytes'])} – a teljes lista csoportonként</summary>\n")
        for k in sorted(g, key=lambda k: -sum((i.get('bytes') or i.get('bytes_est') or 0) for i in g[k])):
            L = sorted(g[k], key=lambda i: (i["tier"], -(i.get("score") or 0)))
            tot = sum((i.get("bytes") or i.get("bytes_est") or 0) for i in L)
            md.append(f"**{k}** – {human(tot)}: " + "; ".join(f"{esc(i.get('name') or i['id'])[:70]} ({human(i.get('bytes') or i.get('bytes_est'))})" for i in L) + "\n")
        md.append("</details>\n")
    return "\n".join(md)


def main():
    items = []
    for f in sorted(glob.glob(os.path.join(HERE, "items_*.jsonl"))):
        for l in open(f, encoding="utf-8"):
            if l.strip():
                items.append(json.loads(l))
    ids = [i["id"] for i in items]
    dup = {i for i in ids if ids.count(i) > 1}
    if dup:
        sys.exit(f"duplikált id: {dup}")
    sec = {os.path.basename(p): open(p, encoding="utf-8").read() for p in sorted(glob.glob(os.path.join(HERE, "sections", "*.md")))}
    sel_src = open(os.path.join(HERE, "select_items.py"), encoding="utf-8").read()

    # katalógus JSONL ideiglenes fájlba a preset-számításhoz
    tmp = tempfile.mkdtemp()
    cat_path = os.path.join(tmp, "c.jsonl")
    open(cat_path, "w", encoding="utf-8").write("\n".join(json.dumps(i, ensure_ascii=False) for i in items))
    preset_rows = []
    for b, hw, who in PRESETS:
        outp = os.path.join(tmp, f"p{b}.json")
        cmd = [sys.executable, "-I", os.path.join(HERE, "select_items.py"), cat_path, "--budget", b, "--out", outp]
        if hw:
            cmd += ["--hw", hw]
        subprocess.run(cmd, check=True, capture_output=True)
        p = json.load(open(outp, encoding="utf-8"))
        its = p["items"]
        llm = [i for i in its if i["cat"].startswith("ai_models")]
        big = sorted([i for i in its if not i["cat"].startswith(("ai_models", "tools", "ai_tools"))], key=lambda x: -(x.get("bytes") or x.get("bytes_est") or 0))[:4]
        preset_rows.append(f"| **{b}** | {who} | {hw or '–'} | {len(its)} | {human(p['used_bytes'])} | "
                           f"{', '.join(i['id'] for i in llm) or '–'} | {', '.join(i['id'] for i in big)} |")

    # kategória-táblák
    bycat = {}
    for it in items:
        bycat.setdefault(it["cat"], []).append(it)
    cat_md = ["---\n\n## 5. Katalógus kategóriánként\n",
              "> Pont = `balanced` összpontszám (0–10). T = tier. Méret: **M** = mért, **H** = hivatalos, **B** = becsült. "
              "A teljes adat (letöltési mód, licenc, megjegyzések) a 10. fejezet JSONL-jében van. Az LLM-ek a 6. fejezetben.\n"]
    order = sorted(bycat, key=lambda c: (min(i["tier"] for i in bycat[c]), -max(score(i) for i in bycat[c])))
    for c in order:
        if c == "ai_models":
            continue
        rows = sorted(bycat[c], key=lambda x: (x["tier"], -score(x)))
        cat_md.append(f"\n### {CAT_HU.get(c, c)} (`{c}`) – {len(rows)} elem\n")
        cat_md.append("| T | Pont | id | Mi ez, mire jó | Méret | Hozzáférés | Link |\n|---|---|---|---|---|---|---|")
        for it in rows:
            st = (it.get("size_status") or "")
            tag = "M" if st.startswith("measured") else "H" if st.startswith("official") else "B"
            sz = it.get("size_human") or human(it.get("bytes") or it.get("bytes_est"))
            acc = it["access"] + (f" ({it['price']})" if it.get("price") else "")
            cat_md.append(f"| {it['tier']} | {score(it)} | `{it['id']}` | **{esc(it.get('name'))}** – {esc(it.get('desc_hu'))} | "
                          f"{esc(sz)} {tag} | {esc(acc)} | {link(it)} |")

    preset_md = ["---\n\n## 4. Előre számolt csomagok\n",
                 "`select_items.py --budget <X> --hw <T>`, `balanced` profil, nyelv: hu, en, multi, hozzáférés: free, free-registration, donation. "
                 "Ez csak tájékoztató, a pontos tervet az ágens futtatja a saját keretével.\n",
                 "| Keret | Tipikus eszköz | LLM-szint | Elemek | Felhasznált | LLM | 4 legnagyobb tartalmi elem |",
                 "|---|---|---|---|---|---|---|", *preset_rows]

    llm_md = sec.get("06_llm.md", "---\n\n## 6. Helyi LLM-ek\n\n(készül)\n") + "\n" + sec.get("06b_unlock.md", "")
    llm_items = sorted(bycat.get("ai_models", []), key=lambda x: (x["tier"], -score(x)))

    LLM_KEYS = ("id", "name", "cat", "tier", "group", "variant_rank", "lang", "access", "license", "bytes", "size_status", "format",
                "download", "scores", "hw_tiers", "platform", "llm_aa", "llm_aa_est", "llm_bits", "active_b", "moe", "released")

    def compact(i):
        if i["cat"].startswith("ai_models") and "llm_aa" in i:
            d = {k: i[k] for k in LLM_KEYS if k in i}
            d["size_status"] = "measured:2026-11-14:hf-api"
            d["license"] = str(d.get("license", ""))[:20]
            return d
        d = dict(i)
        if d.get("bytes"):
            d.pop("size_human", None)
        return d
    jsonl = "\n".join(json.dumps(compact(i), ensure_ascii=False, separators=(",", ":")) for i in
                      sorted(items, key=lambda x: (x["tier"], x["cat"], x["id"])))
    n_measured = sum(1 for i in items if (i.get("size_status") or "").startswith("measured"))
    head = sec["01_head.md"].replace("{{BUILD_DATE}}", datetime.date.today().isoformat()).replace("{{N_ITEMS}}", f"{len(items)} ({n_measured} mért méretű)")
    plans = ssd_plans(cat_path, tmp)
    json.dump([[b, [{k: i.get(k) for k in ("id", "name", "cat", "tier", "bytes", "bytes_est", "score", "desc_hu")} for i in p["items"]], p["used_bytes"]] for b, p in plans],
              open(os.path.join(HERE, "ssd_plans.json"), "w", encoding="utf-8"), ensure_ascii=False)
    parts = [head, sec["02_prompt.md"], sec["03_rules.md"], sec["04_scoring.md"], "\n".join(preset_md), ssd_section(plans), "\n".join(cat_md), llm_md,
             sec["07_recipes.md"], sec.get("08_manual.md", ""), sec.get("09_web.md", ""),
             "---\n\n## 10. Gépi katalógus\n\nSoronként egy JSON-objektum. Mezők: `id`, `name`, `cat`, `tier` (0–5), `group` (egymást kizáró változatok), "
             "`variant_rank`, `variant_role` (`pref` = ajánlott, `luxury`), `desc_hu`, `lang`, `access` (free | free-registration | donation | paid | gray | physical), `price`, "
             "`license`, `bytes` (mért vagy hivatalos), `bytes_est` (becsült), `size_status`, `format`, `info_url`, `download` {method, …}, `url_status`, "
             "`scores` {S,R,A,U,Q,O}, `requires`, `subsumed_by`, `hw_tiers` (LLM: T1–T5), `notes`.\n\n```jsonl\n" + jsonl + "\n```\n",
             "---\n\n## 11. select_items.py\n\n```python select_items.py\n" + sel_src + "```\n",
             "---\n\n## 12. llm_calc.py\n\nEszköz-kalkulátor (lásd 6.10). Kibontás: `sed -n '/^```python llm_calc.py$/,/^```$/p' ARCHIVUM.md | sed '1d;$d' > llm_calc.py`\n\n```python llm_calc.py\n"
             + open(os.path.join(HERE, "llm_calc.py"), encoding="utf-8").read() + "```\n"]
    open(OUT, "w", encoding="utf-8").write("\n\n".join(p.strip("\n") + "\n" for p in parts if p))
    print(f"OK: {OUT}  elemek={len(items)}  méret={os.path.getsize(OUT)/1e3:.0f} KB")
    # --- kompakt változat chatbe töltéshez ---
    full = open(OUT, encoding="utf-8").read()
    seen, keep = set(), []
    for i in sorted(items, key=lambda x: (x["tier"], x["cat"], x["id"])):
        if i["cat"].startswith("ai_models") and "llm_aa" in i:
            key = (i["group"], i["platform"], i["llm_bits"])
            if key in seen:
                continue
            seen.add(key)
        c = compact(i)
        if c.get("notes") and len(c["notes"]) > 240:
            c["notes"] = c["notes"][:240] + "…"
        keep.append(json.dumps(c, ensure_ascii=False, separators=(",", ":")))
    import re as _re
    comp = _re.sub(r"(?s)\n---\n\n## 5\. Katalógus kategóriánként.*?(?=\n---\n\n## 6\.)",
                   "\n---\n\n## 5. Katalógus kategóriánként\n\n*A kompakt változatból kimaradt; a teljes adat a 10. fejezet JSONL-jében van, emberi táblákért lásd a teljes ARCHIVUM.md-t.*\n", full)
    comp = _re.sub(r"(?s)### 6\.4 .*?(?=### 6\.5 )",
                   "### 6.4 Kvantált változatok\n\nA kompakt változatban modellenként és platformonként bitszintenként egy változat szerepel a JSONL-ben. Az összes (609) változat linkkel a teljes ARCHIVUM.md-ben van.\n\n", comp)
    comp = _re.sub(r"(?s)```jsonl\n.*?```", lambda m: "```jsonl\n" + "\n".join(keep) + "\n```", comp, count=1)
    comp = comp.replace("# ARCHIVUM – Offline tudásarchívum", "# ARCHIVUM (kompakt) – Offline tudásarchívum", 1)
    cp = os.path.join(HERE, "..", "ARCHIVUM-kompakt.md")
    open(cp, "w", encoding="utf-8").write(comp)
    print(f"OK: {cp}  JSONL-sorok={len(keep)}  méret={os.path.getsize(cp)/1e3:.0f} KB")


if __name__ == "__main__":
    main()
