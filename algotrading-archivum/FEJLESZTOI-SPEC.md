# A9 – Fejlesztői specifikáció: platform-architektúra, AI-fejlesztési folyamat, mozgatókar, paritásmátrix

> Kutatóágens: A9 · Dátum: 2026-11-15 · Modulok: M9 (döntési réteg, mozgatókar), M12 (paritásmátrix), M14 (AI-jal fejlesztett szoftver)
> Katalógus: `research/a9_platform.jsonl` (118 tétel). A szövegben a `[tétel-id]` jelölés a katalógus `id` mezőjére mutat.
> Ismeretelméleti címkék: **(mért)** = az oldalon vagy API-n láttuk 2026-11-15-én; **(köv.)** = következtetett; **(becs.)** = becsült; **(n.e.)** = nem ellenőrzött.
> Árfolyam az EUR-átszámításhoz: ECB referencia 2026-11-13, 1 EUR = 1,1052 USD (mért).

---

## 0. Cél és hatókör

A dokumentum azt írja le, mit épít a fejlesztőcsapat (AI-kódolóágensekkel), milyen sorrendben, és mivel bizonyítja, hogy kész.

Kiinduló helyzet: egy grid-stratégia fut egy bérelt szerveren MetaTraderen, Vantage-számlán, 1:500 tőkeáttétellel. A célrendszer:

1. **eseményvezérelt, determinisztikusan visszajátszható mag** (backtest és élő ugyanazon a kódúton);
2. **Python-oldali „agy”**, az MT5-terminálban futó **vékony EA-végrehajtóval**;
3. **súlyozott, többmodelles döntési réteg** ördögügyvéd-ágenssel;
4. **kockázati motor és OMS**, amely minden döntés és a bróker között áll;
5. **„AI mozgatókar”**: fokozatos autonómia, kill switch, limitek, auditnapló, promptinjekció elleni védelem;
6. **beállítás-könyvtár**: sémával, verziózással, kísérletkövetéssel és a keresés túlillesztése elleni kapukkal.

Nem cél: HFT/colocation szintű késleltetés, vagyonkezelési ügyfélriportok, magánpiaci modulok.

**Tervezési alapelvek**
- **Egy igazságforrás az állapotra:** az eseménynapló (event sourcing [fowler-event-sourcing]). Minden állapot (pozíció, megbízás, súly, mozgatókar-szint) eseményekből áll elő.
- **Egyszálú, determinisztikus mag:** ugyanaz az elv, mint az LMAX BLP-nél (egy szálon 6 millió megbízás/s, memóriában, event sourcinggal (mért) [fowler-lmax-architecture]) és a NautilusTradernél (egyszálú üzenetfeldolgozás, crash-only (mért) [nautilustrader-architecture]).
- **Fail-closed:** ha bármely kapu (policy, kockázat, adatfrissesség, híd-heartbeat) nem válaszol, a rendszer nem köt.
- **Az LLM soha nem ad közvetlenül megbízást.** Csak sémához kötött szavazatot ad, amelyet determinisztikus kód ellenőriz.

---

## 1. Rendszerarchitektúra

### 1.1 Áttekintő ábra

```mermaid
flowchart LR
  subgraph SRC[Adatforrások]
    MT5T[MT5 terminál tick/bar<br/>Vantage feed]
    REF[Referencia-feedek<br/>Dukascopy, TrueFX - A1]
    NEWS[Hírek, naptár, makró - A4]
    PRED[Predikciós piacok - A3]
  end
  subgraph LAKE[Adattó]
    RAW[(raw/ Parquet<br/>változatlan)]
    CLEAN[(clean/ Iceberg vagy ArcticDB<br/>Pandera-kapu)]
    FS[(Feature store<br/>Feast offline + online)]
  end
  subgraph CORE[Eseménymag - egyszálú]
    BUS{{NATS JetStream busz}}
    DEC[Döntési réteg<br/>szavazók + aggregátor]
    DA[Ördögügyvéd]
    SIZ[Pozícióméretező]
    RISK[Kockázati motor<br/>pre-trade]
    POL[Policy-motor OPA<br/>mozgatókar-szint]
    OMS[OMS állapotgép]
  end
  subgraph EXE[Végrehajtás]
    BR[Híd-adapter<br/>ZeroMQ vagy TCP]
    EA[Vékony EA MQL5<br/>OrderCheck + OrderSend]
  end
  subgraph OPS[Üzemeltetés]
    AUD[(Auditnapló<br/>hash-lánc / immudb)]
    OBS[Prometheus, Loki, OTel<br/>Grafana, Alertmanager]
    HITL[Jóváhagyás: Telegram bot]
    KS[Kill switch x3 út]
    REG[(MLflow regiszter)]
  end
  MT5T --> RAW
  REF --> RAW
  NEWS --> RAW
  PRED --> RAW
  RAW --> CLEAN --> FS --> DEC
  MT5T -- élő tick --> BUS
  BUS --> DEC --> DA --> SIZ --> RISK --> POL --> OMS --> BR --> EA
  EA -- végrehajtási jelentés --> BR --> OMS
  REG --> DEC
  POL <--> HITL
  KS --> OMS
  KS --> EA
  CORE --> AUD
  CORE --> OBS
```

### 1.2 Modulok és felelősségek

| Modul | Felelősség | Nyelv | Fő eszköz / tétel |
|---|---|---|---|
| `atp.data` | ingest, normalizálás, szerződés-validálás, snapshot | Python | Pandera [pandera], Iceberg [apache-iceberg], ArcticDB [arcticdb] |
| `atp.features` | feature-definíciók, point-in-time join | Python | Feast [feast] |
| `atp.core` | eseményhurok, óra (sim/élő), busz-absztrakció | Python, később Rust | NATS [nats], NautilusTrader-minta [nautilustrader-architecture] |
| `atp.decision` | szavazók, aggregátor, kalibráció, ördögügyvéd | Python | River [river], MAPIE [mapie], scikit-learn [sklearn-calibration] |
| `atp.sizing` | méretezés (vol-target, frakcionális Kelly), szorzók | Python | – |
| `atp.risk` | pre-trade és post-trade kontrollok, margin-szimuláció | Python | RTS 6 15. cikk minta [eu-rts6-2017-589] |
| `atp.oms` | megbízás-állapotgép, FIX-szemantika, egyeztetés | Python | FIX [fix-protocol] |
| `atp.bridge` | MT5-híd (ZeroMQ/TCP), heartbeat, újracsatlakozás | Python + MQL5 | pyzmq [pyzmq], mql-zmq [mql-zmq], SocketCreate [mql5-socketcreate] |
| `atp.governance` | mozgatókar-szint, policy, HITL, kill switch | Python + Rego | OPA [opa], OpenFeature [openfeature], Telegram [telegram-bot-api] |
| `atp.audit` | hash-láncolt auditnapló, napi horgony | Python | immudb [immudb] |
| `atp.config` | séma, kompozíció, verziózás | Python | Hydra [hydra], pydantic-settings [pydantic-settings], JSON Schema [json-schema] |
| `atp.research` | backtest, keresés, validálás, regiszter-promóció | Python | Optuna [optuna], MLflow [mlflow-registry], pypbo [pypbo] |
| `atp.obs` | metrikák, trace, LLM-trace | Python | Prometheus [prometheus], OTel [opentelemetry], Langfuse [langfuse] |

> Csomagnév: `atp` (algotrading platform). Ne legyen `platform`, mert az ütközik a Python standard könyvtárával. (köv.)

### 1.3 Adattó-rétegek

```mermaid
flowchart TB
  A[raw/ forrás=x/dt=YYYY-MM-DD/*.parquet<br/>append-only, forrás-hash] -->|Pandera-szerződés| B[clean/ Iceberg-tábla<br/>snapshot_id, séma-verzió]
  B -->|feature_view definíciók| C[features/ Feast offline<br/>point-in-time join]
  C -->|materialize| D[online store<br/>Redis vagy SQLite]
  B --> E[research/ backtest-bemenet<br/>snapshot_id rögzítve]
  E --> F[MLflow run<br/>params + data_snapshot + git_sha]
```

Szabály: **minden backtest-futás rögzíti a `data_snapshot_id`, `config_hash` és `git_sha` hármast.** E nélkül a modell nem regisztrálható (CI-kapu).

### 1.4 Egy döntés útja (szekvencia)

```mermaid
sequenceDiagram
  participant EA as EA (MT5)
  participant BR as Híd
  participant CORE as Mag
  participant V as Szavazók
  participant DA as Ördögügyvéd
  participant R as Kockázat
  participant P as Policy/HITL
  participant O as OMS
  participant A as Audit
  EA->>BR: TICK{sym,bid,ask,ts_srv,seq}
  BR->>CORE: MarketEvent
  CORE->>V: features(t)
  V-->>CORE: Vote[] (p, conf, horizon)
  CORE->>DA: Proposal
  DA-->>CORE: Critique{veto?, reasons, conf_mult}
  CORE->>R: SizedProposal
  R-->>CORE: RiskDecision{approve|reject, codes}
  CORE->>P: OrderIntent + szint
  P-->>CORE: allow | need_approval | deny
  CORE->>O: OrderIntent (ha allow)
  O->>BR: NEW_ORDER{client_id,...}
  BR->>EA: NEW_ORDER
  EA->>EA: OrderCheck() majd OrderSend()
  EA-->>BR: EXEC_REPORT{retcode, deal, price}
  BR-->>O: ExecutionReport
  CORE->>A: minden lépés AuditEvent
```

---

## 2. MT5-integrációs utak

