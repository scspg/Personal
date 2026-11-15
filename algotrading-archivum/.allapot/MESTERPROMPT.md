# ALGOTRADING-ARCHÍVUM – MESTERPROMPT (feljavított specifikáció)

> Ezt a promptot a kutatás és az összeállítás végrehajtója (ember vagy AI-ágens) követi. Ez a teljes munka forrása: ha a kontextus elveszik, innen újra kell tudni indulni. Független az ARCHIVUM (blackout) kiadástól: saját mappa, saját katalógus, saját ZIP (`algotrading-archivum/ALGOTRADING.zip`).

---

## 0. Szerep, cél, átadás

**Szerep:** principal szintű kvantitatív kutató + piaci infrastruktúra-mérnök + adatbeszerző + kockázatkezelő + AI-rendszertervező, egy személyben. Nyelv: magyar; angol csak bevett szakszavaknál, kódnál, API-neveknél.

**Alapelv – platform- és brókerfüggetlenség (megrendelői kérés, 2026-11-15):** a MetaTrader 5 és a Vantage csak a **jelenlegi** eszköz, bármikor cserélhető jobbra. A platform univerzális alapokra épül:
- kanonikus instrumentum-, megbízás- és számlamodell;
- a brókerspecifikus adatok (kontraktusméret, margin, swap, stop-out, kereskedési idő, díjak) **konfigurációs adatok**, nem kód;
- minden végrehajtási hely egy `ExecutionAdapter`-szerződés mögött van (MT4/MT5, cTrader, FIX, IBKR, LMAX, Dukascopy, kripto CCXT, Polymarket, Kalshi, Betfair stb.);
- a stratégiák és a döntési réteg nem tudhatják, melyik brókeren futnak.
Minden tételnél és fejezetnél, ahol a Vantage vagy az MT5 szerepel, jelölni kell az általánosítható részt és a jobb alternatívát. A bróker- és platformválasztás maga is kutatási kérdés (lásd: összehasonlító mátrix, A11).

**Megrendelő helyzete (kiinduló állapot):**
- Már fut egy grid alapú algoritmikus kereskedés egy bérelt szerveren (MetaTrader).
- Elsődleges számla: **Vantage, MetaTrader (MT4/MT5), 1:500 tőkeáttétel**. A legnagyobb fókusz a **gyorsabb pénzkeresés** ezen a számlán, automatizált programmal.
- A szoftvert **AI-jal fejlesztik**; az anyag egy fejlesztőcsapatnak megy át.

**Cél:** egy **pénzügyi meta-platform** teljes tudás-, adat- és eszközalapja, amelyből felépíthető egy rendszer, ami funkcióban és döntési minőségben **felülmúlja** az alábbiakat:
- a Renaissance Medallion ismert működési elveit;
- a BlackRock Aladdin kockázati és portfólió-platformját;
- a Bloomberg Terminal adat- és elemzői univerzumát.

Őszinteségi megkötés: a Medallion-szintű teljesítményt egy dokumentum nem garantálja. Az előny (edge) a kutatási folyamatból, az adatminőségből, a végrehajtásból és a kockázatkezelésből jön. Az anyag dolga, hogy ezek **mindegyikéhez** a világ legjobb elérhető forrását, módszerét és ellenőrzési eljárását adja, és mérhetővé tegye, hol tart a platform a referenciákhoz képest.

**Átadás:**
- ZIP: `ALGOTRADING.md` (fő dokumentum), `ALGOTRADING-kompakt.md`, `ALGOTRADING-chat.md` (LLM-be tölthető), `ALGOTRADING.html` (vizuális, szűrhető, kalkulátorokkal), `katalogus.jsonl` (gépi), letöltő szkript az ingyenes adatokhoz, `FEJLESZTOI-SPEC.md` (a csapatnak), `OLVASS-EL.md`.
- A katalógus legyen **legalább akkora, mint a blackout-kiadásé**: legalább 1000 tétel, legalább 25 fejezet.

---

## 1. A platform modulárisan – mit kell lefedni (a kutatás vázlata)

Minden modulhoz gyűjtendő: (a) adatforrás(ok), (b) nyílt forráskódú eszköz(ök) GitHub/HF/egyéb, (c) fizetős profi megoldás(ok) áraikkal, (d) alapirodalom (könyv, cikk, kurzus), (e) buktatók, (f) hogyan lesz jobb, mint a referencia.

### M1. Piaci adat (minden eszközosztály, minden mélység)
- **FX és CFD:** tick, L1/L2, spread-történet, swap, rollover.
  - Források: Dukascopy, TrueFX, HistData, Tickstory, a broker MT5 export.
  - Vantage szimbólumspecifikációk: kontraktusméret, margin, stop-out szint, kereskedési idők.
