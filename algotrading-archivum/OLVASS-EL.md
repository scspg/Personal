# ALGOTRADING – olvass el először

Kvant-, algo- és AI-kereskedési archívum egy pénzügyi meta-platform építéséhez. A középpontban az aktív, automatizált kereskedés áll, platform- és brókerfüggetlen alapokon (a jelenlegi eszköz MetaTrader – MT4 vagy MT5, ezt a specifikáció Q1 kérdése rögzíti – és Vantage 1:500, de cserélhető); mellette kripto, predikciós piacok, sportfogadás, makró, hírek és kockázati motor. Kutatás: 2026-11-15. Nem befektetési, adó- vagy jogi tanácsadás.

## Mit hol találsz

| Fájl | Mire való |
|---|---|
| `ALGOTRADING.html` | Böngészőben megnyitható. Szűrhető katalógus (ár, hozzáférés, profil), stratégiák, ötletek, infrastruktúra-táblák és kalkulátorok (1:500 margin és stop-out, grid-csőd Monte Carlo, Kelly). Internet nélkül is működik. |
| `ALGOTRADING.md` | A teljes anyag: mesterprompt, pontozás, költségvetés szerinti válogatás, fejezetenként a tételek, stratégia-könyvtár, kockázati matek, hipotézisgyár, szerverhely- és adótáblák, fejlesztői specifikáció. |
| `FEJLESZTOI-SPEC.md` | A fejlesztőcsapatnak: architektúra, MT5-híd, döntési réteg ördögügyvéddel, kockázati motor, a „mozgatókar” jogosultsági szintjei, ütemterv ellenőrizhető átvételi feltételekkel. |
| `ALGOTRADING-chat.md` | Tömör változat LLM-kontextusba (ChatGPT, Claude, helyi modell): egy sor = egy tétel. Kb. 400 KB, 100–120 ezer token: a 200 ezres kontextusú modellekbe egyben belefér, kisebbekbe fejezetenként kell betölteni. |
| `ALGOTRADING-kompakt.md` | Csak a 0–1. szintű (nélkülözhetetlen és erősen ajánlott) tételek. |
| `katalogus.jsonl` | Gépi katalógus, soronként egy JSON-objektum, pontszámokkal (R, E, Q, C, L, F, Z) és profilpontokkal. Séma: mesterprompt 2. és 2.1. fejezet. |
| `strategiak.jsonl`, `otletek.jsonl` | A stratégia-könyvtár és a hipotézisgyár gépi formában (előregisztrációs mezőkkel). |
| `letolto.sh` | Az ingyenes, automatikusan letölthető források (git-repók, fájlok, HF) letöltése. |
| `forras/` | A teljes forrás: kutatási nyersanyag (`research/`), build-szkriptek, mesterprompt, állapotnapló. |

## Fejlesztőknek – innen indulj

1. `FEJLESZTOI-SPEC.md` – a specifikáció saját olvasási sorrendje: §0 (célok, elvek) → §2 (szerződések, `contracts.py`) → §12 (platform- és brókerfüggetlenség; ütközés esetén ez dönt) → §10 (ütemterv, átvételi feltételek). A HTML „Fejlesztői spec” fülén kattintható tartalomjegyzék van.
2. `forras/allapot/MESTERPROMPT.md` – a kutatás és a katalógus specifikációja (séma, rubrika, profilsúlyok).
3. `ALGOTRADING.md` 25–27. fejezet – stratégiák, kockázati matek, hipotézisgyár; 6–7. fejezet – platform- és bróker-összehasonlítás.
4. A „Nyitott kérdések az ügyfélnek” szakasz a specifikációban: ezekre a válasz az F1 fázis feltétele.

## Szójegyzék

| Rövidítés | Jelentés |
|---|---|
| A1–A11 | a kutatási területek (ágensek): A1 piac és végrehajtás, A2 kripto, A3 predikció és sport, A4 makró/hírek/alt adat, A5 nyílt szoftver, A6 AI-kutatás és irodalom, A7 stratégiák/kockázat/ötletek, A8 infrastruktúra/adó/jog, A9 platform-architektúra, A10 bevált módszerek, A11 platform- és bróker-összehasonlítás |
| M1–M16 | a mesterprompt moduljai (M1 piaci adat … M16 bevált statisztikai módszerek) |
| F0–F6 | a fejlesztési ütemterv fázisai |
| L0–L4 | az AI „mozgatókar” (autonóm végrehajtás) jogosultsági szintjei: L0 csak elemzés … L4 korlátozott teljes autonómia |
| ETÜ | ellenőrzött tőkepiaci ügylet (Szja tv. 67/A. §) – kedvezőbb magyar adózás |
| PIT | point-in-time: az adat úgy, ahogy az adott pillanatban ismert volt (look-ahead nélkül) |
| DSR, PSR, PBO, CPCV | deflált Sharpe-mutató, valószínűségi Sharpe-mutató, a backtest túlillesztésének valószínűsége, kombinatorikus tisztított keresztvalidálás |
| NBP | negatívegyenleg-védelem |

## Gyors indulás

1. Nyisd meg az `ALGOTRADING.html`-t, válaszd a „Gyors pénz – aktív automatizált” profilt, és szűrj költségre.
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
