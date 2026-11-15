#!/usr/bin/env python3
"""ALGOTRADING.zip – reprodukálható (rögzített időbélyeg, rendezett tagok)."""
import os, zipfile, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
TS = (2026, 11, 15, 0, 0, 0)
FILES = ["VEGSO-PONTOZAS.md", "ALGOTRADING-chat-mini.md", "ALGOTRADING.md", "ALGOTRADING.html", "ALGOTRADING-kompakt.md", "ALGOTRADING-chat.md", "FEJLESZTOI-SPEC.md", "katalogus.jsonl", "strategiak.jsonl", "otletek.jsonl", "letolto.sh"]
out = os.path.join(ROOT, "ALGOTRADING.zip")
with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as z:
    def add(src, arc):
        zi = zipfile.ZipInfo(arc, TS); zi.compress_type = zipfile.ZIP_DEFLATED
        zi.external_attr = (0o755 if arc.endswith(".sh") else 0o644) << 16
        z.writestr(zi, open(src, "rb").read())
    for f in FILES:
        p = os.path.join(ROOT, f)
        if os.path.exists(p): add(p, "ALGOTRADING/" + f)
    rd = next(p for p in (os.path.join(ROOT, "OLVASS-EL.md"), os.path.join(HERE, "OLVASS-EL.md")) if os.path.exists(p))   # repó vagy kicsomagolt forras/
    add(rd, "ALGOTRADING/OLVASS-EL.md")
    add(rd, "ALGOTRADING/forras/OLVASS-EL.md")
    for d, sub in ((HERE, "forras"), (os.path.join(ROOT, ".allapot"), "forras/allapot")):
        for r, _, fs in sorted(os.walk(d)):
            if "__pycache__" in r: continue
            for f in sorted(fs):
                if f.endswith((".py", ".jsonl", ".md", ".json", ".yaml")) and f != "OLVASS-EL.md":
                    p = os.path.join(r, f); add(p, "ALGOTRADING/" + sub + "/" + os.path.relpath(p, d))
print(f"OK: {out} ({os.path.getsize(out)/1e6:.2f} MB)")