- **Részvények:**
  - tick, OHLCV, L2/L3, opciós lánc, IV-felület;
  - corporate actions, osztalék, split;
  - survivorship-mentes univerzum (delisted).
- **Határidős termékek:** CME, ICE, Eurex; folytonos kontraktusok, roll-szabályok.
- **Kötvények, kamatok:** hozamgörbék, swapok, SOFR/ESTR/BUBOR.
- **Nyersanyag, energia:** áram- és gázpiac (ENTSO-E, EEX, HUPX).
- **Kripto:**
  - CEX tick/L2/L3, funding, open interest, likvidációk;
  - DEX, on-chain, mempool, MEV, stablecoin-áramlások.
- **Referenciaadat:**
  - szimbológia: OpenFIGI, GLEIF LEI, ISIN, CUSIP-jellegű kódok;
  - tőzsdei naptárak, ünnepnapok.
- **Mezőnként rögzítendő:** történeti mélység, granularitás, késleltetés, licenc, ár/hó, API-típus (REST/WS/FIX/gRPC), letöltési mód, ismert adathibák.

### M2. Fundamentális és szabályozói adat
- SEC EDGAR (10-K/10-Q/8-K, XBRL, full-text search, 13F, Form 4 bennfentes, 13D/G), ESMA, EU átláthatósági adatok, BÉT, MNB, KELER.
- Elemzői becslések, earnings calendar, earnings call átiratok.
- Short interest, securities lending, ETF-holdings, fund flows.
- **Faktoradatok:** Kenneth French Data Library, AQR datasets, Shiller, Global Factor Data (JKP), Open Source Asset Pricing.

### M3. Makró, gazdaság, statisztika – „a mélység menjen a végtelenségig”
- **Nemzetközi:** FRED, ALFRED (vintage, look-ahead-mentes!), BIS, IMF, Világbank, OECD, ECB SDW, Eurostat, KSH, MNB, BLS, BEA, Census, Fed H.4.1/H.8, CFTC COT.
- **Jegybanki kommunikáció:** jegybanki beszédek, jegyzőkönyvek (szöveges korpusz).
- **Kutatási célú hosszú idősorok:** Jordà-Schularick-Taylor Macrohistory, Maddison, Bank of England Millennium dataset.
- **Statisztikai referencia:** minden, ami súlyozható jel lehet, akkor is, ha nem kifejezetten pénzügyi:
  - demográfia, energia, időjárás és klíma (NOAA, ERA5);
  - mezőgazdasági termés (USDA WASDE), szállítás (AIS), repülés (OpenSky);
  - műholdkép (Sentinel), éjszakai fények (VIIRS), Google Trends, Wikipedia pageviews;
  - szabadalmak, álláshirdetések, appletöltések, webforgalom, kártyás költés.

### M4. Hírek, szentiment, esemény
- **Valós idejű hírfolyamok:** Reuters, Bloomberg, Dow Jones, Benzinga, Newsquawk, FinancialJuice, Tiingo News, Alpha Vantage News, Polygon News, CryptoPanic.
- **Archív és tömeges:** GDELT, Common Crawl News, nyílt hírhalmazok a HF-en.
- **Közösségi és szöveges források:** X/Twitter API (ár!), Reddit API, Telegram, StockTwits.
- **Gazdasági naptár:** konszenzus vs. tényleges érték, meglepetés-index.
- **Esemény → ármozgás adatbázisok.** LLM-alapú hírértelmezés késleltetési költsége.

### M5. Predikciós piacok és sportfogadás
- **Predikciós piacok:**
  - Polymarket (CLOB API, Gamma API, on-chain történet), Kalshi (API, eseménytípusok), Manifold, PredictIt, Metaculus (előrejelzések), Smarkets, Betfair Exchange (API, történeti adat);
  - jogi hozzáférhetőség Magyarországról és az EU-ból (geoblokk, ÁSZF);
  - likviditás, díjak.
- **Sportfogadás:**
  - Pinnacle (éles szorzók, a „hatékony ár” referencia), odds-API-k, történeti szorzó-adatbázisok (football-data.co.uk stb.);
  - closing line value (CLV), a fogadóirodák limitálási gyakorlata, arbitrázs és value betting.
- **Hosszú és rövid távú „befektetés” sportpiacokon:** bankroll-kezelés (Kelly, frakcionális Kelly), varianciaelemzés.
- **Kereszthasznosítás:** a predikciós piaci árak mint makró- és eseményvalószínűség-jelek a tőzsdei modellekhez.

### M6. Végrehajtás és brókerek
- **MetaTrader:**
  - MQL5/MQL4 referencia, Strategy Tester (valós tickes mód, optimalizáló, felhő-ügynökök);
  - MetaTrader5 Python csomag, ZeroMQ/socket hidak, Expert Advisor-architektúra;
  - VPS és MetaQuotes VPS.
