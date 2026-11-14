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
