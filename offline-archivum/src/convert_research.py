#!/usr/bin/env python3
"""Kutató-ágensek YAML-kimenete (research/*.yaml.txt) -> items_<név>.jsonl, egységes sémára.
Használat: python3 convert_research.py research/medicine_food_agri.yaml.txt items_medfood.jsonl [overrides.py]"""
import json, re, sys, yaml, runpy

UNIT = {"KB": 1e3, "MB": 1e6, "GB": 1e9, "TB": 1e12, "PB": 1e15, "KIB": 2**10, "MIB": 2**20, "GIB": 2**30, "TIB": 2**40, "PIB": 2**50}
FILE_EXT = r"(?:pdf|iso|zip|epub|csv|json|tar\.gz|tgz|7z|gz|xz|bz2|mp4|zim|gguf|djvu|txt|sha1|md5|torrent|exe|dmg|apk|AppImage|img|pbf|tif|nc)"
W = {"S": .30, "R": .25, "A": .15, "U": .15, "Q": .10, "O": .05}
CAT_MAP = {"water": "water_sanitation", "sanitation": "water_sanitation", "open-hardware": "open_hardware"}


def load_yaml(path):
    t = open(path, encoding="utf-8").read()
    blocks = re.findall(r"```ya?ml\n(.*?)```", t, re.S)
    out = []
    for b in (blocks or [t]):
        # elemenként parse-olunk, hogy egy hibás elem ne vigye el az egészet
        chunks = re.split(r"(?m)^(?=- id:)", b)
        for ch in chunks:
            if not ch.lstrip().startswith("- id:"):
                continue
            for attempt in (ch, sanitize(ch)):
                try:
                    d = yaml.safe_load(attempt)
                    if isinstance(d, list):
                        out += [x for x in d if isinstance(x, dict) and x.get("id")]
                    break
                except yaml.YAMLError as e:
                    err = e
            else:
                print(f"YAML hiba {path}: {ch[:60]!r}: {err}", file=sys.stderr)
    return out


SCALAR_KEYS = r"([a-z_0-9]+)"


def sanitize(ch):
    """Idézőjel nélküli, ': '-t tartalmazó skalárértékek idézése."""
    lines = []
    for line in ch.splitlines():
        m = re.match(r"^(\s*-?\s*" + SCALAR_KEYS + r":\s)(.*)$", line)
        if m and m.group(3) and not m.group(3)[:1] in "\"'|>[{":
            v = m.group(3).replace("\\", "\\\\").replace('"', '\\"')
            line = f'{m.group(1)}"{v}"'
        lines.append(line)
    return "\n".join(lines)


def parse_size(s):
    if not s:
        return None
    s = re.sub(r"\([^)]*\)", " ", str(s).replace(",", ""))
    tot = 0.0
    for num, unit in re.findall(r"([\d.]+)\s*([KMGTP]i?B)\b", s, re.I):
        try:
            tot += float(num) * UNIT[unit.upper()]
        except (ValueError, KeyError):
            pass
    return int(tot) if tot else None


def expand_patterns(text, base_url):
    """en_wtnd_2025_{fm,01..23,bm,resc}.pdf -> teljes URL-lista a base_url könyvtárában"""
    urls = []
    if not text or not base_url:
        return urls
    base = base_url.rsplit("/", 1)[0] + "/"
    for stem, body, ext in re.findall(r"([\w.-]+?)_?\{([^}]+)\}\.(\w+)", text):
        if stem.rstrip("_-") not in base_url.rsplit("/", 1)[-1] and stem.rstrip("_-") not in base_url:
            continue  # csak a letöltési URL saját fájlnév-mintáját bontjuk ki
        parts = []
        for p in body.split(","):
            p = p.strip()
            m = re.fullmatch(r"(\d+)\.\.(\d+)", p)
            if m:
                w = len(m.group(1))
                parts += [str(i).zfill(w) for i in range(int(m.group(1)), int(m.group(2)) + 1)]
            elif p:
                parts.append(p)
        sep = "_" if not stem.endswith("_") else ""
        urls += [f"{base}{stem}{sep}{p}.{ext}" for p in parts]
    return urls


def tier_of(sc, access):
    c = sum(W[k] * sc.get(k, 0) for k in W)
    if sc.get("S", 0) >= 8 and sc.get("A", 0) >= 7:
        return 0
    if c >= 6.6:
        return 1
    if c >= 5.6:
        return 2
    if c >= 4.6:
        return 3
    if c >= 3.6:
        return 4
    return 5


def human(b):
    for u, f in (("TB", 1e12), ("GB", 1e9), ("MB", 1e6), ("KB", 1e3)):
        if b and b >= f:
            return f"{b / f:.2f} {u}"
    return None


