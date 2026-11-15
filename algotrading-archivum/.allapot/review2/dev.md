# Tech lead – 2. kör: 90,7 (1. kör 70,3); javítás után ~94,7 (95+ az ügyfél Q1–Q3 válaszaival)
a 93 · b 91 · c 92 · d 88 · e 89 · f 91. Igazolva: contracts.py importál, VenueProfile/Instrument példák sémán és Pydanticon át; súlyfrissítés 20 000 véletlen konfigon max hiba 1e-16; golden méretezés egyezik (E_min 733 USD); §12.4 grep ERE + import-linter; Gantt L4 ~240. nap; újraépítés bájtazonos; HTML 0 JS-hiba, költségszűrő, rendezés, hash, validálás, MC leghosszabb blokk 124 ms.
1 (d) §5.5 update() csoport-plafon: project_capped_simplex(rest,…,1−cap) ValueError, ha a nem-LLM szavazók nem bírják a 75%-ot (20 000-ből 5059 konfigon; {l,a,b} egy LLM-mel reprodukálható) → konstruktorban |rest|·w_max ≥ 1−w_llm_max és |G|·w_min ≤ w_llm_max ellenőrzés; F3.1 Hypothesis csak megvalósítható csoportokat; teszt: megvalósíthatatlan konfig elutasítva.
2 (d) F3.4(a) sosem megy át: egyedül az LLM szavaz → 1 ébren < n_awake_min=2 → None, ördögügyvéd nem fut, UNTRUSTED_SOLE_DRIVER nem tüzel → elvárt: „nincs Proposal (NO_QUORUM)”, vagy sole-driver szabály a kvórum előtt.
3 (d) §5.8 LLM-kritikusnak nincs timeout/kiesés-szabály → 2 s timeout, severity=0,5, CRITIC_TIMEOUT audit, nincs vétó; teszt F3.7.
4 (d) ECE 200 címkén 10 binnel zajos → CALIB_DEGRADED és L2→L1 csapkod → egyenlő tömegű binek, bootstrap felső korlát, hiszterézis (vétó 0,05; visszakapcsolás 3 ablak ≤0,03 után).
5 (d) F3.2 jq gyengébb a szabálynál (.window_start > .llm_knowledge_cutoff vs cutoff + 1 hónap) → .llm_eval_floor kiírása és .window_start >= .llm_eval_floor.
6 (c) §6.1 #3 dedup intent_hash-en 60 s-on belül sosem tüzel (az intent_hash a client_order_id UUIDv7-et és created_ns-t is fedi) → dedup_key = sha256(canonical_json(intent, exclude={client_order_id, created_ns, proposal_id})) a hashing.py-ba; intent_hash marad a jóváhagyáshoz.
7 (b) F6.1 jq (.psr0 >= 0.95 or .n_obs < .min_trl) PASS kevés megfigyelésnél → .psr0 >= 0.95 and .n_obs >= .min_trl; „még nem eldönthető” külön.
8 (b) F1.6 SAFE 5 s-on belül (dead_man_timeout_s=5) vs §6.5 K5 ≤ timeout + 2 s → egy kritérium: SAFE ≤ dead_man_timeout_s + 2 s.
9 (b) éjszakai kill_drill demo/testnet és make deploy-canary jq -e ítélet nélkül; ctrader_replay (F6.3) hiányzik az ADAPTERS-ből → jq -e '.all_pass'; deploy-canary visszagörgetéskor nem nulla kilépés; ctrader_replay az ADAPTERS-be.
10 (b) §12.4 grep CamelCase-t nem fog (class MT5Adapter, -i mellett a „mt5” utáni betű nem [^a-z0-9]) → mt[45]([^0-9]|$).
11 (e) spec-fül 400 px-en scrollWidth 781 (<pre> 1120 px-ig, hosszú inline <code>) → #spec pre{overflow-x:auto;max-width:100%}, #spec code{overflow-wrap:anywhere}.
12 (e) spec-fülön 0 belső horgony 2670 sorra, mermaid nyers kód → heading id + ragadós TOC; mermaid-blokk címke („diagram, mermaid.live”) vagy előre renderelt SVG.
13 (e) ZIP duplikált tag: ALGOTRADING/forras/OLVASS-EL.md explicit (16. sor) + os.walk → a walk hagyja ki.
14 (e) HTML stop-out alap 50% vs Vantage global 20% (mért) → 20% megjegyzéssel vagy helyszín-előbeállítás.
15 (e) üres hash-re visszalépve nem látszik fül → üres hash = kat.
16 (f) ALGOTRADING.md 653., 668. sor VFSC 700271 [mért] vs 967. sor és spec Q1 VIG Group → A1 összefoglaló és tábla a Q1 megfogalmazásával.
17 (f) OLVASS-EL „MetaTrader 5” vs spec §0/Q1 MT4 vagy MT5 nyitott; olvasási sorrend README (§12 először) vs spec fejléce (§0 → §2 → §12 → §10).
18 (f) spec §0.2 szójegyzék elavult (src/research/a* helyett forras/research/a*; az A-lista kihagyja A2, A4, A9, A10) → README szójegyzék sora.
