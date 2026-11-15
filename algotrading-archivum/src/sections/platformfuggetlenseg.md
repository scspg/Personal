## 12. Platform- és brókerfüggetlenség (kötelező tervezési elv)

A MetaTrader 5 és a Vantage a **jelenlegi** végrehajtási hely, nem a platform része. Ez a fejezet minden más fejezetet felülír, ha ütköznek. Elfogadási feltétel: egy új bróker vagy platform bekötése **csak** egy új adaptert (`atp/adapters/<név>/`) és egy új profilkönyvtárat (`venues/<venue_id>/`) igényel. A stratégiák, a döntési réteg, a méretező, a kockázati motor, a mag és a backtest kódja nem változhat. A típusok normatív definíciója a §2.3 `atp/contracts.py`; ez a fejezet a venue-adat publikált sémáját és a példákat adja.

### 12.1 Kanonikus modell: `VenueProfile` és `Instrument`

**`VenueProfile` mezői** (`venues/<venue_id>/profile.yaml`, adat, nem kód; minden értékhez `sources`-bejegyzés):

| Mező | Típus | Kötelező | Jelentés |
|---|---|---|---|
| `schema_version` | `"1.0"` | igen | a séma verziója |
| `venue_id` | string `^[a-z0-9_]{3,40}$` | igen | azonosító, pl. `vantage_mt5_live` |
| `platform` | enum `mt4, mt5, ctrader, fix44, ibkr, ccxt, polymarket_clob, kalshi, betfair, sim` | igen | a protokollcsalád |
| `adapter` | string `modul:Osztály` | igen | pl. `atp.adapters.mt5:Mt5Adapter` |
| `account_type`, `account_currency` | string, devizakód | igen | pl. `raw_ecn`, `USD` |
| `entity` | objektum: `name, regulator, license_id, jurisdiction, source, checked` | igen | a szerződő jogalany **a számlaszerződésből** |
| `blocked_jurisdictions` | ISO-országkód lista | igen | ahol a helyszín tiltott vagy blokkolt (OPA, §7.2) |
| `position_mode` | `hedging \| netting` | igen | |
| `negative_balance_protection` | `yes \| no \| unknown` | igen | EU/UK retail: kötelező NBP; offshore: szerződés szerint |
| `margin_model` | objektum: `kind`, `leverage_by_class{osztály: int}`, `margin_call_pct`, `stop_out_pct`, `stop_out_mode (percent \| money)`, `stop_out_order`, `hedged_margin_pct` | igen | a stop-out **adat** (EU/UK retail 50%, egyes offshore ECN-számlák 20%) |
| `server_tz` | objektum: `mode (utc \| iana \| ny_plus)`, `iana`, `ny_plus_hours` | igen | a DST-szabályt a mód adja (§3.4) |
| `sessions` | `{osztály: [ {days[], open "HH:MM", close "HH:MM"} ]}`, `default` kötelező | igen | szerveridőben |
| `rollover_server_time` | `"HH:MM"` | igen | |
| `commissions` | lista: `applies_to[]` (glob), `kind`, `amount`, `currency` | igen | instrumentumonkénti jutalék |
| `fee_tiers` | lista: `tier, min_30d_volume, maker_bps, taker_bps` | nem | tőzsdei díjsávok |
| `swaps` | lista: `applies_to[]`, `kind (points_per_lot \| pct_annual \| funding \| none)`, `long`, `short`, `triple_day` | igen | instrumentumonkénti swap |
| `rate_limits` | lista: `name, scope, capacity, refill_per_s, cost{művelet: token}` | igen | token-vödrök, pl. Kalshi írási tokenek (`submit: 10`) |
| `capabilities` | `Capabilities` (§2.3) | igen | TIF, post_only, reduce_only, kliens-ID, cancel-on-disconnect, dead-man, végrehajtási mód |
| `symbol_map` | `{canonical_id: venue_symbol}` | igen | a brókerszimbólum csak itt és az `instruments.yaml`-ban |
| `mt` | objektum vagy `null`: `owned_magic_ranges, foreign_magics, manual_magic, comment_max_len, terminal_builds_allowed` | csak `mt4`/`mt5`-n (máshol `null`) | magic-allowlist, együttélés (§3.5) |
| `server_location` | `region, datacenter, verified` | igen | |
| `tos_flags` | `ea_allowed, latency_arbitrage, carry_trade_abuse_clause, scalping_min_hold_s, notes` | igen | ÁSZF-jelzők |
| `sources` | lista: `field, source, checked` | igen (≥ 1) | forrás és dátum mezőnként |

