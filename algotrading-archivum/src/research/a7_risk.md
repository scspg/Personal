# A7 – Kockázati matematika (M10, jogi rész nélkül)

> Kutatási ágens: A7 · Ellenőrzés dátuma: 2026-11-15 · Nyelv: magyar
> **Címkék:** `[számított]` = ebben a munkában Pythonnal számolva (numpy 2.5 / scipy 1.18); `[forrás: …]` = külső, ellenőrzött forrásból; `[feltevés]` = a példához választott bemenő paraméter; `[nem ellenőrzött]` = forrás nem igazolta; `[következtetett]` = levezetés/érvelés, nem mérés.
> **Adat:** ECB EXR napi referencia-árfolyamok (14:15 CET), 1999-01-04 – 2026-11-13, n = 7136 nap, letöltve a `https://data-api.ecb.europa.eu/service/data/EXR/D.{USD,CHF,JPY,GBP}.EUR.SP00.A?format=csvdata` végpontról 2026-11-15-én (mért). USDJPY = (JPY/EUR)/(USD/EUR) keresztárfolyam. Ez napi fixing, nem tick: az intraday szélsőértékeket (és így a valós gapeket) **alulbecsli**.

---

## 0. Kockázati figyelmeztetés (egyszer, tényszerűen, számokkal)

- 1:500 tőkeáttételnél teljes margin-kihasználás mellett **0,2%-os** ellenmozgás nullázza a számla tőkéjét, és már **0,10%** (50% stop-out) ill. **0,16%** (20% stop-out) után kényszerzárás jön `[számított, 1. fejezet]`.
- EURCHF 2015-01-14 → 2015-01-15: ECB-fixing 1,2010 → 1,0280, **−14,4%** egy nap alatt `[számított ECB-adatból]`; ennél a mozgásnál már 7× effektív tőkeáttétel fölött a veszteség meghaladja a számla tőkéjét `[számított]`.
- Egy 10 000 USD-s számlán 0,05 lot/szint, 20 pipes, korlátlan kétirányú EURUSD-grid MC-szimulációjában a stop-out valószínűsége **1 éven belül 38,8%, 3 éven belül 76,8%**, és a **minden pályára vett** várható hozam 1 év alatt **−35%** `[számított, 3.3. fejezet; paraméterek ott]`.
- A tartósan (300+ napig) daytrade-elő brazil egyének 97%-a veszített `[forrás: Chague–De-Losso–Giovannetti 2019, SSRN, https://doi.org/10.2139/ssrn.3423101, absztrakt]`.

---

## 1. Az 1:500-as tőkeáttétel matematikája

### 1.1 Definíciók (MT5)

- **Margin (Forex, leverage-alapú):** `Margin = Lot × ContractSize / Leverage` a margin-devizában; CFD „Contracts Leverage” típusnál `Lot × ContractSize × Ár / Leverage` `[forrás: MetaTrader 5 súgó, https://www.metatrader5.com/en/terminal/help/trading_advanced/margin_forex – WebFetch 2026-11-15]`. USD-számlán EURUSD-nél a margin USD-ben: `Lot × 100 000 × EURUSD / 500`.
- **Equity** = Balance + lebegő P&L (+ swap, − jutalék).
- **Szabad margin** = Equity − Used margin.
- **Margin level** = Equity / Used margin × 100% `[forrás: Vantage súgó, WebSearch-összefoglaló 2026-11-15]`.
- **Stop-out:** ha a margin level ≤ SO, a szerver a legnagyobb veszteségű pozíciótól kezdve zár.
  - Vantage UK (FCA, retail): **50%** `[forrás: helpcenter.vantagemarkets.co.uk, WebSearch-összefoglaló; az oldal curl-lel 403-at adott → közvetlenül nem ellenőrzött]`.
  - Vantage STP/ECN számlák 2025-02-09-től: margin call **50%**, stop-out **20%**; a sajtóközlemény lábjegyzete szerint nem vonatkozik az UK és AU ügyfelekre `[forrás: PR Newswire közlemény (pl. https://www.prnewswire.com/no/pressemeldinger/vantage-forbedrer-handelsmiljoet-med-margin-call-og-stop-out-justeringer-302377570.html), WebSearch-összefoglaló; a lábjegyzet az arab nyelvű változatban – nem ellenőrzött szó szerint]`.
  - ESMA retail CFD-szabály: 50%-os, számlaszintű margin close-out, 30:1 major FX-limit, számlaszintű negatív egyenleg védelem `[forrás: ESMA, https://www.esma.europa.eu/press-news/esma-news/esma-adopts-final-product-intervention-measures-cfds-and-binary-options, curl 200]`.
  - **A saját MT5-számla tényleges SO-értékét a terminálból kell kiolvasni:** `AccountInfoDouble(ACCOUNT_MARGIN_SO_SO)` és `ACCOUNT_MARGIN_SO_MODE` `[következtetett: MQL5-standard]`.

### 1.2 Levezetés: mekkora ellenmozgás viszi el a számlát?

Jelölések:
- E₀: kezdő equity;
- N: nominális kitettség (számla-devizában);
- L_eff = N/E₀: effektív tőkeáttétel;
- λ = 500: a bróker tőkeáttétele;
- M = N/λ: lekötött margin;
- x: relatív ellenmozgás.

Lineáris P&L mellett `E(x) = E₀ − N·x`. A stop-out feltétele E(x) = SO·M, ebből:

