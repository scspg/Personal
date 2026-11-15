# ARCHIVUM – Jövő kiadás: koncepció, pontozás, fejlesztési terv

Állapot: tervezet. Felhasználói kérés (2026-11-14):
- A legnagyobb fókusz az AI-on, a technológiákon, az energián és a földön kívüli dolgokon legyen (spirituális, űr, világegyetem).
- Ne a múltra, hanem a jövőre koncentráljon.
- A múltból azt vigye magával, ami fontos lehet: nagy emberek szavai és tettei, a történelem legjava, a lényeges részletek.
- „Te buszold fel, állítsd össze, pontozd, fejleszd, és ez alapján csináld.”

Ütemezés: előbb lezárom a blackout-kiadást (≥ 90 / átlag ≥ 95, végső átnézés, ZIP). Utána következik ez.

## 1. Alapelv

**Jövő-mag + civilizációs biztosítás + az emberiség öröksége.** Három réteg, a tárhely ebben az arányban oszlik meg:
- **60%: jövő-mag.** AI, számítástechnika, energia, jövőtechnológiák, űr és világegyetem.
- **25%: biztosítás.** A blackout-kiadás életmentő magja (tier 0–1) mindig bekerül, mert a jövő is erre épül.
- **15%: örökség.** Ami a múltból számít: gondolatok, tettek, tanulságok, források. Kurált, kis méretű, nagy sűrűségű anyag.

## 2. Pillérek, pontozva

Pontozási szempontok, mindegyik 0–10:
- **F:** jövőérték – mennyire segít a következő évtizedek technológiáiban.
- **M:** tudásmélység.
- **P:** pótolhatatlanság – ha eltűnik a net, máshonnan nem szerezhető meg.
- **O:** offline használhatóság.
- **H:** méret-hatékonyság – érték per GB.
- **E:** a meglévő katalógus lefedettsége (alacsony = sok a teendő).