A leverage-osztály leképezése: `Instrument.leverage_class` → `margin_model.leverage_by_class[...]` = λ. A `peg_risk` az `Instrument` mezője (gazdasági tulajdonság), és ez kapcsolja be az 5×-ös plafont.

**`VenueProfile` JSON Schema** (`schemas/venue_profile.schema.json`, publikált, normatív):

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema", "$id": "https://atp.local/schemas/venue_profile/1.0.json", "title": "VenueProfile",
  "type": "object", "additionalProperties": false,
  "$defs": {
    "dec": {"type": ["string", "number"], "pattern": "^-?[0-9]+(\\.[0-9]+)?$"},
    "pct": {"type": ["string", "number"], "pattern": "^[0-9]+(\\.[0-9]+)?$", "minimum": 0}, "ccy": {"type": "string", "pattern": "^[A-Z0-9]{2,10}$"},
    "hhmm": {"type": "string", "pattern": "^[0-9]{2}:[0-9]{2}$"}, "day": {"enum": ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]},
    "canon": {"type": "string", "pattern": "^(FX|CFD|CRYPTO|FUT|EQ|PRED|SPORT):[A-Za-z0-9:._-]+$"},
    "globs": {"type": "array", "minItems": 1, "items": {"type": "string"}}, "date": {"type": "string", "format": "date"},
    "pos": {"type": ["string", "number"], "pattern": "^[0-9]*[1-9][0-9]*(\\.[0-9]+)?$|^0\\.[0-9]*[1-9][0-9]*$", "exclusiveMinimum": 0}
  },
  "required": [
    "schema_version", "venue_id", "platform", "adapter", "account_type", "account_currency", "entity", "blocked_jurisdictions", "position_mode",
    "negative_balance_protection", "margin_model", "server_tz", "sessions", "rollover_server_time", "commissions", "swaps", "rate_limits",
    "capabilities", "symbol_map", "server_location", "tos_flags", "sources"
  ],
  "properties": {
    "schema_version": {"const": "1.0"}, "venue_id": {"type": "string", "pattern": "^[a-z0-9_]{3,40}$"},
    "platform": {"enum": ["mt4", "mt5", "ctrader", "fix44", "ibkr", "ccxt", "polymarket_clob", "kalshi", "betfair", "sim"]},
    "adapter": {"type": "string", "pattern": "^[a-z_][a-z0-9_.]*:[A-Za-z_][A-Za-z0-9_]*$"}, "account_type": {"type": "string"},
    "account_currency": {"$ref": "#/$defs/ccy"},
    "entity": {
      "type": "object", "additionalProperties": false, "required": ["name", "regulator", "license_id", "jurisdiction", "source", "checked"],
      "properties": {
        "name": {"type": "string"}, "regulator": {"type": "string"}, "license_id": {"type": "string"}, "jurisdiction": {"type": "string"},
        "source": {"type": "string"}, "checked": {"$ref": "#/$defs/date"}
      }
    },
    "blocked_jurisdictions": {"type": "array", "items": {"type": "string", "pattern": "^[A-Z]{2}$"}},
    "position_mode": {"enum": ["hedging", "netting"]}, "negative_balance_protection": {"enum": ["yes", "no", "unknown"]},
    "margin_model": {
      "type": "object", "additionalProperties": false,
      "required": ["kind", "leverage_by_class", "margin_call_pct", "stop_out_pct", "stop_out_mode", "stop_out_order"],
      "properties": {
        "kind": {"enum": ["fx_leverage", "cfd_leverage", "exchange_margin", "portfolio", "full_collateral"]},
        "leverage_by_class": {"type": "object", "additionalProperties": {"type": "integer", "minimum": 1}}, "margin_call_pct": {"$ref": "#/$defs/pct"},
        "stop_out_pct": {"$ref": "#/$defs/pct"}, "stop_out_mode": {"enum": ["percent", "money"]},
        "stop_out_order": {"enum": ["largest_loss_first", "all_positions", "venue_defined"]}, "hedged_margin_pct": {"$ref": "#/$defs/pct"}
      }
    },
    "server_tz": {
      "type": "object", "additionalProperties": false, "required": ["mode"],
      "properties": {
        "mode": {"enum": ["utc", "iana", "ny_plus"]}, "iana": {"type": ["string", "null"]},
        "ny_plus_hours": {"type": ["integer", "null"], "minimum": -12, "maximum": 14}
      },
      "allOf": [
        {
          "if": {"properties": {"mode": {"const": "iana"}}}, "then": {"required": ["iana"], "properties": {"iana": {"type": "string"}}},
          "else": {"properties": {"iana": {"type": "null"}}}
        },
        {
          "if": {"properties": {"mode": {"const": "ny_plus"}}},
          "then": {"required": ["ny_plus_hours"], "properties": {"ny_plus_hours": {"type": "integer"}}},
          "else": {"properties": {"ny_plus_hours": {"type": "null"}}}
        }
      ]
    },
    "sessions": {
      "type": "object", "required": ["default"],
      "additionalProperties": {
        "type": "array",
        "items": {
          "type": "object", "additionalProperties": false, "required": ["days", "open", "close"],
          "properties": {
            "days": {"type": "array", "items": {"$ref": "#/$defs/day"}}, "open": {"$ref": "#/$defs/hhmm"}, "close": {"$ref": "#/$defs/hhmm"}
          }
        }
      }
    },
    "rollover_server_time": {"$ref": "#/$defs/hhmm"},
    "commissions": {
      "type": "array",
      "items": {
        "type": "object", "additionalProperties": false, "required": ["applies_to", "kind", "amount", "currency"],
        "properties": {
          "applies_to": {"$ref": "#/$defs/globs"}, "kind": {"enum": ["per_lot_side", "per_lot_round_turn", "bps_notional", "per_contract", "none"]},
          "amount": {"$ref": "#/$defs/dec"}, "currency": {"$ref": "#/$defs/ccy"}
        }
      }
    },
    "fee_tiers": {
      "type": "array",
      "items": {
        "type": "object", "additionalProperties": false, "required": ["tier", "min_30d_volume", "maker_bps", "taker_bps"],
        "properties": {
          "tier": {"type": "string"}, "min_30d_volume": {"$ref": "#/$defs/dec"}, "maker_bps": {"$ref": "#/$defs/dec"},
          "taker_bps": {"$ref": "#/$defs/dec"}
        }
      }
    },
    "swaps": {
      "type": "array",
      "items": {
        "type": "object", "additionalProperties": false, "required": ["applies_to", "kind", "long", "short"],
        "properties": {
          "applies_to": {"$ref": "#/$defs/globs"}, "kind": {"enum": ["points_per_lot", "pct_annual", "funding", "none"]},
          "long": {"$ref": "#/$defs/dec"}, "short": {"$ref": "#/$defs/dec"}, "triple_day": {"anyOf": [{"$ref": "#/$defs/day"}, {"type": "null"}]}
        }
      }
    },
    "rate_limits": {
      "type": "array",
      "items": {
        "type": "object", "additionalProperties": false, "required": ["name", "scope", "capacity", "refill_per_s", "cost"],
        "properties": {
          "name": {"type": "string"}, "scope": {"enum": ["account", "connection", "ip", "endpoint"]}, "capacity": {"type": "integer", "minimum": 1},
          "refill_per_s": {"$ref": "#/$defs/pos"}, "cost": {"type": "object", "additionalProperties": {"type": "integer", "minimum": 0}}
        }
      }
    },
    "capabilities": {
      "type": "object", "additionalProperties": false,
      "required": [
        "order_types", "tif", "post_only", "reduce_only", "client_order_id", "client_order_id_max_len", "cancel_on_disconnect", "dead_man",
        "partial_fills", "replace", "oco", "server_side_sl_tp", "trailing_server_side", "streaming_quotes", "l2_depth", "batch_orders",
        "execution_mode"
      ],
      "properties": {
        "order_types": {"type": "array", "items": {"enum": ["market", "limit", "stop", "stop_limit"]}},
        "tif": {"type": "array", "items": {"enum": ["GTC", "IOC", "FOK", "GTD", "DAY"]}}, "post_only": {"type": "boolean"},
        "reduce_only": {"enum": ["native", "emulated", "none"]}, "client_order_id": {"enum": ["native", "comment", "none"]},
        "client_order_id_max_len": {"type": "integer", "minimum": 0}, "cancel_on_disconnect": {"type": "boolean"},
        "dead_man": {"enum": ["none", "venue_heartbeat", "venue_countdown", "ea_local"]},
        "dead_man_timeout_s": {"anyOf": [{"$ref": "#/$defs/dec"}, {"type": "null"}]}, "partial_fills": {"type": "boolean"},
        "replace": {"enum": ["native", "cancel_replace", "none"]}, "oco": {"type": "boolean"}, "server_side_sl_tp": {"type": "boolean"},
        "trailing_server_side": {"type": "boolean"}, "streaming_quotes": {"type": "boolean"}, "l2_depth": {"type": "boolean"},
        "batch_orders": {"type": "boolean"},
        "execution_mode": {"type": "object", "additionalProperties": {"enum": ["market", "instant", "request", "exchange"]}}
      }
    },
    "symbol_map": {"type": "object", "propertyNames": {"$ref": "#/$defs/canon"}, "additionalProperties": {"type": "string"}},
    "mt": {
      "anyOf": [
        {"type": "null"},
        {
          "type": "object", "additionalProperties": false,
          "required": ["owned_magic_ranges", "foreign_magics", "comment_max_len", "terminal_builds_allowed"],
          "properties": {
            "owned_magic_ranges": {
              "type": "array", "items": {"type": "array", "prefixItems": [{"type": "integer"}, {"type": "integer"}], "minItems": 2, "maxItems": 2}
            },
            "foreign_magics": {"type": "array", "items": {"type": "integer"}}, "manual_magic": {"type": "integer"},
            "comment_max_len": {"type": "integer", "minimum": 0}, "terminal_builds_allowed": {"type": "array", "items": {"type": "integer"}}
          }
        }
      ]
    },
    "server_location": {
      "type": "object", "additionalProperties": false, "required": ["region", "verified"],
      "properties": {
        "region": {"type": "string"}, "datacenter": {"type": ["string", "null"]}, "verified": {"enum": ["mért", "becsült", "köv.", "nem ellenőrzött"]}
      }
    },
    "tos_flags": {
      "type": "object", "additionalProperties": false, "required": ["ea_allowed", "latency_arbitrage", "carry_trade_abuse_clause"],
      "properties": {
        "ea_allowed": {"type": "boolean"}, "latency_arbitrage": {"enum": ["forbidden", "allowed", "unknown"]},
        "carry_trade_abuse_clause": {"enum": ["present", "absent", "check"]}, "scalping_min_hold_s": {"type": ["integer", "null"]},
        "notes": {"type": "string"}
      }
    },
    "sources": {
      "type": "array", "minItems": 1,
      "items": {
        "type": "object", "additionalProperties": false, "required": ["field", "source", "checked"],
        "properties": {"field": {"type": "string"}, "source": {"type": "string"}, "checked": {"$ref": "#/$defs/date"}}
      }
    }
  },
  "allOf": [
    {
      "if": {"properties": {"platform": {"enum": ["mt4", "mt5"]}}}, "then": {"required": ["mt"], "properties": {"mt": {"type": "object"}}},
      "else": {"properties": {"mt": {"type": "null"}}}
    }
  ]
}
```

**`Instrument` JSON Schema** (`schemas/instrument.schema.json`):

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema", "$id": "https://atp.local/schemas/instrument/1.0.json", "title": "Instrument",
  "type": "object", "additionalProperties": false,
  "$defs": {
    "dec": {"type": ["string", "number"], "pattern": "^-?[0-9]+(\\.[0-9]+)?$"},
    "pos": {"type": ["string", "number"], "pattern": "^[0-9]*[1-9][0-9]*(\\.[0-9]+)?$|^0\\.[0-9]*[1-9][0-9]*$", "exclusiveMinimum": 0},
    "ccy": {"type": "string", "pattern": "^[A-Z0-9]{2,10}$"}
  },
  "required": [
    "canonical_id", "venue_id", "venue_symbol", "asset_class", "payoff", "qty_unit", "base_ccy", "quote_ccy", "settle_ccy", "contract_size",
    "tick_size", "price_precision", "min_qty", "lot_step", "leverage_class"
  ],
  "properties": {
    "canonical_id": {"type": "string", "pattern": "^(FX|CFD|CRYPTO|FUT|EQ|PRED|SPORT):[A-Za-z0-9:._-]+$"},
    "venue_id": {"type": "string", "pattern": "^[a-z0-9_]{3,40}$"}, "venue_symbol": {"type": "string", "minLength": 1},
    "asset_class": {
      "enum": ["fx", "cfd_index", "cfd_commodity", "cfd_equity", "crypto_spot", "crypto_perp", "future", "equity", "prediction", "sports"]
    },
    "payoff": {"enum": ["linear", "inverse", "quanto", "binary"]}, "qty_unit": {"enum": ["base", "quote", "shares"]},
    "base_ccy": {"$ref": "#/$defs/ccy"}, "quote_ccy": {"$ref": "#/$defs/ccy"}, "settle_ccy": {"$ref": "#/$defs/ccy"},
    "contract_size": {"$ref": "#/$defs/pos"}, "tick_size": {"$ref": "#/$defs/pos"},
    "price_precision": {"type": "integer", "minimum": 0, "maximum": 12}, "min_qty": {"$ref": "#/$defs/pos"}, "lot_step": {"$ref": "#/$defs/pos"},
    "max_qty": {"anyOf": [{"$ref": "#/$defs/pos"}, {"type": "null"}]}, "min_notional": {"anyOf": [{"$ref": "#/$defs/dec"}, {"type": "null"}]},
    "expiry": {"anyOf": [{"type": "string", "format": "date-time"}, {"type": "null"}]},
    "funding_interval_h": {"anyOf": [{"type": "integer", "minimum": 1, "maximum": 24}, {"type": "null"}]},
    "outcome_token_id": {"anyOf": [{"type": "string", "pattern": "^[0-9]+$"}, {"type": "null"}]}, "leverage_class": {"type": "string"},
    "session_class": {"type": "string", "default": "default"}, "peg_risk": {"type": "boolean", "default": false}
  },
  "allOf": [
    {
      "if": {"properties": {"asset_class": {"const": "prediction"}}},
      "then": {"properties": {"payoff": {"const": "binary"}, "qty_unit": {"const": "shares"}}}
    },
    {
      "if": {"properties": {"canonical_id": {"pattern": "^PRED:POLY:"}}},
      "then": {"required": ["outcome_token_id"], "properties": {"outcome_token_id": {"type": "string"}}}
    },
    {"if": {"properties": {"asset_class": {"const": "crypto_perp"}}}, "then": {"required": ["funding_interval_h"]}},
    {"if": {"properties": {"payoff": {"const": "inverse"}}}, "then": {"properties": {"qty_unit": {"const": "quote"}}}}
  ]
}
```

