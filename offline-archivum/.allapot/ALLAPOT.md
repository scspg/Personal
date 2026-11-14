# ARCHIVUM – munkaállapot (kompaktálás elleni mentés)

Frissítve: 2026-11-14, commit után. Ág: `claude/wonderful-cerf-ysp3od`, draft PR: https://github.com/scspg/Personal/pull/1.
A kompaktálás után ELŐSZÖR ezt a fájlt kell elolvasni.

## A felhasználó kötelező feltételei (szó szerint értelmezve)

- **Nyelv és stílus:** magyarul, tömören, principal szinten. A bizonytalanság címkézve: mért / becsült / nem ellenőrzött. Nincs kitalált link vagy szám.
- **Pontszámok:** minden terület ≥ 90 pont, az átlag ≥ 95.
  - Ezután egy VÉGSŐ, mindenre kiterjedő átnézés kell más szemszögekből: AI-ágens próbafuttatás, kezdő felhasználó, túlélési / orvosi / mezőgazdasági szakértő, adatmegőrzési szakember.
  - Ha ez után is minden ≥ 90 és az átlag ≥ 95, CSAK AKKOR jöhet a lezárás és a ZIP elküldése (SendUserFile).
- **ZIP:** az új ZIP-ben minden benne legyen, ami a korábbiban (49 fájl), és ne legyen kisebb. Ellenőrzés: `git show <régi>:offline-archivum/ARCHIVUM.zip`.
- **Sorrend:** ELŐBB a blackout/apokalipszis-változat legyen kész. UTÁNA jönnek a többi hozzáállás profiljai (lásd lent).
- **Tárolók:** több TB-os változat, több konkrét meghajtóra szétosztva. Szempontok:
  - a legbiztonságosabb (víz- és ütésálló, ha van) és a leggyorsabb, legprofibb;
  - több árszint, konkrét linkekkel a legolcsóbb megbízható boltokból;
  - „ha lehet, egyben, a legkompaktabban”, de az indokolt kompromisszum elfogadható (pl. 1 fő + 1 offline másolat).
- **Kontextuskezelés:** kb. 60%-os kontextusnál mentés ebbe a fájlba, és commit.

## Kész

- A katalógus 1248 tételből áll:
  - LLM: 609 kvant;
  - oss-*: 190 (items_oss_a/b/c);
  - hub-*: 70.
- **5b fejezet:** a legjobb nyílt forráskódú szoftver és modell.
- **HTML:** „Szoftverek és modellek” fül.
- **SSD-tervek:** 1–128 TB, monoton (`--include` az előző méret nem-LLM, csoport nélküli tételeire). 64 TB felett T1, 2000 GB és 8 LLM.
  - A „minden egyben” méret ≈ 22,5 TB.
- **Átnézések (3. kör)** – a pontszámok a javítás ELŐTTI állapotra vonatkoznak; minden hiba javítva:
  - UX 70–90;
  - adatok 60–92;
  - szkriptek 62–93.
- **Javítások:**
  - git: sekély klón, `refs/pull` nélkül;
  - hf: mintánként külön hívás;
  - kiwix: `.ok` + `REFRESH`;
  - `ollama_pull` a meghajtóra;
  - CLI-validálás;
  - impersonal szöveg;
  - kompakt TOC;
  - chat-szerkezet;
  - HTML: mobilkártyák, sticky, fókusz, Fogalmak, magyar rendezés;
  - reprodukálható ZIP.
- **Ellenőrző szkriptek** (scratchpad, elveszhetnek):
  - `check.js`: HTML + JS-kimenet;
  - `parity.py`: 22/22;
  - `val.py`: séma (src-ből futtatva);
  - `soft2.js`.

## Folyamatban / következő lépések

0. TÁROLÓ-FEJEZET KÉSZ: 4c (src/gen_storage.py, adat: src/research/storage.json ← storage_hdd.yaml + storage_ssd.yaml, 71 termék); HTML SSD-fülön rétegtábla + szűrhető terméktábla. Kulcs: teljes archívum 22,5 TB → 2× 24–32 TB HDD (más gyártó, egyik offline Faraday+lőszerláda) + mag strapabíró SSD + M-DISC. Ellenőrzések: séma OK, paritás 22/22, mobil 400, horgonyok 0 hiba (rv3/slug.py).
   KÖVETKEZŐ: 4. újrapontozó kör (3 független átnéző) → javítás → végső több szemszögű átnézés → ZIP.

