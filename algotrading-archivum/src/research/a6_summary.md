# A6 – AI döntési réteg, benchmark-platformok, tudásbázis (M9, M12, M13) – összefoglaló

Ellenőrzés: 2026-11-15. Kimenet: `a6_ai_research.jsonl`, 270 tétel (M9: 119, M12: 36, M13: 115). Címkék: 251 mért, 13 becsült, 6 nem ellenőrzött.
148 tétel cikk vagy hivatkozás (arXiv/DOI/SSRN). Mindegyiket arXiv API vagy Crossref ellenőrizte; a könyvek ISBN-jét az Open Library.
A GitHub-csillagok és a push-dátumok forrása az ungh.cc API (a GitHub API a sandboxból tiltott), a licenceké a shields.io. A `last_commit` mező a `pushedAt` értéke.
Árfolyam: 1 EUR = 1,1052 USD (EKB, 2026-11-13).

## 1. Ténylap – Medallion / Aladdin / Bloomberg

| Állítás | Forrás | Címke |
|---|---|---|
| A Medallion 1988-ban indult; 1993-tól kivezették a külső befektetőket; 2009-03-31-én az eszközök >99%-a cég- és munkavállalói tőke | US Senate PSI jelentés (2014), PDF átnézve | mért |
| RenTec bázisopciók, 2000–2013: kb. 34,2 Mrd USD nettó profit, kb. 6,83 Mrd USD becsült adókülönbség | PSI jelentés, táblázat | mért (a forrás maga becsül) |
| Áttétel akár 20:1 (a Reg T szerinti 2:1 helyett); napi 100–150 ezer kereskedés bankonként, évi 26–39 millió | PSI jelentés | mért |
| A pozíciók 87%-a 3 hónapnál rövidebb, kevesebb mint 1%-a 6 hónapnál hosszabb ideig nyitott (SEC-elemzés, 2007–2009) | PSI jelentés | mért |
| 1988–2018: átlagosan 66,1% bruttó és 39,2% nettó éves hozam, bruttó CAGR 63,3% | Cornell (SSRN 3504766), a Zuckerman-könyv adataira építve | becsült (nem auditált, keresési kivonatból) |
| Díjak: 5% kezelési és 44% sikerdíj | harmadik fél | nem ellenőrzött |
| A vezetők kb. 7 Mrd USD adót és bírságot fizetnek (2021); Simons ezen felül kb. 670 M USD-t | CNBC/WSJ sajtó | becsült (nincs hivatalos IRS-közlemény) |
| A 13F-beadványok nem a Medallion stratégiáját mutatják | EDGAR CIK 0001037389 + PSI (rövid tartás) | következtetett |
| Legenda (nem bizonyított): „HMM/beszédfelismerés-alapú mesteralgoritmus”, „soha egy veszteséges év” | Zuckerman, sajtó | nem ellenőrzött |
| Aladdin: portfólió-, kereskedési (OMS/EMS), compliance-, kockázati és működési platform; magánpiacok az eFront-tal (felvásárolva 2019-ben) | blackrock.com/aladdin | mért (marketinganyag) |
| Technology services bevétel kb. 2,0 Mrd USD (+24%) 2025-ben, ennek többsége Aladdin; az ACV organikusan +16% | BlackRock 10-K FY2025 (keresési kivonat; az SEC-oldal 403-at adott) | becsült |
| Kockázati modell: többfaktoros, statisztikai; kb. 2 200+ faktor; 10 év faktorhozam a volatilitáshoz; részben zárt | BlackRock Scenario Tester módszertan | mért |
| Aladdin VaR/Monte Carlo módszertana nyilvánosan nem dokumentált | – | mért (hiány) |
| Bloomberg Terminal: nincs publikus árlista; kb. 31 980 USD/év/terminál (kb. 2 411 EUR/hó), 2 éves szerződés, 2 évente 6–10% emelés | Koyfin blog, árgyűjtők | becsült |
| B-PIPE: kb. 35 M instrumentum, 330–350+ tőzsde, on-prem/AWS/Azure; egyedi ár | Bloomberg/AWS anyagok | becsült |
| BQL: a Bloomberg felhőjében fut; Terminal, Excel (BQL.Query), BQuant (Python) | egyetemi útmutatók | becsült |
| Funkciókódok (GP, FA, ECO, WIRP, OMON, PORT) | általános ismeret; a Bloomberg-oldal 403-at adott | nem ellenőrzött |
| Alternatívák havidíja (mérve): Koyfin 39/79/209/299 USD; TradingView éves fizetéssel 12,95–199,95 USD; Quantpedia Premium 599 USD/12 hó | gyártói oldalak | mért |
| LSEG Workspace kb. 12–24 ezer USD/év; FactSet kb. 12–40 ezer; YCharts kb. 3,6–6 ezer | harmadik fél | becsült |