**Példa helyszínprofilra** – a fenti sémának és a Pydantic-modellnek is megfelel (`tests/contracts/test_schema_sync.py` ellenőrzi). A betöltés: YAML → JSON → séma-validálás és `VenueProfile.model_validate_json`. Az értékek illusztrációk; a valódi értéket a saját szimbólum-exportból és a Client Agreementből kell kitölteni. A jogalany a Help Center szerint (2026-11-05) VIG Group (Mauritius FSC GB20026165; FSCA 51268, ASIC 428901), de a kötelező forrás a saját szerződés:

```yaml
# venues/vantage_mt5_live/profile.yaml – az értékek illusztrációk; a valódit a saját
# szimbólum-exportból és a Client Agreementből kell kitölteni (minden mezőhöz sources-bejegyzés)
schema_version: "1.0"
venue_id: vantage_mt5_live
platform: mt5
adapter: "atp.adapters.mt5:Mt5Adapter"
account_type: raw_ecn
account_currency: USD
entity:
  name: "a számlaszerződésből"
  regulator: "a számlaszerződésből"
  license_id: "a számlaszerződésből"
  jurisdiction: "a számlaszerződésből"
  source: "Client Agreement PDF (sha256 a sources-ban)"
  checked: "2026-11-15"
blocked_jurisdictions: []
position_mode: hedging
negative_balance_protection: unknown
margin_model:
  kind: fx_leverage
  leverage_by_class: {fx_major: 500, fx_minor: 500, fx_peg: 100, index_cfd: 200, crypto_cfd: 20}
  margin_call_pct: "50"
  stop_out_pct: "20"
  stop_out_mode: percent
  stop_out_order: largest_loss_first
  hedged_margin_pct: "0"
server_tz: {mode: ny_plus, ny_plus_hours: 7}
sessions:
  default:
    - {days: [mon, tue, wed, thu], open: "00:05", close: "23:57"}
    - {days: [fri], open: "00:05", close: "23:55"}
rollover_server_time: "00:00"
commissions:
  - {applies_to: ["FX:*"], kind: per_lot_round_turn, amount: "6", currency: USD}
swaps:
  - {applies_to: ["FX:EURUSD"], kind: points_per_lot, long: "-7.1", short: "2.3", triple_day: wed}
rate_limits:
  - {name: orders, scope: account, capacity: 10, refill_per_s: "0.1667", cost: {submit: 1, cancel: 1, replace: 1}}
capabilities:
  order_types: [market, limit, stop, stop_limit]
  tif: [GTC, IOC, FOK, GTD, DAY]
  post_only: false
  reduce_only: emulated
  client_order_id: comment
  client_order_id_max_len: 31
  cancel_on_disconnect: false
  dead_man: ea_local
  dead_man_timeout_s: "5"
  partial_fills: true
  replace: native
  oco: false
  server_side_sl_tp: true
  trailing_server_side: false
  streaming_quotes: true
  l2_depth: false
  batch_orders: false
  execution_mode: {"*": market}
symbol_map: {"FX:EURUSD": "EURUSD", "FX:USDJPY": "USDJPY"}
mt:
  owned_magic_ranges: [[710000, 710999]]
  foreign_magics: [12345]
  manual_magic: 0
  comment_max_len: 31
  terminal_builds_allowed: [5200]
server_location: {region: "London", datacenter: "Equinix LD4", verified: "nem ellenőrzött"}
tos_flags:
  ea_allowed: true
  latency_arbitrage: forbidden
  carry_trade_abuse_clause: present
  notes: "carry trade és cash-back arbitrázs visszaélésnek minősül (A1, snippet)"
sources:
  - {field: margin_model.stop_out_pct, source: "AccountInfoDouble(ACCOUNT_MARGIN_SO_SO) a HELLO-ban", checked: "2026-11-15"}
  - {field: entity, source: "saját Client Agreement", checked: "2026-11-15"}
```