```
x_SO = (E₀ − SO·N/λ) / N = 1/L_eff − SO/λ
x_0  = 1/L_eff                  (nulla equity)
```

**Következmény:** λ = 500 mellett az SO/λ tag legfeljebb 0,2 százalékpont. Az, hogy a számla mekkora mozgást bír ki, **szinte csak az effektív tőkeáttételtől** függ, a bróker 1:500-as értékétől alig. Az 1:500 abban veszélyes, hogy *engedi* a nagy L_eff-et, és a stop-out a margin-szabályok miatt csak nagyon későn szól közbe `[következtetett]`.

**Számpélda** `[számított]`. Paraméterek `[feltevés]`:
- E₀ = 10 000 USD;
- EURUSD = 1,1052 (az ECB 2026-11-13-i fixingje);
- 1 lot = 100 000 EUR;
- pipérték 10 USD/lot.

Ebből:
- a margin 221,04 USD/lot;
- a teljes margin-kihasználás 45,24 lot.

| L_eff | Nominális (USD) | Used margin (USD) | Margin level | Mozgás 50% SO-ig | Mozgás 20% SO-ig | Mozgás 0 equityig |
|---|---|---|---|---|---|---|
| 1 | 10 000 | 20 | 50 000% | 99,9% | 99,96% | 100% |
| 5 | 50 000 | 100 | 10 000% | 19,9% | 19,96% | 20% |
| 10 | 100 000 | 200 | 5 000% | 9,9% | 9,96% | 10% |
| 20 | 200 000 | 400 | 2 500% | 4,9% | 4,96% | 5% |
| 30 | 300 000 | 600 | 1 667% | 3,23% | 3,29% | 3,33% |
| 50 | 500 000 | 1 000 | 1 000% | 1,9% | 1,96% | 2% |
| 100 | 1 000 000 | 2 000 | 500% | 0,9% | 0,96% | 1% |
| 200 | 2 000 000 | 4 000 | 250% | 0,4% | 0,46% | 0,5% |
| 500 | 5 000 000 | 10 000 | 100% | 0,1% | 0,16% | 0,2% |

**Pipekben** (EURUSD, 1,1052 mellett 1% ≈ 110,5 pip) `[számított]`:
- L_eff = 100: kb. 100 pip ellenmozgás → stop-out;
- L_eff = 500: kb. 11 pip ellenmozgás → stop-out (50% SO).

**Viszonyítás a napi kockázathoz.** Az EURUSD 99%-os napi historikus VaR-ja 1,54% `[számított, 5. fejezet]`. Ennél a mozgásnál:
- L_eff ≈ 65 fölött egyetlen 1%-os valószínűségű nap is nullázza a számlát;
- 20× effektív tőkeáttételnél egy ilyen nap a tőke kb. 31%-a `[számított: 20 × 1,54%]`.

### 1.3 Arany és indexek (paraméteres képlet)

- **XAUUSD:** ha 1 lot = 100 oz `[feltevés, broker-specifikus, ellenőrizendő a SymbolInfo-ban]`, akkor 1 USD-s ármozgás = 100 USD/lot. Ha a bróker 1:500 helyett alacsonyabb tőkeáttételt ad aranyra vagy indexre, a margin aránylag nő. Ez nem változtat az x_0 = 1/L_eff képleten.
- **Index-CFD:** ugyanez a képlet érvényes, de a hétvégi és éjszakai gap (2. fejezet) nagyobb.

---

## 2. Gap-kockázat

### 2.1 SNB, 2015. január 15.

- **Az esemény** `[forrás: Congressional Research Service IN10230, https://www.everycrsreport.com/reports/IN10230.html, curl 200]`:
  - az SNB előzetes figyelmeztetés nélkül eltörölte az 1,20-as EURCHF-minimumárfolyamot;
  - január 16-ra a frank kb. paritásig erősödött.
- **ECB-fixing** `[számított]`:
  - 2015-01-14: 1,2010;
  - 2015-01-15: 1,0280;
  - változás: **−14,40%** (log: −15,55%). Ez a teljes 1999–2026-os minta legnagyobb napi mozgása az EURCHF-ben.
- **Az intraday mélypont** a fixingnél mélyebb volt. Egy brókeroktató oldal 29–30%-os intraday frankerősödést említ. Ez nem elsődleges forrás → `[nem ellenőrzött]`.
- **FXCM:**
  - közlése szerint a likviditásszolgáltatók az esemény alatt nem árazták az eszközt, ami ügyfél-negatív egyenlegekhez vezetett;
  - a cég 225 millió USD veszteséget jelentett;
  - részvénye a nyitás előtti kereskedésben 88%-ot esett.

  `[forrás: Investing.com/StreetInsider, WebSearch-összefoglaló; a StreetInsider oldal curl-lel 403-at adott → részben ellenőrzött]`.

**Veszteség a számla tőkéjéhez képest a −14,4%-os fixing-mozgásnál** (long EURCHF) `[számított]`:

| L_eff | 1 | 5 | 10 | 20 | 50 | 100 | 500 |
|---|---|---|---|---|---|---|---|
| Veszteség / E₀ | 0,14× | 0,72× | **1,44×** | 2,88× | 7,2× | 14,4× | 72× |

- **Gap esetén a stop-out nem véd.** A szerver az első elérhető áron zár, és az a stop-out szint alatt van.
- **Negatív egyenleg:**
  - negatív egyenleg védelem (NBP) nélkül a veszteség a betét többszöröse lehet;
  - NBP mellett a bróker viseli a különbséget, és ilyenkor a bróker maga is csődközelbe kerülhet (FXCM-precedens).

