# A8 – Infrastruktúra, szerverhely, hardver, költözés, adó és szabályozás – táblák

Ellenőrzés napja: 2026-11-15. Árfolyam: EKB 2026-11-13, 1 EUR = 365,60 HUF = 1,1052 USD = 0,83559 GBP (mért).
Címkék: **mért** = forrásban vagy saját lekérdezéssel látott érték (jogszabálynál: a net.jogtar.hu hatályos szövege, 2026-11-15); **számolt** = mért bemenetből Pythonnal számolt; **becsült** = proxyból becsült; **következtetett** = a forrás szövegéből levont, de nem kimondott következmény; **nem ellenőrzött** = nem sikerült forrással igazolni.
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
| Magyarország | ETÜ 15%, szocho nincs (mért); offshore CFD ≈ 24,9% egyéb jövedelem (becsült) | 15%, szocho nincs, korlátlan időbeli veszteségkiegyenlítés, de legfeljebb a tárgyév és az előző két év kriptoadójáig (mért) | Engedélyes: nem jövedelem, 76. § (4) (mért); engedély nélküli szervező: a nyeremény címén kapott teljes bevétel jövedelem, 76. § (1) (szöveg: mért; alkalmazás: következtetett); Polymarket blokkolva (mért) | 183 nap / állandó lakóhely (nem ellenőrzött) | ESMA 30:1 (mért); offshore 1:500 (mért, Vantage – a Help Center szerint VIG Group, Mauritius FSC) | 27,9 / 107,6 / 237,7 (mért) | 68,3 (mért) | NAV CRS-alapú vizsgálat (mért) |
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
| CFD/forex MNB-felügyelt, vagy EGT-, OECD- vagy egyezményes államban működő, ott felügyelt brókernél (minden feltételt lásd 5.2) | ETÜ, Szja 67/A (mért) | 15% (mért) | nincs (mért) | Adókiegyenlítés 67/A (6)–(8) szerint: az adóévben és/vagy az előző két évben keletkezett, a keletkezés évének bevallásában feltüntetett veszteség × bevalláskori kulcs, legfeljebb az adóévben és/vagy az előző két évben bevallott ETÜ-jövedelem adója, a már érvényesített kiegyenlítéssel csökkentve (mért). Egy t. évi veszteség tehát a t., t+1. vagy t+2. évi bevallásban érvényesíthető, és a t−2…t+2 évek ETÜ-adójával szemben számolható el (összesen öt adóév); egy adott bevallásban legfeljebb a tárgyév és az azt megelőző két év ETÜ-adójáig (mért szöveg, net.jogtar.hu, 2026-11-15) | hu-szja-tv-67a-etu, hu-szja-tv-67a-6-adokiegyenlites |
| CFD/forex nem EGT-s, nem OECD-s, egyezmény nélküli államban működő brókernél (pl. Mauritius – a Vantage Help Center szerinti VIG Group; korábbi források szerint Kajmán/Vanuatu) | Nem ETÜ, mert a 67/A (3) b) pont államfeltétele nem teljesül (mért feltétel; Mauritius nincs a hatályos egyezmények listáján, mért) → egyéb jövedelem (becsült) | 15% a 89%-on (mért szabály, becsült alkalmazás) | 13% a 89%-on, felső határ nélkül (becsült) | Nincs elhatárolás (becsült) | hu-szja-tv-29-egyeb-jovedelem, hu-dtt-lista-kozbeszerzes-2026 |
| Külföldi brókernél önadózás | Bevallás saját nyilvántartás alapján (mért, 67/A (5)) | – | – | – | hu-szja-tv-67a-etu |
| Kriptoeszköz-ügylet | Szja 67/C (mért) | 15% (mért) | nincs (mért) | Korlátlan időbeli kiegyenlítés, de max. az adóév és 2 előző év adója; nyilvántartás kötelező (mért) | hu-szja-tv-67c-kripto, hu-2025-lxxxiii-kripto-veszteseg |
| Kis értékű kripto | Ügyleti bevételt nem kell megállapítani, ha (1) az ügyletből származó **bevétel** (nem a nyereség) ≤ a minimálbér 10%-a, (2) a bevétel megszerzésének **napján** más, azonos tárgyú ügyletből nem szerez bevételt, és (3) az adóévben az ilyen bevételek összege ≤ a minimálbér. Szja 67/C (2) utolsó mondata (mért, net.jogtar.hu, hatály 2026.X.1.–XII.31.). Ha bármelyik feltétel sérül, a mentesség az adott ügyletre nem jár (következtetett) | – | – | – | hu-szja-tv-67c-kripto |
| Engedélyes szerencsejáték/fogadás | Nem jövedelem, 76. § (4) (mért) | 0 (mért) | – | – | hu-szja-tv-76-nyeremeny |
| Engedély nélküli külföldi fogadóiroda | Nem „jogszerűen szervezett” → a 76. § (4) mentessége nem jár (következtetett). A 76. § (1) szerint a fogadásból származó nyeremény (adóköteles nyeremény) címén kapott **bevétel egészét** jövedelemnek kell tekinteni (mért, net.jogtar.hu, hatály 2026.X.1.–XII.31.): a teljes kifizetés a jövedelem, nem a tétekkel csökkentett nettó nyereség (következtetett a szövegből) | 15%, 8. § (1) (mért szöveg; a 76. §-ra alkalmazva következtetett). Külföldi, nem kifizető szervezőnél a bevallás módja nem ellenőrzött | nem ellenőrzött | Nincs nettósítás: a vesztes fogadások nem csökkentik a nyertesek jövedelmét (következtetett) | hu-szja-tv-76-nyeremeny |
| Polymarket (predikciós piac) | **Nyitott kérdés.** Lehetséges minősítések: fogadás → 76. § (1), teljes bevétel; kriptoeszközzel végrehajtott ügylet → 67/C (USDC-ben elszámolt pozíció); egyéb jövedelem. NAV-állásfoglalást nem találtunk (nem ellenőrzött) | nem ellenőrzött | nem ellenőrzött | a minősítéstől függ | hu-szja-tv-76-nyeremeny, sztfh-polymarket-block-2026 |
| Alacsony adókulcsú államból származó osztalék, kamat, árfolyamnyereség | Egyéb jövedelem (mért, PwC) | 15% (mért) | 13% (mért) | – | hu-alacsony-adokulcsu-allam |
| Kft. (TAO) | 9% társasági adó (mért), majd osztalék | 9% + 15% szja (mért) | 13% az osztalékra, felső határig (mért) | Elhatárolás: nem ellenőrzött | hu-tao-tv-19-9szazalek |
| KIVA | 10% a kivett jövedelemre; TAO és szocho helyett (mért) | 10% (mért) + 15% szja az osztalékra (becsült) | a tagnál felső határig (becsült) | nem ellenőrzött | hu-kiva-katv-21-10szazalek |