| # | Pillér | F | M | P | O | H | E | Prioritás | Mit kell hozzátenni (jelölt források, a kutatáskor ellenőrizendő) |
|---|---|---|---|---|---|---|---|---|---|
| 1 | **AI és gépi tanulás** | 10 | 9 | 8 | 9 | 7 | 6 | **1.** | Tanítás és finomhangolás: PyTorch-csomagok, CUDA/ROCm-telepítők, Unsloth, Axolotl, TRL, vLLM, llama.cpp. Tankönyvek és kurzusok: d2l.ai, Understanding Deep Learning (Prince, ingyenes PDF), Karpathy „Zero to Hero” és nanoGPT/nanochat, fast.ai, Stanford CS229/CS231n/CS336-jegyzetek, MIT 6.S191. Cikkek: arXiv cs.LG/cs.AI/cs.CL válogatás, mérföldkő-cikkek listával. AI-biztonság és alignment: Anthropic-, DeepMind- és OpenAI-kutatások, Alignment Forum archívum. Adathalmazok: FineWeb-Edu, The Stack v2 (meta), értékelő benchmarkok. Ágens-keretek. |
| 2 | **Energia** | 10 | 8 | 7 | 8 | 8 | 5 | **2.** | Napelem és akkumulátor (NREL-adatok és -tankönyvek, pvlib, SAM). Atomenergia: IAEA-kiadványok, tankönyvek, nyílt reaktortervek. Fúzió: ITER-dokumentáció, tankönyvek. Hidrogén, hálózat, hőszivattyú. Saját gyártású turbina, Stirling-motor. |
| 3 | **Jövőtechnológiák** | 10 | 8 | 7 | 7 | 6 | 3 | **3.** | Robotika: ROS 2 + dokumentáció, nyílt robottervek. Félvezetőgyártás: SkyWater/GF nyílt PDK, OpenROAD, OpenLane, Magic. Kvantumszámítás: Qiskit, tankönyvek. Anyagtudomány: Materials Project-adatok. Szintetikus biológia: iGEM-alkatrészregiszter, OpenWetWare. Nanotechnológia, 3D bioprint. Hosszú élet és orvosi kutatás. |
| 4 | **Űr és világegyetem** | 9 | 8 | 6 | 8 | 7 | 4 | **4.** | NASA NTRS (megvan), ESA, NASA Exoplanet Archive (CSV). Gaia-katalógus kivonat. Stellarium, Celestia, KStars. Pályamechanika: GMAT, Orekit, poliastro. Rakéta: OpenRocket, RPA, NASA CEA. Csillagászati tankönyvek (OpenStax Astronomy). Astronomy Stack Exchange ZIM. Asztrobiológia, SETI-irodalom. |
| 5 | **Földön kívüli jelenségek (UAP)** | 5 | 5 | 7 | 9 | 9 | 1 | **7.** | Feloldott titkosítású források: NARA UAP-gyűjtemény, Project Blue Book (archive.org), AARO-jelentések, kongresszusi meghallgatások jegyzőkönyvei. Ismeretelméleti címke kötelező: forrás ≠ bizonyíték. |
| 6 | **Spiritualitás, filozófia, tudat** | 7 | 8 | 6 | 9 | 10 | 3 | **5.** | Világvallások szent szövegei (sacred-texts archívum, Wikiforrás). Klasszikus filozófia (Gutenberg, Perseus). Stanford Encyclopedia of Philosophy (offline változat ellenőrizendő). Buddhista források (Access to Insight, SuttaCentral offline). Tudatkutatás, meditációs útmutatók. Etika és AI-etika. |
| 7 | **Az emberiség öröksége: nagy emberek, szavak, tettek** | 6 | 8 | 7 | 10 | 10 | 4 | **6.** | Wikiquote ZIM (en + hu), Nobel-előadások (nobelprize.org), nagy beszédek közkincs-forrásokból. Életrajzok (Wikipédia-válogatás). Történelmi elsődleges források: Avalon Project, Fordham Internet History Sourcebooks. „Great Books”-lista a Gutenbergről. Magyar nagyok: MEK, Arcanum-kivonatok. Tudománytörténet: hogyan jutottunk ide. |
| 8 | **Jövőkutatás és globális adatok** | 8 | 7 | 6 | 9 | 9 | 2 | **8.** | Our World in Data (CC BY, GitHub-adatok). Világbank, ENSZ-adatok. Egzisztenciális kockázatok irodalma (ingyenes részek). Forgatókönyv-tervezés módszertana. |
| 9 | **Tudományos alapok** | 8 | 9 | 5 | 9 | 8 | 8 | **9.** | Nagyrészt megvan: OpenStax, LibreTexts, arXiv, Khan Academy. Ellenőrizni kell a fizika és a matematika mélységét. |

A prioritás a súlyozott összegből jön: 0,35·F + 0,2·M + 0,15·P + 0,1·O + 0,1·H + 0,1·(10−E).

## 3. Megvalósítás

1. **Új pontozási dimenzió, F (jövőérték)** minden tételre: kategória-alapértékkel, és az új tételeknél egyedi értékkel. Új profil a `select_items.py`-ban: `future`, súlyok F 0,40 · R 0,15 · U 0,15 · Q 0,10 · A 0,10 · O 0,05 · S 0,05.
   - Az életmentő tier 0 mag kötelező (`--include`).
   - Az örökségréteg kvótája 15%.
2. **Kutatóágensek**, pillérenként egy, ellenőrzött linkekkel és mért méretekkel, a mostani minőségi szabályokkal:
   - AI;
   - energia + jövőtechnológiák;
   - űr + UAP;
   - spiritualitás + örökség + jövőkutatás.
3. **Új fejezetek:**
   - „Jövő-mag” (pillérenként a legjobb források);
   - „Az emberiség öröksége” (kurált lista);
   - a HTML-ben „Jövő” nézet és profilválasztó.