**Példa instrumentumokra** (`venues/<venue_id>/instruments.yaml`; a Polymarket-sor azonosítója illusztráció, a minimális méret és a tick ellenőrizendő):

```yaml
# venues/vantage_mt5_live/instruments.yaml (részlet) – az adapter instruments() exportjából
- canonical_id: "FX:EURUSD"
  venue_id: vantage_mt5_live
  venue_symbol: EURUSD
  asset_class: fx
  payoff: linear
  qty_unit: base
  base_ccy: EUR
  quote_ccy: USD
  settle_ccy: USD
  contract_size: "100000"
  tick_size: "0.00001"
  price_precision: 5
  min_qty: "1000"
  lot_step: "1000"
  max_qty: "10000000"
  leverage_class: fx_major
- canonical_id: "PRED:POLY:123456789012345678901234567890"
  venue_id: polymarket_clob
  venue_symbol: "123456789012345678901234567890"
  asset_class: prediction
  payoff: binary
  qty_unit: shares
  base_ccy: SHARE
  quote_ccy: USDC
  settle_ccy: USDC
  contract_size: "1"
  tick_size: "0.01"
  price_precision: 2
  min_qty: "5"
  lot_step: "1"
  min_notional: "1"
  expiry: "2026-12-31T23:59:59Z"
  outcome_token_id: "123456789012345678901234567890"
  leverage_class: none
```