### 2.2 Más, ECB-adatból mért sokkok `[számított]`

| Esemény | Mozgás (ECB-fixing) |
|---|---|
| EURGBP, 2016-06-23 → 24 (Brexit) | +5,42% (GBP-gyengülés) |
| USDJPY, 2024-08-02 → 05 (jen-carry leépülés) | −4,49%; ez a minta legnagyobb napi USDJPY-esése (log −4,60%) |
| EURJPY, 2024-07-31 → 08-05 | −4,17% |
| EURUSD legnagyobb napi esése (2008-12-19) | log −4,74% |

### 2.3 Hétvégi gap

- A napi ECB-fixingből a hétfői hozam a péntek 14:15 → hétfő 14:15 közötti, 3 naptári napos változás.
- **Mért értékek** `[számított]`:

  | | Átlagos abszolút hozam | 99%-os kvantilis |
  |---|---|---|
  | Hétfő | 0,458% | 1,855% |
  | Többi nap | 0,416% | 1,782% |

- **Értelmezés** `[következtetett]`: a hétvége kb. 10%-kal növeli az átlagos napi mozgást. A valódi hétvégi *gap* (péntek 23:00 zárás → vasárnap 23:00 nyitás) tickadatból mérendő: Dukascopy, illetve a broker MT5-exportja (a1 ágens).
- **A gap valódi veszélye a ritka, rendkívüli hétvégi eseményekből jön:** választás, jegybanki hétvégi döntés, geopolitika. Ezek a napi átlagban alig látszanak.
- **Szabály a gridhez** `[következtetett]`: péntek zárás előtt a nettó kitettséget le kell vinni. Feltétel:

  `L_eff × (hétvégi 99,9%-os gap) < 20–30% E₀`.

---

## 3. Grid és martingale csődvalószínűség

### 3.1 Az aritmetikus grid zárt alakja

**Modell:** long grid.
- Vétel P₀ alatt Δ-nként, a j-edik szinten (j = 1..k), q lottal.
- TP = Δ (a j-edik pozíció a (j−1)-edik szinten zár).
- Az ár a P₀ − x·Δ ponton van (x ≥ 0), k = ⌊x⌋ nyitott pozíció.

**Lebegő veszteség és margin** (pipérték v = 10 USD/lot, s = spread pipben):

```
L(x) = q·v·Δ·( k·x − k(k+1)/2 ) + k·q·v·s
M(x) = k·q·ContractSize·P/λ
```

A ruin-távolság x* az E₀ − L(x*) = SO·M(x*) egyenlet legkisebb megoldása.

- A veszteség **x-ben kvadratikus** (≈ q·v·Δ·x²/2), a margin lineáris.
- A gridet **nem a margin, hanem a lebegő veszteség** viszi el.
- Ezért szinte közömbös, hogy a stop-out 20% vagy 50% (lásd a táblázatot).

**Ruin-valószínűség adott horizonton.** Feltevés: driftmentes GBM log-áron, σ éves volatilitással. A reflexiós elv szerint:

```
P( min_{t≤T} ln(P_t/P₀) ≤ −d ) = 2·(1 − Φ( d / (σ√T) ))
```

ahol d = x*·Δ/P₀.

- σ = 6,63% = az EURUSD realizált éves volatilitása az utolsó 3 évben `[számított ECB-adatból]`.
- Teljes 1999–2026-os mintán σ = 9,21% `[számított]`.

**Paraméterek** `[feltevés]`:
- E₀ = 10 000 USD;
- EURUSD;
- spread 1 pip;
- korlátlan szintszám.

Eredmények `[számított]`:

| Lot/szint | Δ (pip) | SO | Szintek a stop-outig | Ellenmozgás (pip) | Ellenmozgás (%) | P(ruin) 1 hó | 3 hó | 1 év | 3 év |
|---|---|---|---|---|---|---|---|---|---|
| 0,01 | 20 | 50% | 99 | 1 998 | 18,1% | ≈0 | ≈0 | 0,6% | 11,6% |
| 0,01 | 10 | 50% | 140 | 1 407 | 12,7% | ≈0 | 0,01% | 5,5% | 26,8% |
| 0,05 | 20 | 50% | 44 | 893 | 8,1% | 0,002% | 1,5% | 22,3% | 48,2% |
| 0,05 | 20 | 20% | 44 | 899 | 8,1% | 0,002% | 1,4% | 22,0% | 47,9% |
| 0,10 | 20 | 50% | 31 | 631 | 5,7% | 0,29% | 8,5% | 39,0% | 61,9% |
| 0,10 | 50 | 50% | 20 | 1 013 | 9,2% | ≈0 | 0,6% | 16,7% | 42,5% |
| 0,20 | 30 | 50% | 18 | 551 | 5,0% | 0,93% | 13,3% | 45,2% | 66,4% |

