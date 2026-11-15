# A8 – Infrastruktúra, szerverhely, hardver, költözés, adó és szabályozás – táblák

Ellenőrzés napja: 2026-11-15. Árfolyam: EKB 2026-11-13, 1 EUR = 365,60 HUF = 1,1052 USD = 0,83559 GBP (mért).
Címkék: **mért** = forrásban vagy saját lekérdezéssel látott érték; **becsült** = számolt vagy proxyból becsült; **nem ellenőrzött** = nem sikerült forrással igazolni.
Ez nem jogi vagy adótanács: tények és források. A források URL-jei a `a8_infra_legal.jsonl` tételeiben szerepelnek (az `id` oszlop alapján kereshetők).

---

## 1. Szerverhelyek

| Szereplő / szerver | Hely (adatközpont) | Forrás (id) | Megjegyzés |
|---|---|---|---|
| Vantage MT4/MT5 – elsődleges | London és New York, Equinix-partnerség (mért) | vantage-server-locations-helpcenter | Az épületet (LD4/LD5, NY4/NY5) a Vantage nem nevezi meg (mért) |
| Vantage – további | Sydney, Szingapúr, Hongkong, Tajpej (mért) | vantage-server-locations-helpcenter | Ázsiai access pointok (becsült) |
| VantageInternational-Live 20/22 DC1-LD, DC10-LD | London (mért, szervernév-címke) | vpsmart-vantage-ping-table | Épületkód nincs (nem ellenőrzött) |
| VantageInternational-Live 9 DC2-NY | New York (mért, szervernév-címke) | vpsmart-vantage-ping-table | NY4 valószínű (becsült) |
| Vantageinternational-Live4 (MT5) AS1/AS2/AS10-LD, AS3-NY | London és NY access szerverek (mért) | vpsmart-vantage-ping-table | A trade szerver helye eltérhet az access pointtól (becsült) |
| Live 22 DC9-Vignia; Live 3 Access Server 6/7/22/23-NV | Virginia; „NV” (mért, címke) | vpsmart-vantage-ping-table | „NV” jelentése nem ellenőrzött |
| Vantage Markets LD4-ből | 1,01 ms tipikus (mért, gyártói tábla) | nycservers | Módszertan nélkül (nem ellenőrzött) |
| Vantage – TradingFXVPS-ről | ~0,33 ms (mért, gyártói tábla) | tradingfxvps | Melyik városból: nem ellenőrzött |
| Vantage – ForexVPS NY és London VPS-ről | ~1 ms mindkettőről (mért, gyártói állítás) | forexvps-net | Független mérés nincs (nem ellenőrzött) |
| Equinix LD4 | 2 Buckingham Avenue, Slough, SL1 4NB (mért, Deribit docs) | equinix-ld4-slough-fx-hub | LMAX, FastMatch, Deribit matching engine (mért) |
| Equinix NY4 | Secaucus, NJ kampusz (mért) | equinix-ny4-secaucus-fx-hub | IC Markets, Axi, Global Prime, FP Markets (mért, bróker-közlés) |
| Equinix TY3 | Tokió (mért) | equinix-ty3-tokyo-fx-hub | FXCM 2013, LMAX 2014 matching engine (mért) |
| Equinix SG1 / HK1 | Szingapúr / Hongkong (nem ellenőrzött épületszinten) | equinix-sg1-hk1-asia | NYCServers kínál VPS-t (mért) |
| Deribit | Equinix LD4 (mért) | deribit-ld4-colocation | 2U colocation, cross-connect (mért) |
| Binance | AWS Tokió, ap-northeast-1 (mért, Glassnode) | binance-aws-tokyo | Tokióból 8 ms TTFB (mért, CCXT) |
| Bybit | Szingapúr (mért, CCXT legjobb régió) | bybit-okx-asia-regions | 10 ms (mért) |
| OKX | Hongkong (mért, CCXT legjobb régió) | bybit-okx-asia-regions | Tokióba költözés: nem ellenőrzött |
| Coinbase | US-East / CDN (mért, CCXT) | coinbase-kraken-us-eu | London 10 ms, Frankfurt 14 ms (mért) |
| Kraken | London a leggyorsabb (mért, CCXT) | coinbase-kraken-us-eu | AWS-régiók: nem ellenőrzött |
| Hyperliquid | Tokió a leggyorsabb (mért) | ccxt-exchange-latency-map-2026 | 6 ms (mért) |
| Polymarket | AWS eu-west-2, London (mért, hivatalos docs) | polymarket-servers-eu-west-2 | Colocation KYC-vel (mért); HU-ból SZTFH-blokk (mért) |
| Kalshi | AWS us-east-2, Ohio (mért, Glassnode) | kalshi-aws-us-east-2 | HU hozzáférés: nem ellenőrzött |