- **Vantage:**
  - jogalanyok és szabályozók (melyik adja az 1:500-at);
  - MT4/MT5 szerverek fizikai helye, számlatípusok (Standard, RAW, PRO), jutalék, spread, swap, stop-out;
  - ÁSZF a scalpingról, a HFT-ről, a latency arbitrage-ról és az EA-król;
  - B-book vagy A-book jelek; kifizetési tapasztalatok.
- **Alternatív és kiegészítő végrehajtás:**
  - cTrader, FIX API (QuickFIX/J, QuickFIX/n), Interactive Brokers (TWS API);
  - LMAX, Dukascopy JForex;
  - kripto: CCXT, a tőzsdék natív API-jai, rate limitek, colocation (pl. Binance–AWS Tokió).
- **Végrehajtási minőség:** slippage-mérés, fill-arány, requote, last look, spread-tágulás rollovernél és híreknél, hétvégi gap.

### M7. Kutatás, backtest, szimuláció
- **Motorok:**
  - QuantConnect LEAN, NautilusTrader, vectorbt (PRO), backtrader, zipline-reloaded, Backtesting.py, hftbacktest, bt;
  - freqtrade, hummingbot, Jesse, Microsoft Qlib, FinRL, TensorTrade;
  - MT5 Strategy Tester.
  - Mindegyiknél mérve: GitHub csillag, utolsó commit, licenc, sebesség, eseményvezérelt vagy vektoros.
- **Jövőbeli variációk számítása:**
  - Monte Carlo (bootstrap, block bootstrap, stationary bootstrap);
  - szintetikus piacgenerálás: GAN/diffúziós idősor, ágens alapú piacmodellek (ABIDES), regime-switching szimuláció;
  - stresszforgatókönyvek.
- **Validálás, overfitting ellen:**
  - walk-forward, purged/embargoed k-fold, Combinatorial Purged CV (López de Prado);
  - Deflated Sharpe Ratio, Probability of Backtest Overfitting (PBO), White's Reality Check, Hansen SPA;
  - több hipotézis tesztelése: Harvey–Liu–Zhu t>3 küszöb.
- **Adattároló:** ArcticDB, kdb+/KX (ár), QuestDB, ClickHouse, TimescaleDB, DuckDB + Parquet, Apache Iceberg; tickadat-tömörítés.

### M8. Stratégia-könyvtár (mind, forrással, matekkal, buktatóval)
- **Grid és martingale:**
  - grid (aritmetikus, geometrikus, dinamikus ATR-alapú, trendszűrős);
  - martingale és anti-martingale, hedge-grid.
  - **Kötelező:** csődvalószínűség-matek, margin call-modell 1:500 mellett.
- **Klasszikus stratégiacsaládok:**
  - mean reversion; statisztikai arbitrázs (párok, kointegráció, Kalman-szűrős hedge ratio, PCA-reziduum);
  - momentum (idősoros és keresztmetszeti), trendkövetés (CTA), carry (FX, futures), volatilitási kockázati prémium;
  - market making (Avellaneda–Stoikov), order-flow és mikrostruktúra (OFI, VPIN);
  - hír- és eseményvezérelt, szezonalitás és naptáranomáliák (a lecsengés bizonyítékával).
- **ML, mélytanulás, RL:**
  - ML (gradient boosting, random forest), mélytanulás (LSTM, TCN, Transformer);
  - **idősoros alapmodellek:** TimesFM, Chronos, Moirai, Lag-Llama, TimeGPT;
  - megerősítéses tanulás.
- **Rezsim, méretezés, keresztpiaci stratégiák:**
  - rezsimfelismerés (HMM, változáspont-detektálás);
  - pozícióméretezés (Kelly, volatilitás-célzás, risk parity);
  - kripto: funding/basis arbitrázs, cross-exchange arbitrázs;
  - predikciós piaci arbitrázs (Polymarket ↔ Kalshi ↔ Betfair) és sport value betting.
- **Minden stratégiához:** képlet, paraméterek, „mikor működik / mikor hal meg”, publikált teljesítmény és annak lecsengése, implementációs repó.

### M9. AI döntési réteg – súlyozott, többmodelles, ördögügyvéddel
- **Felépítés:** a döntés több, egymástól független „szavazóból” áll, a szavazatokat súlyozva összegzik.
  - statisztikai modellek;
  - ML-modellek;
  - LLM-ágensek (hírek, makró, narratíva);
  - külön **ördögügyvéd-ágens**, amely minden javaslat ellen érvel (a felhasználó és az AI javaslata ellen is).
  - Blokkolási joga feltételhez kötött: ha a kockázati vagy kalibrációs küszöb sérül, a javaslat nem megy ki.
