# A4 – Makró, statisztika, hírek, alternatív adat, magyar források (M2, M3, M4)

Ellenőrzés napja: 2026-11-15. Kimenet: `a4_macro_news_alt.jsonl`, **298 tétel**, egyedi id-kkel, a variánsok `group` mezővel összefogva.

## Számok
- Kategóriák: M3 makró/statisztika 143, M2 fundamentális/szabályozói 66, M4 hírek/szentiment 46, M3 alternatív adat 43.
- Szint: 0 = 33, 1 = 79, 2 = 103, 3 = 83.
- Hozzáférés: free 193, freemium 38, paid 28, institutional 24, registration 15.
- `verified`: mért 233, becsült 51, nem ellenőrzött 14.
- Magyar vonatkozású (`regions` tartalmazza a `hu`-t): 57 tétel, ebből 19 kifejezetten magyar forrás.
- Átváltás: 1 EUR = 1,1052 USD (ECB-referencia, 2026-11-13, az ECB API-ból mérve); 1 GBP = 1,1965 EUR (MNB-keresztárfolyam, mérve). Az `EUR/hó` mező mindig az árszöveg mért vagy becsült címkéjét örökli.

## Módszer
- Kb. 600 URL-t ellenőriztem curl-lel, kis GET-kérésekkel. A bot-UA-ra 403-at adó oldalakat (SEC, BLS, Bloomberg, Benzinga, FMP, Investing, Forex Factory) WebSearch-csel igazoltam, és `becsült` címkét kaptak.
- Az árakat WebFetch-csel a hivatalos árlapról vettem (`mért`), vagy keresési kivonatból (`becsült`).
- Mért árak: NewsAPI, Tiingo, Alpha Vantage, Massive/Polygon, Marketaux, StockNewsAPI, GNews, TheNewsAPI, Perigon, NewsAPI.ai, EODHD, sec-api.io, Coresignal, Open-Meteo limitek, X API pay-per-use.
- Élő API-próbák (működnek): MNB SOAP (`arfolyamok.asmx`), ECB SDMX, Eurostat, World Bank, GDELT DOC 2.0, SEC XBRL frames, KSH HVD API (13 adatkészlet), faireconomy (Forex Factory) heti JSON, benne forecast és previous mezőkkel.
- A GitHub API a sandboxból tiltott volt, ezért csillagszámot nem mértem (kivétel: edgartools ~2,9k, WebFetch-csel). Helyette a PyPI utolsó kiadási dátumát mértem 50+ csomagra, ez a jegyzetekben szerepel.

## Fontos tények (mért)
- A Polygon.io 2025-10-30 óta **Massive.com** néven fut. A régi `api.polygon.io` átmenetileg még működik.
- Az **X API** 2026-02-06 óta pay-per-use: 0,005 USD/post-olvasás, havi 3 millió post plafon. 1 millió post olvasása kb. 4525 EUR.
- A **Google Trends API** 2025-07-24 óta zárt alfában fut: konzisztens skálázás, kb. 5 éves ablak. A pytrends 2023 óta nem frissül.
- Az **IMF** régi adatportálja 2025-11-05-én megszűnt. Az új SDMX 3.0 végpont: `api.imf.org/external/sdmx/3.0` (forrása becsült).
- A **NewsAPI** ingyenes csomagja productionben (belső használatra is) tilos.
- Az **Open-Meteo** ingyenes szintje csak nem kereskedelmi célra használható.
- Az **OSAP** 2026-10-28-án frissült (CRSP v2, Hugging Face terjesztés). A **JKP** 153 faktor, 93 ország, 2026 áprilisi frissítés.
- A **HUPX** adatcsomagjai a HUPX Labs-ra költöztek (API, sFTP), árat nem közölnek.
- Az **MNB**-nek nincs dokumentált statisztikai REST/SDMX API-ja (csak az árfolyam-SOAP). A **KSH** HVD API kulcs nélküli, de csak 13 adatkészletet ad.