| Út | Leírás | Előny | Hátrány | Ítélet |
|---|---|---|---|---|
| A. Tiszta EA | minden logika MQL5-ben | legkisebb késleltetés, MetaQuotes VPS-en is fut | ML/LLM, adattó és tesztelés nehéz; AI-generált MQL5 hibaérzékeny | csak a vészhelyzeti védőlogika maradjon itt |
| **B. Vékony EA + Python-agy (ZeroMQ vagy natív TCP)** | az EA I/O: tick-küldés, parancs-végrehajtás, helyi védőkorlátok | teljes Python-ökoszisztéma; az EA kicsi és tesztelhető | extra hop (ms-nagyságrend, becs.); a híd hibakezelése kritikus | **ajánlott** |
| C. MetaTrader5 Python csomag | IPC a futó terminálhoz [mt5-python-package] | hivatalos, egyszerű; `order_check`/`order_send` elérhető (mért) | csak `win_amd64` wheel (mért); Linuxon Wine-Python vagy RPyC [mt5linux]; polling-alapú | kiegészítő: történeti letöltés, egyeztetés |
| D. Manager/Gateway/Server API | brókeroldali API-k [mt5-broker-apis], [mt5manager-pypi] | szerveroldali hozzáférés | **retail ügyfélnek nem elérhető** (köv.: csak a bróker szerveréhez) | nem releváns |
| E. Linux/Wine üzem | hivatalos `mt5linux.sh` szkript (mért) [mt5-linux-wine], Docker-image [mt5-docker-gmag11] | egy gépen a Python-stack mellett | Wine-frissítés törhet; headless kijelzőhöz Xvfb/VNC kell | elfogadható; a terminál-verziót rögzíteni |

### 2.1 Híd-protokoll (B út)

Transzport: két csatorna. **Adat:** PUB/SUB vagy TCP stream. **Parancs:** REQ/REP időkorláttal, vagy DEALER/ROUTER. Keretezés: hosszelőtagos JSON (UTF-8). Az MQL5-oldalon nincs protobuf, ezért JSON.

| Üzenet | Irány | Mezők |
|---|---|---|
| `HELLO` | EA→Py | `ea_version`, `terminal_build`, `account_login_hash`, `server`, `symbols[]` |
| `TICK` | EA→Py | `seq`, `sym`, `bid`, `ask`, `last`, `vol`, `ts_srv_ms`, `ts_local_ms` |
| `HEARTBEAT` | kétirányú | `seq`, `ts`, `mode` (`NORMAL`/`SAFE`) |
| `NEW_ORDER` | Py→EA | `client_order_id` (UUIDv7), `sym`, `side`, `type`, `volume`, `price`, `sl`, `tp`, `deviation_pts`, `filling`, `magic`, `expires_ms`, `intent_hash` |
| `CANCEL` / `MODIFY` / `CLOSE` | Py→EA | `client_order_id` vagy `ticket`, … |
| `EXEC_REPORT` | EA→Py | `client_order_id`, `retcode`, `retcode_ext`, `order`, `deal`, `price`, `volume`, `comment`, `ts_srv_ms` |
| `POSITIONS` | EA→Py | pillanatkép az egyeztetéshez (1–5 s-onként) |
| `KILL` | Py→EA vagy helyi | `scope` (`ALL`/`SYMBOL`/`MAGIC`), `close_positions` (bool), `reason` |

**Az EA helyi védőkorlátai** (a Pythontól függetlenül, MQL5 inputokból):
- `MaxLotPerOrder`, `MaxOpenLots`, `MaxOrdersPerMinute`, `MinMarginLevelPct`, `MaxSpreadPts`;
- heartbeat-időtúllépés (pl. 5 s) esetén `SAFE` mód: nincs új megbízás, függő megbízások törlése, a pozíciók zárása konfigurálható;
- duplikátum-szűrés `client_order_id` alapján (idempotencia);
- `expires_ms` lejárt parancs nem hajtható végre.

### 2.2 MQL5 kódgenerálási buktatók (AI-ágenseknek kötelező ellenőrzőlista)