- **Súlyozási módszerek** (a „neurális súlyok” analógiájára):
  - Bayesian Model Averaging, stacking/meta-learner;
  - online tanulás: Hedge/multiplicative weights, Exp3, Thompson sampling;
  - kalibráció: Brier, log-loss, reliability diagram, isotonic/Platt;
  - meta-labeling, konformális predikció (bizonytalansági sávok).
- **Kész keretrendszerek és cikkek:** TradingAgents, FinRobot, FinGPT, FinMem, FinAgent, BloombergGPT (cikk), a pénzügyi LLM-benchmarkok.
  - A „Javhez hasonló” statisztikai AI-t ellenőrizni kell: mire gondolhatott a megrendelő (pl. Jane Street-szerű?). Röviden jelölni a lehetséges értelmezéseket, és mindegyikhez forrást adni.
- **Az „AI mozgatókar” (autonóm végrehajtó jogkör):**
  - jogosultsági szintek: javaslat → jóváhagyással kötés → korlátozott autonómia → teljes autonómia;
  - kill switch, napi veszteséglimit, maximális nyitott kitettség;
  - auditnapló, ember-a-hurokban szabályok, promptinjekció elleni védelem (hírfolyamból érkező manipuláció).

### M10. Kockázat, tőke, számla
- **Az 1:500-as áttétel matematikája:**
  - margin, szabad margin, stop-out;
  - mekkora mozgás viszi el a számlát;
  - csődvalószínűség grid és martingale esetén; Kelly-túlméretezés.
- **Kockázati mértékek:** VaR, CVaR/ES, drawdown-eloszlás, farokkockázat (EVT), korrelációs összeomlás, likviditás, gap-kockázat.
- **Partnerkockázat:**
  - brókerkockázat: offshore jogalany, szegregált számla, befektetővédelem, kifizetési kockázat;
  - kriptotőzsde-kockázat.
- **Portfólió-szintű kockázati motor** (Aladdin-szerű):
  - faktormodellek (Barra-szerű, nyílt alternatívák);
  - stressztesztek, történelmi forgatókönyvek (1987, 2008, 2015 CHF, 2020 március, 2022, 2024 augusztus jen-carry).

### M11. Infrastruktúra: hardver, szerverhely, költözés
- **Brókerszerverek fizikai helye:**
  - Vantage MT4/MT5: melyik adatközpont (Equinix LD4/LD5, NY4/NY5, TY3, SG1 stb.), ellenőrzött forrásból;
  - nagy kriptotőzsdék régiói;
  - a Polymarket és a Kalshi infrastruktúrája.
- **VPS és colocation:**
  - szolgáltatók árral és ping-adattal: BeeksFX, ForexVPS, NYCServers, MetaQuotes VPS, Equinix-közeli VPS-ek, Hetzner/OVH a nem késleltetésérzékeny részre;
  - cross-connect.
- **Hardver:**
  - kereskedőszerver: magas órajelű CPU, RAM, NVMe, kernel-hangolás, NIC, PTP-időszinkron;
  - kutatógép: GPU-k, RAM, tárhely a tickadathoz.
  - Konkrét konfigurációk 3 árszinten, magyar és EU-s boltlinkekkel.
- **Hova költözzünk:**
  - mátrix: adó (tőkenyereség, kripto, fogadás), szabályozás, brókerhozzáférés, késleltetés a fő adatközpontokhoz, megélhetési költség;
  - jelöltek: Magyarország, Ciprus, Málta, Portugália, Svájc, Egyesült Arab Emírségek, Szingapúr, Egyesült Királyság, Írország, Észtország, Grúzia, Monaco, Puerto Rico.
  - Magyar adó: CFD, forex, offshore bróker, kripto (2022-es szabály), sportfogadás, predikciós piac.

### M12. Benchmark-platformok szétszedése
- **Bloomberg Terminal:** funkciók (GP, FA, ECO, WIRP, OMON, PORT, BQL), adatkörök, ár. Mi a nyílt vagy olcsóbb megfelelő (OpenBB, Koyfin, TradingView, Refinitiv Workspace, FactSet)?
- **BlackRock Aladdin:** modulok (risk, OMS/EMS, compliance, Aladdin Wealth, eFront), a kockázati modell elvei.
- **Renaissance Medallion:** nyilvánosan ismert elvek (Zuckerman: *The Man Who Solved the Market*, interjúk, perek, 13F), bizonyított számok vs. legendák.
- **Más szereplők:** Two Sigma, Citadel, Jane Street, D. E. Shaw, Man AHL, AQR, WorldQuant (alpha-gyár), Numerai (crowd-sourced, nyílt adattal), Jump, XTX.
- **Paritásmátrix:** funkció × (Bloomberg, Aladdin, Medallion-elv, a mi platformunk).
  - Hol tudunk jobbak lenni? Például: predikciós piaci jelek, LLM-ensemble, gyorsabb kísérletezési ciklus, testreszabott kockázat kis számlára.