Hatásos teher 100 egység nyereségre (becsült): ETÜ 15; offshore CFD egyéb jövedelemként ≈ 24,9; kripto 15; Kft. + osztalék ≈ 34,5 (a szocho felső határa felett ≈ 22,7); KIVA + osztalék ≈ 10 + 13,5 + szocho.

Szabályozási kulcspontok (mért):
- **ESMA lakossági limitek:** 30:1 fő devizapár; 20:1 egyéb devizapár, arany és fő index; 10:1 egyéb nyersanyag; 5:1 részvény; 2:1 kripto. 50%-os margin close-out, negatívegyenleg-védelem.
- **Szakmai ügyfél (kérésre):** a három feltételből **legalább kettő** kell, egy önmagában nem elég (Bszt. 49. § (1), mért, net.jogtar.hu, 2026-11-15; MiFID II II. melléklet):
  - a) az előző egy évben negyedévente átlagosan legalább 10 ügylet, egyenként 40 000 EUR értékben, vagy az év során összesen 400 000 EUR értékben;
  - b) a pénzügyi eszközökből álló portfólió és a betétek együtt meghaladják az 500 000 EUR-t;
  - c) legalább 1 év releváns munkaviszony a pénzügyi szektorban.
  - Hatály: a Bszt. 49. § (1) a magyar befektetési vállalkozásokra vonatkozik; a CySEC-jogalanyok (Pepperstone EU, FP Markets EU) a ciprusi átültetést és saját „jelentős méret” definíciójukat alkalmazzák (pl. FP Markets: 1 lot, mért, a11-pro-fpmarkets-eu).
  - A szakmai minősítéssel megszűnik az ESMA lakossági tőkeáttételi limitje és az 50%-os close-out, és elveszhet a negatívegyenleg-védelem (mért, mifid2-annex-ii-professional-client).
  - **Megjegyzés** (számolt + következtetett): az A7-ben ajánlott ≤ 10× effektív tőkeáttétel a 30:1 lakossági limiten belül van; 1:30 mellett 10× effektív áttételnél a margin level 30/10 = 300%. Józan méretezéshez tehát a szakmai státusz ritkán szükséges. A magasabb brókeráttétel csak a nagyobb kitettséget engedi.