def convert(x, ov):
    sc = x.get("scores") or {}
    sc = {"S": sc.get("survival", 0), "R": sc.get("rebuild", 0), "A": sc.get("actionable", 0),
          "U": sc.get("uniqueness", 0), "Q": sc.get("reliability", 0), "O": sc.get("offline_ease", 0)}
    sc = {k: int(round(float(v or 0))) for k, v in sc.items()}
    method = (x.get("method") or "manual").strip()
    if method == "purchase":
        method = "manual"
    dl_url = x.get("url_download")
    notes = x.get("notes") or ""
    dl = {"method": method}
    if method in ("http",):
        urls = expand_patterns(notes, dl_url) if "{" in notes else []
        if not urls:
            urls = [dl_url] if dl_url else []
            urls += [u.rstrip(".,);") for u in re.findall(r"https?://\S+?\." + FILE_EXT + r"\b", notes)]
        seen = []
        [seen.append(u) for u in urls if u and u not in seen]
        dl["urls"] = seen
    elif method == "wget-mirror":
        dl["url"] = dl_url or x.get("url_info")
    elif method in ("rsync", "torrent", "jigdo", "s3", "ollama", "hf"):
        dl["url"] = dl_url
    elif method == "kiwix":
        m = re.search(r"book=([\w.\-]+)(?:\s+flavour=(\w+))?", notes)
        dl = {"method": "kiwix", "book": m.group(1) if m else None, "flavour": (m.group(2) if m else None), "url": dl_url}
        if not dl["book"]:
            dl = {"method": "http", "urls": [dl_url]} if dl_url else {"method": "manual"}
    elif method == "git":
        dl["repos"] = [u for u in re.split(r"[\s,]+", str(dl_url or x.get("url_info") or "")) if u.startswith("http")]
    elif method in ("archive.org", "ia-cli"):
        dl["method"] = "archive.org"
        ids = re.findall(r"archive\.org/details/([\w.\-]+)", f"{dl_url} {x.get('url_info')} {notes}")
        dl["ids"] = list(dict.fromkeys(ids))
    else:
        dl["method"] = "manual"
        if dl_url:
            dl["url"] = dl_url
    # prózában megadott "URL"-ek: csak valódi URL-tokenek maradnak; ha nincs ilyen, AI-feladat (method=agent)
    URL_RE = r"https?://[^\s;,'\"()<>]+"
    if dl.get("urls"):
        toks = []
        for u in dl["urls"]:
            toks += [t.rstrip(".") for t in re.findall(URL_RE, str(u)) if "<" not in t]
        prose = any(not re.fullmatch(URL_RE, str(u)) for u in dl["urls"])
        if prose:
            dl = {"method": "agent", "note": " | ".join(map(str, dl["urls"])), "seed_urls": toks}
        else:
            dl["urls"] = toks
    if dl.get("url") and dl["method"] in ("wget-mirror", "rsync", "torrent") and not re.match(r"^(https?|rsync)://|^[\w.-]+::", str(dl["url"])):
        dl = {"method": "agent", "note": str(dl["url"]), "seed_urls": re.findall(URL_RE, str(dl["url"])) or ([x.get("url_info")] if x.get("url_info") else [])}
    if method in ("http", "wget-mirror", "rsync", "git", "archive.org", "ia-cli", "torrent", "jigdo", "s3") and dl["method"] != "agent" and not (
            dl.get("urls") or dl.get("url") or dl.get("repos") or dl.get("ids")):
        dl = {"method": "manual", "note": "nincs ellenőrzött közvetlen link – lásd info_url"}
    b = parse_size(x.get("size"))
    st = str(x.get("size_status") or "")
    approx = "~" in str(x.get("size")) or st.startswith("estimated") or "unknown" in str(x.get("size")).lower()
    it = {"id": x["id"], "name": x.get("name"), "cat": CAT_MAP.get(x.get("category"), x.get("category")),
          "tier": tier_of(sc, x.get("access")), "desc_hu": x.get("description_hu"), "lang": x.get("language") or "en",
          "access": x.get("access") or "free", "license": x.get("license")}
    if x.get("price"):
        it["price"] = str(x["price"])
    if b and not approx:
        it["bytes"] = b
    elif b:
        it["bytes_est"] = b
    it["size_human"] = str(x.get("size") or "?")
    it["size_status"] = st
    it["format"] = x.get("format")
    it["info_url"] = x.get("url_info")
    it["download"] = dl
    it["url_status"] = x.get("url_status")
    it["scores"] = sc
    if notes:
        it["notes"] = notes
    if it["lang"] not in ("hu", "en", "multi"):
        it["lang"] = "multi" if ("," in it["lang"] or "multi" in it["lang"]) else it["lang"]
    if it["format"] and re.search(r"pdf|epub|djvu", str(it["format"]), re.I):
        it["requires"] = []
    for k in ("hw_tiers", "group", "variant_rank", "variant_role", "subsumed_by", "requires"):
        if x.get(k) is not None:
            it[k] = x[k]
    it.update(ov.get(x["id"], {}))
    return it


def main():
    src, dst = sys.argv[1], sys.argv[2]
    ov = runpy.run_path(sys.argv[3]).get("OVERRIDES", {}) if len(sys.argv) > 3 else {}
    rows = [convert(x, ov) for x in load_yaml(src)]
    drop = set(ov.get("_drop", []))
    rows = [r for r in rows if r["id"] not in drop]
    open(dst, "w", encoding="utf-8").write("\n".join(json.dumps(r, ensure_ascii=False, separators=(",", ":")) for r in rows) + "\n")
    print(f"{dst}: {len(rows)} elem")
    for r in rows:
        d = r["download"]
        n = len(d.get("urls") or []) or (1 if d.get("url") or d.get("repos") or d.get("ids") else 0)
        print(f"  T{r['tier']} {r['access']:<17} {d['method']:<11} n={n:<3} {r.get('bytes') or r.get('bytes_est') or '-':>12} {r['id']}")


if __name__ == "__main__":
    main()
