# Offline archívum (ARCHIVUM)

- **`ARCHIVUM.md`**: a teljes katalógus (~1 MB, 922 tétel, ebből 609 LLM-kvant). Eszközhasználó AI-ágensnek való: Claude Code, Codex vagy más ágens, amely parancsot futtat.
- **`ARCHIVUM-kompakt.md`**: chatbe feltöltéshez (~540 KB). Kimarad belőle az emberi kategóriatábla és az LLM-kvantok teljes listája.

Mindkettő önálló: tartalmazza az AI-promptot, a szabályokat, a pontozást, a gépi JSONL-katalógust és a beágyazott `select_items.py`-t.

```bash
sed -n '/^```python select_items.py$/,/^```$/p' ARCHIVUM.md | sed '1d;$d' > select_items.py
python3 select_items.py ARCHIVUM.md --budget 1TB --hw T3 --mem 160GB --emit-sh dl.sh
```

Újragenerálás: `cd src && python3 gen_sections.py && python3 build.py`.
Források:
- `src/items_*.jsonl`: tételek;
- `src/research/`: a kutatási nyersanyag;
- `src/overrides_*.py`: kézi javítások.

## Fájlok a ZIP-ben
- **`ARCHIVUM-LLM.html`** – offline kalkulátor (4 változat bármely eszközre), eszközmátrix 22 profillal (köztük a feloldott RTX 6090), modelltábla (AA v5, % Opus 5.5), **SSD-tervező 1–32 TB**. Böngészőben nyisd meg, internet nem kell.
- **`ARCHIVUM.md`** – a teljes katalógus (989 tétel), AI-ágensnek; **`ARCHIVUM-kompakt.md`** – chatbe tölthető változat.
  - 1. fejezet: AI-prompt · 2: szabályok · 3: pontozás · 4/4b: csomagok tárhely és SSD-méret szerint · 5: katalógus kategóriánként
  - 6: LLM-ek (6.1 rangsor + % Opus · 6.3–6.5 modellek, cenzúrázatlanok, gépigény · 6.10 eszközönkénti 4 változat · 6.11 GeForce-feloldás)
  - 7: letöltési receptek · 8: fizetős/fizikai beszerzések · 9: captcha-mentes web (Camoufox stb.) · 10: gépi JSONL · 11–12: szkriptek
- `eszkozok/select_items.py` – letöltési terv a tárhelyhez (`--budget 2TB --hw T2 --mem 300GB --emit-sh dl.sh`)
- `eszkozok/llm_calc.py` – LLM-kalkulátor parancssorból (`--preset all` vagy saját adatok: `--gpu 32:1790 --ram 128 --ram-bw 96`)
- `forras/` – minden generátor és a kutatási nyersanyag (újragenerálás: `cd forras && python3 gen_sections.py && python3 build.py && python3 gen_html.py && python3 make_zip.py`)
