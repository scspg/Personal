# A10 – Bevált módszerek: statisztikai összefüggésekből értelem és eredmény (M16)

Ellenőrizve: 2026-11-15. Kimenet: `a10_methods.jsonl`, 186 tétel: 115 esettanulmány (`cat: case_study`) és 71 módszer (`cat: method`).
A források ellenőrzése: Crossref DOI-k, arXiv API, Wikipedia-kivonatok, PyPI JSON, ungh.cc (csillagok és pushedAt), Kaggle-oldalcímek.
Az eredmények címkéje: `result_verified` = mért 82, becsült 16, nem ellenőrzött 17. A legendákat a `result_hu` mező külön jelöli.

## 1. Visszatérő minták: mit csinált jól minden sikeres eset

1. **A piaci árat priorként kezelték, nem ellenfélként.** Benter a saját logitját a totalizátor-oddsszal kombinálta. Kaunitz és társai a konszenzus-oddsot vették „igazságnak”. Az IEM és a GJP aggregált. A modell csak a reziduált keresi. (mért)
2. **Sok gyenge, alacsonyan korreláló jelet kombináltak, nem egy erőset.** Példák: a 101 alfa (páronkénti korreláció 15,9%), a Medallion-elv, a Netflix-blend és az M4, ahol a 17 legjobb módszerből 12 kombináció volt. Ide tartozik Turing log-odds („ban”) összegzése is.
3. **Az előnyt állapotfüggően méretezték.** Ilyen Thorp és a Kelly-elv, a „big player” az MIT-csapatban, és a Cash WinFall roll-down hetei. Akkor fogadtak nagyot, amikor az előny mérhetően pozitív volt.
4. **Strukturális okot kerestek, nem csak korrelációt.** Ilyen a tőkeáttétel-korlát (BAB), a carry kockázati prémiuma, a figyelemkorlát (Cohen–Frazzini, Lazy Prices) és a mechanikus árhatás (OFI, aukció-imbalance). A klasszikus példák is ezt mutatják: Snow, Doll–Hill, Fisher.
5. **Mérhető visszajelzést és kemény verifikációt használtak.** Ilyen a Brier-pontozás (GJP), az ECMWF napi verifikációja, az élő értékelés a Kaggle privát ranglistáján és az M6-ban, és a záróvonal-érték (CLV) a sportban.
6. **A hiányzó és kiválasztott adatot explicit modellezték.** Wald túlélési torzítása, a Bayes-i keresés „nem találtuk” frissítése, a német tank-probléma kemény sorozatszámai, és Zillow győztes átka ellenpéldaként.
7. **Az adat nem volt manipulálható, és gyorsabb volt a hivatalosnál.** Példák: a Billion Prices Project, az éjszakai fények, a műholdas parkolók és tartályok, a nowcast DFM és Srivastava „generátor-nyoma”.
8. **Kapacitás- és elterjedés-tudatosak voltak.** A Medallion 1993 óta zárt. A Moneyball-előny akkor tűnt el, amikor a liga lemásolta. McLean–Pontiff szerint publikálás után ~58%-kal kisebb a hozam. Neely és társai szerint az FX-szabályok a '90-es évek elejére kihaltak.

**A kudarcok közös oka:**
- Sok kipróbált változat után a legjobb kiválasztása: GFT, Bollen-féle Twitter, Preis „debt”, Leinweber vaja.
- Nyugodt időszakbeli korreláció válságra alkalmazva: LTCM, Gauss-kopula, quant quake 2007.
- Az adatforrás generáló algoritmusa megváltozott: GFT, Google Trends revíziók.
- Kedvezőtlen szelekció: Zillow.

## 2. „Másold, majd szárnyald túl” – a platform forgatókönyve

**A. Másolás (0–3. hónap): bizonyítottan működő, olcsó minták**
1. **Adatkapu.** Túlélési torzítástól mentes univerzumot használj, delistált coinokkal és lejárt instrumentumokkal. Az időbélyeg a közzététel idejét jelölje (vintage). Benford-szűrő kell a harmadik féltől vett volumenre.
2. **Validációs kapu.** Walk-forward és purged/embargoed CV, majd FDR (BH/BY), Hansen SPA, Deflated Sharpe és PBO. Minden kipróbálást naplózz (a GJP és a replikációs válság tanulsága).
3. **Alapjelek MT5-re.**
   - idősori momentum (MOP 2012);
   - carry a bróker swaptáblájával;
   - devizamomentum;
   - kointegrált párok Kalman-bétával;
   - HAR-RV volatilitás a grid-lépésközhöz.