### 12.2 Adapterek – a szerződés minden végrehajtási helyre azonos

| Adapter | Protokoll / API | Fázis | Megjegyzés |
|---|---|---|---|
| Sim / papír | belső | F0 | **minden** adapter paritástesztjének referenciája (§3.9) |
| MT5 (első) | vékony EA + ZeroMQ DEALER/ROUTER (ADR-01); kiegészítőként a MetaTrader5 Python-csomag | F1 | §4 |
| CCXT testnet (második, valódi) | REST + WS, Binance USDⓈ-M Futures testnet (tartalék: Bybit testnet) | F2–F4 | §3.8, ADR-10 |
| MT4 | EA (MQL4) + ugyanaz a hídprotokoll | F1, ha a Q1 válasza MT4; különben F6 | |
| cTrader | Open API (protobuf/WS), FIX 4.4 | F6 (harmadik) | A11 migrációs út |
| FIX 4.4 (általános) | QuickFIX/J vagy QuickFIX/n | F6+ | LMAX, Dukascopy, prime broker, sok ECN |
| Interactive Brokers | TWS API / Client Portal | F6+ | részvény, opció, határidős, FX; EU-s jogalany |
| Kripto élő | CCXT + natív WS | F6+ | külön jogi/adó-ellenőrzés után |
| Predikciós piacok | Polymarket CLOB, Kalshi API | F6+ | HU-ból blokkolt/korlátozott (OPA `VENUE_BLOCKED`), csak adatként |
| Fogadási tőzsde | Betfair Exchange API | F6+ | HU-ból blokkolt (SZTFH) |