## TOP 10 (a platform szempontjából; FX/MT5 és makró-kockázat fókusz)
1. **ALFRED + FRED** (`alfred-vintages`, `fred-api`): vintage-alapú, look-ahead-mentes makró-backtest. Ingyenes.
2. **Gazdasági naptár konszenzussal**: `forex-factory-calendar` (ingyenes JSON) és `trading-economics-api` (fizetős, historikus naptár). Ezek a hírkereskedés és a saját meglepetés-index alapjai.
3. **Jegybanki kommunikáció**: `fed-speeches-fomc`, `ecb-speeches-accounts`, `bis-cb-speeches`, `mnb-monetaris-politika`, valamint a címkézett `hf-fomc-communication`. Belőlük LLM/embedding-alapú hawkish/dovish jel építhető.
4. **CFTC COT** (`cftc-cot`): FX- és nyersanyag-pozicionálás, crowding.
5. **ECB Data Portal + Eurostat + BIS** (`ecb-data-portal`, `eurostat-api`, `bis-data-portal`): EUR- és régiós makró, REER, €STR.
6. **Magyar mag**: `mnb-arfolyam-soap`, `akk-statisztika` (referenciahozamok, aukciók), `ksh-stadat`. Ez a forint- és BUBOR-környezet.
7. **SEC EDGAR család** (`sec-edgar-data-api`, `sec-xbrl-frames`, `sec-insider-transactions-data-sets`, `edgartools`): ingyenes, pont-idejű fundamentumok és bennfentes kereskedés.
8. **Faktoradatok** (`ken-french-data-library`, `jkp-global-factor-data`, `open-source-asset-pricing`, `aqr-datasets`): a kutatási benchmark és a McLean–Pontiff lecsengés mérése.
9. **Energia és időjárás lánc** (`entsoe-transparency`, `gie-agsi-alsi`, `eia-open-data`, `ecmwf-open-data`, `copernicus-cds-era5`): ebből építhető az időjárás → energia → deviza jel.
10. **GDELT + CC-NEWS + FNSPID** (`gdelt`, `common-crawl-news`, `fnspid`): ingyenes hírkorpusz eseménytanulmányokhoz és LLM-hírértelmezéshez.

Fizetős „ár/érték” ajánlások:
- Newsquawk Basic: ~199 EUR/hó (becsült).
- Benzinga news Massive-en: 99 USD/hó (mért).
- Tiingo Power: 30 USD/hó (mért).
- sec-api.io: 49 USD/hó (mért).

## Az 5 legnagyobb hiány
1. **Historikus konszenzus és meglepetés-adat olcsón**: nincs megbízható, ingyenes, pont-idejű konszenzus-archívum. A Bloomberg ECO és a Citi Surprise intézményi termék, a Forex Factory csak az aktuális hetet adja. A konszenzust naponta saját magunknak kell archiválni.
2. **Intézményi árak**: nem publikus és nem ellenőrzött az LSEG MRN, a RavenPack, a Kpler/Vortexa, a MarineTraffic-kreditek, a kártyás költési panelek, a BÉT díjtáblázata és a HUPX adatcsomagjai. Ezekhez ajánlatkérés kell.
3. **GitHub-mérések**: csillagszám és utolsó commit a sandbox GitHub-tiltása miatt nincs. Ezt egy GitHub-hozzáféréssel rendelkező futásban pótolni kell (a PyPI-dátumok csak közelítést adnak).
4. **Magyar gépi hozzáférés**: nincs MNB statisztikai API, a KSH API szűk, a BÉT és a KELER adat-API-ja nem ellenőrzött, a STATINFO-ban átirányítási hurok van. A magyar makró legjobb gépi útja jelenleg az Eurostat, az ECB és a BIS SDMX, plusz az MNB SOAP és a KSH STADAT.
5. **Ellenőrizetlen vagy változó források**:
   - A Ken French oldal a sandboxból 503-at adott.
   - A FinancialJuice ára, a StockTwits API státusza és a Reddit API állítólagos 2026-10-31-i változása nem ellenőrzött.
   - A Benzinga Pro és a Newsquawk ára csak keresési kivonatból származik.
   - A közösségimédia-API-k (X, Reddit) ára és hozzáférése gyorsan romlik.

## Buktatók (összefoglalva)
- **Look-ahead**: a FRED, az Eurostat, a KSH és az OECD CLI revideált adatot ad. Csak az ALFRED, a Philly RTDSM és a saját napi pillanatképek pont-idejűek.
- **ÁSZF**: a következőknél tilos a scraping, vagy a használatot licenc köti: Forex Factory, Investing.com, Seeking Alpha, X, Reddit. Kereskedelmi célra nem használható: NewsAPI Dev, Open-Meteo free, OpenSky, JKP (CC BY-NC), Tiingo Starter/Power.
- **Késleltetés**: a BLS, EIA és USDA API-ja percekkel a kiadás után frissül. Hírkereskedéshez squawk vagy newswire kell.
- **Promptinjekció**: minden hír- és közösségimédia-szöveget szanitizálni kell, mielőtt LLM-ágens kapja meg.
- **Edge-lecsengés**: a publikált jelek (insider, WSB, Google Trends, szentiment-faktorok) gyengülnek a publikálás után.