## 2. VPS és colocation

| Szolgáltató | Ár (eredeti) | EUR/hó (becsült átszámítás) | Helyszínek | Ping a Vantage / LD4 / NY4 felé | Megjegyzés |
|---|---|---|---|---|---|
| MetaQuotes VPS | 15 USD/hó (1 hó) – 10 USD/hó (12 hó) (mért) | 9–14 (becsült) | „30+ hosting point” (mért) | 96% bróker <10 ms, 84% <3 ms (mért, gyártói) | DLL tiltott, csak EA (mért) |
| NYCServers | 20,83–50 USD/hó VPS; 145,83 USD/hó dedikált (mért) | 19–45; 132 (becsült) | NY4, LD4, TY3, SG1, HK1, DUB1 (mért) | Vantage Markets LD4: 1,01 ms (mért, gyártói) | Éves fizetéssel −20% (mért) |
| ForexVPS.net | 36 / 54 / 72 USD/hó havi; 28,80 / 43,20 / 57,60 éves (mért) | 26–65 (becsült) | „22 location” (mért) | Vantage ~1 ms NY és London (mért, gyártói) | Dedikált 270 USD/hó-tól (mért) |
| Beeks Group (BeeksFX) | 32 / 57 / 100 GBP/hó + ÁFA (mért) | 38 / 68 / 120 (becsült) | „18 data centres” (mért, MassiveGRID idézi); LD4/LD5 (nem ellenőrzött) | nem ellenőrzött | Proximity/Exchange Cloud egyedi ár (mért) |
| FXVM | 15 / 25 / 35 / 50 USD/hó (mért) | 14–45 (becsült) | LD4, NY4, AM6, TY8 + 5 Equinix (mért) | Tábla üres; „0–5 ms” (mért, gyártói) | −15% kupon (mért) |
| TradingFXVPS | 17,50 USD/hó (éves 210 USD), Standard+ 22,11 (mért) | 16–20 (becsült) | London, New York, Frankfurt, Amszterdam (mért) | Vantage ~0,33 ms (mért, gyártói) | Ryzen 9 4,3 GHz, DDR5 (mért) |
| MassiveGRID NY/London | 4,79–65,16 USD/hó (mért) | 4–59 (becsült) | NY metró, nem Equinix-épület (mért, FAQ) | „<1 ms” (mért, gyártói, módszertan nélkül) | NY4-hez valós ~1–2 ms (becsült) |
| VPS-Mart (Vantage-oldal) | 4,05–51,99 USD/hó (mért) | 4–47 (becsült) | USA (Dallas/Kansas) (mért) | Vantage LD 95–103 ms, NY 29–95 ms az USA-ból (mért) | Vantage-hez földrajzilag rossz (becsült) |
| Commercial Network Services | nem ellenőrzött | nem ellenőrzött | NY4 cross-connect 2017 (mért) | nem ellenőrzött | Honlap nem elérhető (mért) |
| „Liquid Trading/Beeks” | nem található (mért: a liquidtrading.com eladó domain) | – | – | – | Feltehetően a Beeks-re utal (becsült) |
| Vantage ingyenes VPS-program | 25 vagy 50 USD/hó visszatérítés (mért) | 23 / 45 (becsült) | bármely szolgáltató számlája (mért) | – | ≥1000 USD befizetés, havi forgalom: 0,5 M USD → 25, 1 M USD → 50 (mért, T&C keresési találat) |
| Hetzner Cloud | 5,49 EUR/hó-tól; dedikált vCPU 36,99-től (mért) | 5,49–36,99+ (mért) | FSN, NBG, HEL, Ashburn, Hillsboro, SG (mért) | LD4-hez ~15–25 ms (becsült) | Kutatás, adatgyűjtés |
| Hetzner AX | 59–614 EUR/hó + telepítés (mért) | 59–614 (mért) | DE/FI (nem ellenőrzött modellenként) | nem releváns | Tick-DB, backtest-farm |
| Hetzner GEX (GPU) | 214 / 999 / 1499 / 3599 EUR/hó (mért) | ugyanaz (mért) | HEL1, FSN1 (mért) | nem releváns | ML-tanítás |
| OVHcloud Rise | 56,99–64,99 EUR/hó-tól (mért) | ugyanaz (mért) | nem ellenőrzött | nem releváns | „Soon available” (mért) |
| AWS eu-west-2 / ap-northeast-1 | nem ellenőrzött | nem ellenőrzött | London / Tokió (mért) | Polymarket / Binance közelében (mért) | Kripto és predikciós botokhoz |

