# A2 – Kripto (M1, M6, M8 kripto-rész): összefoglaló

Ellenőrzés dátuma: 2026-11-15. Kimenet: `a2_crypto.jsonl`, **133 tétel**. Ebből verified = mért: 81, becsült: 24, nem ellenőrzött: 28.
Tier: 0 = 15, 1 = 36, 2 = 45, 3 = 37. A GitHub-adat 44 tételnél mért: csillag ungh.cc tükörből, utolsó commit shallow git clone-ból.
Árfolyam: ECB 2026-11-13, 1 EUR = 1,1052 USD. Az EUR/hó érték az USD-árból becsült átváltás.

## Kategóriák
- CEX/DEX API és rate limit (12), infrastruktúra/colocation/node (21), piaci tick/L2 (12), derivatíva-adat (3)
- On-chain (20), MEV/mempool (12), DEX (2), OSS eszközök (14), stratégiák (10), irodalom (15), jog/adó HU+EU (12)

## Fő megállapítások
1. **Rate limitek (mért):**
   - Binance spot: 6000 weight/perc, 100 order/10 s, 200 000/nap (exchangeInfo a data-api.binance.vision-ön).
   - Bybit: 600 kérés/5 s/IP.
   - OKX: 1000 order/2 s alszámlánként.
   - Hyperliquid: 1200 weight/perc/IP, plusz címalapú limit, ahol 1 USDC forgalom = 1 kérés.
   - Kraken: számláló, 15–20, bomlással.
   - Deribit: kreditrendszer (becsült számok).
2. **A Binance API innen HTTP 451-et ad** (korlátozott hely). Másodlagos források szerint a Binance-nek nincs MiCA CASP-engedélye (2026-11). Magyar szereplőnek a Bybit EU, az OKX Europe, a Coinbase, a Kraken és a Bitstamp a jogilag tiszta CEX-út.
3. **Szerverhelyek** (főleg másodlagos/vendor források, becsült):
   - Binance és Hyperliquid: AWS Tokió (ap-northeast-1).
   - Bybit: Szingapúr. OKX: Hongkong.
   - Coinbase: AWS us-east-1 (2026-05-07-i postmortem).
   - Deribit Starbase: LD4 vagy AWS PrivateLink (mért doksi).
   - Európából Tokió kb. 240–270 ms: a latenciaérzékeny kripto-stratégiákhoz tokiói VPS kell.
4. **Adatforrás-gerinc:**
   - Ingyenes: data.binance.vision (mért mappák: USDⓈ-M bookDepth, metrics, fundingRate; COIN-M liquidationSnapshot; 2017-től) és public.bybit.com (2019-10-től).
   - Fizetős: Tardis.dev (Solo perp 700 USD/hó ≈ 633 EUR, mért) a tick/L2 standard.
   - Gyűjtés és szimuláció: cryptofeed és hftbacktest saját gyűjtéshez, illetve queue-szimulációhoz.
5. **Piaci konszolidáció 2025–26** (ezért a régi integrációk elavulnak):
   - A Talos megvette a Coin Metricset (2025-07-16).
   - A Kaiko megvette az Amberdatát (2026 jún.).
   - A Flipside Studio/API 2025-07-31-én leállt.
   - A CoinDesk Data (CCData) ingyenes API-ja 2026-05-21-én megszűnt.
6. **Derivatíva-adat (mért):**
   - CoinGlass: 273–6856 USD/év, kedvezményes időszakban mérve.
   - Laevitas: API csak az Enterprise csomagban, 500 USD/hó/seat.
   - CryptoQuant: on-chain API 99–109 USD/hó.
   - Glassnode: API csak Professional (584 USD/hó-tól) + add-on.
   - DefiLlama: az ingyenes API kulcs nélkül működik (mért), a Pro 300 USD/hó.
7. **Hyperliquid funding (mért doksi):**
   - Óránként fizet, 1/8 rátával.
   - Kamatkomponens 0,01%/8 h (11,6% APR).
   - Plafon 0,5%/óra.
   - Ez a cross-venue funding-spread stratégia alapja.
8. **Kulcsesemény:** 2025-10-10/11, ~19 Mrd USD likvidáció (CoinGlass szerint rekord), Hyperliquid ADL. Ez a likvidációs kaszkád stratégia és a stressz-forgatókönyv (M10) mintapéldája.
9. **Irodalom:** 25 cikk, a 15 irodalmi tétel és a 10 stratégia forrása együtt. arXiv-azonosítók az arXiv API-val, NBER-címek az oldalról ellenőrizve. Kettő SSRN (Griffin–Shams, Lehar–Parlour) nem ellenőrzött (403).

