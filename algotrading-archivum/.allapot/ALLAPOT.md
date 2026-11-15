# ALGOTRADING-ARCHÍVUM – állapot (kompaktálás elleni mentés)

Független kiadás (nem az ARCHIVUM része). Forrás-spec: `.allapot/MESTERPROMPT.md` (M1–M15 modul, séma, pontozás R/E/Q/C/L/F/Z, minőségkapu ≥90/≥95, 9 ágens).

## Felhasználói kérés (2026-11-15, lényeg)
- Külön kiadás: kvant/algo trading, befektetés, tőzsde, kripto, részvény, CFD, MetaTrader-alapú algoritmikus kereskedés, AI trading, Polymarket/Kalshi, sportfogadás (hosszú/rövid táv), statisztikai elhajlások, hírek, gazdaság, Bloomberg- és Aladdin-szerű platform alap- és főadatai.
- Saját mega-prompt, feljavítva → az alapján kutatás. Fejlesztőcsapatnak adja át.
- Megrendelőnél már fut grid alapú algo bérelt szerveren. Cél: sokrétű, óriási beállítástárral, minden stratégia: számolás, előrejelzés, backtest, jövőbeli variációk; súlyozott statisztika; több AI (statisztikai, „Javhez hasonló” – értelmezendő), LLM, ördögügyvéd (mindenki ellen, a felhasználó ellen is) → meta-platform.
- Fő fókusz: gyorsabb pénzkeresés Vantage 1:500 MetaTrader-számlán automatizált programmal; a szoftvert AI-jal gyártják; „AI mozgatókar” (autonóm jogkör).
- Hardver, szerverhelyek, hova költözzünk, milyen gép – mind kutatva. A világ összes releváns linkje. Kapcsolódó statisztikák, „végtelen mélység”. Új, soha nem gondolt ötletek, stratégiák.
- Cél: jobb platform alapja, mint a Medallion, az Aladdin, a Bloomberg.
- Méret: legalább akkora, mint a blackout-kiadás. Kimenet: algotrading ZIP.

## Lépések
1. [KÉSZ] MESTERPROMPT.md
2. [FUT] 9 kutatóágens → src/research/a1..a9
3. build (md/kompakt/chat/html/jsonl/letöltő), pontozás, profilok
4. 6 átnéző → javítás → ≥90/≥95 → ZIP, commit, átadás

## Build-lánc KÉSZ (src/): build.py (research/*.jsonl → md/kompakt/chat/katalogus.jsonl/letolto.sh/FEJLESZTOI-SPEC.md, dedup id+url, profilpont 5 profil), gen_html.py (szűrhető katalógus, stratégiák, ötletek, a8 táblák, kalkulátorok: margin/stop-out, grid-csőd MC, Kelly – böngészőben tesztelve, 400px OK, 0 JS-hiba), make_zip.py (reprodukálható).
Futtatás: cd src && python3 -I build.py && python3 -I gen_html.py && python3 -I make_zip.py ; böngészőteszt: node $S/algo_check.js <html> <png>
9 ágens fut (a1..a9) → research/. Utána: build, átnézők (6), javítás.
- A9 KÉSZ: 118 tétel, a9_spec.md 873 sor (72 soros paritásmátrix, L0–L4 mozgatókar, F0–F6 ütemterv). Megj.: GitHub API nem érhető el (ecosyste.ms tükör), NautilusTrader/LEAN/ArcticDB duplikátum A5-tel (group mező).
- A2 KÉSZ: 133 tétel (81 mért/24 becsült/28 nem ell.), a2_summary.md. Hiány: webkeresési keret elfogyott; tőzsdei AZ-k nem hivatalosak; magyar 2026-os hatályon kívül helyezés részletei.
- A3 KÉSZ: 112 tétel (66 mért/42 becsült/4 nem ell.). Kulcs: SZTFH ideiglenes Polymarket-ISP-blokk 2026-01-16 óta; Kalshi HU korlátozott (becsült); Pinnacle API zárva 2025-07-23 óta → CLV-referencia Betfair; py-clob-client archivált → py-sdk, CLOB V2. Hiány: on-chain sport venue-k (Azuro, SX Bet, Overtime), Betfair historical ár.
