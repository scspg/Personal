#!/usr/bin/env python3
"""ARCHIVUM.zip összeállítása a letöltéshez (a felhasználónak ezt az egy fájlt kell letöltenie)."""
import os, zipfile, datetime
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.join(HERE, "..")
OUT = os.path.join(ROOT, "ARCHIVUM.zip")
RD = "README.md" if os.path.exists(os.path.join(ROOT, "README.md")) else "OLVASS-EL.md"   # a ZIP-ből újraépítve is működjön
SRC = "src" if os.path.isdir(os.path.join(ROOT, "src")) else "forras"
FILES = [("ARCHIVUM.md", "ARCHIVUM.md"), ("ARCHIVUM-kompakt.md", "ARCHIVUM-kompakt.md"), ("ARCHIVUM-chat.md", "ARCHIVUM-chat.md"),
         ("ARCHIVUM-LLM.html", "ARCHIVUM-LLM.html"), (RD, "OLVASS-EL.md"),
         (f"{SRC}/select_items.py", "eszkozok/select_items.py"), (f"{SRC}/llm_calc.py", "eszkozok/llm_calc.py")]
SKIP = ("plan.json", "dl.sh", "download.sh")          # select_items.py kimenetei ne kerüljenek a ZIP-be


def add(z, path, arc):                               # rögzített időbélyeg és jogosultság → bájtra azonos ZIP
    zi = zipfile.ZipInfo(arc, (1980, 1, 1, 0, 0, 0)); zi.compress_type = zipfile.ZIP_DEFLATED; zi.external_attr = 0o644 << 16
    with open(path, "rb") as f:
        z.writestr(zi, f.read(), compresslevel=9)


with zipfile.ZipFile(OUT, "w") as z:
    for src, dst in FILES:
        add(z, os.path.join(ROOT, src), "ARCHIVUM/" + dst)
    for dp, dn, fn in os.walk(HERE):            # forrás + kutatási nyersanyag (újragenerálhatóság)
        dn[:] = sorted(d for d in dn if d != "__pycache__")
        for f in sorted(fn):
            if f in SKIP or f.endswith(".pyc"):
                continue
            p = os.path.join(dp, f)
            add(z, p, "ARCHIVUM/forras/" + os.path.relpath(p, HERE))
print(f"OK: {OUT} ({os.path.getsize(OUT) / 1e6:.2f} MB), {datetime.date.today()}")