### 12.3 Bróker- vagy platformcsere ellenőrzőlistája

1. Helyszínprofil kitöltése a bróker hivatalos szimbólum-specifikációjából és az ügyfélszerződésből; minden mezőhöz forrás és dátum (`sources`).
2. Az adapter-szerződés tesztkészlete zöld a protokoll-szimulátoron és a felvett visszajátszáson, a §3.9 tűréseivel (nem élő-élő összevetés).
3. Comment- vagy kliens-ID-próba, dead-man próba, hat szintes kill-gyakorlat (§6.5) a demón.
4. Végrehajtás-audit élesben, minimális mérettel, a §3.7 mintaméretéig: feltételes szimmetria, last-look szignatúra, markoutok, requote, fill-arány, spread rollover körül, hétvégi gap. Régiónként külön VPS-ről, a késleltetéssel normalizálva.
5. Költség-összevetés a régi és az új helyszín között ugyanarra a stratégiára (spread + jutalék + swap + visszatérítések).
6. Adó- és jogi besorolás: EGT/OECD/egyezményes felügyelet → ellenőrzött tőkepiaci ügylet-e (A8 magyar adó tábla); `blocked_jurisdictions` kitöltve.
7. Csak ezután: tőke áthelyezése fokozatosan, kill switch és limitek az új profillal, farokkapu az új profil stop-outjával és margin-modelljével.