### M13. Tudás: könyvek, cikkek, kurzusok, közösségek
- **Könyvek:** López de Prado (AFML, ML for Asset Managers), Chan, Carver, Kissell, Harris (*Trading and Exchanges*), Natenberg, Taleb, Thorp, Zuckerman, Grinold–Kahn, Tsay, Hamilton.
- **Cikkgyűjtemények:** SSRN, arXiv q-fin, a Journal of Portfolio Management kulcscikkei, Quantpedia (ár), Alpha Architect.
- **Kurzusok:** MIT OCW, Coursera, QuantConnect Bootcamp, WorldQuant University (ingyenes MSc).
- **Közösségek:** MQL5.com fórum és Market (buktatók: hamis EA-k), QuantConnect, r/algotrading, QuantNet, Wilmott, Elite Trader, Nuclear Phynance.

### M14. AI-jal fejlesztett szoftver – folyamat a csapatnak
- **Repó- és architektúra-sablon:**
  - eseményvezérelt mag;
  - adattó (nyers → tisztított → feature store), modell-regiszter (MLflow);
  - kísérletkövetés, OMS, kockázati motor, EA-híd, megfigyelés (Prometheus/Grafana), riasztás.
- **AI-kódolás:**
  - ágensek és agentic IDE-k, spec-first fejlesztés, tesztek, property-based testing;
  - MQL5 kódgenerálás buktatói;
  - CI: backtest-regresszió minden commitra, paper trading → kis tőke → skálázás kapuk.
- **Biztonság:** API-kulcsok és secrets, a számla védelme, a „mozgatókar” jogosultságai, ellátási lánc (csomagok).

### M15. Új ötletek, ahol még senki nem gondolkodott
- **Hipotézisgyár:** legalább 150 új vagy ritkán használt ötlet. Mindegyiknél:
  - mechanizmus;
  - adatforrás(ok);
  - tesztelhetőség (hogyan cáfolható);
  - becsült kapacitás;
  - kockázat;
  - újszerűségi pont (0–10, őszintén: ha publikált, hivatkozni rá).
- **Kereszt-domain irányok:**
  - predikciós piac → FX/index; sportfogadási mikrostruktúra → FX;
  - LLM-ek közötti egyet nem értés mint volatilitásjel;
  - időjárás → energia → devizák; hajózás → nyersanyagdevizák;
  - jegybanki beszédek embeddingje; az opciós implikált eloszlás összevetése predikciós piaci valószínűséggel;
  - funding-rezsim; figyelem-adatok;
  - ágens alapú önjáték-szimuláció; „az ördögügyvéd bizalma” mint pozícióméret-szorzó;
  - brókeroldali viselkedés modellezése (spread-tágulás előrejelzése).

### M16. Bevált módszerek: statisztikai összefüggésekből értelem és eredmény (a felhasználó kiemelt kérése, 2026-11-15)
**Cél:** megtalálni mindenkit, aki igazoltan működő módszerrel nyert ki statisztikai összefüggésekből használható következtetést és pénzt vagy döntési előnyt, bármely területen. A mintázatokat és módszereket minimum lemásolhatóvá, maximum jobbá kell tenni.

**Minden esettanulmányhoz rögzítendő:**
- ki, mikor;
- milyen adat;
- milyen módszer;
- mi lett az igazolt eredmény, forrással; a legenda külön jelölve;
- miért működött;
- mikor és miért halt meg;
- reprodukálható kód vagy cikk;
- hogyan csinálnánk jobban (konkrétan);
- mire használható a platformon.

**Esettanulmányok területei:**
- **Kvant pénzügy:** Thorp/Princeton-Newport, Renaissance (Baum–Welch/HMM, Berlekamp, Laufer), D. E. Shaw, WorldQuant 101 Alphas, Two Sigma.
- **Nyertes versenymegoldások:** Kaggle Jane Street, Optiver, G-Research; Numerai.
- **Sportfogadás és szerencsejáték:** Bill Benter (lóverseny, Hongkong, multinomiális logit), Billy Walters, Starlizard/Tony Bloom, Smartodds/Matthew Benham, Voulgaris, Moneyball/sabermetrika.
- **Kaszinó és lottó:** MIT blackjack-csapat; Thorp–Shannon rulett; lottó-kiskapuk (Cash WinFall/Selbee, Srivastava kaparós sorsjegyei).
- **Előrejelzés és nowcasting:**
  - Tetlock szuperelőrejelzői, Silver/538, Iowa Electronic Markets;
  - NY Fed Staff Nowcast (dinamikus faktormodell), Billion Prices Project;
  - M4/M5 előrejelzési versenyek tanulságai.
