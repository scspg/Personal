# ARCHIVUM – offline tudásarchívum (olvass el)

## Kezdd itt
1. **Nyisd meg böngészőben az `ARCHIVUM-LLM.html`-t** (internet nem kell): kalkulátor (melyik AI-modell fut a gépeiden), eszközmátrix, modelltábla, a legjobb nyílt forráskódú szoftverek és modellek kereshető listája, SSD-tervező 1–128 TB-ra és tárolóválasztó (termékek, árak, bolti linkek).
2. **Letöltés a meghajtóra:** add oda az `ARCHIVUM.md`-t egy parancsot futtatni tudó AI-ágensnek (Claude Code, Codex stb.), és másold be neki az 1. fejezet promptját kitöltve. Vagy kézzel:
   ```bash
   python3 eszkozok/select_items.py ARCHIVUM.md --budget 1TB --hw T3 --mem 160GB --emit-sh dl.sh
   less dl.sh && DEST=/media/usb/archivum bash dl.sh
   ```
3. **Chatbe** (eszköz nélküli AI-nak) az `ARCHIVUM-chat.md`-t add be.

## Fájlok
| Fájl | Méret | Mire való |
|---|---|---|
| `ARCHIVUM-LLM.html` | 0,9 MB | interaktív kalkulátor, eszközmátrix, modelltábla (AA v5, % Opus 5.5), szoftver- és modellkönyvtár (kereshető), SSD-tervező |
| `ARCHIVUM.md` | 2,2 MB | teljes katalógus: 1261 tétel (ebből 609 LLM-kvant), prompt, szabályok, receptek, szkriptek |
| `ARCHIVUM-kompakt.md` | 1,6 MB | ugyanez kevesebb LLM-kvanttal (897 tétel) – hosszú kontextusú modellnek |
| `ARCHIVUM-chat.md` | 0,1 MB | rövid összefoglaló chatbe: csomagok, SSD-méretek, LLM-rangsor, eszközajánlások, legjobb szoftverek |
| `eszkozok/select_items.py` | – | letöltési terv a tárhelyhez (`--budget 2TB --hw T2 --mem 300GB --emit-sh dl.sh`) |
| `eszkozok/llm_calc.py` | – | LLM-kalkulátor (`--preset all`, vagy saját: `--gpu 32:1790 --ram 128 --ram-bw 96`) |
| `forras/` | – | generátorok és a kutatási nyersanyag |

## A katalógus fejezetei
1 AI-prompt · 2 szabályok · 3 pontozás · 4/4b csomagok tárhely és SSD-méret szerint · 5 katalógus kategóriánként · 5b mindenre a legjobb nyílt forráskódú szoftver és modell (GitHub, GitLab, Codeberg, Hugging Face stb.) ·
4c tárolók (termékek árral és bolti linkkel, 2 példányos stratégia, kockázatszámítás) ·
6 LLM-ek (6.1 rangsor + % Opus · 6.5 cenzúrázatlanok és gépigény · 6.10 eszközönként 4 változat · 6.11 GeForce-feloldás) ·
7 letöltési receptek · 8 fizetős/fizikai beszerzések · 9 captcha-mentes web · 10 gépi JSONL · 11–12 szkriptek

## Újragenerálás
```bash
cd forras && python3 gen_sections.py && python3 build.py && python3 gen_html.py && python3 make_zip.py
```
(Python 3.9+, csak standard könyvtár; a `forras/` mappában a `make_zip.py` a ZIP szerkezetéből is működik.)