**Olvasat** `[következtetett]`:
- (i) Kétszer sűrűbb grid ugyanazzal a lottal kb. kétszer akkora kitettséget jelent ugyanazon távolságon, így a ruin-távolság √2-vel csökken (20→10 pip: 18,1% → 12,7%).
- (ii) A ruin-valószínűség a horizonttal monoton nő, és hosszú távon 1-hez tart. A grid tehát **nem „ha”, hanem „mikor”** kérdés, hacsak nincs valódi mean-reversion edge vagy kemény kosár-stop.
- (iii) A **TSMOM-irodalom** (Moskowitz–Ooi–Pedersen 2012, https://doi.org/10.1016/j.jfineco.2011.11.003) szerint a trendek 1–12 hónapon perzisztensek, vagyis pozitív drift van az ellenmozgás irányában. Ez a valós ruin-valószínűséget a driftmentes becslésnél *nagyobbá* teszi.

### 3.2 Diszkrét gambler's ruin (Δ-lépéses véletlen bolyongás)

Annak valószínűsége, hogy a bolyongás előbb lép k szintet lefelé, mint m szintet felfelé (p = felfelé lépés valószínűsége):

```
p = 1/2:   P_ruin = m/(k+m)
p ≠ 1/2:   P_ruin = (r^k − r^(k+m)) / (1 − r^(k+m)),   r = (1−p)/p
```

Eredmények `[számított]`:

| Feltétel | P_ruin |
|---|---|
| k = 20, m = 1, p = 0,50 | 4,76% egy ciklusra |
| k = 20, m = 1, p = 0,49 (1%-os ellen-drift) | 6,90% |
| k = 40, m = 1 | 2,44% |
| k = 10, m = 1 | 9,09% |

**Ciklusok sorozata:** n független ciklusban P(túlélés) = (1 − P_ruin)ⁿ. Például k = 20, p = 0,5 mellett 100 ciklus után a túlélés 0,9524¹⁰⁰ ≈ 0,76% `[számított]`. Vagyis kb. 21 nyerő ciklusra jut egy teljes veszteség. A nettó várható érték fair játékban 0, költséggel negatív.

### 3.3 Monte Carlo: kétirányú grid realizált TP-vel, spreaddel, swappal, vastag farokkal

**Modell** `[feltevés]`:
- óránkénti lépés, 1 év = 6 048 óra;
- Student-t(4) innovációk, egységnyi varianciára skálázva;
- σ = 6,63%/év;
- kétirányú, fix szintű grid: long P₀ alatt, short P₀ fölött;
- TP = Δ;
- spread 1 pip nyitásonként;
- swap −0,5 pip/lot/éjszaka minden nyitott pozícióra;
- stop-out ellenőrzése minden órában;
- 4 000 pálya (3 évnél 2 000);
- seed = 42.

Eredmények `[számított]`:

| Konfiguráció | Esemény | P(esemény) | Medián idő az eseményig | Medián végső equity (túlélők) | **Várható hozam (minden pálya)** |
|---|---|---|---|---|---|
| 0,01 lot, Δ = 20, SO 50% | stop-out | 1,6% | 10,0 hó | 9 972 USD | **−8,1%** |
| 0,05 lot, Δ = 20, SO 50% | stop-out | 38,8% | 7,0 hó | 11 502 USD | **−35,2%** |
| 0,10 lot, Δ = 20, SO 50% | stop-out | 62,8% | 5,3 hó | 14 451 USD | **−50,1%** |
| 0,10 lot, Δ = 20, SO 20% | stop-out | 61,4% | 5,3 hó | 14 449 USD | **−49,7%** (átlagos equity a stop-outnál: −106 USD → negatív egyenleg) |
| 0,05 lot, Δ = 10, SO 50% | stop-out | 67,6% | 5,2 hó | 12 267 USD | **−62,9%** |
| 0,05 lot, Δ = 20, max 10 szint, kosár-stop −20% | kosár-stop | 90,2% (legalább egyszer) | 4,1 hó | 11 862 USD | **−10,5%** |
| 0,05 lot, Δ = 20, σ × 1,5 = 9,95% | stop-out | 67,0% | 5,0 hó | 14 261 USD | **−57,2%** |
| 0,05 lot, Δ = 20, 3 év | stop-out | 76,8% | 12,9 hó | 16 120 USD | **−65,0%** |

**Kulcsmegfigyelések** `[számított + következtetett]`:

1. **Túlélési torzítás.** A ≥ 0,05 lotos konfigurációkban a túlélők medián equity-je +15–45% (1 év), illetve +61% (3 év). A *minden pályára* vett várható hozam viszont −8% és −65% között van. Az MQL5 Market és a myfxbook „sikeres grid” görbéi a túlélő ágat mutatják.
2. **A 20% vs. 50% stop-out szinte közömbös** (62,8% vs. 61,4%). Az alacsonyabb SO-nál viszont a diszkrét óránkénti árfolyamon és vastag farkon az **átlagos equity a stop-outnál negatív** (−106 USD) → NBP nélkül adósság.
3. **A kosár-stop a ruint kisebb, gyakori veszteségekre cseréli:** 90% eséllyel legalább egyszer elveszít ~14%-ot (átlagos equity az eseménynél 8 639 USD). A várható érték így is negatív (−10,5%), de nincs teljes csőd. **A grid stop nélkül nem „biztonságos”, csak a veszteségeloszlást tolja a farokba.**
4. **Vol-rezsim:** 1,5× volatilitásnál a ruin 38,8% → 67,0%. Ezért kötelező a vol-alapú lot-skálázás (strat-regime-garch-vol-filter, strat-sizing-vol-targeting).

**A modell korlátai** `[következtetett]`:
- nincs benne valódi mean-reversion edge (driftmentes);
- az órás felbontás a szintátlépéseket és a stop-outot közelíti;
- a swap egyetlen átlagos értékkel szerepel;
- nincs hétvégi gap;
- nincs spread-tágulás rolloverkor.

A valódi EA-paraméterekkel és a Vantage-szimbólumspecifikációval (a1 ágens) újra kell futtatni. A kód a függelékben van.

### 3.4 Martingale – zárt alak és diszkrét DP

**Duplázás.** Az alaptét q₀, TP = SL = s pip. A k-adik veszteség után:
- a lot q₀·2ᵏ;
- a kumulált veszteség q₀·v·s·(2ᵏ − 1).

**Paraméterek** `[feltevés]`:
- E₀ = 10 000 USD;
- q₀ = 0,01 lot;
- s = 20 pip;
- 1:500, EURUSD 1,1052.

Megnyithatóság `[számított]`:

| k | Lot | Kumulált veszteség előtte | Margin | Megnyitható? (equity ≥ 0,5·margin + a lépés SL-je) |
|---|---|---|---|---|
| 0 | 0,01 | 0 | 2,2 | igen |
| 5 | 0,32 | 62 | 70,7 | igen |
| 8 | 2,56 | 510 | 565,9 | igen |
| 10 | 10,24 | 2 046 | 2 263 | igen |
| 11 | 20,48 | 4 094 | 4 527 | **nem** |

Tehát **K_max = 11** egymás utáni veszteség a csőd, amikor a következő lépés már nem nyitható.

**Nyerési valószínűség spreaddel.** 1 pip spread mellett a TP 21, az SL 19 pip távolságra van. Driftmentes bolyongásnál p_win = 19/40 = 0,475, p_loss = 0,525 `[számított]`.

**P(legalább egy ≥ 11 hosszú vesztes sorozat n trade alatt)**, pontos dinamikus programozással `[számított]`:

| n trade | 100 | 500 | 1 000 | 2 000 | 5 000 |
|---|---|---|---|---|---|
| P(csőd) | 3,6% | 17,8% | 32,6% | 54,8% | 86,3% |

**Várható érték** `[következtetett]`:
- egy ciklus (első nyerésig) várható nyeresége fair játékban pontosan 0;
- spreaddel negatív;
- a martingale csak az eloszlást torzítja: P(ciklus nyer) ≈ 1 − 0,525¹¹ ≈ 99,92%, de a vesztes ciklus −4 094 USD.

**Lágy martingale (1 < r < 2):**
- a kumulált veszteség geometriai sor: q₀·v·s·(rᵏ − 1)/(r − 1);
- ugyanazon tőkéből több lépést enged;
- a breakeven viszont lassabban jön vissza (strat-martingale-soft).

---

## 4. A Kelly-túlméretezés görbéje

### 4.1 Folytonos eset

**Növekedés.** Log-normális hozamokra, f tőkeáttétellel:

```
g(f) = r + f(μ−r) − f²σ²/2
f*   = (μ−r)/σ²
g(f)−r = (μ−r)²/σ² · (c − c²/2),   c = f/f*
```

Relatív növekedés: `G(c) = 2c − c²` (G(1) = 1).

**Elérési valószínűség.** Annak valószínűsége, hogy a vagyon valaha a kiinduló érték α-szorosára esik (GBM, elérési valószínűség):

```
P = α^(2/c − 1)    (c < 2)
```

Levezetés: a log-vagyon driftje m = k(c − c²/2), a szórása s = c·√k, ahol k = (μ−r)²/σ². Ebből P = exp(2m·ln α / s²), és 2m/s² = 2/c − 1 `[következtetett, levezetés]`.

| c = f/f* | 0,25 | 0,5 | 0,75 | 1 (Kelly) | 1,5 | 2 | 2,5 | 3 |
|---|---|---|---|---|---|---|---|---|
| Növekedés a Kelly %-ában | 43,8% | 75% | 93,8% | 100% | 75% | **0%** | −125% | −300% |
| P(valaha a kezdő tőke 50%-ára esik) | 0,8% | 12,5% | 31,5% | 50% | 79,4% | 100% | 100% | 100% |
| P(valaha a kezdő tőke 10%-ára esik) | 10⁻⁷ | 0,1% | 2,2% | 10% | 46,4% | 100% | 100% | 100% |

`[számított]`.

**MC-ellenőrzés** `[számított]`: μ = 10%, σ = 20%, 200 év, 2 000 pálya; a vagyon valaha a kezdő tőke 50%-a alá esik:

| | MC | Képlet |
|---|---|---|
| c = 1 | 52,5% | 50% |
| c = 0,5 | 13,1% | 12,5% |

**Tanulság** `[következtetett]`:
- 2× Kelly fölött a hosszú távú növekedés negatív, és a csőd biztos.
- A μ becslési hibája miatt (a Sharpe-hiba ≈ √(1/T) évente) a „becsült Kelly” könnyen 2× fölé esik.
- **Gyakorlati alapérték: ¼–½ Kelly.**

Forrás: Kelly 1956 (https://doi.org/10.1002/j.1538-7305.1956.tb03809.x); MacLean–Thorp–Ziemba 2011 (https://doi.org/10.1142/9789814293501_0039) — DOI ellenőrizve.

### 4.2 Diszkrét (bináris) eset

**Képlet:** `g(f) = p·ln(1+bf) + (1−p)·ln(1−f)`, `f* = (bp − q)/b`.

**Példa:** p = 0,55, b = 1 (egyenlő odds) → f* = 0,10 `[számított]`.

| f | 0,025 | 0,05 | 0,10 | 0,15 | 0,20 | 0,25 | 0,30 |
|---|---|---|---|---|---|---|---|
| g / tét (log) | 0,00219 | 0,00375 | **0,00501** | 0,00374 | **−0,00014** | −0,00673 | −0,01620 |

**Az MT5-ön az 1:500 miatt a „tét” az effektív tőkeáttétel** `[következtetett]`. Ha egy stratégia valódi Sharpe-ja 1 és vol-ja 10%, akkor f* = μ/σ² = 0,10/0,01 = 10× effektív tőkeáttétel. A 20× fölé menő méretezés tehát még pozitív edge mellett is negatív növekedést ad. A grid lebegő kitettsége ezt rendszeresen túllépi.

---

## 5. Drawdown-eloszlások, VaR, CVaR, EVT

### 5.1 Maximális drawdown eloszlása (MC)

**Modell:** GBM, éves vol 20%, adott Sharpe, 5 000 pálya `[feltevés + számított]`.

| Sharpe | Horizont | MDD medián | MDD 90% | MDD 99% |
|---|---|---|---|---|
| 0 | 1 év | 20,1% | 32,4% | 43,1% |
| 0 | 5 év | 42,2% | 60,7% | 73,7% |
| 0,5 | 1 év | 17,0% | 27,7% | 38,7% |
| 0,5 | 5 év | 31,2% | 47,4% | 62,1% |
| 1,0 | 1 év | 14,7% | 24,1% | 34,5% |
| 1,0 | 5 év | 24,9% | 36,5% | 49,0% |
| 2,0 | 1 év | 11,7% | 18,2% | 26,2% |
| 2,0 | 5 év | 17,9% | 25,3% | 33,0% |

**Felhasználás** `[következtetett]`:
- **Kill-switch kalibrálás:** ha a stratégia állított Sharpe-ja 1 és vol-ja 20%, akkor az 5 éves 99%-os MDD kb. 49%. Az ennél nagyobb élő drawdown statisztikai bizonyíték arra, hogy a valós Sharpe alacsonyabb.
- **Képlet-alap:** Brown-mozgás MDD-jére Magdon-Ismail et al. (2004) ad elméleti eredményt (https://doi.org/10.1239/jap/1077134674, DOI ellenőrizve).

### 5.2 Napi VaR / CVaR / EVT valós devizaadaton

**Adat:** ECB 1999–2026, n = 7 135 napi log-hozam; veszteség = −hozam (long pozíció).

**Módszerek** `[számított]`:
- **Normális:** μ, σ.
- **Historikus:** empirikus kvantilis, CVaR = feltételes átlag.
- **Student-t:** ML-illesztés.
- **EVT (POT):** küszöb u = 95. percentilis, GPD (ξ, β) ML-lel, loc = 0. A VaR és az ES a McNeil–Frey-képlettel (https://doi.org/10.1016/S0927-5398(00)00012-8, DOI ellenőrizve):

  ```
  VaR_α = u + β/ξ·[ (n/N_u·(1−α))^(−ξ) − 1 ]
  ES_α  = (VaR_α + β − ξu)/(1−ξ)
  ```

Napi veszteség, % `[számított]`:

| Pár | Normális VaR 99% | Hist. VaR 99% | Hist. CVaR 99% | t VaR 99% | EVT VaR 99% | EVT ES 99% | EVT VaR 99,9% | EVT ES 99,9% | Max. napi veszteség (dátum) | GPD ξ | Többlet-kurtózis | t df |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| EURUSD | 1,35 | 1,54 | 1,92 | 1,54 | 1,51 | 1,92 | 2,47 | 2,95 | 4,74 (2008-12-19) | 0,07 | 3,3 | 4,7 |
| USDJPY | 1,44 | 1,80 | 2,36 | 1,68 | 1,76 | 2,37 | 3,19 | 4,00 | 4,60 (2024-08-05) | 0,13 | 4,1 | 3,8 |
| EURCHF | 0,93 | 1,00 | 1,64 | 1,22 | 1,00 | 1,57 | 2,32 | 3,49 | **15,55 (2015-01-15)** | 0,31 | **359** | 2,0 |
| EURGBP | 1,11 | 1,22 | 1,59 | 1,97 | 1,21 | 1,58 | 2,08 | 2,58 | 2,97 (2019-10-11) | 0,12 | 5,8 | 2,1 |

**Olvasat** `[következtetett]`:
- (i) A normális VaR minden páron alulbecsül.
- (ii) **EURCHF:** még az EVT 99,9%-os ES (3,5%) is a valós SNB-mozgás (15,6%) negyede. Peggelt vagy floorral védett rezsimben a múltbeli eloszlás nem mondja meg az eltörlés kockázatát (rezsim- vagy politikai kockázat). Ezt **stresszforgatókönyvként** kell kezelni, nem statisztikaként.
- (iii) **Tőkeáttétellel szorozva:** 20× effektív tőkeáttétel mellett az EURUSD 99,9%-os EVT ES-e 59% E₀/nap.
- (iv) A t-eloszlás df ≈ 2–5 → a variancia alig véges (vastag farok).

### 5.3 Stresszforgatókönyvek (M10)

**Forrásként** a fenti ECB-mért mozgások szolgálnak: 2015 CHF; 2016 GBP; 2024 aug. JPY; 2008 dec. EURUSD.

**Követelmény a gridhez:** a nyitott kitettségnek (a lebegő plusz a még nyitható szintekkel együtt) túl kell élnie egy ilyen napi mozgást, úgy hogy a margin level a stop-out fölött marad.

**Képlet:**

```
L_eff,max = (1 − SO/λ·L_eff) / x_stressz  ≈  1/x_stressz
```

Ez a 4,5%-os JPY-mozgásra L_eff ≤ 22, a 14,4%-os CHF-sokkra L_eff ≤ 6,9 `[számított]`.

---

## 6. Brókeroldali kockázatok

### 6.1 Spread-tágulás rolloverkor és híreknél

- **Szerveridő és rollover:**
  - egy harmadik féltől származó Vantage-költségútmutató szerint a swap a 22:00-s szerveridő után tartott pozíciókra jár;
  - a szerveridő GMT+2, nyáron GMT+3;
  - ez nem elsődleges forrás → `[nem ellenőrzött]`.
- **Triple swap szerdán:** ipari konvenció, mert a FX T+2-es elszámolása a hétvégét szerdára hozza. A tényleges napot az MT5 szimbólumspecifikáció „Swap 3-days” mezője mutatja `[forrás: több brókersúgó, WebSearch 2026-11-15]`.
- **A rollover körüli spread-tágulás mértékére nem találtunk megbízható, brókerfüggetlen forrást** `[nem ellenőrzött]`.
- **Mérési utasítás:**
  - a saját MT5-számla tickadatából (CopyTicks) percenként rögzíteni a spread medián- és 99%-os értékét;
  - különösen a rollover ±1 órás ablakában és makrobejelentések ±5 percében.
- **Grid-szabály** `[következtetett]`:
  - a ±1 órás ablakban nem nyitunk szintet;
  - a TP-t és az SL-t ask/bid oldalon számoljuk, nem mid alapján;
  - a stop-out távolságot a 99%-os spreaddel csökkentjük.

### 6.2 Negatív egyenleg védelem (NBP) jogalanyonként

| Jogalany (Vantage) | Szabályozó | NBP | Max. retail tőkeáttétel FX | Forrás/címke |
|---|---|---|---|---|
| Vantage Global Prime LLP | FCA (UK) | igen (retail, számlaszintű) | 30:1 (ESMA/FCA-szabály) | FCA/ESMA-szabály `[forrás: ESMA, curl 200]`; jogalany-hozzárendelés: review-oldalak `[nem ellenőrzött]` |
| Vantage Global Prime Pty Ltd | ASIC (AU) | igen (retail) | 30:1 (ASIC retail CFD-szabály) | review-oldalak `[nem ellenőrzött]` |
| Nemzetközi jogalany (VFSC, Vanuatu; a források a nevet eltérően adják meg: „Vantage Global Limited” / „Vantage International Group”, licencszám 700271) | VFSC | „best effort” vagy nem garantált a források szerint | ezt a jogalanyt kötik az 1:500-hoz (következtetett) | review-oldalak, WebSearch-összefoglaló `[nem ellenőrzött; az elsődleges forrás az ügyfélszerződés (Client Agreement)]` |

- **Következmény** `[következtetett]`: az 1:500 szinte biztosan offshore jogalanyt jelent, ahol az NBP nem jogi garancia. A 2.1 fejezet szerinti gap után a negatív egyenleg **behajtható követelés** lehet.
- **A pontos ÁSZF-ellenőrzés az a8 ágens feladata** (M10 jogi rész).

### 6.3 Egyéb partnerkockázatok (röviden, számokkal, ahol van)

- **Likviditásszolgáltatói kiesés.** Az FXCM-eset alatt a likviditásszolgáltatók nem áraztak `[forrás, 2.1]`.
  - B-book brókernél a bróker az ügyfél ellenfele;
  - A-booknál a bróker likviditás-továbbadó.

  Mindkét esetben a gap a kliensen csapódik le, NBP nélkül.
- **Tőkeáttétel-korlát hatása:** a CFTC 2010-ben az amerikai retail FX-tőkeáttételt 50:1-re korlátozta. Heimer–Simsek (2019) szerint ez a legagresszívebb kereskedőknél kisebb veszteséget eredményezett, a piaci likviditás romlása nélkül `[forrás: NBER w24176, https://www.nber.org/papers/w24176, WebSearch-összefoglaló]`.
- **Számla- és profit-visszavonás** latency-arbitrázs vagy „abuse” címén: a brókerek ÁSZF-je általában fenntartja ezt a jogot (a8-ellenőrzés, `[nem ellenőrzött]` itt).

---

## 7. Összefoglaló kulcsszámok (a többi ágens és a fő dokumentum számára)

| # | Állítás | Érték | Címke |
|---|---|---|---|
| 1 | Ellenmozgás a nulla equityig 1:500 teljes kihasználásnál | 0,20% (≈22 pip EURUSD) | számított |
| 2 | Ellenmozgás 50% / 20% stop-outig, teljes kihasználásnál | 0,10% / 0,16% | számított |
| 3 | Ellenmozgás a nulla equityig L_eff = 20 / 50 / 100 mellett | 5% / 2% / 1% | számított |
| 4 | SNB 2015, EURCHF napi változás (ECB-fixing) | −14,4% | számított (ECB-adat) |
| 5 | Grid 0,05 lot/20 pip/10k USD: P(stop-out) 1 év / 3 év (MC) | 38,8% / 76,8% | számított |
| 6 | Ugyanez: várható hozam minden pályán, 1 év | −35% | számított |
| 7 | Martingale 0,01 lot/20 pip/10k USD: P(csőd) 1 000 trade alatt | 32,6% | számított |
| 8 | 2× Kelly növekedése | 0 (fölötte negatív) | számított |
| 9 | ½ Kelly: P(valaha a kezdő tőke 50%-ára esik) | 12,5% | számított |
| 10 | EURUSD napi 99% VaR / 99,9% EVT ES | 1,54% / 2,95% | számított |
| 11 | Ajánlott max L_eff a JPY-2024 / CHF-2015 stresszre | ≤22 / ≤6,9 | számított |
| 12 | Vantage stop-out: UK retail / STP-ECN (nem UK/AU) | 50% / 20% | forrás (WebSearch) |

---

## Függelék A – A számítások kódja (kivonat, reprodukálható)

```python
import numpy as np, pandas as pd
from scipy import stats
# Adat: ECB EXR, pl. https://data-api.ecb.europa.eu/service/data/EXR/D.USD.EUR.SP00.A?format=csvdata
def move_to_stopout(L_eff, SO, lev=500):          # 1.2
    return 1/L_eff - SO/lev
def grid_kstar(E0, q, delta_pips, SO, P, lev=500, pipv=10, cs=100_000, spread=1.0):  # 3.1
    xs = np.arange(0, 5000, 0.001); k = np.floor(xs)
    eq = E0 - (k*xs - k*(k+1)/2)*delta_pips*q*pipv - k*spread*q*pipv
    mg = k*q*cs*P/lev
    i = np.where((k > 0) & (eq <= SO*mg))[0][0]; return int(k[i]), xs[i]*delta_pips
def p_ruin_reflection(d_rel, sigma, T):            # 3.1
    return 2*(1 - stats.norm.cdf(d_rel/(sigma*np.sqrt(T))))
def p_run(n, K, p_loss):                           # 3.4: P(legalább egy >=K hosszú vesztes sorozat)
    st = np.zeros(K); st[0] = 1; hit = 0
    for _ in range(n):
        new = np.zeros(K); new[0] = st.sum()*(1-p_loss); new[1:] = st[:-1]*p_loss
        hit += st[-1]*p_loss; st = new
    return hit
def kelly_table(c): return 2*c - c**2, 0.5**(2/c - 1)  # 4.1: rel. növekedés, P(50%-ra esés)
def evt_var_es(loss, a, q_u=0.95):                 # 5.2 POT-GPD
    u = np.quantile(loss, q_u); exc = loss[loss > u] - u
    xi, _, beta = stats.genpareto.fit(exc, floc=0); n, nu = len(loss), len(exc)
    var = u + beta/xi*((n/nu*(1-a))**(-xi) - 1); es = (var + beta - xi*u)/(1 - xi); return var, es
# MC grid (3.3): óránkénti t(4)-innovációk, kétirányú grid, nL/nS állapot:
#   vétel: n = max(n, floor(x)); zárás: n = min(n, ceil(x)); realizált += eladások*Δ*pipv − vételek*spread*pipv
#   lebegő = −(n*x − n(n+1)/2)*Δ*pipv ; stop-out ha equity <= SO*margin
```

A teljes MC-kód (≈100 sor) a fenti logikát vektorizálja 4 000 pályára (seed = 42); futásidő néhány perc.

## Függelék B – Hivatkozások (ellenőrzés módja)

- **Kelly (1956)** https://doi.org/10.1002/j.1538-7305.1956.tb03809.x – Crossref DOI ellenőrizve.
- **MacLean–Thorp–Ziemba (2011)** https://doi.org/10.1142/9789814293501_0039 – Crossref.
- **Moskowitz–Ooi–Pedersen (2012)** https://doi.org/10.1016/j.jfineco.2011.11.003 – Crossref.
- **McNeil–Frey (2000)** https://doi.org/10.1016/S0927-5398(00)00012-8 – Crossref.
- **Artzner–Delbaen–Eber–Heath (1999), Coherent Measures of Risk** https://doi.org/10.1111/1467-9965.00068 – Crossref.
- **Magdon-Ismail–Atiya–Pratap–Abu-Mostafa (2004)** https://doi.org/10.1239/jap/1077134674 – Crossref.
- **Chague–De-Losso–Giovannetti (2019)** https://doi.org/10.2139/ssrn.3423101 – Crossref + absztrakt.
- **Heimer–Simsek (2019)** https://www.nber.org/papers/w24176 – curl 200 + WebSearch.
- **Dynamic Grid Trading (2025)** https://arxiv.org/abs/2506.11921 – arXiv API + absztrakt: egyszerű feltevések mellett a hagyományos grid várható hozama ≈ 0.
- **ESMA CFD-intervenció (2018)** https://www.esma.europa.eu/press-news/esma-news/esma-adopts-final-product-intervention-measures-cfds-and-binary-options – curl 200.
- **CRS IN10230 (SNB 2015)** https://www.everycrsreport.com/reports/IN10230.html – curl 200.
- **MT5 margin-képletek** https://www.metatrader5.com/en/terminal/help/trading_advanced/margin_forex – WebFetch.
- **Vantage stop-out (UK súgó)** https://helpcenter.vantagemarkets.co.uk/hc/en-gb/articles/11933242268303 – curl 403, tartalom csak WebSearch-összefoglalóból → részben ellenőrzött.