4. **Rezsimkapcsoló a gridhez.** HMM/Markov-switching és BOCPD, a varianciahányados és a permutációs entrópia mint feature. A grid csak mean-reversion rezsimben fusson.
5. **Méretezés.** ¼–½ Kelly a Bayes-i előny-posterior alsó kvantilisével. Volatilitás-célzás és kitettségplafon kell, mert LTCM és a grid profilja egyformán „sokszor nyer, ritkán mindent veszít”.
6. **Sport és predikciós piac.** Benter-séma: a piaci valószínűség és a saját modell (Dixon–Coles + xG, Elo/Glicko, többkimenetű logit) kombinált p-t ad, ebből Kelly. A fő metrika a CLV és a Brier.

**B. Túlszárnyalás (3–12. hónap): ahol a régiek technológiailag korlátozottak voltak**
1. **Alfa-gyár.** A 101 alfa nyelvtanán GP (gplearn) és RL (AlphaGen) generál alfákat. A fitness a meglévő portfólióhoz adott walk-forward hozzájárulás, nem az egyedi IC. Minden alfa átmegy a DSR/FDR kapun.
2. **Oksági szűrés a feature-ökön.** PCMCI (Tigramite) és Granger/transfer entropy lead–lag háló. Csak a stabil oksági „ősök” mennek a GBM-be. A beavatkozások hatását DoWhy/EconML méri, például bróker-váltásét, VPS-költözését és spread-változásét.
3. **Döntési réteg (M9).**
   - A modellek és ágensek Brier/log-loss naplót vezetnek.
   - Az aggregálás log-odds átlaggal és extremizálással történik (GJP).
   - A súly az egyedi hozzájárulás (Numerai MMC-analógia).
   - A kimenet monoton, magyarázható scorecard: FICO-elv és SHAP.
4. **Lecsengés-kezelés élesben.** ADWIN/river drift, SPRT az új EA-kra, és champion–challenger kis tőkével (Bing A/B, Ubiquant „betting strategy”). SHAP-drift esetén újratanítás.
5. **Alt-adat óvatosan.**
   - nowcast DFM a makró-meglepetésre (USD, EUR, HUF);
   - online árak és inflációs nowcast;
   - LLM-hírpontszám (Lopez-Lira), szigorú tudásvágás-kezeléssel.
   Minden keresési és közösségi jel a GFT- és Bollen-kapun megy át: előre regisztrált lista, mintán kívüli teszt, forrásváltozás-teszt.
6. **Farokkockázat.** t/vine-kopula, RMT/Ledoit–Wolf kovariancia, MST-alapú klaszterszám és HRP a stratégia-allokációhoz. Ez a válságkorrelációt kezeli, a Gauss-kopula tanulsága alapján.

**C. Amit nem másolunk:**
- latency-arbitrázst (Budish: reménytelen és ÁSZF-ellenes);
- tiltott eszközöket (rulett-számítógép);
- bennfentes információt (Walters);
- kiskapu-bónuszok tömeges kihasználását ÁSZF-ellenőrzés nélkül.

## 3. Az első 15 megvalósítandó módszer (prioritás szerint)

