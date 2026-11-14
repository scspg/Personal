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
with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as z:
    for src, dst in FILES:
        z.write(os.path.join(ROOT, src), "ARCHIVUM/" + dst)
    for dp, dn, fn in os.walk(HERE):            # forrás + kutatási nyersanyag (újragenerálhatóság)
        if "__pycache__" in dp:
            continue
        for f in fn:
            p = os.path.join(dp, f)
            z.write(p, "ARCHIVUM/forras/" + os.path.relpath(p, HERE))
print(f"OK: {OUT} ({os.path.getsize(OUT) / 1e6:.2f} MB), {datetime.date.today()}")