## 3. Hardver – három árszint (ipon.hu árak, 2026-11-15)

Minden alkatrészár **mért** (ipon.hu; a 2. szintű kereskedőgép NIC-je amazon.de-ről, USD-ben). Az összegek a részárak összeadásából **becsültek** (ház, hűtő, OS nélkül).

### 3.1 Kereskedőgép (alacsony késleltetés)

| Szint | CPU | Alaplap | RAM | NVMe | NIC | Táp | Összesen |
|---|---|---|---|---|---|---|---|
| 1 – belépő | Ryzen 7 9700X 107 989 Ft (mért) | ASRock B850M Pro RS 52 690 Ft (mért) | 32 GB DDR5-6000 279 790 Ft (mért) | 990 PRO 2 TB 184 989 Ft (mért) | Intel X710-DA2 115 590 Ft (mért) | 1000 W Gold 34 190 Ft (mért) | 775 238 Ft ≈ 2120 EUR (becsült) |
| 2 – közép | Ryzen 9 9950X3D 255 090 Ft (mért) | MSI PRO X870E-S 97 890 Ft (mért) | 64 GB DDR5-6000 CL30 501 390 Ft (mért) | 9100 PRO 4 TB 346 490 Ft (mért) | Mellanox CX-4 Lx 2×25G 168,37 USD (mért, amazon.de) | be quiet! 1000 W 45 991 Ft (mért) | 1 302 548 Ft ≈ 3563 EUR (becsült) |
| 3 – prémium | Ryzen 9 9950X3D2 339 990 Ft (mért) | ASUS ROG Strix X870E-H 109 990 Ft (mért) | 128 GB DDR5-5600 1 023 590 Ft (mért) | 2× 9100 PRO 4 TB 692 980 Ft (mért) | NVIDIA ConnectX-7 25G 442 290 Ft (mért); Solarflare nem ellenőrzött | Lian Li SX 1000 W Platinum 50 289 Ft (mért) | 2 659 129 Ft ≈ 7273 EUR (becsült) |

PTP: a fenti NIC-ek hardveres időbélyeget támogatnak (nem ellenőrzött típusonként); GPS/PTP grandmaster ára nem ellenőrzött. Kernelhangolás (isolcpus, IRQ affinity, C-state tiltás) leírása nem ellenőrzött ebben a körben. Egy Vantage MT5 retail számlához saját gép helyett LD/NY VPS kell; saját gép csak colocationben vagy FIX/kripto végrehajtáshoz éri meg (becsült).

### 3.2 Kutató / ML munkaállomás

| Szint | CPU | Alaplap | RAM | GPU | NVMe | HDD (tickadat) | Táp | Összesen |
|---|---|---|---|---|---|---|---|---|
| 1 | Ryzen 9 9950X3D 255 090 Ft (mért) | MSI PRO X870E-S 97 890 Ft (mért) | 128 GB DDR5-5600 1 023 590 Ft (mért) | RTX 5070 Ti 16 GB 579 990 Ft (mért) | 990 PRO 4 TB 290 090 Ft (mért) | 2× Toshiba MG10 22 TB 788 980 Ft (mért) | 1000 W 45 991 Ft (mért) | 3 081 621 Ft ≈ 8429 EUR (becsült) |
| 2 | Threadripper 9960X 632 390 Ft (mért) | ASRock TRX50 WS 246 990 Ft (mért) | 128 GB DDR5-6400 RDIMM ECC 2 582 290 Ft (mért) | RTX 5090 32 GB 3 418 390 Ft (mért) | 2× 9100 PRO 4 TB 692 980 Ft (mért) | 4× MG10 22 TB 1 577 960 Ft (mért) | 1600 W 49 790 Ft (mért) | 9 200 790 Ft ≈ 25 166 EUR (becsült) |
| 3 | Threadripper 9970X 1 061 890 Ft (mért) | ASUS Pro WS TRX50-SAGE 312 190 Ft (mért) | 256 GB RDIMM ECC 5 164 580 Ft (mért, 2 kit) | RTX PRO 6000 Max-Q 96 GB 6 743 290 Ft (mért) | 2× 9100 PRO 4 TB 692 980 Ft (mért) | 8× MG10 22 TB 3 155 920 Ft (mért) | 1000 W 45 991 Ft (mért) | 17 176 841 Ft ≈ 46 983 EUR (becsült) |

