# A1 – Piaci adat (M1) + végrehajtás és brókerek (M6) – összefoglaló

Ellenőrzés napja: 2026-11-15. Kimenet: `a1_market_exec.jsonl`, 160 tétel (M1: 75, M6: 85). Címkék: mért 87, becsült 62, nem ellenőrzött 11.
Módszer: WebFetch/curl a forrásoldalakra, kis API-próbák (GLEIF, OpenFIGI, NY Fed, ECB, Energy-Charts, Cboe VIX, MNB WSDL), PyPI JSON. GitHub-csillagok és utolsó push az ungh.cc GitHub-API proxyn át, licenc a shields.io-n át (a GitHub közvetlenül 403-at adott a proxyn).
EUR-átszámítás: ECB referencia 2026-11-13, 1 EUR = 1.1052 USD (mért). Minden EUR/hó érték becsült.
Korlát: a munkamenet közös WebSearch-kerete elfogyott a futás közben. Utána csak WebFetch, curl és API-próbák mentek, ezért a brókeradatok egy része „becsült” maradt.

## Fő megállapítások
- A Vantage 1:500-as számlája offshore jogalanyhoz tartozik. A korábban idézett Vantage Global Limited (VFSC 700271) **történeti** adat [mért egy régebbi PDF-ből]; a Help Center (2026-11-05) szerint ma a VIG Group (Mauritius FSC GB20026165) szerződtet, és a kötelező forrás az ügyfél saját Client Agreementje (lásd a11_matrix.md 1. fejezet). Ennek EU-s befektetővédelme nincs, és MiFID-útlevele sincs. Ehhez a jogalanyhoz LEI-t sem találtam [mért].
- Felügyeleti nyomás [mért]:
  - AFM penalty payment order a Vantage Global Limited ellen, 2024-10-24.
  - Az FCA 2026-04-02-án warning listára tette a vantagemarkets.com-ot, és kimondta, hogy az nem azonos az FCA-engedélyes Vantage Global Prime LLP-vel.
  - EU-s kockázat: a magyar ügyfelek kiszolgálása bármikor megszűnhet. B-terv bróker és rendszeres profitkivétel kell.
- A Client Agreement (2023-05, 2025-08) tiltja az „abusive” kereskedést. Néven nevezi a cash-back arbitrázst és a „carry trade”-et [becsült, keresési kivonat; a PDF 403]. A swapgyűjtő hedge-grid ÁSZF-kockázatos lehet. EA-tilalmat nem találtam.
- Szerverhely: a Vantage hivatalosan London + New York, Equinix-partnerség [becsült]. LD4-et nem nevez meg. A VPS-cégek állításai ellentmondanak egymásnak (LD4 vs NY4/TY3). A szervernevek 2026-05-30 óta `VantageInternational-*` [becsült]. Az access-szerver címkék (VPS-Mart): Live4/Live6 londoni és NY/NV pontok, Live3 főleg NV [mért, harmadik fél].
- Az MT5 saját exportja a legértékesebb Vantage-specifikus adat (tick, spread, swap, margin, kereskedési idő), és máshol nem kapható meg. Tételek: `mt5-symbol-spec-export`, `method-vantage-spread-swap-logger`, `method-vantage-execution-audit`.
- Az ingyenes FX tick gerince a Dukascopy, de 2025–26-ban AWS WAF került elé [mért, dukascopy-node]. A HistData utolsó adatposztja 2022-11 [mért]. Független TCA: tcapy (alpha, 2021-es release) [mért].
- Árak a kulcsvendoroknál [mért]: Databento Standard $199/hó (+$125 kredit), ORATS $199–899, Theta Data $40/80/160, Tiingo Power $30, EODHD $19.99–99.99, Twelve Data $79–999, Alpha Vantage $49.99–249.99, IQFeed $108.15 + tőzsdei díjak, MetaQuotes VPS $10–15.
- A Polygon.io neve 2025 októbere óta Massive [mért, redirect]. Az ib_insync helyett ib_async kell [mért]. A PyPI-n lévő `ibapi` 2020-as [mért].