## Magyar és EU-s jog (verifikált állapot)
- **Kriptoadó:** 15% szja, Szja tv. **67/C. §** (nem 67/B). 2022-01-01 óta él (NAV, mért).
  - Kisösszegű mentesség: ügyletenként ≤ 20 000 Ft és évente ≤ 200 000 Ft (a NAV-oldal példája).
  - Veszteség: adókiegyenlítés 2 évre visszamenőleg.
  - Szocho: a NAV-oldal nem említi.
- **2025-ös validálási rezsim** (hatály 2025-07-01): kötelező validátor-igazolás és két Btk.-tényállás. Ennek nyomán a Revolut (2025-07-17), a MoonPay, a Strike és a Kriptomat kivonult.
- **Eltörlés:** parlamenti szavazás 2026-07-28 (143 igen, 46 nem, 1 tartózkodás), kihirdetés 2026-07-31 (sajtó). A törvényszámot nem sikerült elsődleges forrásból ellenőrizni.
- **Helyi engedély:** az MNB 2026-07-20-án első helyi MiCA-engedélyt adott (CoinCash/Tiwala Solutions, egy forrás szerint).
- **MiCA:** a grandfathering 2026-07-01-én lejárt.
- **ESMA (2026-02-24):** a perp CFD-nek minősülhet. Lakossági ügyfélnél ez a kripto-CFD 2:1 limitjét jelenti, ami alapjaiban érinti a perp-alapú stratégiákat EU-ból.
- **DAC8:** alkalmazás 2026-01-01-től, első adatcsere 2027-09-30-ig. A NAV minden EU-s CASP-ügyletet látni fog.

## Hiányok, forráskorlátos tételek
- **Keresési keret:** a WebSearch-keret a munka végén elfogyott (megosztott, 200 kérés/kör). Az ESMA interim regiszter pontos URL-jét és néhány árat ezért nem tudtam ellenőrizni.
- **Árak és limitek:**
  - Nem ellenőrzött ár: Kaiko, Amberdata, Velo, Dune (pontos csomagárak), Arkham API, Messari, Artemis, Allium, Bitquery és az RPC-szolgáltatók (Helius, Triton, QuickNode, Alchemy, Infura).
  - Nem ellenőrzött limit: Coinbase Advanced Trade rate limitek; Binance USDⓈ-M 10 másodperces order-limit; dYdX Indexer-limit (csak kliens-kódkommentből).
- **Szerverhelyek:** egyik tőzsde sem publikálja hivatalosan az AZ-t, mind becsült. Saját ping/RTT-mérés kell Tokióból, Szingapúrból, Hongkongból és Virginiából. A Kraken colocationjéről nincs forrás.
- **Magyar jogi pontok, jogászi ellenőrzést igényelnek:**
  - a perp/CFD jövedelem adóbeli minősítése (kriptoügylet vagy egyéb);
  - az MNB-féle esetleges derivatíva-korlát;
  - a 2026-os hatályon kívül helyező törvény száma és hatálybalépése;
  - a Revolut és a Bitstamp magyar újraindulása.
- **Mérési korlátok:**
  - Coin Metrics Community licenc és rate limit (CC BY-NC?), nem ellenőrzött.
  - A Tardis és a Binance tényleges fájlméretei (bytes_est) nincsenek mérve, mert a letöltés nem volt „kis próba”.
  - Opciós volatilitási prémium (Deribit DVOL) stratégia és cikk nincs felvéve, mert a keret elfogyott.
- **GitHub-licenc:** több repónál a GitHub nem azonosít licencet (cryptofeed, mempool, dydx, spellbook, pybit, python-okx, binance-public-data). Ezeknél a mező „nem azonosított”.
## Javasolt következő lépések
- Tokiói és szingapúri VPS-en latencia-próba (CCXT/Nautilus, p50/p99) a binance-, bybit-, okx- és hyperliquid-tételekhez.
- Az ESMA CASP-regiszter letöltése, és jogalanyonkénti ellenőrzés a „mica-engedelyes-tozsdek-hu” tételhez.
- Funding-adatcsomag: data.binance.vision fundingRate + Hyperliquid fundingHistory + Bybit. Erre jöhet a cross-venue spread backtest a díjakkal együtt.