- **Alternatív adat:** műholdas parkolóhely- és olajtartály-árnyék számlálás, kártyás költés → negyedéves eredmény, Google Trends (Preis 2013), Twitter-hangulat (Bollen 2011, és a megismétlési vita).
- **Klasszikus statisztikai áttörések:** Wald túlélési torzítása, Turing Banburismus (szekvenciális elemzés), bayesi keresés (USS Scorpion, AF447), Benford-törvény csalásfelderítésre, John Snow kolera (kauzalitás).
- **Ellenpéldák:** Google Flu Trends kudarca, LTCM (korrelációs összeomlás).
- **Játékelmélet és MI:** Libratus/Pluribus, AlphaGo/AlphaZero, FICO-hitelpontozás, aktuáriusi módszerek.

**Módszertár** (mindegyiknél: mikor jó, mikor csal, Python-könyvtár):
- **Kauzalitás:** Granger, transfer entropy, kauzális felfedezés (PC/FCI, PCMCI/Tigramite), DoWhy/EconML, szintetikus kontroll, különbségek különbsége, instrumentális változó.
- **Függőség és hasonlóság:** kölcsönös információ, kopulák, DTW, kointegráció.
- **Állapottér- és rezsimmodellek:** Kalman/állapottér, HMM, változáspont-detektálás.
- **Automatikus jelbányászat:** szimbolikus regresszió (PySR), genetikus programozás alfa-bányászathoz, AutoML.
- **Magyarázat és ensemble:** SHAP/permutációs fontosság, ensemble (Netflix Prize tanulságai).
- **Védelem hamis összefüggések ellen:** többszörös tesztelés (FDR, Bonferroni, Harvey–Liu–Zhu), Tyler Vigen-féle hamis korrelációk, adat-szaglászás.

**Kimenet:** `research/a10_methods.jsonl` (legalább 120 esettanulmány + módszer, a sémán felül ezekkel a mezőkkel: who, data_hu, method_hu, result_hu, result_verified, why_worked_hu, died_hu, improve_hu, platform_use_hu, code_urls) és `research/a10_summary.md`.

---

## 2. Tételszintű séma (katalogus.jsonl)

```json
{"id": "kebab-id", "name": "…", "cat": "…", "sub": "…", "url": "fő link", "docs_url": "…", "info_url": "…",
 "access": "free|registration|freemium|paid|institutional", "price": "eredeti szöveg", "price_eur_month": 0,
 "provider": "…", "assets": ["fx","cfd","equity","options","futures","crypto","prediction","sports","macro","alt"],
 "regions": ["global","us","eu","hu"], "history_from": "YYYY", "granularity": "tick|l2|l3|1s|1m|1h|1d|event|text",
 "latency": "realtime|delayed|eod|batch", "api": "rest|ws|fix|grpc|sdk|bulk|none", "license": "…",
 "bytes_est": null, "download": {"method": "http|git|hf|api|manual|agent", "url": "…"},
 "github": {"repo": "owner/name", "stars": 0, "last_commit": "YYYY-MM-DD", "license": "…"},
 "scores": {"R": 0, "E": 0, "Q": 0, "C": 0, "L": 0, "F": 0, "Z": 0},
 "tier": 0, "notes_hu": "…", "pitfalls_hu": "…", "verified": "mért|becsült|nem ellenőrzött", "checked": "2026-11-15"}
```

**Pontozás (0–10):**
- R: relevancia a platformhoz;
- E: edge-potenciál (alfa-forrás-e);
- Q: adatminőség, megbízhatóság;
- C: költséghatékonyság;
- L: késleltetés vagy frissesség;
- F: karbantartottság, jövőállóság;
- Z: jogi és ÁSZF-biztonság (Magyarországról használható-e).

**Összpont profilonként:**
- „gyors pénz – aktív automatizált kereskedés” (platformfüggetlen; jelenleg MT5/Vantage): E és L hangsúllyal;
- „Aladdin-kockázat”: Q és R;
- „kutatás”: R és Q;
- „predikciós/sport”: E és Z.

**Szint:**
- 0 = nélkülözhetetlen mag;
- 1 = erősen ajánlott;
- 2 = bővítés;
- 3 = luxus vagy intézményi.

### 2.1. Mezőszabályok (gépileg ellenőrizhető)

- **Kötelező, nem null:** `id` (kebab-case, egyedi), `name`, `cat`, `url` (http/https; websocket-végpont az `api_endpoint` mezőbe), `access`, `scores` (mind a 7 kulcs, egész 0–10), `tier` (0–3), `verified`, `checked` (ÉÉÉÉ-HH-NN).
- **Opcionális, hiány esetén `null` (soha nem üres szöveg):** `docs_url`, `info_url`, `price`, `price_eur_month`, `provider`, `granularity`, `latency`, `license`, `history_from`, `bytes_est`, `download`, `github`.
- **Felsorolt értékek:**
  - `access`: free | registration | freemium | paid | institutional
  - `assets`: fx, cfd, equity, options, futures, rates, commodities, energy, crypto, prediction, sports, macro, alt
  - `regions`: global, us, eu, uk, hu, asia, other
  - `granularity`: tick | l2 | l3 | 1s | 1m | 1h | 1d | event | text
  - `latency`: realtime | delayed | eod | batch
  - `api`: rest | ws | fix | grpc | sdk | soap | bulk | none
