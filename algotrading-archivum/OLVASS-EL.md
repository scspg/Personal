# ALGOTRADING – olvass el először

Kvant-, algo- és AI-kereskedési archívum egy pénzügyi meta-platform építéséhez. A középpontban a MetaTrader 5 (Vantage, 1:500) automatizált kereskedés áll; mellette kripto, predikciós piacok, sportfogadás, makró, hírek és kockázati motor. Kutatás: 2026-11-15. Nem befektetési, adó- vagy jogi tanácsadás.

## Mit hol találsz

| Fájl | Mire való |
|---|---|
| `ALGOTRADING.html` | Böngészőben megnyitható. Szűrhető katalógus (ár, hozzáférés, profil), stratégiák, ötletek, infrastruktúra-táblák és kalkulátorok (1:500 margin és stop-out, grid-csőd Monte Carlo, Kelly). Internet nélkül is működik. |
| `ALGOTRADING.md` | A teljes anyag: mesterprompt, pontozás, költségvetés szerinti válogatás, fejezetenként a tételek, stratégia-könyvtár, kockázati matek, hipotézisgyár, szerverhely- és adótáblák, fejlesztői specifikáció. |
| `FEJLESZTOI-SPEC.md` | A fejlesztőcsapatnak: architektúra, MT5-híd, döntési réteg ördögügyvéddel, kockázati motor, a „mozgatókar” jogosultsági szintjei, ütemterv ellenőrizhető átvételi feltételekkel. |
| `ALGOTRADING-chat.md` | Tömör változat LLM-kontextusba (ChatGPT, Claude, helyi modell): egy sor = egy tétel. |
| `ALGOTRADING-kompakt.md` | Csak a 0–1. szintű (nélkülözhetetlen és erősen ajánlott) tételek. |
| `katalogus.jsonl` | Gépi katalógus, soronként egy JSON-objektum, pontszámokkal (R, E, Q, C, L, F, Z) és profilpontokkal. |
| `letolto.sh` | Az ingyenes, automatikusan letölthető források (git-repók, fájlok, HF) letöltése. |
| `forras/` | A teljes forrás: kutatási nyersanyag (`research/`), build-szkriptek, mesterprompt, állapotnapló. |

## Gyors indulás

1. Nyisd meg az `ALGOTRADING.html`-t, válaszd a „Gyors pénz MT5-ön” profilt, és szűrj költségre.
2. A kockázati számokat a „Kalkulátorok” fülön a saját számlád adataival számold újra.
3. Ingyenes források letöltése (Linux/macOS, Windowson WSL-ben):

```bash
DEST=/abszolut/ut/algo bash letolto.sh
```

4. Újraépítés a forrásból (Python 3.9+, külső csomag nem kell):

```bash
cd forras && python3 -I build.py && python3 -I gen_html.py && python3 -I make_zip.py
```

## Jelölések

- **Ellenőrzés:** „mért” = a forrás oldalán látott adat a kutatás napján; „becsült” = számított vagy közvetett; „nem ellenőrzött” = nem volt megerősíthető.
- **Szint:** 0 = nélkülözhetetlen mag · 1 = erősen ajánlott · 2 = bővítés · 3 = luxus vagy intézményi.
- **Pontok (0–10):** R relevancia · E edge-potenciál · Q minőség · C költséghatékonyság · L késleltetés/frissesség · F karbantartottság · Z jogi/ÁSZF-biztonság. A profilpont 0–100.

## A legfontosabb figyelmeztetések (részletek a kockázati fejezetben)

- 1:500 áttételnél teljes margin-kihasználás mellett 0,2%-os (EURUSD-n kb. 22 pipes) ellenirányú mozgás nullázza a számlát.
- A grid és a martingale csődvalószínűsége valódi előny nélkül néhány éven belül a többségi esetet jelenti; a túlélő pályák hozama túlélési torzítás.
- Az offshore jogalanynál vezetett CFD-számla magyar adózása valószínűleg kedvezőtlenebb (egyéb jövedelem), mint az EU-s brókernél; a NAV külföldi számlaadatokat kap (CRS).
- A Vantage ügyfélszerződésének visszaélés-záradékait (carry trade, arbitrázs) élesítés előtt el kell olvasni.