- **Stop-out mint brókerprofil-adat:** EU/UK lakossági számlán 50%, kötelező negatívegyenleg-védelemmel. Egyes offshore ECN-számlákon 20%: a Vantage globális Help Center szerint „all trading platforms” 20% (mért, cikk frissítve 2025-09-12). Ez példa, nem általános érték; a saját számla értéke a szerződésből és a terminálból olvasandó (A7 1.1).
- **NAV:** CRS/DAC2 adat-összevetés és jogkövetési vizsgálat 2025 novemberétől (mért).
- **MiCA** – (EU) 2023/1114 rendelet (mért, EUR-Lex szöveg, https://eur-lex.europa.eu/eli/reg/2023/1114/oj):
  - alkalmazandó 2024-12-30-tól, a III. és IV. cím (ART, EMT) 2024-06-30-tól (149. cikk);
  - a 2024-12-30 előtt nemzeti jog szerint működő kriptoszolgáltatók legfeljebb 2026-07-01-ig vagy az engedélyről szóló döntésig működhettek tovább; a tagállam ezt rövidíthette (143. cikk (3)).
- **DAC8** – a Tanács (EU) 2023/2226 irányelve a 2011/16/EU módosításáról (mért, EUR-Lex szöveg, https://eur-lex.europa.eu/eli/dir/2023/2226/oj):
  - átültetés 2025-12-31-ig, alkalmazás 2026-01-01-től;
  - a kriptoeszköz-szolgáltatók adatait a naptári év végét követő 9 hónapon belül kell cserélni.
  - A magyar átültető jogszabályt nem ellenőriztük (nem ellenőrzött).

### 5.1 Szerződő jogalany és befektetővédelem (Vantage példáján)

- **A Vantage globális Help Center** („Who is Vantage?”, frissítve 2026-11-05) ezeket a jogalanyokat sorolja fel (mért, Zendesk API):
  - VIG Group – Mauritius Financial Services Commission (FSC), licenc GB20026165;
  - Vantage Markets (Pty) Ltd – FSCA (Dél-Afrika), 51268;
  - Vantage Global Prime Pty Ltd – ASIC (Ausztrália), AFSL 428901.
- **VFSC (Vanuatu) és CIMA (Kajmán) jogalanyt a cikk már nem említ**; ezek korábbi forrásokból származnak (vantage-entities-helpcenter-2026).
- **A mérvadó forrás a saját Client Agreement.** A Help Center szerint is az ügyfélszerződésben megnevezett jogalany határozza meg a szabályokat és a védelmeket, és az egyik jogalany védelmei nem vonatkoznak automatikusan a másikra (mért). A súgó és ez a táblázat csak kiindulópont.
- **ETÜ-következmény:**
  - Mauritius nem EGT-állam, nem OECD-tag, és nem szerepel a Magyarországgal hatályos kettősadó-egyezményt kötött államok listáján (mért, Közbeszerzési Hatóság útmutató, 2026-05-21; hu-dtt-lista-kozbeszerzes-2026). Ezért a VIG Group-pal kötött CFD/forex ügylet nem ETÜ (következtetett a 67/A (3) b) pontból).
  - Dél-Afrika szerepel az egyezmény-listán (mért). Az FSCA-jogalanynál a bb) feltétel (FSCA–MNB információcsere) és a bc) feltétel nem ellenőrzött.
  - Ausztrália OECD-tagállam, és szerepel az egyezmény-listán (a lista: mért). Hogy az ASIC-jogalany magyar ügyfelet fogad-e, nem ellenőrzött.