1. **Két tároló-kutató ágens fut** (HDD/archív, illetve SSD).
   - Kimenet: `scratchpad/storage_hdd.yaml`, `storage_ssd.yaml`.
   - Továbbítva nekik: „egy eszköz vs 1+1 másolat” számszerűen, a legsűrűbb egyeszközös megoldás 8–128 TB-ra, és a legkompaktabb kételemes, víz-, ütés- és EMP-álló összeállítás.
   → Ezekből új fejezet: **4c. Tárolók és szétosztás**. Tartalma:
   - terméktáblák árszintenként, linkekkel;
   - meghajtónkénti szétosztás méretenként (mi hova: tier 0–2 robusztus SSD-re + M-DISC, LLM a gép NVMe-jére, nagy tükrök HDD-re);
   - 3-2-1 és adatintegritás (ZFS/Btrfs scrub, par2, SMART, évenkénti bekapcsolás).
   → A HTML SSD-fülébe is.
2. Újrapontozás 3 független átnézővel → javítás, amíg minden ≥ 90 és az átlag ≥ 95.
3. Végső, több szemszögű átnézés (lásd fent) → javítás.
4. Build-sorrend:
   1. `gen_sections`
   2. `build`
   3. `gen_sections`
   4. `build`
   5. `gen_html`
   6. `make_zip` (UTOLSÓ lépés)
   - Utána commit és push.
   - A ZIP-et SendUserFile-lal küldöm, és pontszámtáblával válaszolok.
5. **UTÁNA – JÖVŐ KIADÁS (fő fókusz, lásd JOVO_KONCEPCIO.md: AI, technológia, energia, űr/világegyetem, spirituális, földön kívüli + az emberiség öröksége), majd a többi hozzáállás profiljai** (a felhasználó kérése; a blackout-változat után):
   - kutatás/tudomány;
   - AI-fejlesztés;
   - szoftverfejlesztés/építés;
   - gyártás/mérnöki;
   - orvosi;
   - önellátás/mezőgazdaság;
   - energia;
   - kommunikáció/rádió;
   - oktatás/család;
   - magyar örökség;
   - homelab/digitális önállóság;
   - közösségszervezés/jog/üzlet.

   A megvalósítás menete:
   - új `PROFILES` súlyok és kategória-fókusz a `select_items.py`-ban;
   - profilonként hiányelemzés + kutatóágens a lefedettségre (pl. AI-fejlesztés: CUDA/ROCm toolkit, PyTorch-wheelek, tanítókeretek, adathalmazok; kutatás: arXiv/PMC/OpenAlex, Zotero, Jupyter);
   - profilonként SSD-csomagok;
   - HTML-ben profilválasztó.

## Fájltérkép

- Kimenetek: `offline-archivum/`
  - `ARCHIVUM.md`
  - `ARCHIVUM-kompakt.md`
  - `ARCHIVUM-chat.md`
  - `ARCHIVUM-LLM.html`
  - `README.md`
  - `ARCHIVUM.zip`
- Forrás: `offline-archivum/src/`
  - `build.py`
  - `gen_sections.py`
  - `gen_html.py`
  - `select_items.py`
  - `llm_calc.py`
  - `fixes.py` (minden adatjavítás itt van)
  - `items_*.jsonl`
  - `sections/*.md`
  - `research/`

## 4. kör – UX-átnéző: 1–25 JAVÍTVA (commit 4a328e7), kivéve #2 ZIP (a végén)
1 22 TB-os lemez nem fér 22,5 TB-ot → A példány ≥24 TB; 2 ZIP elavult → make_zip utoljára; 3 nyers JSON-kulcsok (22_TB_valtozat, kozep...) → LABEL dict gen_storage; 4 None a sebességben → speed() javít; 5 mobil: #ssd td.num rejti az árat, .stortab max-content → scope + mobil width100%; 6 HTML-ből hiányzik árszint/kételemes/egyeszközös/kockázat → kártyák; 7 desktop tábla 2479px → linkek a név alá, oszlopok szűkítése; 8 aria-current="location"; 9 Fogalmak saját section; 10 "0,0 GB" → MB formázó; 11 4b intro 64/128 TB T1 szöveg (MD+HTML); 12 4. vs 4b eltérés magyarázó mondat; 13 71 vs 70 termék, SanDisk-megjegyzés callout; 14 IronWolf Pro 32 „mért”→becsült; 15 ioSafe 362 USD = 4 TB; 16 összeállítás-tábla: kapacitás, extrém ár, Mit bír ki / Megjegyzés külön; 17 felsorolások sub-bullet; 18 mag: Samsung T7 Shield 4TB alap, LaCie/ADATA olcsóbb; 19 SSD 1,6% magyarázat; 20 tizedesvessző (6.4/6.5, chat, 4c); 21 tüzet, lőszerláda, „”, gondolatjel, lágy kötőjel; 22 ékezetfüggetlen keresés; 23 tároló rendezés; 24 README 4c + nav „SSD és tárolók”; 25 prompt 9a második példány lépés + Fogalmak tárolófogalmak.
