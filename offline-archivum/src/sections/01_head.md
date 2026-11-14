# ARCHIVUM – Offline tudásarchívum blackout és összeomlás esetére

> **Verzió:** {{BUILD_DATE}} · **Elemek:** {{N_ITEMS}} · **Minden ellenőrizhető méret mért adat** (Kiwix OPDS, HTTP Content-Length, Hugging Face API, Ollama registry). A státuszt minden elem `size_status` / `url_status` mezője mutatja.
> **Cél:** ezt az egy fájlt egy eszközhasználó AI-ágensnek (Claude Code, Codex, Open Interpreter, aider stb.) beadva az ágens kiválasztja a tárhelyhez illő csomagot, és letölti, ellenőrzi és rendszerezi.

## Tartalom
0. [Gyorsindítás embernek](#0-gyorsindítás-embernek)
1. [AGENT PROMPT – ezt másold be az AI-nak](#1-agent-prompt)
2. [Szabályok és buktatók – mire figyeljen az AI](#2-szabályok-és-buktatók)
3. [Pontozási rendszer](#3-pontozási-rendszer)
4. [Előre számolt csomagok tárhely szerint](#4-előre-számolt-csomagok) · **4b. [Hány TB-os SSD kell? (1–32 TB)](#4b-hány-tb-os-ssd-kell--csomagok-1-2-4-8-16-és-32-tb-ra)**
5. [Katalógus kategóriánként (emberi nézet)](#5-katalógus-kategóriánként) · **5b. [Mindenre a legjobb nyílt forráskódú szoftver és modell](#5b-mindenre-a-legjobb-nyílt-forráskódú-szoftver-és-modell)**
6. [NAGY FEJEZET: helyi, nyílt súlyú LLM-ek](#6-helyi-llm-ek) – 6.10: eszközönkénti ajánlás 4 változatban · 6.11: GeForce-feloldás
7. [Letöltési receptek módszerenként](#7-letöltési-receptek)
8. [Fizetős, regisztrációs és fizikai beszerzések](#8-fizetős-regisztrációs-és-fizikai-beszerzések)
9. [Webes hozzáférés az AI-nak: captcha- és blokkmentes keresés és letöltés (Camoufox és társai)](#9-webes-hozzáférés-az-ai-nak-captcha--és-blokkmentes-keresés-és-letöltés)
10. [Gépi katalógus (JSONL) – a szkript ezt olvassa](#10-gépi-katalógus)
11. [select_items.py – kiválasztó és letöltő-generátor](#11-select_itemspy)
12. [llm_calc.py – LLM-eszközkalkulátor (melyik modell fut a gépeden)](#12-llm_calcpy)

---

## 0. Gyorsindítás embernek

1. Szerezz egy meghajtót. Ajánlott: **exFAT** (Windows/Mac/Linux mind olvassa) vagy **ext4** (csak Linux). **FAT32-t ne használj**, mert nem kezel 4 GB-nál nagyobb fájlt, a Wikipedia ZIM pedig 127 GB.
2. Add ezt a fájlt egy olyan AI-ágensnek, amely parancsot tud futtatni. Írd mellé például ezt: *„Van egy 1 TB-os meghajtóm a /media/usb alatt, RTX 4090 + 128 GB RAM gépem, magyar és angol anyag kell, főleg orvosi és mezőgazdasági. Csináld meg.”*
3. Ha kézzel csinálnád:
   ```bash
   # a szkript a 11. fejezetből bontható ki, és magát az .md fájlt olvassa (10. fejezet):
   sed -n '/^```python select_items.py$/,/^```$/p' ARCHIVUM.md | sed '1d;$d' > select_items.py
   python3 select_items.py ARCHIVUM.md --budget 1TB --profile balanced --langs hu,en,multi --hw T3 --mem 160GB --emit-sh dl.sh
   less dl.sh && DEST=/media/usb/archivum bash dl.sh
   ```
4. **Fontos:**
   - Két példány legyen, két külön helyen.
   - A 0. szint (orvoslás, víz) **legyen kinyomtatva** is.
   - Az olvasóprogramok telepítői (Kiwix, VLC, PDF-olvasó, llama.cpp) is kerüljenek fel a meghajtóra (a `tool-*` elemek).