- **Csoport és származtatott mezők:**
  - `group`: azonos forrás változatai.
  - A build tölti ki, kézzel nem írandó: `src` (kutatási fájl), `prof` (profilpontok 0–100), `also_in` (duplikátumként összefésült források).
- **Adattételeknél (M1–M4) kötelező:**
  - `pit` (true/false/null): időponthelyes, look-ahead-mentes-e;
  - `survivorship_free` (true/false/null);
  - `vintages` (true/false/null);
  - `revision_policy` (szöveg);
  - `timestamp_semantics` (pl. „esemény ideje UTC”, „közzététel ideje”, „nap vége”).
- **Elemzési tételek** (A10 esettanulmány `cat: case_study` és módszer `cat: method`; A11 jogalanyonkénti bróker- és platform-mátrixsor): ugyanarra a cikkre vagy oldalra hivatkozhatnak, mint egy forrástétel. Ez nem duplikáció, mert nem forrás, hanem elemzés. A build nem vonja össze őket, hanem a `group` mezővel köti a megfelelő forrástételhez. Egy bróker több jogalanya (pl. EU-s és offshore) külön sor, mert a jogi és adó-besorolásuk eltér.
  - Plusz mezők: `who`, `data_hu`, `method_hu`, `result_hu`, `result_verified`, `why_worked_hu`, `died_hu`, `improve_hu` (egy konkrét, tesztelhető változtatás), `platform_use_hu`, `code_urls`.
- **Stratégia (`a7_strategies.jsonl`, `cat: strategy`) plusz mezői:**
  - `sub` (család);
  - `formula_hu`;
  - `params`;
  - `works_when_hu`, `dies_when_hu`, `decay_hu`;
  - `evidence` (lista: `{ref, url, reported_hu, label}`);
  - `impl_repos` (lista: `{repo, url, last_commit, stars, verified}`);
  - `mt5_fit` (0–10, FX/CFD-alkalmasság).
- **Ötlet (`a7_ideas.jsonl`) mezői:**
  - `id`, `title_hu`, `mechanism_hu`, `data_sources`, `test_hu`;
  - `prereg` objektum: metric, horizon, min_n, alpha, multiplicity, oos_start, cost_model, kill_rule;
  - `prior_art` (lista: `{ref, doi_or_url}`) vagy üres lista + `prior_art_note`;
  - `capacity_hu`, `risk_hu`;
  - `novelty` (0–10), `mt5_fit` (0–10).

### 2.2. Profilsúlyok (a `build.py` PROFILES táblájával azonos)

| Profil | R | E | Q | C | L | F | Z |
|---|---|---|---|---|---|---|---|
| Gyors pénz – aktív automatizált kereskedés | 0,15 | 0,30 | 0,10 | 0,10 | 0,20 | 0,05 | 0,10 |
| Aladdin-szerű kockázat | 0,25 | 0,05 | 0,30 | 0,10 | 0,05 | 0,15 | 0,10 |
| Kutatás | 0,25 | 0,20 | 0,25 | 0,10 | 0,00 | 0,15 | 0,05 |
| Predikciós piacok és sport | 0,15 | 0,30 | 0,15 | 0,10 | 0,10 | 0,00 | 0,20 |
| Kiegyensúlyozott | 0,20 | 0,20 | 0,20 | 0,10 | 0,10 | 0,10 | 0,10 |

A profilpont: Σ(súly × pont) / Σ(súly a nem null pontokra) × 10. Ez reprodukálható: egy tétel profilpontja a hét alappontból és a fenti súlyokból pontosan kijön.

### 2.3. Pontozási rubrika (0–10 horgonyok)

| Pont | R relevancia | E edge-potenciál | Q minőség | C költséghatékonyság | L késleltetés/frissesség | F karbantartottság | Z jogi/ÁSZF |
|---|---|---|---|---|---|---|---|
| 10 | a platform magja, nélküle nem működik | dokumentált, élő, kapacitásos előny | hivatalos, auditált, PIT | ingyenes, teljes | valós idejű, ms | heti commit, nagy közösség | HU-ból teljesen legális, ÁSZF-kockázat nincs |
| 7 | fontos modulhoz kell | publikált, de lecsengő előny | megbízható gyártó, ismert hibákkal | ár arányos az értékkel | percen belül | havi frissítés | kisebb ÁSZF-feltétel |
| 4 | kiegészítő | csak más jel feature-e | közösségi, ellenőrizetlen | drága a haszonhoz képest | napi | évente | geoblokk vagy szürke zóna |
| 0–1 | nem kapcsolódik | nincs előny | megbízhatatlan | tiltóan drága | elavult | elhagyott | tilos vagy blokkolt HU-ból |

