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
 "server_bundle": "Offline szerver-csomagok", "tools": "Olvasók, futtatók (kötelező)", "bundle": "Kész csomagok (kereskedelmi)",
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
        llm = [i for i in its if i["cat"] == "ai_models"]
        big = sorted([i for i in its if i["cat"] not in ("ai_models", "tools")], key=lambda x: -(x.get("bytes") or x.get("bytes_est") or 0))[:4]
        preset_rows.append(f"| **{b}** | {who} | {hw or '–'} | {len(its)} | {human(p['used_bytes'])} | "
                           f"{', '.join(i['id'] for i in llm) or '–'} | {', '.join(i['id'] for i in big)} |")

    # kategória-táblák
    bycat = {}
    for it in items:
        bycat.setdefault(it["cat"], []).append(it)
    cat_md = ["---\n\n## 5. Katalógus kategóriánként\n",
              "> Pont = `balanced` összpontszám (0–10). T = tier. Méret: **M** = mért, **H** = hivatalos, **B** = becsült. "
              "A teljes adat (letöltési mód, licenc, megjegyzések) a 9. fejezet JSONL-jében van.\n"]
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

    llm_md = sec.get("06_llm.md", "---\n\n## 6. Helyi LLM-ek\n\n(készül)\n")
    llm_items = sorted(bycat.get("ai_models", []), key=lambda x: (x["tier"], -score(x)))

    jsonl = "\n".join(json.dumps(i, ensure_ascii=False, separators=(",", ":")) for i in
                      sorted(items, key=lambda x: (x["tier"], x["cat"], x["id"])))
    n_measured = sum(1 for i in items if (i.get("size_status") or "").startswith("measured"))
    head = sec["01_head.md"].replace("{{BUILD_DATE}}", datetime.date.today().isoformat()).replace("{{N_ITEMS}}", f"{len(items)} ({n_measured} mért méretű)")
    parts = [head, sec["02_prompt.md"], sec["03_rules.md"], sec["04_scoring.md"], "\n".join(preset_md), "\n".join(cat_md), llm_md,
             sec["07_recipes.md"], sec.get("08_manual.md", ""),
             "---\n\n## 9. Gépi katalógus\n\nSoronként egy JSON-objektum. Mezők: `id`, `name`, `cat`, `tier` (0–5), `group` (egymást kizáró változatok), "
             "`variant_rank`, `variant_role` (`pref` = ajánlott, `luxury`), `desc_hu`, `lang`, `access` (free | free-registration | donation | paid | gray | physical), `price`, "
             "`license`, `bytes` (mért vagy hivatalos), `bytes_est` (becsült), `size_status`, `format`, `info_url`, `download` {method, …}, `url_status`, "
             "`scores` {S,R,A,U,Q,O}, `requires`, `subsumed_by`, `hw_tiers` (LLM: T1–T5), `notes`.\n\n```jsonl\n" + jsonl + "\n```\n",
             "---\n\n## 10. select_items.py\n\n```python select_items.py\n" + sel_src + "```\n"]
    open(OUT, "w", encoding="utf-8").write("\n\n".join(p.strip("\n") + "\n" for p in parts if p))
    print(f"OK: {OUT}  elemek={len(items)}  méret={os.path.getsize(OUT)/1e3:.0f} KB")


if __name__ == "__main__":
    main()
