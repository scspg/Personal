# A5 – Nyílt szoftver (M7, M14 és a többi modul eszközei) – összefoglaló

Ellenőrzés napja: 2026-11-15. Tételek: 277 (`a5_oss.jsonl`). Ebből 234 GitHub-repó, 36 Hugging Face modell/adathalmaz, 7 nem GitHub-tétel (MetaTrader5 PyPI, MT5 Strategy Tester, MQL5 Algo Forge, VectorBT PRO, MLFinLab, TimeGPT, kdb+).
Mérési módszer: a csillagszám az ecosyste.ms GitHub-tükörből jön (ha 2026-10-01 után szinkronizált), különben a deps.dev-ből vagy a GitHub-oldalról (WebFetch). Az utolsó commit a `git clone --depth 1` alapértelmezett ágának committer-dátuma. A licencet a LICENSE fájl szövegéből olvastam ki minden olyan esetben, ahol az API „non-standard” értéket adott. A HF-adatok a huggingface.co/api-ból származnak. 12 tétel „becsült”, mert régi a tükör-szinkronja vagy nincs nyilvános ár.

## Ajánlott stack MT5-központú meta-platformhoz (következtetett)

**1. Végrehajtási él (Windows VPS vagy Docker+Wine)**
- MT5 terminál + **MQL5 EA** mint „buta végrehajtó”. Kockázati kill switch és napi veszteséglimit az EA-ban is legyen, ne csak kívül.
- Kiinduló váz: EA31337-classes (GPL!) vagy saját sablon (EarnForex MT5 EA Template).
- Híd:
  - **mql-zmq + libzmq/pyzmq**: alacsony késleltetés, de DLL-import kell.
  - **MetaTrader5 Python csomag** (5.0.6231, csak win_amd64): polling, egyszerűbb.
- Linux-oldali kutatás/döntés: **mt5linux** (RPyC) vagy a **gmag11 MetaTrader5-Docker-Image**. Az RPyC-port távoli kódfuttatást enged, ezért csak belső hálón vagy tűzfal mögött legyen.
- Verziókezelés: **MQL5 Algo Forge** (Forgejo), tükrözve saját Git-be. Titkok: **OpenBao** + **gitleaks** pre-commit.