4. **SSD-csomagok** a `future` profillal, 1–128 TB-ig, a blackout-csomagok mellett.
5. **Minőségi kapu:** ugyanaz, mint a blackoutnál – minden terület ≥ 90 pont, átlag ≥ 95 –, végül több szemszögű átnézés: AI-kutató, mérnök, csillagász, filozófus/teológus és történész szemmel.

## 4. Következő szintek – ahol a mai AI és technológia megáll, onnan tovább

Felhasználói kérés (2026-11-14): „menj el a következő szintre: ahol megáll az AI és a technológia, ott vidd tovább a következő szintekre”.

**Elv:** nem csak a meglévő tudást archiváljuk, hanem a **továbbfejlesztés képességét** is. Ez három dolgot jelent:
- a határterületek térképe (mi a következő lépcső, és mi akadályozza);
- a kutatás eszközei offline (szimulátorok, modellek, adatok);
- a módszertan (hogyan kutass, kísérletezz, validálj).

### 4.1 Technológiai szintlétra (minden pillérnél ezt a 6 fokot töltjük ki)

| Szint | Mit jelent | Ismeretelméleti címke | Mit archiválunk hozzá |
|---|---|---|---|
| **L0 – ma működő** | termékben, nyílt forrásként elérhető | mért | szoftver, modell, kézikönyv (a mostani katalógus) |
| **L1 – frontier** | 2025–2026 legjobb kutatási eredményei | mért, publikált | mérföldkő-cikkek, kódok, súlyok, benchmarkok |
| **L2 – laborban igazolt, még nem skálázott** | prototípus létezik | publikált, nem reprodukált | cikkek + nyílt replikációk + a szűk keresztmetszetek listája |
| **L3 – fizikailag megengedett, mérnöki áttörést igényel** | elmélet kész, a megvalósítás nincs meg | elméleti | tankönyvi levezetések, számítások, ütemterv-dokumentumok |
| **L4 – spekulatív határ** | alapkutatási kérdés, nyitott elmélet | spekulatív | áttekintő cikkek, ellenérvek, nyitott problémák listája |
| **L5 – filozófiai horizont** | értelem, tudat, értelem a kozmoszban | filozófiai | a legjobb gondolkodók érvei pró és kontra |

### 4.2 Pillérenként a következő lépcsők (mit kell a kutatásnak összegyűjtenie)

