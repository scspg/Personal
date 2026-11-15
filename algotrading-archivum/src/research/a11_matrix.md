# A11 – Platform- és bróker-összehasonlítás: van-e jobb az MT5/Vantage-nél? (magyar lakos, AI-vezérelt aktív automatizált kereskedés)

Ellenőrzés: 2026-11-15. Tételek: `a11_platforms.jsonl`, 73 db (26 platform, 31 bróker, 16 pro-status; 48 mért, 20 becsült, 5 nem ellenőrzött).
Források: brókeroldalak láblécei és díjoldalai (curl/WebFetch), az ESMA MiFID-register Solr API-ja (`registers.esma.europa.eu/solr/esma_registers_upreg`, LEI alapján), a GLEIF API, a 2026-os magyar DTT-lista PDF-je (kozbeszerzes.hu), PyPI és ungh.cc. Az A1 és az A8 tényeire hivatkozom, nem ismétlem őket.
**Pontszámok:** 0–10, saját becslés (becsült) a mért tényekből. Súlyok: automatizálás/API 20, költség 15, végrehajtási bizonyíték 15, szabályozás 15, magyar adó 10, tőkeáttétel 10, eszközök 10, adat 5. Ez nem jogi vagy adótanács.

## 1. Fő megállapítás

- **Van jobb, és nem is egy.** A 31 brókerjogalany közül a jelenlegi Vantage-számla a **28. (4,95 pont)**. Összesen három sor kerül mögé: az Exness (SC), az SVG-s AxiTrader és az XM Global. Egyetlen kritériumban vezet: a tőkeáttételben (1:500).
- **Vantage-jogalany (javítva, 2026-11-15).** A Vantage Help Center (frissítve 2026-11-05) a VIG Group (Mauritius FSC GB20026165), az FSCA 51268 és az ASIC 428901 jogalanyt sorolja fel, VFSC-t és CIMA-t már nem. A VFSC 700271 egy régebbi elsődleges PDF-ből származik, ezért történeti adat. A mérvadó forrás az ügyfél saját Client Agreementje. Mauritius nincs a magyar DTT-listán, így a mauritiusi számla nem ETÜ; Dél-Afrika rajta van, ezért FSCA-s számlánál csak a 67/A bb) és bc) feltételt kell még ellenőrizni.
- Az 1:500-as tőkeáttétel **legálisan, EU-s felügyelet mellett is elérhető** elective professional státusszal (mért): Pepperstone EU, FP Markets EU és Tickmill Europe 1:500; Axi EU 1:400; OANDA TMS 1:200.
  - **Feltétel: a háromból kettő** (MiFID II II. melléklet II.1. pont; ESMA Interactive Single Rulebook: https://www.esma.europa.eu/publications-and-data/interactive-single-rulebook/mifid-ii/annex-ii; brókeroldali megfogalmazás pl. https://www.icmarkets.eu/en/trading-accounts/professional-clients, mindkettő HTTP 200, 2026-11-15): (1) az elmúlt 4 negyedévben negyedévente átlagosan legalább 10 jelentős méretű ügylet a releváns piacon; (2) 500 000 EUR feletti pénzügyi portfólió (készpénzbetéttel együtt); (3) legalább 1 év munka a pénzügyi szektorban olyan pozícióban, amely a tervezett ügyletek ismeretét igényli. **A legtöbb retail kereskedő csak az (1)-et tudja teljesíteni**, így 1:500 EU-s felügyelet mellett csak akkor érhető el, ha a (2) vagy a (3) is teljesül. Egyébként az EU-s út 1:30 (major FX). **Józan méretezéshez pro státusz nem kell:** a legfeljebb 10× hatásos tőkeáttétel belefér a 30:1-es lakossági keretbe (major FX), az 1:500 csak a margin-igényt csökkenti, nem a javasolt kitettséget. A Bszt. 49. § (1) a magyar befektetési vállalkozásokra vonatkozik (a) pont: negyedévente átlagosan legalább 10, egyenként 40 000 EUR értékű ügylet, vagy évente összesen 400 000 EUR; mért, net.jogtar.hu); a CySEC-jogalanyok (Pepperstone EU, FP Markets EU stb.) a ciprusi átültetést és saját „jelentős méret” definíciójukat alkalmazzák (pl. FP Markets: 1 lot, mért).
- Az EU-s brókernél kötött ügylet valószínűleg ETÜ: 15% adó, veszteség-kiegyenlítéssel: a t. évi veszteség a t−2…t+2 évek ETÜ-adójával szemben érvényesíthető (összesen öt adóév, a t., t+1. vagy t+2. évi bevallásban), egy adott bevallásban legfeljebb a tárgyév és az azt megelőző két év ETÜ-adójáig (Szja 67/A (6)–(8), mért, net.jogtar.hu). Az offshore ügylet nem ETÜ, ≈24,9% teher (A8, becsült).
- A Vantage nem szerepel az ESMA MiFID-registerben (mért). Az offshore szabályozók (Vanuatu, Seychelles, Bahama, SVG, Mauritius) államai nincsenek rajta a 2026-os magyar DTT-listán (mért).
- Ha a megrendelő offshore marad, az IC Markets Global (Raw Trading, FSA SD018) is jobb a Vantage-nél (6,25 pont): olcsóbb, jobb a végrehajtási reputációja, és ugyanúgy MT5/cTrader.

## 2. Bróker-mátrix (HU-lakosra vonatkozó entitás)

| # | Bróker (entitás) | Auto | Költs. | Végr.* | Szab. | Adó | Tőkeátt. | Eszk. | Adat | Súlyozott | ETÜ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | IBKR Ireland (CBI) | 9 | 9 | 8 | 9.5 | 9.5 | 5 | 10 | 8 | **8.62** | igen |
| 2 | LMAX Broker Europe (CySEC, csak pro) | 9 | 8 | 10 | 8 | 9 | 7 | 5 | 7 | **8.15** | igen |
| 3 | Pepperstone EU (CySEC 388/20) | 8 | 7.5 | 7 | 8.5 | 9 | 7 | 7 | 5 | **7.60** | igen |
| 4 | Darwinex (CNMV/FCA) | 9 | 8 | 7 | 8 | 8.5 | 6 | 6 | 6 | **7.60** | igen |
| 5 | IC Markets EU (CySEC 362/18) | 8 | 8 | 7 | 8 | 9 | 6 | 6 | 5 | **7.40** | igen |
| 6 | FP Markets EU (CySEC 371/18) | 8 | 8 | 6 | 8 | 9 | 7 | 6 | 5 | **7.35** | igen |
| 7 | Dukascopy Europe (Latvijas Banka) | 8.5 | 6 | 7.5 | 8.5 | 9 | 4 | 6 | 9 | **7.35** | igen |
| 8 | Dukascopy Bank (FINMA) | 8.5 | 6 | 7.5 | 9 | 7 | 5 | 6 | 9 | **7.33** | ? |
| 9 | Tickmill Europe (CySEC 278/15) | 7 | 8.5 | 6 | 8 | 9 | 7.5 | 6 | 5 | **7.28** | igen |
| 10 | Saxo Bank (DK) | 6.5 | 5 | 7 | 9.5 | 9 | 5 | 10 | 7 | **7.28** | igen |
| 11 | IG Europe (BaFin) | 7 | 5 | 6.5 | 9 | 9 | 5 | 9 | 6 | **7.08** | igen |
| 12 | OANDA TMS (KNF) | 6 | 6 | 6 | 8 | 9 | 6 | 6 | 7 | **6.65** | igen |
| 13 | Swissquote Europe (CSSF, FX csak pro) | 5 | 5 | 6 | 9.5 | 9 | 6 | 8 | 5 | **6.62** | igen |
| 14 | Admirals Europe (CySEC 201/13) | 6 | 6 | 5 | 8 | 9 | 5 | 7 | 5 | **6.40** | igen |
| 15 | Swissquote CH (FINMA) | 5 | 5 | 6 | 9.5 | 7 | 5 | 8 | 5 | **6.33** | ? |
| 16 | FXCM/Stratos Europe (CySEC) | 7 | 5 | 6 | 7.5 | 9 | 4 | 5 | 7 | **6.33** | igen |
| 17 | Pepperstone SCB (Bahama) | 8 | 7.5 | 7 | 3 | 1 | 10 | 7 | 5 | **6.28** | nem |
| 18 | IC Markets Global (FSA SC) | 8 | 8.5 | 7 | 2.5 | 1 | 10 | 6 | 5 | **6.25** | nem |
| 19 | Axi EU (CySEC 433/23) | 5 | 6 | 6 | 7.5 | 9 | 7 | 5 | 4 | **6.22** | igen |
| 20 | Eightcap EU (CySEC) | 6 | 6.5 | 5 | 7.5 | 9 | 4 | 5 | 4 | **6.05** | igen |
| 21 | FP Markets Global (SC) | 8 | 8 | 6 | 2.5 | 1 | 10 | 6 | 5 | **6.03** | nem |
| 22 | Tickmill SC (FSA SD008) | 7 | 8.5 | 6 | 2.5 | 1 | 10 | 6 | 5 | **5.90** | nem |
| 23 | XM / Trading Point (CySEC) | 5 | 5 | 5 | 7.5 | 9 | 4 | 6 | 4 | **5.73** | igen |
| 24 | Exness (Cy) (CySEC) | 5 | 6 | 5 | 7 | 9 | 4 | 5 | 4 | **5.70** | igen |
| 25 | BlackBull (FSA SD045) | 7 | 7 | 5 | 2.5 | 1 | 10 | 7 | 4 | **5.58** | nem |
| 26 | Admirals SC | 6 | 6 | 5 | 2.5 | 1 | 9 | 7 | 5 | **5.17** | nem |
| 27 | Eightcap Global (SCB/FSA) | 6 | 6.5 | 5 | 2.5 | 1 | 9 | 5 | 4 | **5.00** | nem |
| 28 | **Vantage (jelenlegi; VIG Group, Mauritius FSC GB20026165 a Help Center szerint, VFSC 700271 történeti)** | 6 | 7 | 4 | 2 | 1 | 10 | 5 | 4 | **4.95** | nem |
| 29 | Exness (SC) | 5 | 7 | 5 | 2 | 1 | 10 | 5 | 4 | **4.90** | nem |
| 30 | AxiTrader (SVG) | 5 | 6 | 6 | 1 | 1 | 9 | 5 | 4 | **4.65** | nem |
| 31 | XM Global | 5 | 5 | 5 | 2 | 1 | 9 | 6 | 4 | **4.60** | nem |

\* **Végr. = gyártói állítás alapján** (no last look, matching-idő, szerverhely, átlagos spread a bróker közlése szerint); független TCA-mérés egyik brókerről sincs (becsült).

**Érzékenység (becsült).** Ha a pro státusz nem jön össze, az EU-s brókerek tőkeáttétel-pontja 3-ra esik (−0,3–0,45 pont): Pepperstone EU 7,2; IC Markets EU 7,1; Tickmill Europe 6,83. A Vantage így is az utolsó harmadban van.

**Érzékenység: adósúly = 0** (a maradék súlyok 90-re normálva; saját újraszámolás a fenti táblából, becsült). Top 10: 1. IBKR Ireland 8,53; 2. LMAX Broker Europe 8,06; 3. Darwinex 7,50; 4. Pepperstone EU 7,44; 5. Dukascopy Bank (FINMA) 7,36; 6. IC Markets EU 7,22; 7–8. FP Markets EU és Dukascopy Europe 7,17; 9–10. Tickmill Europe és Saxo Bank 7,08. Az offshore jogalanyok nyernek a legtöbbet (Pepperstone SCB 6,28 → 6,86, a 11–12. hely az IG Europe-pal holtversenyben), de a top 10 összetétele nem változik, csak a sorrend (a Dukascopy Bank a 8. helyről az 5.-re lép). A jelenlegi Vantage-számla 5,39 ponttal a 26. lesz, mögötte az XM/Trading Point (CySEC), mindkét Exness, az AxiTrader (SVG) és az XM Global. Az adó tehát nem dönti el a Vantage helyét.

**EURUSD raw, 1 lot, oda-vissza jutalék** (mért díj; a lotérték becsült): IBKR ≈4,7 USD + IdealPro-spread; Dukascopy ≈4,2 USD (50 000 USD betét felett) vagy ≈8,2 USD (5000 USD alatt); Darwinex pro 3 USD; FP Markets EU, Tickmill Europe, BlackBull 6 USD; Vantage Raw 6 USD (A1, becsült); IC Markets EU és Pepperstone EU 7 USD (IC: 0,1 pip átlagos spread, mért).

## 3. Platform-/API-mátrix (a tipikus HU-útvonallal pontozva)

| # | Platform / API | Auto | Költs. | Végr.* | Szab. | Adó | Tőkeátt. | Eszk. | Adat | Súlyozott |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | IBKR TWS + Web API | 9 | 9 | 8 | 9 | 9 | 5 | 10 | 8 | **8.50** |
| 2 | LMAX FIX | 9 | 8 | 10 | 8 | 9 | 7 | 5 | 7 | **8.15** |
| 3 | Darwinex MT5+FIX+ZeroMQ | 9 | 8 | 7 | 8 | 8 | 6 | 6 | 6 | **7.55** |
| 4 | Dukascopy JForex/FIX | 9 | 6 | 8 | 8 | 9 | 4 | 6 | 9 | **7.45** |
| 5 | cTrader FIX 4.4 | 9 | 9 | 7 | 7 | 7 | 6 | 5 | 6 | **7.35** |
| 6 | QuantConnect LEAN live | 8 | 7 | 6 | 8 | 8 | 5 | 9 | 8 | **7.35** |
| 7 | cTrader Open API/cBots | 8 | 9 | 7 | 7 | 7 | 6 | 6 | 6 | **7.25** |
| 8 | Saxo OpenAPI | 6 | 5 | 7 | 9 | 9 | 5 | 10 | 7 | **7.10** |
| 9 | IG REST/Streaming | 7 | 5 | 6 | 9 | 9 | 5 | 9 | 6 | **7.00** |
| 10 | Sierra Chart | 7 | 8 | 8 | 7 | 5 | 7 | 4 | 9 | **6.90** |
| 11 | Rithmic | 8 | 6 | 8 | 7 | 6 | 7 | 4 | 8 | **6.85** |
| 12 | CQG | 8 | 5 | 8 | 7 | 7 | 7 | 5 | 7 | **6.85** |
| 13 | NinjaTrader | 7 | 8 | 7 | 7 | 5 | 8 | 4 | 7 | **6.75** |
| 14 | MetaTrader 5 | 6 | 9 | 6 | 6 | 5 | 6 | 6 | 6 | **6.35** |
| 15 | TradingView webhook | 5 | 7 | 3 | 7 | 5 | 5 | 8 | 7 | **5.70** |
| 16 | MetaTrader 4 | 4 | 9 | 5 | 6 | 5 | 6 | 4 | 4 | **5.50** |

\* Végr. = gyártói állítás alapján (lásd a 2. fejezet megjegyzését).

Kulcsadatok (mért): a cTrader Open API 50 kérés/s, a cTrader FIX 4.4 minimum nélkül érhető el. A Saxo OpenAPI 1 megbízás/s és 120 kérés/perc, a nap végén FIFO-nettósít. A TradingView webhook csak a 80/443-as portra megy, 3 s timeouttal, kétlépcsős azonosítással. Az MT5 Python csomagnak csak Windows-wheele van. A QuantConnect FX/CFD-t élőben csak OANDA-n át köt (az OANDA EU v20 API-ja nem ellenőrzött).
Infrastruktúra (mért): LMAX 3 ms matching, no last look; Darwinex Equinix LD4, no last look; IC Markets EU MT-szerverek Equinix NY4.

## 4. Ajánlás ügyféltípusonként

**(a) MT-centrikus retail** (a meglévő EA marad, MT5):
1. **Pepperstone EU:** az 1:500-as pro tőkeáttétel mért, és MT5, cTrader, TradingView is van egy CySEC- és BaFin-csoportnál.
2. **IC Markets EU:** NY4-es Raw MT5-szerverek, 0,1 pip átlagos spread, a cTrader FIX pedig átjáró az API-first felé.
3. **Darwinex:** MT5 és FIX 4.4 egy helyen, LD4, no last look, emellett külső tőke (15% sikerdíj). Grid/martingale-nél a D-Score büntet.
- Tartalék: a Tickmill Europe a legolcsóbb (3 USD/oldal), és pro ügyfélnek is ad negatívegyenleg-védelmet (visszavonhatóan).

**(b) API/FIX-first algo** (a meta-platform ExecutionAdapterei):
1. **IBKR Ireland:** TWS és Web API, a legalacsonyabb FX-díj, QuantConnect- és Nautilus-adapter, minden eszközosztály. Az interactivebrokers.hu ide irányít, és magyar TBSZ-számla is van.
2. **LMAX Broker Europe:** FIX, firm likviditás last look nélkül. Ez a végrehajtási minőség mércéje, de csak pro státusszal érhető el.
3. **Dukascopy Europe:** JForex Java API és FIX 4.4, és ugyanaz az SWFX-feed adja a backteszthez az ingyenes tickadatot.
- Közel van: a Darwinex FIX 4.4 és a cTrader FIX bármely EU-s cTrader-brókernél.

**(c) Multi-asset, intézményi szintű:**
1. **IBKR Ireland:** 150+ piac, egyetlen API.
2. **Saxo Bank:** dán bank, S&P A-, OpenAPI és FIX. A FIFO-nettósítás és az 1 megbízás/s limit korlát.
3. **IG Europe:** BaFin-felügyelet, 17 000+ piac, REST/streaming API. Market maker.
- Az FX-végrehajtási lábhoz LMAX javasolt.

**A Vantage helye:** mindhárom profilban a lista alján van. Nincs FIX, nincs EU-s felügyelet, és két hatósági lépés is érinti (AFM, FCA).

## 5. Migrációs út (indokolt)

1. **Absztrakció (0. hét).** Az EA váljon vékony végrehajtóvá. A szimbólum-, margin-, stop-out- és díjadatok konfigurációba kerüljenek. Kell egy ExecutionAdapter-interfész MT5-re, cTraderre, FIX-re és IBKR-re (A9).
2. **Párhuzamos EU-s MT5-számla (1–4. hét).** A választás: Pepperstone EU, IC Markets EU vagy Tickmill Europe. Ugyanaz az EA fusson, de 1:30-ra méretezve (≈1/16 pozícióméret, A1). Helyszínrégiónként egy VPS kell (pl. IC Markets EU: NY4; Vantage: a saját szerverrégiója), és a slippage-et, a fill-arányt, a spreadet és a swapot a mért round-trip idővel (RTT) normalizálva kell összevetni (A1: `method-vantage-execution-audit`). Egyetlen VPS-ről mérve a helyszínek közti hálózati különbség (London→New York 70,1 ms, mért: A8 `wondernetwork-pings`) torzítaná az eredményt.
3. **Pro kérelem (párhuzamosan).** Bizonyíték: a Vantage MT5-története 4 negyedévre, negyedévente legalább 10, legalább 1 lotos ügylettel, ÉS ezen felül 500 000 EUR feletti portfólió vagy legalább 1 év pénzügyi szakmai munka (a háromból kettő kell; az ügyletszám egymagában nem elég) (`a11-pro-evidence-pack`). Érdemes 2–3 brókernél egyszerre beadni.
4. **API-láb (2–3. hónap).** IBKR (FX, futures, részvény) vagy cTrader FIX / Darwinex FIX. A FIX-kód (QuickFIX) később LMAX-ra is átvihető.
5. **Leépítés.** A Vantage-ből rendszeres profitkivétel, a tőke fokozatosan átkerül. Az EU-s számlákról az ETÜ-igazolást (67/A (3) bc) minden évben ki kell kérni.
6. **Kapuk.** Egy lépés csak akkor jöhet, ha a mért all-in költség és a slippage nem rosszabb a Vantage-nél, és a margin-modell 1:500 vagy 1:30 mellett is megmarad.

## 6. Hiányok és korlátok

- Az ÁSZF-ek EA-, HFT-, scalping- és latency-arbitrage-tilalmait egyik brókernél sem olvastam végig. Ezeket PDF-ből archiválni kell (nem ellenőrzött).
- A szerverhely csak két esetben mért: IC Markets EU NY4, Darwinex LD4. A többi becsült. Saját traceroute és round-trip mérés kell.
- Nem ellenőrzött CySEC-licencszám (az ESMA-registerben aktívak, mért): Exness Cy, XM, Eightcap EU, Stratos. Nem ellenőrzött pro tőkeáttétel: IC Markets EU, IG, Saxo, IBKR, Darwinex, LMAX, Dukascopy.
- 403 miatt nem olvastam: Exness, XM, FXCM, Vantage. A MultiCharts árlapja 404.
- Nem ellenőrzött, hogy az OANDA EU ad-e v20 API-t, és hogy magyar lakos nyithat-e számlát az Alpacánál, a TradeStationnél vagy a NinjaTrader Clearingnél.
- Az MNB- és ESMA-figyelmeztetéseket név szerint nem tudtam lekérdezni (az MNB figyelmeztetés-URL-jei 404-et adnak). Az A1 szerinti FCA-lépés (figyelmeztető lista, 2026-04-02) mért; az AFM-lépés (2024-10-24) másodlagos forrásból (Finance Magnates, 2024-11-13) származik.
- Független végrehajtási minőségi adat (TCA) egyik retail brókerről sincs. A „végrehajtás” pontok gyártói állításokon és infrastruktúra-tényeken alapulnak (becsült).