- **BEVA (Befektető-védelmi Alap):** a kártalanítás felső határa személyenként és Alap-tagonként összevontan **100 000 EUR**. 1 millió Ft-ig 100%-os, felette 1 millió Ft és az e feletti rész 90%-a.
  - Forrás: Tpt. (2001. évi CXX. tv.) 217. § (2); megállapította a 2015. évi LXXXV. tv. 18. § (1), **hatályos 2016-01-01-től** (mért, net.jogtar.hu, 2026-11-15).
  - A korábbi „20 000 EUR” érték téves BEVA-ra. A Tpt.-ben 20 000 EUR csak a 2007-12-31-ig tartó EU-csatlakozási átmeneti szabályban szerepel (415. § (2) b), mért). A katalógus investor-protection-offshore-vs-eu tételét ehhez kell igazítani.
  - A BEVA csak a tagjai (magyar engedélyes befektetési vállalkozások) ügyfeleit védi. Mauritiusi, dél-afrikai vagy más EGT-n kívüli jogalanynál nem alkalmazandó (következtetett).

### 5.2 Az ETÜ összes feltétele – Szja 67/A (3) (mért, net.jogtar.hu, hatály 2026.X.1.–XII.31.)

**Az ügylet tárgya és módja:**
- befektetési szolgáltatóval vagy annak közreműködésével kötött ügylet;
- csereügyletnek nem minősülő pénzügyi eszközre (a zárt körben kibocsátott értékpapír kivételével) vagy árura; vagy pénzügyi elszámolással lezáródó azonnali deviza/valuta-ügylet;
- megfelel az ügyletre vonatkozó törvényi előírásoknak;
- nem ETÜ az az ügylet, amelynél a magánszemély vagy vele érdekközösségben lévő személy által meghatározott, a szokásos piaci értéktől eltérő árat alkalmaznak.

**Emellett a következők egyike teljesül:**
- **a)** az MNB (Felügyelet) által felügyelt tevékenység tárgya; **vagy**
- **b)** EGT-államban, OECD-tagállamban vagy olyan államban működő befektetési szolgáltatóval (közreműködésével) kötötték, amellyel Magyarországnak kettős adóztatást elkerülő egyezménye van, **és** együttesen:
  - **ba)** az adott állam hatáskörrel rendelkező felügyeleti hatósága felügyeli;
  - **bb)** nem EGT-állam esetén biztosított az információcsere az adott felügyeleti hatóság és az MNB között;
  - **bc)** a magánszemély rendelkezik a szolgáltató által a nevére kiállított igazolással, amely az adóévben megkötött **valamennyi ügylet minden**, az adókötelezettséghez szükséges adatát tartalmazza.

**Bevallás és veszteség:**
- Külföldi, nem kifizető szolgáltatónál önadózás saját nyilvántartás vagy a szolgáltatói bizonylatok alapján (67/A (5) b)).
- Veszteség: lásd az 5. tábla ETÜ-sorát (67/A (6)–(8)).

### 5.3 Magyar kripto-validálási rezsim – dátumok (az A2 ágenssel összehangolva)

| Esemény | Dátum | Forrás / címke |
|---|---|---|
| A validálási kötelezettség és a két új Btk.-tényállás hatálybalépése | **2025-07-01** | A2: hu-kripto-validalas-2025-hatalyon-kivul-2026 (The Block; sajtó) |
| A Revolut felfüggeszti a kriptoszolgáltatást Magyarországon | **2025-07-04/05** | hvg, 2025-07-05 (az átnéző forrásmegjelölése; saját letöltéssel nem ellenőrzött) |
| A Revolut teljes kivonulása, a kriptoszámlák lezárása (külön esemény) | **2025-12-18** | a8 hu-kriptotorveny-2024-vii-validalas (sajtó) |
| Az Országgyűlés elfogadja a visszavonó törvényt (143 igen, 46 nem) | **2026-07-28** (sajtójelentés) | A2 és a8 egyezik (sajtó) |
| Kihirdetés a Magyar Közlönyben | 2026-07-31 | A2 (sajtó), nem ellenőrzött |
| Hatálybalépés | forrásonként eltér (a Pénzcentrum szerint 2026-08-07) | nem ellenőrzött, a Magyar Közlönyben ellenőrizendő |