| Pillér | L1 frontier (ma) | L2–L3 következő lépcső | L4–L5 horizont | Továbbfejlesztés eszközei offline (jelöltek, ellenőrizendők) |
|---|---|---|---|---|
| **AI** | frontier LLM-ek, érvelő modellek, ágensek, multimodális modellek | önfejlesztő/kutató AI-ágensek, folyamatos tanulás, világmodellek, neuroszimbolikus érvelés, energiahatékony (neuromorf) hardver | AGI/ASI, alignment-elmélet, gépi tudat kérdése | nanoGPT/nanochat, teljes tanítási lánc (adat → tokenizáló → előtanítás → RL), mechanisztikus értelmezhetőség (TransformerLens, SAE-k), AI-biztonsági irodalom |
| **Számítás** | GPU-klaszterek, 2–3 nm-es chipek | fotonikus és analóg számítás, 3D-chipek, kvantum-hibajavítás | reverzibilis számítás, a számítás fizikai határai (Landauer, Bremermann) | nyílt PDK + OpenROAD (saját chip), Qiskit/Stim (kvantum), Verilog-szimulátorok |
| **Energia** | perovszkit-napelem, nátriumion-akku, SMR atomreaktor | fúziós pilot erőművek, űrbeli napenergia, szilárdtest-akku | Kardasev-skála, Dyson-típusú gyűjtés, antianyag | OpenMC (neutronika), pvlib, SAM, plazmakódok (pl. Gkeyll), hálózat-szimuláció (PyPSA) |
| **Anyag, nano, kémia** | AI-alapú anyagfelfedezés (GNoME-típus) | atomprecíz gyártás, programozható anyagok | molekuláris nanotechnológia (Drexler) | Quantum ESPRESSO, CP2K, LAMMPS, GROMACS, OpenMM, RDKit, Materials Project-adatok |
| **Biológia, élet** | fehérjeszerkezet-előrejelzés, génszerkesztés | sejtprogramozás, mesterséges sejt, regeneráció, öregedéskutatás | hosszú élet, „longevity escape velocity”, agyi emuláció | Boltz/OpenFold-típusú nyílt szerkezet-előrejelzők, BLAST, Biopython, nyílt genomadatok |
| **Agy és ember–gép kapcsolat** | nem invazív és invazív BCI-k | nagy sávszélességű BCI, konnektomika | teljes agyi emuláció, tudatfeltöltés vitája | MNE-Python, OpenBCI, konnektóm-adatok (pl. légy-konnektóm) |
| **Űr** | újrafelhasználható rakéták, Hold-program | Mars-bázis, űrbeli bányászat, nukleáris meghajtás | csillagközi szondák (Breakthrough Starshot), generációs hajók | GMAT, Orekit, poliastro, REBOUND, OpenRocket, NASA CEA |
| **Kozmosz és fizika** | gravitációs hullámok, JWST, exobolygó-légkörök | technoszignatúra-keresés, kvantumgravitációs kísérletek | sötét anyag/energia, multiverzum, a fizika nyitott kérdései | csillagászati adatok (Gaia, exobolygók), Astropy, kozmológiai szimulációs kódok |
| **Értelem a világegyetemben** | SETI-programok, UAP-adatgyűjtés | technoszignatúra-statisztika | Fermi-paradoxon, Drake-egyenlet, „nagy szűrő” | SETI-irodalom, feloldott titkosítású dokumentumok (címkézve) |
| **Társadalom és gazdaság** | AI és munka, automatizálás | bőség utáni gazdaság, decentralizált intézmények | civilizáció-tervezés, hosszú távú gondolkodás | Our World in Data, jövőkutatási módszertan, egzisztenciális kockázatok irodalma |
| **Tudat és spiritualitás** | tudatkutatási elméletek (IIT, GWT), meditációs kutatás | tudatmérés, gépi tudat tesztjei | a lét, az értelem és a kozmikus cél kérdései | filozófiai és szent szövegek, áttekintő irodalom |

### 4.3 „Kutatómotor” – a továbblépés képessége internet nélkül (új, kiemelt csomag)

| Elem | Tartalom | Pontszám (F/M/P/O/H) | Prioritás |
|---|---|---|---|
| **Szimulációs verem** | fizika és mérnöki szimuláció (OpenFOAM CFD, FEniCS/Elmer FEM, LAMMPS/GROMACS, Quantum ESPRESSO, OpenMC, áramkör-szimulátorok), Jupyter, NumPy/SciPy/SymPy, Julia | 10/9/8/9/8 | 1. |
| **Saját AI fejlesztése** | teljes tanítási lánc + adathalmazok + a helyi LLM mint kutatási asszisztens (RAG a teljes archívumon) | 10/9/8/9/7 | 1. |
| **Kísérleti módszertan** | tudományos módszer, statisztika, kísérlettervezés, laborbiztonság, mérőeszköz-építés | 9/8/7/10/10 | 2. |
| **Határterület-térképek** | nyitott problémák listái (matematika, fizika, AI, biológia), ütemtervek, „mi hiányzik a következő lépéshez” | 10/8/8/10/10 | 2. |
| **Gyártási lánc a kutatáshoz** | 3D-nyomtatás → CNC → elektronika → saját chip (nyílt PDK); laboreszközök nyílt tervei | 9/8/8/9/8 | 3. |

**Megvalósítás:** a 3. pontban leírt kutatóágensek kiegészülnek egy „Kutatómotor + szintlétra” ágenssel. Az új tételek kapnak egy `level` mezőt (L0–L5), a jövő-fejezet pedig szintlétra-mátrixként jelenik meg (pillér × szint), kattintható tételekkel a HTML-ben.