1. `OrderSend` visszatérési értéke mellett **mindig** a `MqlTradeResult.retcode`-ot kell vizsgálni [mql5-trade-return-codes]. A requote és az árváltozás korlátos számú újrapróbálást kap.
2. A filling mode szimbólumonként eltér: `SYMBOL_FILLING_MODE` alapján kell választani, nem fixen FOK-ot [mql5-ordercheck].
3. A `OrderCheck()` minden küldés előtt fut, a margin-ellenőrzéssel együtt.
4. Netting és hedging számlatípus eltérő pozíciókezelést kíván (`ACCOUNT_MARGIN_MODE`). (köv.)
5. A `volume` normalizálása: `SYMBOL_VOLUME_MIN`, `SYMBOL_VOLUME_STEP`, `SYMBOL_VOLUME_MAX`. Az árak normalizálása: `SYMBOL_DIGITS`, `SYMBOL_TRADE_TICK_SIZE`. A stop-szint: `SYMBOL_TRADE_STOPS_LEVEL`, `SYMBOL_TRADE_FREEZE_LEVEL`.
6. Az MQL5 időkezelése: `TimeCurrent()` a szerveridő, `TimeLocal()` a helyi idő. Minden üzenetben mindkettő szerepel.
7. Globális változók és statikus állapot újrainicializálódik időkeret-váltáskor és újrafordításkor (az `OnInit`/`OnDeinit` reason kódjait kezelni kell) (https://www.mql5.com/en/docs/runtime/running).
8. DLL-import (ZeroMQ) a terminálbeállításokban engedélyezendő; a MetaQuotes VPS-en ez korlátozott lehet (n.e.). Alternatíva a natív `SocketCreate` [mql5-socketcreate].
9. Az AI hajlamos nem létező MQL5-függvényeket vagy MQL4-szintaxist (`OrderSend` MQL4-paraméterekkel) generálni. A CI-ben a MetaEditor parancssori fordítója fut (Wine alatt), figyelmeztetés = hiba. (köv., a pontos CLI-kapcsolók n.e.)
10. Strategy Testerben a hálózati függvények korlátozottak (n.e.). Az EA-nak ezért van egy `BacktestStub` módja, amelyben a döntés egy előre generált jelfájlból jön.

---

## 3. Modulinterfészek

A szerződések Python `Protocol`-ok és Pydantic-modellek. Az üzenetek JSON Schema-exportja a `schemas/` mappában verziózott. Breaking change MAJOR verzióemelést kíván [semver].

```python
# atp/contracts.py  (kivonat)
from typing import Protocol, Literal, Sequence
from pydantic import BaseModel, Field
from datetime import datetime

Side = Literal["buy", "sell"]

class Vote(BaseModel):
    voter_id: str                 # pl. "stat.ou_meanrev.v3"
    voter_kind: Literal["stat", "ml", "llm", "rule"]
    symbol: str
    horizon_s: int                # a címke-horizont (triple-barrier)
    p_up: float = Field(ge=0, le=1)       # kalibrált valószínűség
    exp_ret_bps: float | None = None
    interval_bps: tuple[float, float] | None = None   # konformális sáv
    confidence: float = Field(ge=0, le=1)
    features_ref: str             # feature-snapshot azonosító
    model_version: str            # MLflow modell@alias -> verzió
    rationale: str | None = None  # csak naplózásra; döntés NEM épülhet rá
    taint: Literal["trusted", "untrusted_text"] = "trusted"
    ts: datetime

class Proposal(BaseModel):
    proposal_id: str
    origin: Literal["ensemble", "user", "ai_agent"]
    symbol: str
    side: Side
    p_ens: float
    disagreement: float           # súlyozott logit-szórás
    votes: Sequence[Vote]

class Critique(BaseModel):
    proposal_id: str
    veto: bool
    veto_codes: list[str]         # pl. ["CALIB_DEGRADED","EVENT_WINDOW"]
    counter_args: list[str]
    conf_mult: float = Field(ge=0, le=1)  # méretszorzó

class SizedProposal(BaseModel):
    proposal: Proposal
    critique: Critique
    volume_lots: float
    sl: float | None
    tp: float | None
    sizing_trace: dict            # minden szorzó naplózva

class RiskDecision(BaseModel):
    approve: bool
    codes: list[str]              # pl. ["MAX_EXPOSURE","DAILY_LOSS","SPREAD"]
    post_trade_margin_level: float
    worst_case_loss_ccy: float

class OrderIntent(BaseModel):
    client_order_id: str          # UUIDv7
    symbol: str; side: Side
    type: Literal["market", "limit", "stop"]
    volume: float; price: float | None
    sl: float | None; tp: float | None
    autonomy_level: int           # 0..4
    intent_hash: str              # sha256(kanonikus JSON)

class Voter(Protocol):
    id: str
    def vote(self, symbol: str, t: datetime, features: dict) -> Vote | None: ...

class Aggregator(Protocol):
    def combine(self, votes: Sequence[Vote]) -> Proposal | None: ...
    def update(self, voter_id: str, loss: float, t: datetime) -> None: ...

class DevilsAdvocate(Protocol):
    def critique(self, p: Proposal, ctx: "RiskContext") -> Critique: ...

class Sizer(Protocol):
    def size(self, p: Proposal, c: Critique, ctx: "RiskContext") -> SizedProposal: ...

class RiskEngine(Protocol):
    def pre_trade(self, s: SizedProposal) -> RiskDecision: ...
    def on_fill(self, r: "ExecutionReport") -> None: ...

class PolicyEngine(Protocol):
    def evaluate(self, intent: OrderIntent, ctx: dict) -> Literal["allow", "need_approval", "deny"]: ...

class ExecutionAdapter(Protocol):
    def submit(self, intent: OrderIntent) -> None: ...
    def cancel_all(self, scope: str) -> None: ...
    def positions(self) -> list[dict]: ...

class AuditLog(Protocol):
    def append(self, event: "AuditEvent") -> str: ...   # visszaadja az új hash-t
    def verify(self, from_seq: int = 0) -> bool: ...
```

### 3.1 OMS-állapotgép

```mermaid
stateDiagram-v2
  [*] --> PendingNew: OrderIntent elfogadva
  PendingNew --> Rejected: retcode hiba / risk / policy deny
  PendingNew --> New: EA nyugtázta
  New --> PartiallyFilled
  New --> Filled
  PartiallyFilled --> Filled
  New --> PendingCancel: cancel
  PendingCancel --> Cancelled
  New --> Expired: expires_ms
  PendingNew --> Unknown: időtúllépés
  Unknown --> New: egyeztetés talált
  Unknown --> Rejected: egyeztetés nem talált
  Filled --> [*]
  Cancelled --> [*]
  Rejected --> [*]
```

Az `Unknown` állapot kötelező. Időtúllépés után **nem küldünk újra**, hanem a `POSITIONS`/history alapján egyeztetünk. Ez a dupla kötés elleni védelem.

### 3.2 Adatsémák

**Tick (clean)**

| Mező | Típus | Szabály (Pandera) |
|---|---|---|
| `ts_srv` | timestamp[ns, UTC] | szimbólumonként szigorúan nő, vagy azonos `seq`-kel |
| `symbol` | string | a szimbólum-referenciatáblában létezik |
| `bid`, `ask` | float64 | `0 < bid <= ask`; `(ask-bid)/mid < 0.01` (FX), egyébként flag |
| `source` | enum | `mt5_vantage`, `dukascopy`, `truefx`, … |
| `ingest_id` | string | a raw-fájl sha256-ja |

**AuditEvent**

| Mező | Típus | Megjegyzés |
|---|---|---|
| `seq` | int64 | monoton |
| `ts` | timestamp UTC | |
| `actor` | enum | `system`, `voter:<id>`, `devil`, `risk`, `policy`, `human:<user>`, `ea` |
| `type` | enum | `VOTE`, `PROPOSAL`, `CRITIQUE`, `RISK`, `POLICY`, `APPROVAL`, `ORDER`, `EXEC`, `KILL`, `LEVEL_CHANGE`, `CONFIG_CHANGE` |
| `payload` | JSON | kanonikus JSON (rendezett kulcsok) |
| `prev_hash` | hex | az előző esemény hash-e |
| `hash` | hex | `sha256(prev_hash ‖ canonical(payload) ‖ seq ‖ ts)` |

Napi horgony: a nap utolsó hash-ét egy független helyre írjuk (pl. aláírt git-tag vagy e-mail). Az immudb [immudb] ennek kiváltója lehet.

**ExperimentRun (MLflow-tag-ek, kötelező)**: `git_sha`, `config_hash`, `config_semver`, `data_snapshot_id`, `search_study_id`, `n_trials_in_study`, `cv_scheme`, `dsr`, `pbo`, `oos_window`.

---

## 4. Döntési réteg (M9) – mérnöki terv

### 4.1 Komponensek

```mermaid
flowchart TB
  F[Feature-snapshot t] --> S1[Statisztikai szavazók<br/>OU mean-rev, Kalman pár, vol-rezsim HMM]
  F --> S2[ML-szavazók<br/>GBM, idősoros alapmodell - A5/A6]
  N[Hír/makró szöveg<br/>UNTRUSTED] --> Q[Karantén-LLM<br/>csak olvas, nincs eszköze]
  Q -->|séma-JSON: esemény, irány, bizonyosság, forrás-ID| S3[LLM-szavazó<br/>determinisztikus átalakító]
  S1 & S2 & S3 --> CAL[Szavazónkénti kalibráció<br/>isotonic/Platt, rolling]
  CAL --> AGG[Aggregátor<br/>logit-pooling + Hedge/fixed-share súlyok]
  AGG --> ECAL[Ensemble-kalibráció + konformális sáv]
  ECAL --> DA[Ördögügyvéd<br/>szabálykészlet + LLM-kritikus]
  DA --> SZ[Méretező hook]
  SZ --> RISK[Kockázati motor]
  LBL[Lezárt címkék t-h] --> UPD[Online súlyfrissítés] --> AGG
```

### 4.2 Szavazók

- **Statisztikai:** paraméteres modellek explicit feltételezésekkel. Mindegyik `p_up`-ot ad a horizontra (pl. z-score → logisztikus leképezés, majd kalibráció).
- **ML:** az MLflow-regiszterből `@champion` aliasszal töltve [mlflow-registry]. A `@challenger` árnyékban fut, súlyt nem kap, csak pontozzuk.
- **LLM:** a Dual LLM minta szerint [dual-llm-pattern]. A karanténba zárt LLM a szöveget fix JSON-sémába alakítja (`event_type`, `direction`, `certainty`, `source_ids[]`, `published_ts`). A szavazót **determinisztikus** kód képzi ebből. A `rationale` szabad szöveg csak naplózásra szolgál, a döntés nem épülhet rá. A szavazat `taint="untrusted_text"` jelölést kap.
- **Szabály (rule):** például „nincs új grid-szint magas hatású hír előtt ±N perccel”.

### 4.3 Aggregálás

Logit-pooling súlyokkal:

`ℓ_ens = Σ_i w_i · logit(p_i)` ; `p_ens = σ(ℓ_ens)` ; `D = sqrt(Σ_i w_i (logit p_i − ℓ_ens)²)` (egyet nem értés).

Indoklás: a logit-pooling jobban kezeli a magabiztos, de ritka jeleket, mint a lineáris átlag. A súlyok a 4.4 szerint frissülnek. Alternatíva a stacking meta-learner (purged CV-vel tanítva). A két változatot a backtest-kapu dönti el. (köv.)

### 4.4 Online súlyfrissítés (Hedge + fixed share)

Késleltetett visszajelzés: az `i` szavazó `t`-kori szavazatának vesztesége a `t+h` horizont lezárultakor számolható.

1. Veszteség: `L_i = −[y log p_i + (1−y) log(1−p_i)]` (log-loss, kalibrált `p`-n). Opcionálisan a költséggel súlyozott irány-hasznosság.
2. Multiplikatív lépés: `w̃_i = w_i · exp(−η · L_i)`.
3. Fixed share keverés a rezsimváltáshoz: `w_i ← (1−α)·w̃_i/Σw̃ + α/N`.
4. Korlátok: `w_min ≤ w_i ≤ w_max` (pl. 0,02 és 0,35), majd újranormálás. Az LLM-szavazók összsúlya `≤ w_llm_max` (pl. 0,25) a promptinjekciós felület korlátozására.
5. Hiperparaméterek: `η ∈ [0,05; 1]`, `α ∈ [0; 0,05]`. Ezeket csak a kutatási hangoláson keresztül hangoljuk, a trial-számlálás alatt (6. fejezet).
6. Hideg indítás: új szavazó `w_min`-nel indul, és legalább `n_min` lezárt címke után számít.

Elméleti háttér: Hedge/multiplicative weights és fixed-share (Herbster–Warmuth). A forrásokat az A6 gyűjti, itt nem duplikáljuk. A River könyvtár online eszközei használhatók [river].

**Tulajdonság-tesztek (Hypothesis) [hypothesis]:** `Σw = 1`; minden `w_i ∈ [w_min, w_max]`; azonos veszteségek mellett a súlyok nem változnak; egy domináns szavazó súlya `η·ΔL` arányában monoton nő; NaN-veszteség esetén a súly változatlan, és riasztás megy.

### 4.5 Kalibráció és bizonytalanság

- A szavazónkénti kalibráció rolling ablakon fut, időben a tanító után (purged). Kis mintán Platt, `n > 1000` felett isotonic [sklearn-calibration].
- Ensemble-szinten újrakalibrálunk, és figyeljük a Brier-pontot és az ECE-t (expected calibration error, 10 bin).
- A konformális sáv adaptív idősoros változat (például ACI) [mapie]. Ha a hozam-intervallum tartalmazza a 0-t a költségek után, nincs kötés.

### 4.6 Ördögügyvéd-ágens

Két rétegből áll: (1) **determinisztikus szabálykészlet** (vétójog), (2) **LLM-kritikus**, amely ellenérveket ír, és csak `conf_mult`-ot csökkenthet, vétót nem adhat. Minden javaslatra lefut, az `origin=user` és az `origin=ai_agent` javaslatokra is.

**Kemény vétófeltételek (kód, reason code):**

| Kód | Feltétel (alapértelmezés, konfigurálható) |
|---|---|
| `RISK_LIMIT` | a kockázati motor előzetes szimulációja limitet sért (lásd 5. fejezet) |
| `CALIB_DEGRADED` | az ensemble rolling ECE-je > 0,05, vagy a Brier skill score < 0 az utolsó N=200 lezárt címkén |
| `DATA_STALE` | a tick kora > 2 s, vagy feature-hiány, vagy a Pandera-kapu bukott |
| `UNTRUSTED_SOLE_DRIVER` | a `p_ens` irányát egyedül `untrusted_text` szavazó dönti el (nélküle előjelet váltana) |
| `SINGLE_SOURCE_NEWS` | a hír-alapú szavazat < 2 független forrásra épül |
| `EVENT_WINDOW` | magas hatású naptári esemény ±N perc, és a stratégia nem eseményre minősített |
| `SPREAD_WIDE` | spread > k × szimbólum-medián (rollover, hír) |
| `DISAGREEMENT` | `D` > küszöb (a szavazók erősen ellentmondanak) |
| `REGIME_MISMATCH` | a stratégia rezsim-címkéje ≠ az aktuális rezsim (például trendszűrős grid trendben) |
| `DRIFT` | drift-detektor (ADWIN) jelzett az utolsó X percben |

Ha bármelyik teljesül, `veto=true`. A `RISK_LIMIT` és a `DATA_STALE` vétót **ember sem írhatja felül**. A többit L1–L2 szinten egy ember felülbírálhatja, második megerősítéssel, és ez auditált.

**Puha ellenérv:** az LLM-kritikus kap egy strukturált összefoglalót: a javaslatot, a szavazatokat, a rezsimet, a közelmúlt teljesítményét. Megbízhatatlan szöveget **nem** kap. A kimenete `{counter_args[], severity 0..1}`, amelyből `conf_mult = 1 − 0,5·severity`.

### 4.7 Méretező hook

```
size = min( risk_cap_lots,
            vol_target_lots
            × kelly_frac(p_ens, payoff_b) × λ        # λ = 0,25 frakcionális Kelly
            × calib_mult(ECE)                         # 1 ha ECE<0,02, lineárisan 0-ig 0,05-nél
            × critique.conf_mult
            × (1 − min(1, D / D_max))
            × autonomy_mult(level) )                  # pl. L2: 1, L3: 0,5 az első 30 napban
kelly_frac(p,b) = max(0, p − (1−p)/b)
```

A méretező minden szorzót a `sizing_trace`-be ír. Ha `size < SYMBOL_VOLUME_MIN`, nincs kötés, felfelé kerekítés tilos.

---

## 5. Kockázati motor (pre-trade és post-trade)

Minták: SEC 15c3-5 (előre beállított tőkeküszöbök, hibásnak tűnő megbízások elutasítása (mért)) [sec-15c3-5], RTS 6 12. cikk (kill functionality) és 15. cikk (pre-trade kontrollok (mért)) [eu-rts6-2017-589], FIA 2024 [fia-automated-trading-risk-controls-2024]. Ezek ránk jogilag nem vonatkoznak, mintaként használjuk.

**Pre-trade ellenőrzések (sorrendben, mind kötelező):**
1. Számla- és szimbólum-engedélylista, kereskedési idő (szimbólum-session).
2. Max. megbízásméret (lot), max. nominális érték, árgallér (a limitár ≤ X pont a midtől).
3. Megbízás-ráta (per perc/szimbólum), duplikátum-szűrés (`intent_hash` 60 s-on belül).
4. **Margin-szimuláció 1:500 mellett:** a kötés utáni margin-szint ≥ `min_margin_level_pct` (pl. 300%), a bróker stop-out szintje fölött nagy pufferrel. A stop-out szintet az A1/A8 ellenőrzi.
5. Worst-case veszteség: az SL-ig, gap-forgatókönyvvel (k × ATR, hétvégén nagyobb k), ≤ a napi veszteségkeret maradéka.
6. Teljes nyitott kitettség (lot és nominális), szimbólum- és devizakoncentráció, korrelált klaszter-limit.
7. Grid-specifikus: max. szintszám, max. átlagolási lot-szorzó (martingale-tiltás vagy -plafon), a grid teljes worst-case vesztesége ≤ a keret.
8. Napi veszteséglimit (realizált és nem realizált), heti drawdown-limit, egymást követő veszteségek száma.

**Post-trade:** drop-copy jellegű egyeztetés az MT5 history és az OMS között (1–5 s), slippage-mérés (várt és tényleges ár), fill-arány, requote-arány.

**Kill switch: három független út**
1. **Szoftveres:** az `atp.governance` `KILL` eseményt küld. Az OMS minden függő megbízást töröl, és (konfigurációtól függően) zárja a pozíciókat. A mozgatókar szintje L0-ra áll.
2. **EA-helyi:** heartbeat-kiesés vagy `MinMarginLevelPct` alatt az EA önállóan `SAFE` módba lép (a Pythontól függetlenül).
3. **Ember, sávon kívül:** a Telegram-bot `/kill` parancsa, csak engedélyezett `user_id`-ről [telegram-bot-api]. Tartalékként kézi belépés a terminálba, „AutoTrading” kikapcsolás.

Tanulság a Knight Capital-esetből (mért a SEC-végzésben): kb. 45 perc alatt több millió megbízás ment ki, és több mint 460 millió dollár veszteség keletkezett. Az ok egy régi, aktiválható „Power Peg” kód és egy hiányos deploy volt [knight-capital-sec-order]. Ebből három szabály következik: (a) holt kód és újrahasznosított flag tilos; (b) deploy után automatikus smoke-teszt és kanári (egy szimbólum, minimális lot); (c) automatikus leállás, ha a megbízás-ráta vagy a pozíció a plafont átlépi.

---

## 6. Konfigurációs tér – a „hatalmas beállítás-könyvtár”

### 6.1 Szerkezet

```
conf/
  strategy/   grid_atr.yaml  grid_trendfilter.yaml  meanrev_ou.yaml ...
  risk/       micro_live.yaml  paper.yaml  scale_t1.yaml
  execution/  vantage_mt5_raw.yaml  vantage_mt5_std.yaml
  ensemble/   default.yaml  llm_heavy.yaml
  governance/ L0.yaml ... L4.yaml
  search/     grid_atr_space.yaml
  experiment/ 2026-11-grid-atr-wf.yaml      # kompozíció: defaults lista
```

- Kompozíció és felülírás: Hydra [hydra]. Validálás: Pydantic-modell [pydantic-settings]. Export: JSON Schema [json-schema].
- **Kanonikus hash:** `config_hash = sha256(canonical_json(resolved_config))`. Minden futás, megbízás és auditesemény hordozza.
- **Verziózás:** a stratégia-konfiguráció SemVer szerint verziózott [semver]. MAJOR = viselkedésváltozás (bármely golden-backtest eltérés), és ez új paper-kaput igényel. MINOR = új opcionális paraméter, alapértéke a régi viselkedést adja. PATCH = dokumentáció és metaadat.
- Titok nem kerülhet konfigurációba. A titkok helye a SOPS/OpenBao, `SecretStr` típussal [sops], [openbao].

```python
class GridATRConfig(BaseModel):
    kind: Literal["grid_atr"] = "grid_atr"
    version: str = "1.4.0"
    symbol: str
    atr_period: int = Field(14, ge=5, le=200)
    step_atr_mult: float = Field(1.0, gt=0.1, le=10)
    max_levels: int = Field(6, ge=1, le=20)
    lot_base: float = Field(0.01, gt=0)
    lot_mult: float = Field(1.0, ge=1.0, le=1.5)       # >1 = martingale, plafonozva
    trend_filter: Literal["none", "ema", "adx"] = "ema"
    basket_tp_ccy: float | None = None
    basket_sl_ccy: float                                # kötelező: nincs SL nélküli grid
```

### 6.2 Kísérletkövetés

- MLflow run minden backtestre és keresési trialre [mlflow-registry], a 3.2-ben felsorolt kötelező tag-ekkel.
- Az Optuna-study tárolója RDB (Postgres/SQLite). A study-ID az MLflow-tag része [optuna].
- Adat-verzió: Iceberg/ArcticDB snapshot-ID [apache-iceberg], [arcticdb]. A kisebb, származtatott halmazok DVC-vel verziózhatók [dvc].

### 6.3 Paraméterkeresés

| Módszer | Mikor | Eszköz |
|---|---|---|
| TPE (alapértelmezés) | vegyes, feltételes terek, 50–500 trial | Optuna [optuna] |
| CMA-ES | folytonos, 3–20 dimenzió | Optuna |
| Többcélú NSGA-II | Sharpe és max drawdown, illetve fordulatszám | Optuna |
| GP-alapú Bayes-optimalizálás | drága, zajos kiértékelés (teljes walk-forward), < 100 trial | Ax/BoTorch [ax-platform], [botorch] |
| RF-szurrogát (SMAC) | sok kategorikus/feltételes paraméter | SMAC3 [smac3] |
| Elosztott | több gép/GPU | Ray Tune [ray-tune] |

A célfüggvény **soha nem a nyers in-sample Sharpe**. A célfüggvény: a purged walk-forward fold-ok OOS-metrikáinak mediánja, mínusz büntetés (fordulatszám-költség, paraméter-instabilitás: a fold-ok közti szórás).

### 6.4 A keresés túlillesztése elleni védelem (kötelező kapuk)

1. **Trial-könyvelés:** minden kipróbált konfiguráció (a sikerteleneket is beleértve) bekerül a study-ba. Az `n_trials_in_study` a Deflated Sharpe Ratio bemenete. A DSR-t és a PBO-t az A6/A7 dokumentálja, itt csak a kaput írjuk elő.
2. **Lezárt holdout:** a legutóbbi időszak (például 6 hónap) a keresés alatt **gépileg elérhetetlen**. Az adatelérési réteg dátum-tiltást alkalmaz `research` szerepkörben. Ezt csak a végső jelöltre, egyszer lehet feloldani, és a feloldás auditesemény.
3. **PBO (CSCV)** a study legjobb N konfigurációján: `PBO < 0,2` [pypbo]. A módszer: Bailey–Borwein–López de Prado–Zhu, J. Comput. Finance 20(4), 2017 (mért a risk.net oldalon).
4. **DSR ≥ 0,95** a teljes trial-szám figyelembevételével. Több-hipotézis küszöb: t > 3 (Harvey–Liu–Zhu, A6 forrása).
5. **Paraméter-stabilitás:** a legjobb pont ±10%-os környezetében az OOS-metrika ≥ a csúcs 70%-a. Csak „fennsíkot” fogadunk el, csúcsot nem.
6. **Keresési költségvetés:** a stratégiánkénti trial-plafon a study indulásakor rögzített, és utólag nem emelhető új study nélkül. Új study esetén a trial-számok összeadódnak a DSR-ben.
7. **Paper-egyezés:** a paper-kereskedés realizált Sharpe-ja és slippage-e a backtest-előrejelzés 1σ-sávján belül van (lásd 9. fejezet, F5).

---

## 7. AI mozgatókar – governance

### 7.1 Jogosultsági szintek

| Szint | Név | Mit tehet az AI | Ember szerepe | Belépési feltétel | Automatikus visszaesés |
|---|---|---|---|---|---|
| L0 | Leállítva | semmit (csak adatgyűjtés) | – | kill vagy indulás | – |
| L1 | Javaslat | javaslatot küld, nem köt | dönt és kézzel köt | F3 kész | – |
| L2 | Jóváhagyással kötés | `OrderIntent`-et készít, amely jóváhagyás után megy ki (TTL 60 s, árelmozdulás-korlát) | jóváhagy vagy elutasít (Telegram) | ≥ 30 nap L1, kalibráció rendben | ECE > 0,05 → L1 |
| L3 | Korlátozott autonómia | önállóan köt a sávon belül (max. lot, napi veszteség, szimbólumlista, időablak); a sávon kívül L2 | napi review, kill | F5 micro-live kapu teljesült | napi veszteséglimit, 3 vétó/óra, drift → L2 vagy L0 |
| L4 | Teljes autonómia | stratégián belül teljes, a kockázati motor keretein belül | heti review, kill | F6 skálázási kapu, ≥ 90 nap L3 | bármely kemény limit → L0 |

- A szintváltás auditesemény (`LEVEL_CHANGE`). **Felfelé csak ember léptethet**, két lépésben: kérés, majd megerősítés más csatornán. **Lefelé automatikusan is** léphet a rendszer.
- A policy deklaratív (Rego, OPA) [opa], verziózott és tesztelt (`opa test`). Ha a policy-motor nem elérhető, a válasz `deny`.

```rego
package atp.autonomy
default decision := "deny"
decision := "allow" if {
  input.level >= 3
  input.intent.volume <= data.limits[input.level].max_lot
  input.ctx.daily_pnl > -data.limits[input.level].daily_loss
  input.intent.symbol in data.limits[input.level].symbols
  not input.ctx.kill_active
}
decision := "need_approval" if {
  input.level == 2
  not input.ctx.kill_active
}
decision := "need_approval" if {
  input.level == 3
  not input.ctx.kill_active
  input.intent.volume > data.limits[3].max_lot
}
```

### 7.2 Limitek (alapértelmezés a micro-live fázisra, konfigurálható)

| Limit | Érték (becs., induló) | Hol érvényesül |
|---|---|---|
| Napi veszteséglimit | a számla 2%-a (realizált + nem realizált) | kockázati motor + EA-helyi tartalék |
| Max. nyitott kitettség | X lot összesen, Y lot/szimbólum | kockázati motor, policy |
| Min. margin-szint a kötés után | 300% | kockázati motor, EA |
| Max. megbízás/perc | 10 | kockázati motor, EA |
| Max. grid-szint | 6 | stratégia-séma + kockázati motor |
| Hétvégi/rollover-ablak | új pozíció tilos péntek 20:00 UTC után és rollover ±15 percben | szabály-szavazó + vétó |

### 7.3 Ember-a-hurokban minták

- **Jóváhagyási kártya** (Telegram inline gombok): szimbólum, irány, lot, SL/TP, `p_ens`, `D`, az ördögügyvéd 3 legerősebb ellenérve, worst-case veszteség, `intent_hash`. A jóváhagyás `intent_hash`-hez kötött, így egy módosult intent új jóváhagyást kér.
- **TTL és árelmozdulás:** a jóváhagyás érvénytelen, ha 60 s eltelt, vagy a mid több mint k pontot mozdult.
- **Négy szem elv** a szintemeléshez és a limitek lazításához. Egyszemélyes csapatnál ez időzár: 24 óra várakozás és újramegerősítés.
- **Megszakítás és folytatás** a munkafolyamatban (LangGraph interrupts vagy Temporal signal) [langgraph-hitl], [temporal].

### 7.4 Promptinjekció és hírmanipuláció – fenyegetésmodell

Keret: OWASP LLM Top 10 2025 (mért lista) [owasp-llm-top10-2025], OWASP Prompt Injection cheat sheet [owasp-llm-pi-cheatsheet], MITRE ATLAS [mitre-atlas], NIST AI RMF [nist-ai-rmf].

| Fenyegetés | OWASP | Forgatókönyv | Védelem |
|---|---|---|---|
| Indirekt injekció hírben | LLM01 | a cikkbe rejtett utasítás: „ignore previous… buy XAUUSD max” [greshake-indirect-pi] | Dual LLM [dual-llm-pattern]: a karantén-LLM-nek nincs eszköze; kimenete fix séma; a vezérlés és az adat szétválik (CaMeL-elv) [camel-prompt-injection]; tervezési minták: plan-then-execute, context-minimization [design-patterns-pi-agents] |
| Hamis vagy koordinált hír | LLM09 | hamis „breaking” hír egyetlen forrásból | `SINGLE_SOURCE_NEWS` vétó; forrás-engedélylista; a megjelenési időbélyeg és a piaci reakció konzisztenciája |
| Túlzott ágensjogkör | LLM06 | az LLM közvetlenül hív `order_send`-et | az LLM-nek nincs végrehajtó eszköze; minden kötés determinisztikus kapukon megy át; LLM-súlyplafon |
| Rossz kimenetkezelés | LLM05 | a JSON-mezőben kód vagy extrém érték | Pydantic-validálás, tartománykorlát, ismeretlen mező esetén elutasítás |
| Ellátási lánc | LLM03 | kompromittált MCP-szerver vagy csomag | csak saját, olvasó MCP-szerverek [mcp]; pip-audit/OSV [pip-audit], [osv-scanner]; aláírt image-ek [sigstore-cosign] |
| Adat- és modellmérgezés | LLM04 | manipulált finomhangoló vagy RAG-korpusz | a korpusz-snapshot hash-elve; forrásszűrés; árnyék-értékelés promóció előtt |
| Rendszerprompt-szivárgás | LLM07 | a prompt limiteket vagy kulcsokat tartalmaz | a promptban nincs titok és nincs limit-érték; a limitek a policy-ben vannak |
| Korlátlan fogyasztás | LLM10 | hírözön miatt költségrobbanás | rate limit, napi tokenkeret, Langfuse-költségriasztás [langfuse] |

**Tesztelés:** a `tests/redteam/` injekciós korpusz (legalább 200 eset: magyar és angol, rejtett HTML, base64, Unicode-trükkök) minden prompt- vagy modellváltásnál lefut promptfoo-val [promptfoo]. Negyedévente garak [garak]. Elvárt eredmény: 0 olyan eset, amelyben a karantén-kimenet sémán kívüli mezőt tartalmaz, vagy a szavazat előjele az injekció hatására megfordul.

---

## 8. AI-jal fejlesztett szoftver – folyamat

### 8.1 Spec-first ciklus

```mermaid
flowchart LR
  S[FEJLESZTOI-SPEC fejezet] --> T[Feladat-bontás<br/>spec-kit: spec, plan, tasks]
  T --> AC[Elfogadási kritériumok<br/>futtatható tesztté írva ELŐSZÖR]
  AC --> IMP[Implementáció kódolóágenssel<br/>kis PR-ek]
  IMP --> CI[CI-kapuk]
  CI -->|zöld| REV[Emberi review<br/>CODEOWNERS a risk/governance/bridge mappákra]
  REV --> MERGE[Merge, aláírt build]
  CI -->|piros| IMP
```

- Sablon: GitHub Spec Kit [github-spec-kit]. Ágens-utasítások: `AGENTS.md` [agents-md] és `CLAUDE.md` [claude-code-best-practices], a biztonsági részhez az OpenSSF útmutatóját használjuk [openssf-ai-code-assistant-guide].
- **Tilos az ágensnek:** a `risk/`, `governance/`, `bridge/ea/` mappákban review nélkül merge-elni; limitértéket módosítani; tesztet törölni vagy gyengíteni; új függőséget az engedélylistán kívül felvenni. Az utolsó azért fontos, mert a modellek nem létező csomagneveket hallucinálnak [package-hallucination-paper].
- Az ágens dolgozhat sandboxban (konténer), demo-számla hitelesítőkkel. **Éles kulcsokat soha nem lát.**

### 8.2 Kódolóágensek és árak (mért, 2026-11-15)

| Eszköz | Típus | Ár (eredeti) | EUR/hó | Tétel |
|---|---|---|---|---|
| Claude Code | terminál/IDE ágens | Pro $20/hó (éves díjjal $17), Max $100, Ultra $200; Team Standard $25/fő (éves $20) | 18,10 (Pro) | [claude-code] |
| OpenAI Codex CLI | terminál ágens, OSS | ChatGPT Plus $20/hó; Pro $100/$200/$500; Business $25/fő (éves $20); API-kulccsal használat alapú | 18,10 (Plus) | [openai-codex-cli] |
| Cursor | agentic IDE | Free; Plus $8 (csak Grok); Premium $30; Super $100; Ultra $200; Teams $30+/fő | 27,14 (Premium) | [cursor] |
| GitHub Copilot | IDE + coding agent | Free; Pro $10; Pro+ $39; Max $100 | 9,05 (Pro) | [github-copilot] |
| OpenHands | OSS autonóm ágens | Agent Canvas ingyenes; Teams $500/hó 10 főig (+$50/fő) | 0 (OSS) | [openhands] |
| Aider | OSS terminál | ingyenes + modell-API költség | 0 + API | [aider] |
| Cline | OSS IDE/CLI | ingyenes + modell-API költség | 0 + API | [cline] |
| Gemini CLI | OSS terminál | n.e. | n.e. | [gemini-cli] |

Ajánlás (köv.): fő ágensnek egy terminál-ágens (Claude Code vagy Codex CLI) hookokkal, amelyek a teszteket és a lintert kikényszerítik. Második ágensnek egy független modellcsalád, amely a review-t végzi (a kódot és a tesztet ne ugyanaz a modell írja és ellenőrizze).

### 8.3 Tesztstratégia

| Szint | Mit | Eszköz | Kapu |
|---|---|---|---|
| Unit | tiszta függvények (margin-képlet, normalizálás) | pytest | 100% a `risk/` és `sizing/` mappában (áglefedettség ≥ 90%) |
| Property-based | invariánsok, OMS-állapotgép (stateful) | Hypothesis [hypothesis] | 0 ellenpélda, 1000 példa/teszt CI-ban |
| Golden / regresszió | referencia-backtest equity-görbe, trade-lista | pytest-regressions [pytest-regressions], syrupy [syrupy] | eltérés = piros; frissítés csak `golden-update` címkés PR-ben |
| Backtest-regresszió | 3 rögzített adat-snapshot × 5 stratégia | `atp.research.regress` | metrika-eltérés < 1e-9 (determinisztikus), Sharpe-változás jelentés |
| Szerződés | JSON Schema és üzenetek | buf/JSON Schema [buf-protobuf] | nincs breaking change MAJOR nélkül |
| Adat | Pandera-szerződések | Pandera [pandera] | 0 sértés a clean rétegben |
| Híd-integráció | Python ↔ EA demo-számlán | `tests/bridge` | roundtrip p99 < 50 ms (becs. cél), 0 elveszett `EXEC_REPORT` |
| LLM red team | injekciós korpusz | promptfoo [promptfoo] | 0 sikeres injekció |
| Biztonság | SAST, secrets, sérülékenység | Semgrep [semgrep], Gitleaks [gitleaks], pip-audit [pip-audit], OSV [osv-scanner] | 0 high/critical, 0 secret |

### 8.4 CI-pipeline

```mermaid
flowchart LR
  P[push/PR] --> L[uv sync --locked<br/>ruff + mypy]
  L --> SEC[gitleaks + semgrep<br/>pip-audit + osv-scanner]
  SEC --> UT[pytest unit + hypothesis]
  UT --> GD[golden + backtest-regresszió]
  GD --> RT[promptfoo red team<br/>ha prompt/modell változott]
  RT --> MQ[MQL5-fordítás Wine alatt<br/>figyelmeztetés = hiba]
  MQ --> SB[SBOM syft + cosign aláírás]
  SB --> ART[(aláírt artefaktum)]
```

### 8.5 Secrets és ellátási lánc

- **1. fázis:** SOPS + age, titkosított fájlok gitben [sops], [age]; runtime-ban csak memóriában. **2. fázis:** OpenBao vagy Vault, szolgáltatásonkénti policyval és rövid életű tokenekkel [openbao], [hashicorp-vault].
- A bróker-jelszó külön secret, csak az EA-gép olvassa. Befektetői (read-only) jelszó az elemző komponenseknek, ha a bróker ad ilyet (n.e.).
- Függőségek: `uv.lock` hash-ekkel [uv]; Renovate minimumRelease-késleltetéssel [renovate]; új függőség előtt OpenSSF Scorecard [ossf-scorecard]; SBOM [syft], [cyclonedx]; aláírt image [sigstore-cosign]; cél: SLSA Build L2 [slsa]; folyamat-ellenőrzőlista: NIST SSDF [nist-ssdf].
- A közösségi Docker-image-eket (MT5) nem húzzuk be közvetlenül, saját buildet készítünk rögzített base-image hash-sel [mt5-docker-gmag11].

### 8.6 Megfigyelés

- **Metrikák (Prometheus) [prometheus]:** `tick_to_decision_ms`, `decision_to_ack_ms`, `slippage_pts` (hisztogram), `fill_ratio`, `requote_total`, `margin_level_pct`, `daily_pnl_ccy`, `open_lots`, `autonomy_level`, `veto_total{code}`, `ensemble_ece`, `voter_weight{voter}`, `bridge_heartbeat_age_s`, `llm_tokens_total`, `llm_cost_usd`.
- **Riasztások (Alertmanager → Telegram) [alertmanager]:** heartbeat > 5 s; margin-szint < 500%; a napi veszteség eléri a limit 50%-át, illetve 80%-át; ECE > 0,05; vétó-ráta > 3/óra; slippage p95 > a backtest-feltételezés 2×-ese.
- **Trace:** OpenTelemetry, a GenAI szemantikai konvenciókkal [opentelemetry]. LLM-trace és prompt-verziók: Langfuse [langfuse]. Dashboard: Grafana [grafana]. Naplók: Loki [loki]. Üzemeltetési elvek (SLO, postmortem): Google SRE [google-sre-books].

---

## 9. Fázisos ütemterv elfogadási kritériumokkal

Minden kritérium három részből áll: **bemenet → elvárt kimenet → ellenőrző parancs**. A parancsok a repó gyökeréből futnak (`make` célpontok vagy `uv run`). Az ütemterv időtartamai becslések.

```mermaid
gantt
  title Ütemterv (becs.)
  dateFormat YYYY-MM-DD
  section Alap
  F0 Repó, CI, secrets      :f0, 2026-11-23, 10d
  F1 Adat + MT5-híd         :f1, after f0, 21d
  section Kutatás
  F2 Mag + backtest + golden :f2, after f1, 21d
  F3 Döntési réteg           :f3, after f2, 28d
  section Élesítés
  F4 Kockázat, OMS, mozgatókar :f4, after f2, 28d
  F5 Paper → micro live      :f5, after f4, 45d
  F6 Skálázás                :f6, after f5, 60d
```

### F0 – Repó, CI, secrets

| # | Bemenet | Elvárt kimenet | Ellenőrzés |
|---|---|---|---|
| F0.1 | üres klón | a függőségek a lockfájlból települnek | `uv sync --locked && uv run pytest -q` → exit 0 |
| F0.2 | teljes git-történet | nincs titok | `gitleaks detect --no-banner` → exit 0 |
| F0.3 | `uv.lock` | nincs ismert high/critical sérülékenység | `uv run pip-audit` → exit 0; `osv-scanner scan -L uv.lock` → exit 0 |
| F0.4 | `secrets/dev.enc.yaml` | SOPS-szal visszafejthető, a plaintext nincs a repóban | `sops -d secrets/dev.enc.yaml >/dev/null && git grep -n "password:" -- ':!*.enc.yaml'` → az első exit 0, a második nem talál semmit |
| F0.5 | PR a `risk/` mappába | review nélkül nem merge-elhető | `gh api repos/{owner}/{repo}/branches/main/protection` → `required_pull_request_reviews` beállítva; CODEOWNERS tartalmazza a `risk/` mappát |

### F1 – Adat és MT5-híd

| # | Bemenet | Elvárt kimenet | Ellenőrzés |
|---|---|---|---|
| F1.1 | EURUSD, 2026-10-01..2026-10-31, MT5 demo | `raw/source=mt5/…/*.parquet`, forrás-hash | `uv run python -m atp.data.ingest --source mt5 --symbol EURUSD --start 2026-10-01 --end 2026-10-31` → exit 0, legalább 1 fájl |
| F1.2 | ugyanez → clean | 0 Pandera-sértés; `bid <= ask` 100% | `uv run pytest tests/data/test_contracts.py -q` → 0 fail |
| F1.3 | szándékosan hibás fixture (bid>ask, visszafelé ugró ts) | a kapu elutasítja, a hibát naplózza | `uv run pytest tests/data/test_contracts.py::test_rejects_bad_ticks` → pass |
| F1.4 | EA demo-terminálon + Python-híd | `HELLO`, `TICK` stream, heartbeat | `uv run pytest tests/bridge/test_handshake.py -q` → pass; `bridge_heartbeat_age_s < 2` |
| F1.5 | 1000 `NEW_ORDER` 0,01 lottal (demo, nyit és zár) | 1000 `EXEC_REPORT`, 0 duplikátum, roundtrip p99 < 50 ms (becs.) | `uv run python -m atp.bridge.soak --n 1000 --demo` → a JSON-riport `lost=0`, `dup=0` |
| F1.6 | Python-folyamat leállítása nyitott demo-pozícióval | az EA 5 s-on belül `SAFE` módba lép, a függő megbízásokat törli | `uv run pytest tests/bridge/test_heartbeat_loss.py` → pass (az EA-napló `SAFE_MODE` sort tartalmaz) |
| F1.7 | ugyanaz a `client_order_id` kétszer | az EA a másodikat elutasítja | `tests/bridge/test_idempotency.py` → pass |

### F2 – Eseménymag, backtest, golden

| # | Bemenet | Elvárt kimenet | Ellenőrzés |
|---|---|---|---|
| F2.1 | `conf/experiment/golden_grid.yaml` + snapshot S1 | determinisztikus equity-görbe; két futás bitre azonos | `make regress` → `tests/regression/test_golden.py` pass; az eltérés 0 |
| F2.2 | ugyanaz a stratégia backtest- és sim-élő (replay) módban | azonos megbízás-sorozat | `uv run pytest tests/core/test_parity.py` → pass |
| F2.3 | OMS stateful teszt | nincs illegális átmenet; az `Unknown` állapot egyeztetődik | `uv run pytest tests/oms/test_state_machine.py --hypothesis-profile=ci` → 0 ellenpélda |
| F2.4 | margin-szimulátor 1:500 mellett | a képlet egyezik a terminál `order_calc_margin` értékével ±1% | `uv run pytest tests/risk/test_margin_vs_mt5.py --demo` → pass |
| F2.5 | futás MLflow-ban | a kötelező tag-ek megvannak | `uv run python -m atp.research.check_run <run_id>` → `OK` |

### F3 – Döntési réteg

| # | Bemenet | Elvárt kimenet | Ellenőrzés |
|---|---|---|---|
| F3.1 | súlyfrissítő | invariánsok teljesülnek (Σw=1, korlátok, NaN-tűrés) | `uv run pytest tests/decision/test_weights_props.py` → 0 ellenpélda |
| F3.2 | 3 stat + 2 ML + 1 LLM szavazó, OOS-ablak | ensemble ECE ≤ 0,03, Brier skill > 0 | `uv run python -m atp.decision.eval --window oos_2026q3` → riport `ece<=0.03`, `bss>0` |
| F3.3 | injekciós korpusz (≥ 200 eset) | 0 sémán kívüli kimenet, 0 előjelfordulás | `npx promptfoo eval -c tests/redteam/promptfooconfig.yaml` → 0 failure |
| F3.4 | szintetikus eset: csak az LLM szavaz long, a többi semleges | `UNTRUSTED_SOLE_DRIVER` vétó | `uv run pytest tests/decision/test_devil_veto.py::test_untrusted_sole_driver` → pass |
| F3.5 | rontott kalibráció (zajosított p) | `CALIB_DEGRADED` vétó, `calib_mult = 0` | `tests/decision/test_devil_veto.py::test_calibration_gate` → pass |
| F3.6 | méretező: határesetek | `size ≤ risk_cap`; `size < vol_min` esetén nincs kötés; nincs felfelé kerekítés | `uv run pytest tests/sizing -q` → pass |

### F4 – Kockázati motor, OMS, mozgatókar

| # | Bemenet | Elvárt kimenet | Ellenőrzés |
|---|---|---|---|
| F4.1 | napi veszteség szimulált átlépése | új megbízás tiltva, a szint L0-ra áll, auditesemény | `uv run pytest tests/risk/test_daily_loss.py` → pass |
| F4.2 | kill drill demo-számlán, 5 függő megbízással és 2 pozícióval | minden függő megbízás törölve ≤ 2 s; zárás konfiguráció szerint | `uv run python -m atp.governance.killswitch --drill --demo` → riport `pending=0`, `elapsed_ms<2000` |
| F4.3 | `/kill` nem engedélyezett Telegram-user_id-ről | elutasítva, riasztás megy | `tests/governance/test_telegram_auth.py` → pass |
| F4.4 | OPA-policy-k | minden szint-eset tesztelve | `opa test policy/ -v` → PASS |
| F4.5 | a policy-motor leállítva | minden intent `deny` (fail-closed) | `tests/governance/test_fail_closed.py` → pass |
| F4.6 | auditnapló 10 000 eseménnyel, egy esemény utólag módosítva | `verify()` hamis, a hibás seq kijelölve | `uv run python -m atp.audit.verify --from 0` → exit ≠ 0 a manipulált fixture-ön, exit 0 az érintetlenen |
| F4.7 | L2 jóváhagyás 61 s után | lejárt, nem megy ki | `tests/governance/test_approval_ttl.py` → pass |

### F5 – Paper → micro live

| # | Bemenet | Elvárt kimenet | Ellenőrzés |
|---|---|---|---|
| F5.1 | ≥ 30 kereskedési nap paper (demo), ≥ 200 kötés | a realizált Sharpe a backtest-előrejelzés 1σ-sávjában; a slippage p50 ≤ a modellezett 1,5×-ese | `uv run python -m atp.research.paper_vs_bt --days 30` → `PASS` |
| F5.2 | a jelölt konfiguráció study-ja | DSR ≥ 0,95; PBO < 0,2; fennsík-teszt OK | `uv run python -m atp.research.gate --study <id>` → `PASS` |
| F5.3 | micro live (élő számla, minimális lot, L2 → L3) | 0 kemény limit-sértés 20 nap alatt; az egyeztetési eltérés 0 | `uv run python -m atp.ops.daily_report --live --days 20` → `violations=0`, `recon_diff=0` |
| F5.4 | kanári deploy | egy szimbólum, 1 óra, utána automatikus bővítés vagy visszaállás | `make deploy-canary` → a smoke-teszt `PASS`, különben automatikus rollback |

### F6 – Skálázás

| # | Bemenet | Elvárt kimenet | Ellenőrzés |
|---|---|---|---|
| F6.1 | ≥ 90 nap L3 | max drawdown ≤ a tervezett; a vétó-ráta stabil; a kalibráció rendben | `atp.ops.scale_gate --days 90` → `PASS` |
| F6.2 | méret-emelés lépcsőzetesen (×1,5 lépcsőnként, legalább 2 hét/lépcső) | a slippage nem nő 25%-nál többet lépcsőnként | `atp.ops.capacity_report` → `PASS` |
| F6.3 | második végrehajtó (FIX/cTrader adapter, A1) | ugyanaz az OMS-szerződés, a paritásteszt zöld | `pytest tests/core/test_parity.py --adapter fix_sim` → pass |

---

## 10. Paritásmátrix

Jelmagyarázat: **+** = felülmúlja a referenciákat ezen a ponton; **≈** = egyenértékű a célunkhoz; **−** = elmarad (tudatosan vagy forráskorlát miatt). A Bloomberg- és Aladdin-funkciókódok és modulnevek részletes ellenőrzése az A6 feladata. Ahol itt kódot használunk, az az A6 ellenőrzéséig (n.e.). A Medallion-oszlop a nyilvánosan ismert elvekre épül (Zuckerman 2019; az A6 forrásai), (köv.).

| # | Funkció | Bloomberg | Aladdin | Medallion-elv | Mi platformunk: hogyan, mivel | Ítélet |
|---|---|---|---|---|---|---|
| 1 | Valós idejű FX/CFD ár | multi-dealer és saját feedek | piaci adat integráció | saját gyűjtés | a végrehajtó bróker MT5-feedje + referenciafeed (A1) | ≈ (a végrehajtáshoz pontosabb) |
| 2 | Történeti tick | igen (díjköteles mélység) | korlátozott | évtizedes saját archívum | MT5 export + Dukascopy/TrueFX (A1), raw-réteg | ≈ |
| 3 | Adattisztítás | szolgáltatói | szolgáltatói | **központi elv** | Pandera-szerződések, kettős forrás összevetése [pandera] | ≈ |
| 4 | Point-in-time adat | részben | igen | igen | Iceberg-snapshot, ALFRED vintage (A4) [apache-iceberg] | ≈ |
| 5 | Adatverzió-visszajátszás | – | részben | igen | `data_snapshot_id` minden futásban | + |
| 6 | Gazdasági naptár (ECO) | igen | – | – | A4 naptár + meglepetés-index | ≈ |
| 7 | Kamatvárakozás (WIRP) | igen | részben | – | futures-implikált + predikciós piac (A3) | + |
| 8 | Opciós monitor (OMON) | igen | igen | – | A1/A2 források; nem prioritás | − |
| 9 | Grafikon (GP) | igen | – | – | Grafana / TradingView | ≈ |
| 10 | Fundamentális elemzés (FA) | igen | igen | korlátozott szerep | EDGAR XBRL (A4) | − (szélesség) |
| 11 | Hírfolyam | saját + harmadik fél | – | – | Tiingo/Benzinga/GDELT (A4) | − (késleltetés) |
| 12 | Hír-szentiment | igen | részben | – | karantén-LLM + séma + több forrás | + (ellenőrzött LLM-ensemble) |
| 13 | Alternatív adat | korlátozott | korlátozott | széles (köv.) | A4 alt-adat katalógus | ≈ |
| 14 | Predikciós piaci valószínűségek | korlátozott (n.e.) | – | – | Polymarket/Kalshi szavazó (A3) | + |
| 15 | Lekérdező nyelv (BQL) | igen | igen | belső | DuckDB SQL + Python | ≈ |
| 16 | Screening | igen | igen | – | DuckDB-lekérdezések | ≈ |
| 17 | Riasztások | igen | igen | – | Alertmanager + Telegram [alertmanager] | ≈ |
| 18 | Kommunikáció/chat | igen (erős hálózat) | – | – | Telegram/Slack | − |
| 19 | Backtest-motor | igen (n.e.) | – | belső | Nautilus/LEAN + MT5 Tester [nautilustrader-architecture], [quantconnect-lean-architecture] | + (eseményvezérelt, paritás) |
| 20 | Walk-forward / purged CV | – | – | igen (köv.) | A6/A7 módszerek, kötelező kapu | + |
| 21 | Paraméter-optimalizálás | korlátozott | – | igen | Optuna/Ax [optuna], [ax-platform] | + |
| 22 | Túlillesztés-kontroll (DSR, PBO) | – | – | igen (köv.) | trial-könyvelés + PBO + DSR [pypbo] | + |
| 23 | Monte Carlo / szintetikus piac | részben | igen | igen | A7 módszerek | ≈ |
| 24 | Kísérletkövetés | – | – | belső | MLflow [mlflow-registry] | ≈ |
| 25 | Feature store | – | – | belső | Feast [feast] | ≈ |
| 26 | Modell-regiszter, champion/challenger | – | részben | belső | MLflow aliasok + árnyékfuttatás | ≈ |
| 27 | Idősoros alapmodellek | – | – | n.e. | A5/A6 (Chronos, TimesFM) ML-szavazóként | + |
| 28 | ML-modellek | BQuant (n.e.) | igen | igen | GBM stb. | ≈ |
| 29 | LLM-ágensek | asszisztens (n.e.) | Copilot-jellegű (n.e.) | n.e. | LLM-szavazók, Dual LLM [dual-llm-pattern] | + |
| 30 | Sok gyenge jel kombinálása | – | – | **központi elv** | logit-pooling + online súlyok | ≈ |
| 31 | Online súlyfrissítés | – | – | n.e. | Hedge + fixed share, River [river] | + |
| 32 | Kalibráció | – | – | n.e. | Platt/isotonic, ECE-kapu [sklearn-calibration] | + |
| 33 | Bizonytalansági sávok | – | részben | n.e. | konformális (MAPIE) [mapie] | + |
| 34 | Ördögügyvéd-vétó | – | – | – | szabály + LLM-kritikus | + (egyedi) |
| 35 | Rezsimfelismerés | – | igen | igen (köv.) | HMM/változáspont (A7), drift-detektor | ≈ |
| 36 | Hipotézisgyár | – | – | igen | A7 ötlettár → study-sablonok | ≈ |
| 37 | Portfólió-analitika (PORT) | igen | **erős** | belső | saját riport + A5 eszközök | − |
| 38 | Faktormodell (Barra-szerű) | igen | **erős** | igen | A7 nyílt faktormodellek | − |
| 39 | VaR/CVaR | igen | igen | igen | saját modul (A7 képletek) | ≈ |
| 40 | Történelmi stresszteszt | igen | igen | igen | 2015 CHF, 2020 március, 2024 augusztus jen-carry forgatókönyvek (A7) | ≈ |
| 41 | Margin/stop-out szimuláció 1:500 | – | – | – | pre-trade margin-szimulátor MT5-egyeztetéssel (F2.4) | + |
| 42 | Csődvalószínűség grid/martingale esetén | – | – | – | A7 matek + grid-limitek a sémában | + |
| 43 | Korreláció-összeomlás | igen | igen | igen | klaszter-limit + stressz | ≈ |
| 44 | Likviditási kockázat | igen | igen | igen | spread-vétó; mélységadat nincs (MT5 retail) | − |
| 45 | Partnerkockázat (bróker) | – | igen | igen | A8 brókerkockázati mátrix | ≈ |
| 46 | Pre-trade limitek | EMSX (n.e.) | igen | igen | RTS 6 15. cikk / 15c3-5 minta [eu-rts6-2017-589] | ≈ |
| 47 | Kill switch | – | igen (n.e.) | n.e. | 3 független út + drill-teszt (F4.2) | + (tesztelt) |
| 48 | Napi veszteséglimit | – | igen | n.e. | kockázati motor + EA-tartalék | ≈ |
| 49 | Compliance-szabálymotor | – | **erős** | belső | OPA/Rego, tesztelt policy-k [opa] | ≈ |
| 50 | OMS | igen | **erős** | belső | FIX-szemantikájú állapotgép [fix-protocol] | ≈ |
| 51 | EMS / algoritmikus végrehajtás | igen | igen | **erős** (köv.) | MT5: market/limit + saját időzítés | − |
| 52 | TCA / slippage-mérés | igen | igen | **erős** | slippage-hisztogram, backtest-összevetés | ≈ |
| 53 | Smart order routing | igen | igen | igen | egy bróker; később adapter (F6.3) | − |
| 54 | Spread-tágulás előrejelzése | – | – | n.e. | A7 ötlet: brókermodell-szavazó | + |
| 55 | Multibroker-absztrakció | igen | igen | igen | `ExecutionAdapter`-szerződés | ≈ |
| 56 | Késleltetés-monitorozás | – | – | **erős** | `tick_to_decision_ms` stb. [prometheus] | ≈ |
| 57 | Megfigyelés / dashboard | igen | igen | belső | Prometheus + Grafana + OTel [grafana], [opentelemetry] | ≈ |
| 58 | Manipulálhatatlan auditnapló | n.e. | igen (n.e.) | n.e. | hash-lánc + napi horgony / immudb [immudb] | + |
| 59 | Secrets-kezelés | – | igen | igen | SOPS → OpenBao [sops], [openbao] | ≈ |
| 60 | Ellátásilánc-biztonság | – | igen | igen | SBOM, cosign, pip-audit, SLSA [syft], [sigstore-cosign], [slsa] | ≈ |
| 61 | Fokozatos AI-autonómia (mozgatókar) | – | – | – | L0–L4 szintek, policy-kapuk | + (egyedi) |
| 62 | Promptinjekció-védelem | n.e. | n.e. | – | OWASP LLM01-alapú architektúra + red team [owasp-llm-top10-2025], [promptfoo] | + |
| 63 | Mobil jóváhagyás (HITL) | igen (mobil app) | részben | – | Telegram-kártya `intent_hash`-sel [telegram-bot-api] | ≈ |
| 64 | Kísérletezési ciklusidő | lassú (nem kutatóplatform) | lassú | gyors (köv.) | spec-first + AI-ágensek + CI-kapuk | + |
| 65 | Testreszabás kis számlára | – | – | – | konfig-könyvtár, kis-számla limitek | + |
| 66 | Költség | magas (A6 árazza) | intézményi | – | OSS-stack + ágens-előfizetés | + |
| 67 | Adatlefedettség szélessége | **legerősebb** | erős | erős | ingyenes és olcsó források (A1–A4) | − |
| 68 | Kutatócsapat mérete és tapasztalata | – | – | **legerősebb** | kicsi csapat + AI-ágensek | − |
| 69 | Determinisztikus visszajátszás | – | n.e. | n.e. | event sourcing, egyszálú mag [fowler-lmax-architecture] | + |
| 70 | Vagyonkezelési riport (Aladdin Wealth) | – | igen | – | nem cél | − |
| 71 | Magánpiacok (eFront) | – | igen | – | nem cél | − |
| 72 | Reprodukálható build és deploy | – | n.e. | n.e. | uv.lock, aláírt image, kanári [uv] | + |

Összegzés: 72 sorból **+** 26, **≈** 33, **−** 13. A „−” sorok nagy része tudatos hatókör-korlát (wealth, eFront, opciók) vagy forráskorlát (adatszélesség, kutatói létszám). Az előnyünk a folyamatban van: a kapukban, a kalibrációban, a mozgatókarban és a kis számlára szabott kockázatkezelésben. (köv.)

---

## 11. Hiányok és nem ellenőrzött pontok

- **Citadel / Citadel Securities mérnöki előadásai:** nyilvános, ellenőrizhető forrást nem találtunk (a careers oldal 403-at adott). Nincs katalógustétel.
- **Jane Street Tech Talks:** az oldal létezik (mért), a címlistát gépileg nem tudtuk kinyerni.
- **MT5 Manager/Gateway API részletes dokumentációja:** bejelentkezéshez kötött (support.metaquotes.net). A retail számára nem elérhetőség következtetés.
- **MetaEditor parancssori fordító kapcsolói Wine alatt:** (n.e.). Az F-fázisban a csapatnak ki kell próbálnia.
- **MQL5 hálózati függvények a Strategy Testerben:** a korlátozás részletei (n.e.).
- **Gemini CLI ára és kvótája:** (n.e.).
- **GitHub-metaadatok:** a GitHub API ebben a környezetben nem volt elérhető. A csillagok és az utolsó push a repos.ecosyste.ms tükörből származnak (mért, 2026-11-15), ezért néhány napot késhetnek. Az Ax GitHub-adata nem volt lekérhető.
- **EUR-Lex:** JS-kihívás mögött van. Az RTS 6 szövegét a legislation.gov.uk UK-változatán ellenőriztük.
- **Duplikációs kockázat:** a NautilusTrader, a LEAN és az ArcticDB az A5-ben is szerepelhet. Itt `group` mezővel jelöltük őket, és az architektúra-dokumentációra mutatnak. Az összefésüléskor egy tételbe kell vonni őket.
- A 7.2 limitértékei és a 4.6 küszöbei kiinduló becslések. Az F3–F5 során kalibrálandók.

## 12. Platform- és brókerfüggetlenség (kötelező tervezési elv)

A MetaTrader 5 és a Vantage a **jelenlegi** végrehajtási hely, nem a platform része. Ez a fejezet minden más fejezetet felülír, ha ütköznek. Elfogadási feltétel: egy új bróker vagy platform bekötése **csak** egy új adaptert és egy új helyszínprofil-fájlt igényel. A stratégiák, a döntési réteg, a kockázati motor és a backtest kódja nem változhat.

### 12.1. Kanonikus modell (brókerfüggetlen típusok)

| Típus | Kötelező mezők | Megjegyzés |
|---|---|---|
| `Instrument` | `canonical_id` (pl. `FX:EURUSD`, `CFD:US500`, `CRYPTO:BTC-USDT-PERP`, `PRED:POLY:<market_id>`), `asset_class`, `base`, `quote`, `tick_size`, `lot_step`, `min_qty` | A brókerszimbólum (`EURUSD.r`, `EURUSD+`) csak a profilban jelenik meg |
| `VenueProfile` | `venue_id`, `entity` (jogalany + szabályozó), `leverage_by_class`, `margin_model`, `stop_out_pct`, `margin_call_pct`, `negative_balance_protection`, `swap_model`, `commission_model`, `sessions`, `symbol_map`, `server_location`, `tos_flags` | **Adat** (YAML/JSON, verziózva), nem kód |
| `Order` / `Fill` / `Position` / `AccountState` | idempotencia-kulcs, kanonikus instrumentum, mennyiség kanonikus egységben (névérték vagy kontraktus), időbélyeg UTC ns | Az adapter fordít az oda-vissza irányban |
| `Capabilities` | `hedging_mode`, `netting_mode`, `partial_fills`, `oco`, `trailing_server_side`, `streaming_quotes`, `l2_depth`, `max_orders_per_sec`, `modify_in_place` | A stratégia ezt kérdezi le, nem a bróker nevét |

Példa helyszínprofilra (a mezőértékek illusztrációk, a valódi értéket a bróker szimbólum-specifikációjából kell exportálni):

```yaml
venue_id: vantage_mt5_live
entity: {name: "a számlaszerződésben megnevezett jogalany", regulator: "kitöltendő", license: "kitöltendő"}
platform: mt5
leverage_by_class: {fx_major: 500, index_cfd: 200, crypto_cfd: 20}   # kitöltendő a valós specifikációból
stop_out_pct: 50            # kitöltendő; a 20% vs 50% a kockázati motort közvetlenül érinti
negative_balance_protection: unknown
swap_model: {type: points_per_lot, triple_day: wednesday}
commission_model: {type: per_lot_round_turn, usd: 0}
symbol_map: {"FX:EURUSD": "EURUSD"}
tos_flags: {latency_arbitrage: forbidden, carry_trade_abuse_clause: check, ea_allowed: true}
```

### 12.2. Adapterek – a szerződés minden végrehajtási helyre azonos

| Adapter | Protokoll / API | Prioritás | Megjegyzés |
|---|---|---|---|
| MT5 (jelenlegi) | vékony EA + ZeroMQ/TCP, vagy MetaTrader5 Python-csomag (Windows) | F1 | lásd a 2. fejezetet |
| MT4 | EA + ZeroMQ | F6 | csak ha szükséges |
| cTrader | cTrader Open API (protobuf/WS), FIX | F6 | |
| FIX 4.4 (általános) | QuickFIX/J vagy QuickFIX/n | F6 | LMAX, Dukascopy, prime broker, sok ECN |
| Interactive Brokers | TWS API / Client Portal | F6 | részvény, opció, határidős, FX; EU-s jogalany |
| Kripto CEX/DEX | CCXT + natív WS | F6 | funding, perp, spot |
| Predikciós piacok | Polymarket CLOB, Kalshi API | F6+ | HU-ból jogi korlát, lásd az A3 fejezetet |
| Fogadási tőzsde | Betfair Exchange API | F6+ | HU-ból jogi korlát |
| Papír / szimulátor | belső | F0 | **minden** adapter paritástesztjének referenciája |

### 12.3. Bróker- vagy platformcsere ellenőrzőlistája

1. Helyszínprofil kitöltése a bróker hivatalos szimbólum-specifikációjából és az ügyfélszerződésből; minden mezőhöz forrás és dátum.
2. Adapter-paritásteszt a papíradapter ellen: ugyanaz a megbízássorozat → azonos `Position` és `AccountState` (tűrés: díj és swap).
3. Végrehajtás-audit élesben, minimális mérettel 2–4 hétig: csúszás-szimmetria, requote, töltési arány, spread rollover körül, hétvégi gap.
4. Költség-összevetés a régi és az új helyszín között ugyanarra a stratégiára (spread + jutalék + swap + visszatérítések).
5. Adó- és jogi besorolás ellenőrzése: EGT/OECD/egyezményes felügyelet → ellenőrzött tőkepiaci ügylet-e (lásd: magyar adó tábla).
6. Csak ezután: tőke áthelyezése fokozatosan, kill switch és limitek az új profillal.

### 12.4. Elfogadási feltételek

| Kritérium | Bemenet | Elvárt kimenet | Ellenőrző parancs |
|---|---|---|---|
| Stratégiakód brókerfüggetlen | a stratégia forrása | nincs benne brókernév és brókerszimbólum | `grep -rniE "vantage\|mt5\|metatrader" atp/strategies/` → üres |
| Profil adatként | új `VenueProfile` YAML | betöltés és validálás hiba nélkül | `python -m atp.venues validate venues/*.yaml` → 0 hiba |
| Paritás | azonos megbízás-szkript két adapteren | azonos pozícióállapot | `pytest tests/core/test_parity.py --adapter <új>` → pass |
| Kockázati motor profilvezérelt | stop-out 20% vs 50% profil | eltérő margin-riasztási küszöb | `pytest tests/risk/test_profile_stopout.py` → pass |
