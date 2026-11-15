"""Kiwix metaadat (kiwix_meta.tsv) + OPDS-ből mért méretek (kiwix_resolved.jsonl) -> items_kiwix.jsonl"""
import json, sys
meta_path, resolved_path, out_path = sys.argv[1:4]
res = {}
for l in open(resolved_path):
    d = json.loads(l); res[(d["name"], d["flavour"])] = d
dirs = {"wikipedia":"wikipedia","wikibooks":"wikibooks","wiktionary":"wiktionary","wikisource":"wikisource",
        "wikiversity":"wikiversity","wikivoyage":"wikivoyage","libretexts":"libretexts","gutenberg":"gutenberg",
        "phet":"phet","ted":"ted","ifixit":"ifixit"}
def human(b):
    for u,f in (("TB",1e12),("GB",1e9),("MB",1e6)):
        if b >= f: return f"{b/f:.2f} {u}"
    return f"{b/1e3:.0f} KB"
out = open(out_path, "w")
for line in open(meta_path):
    if line.startswith("#") or not line.strip(): continue
    c = line.rstrip("\n").split("\t")
    book, fl, iid, tier, cat, group, vrank, pref, S,R,A,U,Q,O, lang, desc, sub = c
    r = res.get((book, fl))
    url = r["url"] if r else None
    fname = url.rsplit("/",1)[-1] if url else None
    d = url.split("/zim/")[1].split("/")[0] if url else None
    item = {
      "id": iid, "name": fname[:-4] if fname else book, "cat": cat, "tier": int(tier),
      "group": None if group=="-" else group, "variant_rank": None if vrank=="-" else int(vrank),
      "variant_role": None if pref=="-" else pref,
      "desc_hu": desc, "lang": lang, "access": "free", "price": None, "license": "lásd ZIM metaadat (többnyire CC-BY-SA / közkincs)",
      "bytes": r["bytes"] if r else None, "size_human": human(r["bytes"]) if r else None,
      "size_status": "measured:2026-11-14:kiwix-opds", "format": "zim",
      "info_url": f"https://library.kiwix.org/#lang=&q={book}",
      "download": {"method":"kiwix","book":book,"flavour":fl or None,"dir":d,"snapshot_file":fname,
                   "url": url, "meta4": url+".meta4" if url else None, "torrent": url+".torrent" if url else None,
                   "sha256": url+".sha256" if url else None},
      "url_status": "200 verified 2026-11-14" if r else "unverified",
      "scores": {"S":int(S),"R":int(R),"A":int(A),"U":int(U),"Q":int(Q),"O":int(O)},
      "requires": ["tool-kiwix"], "subsumed_by": [] if sub=="-" else sub.split(","), "notes": None}
    out.write(json.dumps(item, ensure_ascii=False)+"\n")