## 2. Javasolt döntési architektúra: súlyozott ensemble és ördögügyvéd

**2.1 Szavazók.** Minden szavazó ugyanazt adja: kalibrált valószínűség p_i (h horizonton), várható hozam és bizonytalanság.
- **Statisztikai szavazók:** HAR-RV (Corsi 2009), idősoros momentum (Moskowitz–Ooi–Pedersen 2012), FX carry (Koijen et al. 2018; Lustig et al. 2011).
- **ML-szavazók:** GBM vagy NN meta-labelinggel (López de Prado: AFML; Joubert 2022).
- **LLM-ágensek:** hír-, makró- és narratíva-ágens (Lopez-Lira–Tang 2023; TradingAgents Bull/Bear vita, arXiv 2412.20138).

**2.2 Kalibráció (kapu).** Minden szavazó kap egy izotonikus vagy Platt-kalibrátort purged/embargoed CV-n (Zadrozny–Elkan 2002; Niculescu-Mizil–Caruana 2005; sklearn CalibratedClassifierCV időrendi splittel).
Folyamatosan figyeljük a gördülő Brier-pontszámot és a log-loss-t (Brier 1950; Gneiting–Raftery 2007).

**2.3 Felvételi kapu.** Új szavazó csak akkor kerül be, ha:
- DSR > 0,95 (Bailey–López de Prado);
- PBO < 0,2 CSCV-vel (Bailey–Borwein–LdP–Zhu);
- új faktornál t > 3 (Harvey–Liu–Zhu 2016);
- túléli a SPA- vagy StepM-tesztet (Hansen 2005; Romano–Wolf 2005);
- és bekerül a Model Confidence Setbe (Hansen–Lunde–Nason 2011).

Eszköz: `arch` (SPA/StepM/MCS), `pypbo`. A küszöbök javaslatok (becsült).

**2.4 Súlyozás, két szinten.**
- (a) **Offline:** nemnegatív stacking out-of-fold predikciókon (Wolpert 1992; Breiman 1996; Yao–Vehtari et al. 2018). A súlyokat az egyenlő súly felé zsugorítjuk, mert a becsült optimális súlyok gyakran rosszabbak az egyenlő súlynál (Timmermann 2006, „forecast combination puzzle”). A BMA-t csak kontrollnak használjuk, mert M-open helyzetben túlkoncentrál (Hoeting et al. 1999).
- (b) **Online:** Hedge/multiplicatív súlyfrissítés log-loss-szal, fixed-share keveréssel a rezsimváltás miatt (Freund–Schapire 1997; Littlestone–Warmuth 1994; Arora–Hazan–Kale 2012).
  - Ha egy stratégiának csak az élőben futtatott eredménye látszik: Exp3 (Auer et al. 2002).
  - A stratégiák közti tőkeallokáció diszkontált Thompson-mintavétellel (Russo et al. 2017).
  - Portfólió szinten: EG/OLPS benchmark (Helmbold et al. 1998; Li–Hoi 2014).

**2.5 Bizonytalanság → pozícióméret.**
- U1 = a súlyozott p_i-k szórása (egyet nem értés; Lakshminarayanan et al. 2016).
- U2 = az LLM-szavazók szemantikus entrópiája (Kuhn et al. 2023; Farquhar et al., Nature 2024).
- U3 = a konformális sáv szélessége ACI/AgACI-val (Gibbs–Candès 2021; Zaffran et al. 2022; MAPIE).
- Méret = frakcionális Kelly (Kelly 1956; Thorp 2006) × meta-labeling konfidencia (Meyer–Barziy–Joubert 2023) × g(U1, U2, U3) × (1 − DA-büntetés).
- Az egyet nem értés külön jelként is tesztelendő: Kirtac (arXiv 2603.20965, mért) és Cheng–Hu (2026, nem ellenőrzött).

