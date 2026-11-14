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