EU-s összevetés (alternate.de, mért): Ryzen 9 9950X3D 579 EUR; RTX 5090 (INNO3D X3) 8877 EUR; RTX PRO 6000 Max-Q 17 850 EUR; 64 GB DDR5-6000 1336 EUR; Exos X24 24 TB 1235 EUR. A pcx.hu, aqua.hu, alza.hu, arukereso.hu és a mindfactory.de árai gépileg nem voltak olvashatók (nem ellenőrzött).
Bérelt alternatíva (mért): Hetzner AX102 159 EUR/hó, GEX45 (24 GB GPU) 214 EUR/hó, GEX63 (96 GB GPU) 999 EUR/hó.

## 4. Relokációs mátrix

Késleltetés: WonderNetwork város–város átlagping 2026-11-15 (mért); Monaco és Andorra proxyval (becsült). Megélhetés: Eurostat PLI 2024, EU27 = 100 (mért); ahol nincs adat: nem ellenőrzött.

| Ország | Tőzsdei/CFD/forex nyereség | Kripto | Fogadás / predikciós piac | Illetőség | Bróker, tőkeáttétel | LD / NY / TY (ms) | Megélhetés (PLI) | Szabályozói megjegyzés |
|---|---|---|---|---|---|---|---|---|
| Magyarország | ETÜ 15%, szocho nincs (mért); offshore CFD ≈ 24,9% egyéb jövedelem (becsült) | 15%, szocho nincs, korlátlan veszteségkiegyenlítés (mért) | Engedélyes: mentes (mért); Polymarket blokkolva (mért) | 183 nap / állandó lakóhely (nem ellenőrzött) | ESMA 30:1 (mért); offshore 1:500 (mért, Vantage) | 27,9 / 107,6 / 237,7 (mért) | 68,3 (mért) | NAV CRS-alapú vizsgálat (mért) |
| Ciprus | Értékpapír és származékos „titles” mentes (mért); CFD/forex nincs nevesítve (nem ellenőrzött) | 8% flat (mért) | nem ellenőrzött | 183 nap vagy 60 napos szabály (mért) | CySEC, ESMA 30:1 (mért) | 64,2 / 171,5 / 302,9 (mért, Limassol) | 95,1 (mért) | Non-dom: osztalék és kamat SDC-mentes (mért) |
| Málta | Részvény/értékpapír: marginális kulcs (mért); non-dom külföldi nyeresége nem adózik (mért) | nem ellenőrzött | nem ellenőrzött | nem ellenőrzött | MFSA, ESMA 30:1 (becsült) | 43,9 / 113,8 / 244,5 (mért) | 93,1 (mért) | Remittance basis (mért) |
| Portugália | 28% flat (mért) | nem ellenőrzött | Polymarket blokkolva (mért, sajtó) | IFICI: előtte 5 évig nem rezidens (mért) | ESMA 30:1 (becsült) | 47,9 / 114,6 / 279,7 (mért) | 85,0 (mért) | NHR 2024-től megszűnt; IFICI csak jogosult tevékenységre (mért) |
| Svájc | Magán árfolyamnyereség mentes, ha nem hivatásos kereskedő (mért) | nem ellenőrzött | nem ellenőrzött | nem ellenőrzött | FINMA, tőkeáttétel nem ellenőrzött | 21,1 / 90,7 / 225,8 (mért, Zürich) | 184,3 (mért) | Hivatásos minősítés kockázata grid EA-nál (becsült) |
| EAE (Dubaj) | Nincs szja (mért); üzleti tevékenységre 9% CT > 1 M AED forgalom felett (mért) | Nincs szja (mért) | nem ellenőrzött | nem ellenőrzött | DFSA/SCA, nem ellenőrzött | 184,8 / 255,5 / 248,2 (mért) | nem ellenőrzött | HU–EAE egyezmény van (mért) |
| Szingapúr | Magánbefektetés: általában nem adóköteles (mért) | Digitális token ugyanígy (mért) | Polymarket close-only (mért) | nem ellenőrzött | MAS, nem ellenőrzött | 154,8 / 222,4 / 66,1 (mért) | nem ellenőrzött | Üzletszerű kereskedés adóköteles lehet (nem ellenőrzött) |
| Egyesült Királyság | CGT 18% / 24% (mért); spread betting mentessége nem ellenőrzött | CGT (nem ellenőrzött) | Fogadás mentes (mért); Polymarket close-only (mért) | nem ellenőrzött | FCA 30:1 (nem ellenőrzött) | 0,1 / 70,1 / 232,8 (mért) | 129,1 (mért) | Non-dom megszűnt, 4 éves FIG (mért) |
| Írország | CGT 33%, 1270 EUR mentesség (mért) | nem ellenőrzött | Engedélyes lottó mentes (mért); Polymarket csak frontend-korlát (mért) | Remittance basis non-domnak (mért) | ESMA 30:1 (becsült) | 10,9 / 84,1 / 252,8 (mért) | 141,2 (mért) | eu-west-1 a Polymarkethez (mért) |
| Észtország | 22% (mért); befektetési számla halasztás (mért) | nem ellenőrzött | nem ellenőrzött | nem ellenőrzött | ESMA 30:1 (becsült) | 43,9 / 91,3 / 264,3 (mért) | 96,5 (mért) | 2026-os kulcs: nem ellenőrzött |
| Grúzia | Területi elv: nem grúz forrás mentes (mért); flat 20% (mért) | nem ellenőrzött | nem ellenőrzött | 183 nap / 12 hónap (mért) | Offshore elérhető (becsült) | 75,4 / 149,1 / 296,8 (mért) | nem ellenőrzött | Forrás-szabály CFD-re vitatható (becsült) |
| Monaco | Nincs szja, kivéve francia állampolgárok (nem ellenőrzött) | nem ellenőrzött | Kalshi korlátozott (nem ellenőrzött) | nem ellenőrzött | nem ellenőrzött | ≈17 / 84 / 226 (becsült) | nagyon magas (becsült) | Nincs HU egyezmény a listán (mért) |
| Puerto Rico | Act 60: kamat, osztalék mentes; tőkenyereség mentes vagy csökkentett (mért) | nem ellenőrzött | Kalshi USA-ban szabályozott (becsült) | Előtte 10 évig nem rezidens; belépés 2035-12-31-ig (mért) | US-szabályok, CFD nem (nem ellenőrzött) | 121,0 / 71,3 / 215,4 (mért) | nem ellenőrzött | Mentesség 2035-12-31-ig (mért) |
| Andorra | Max. 10% szja (nem ellenőrzött) | nem ellenőrzött | nem ellenőrzött | nem ellenőrzött | AFA, nem ellenőrzött | ≈25 / 100 / 264 (becsült) | nem ellenőrzött | HU–Andorra egyezmény (mért) |
| Bulgária | 10% flat, éves nettósítás; EU-s szabályozott piaci részvény mentes (mért) | nem ellenőrzött | nem ellenőrzött | nem ellenőrzött | ESMA 30:1 (becsült) | 40,5 / 119,0 / 263,9 (mért) | 56,9 (mért) | Devizaügylet is 10% (mért) |
| Csehország | 3 év tartás után mentes; 2026-tól plafon nélkül (mért) | 40 M CZK-s limit marad (mért) | Polymarket tiltólistán (mért, sajtó) | nem ellenőrzött | ESMA 30:1 (becsült) | 27,3 / 101,6 / 241,9 (mért) | 80,2 (mért) | CFD/forex nincs adat (nem ellenőrzött) |
| Szlovákia | Jegyzett részvény > 1 év mentes (mért) | nem ellenőrzött | „Winnings” adóköteles (mért); Polymarket close-only (mért) | nem ellenőrzött | ESMA 30:1 (becsült) | 27,4 / 97,0 / 259,4 (mért) | 81,1 (mért) | Osztalék 7% (mért) |
| Ausztria | 27,5% (értékpapír, derivatíva) (mért) | 27,5%; kripto–kripto csere nem adóesemény (mért) | Fogadási nyeremény mentes (mért) | nem ellenőrzött | ESMA 30:1 (becsült) | 26,2 / 101,7 / 249,4 (mért) | 119,7 (mért) | Veszteség csak az adott évben (mért) |