**2. Eseménymag és busz**
- **NautilusTrader** (Rust mag, LGPL-3.0) mint eseményvezérelt mag és backtest/élő paritás, saját MT5-adapterrel (ZeroMQ-n). Alternatíva: LEAN (C#), ha a csapat .NET-es.
- Modulok közötti busz: **NATS** (JetStream).
- Állapot és limitek: **Valkey**.

**3. Kutatás és backtest**
- Gyors paraméter-rács grid/martingale-hez: **vectorbt** (Commons Clause!) vagy a **VectorBT PRO** ($25/hó, mért).
- Végső validáció: **MT5 Strategy Tester**, valós-tick módban, Vantage-specifikációkkal.
- Mikrostruktúra és market making: **hftbacktest**.
- Szintetikus piacok: ABIDES (archivált, de használható), TimeGAN és Diffusion-TS (kutatási kód).

**4. Validálás (overfitting ellen)**
- CPCV és walk-forward: **skfolio**.
- Hansen SPA, StepM, MCS, stationary/block bootstrap: **arch**.
- PBO, DSR: **pypbo** (AGPL).
- Optimalizálás: **Optuna**, minden próba naplózva.
- Az MLFinLab fizetős lett (£100+ÁFA/hó). A nyilvános GitHub-repó 2021 óta áll és nem nyílt licencű. Kiváltja a RiskLabAI.py (BSD, de kicsi) és saját kód.

**5. Adat és tárolás**
- Tickgyűjtés élőben: **QuestDB**.
- Tömeges elemzés: **ClickHouse**.
- Kutatói adattó: **Parquet + DuckDB + Polars + Arrow**, verziózva **ArcticDB**-vel (BSL 1.1: saját használat megengedett, DBaaS-ként tilos) vagy Iceberggel.
- Ingyenes FX-tick: **dukascopy-node** (ÁSZF: nem terjeszthető). Broker-specifikus spreadet csak az MT5-exportból kapunk.
- A kdb+ ára nem publikus, a Personal Edition nem kereskedelmi célú. A mi léptékünkön QuestDB + ClickHouse kiváltja (következtetett).

**6. Modellek**
- **LightGBM** és **StatsForecast** baseline-ok, **Darts** / **NeuralForecast**.
- Rezsim: ruptures, hmmlearn. Online súlyozás: **River**. Bizonytalansági sávok: **MAPIE**.
- TS-alapmodellek feature-ként, nem önálló jelként:
  - **Chronos-2** (Apache-2.0, 119M paraméter, 7,85M letöltés/hó);
  - **TimesFM 2.5** (Apache-2.0, 231M);
  - **Granite TTM** (805K, gyors);
  - **Kronos** (MIT, pénzügyi OHLCV; a ~47k csillag hype, nem bizonyíték).
- A Moirai súlyai CC-BY-NC-4.0 licencűek, kereskedelmi célra ne.

**7. MLOps és megfigyelés**
- **MLflow** (regiszter), **Feast** (point-in-time feature-ök), **Dagster** vagy **Prefect**.
- **Prometheus + Grafana + Loki** (a Grafana és a Loki AGPL), OpenTelemetry a jel → megbízás → fill késleltetés méréséhez, Evidently a drift figyelésére.

**8. Felület**
- **TradingView Lightweight Charts** (kötelező attribúció + link), **FINOS Perspective** élő blotterhez, **Streamlit** jóváhagyási kapuhoz.

**9. Fejlesztés**
- **uv** (lockfile), **Ruff**, **Hypothesis** (property-based testing a margin-, lot- és order-állapotgép invariánsaira), gitleaks/TruffleHog.

## Licenc- és megbízhatósági figyelmeztetések (mért)

- **Nem nyílt licenc**, bár a GitHubon nyitott repónak látszik:
  - StockSharp: Custom License;
  - rateslib: „not open source”;
  - pymt5adapter: „All rights reserved”;
  - MetaApi SDK;
  - mlfinlab.
- **Commons Clause**: vectorbt, PyBroker.
- **BSL**: ArcticDB, Pathway, Redpanda.
- **Nem kereskedelmi (NC) licencű súlyok vagy adatok**:
  - Moirai;
  - ProsusAI/finbert HF-kártya: 2026-ban cc-by-nc-sa-4.0;
  - Financial PhraseBank, FinanceBench.
- **Elérhetetlen vagy archivált repók**:
  - pandas-ta: a GitHub-repó 2026-11-15-én nem érhető el, a PyPI csomag megvan, ez ellátásilánc-kockázat;
  - archivált: khramkov/MQL5-JSON-API (HTTP 451), ib_insync (utódja az ib_async), PyAlgoTrade, ABIDES-JPMC, AutoTrader, Gekko, Zenbot.
- **Inaktív, bár népszerű**: backtrader (utolsó commit 2023-04), Quantopian zipline/pyfolio/alphalens/empyrical (helyettük a `-reloaded` forkok).
- **yfinance**: nem hivatalos API, a Yahoo ÁSZF-je miatt kereskedelmi platformba nem építhető.

## Hiányok (gaps)

1. **Nincs érett, nyílt, karbantartott MT5-adapter** a Nautilushoz vagy a LEAN-hez. A meglévő hidak (DWX 2022, mql-zmq 2023) elöregedtek. Saját, tesztelt ZeroMQ/gRPC hidat kell írni, nyugtázott és idempotens üzenetekkel.
2. **Nincs nyílt MT5-tickhű szimulátor.** A Strategy Tester zárt, nem modellezi a slippage-et, a requote-ot és a last look-ot. Saját végrehajtási modellt kell kalibrálni a Vantage valós fill-naplóiból.
3. **Nincs nyílt, aktív implementáció a teljes López de Prado-eszköztárra** (triple barrier, meta-labeling, CPCV, DSR, PBO egy helyen). Az MLFinLab fizetős, a RiskLabAI kicsi, a pypbo AGPL és alig aktív.
4. **Nincs független pénzügyi benchmark a TS-alapmodellekre.** A GIFT-Eval és társai nem pénzügyi hozamokat mérnek. Saját FX/CFD walk-forward benchmark kell, naiv random walk baseline-nal.
5. **MQL5 ML-futtatás.** A MALE5 kicsi, az ONNX-út MT5-ben dokumentálatlan nyílt példákban. Nincs nyílt, MQL5 ↔ Python paritástesztelt indikátorkönyvtár: a TA-Lib és az MT5 bemelegedési szakasza eltér.
6. **Nincs nyílt, Aladdin-szerű, kis számlára méretezett kockázati motor.** Az ORE intézményi léptékű. A margin/stop-out 1:500-as modellje saját fejlesztés.
7. **Ellenőrizetlen, további kutatást igénylő pontok**:
   - a Jesse élő moduljának ára;
   - a TimeGPT jelenlegi publikus árlistája (most csak Enterprise);
   - a KDB-X Community Edition feltételei;
   - a W&B csapatár;
   - a vn.py és a StockSharp MT5-konnektorainak állapota.