| # | Módszer (jsonl id) | Miért első | Könyvtár |
|---|---|---|---|
| 1 | Purged/embargoed CV + walk-forward (`m-purged-cv-cpcv`) | Enélkül minden más eredmény hamis | skfolio, saját |
| 2 | FDR (`m-fdr-benjamini-hochberg`) + Harvey–Liu–Zhu t>3 | A jelgyár kapuja | statsmodels |
| 3 | Reality Check / SPA / StepM (`m-reality-check-spa-stepm`) | EA-paraméterkeresés után kötelező | arch |
| 4 | Deflated Sharpe + PBO (`m-deflated-sharpe`, `m-pbo-cscv`) | A backtest-szépítés mérése | saját, pypbo |
| 5 | Frakcionált Kelly (`m-kelly-criterion`) | Pozícióméret a grid-kockázathoz | numpy/cvxpy |
| 6 | GARCH/HAR-RV (`m-garch-har-rv`) | Grid-lépésköz, stop, vol-célzás | arch |
| 7 | HMM / Markov-switching rezsim (`m-hmm-regime`) | Grid ki/be kapcsoló | hmmlearn, statsmodels |
| 8 | BOCPD + ruptures (`m-bocpd`, `m-change-point-ruptures`) | Élő „vészfék” | saját, ruptures |
| 9 | Kointegráció + Kalman-béta + OU-félidő | Pár- és kosár-stratégiák MT5-ön | statsmodels, filterpy |
| 10 | LightGBM + SHAP (`m-gradient-boosting`, `m-shap`) | A Kaggle-győztesek alapja, magyarázattal | lightgbm, shap |
| 11 | Stacking/ensemble + extremizált aggregálás | M9 döntési réteg | mlxtend, saját |
| 12 | Kalibráció + Brier/log-loss (`m-calibration-proper-scoring`) | Ágens-értékelés és súlyozás | sklearn, scoringrules |
| 13 | Drift-detektálás + SPRT (`m-concept-drift-adwin`, `m-sprt-sequential`) | A lecsengés operatív kezelése | river, saját |
| 14 | PCMCI / Granger lead–lag (`m-pcmci-tigramite`) | Oksági feature-szűrés | tigramite (GPL!) |
| 15 | Bayes-i hierarchikus shrinkage (`m-bayesian-hierarchical`) | Kis mintás EA- és csapatbecslés, Kelly-posterior | pymc |

## 4. A 10 legjobban átvihető esettanulmány a platformra

`cs-benter-horse-racing`, `cs-kaunitz-beat-the-bookies`, `cs-aqr-time-series-momentum`, `cs-fx-carry-lustig`, `cs-gatev-pairs-trading`, `cs-avellaneda-lee-pca-statarb`, `cs-worldquant-101-alphas`, `cs-gjp-superforecasters`, `cs-kaggle-g-research-crypto`, `cs-fx-technical-rules-amh`. Az utolsó azért került ide, mert figyelmeztet: a klasszikus indikátor-EA-k előnye elfogyott.

## 5. Hiányok és korlátok

- **Kaggle-győztesek.** A Kaggle-diszkussziók tartalma JS-sel töltődik, így csak a címek ellenőrizhetők. Ezek: Jane Street 2021 (Yirun, supervised AE+MLP), Optiver RV („Nearest Neighbors”), Optiver Close, M5, Web Traffic, Rossmann, Ubiquant. A módszerrészletek „nem ellenőrzött” címkét kaptak. A Jane Street 2024–25 és a Two Sigma (2016–17, 2018–19) győztesei nem ellenőrzöttek.
- **Teljesítményszámok.** A Renaissance, PNP, Benter, Walters, Starlizard és Numerai számai sajtó- vagy Wikipedia-forrásból jönnek, auditált adat nincs (becsült / nem ellenőrzött).
- **Le nem töltött források.**
  - Az Avellaneda–Lee Sharpe-számai és a Froot és társai számszerű eredményei: az absztrakt nem volt elérhető.
  - A Cash WinFall főfelügyelői jelentése: 403.
  - A Ken French Data Library: időtúllépés.
  - Az RS Metrics oldala: 403.
- **Csomagok.** A GitHub API helyett ungh.cc-t használtunk. Elavult vagy lassan karbantartott csomagok: hmmlearn (2024 óta nincs kiadás), fracdiff, hurst, PyInform, bayesian-changepoint-detection és benford-py. Az mlfinlab nincs a PyPI-n (fizetős), a pypbo és az IDTxl csak GitHubon érhető el. A tigramite GPL-3.0 licencű, ez kereskedelmi beágyazásnál számít.
- **Mérési hiány.** FX- vagy kripto-specifikus publikálás utáni lecsengést nem mértek McLean–Pontiff-szerűen. A tételekben ez következtetett állítás.