### 12.4 Elfogadási feltételek

| Kritérium | Bemenet | Elvárt kimenet |
|---|---|---|
| A venue-semleges mag nem importál adaptert vagy venue-SDK-t | `atp.strategies`, `decision`, `sizing`, `risk`, `core`, `oms` | az import-linter `forbidden` szerződése zöld |
| Nincs brókernév és bróker-konstans a venue-semleges kódban | ugyanezek a mappák | a `grep` üres |
| Profil adatként | új `VenueProfile` és `Instrument` YAML | séma- és Pydantic-validálás hiba nélkül, a kettő egyezik |
| Paritás | azonos megbízás-szkript a sim-adapteren és az új adapter szimulátorán/visszajátszásán | a §3.9 tűrései |
| Profilvezérelt kockázat | stop-out 20% vs 50% profil | eltérő `x_SO` és riasztási küszöb |

**Import-linter szerződés** (`pyproject.toml`):

```toml
[tool.importlinter]
root_package = "atp"
include_external_packages = true

[[tool.importlinter.contracts]]
name = "A venue-semleges mag nem importal adaptert, profil-betoltot es venue-SDK-t"
type = "forbidden"
source_modules = ["atp.strategies", "atp.decision", "atp.sizing", "atp.risk", "atp.core", "atp.oms"]
forbidden_modules = ["atp.adapters", "atp.venues", "MetaTrader5", "ccxt", "zmq"]
```

```bash
# venue-semlegesség (GNU grep, ERE)
uv run lint-imports
test -z "$(grep -rniE '(vantage|metatrader|mql[45]|(^|[^a-z0-9])mt[45]([^a-z0-9]|$))' \
  atp/strategies atp/decision atp/sizing atp/risk atp/core atp/oms || true)"
test -z "$(grep -rnE '(SYMBOL_[A-Z_]+|ACCOUNT_[A-Z_]+|ORDER_FILLING_[A-Z]+|TRADE_ACTION_[A-Z]+)' \
  atp/strategies atp/decision atp/sizing atp/risk atp/core atp/oms || true)"
# profil adatként
uv run python -m atp.venues validate venues/*/profile.yaml venues/*/instruments.yaml
uv run pytest tests/contracts/test_schema_sync.py -q
# paritás és profilvezérelt kockázat
uv run pytest tests/core/test_parity.py tests/adapters/test_contract.py -q --adapter mt5_bridge_sim
uv run pytest tests/core/test_parity.py tests/adapters/test_contract.py -q --adapter ccxt_replay
uv run pytest tests/risk/test_profile_stopout.py -q
```