**2.6 Ördögügyvéd-ágens (DA).** Külön modell vagy prompt, hozzáférés nélkül a javaslattevő érveléséhez.
- **Lépései:**
  - pre-mortem: „miért bukik el ez a kötés?”;
  - előrelátó reflexió (Wang et al. 2024, „Devil's Advocate”, arXiv 2405.16334);
  - kijelölt ellenvélemény vitában, bíróval (Liang et al. 2023 MAD; Du et al. 2023);
  - a bíró a javaslattevő és a DA vitáját értékeli (Khan et al. 2024; Irving et al. 2018).
- **Kimenet:** strukturált kockázatlista + p_fail.
- **Blokkolni csak kemény feltételnél szabad:**
  - a kalibrált p és a konformális sáv nem zárja ki a nulla várható értéket;
  - a gördülő Brier átlépte a küszöböt (kalibrációs drift);
  - kockázati limit sérül (napi veszteség, kitettség, margin/stop-out távolság 1:500 mellett);
  - adat-/időzítési hiba (elavult hír, look-ahead, injekciógyanús hírszöveg).
- **Egyébként a DA csak méretet csökkent.** A DA vétójogát a saját mért pontossága (Brier-pontszáma) súlyozza, így a túl óvatos DA súlya automatikusan csökken.
- **Minden DA-érv auditnaplóba kerül.** Ugyanez vonatkozik a felhasználó javaslataira is.

**2.7 Benchmark az LLM-rétegre.** Csak szennyezésmentes (a tudáshatár utáni) tesztet fogadunk el: StockBench (a legtöbb ágens nem veri a buy-and-hold-ot), LiveTradeBench (élő, Polymarketet is tartalmaz), InvestorBench, FinBen.
- A FinanceBench szerint az LLM + RAG a kérdések 81%-át hibásan válaszolta meg vagy elutasította (2023): numerikus adatnál kötelező az eszközhasználat.
- Minden publikált jelnél lecsengéssel számolunk: out-of-sample −26%, a publikáció után −58% (McLean–Pontiff 2016, mért).

## 3. „Javhez” – értelmezések

1. **Jev (TypeSafe AI, 2026-09).** Nem szöveget generáló döntési modell: kalibrált opció-valószínűségeket ad, 70–500 ms alatt, RLCD-tanítással. Nyelvtanilag illik („Jev-hez”), és tartalmilag is („statisztikai” AI). **Legvalószínűbb** (becsült). Szerepe: gyors kapuőr-szavazó lehet.
2. **Jane Street** (a spec sejtése): ML-alapú árjegyző; két nyilvános Kaggle-verseny valós, anonimizált adattal.
3. **JAX** (Google): numerikus ML-könyvtár; a Bayesi/online súlyozó réteg implementációs alapja lehet.
4. **Jarvis** (Microsoft JARVIS/HuggingGPT): orchestrátor-minta.
5. **Java** (Weka, DL4J): gyenge illeszkedés.
6. **Simons/RenTech**: tartalmi, nem nyelvi egyezés.

**Teendő:** a megrendelővel megerősíteni.

## 4. Top 10 tétel
1. TradingAgents (122 566 ★, 2026-11-04, Apache-2.0): Bull/Bear vita, a DA-réteg mintája.
2. DSR + PBO + PSR (Bailey–López de Prado) validációs kapu.
3. Harvey–Liu–Zhu (2016): a t>3 küszöb.
4. McLean–Pontiff (2016): a lecsengés kvantifikálva.
5. López de Prado: AFML (ISBN 9781119482086): meta-labeling, CPCV.
6. A US Senate PSI jelentése (2014): az egyetlen elsődleges, hiteles Medallion-forrás.
7. Microsoft RD-Agent (15 375 ★): automatizált faktor-/hipotézisgyár.
8. Gibbs–Candès ACI + MAPIE: bizonytalansági sáv idősorra.
9. Liang et al. MAD + Wang et al. Devil's Advocate: az ördögügyvéd módszertana.
10. OpenBB (75 412 ★): nyílt Bloomberg-alternatíva adatrétegnek és MCP-nek AI-ágensekhez.

## 5. Hiányok
- A Bloomberg, Citadel, SSRN, SEC, Alpha Architect, QuantNet és Wilmott oldalai botvédelem (403) miatt nem voltak letölthetők.
- Hivatalos Bloomberg-, LSEG-, FactSet- és YCharts-ár nem létezik: csak becslés van.
- A FinAgent és a FinCon hivatalos kódja nincs azonosítva.
- A Medallion hozamtáblája csak másodlagos forrásból (Zuckerman, Cornell) érhető el.
- Az Aladdin VaR-módszertana nem nyilvános.
- A könyvárakat nem mértem.
