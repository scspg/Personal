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