## 5. Magyar adó-összefoglaló (magánszemély)

| Jövedelem | Minősítés | Kulcs | Szocho | Veszteség | Forrás (id) |
|---|---|---|---|---|---|
| CFD/forex EGT-s (vagy OECD-s, illetve egyezményes és felügyelt) brókernél | ETÜ, Szja 67/A (mért) | 15% (mért) | nincs (mért) | Tárgyév + 2 előző év adókiegyenlítés (mért) | hu-szja-tv-67a-etu, hu-szja-tv-67a-6-adokiegyenlites |
| CFD/forex nem EGT-s, nem OECD-s, egyezmény nélküli államban működő brókernél (pl. Mauritius/Kajmán/Vanuatu) | Nem ETÜ (mért feltétel) → egyéb jövedelem (becsült) | 15% a 89%-on (mért szabály, becsült alkalmazás) | 13% a 89%-on, felső határ nélkül (becsült) | Nincs elhatárolás (becsült) | hu-szja-tv-29-egyeb-jovedelem, hu-dtt-lista-kozbeszerzes-2026 |
| Külföldi brókernél önadózás | Bevallás saját nyilvántartás alapján (mért, 67/A (5)) | – | – | – | hu-szja-tv-67a-etu |
| Kriptoeszköz-ügylet | Szja 67/C (mért) | 15% (mért) | nincs (mért) | Korlátlan időbeli kiegyenlítés, de max. az adóév és 2 előző év adója; nyilvántartás kötelező (mért) | hu-szja-tv-67c-kripto, hu-2025-lxxxiii-kripto-veszteseg |
| Kis értékű kripto | Mentes, ha ügyletenként ≤ minimálbér 10%-a és évente ≤ minimálbér (mért) | – | – | – | hu-szja-tv-67c-kripto |
| Engedélyes szerencsejáték/fogadás | Nem jövedelem, 76. § (4) (mért) | 0 (mért) | – | – | hu-szja-tv-76-nyeremeny |
| Engedély nélküli külföldi fogadóiroda / Polymarket | Nem „jogszerűen szervezett” → nem mentes (becsült) | nem ellenőrzött (valószínűleg egyéb jövedelem) | nem ellenőrzött | – | hu-szja-tv-76-nyeremeny, sztfh-polymarket-block-2026 |
| Alacsony adókulcsú államból származó osztalék, kamat, árfolyamnyereség | Egyéb jövedelem (mért, PwC) | 15% (mért) | 13% (mért) | – | hu-alacsony-adokulcsu-allam |
| Kft. (TAO) | 9% társasági adó (mért), majd osztalék | 9% + 15% szja (mért) | 13% az osztalékra, felső határig (mért) | Elhatárolás: nem ellenőrzött | hu-tao-tv-19-9szazalek |
| KIVA | 10% a kivett jövedelemre; TAO és szocho helyett (mért) | 10% (mért) + 15% szja az osztalékra (becsült) | a tagnál felső határig (becsült) | nem ellenőrzött | hu-kiva-katv-21-10szazalek |

Hatásos teher 100 egység nyereségre (becsült): ETÜ 15; offshore CFD egyéb jövedelemként ≈ 24,9; kripto 15; Kft. + osztalék ≈ 34,5 (a szocho felső határa felett ≈ 22,7); KIVA + osztalék ≈ 10 + 13,5 + szocho.

Szabályozási kulcspontok (mért): ESMA lakossági limitek: 30:1 fő devizapár, 20:1 egyéb devizapár, arany és fő index, 10:1 egyéb nyersanyag, 5:1 részvény, 2:1 kripto; 50%-os margin close-out; negatívegyenleg-védelem. Szakmai ügyfél: 3 feltételből 2 (negyedévente átlagosan 10 jelentős ügylet 4 negyedéven át; 500 000 EUR feletti portfólió; legalább 1 év pénzügyi szakmai munka). Vantage stop-out 20% (mért). NAV: CRS/DAC2 adat-összevetés és jogkövetési vizsgálat 2025 novemberétől (mért). DAC8 és MiCA részletei nem ellenőrzöttek (az EUR-Lex nem volt letölthető).