## Vantage-adatlap (minden ténynél címke)
| Tény | Érték | Címke |
|---|---|---|
| Offshore jogalany (1:500) | Ma: VIG Group, Mauritius FSC GB20026165 (Help Center 2026-11-05); történeti: Vantage Global Limited, VFSC 700271 (Financial Dealers Licensing Act CAP 70); kötelező forrás: a Client Agreement | mért (Help Center; a VFSC-adat régebbi PAMM Agreement PDF-ből, történeti) |
| Kajmáni jogalany | Vantage International Group Ltd, CIMA SIBL 1383491; LEI 549300F1FE68O6Z81Y75 | szám: becsült; LEI: mért |
| UK jogalany | Vantage Global Prime LLP, FCA FRN 590299; LEI 213800EXN2WUODF1C670; retail 1:30 | FRN, LEI: mért; 1:30: becsült |
| AU jogalany | Vantage Global Prime Pty Ltd, AFSL 428901; LEI 5493003EAMXFPEID3T86 | AFSL: becsült; LEI: mért |
| ZA jogalany | Vantage Markets (Pty) Ltd, FSCA FSP 51268 | becsült |
| Tőkeáttétel | global help: 1:100–1:500; APAC: 1:2000-ig; Premium Unlimited (2026-03) | becsült |
| Számlák | Standard STP (0 jutalék), Raw ECN ($3/oldal), Pro ECN ($1.5–2/oldal, min. $10k) | becsült (ellentmondó források) |
| Min. betét | Standard/Raw $50 | becsült |
| Margin call / stop-out | 50% / 20% (global); UK: 50% | becsült |
| Swap | nincs megbízható nyilvános tábla → mérni kell MT5-ből | nem ellenőrzött |
| Szerverek | MT5: VantageInternational-Demo, Live3/4/6; MT4: Live 8/9/20/22 | becsült (név), mért (3. fél ping) |
| Adatközpont | London + New York, Equinix-partner; LD4 nem megerősített | becsült |
| ÁSZF | abusive trading; cash-back arbitrázs és carry trade tiltva; EA nem tiltott | becsült / nem ellenőrzött |
| Szabályozói ügyek | AFM 2024-10-24; FCA warning 2026-04-02; DFSA 2023 | mért |
| Kifizetési reputáció | Trustpilot ~4.3; FPA 2026: profit-levonások nagy nyereség után | becsült (anekdotikus) |
| MNB-figyelmeztetés | nem találtam | nem ellenőrzött |

## Lefedettségi hiányok
1. A Vantage Client Agreement teljes szövege (Cloudflare 403). A latency arbitrage, a scalping és a profit-törlés pontos klauzuláját nem olvastam. A swaptáblák és a pontos szerver-IP/DC sem ismert. Böngészőből le kell tölteni és archiválni.
2. A bróker-összehasonlításban (Exness, FP Markets, XM, BlackBull, Darwinex, Admirals) a licencszámok és a tőkeáttétel részben becsültek. Ennek oka a 403 és az elfogyott keresési keret. A jogalanyok létét a GLEIF igazolja.
3. A Vantage és a többi bróker valós trade-szerver helye nincs mérve (saját VPS-ről traceroute és order round-trip kell). Nem tudni, a Vantage melyik bridge-et/LP-t használja (PrimeXM/oneZero/Centroid).
4. Nem ellenőrzött árak: Tickstory, Tick Data Suite, MetaApi, Kibot, Massive opció/FX, Norgate szintenként, IBKR market data (403), CME DataMine.
5. Hiányos magyar adat: BUBOR-letöltési URL, a BÉT adatlicenc-oldala, a MAVIR/HUPX API. Az Alpaca, a tastytrade és az OANDA EU magyar elérhetősége sem ellenőrzött.

## Forráskorlátos (fizetős vagy intézményi)
- Csak intézményi: CRSP és WRDS, OptionMetrics IvyDB, LSEG Tick History, ICE Data Services, BestX, Tradefeedr, PrimeXM/oneZero/Centroid, LMAX (professional státusz, ≥€500k portfólió).
- Drága vagy egyedi ajánlat: TrueFX streaming ($4 950–7 450/hó), CME DataMine, Cboe DataShop, Tick Data LLC, AlgoSeek, Barchart, Eurex.
- Retail-barát alternatívák:
  - Databento (CME/ICE/US equity L3);
  - Theta Data és ORATS (opciók);
  - Norgate és FirstRate (survivorship-mentes);
  - Dukascopy (FX tick);
  - MT5 saját export (Vantage-specifikus).