### 2.4. Átnézői rubrika (a minőségkapuhoz)

Minden átnéző területenként 0–100 pontot ad. Levonás: hibás tény −3; kitalált forrás −10 (azonnali kizáró ok); hiányzó, a szerepköréhez szükséges elem −2…−8; nem futtatható átvételi feltétel −2; belső ellentmondás −2. Minden levonáshoz hely (fájl, sor vagy id) és konkrét javítás tartozik. A kapu: minden terület ≥ 90, a hat átnéző átlaga ≥ 95. Ha forráskorlát miatt nem érhető el, azt a jelentésben külön meg kell nevezni.

---

## 3. Szabályok (nem alku tárgya)

1. **Nincs kitalált link, ár, szám, repó, API-végpont.** Minden tétel URL-je valódi, ellenőrzött (WebSearch/WebFetch); amit nem sikerült ellenőrizni: `verified: "nem ellenőrzött"`. GitHub-csillag és utolsó commit mérve (API vagy oldal), dátummal.
2. **Árak:** eredeti pénznem + EUR/hó átszámítás; „mért” (az oldalon látott) vagy „becsült”.
3. **Jogi és ÁSZF-jelölés:** geoblokk, KYC, ÁSZF-tilalom (pl. latency arbitrage, scraping), engedélyhiány.
4. **Az előny lecsengését jelölni kell:** publikált anomáliák a publikálás után átlagosan gyengülnek (McLean–Pontiff); minden stratégiánál jelezni.
5. **Kockázati figyelmeztetés egyszer, tényszerűen,** a kockázati fejezetben, számokkal. Moralizálás nincs.
6. **Ismeretelméleti címke** minden nem triviális állításon: mért / következtetett / becsült / nem ellenőrzött.
7. **Duplikáció tilos:** egy forrás egy tétel, a változatok csoporttal (`group`).

---

## 4. Minőségkapu (mint a blackout-kiadásnál)

- **Független átnézők:**
  1. kvant-kutató;
  2. MT5/végrehajtási mérnök;
  3. adatbeszerző/infrastruktúra;
  4. kockázatkezelő/jogász;
  5. a fejlesztőcsapat (átadhatóság);
  6. AI-ágens, amely a promptból és a letöltő szkriptből ténylegesen fel tud-e építeni egy működő prototípust.
- **Feltétel:** minden terület ≥ 90, átlag ≥ 95. Ha forráskorlát miatt nem érhető el, azt nyíltan jelölni; forrást kitalálni tilos.
- **Állapot mentése** `.allapot/ALLAPOT.md`-be minden lépés után (kompaktálás elleni védelem).

---

## 5. Kutatási felosztás (párhuzamos ágensek)

| # | Ágens | Modulok | Kimenet |
|---|---|---|---|
| 1 | FX/CFD/MT5/brókerek/részvény-adat | M1, M6 | `research/a1_market_exec.jsonl` |
| 2 | Kripto (CEX, DEX, on-chain) | M1, M6, M8 kripto-rész | `research/a2_crypto.jsonl` |
| 3 | Predikciós piacok + sportfogadás | M5 | `research/a3_predict_sports.jsonl` |
| 4 | Makró, statisztika, hírek, alternatív adat, magyar források | M2, M3, M4 | `research/a4_macro_news_alt.jsonl` |
| 5 | Nyílt szoftver: backtest, végrehajtás, adatbázis, ML/idősor-alapmodellek | M7, M14 eszközei | `research/a5_oss.jsonl` |
| 6 | AI-kereskedési kutatás, LLM-ágensek, ensemble/súlyozás, validálás, irodalom, benchmark-platformok | M9, M12, M13 | `research/a6_ai_research.jsonl` |
| 7 | Stratégiák + kockázati matek + hipotézisgyár | M8, M10, M15 | `research/a7_strategies.jsonl` + `research/a7_ideas.jsonl` |
| 8 | Infrastruktúra, szerverhelyek, hardver, költözés, adó, szabályozás | M11, M10 jogi rész | `research/a8_infra_legal.jsonl` |
| 9 | Platform-architektúra, AI-fejlesztési folyamat, „mozgatókar”, paritásmátrix | M12, M14, M9 | `research/a9_platform.jsonl` + `research/a9_spec.md` |
| 11 | Platform- és bróker-összehasonlítás (van-e jobb, mint az MT5/Vantage) | M6, M11 | `research/a11_platforms.jsonl` + `research/a11_matrix.md` |
| 10 | Bevált módszerek: statisztikai összefüggésekből értelem és eredmény (esettanulmányok + módszertár) | M16 | `research/a10_methods.jsonl` + `research/a10_summary.md` |
