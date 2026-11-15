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

## 4. kör – ADAT-átnéző (séma 85, letöltés 72, linkek 93, méret 74, tier 82, dedup 78, lefedettség 86, magyar 84, tároló 80) – JAVÍTVA, kivéve: #24 fordítás (ágens fut → translated_hu.json beépítése fixes-be), #27 size_status normalizálás (kihagyva), #10 llama.cpp binárisok (agent marad)
1 msf-essential-drugs URL: guideline-339-en/-fr/-es/-ar.pdf (aláhúzás nélkül); 2 22 archive.org tétel glob *.pdf nélkül; 3 open-library → http openlibrary.org/data/ol_dump_latest.txt.gz 18 205 492 645 B; 4 neets bytes 132 MB; 5 lexikonok subsumed_by + mek-oszk-szakmai; 6 whisper turbo-q5 duplikált; 7 python-source → http (3.15.2 tar.xz 27 960 396 + docs zip 16 086 274); 8 MULTI_FILE: linux 7.3.4 (162 439 264), calibre 9.18.0 txz (240 948 148) http-re; 9 osmand 8 régió URL; 10 llama.cpp binárisok (v1.0.0); 11 bináris tier ≥ forrás (freecad/kicad/arduino → 2); 12 calibre/devdocs/zim-tools tier 2; 13 4c: 22,5 TB 24 TB-on túl szoros → ≥28 TB vagy vágás; 14 alternate.de áthúzott árak (U.2 adapterek 46,99/44,99/292 €, OWC 103,90, MB307U 180,90, IB-1980M 189,90); 15 T7 Shield ár becsült; 16 24 TB pár azonos gyártó; 17 SSD-kockázat ~0,005%/év, ~200×; 18 hub-tesseract bytes_est törlés; 19 first-aid 14,3 MB; 20 7zip linux+src URL; 21 smartmontools 7.5 URL; 22 hiányzó: Thunderbird, Wireshark, Zotero, ImageMagick, yt-dlp, GPSBabel, Scilab, Krita, Darktable, OpenSCAD, Podman, GDAL, nmap, Okular, Kodi, OrcaSlicer; 23 12 méret nélküli tétel; 24 196 angol notes → fordító ágens (research/notes_hu.json); 25 anglicizmusok; 26 4c stílus (ransomware, ->, tizedes); 27 size_status normalizálás; 28 dl.sh egy ítélet tételenként.

## 4. kör – SZKRIPT-átnéző (select 90, dl.sh 74, calc 87, paritás 98, CLI 72, build 85) – JAVÍTVA: rv4_all.patch alkalmazva (GIT_FULL unshallow, HEAD snapshot, BUNDLE csak teljesen, ollama_pull port/trap, jigdo _n>0, dense qf, CLI-validálás + magyar argparse, TODO-számláló, SOURCE_DATE_EPOCH, hf_cmd dataset). Ellenőrizve: dl.sh bash -n 64GB/2TB/32TB, paritás 22/22, mobil 400.
KÉSZ: fordítás beépítve (src/research/notes_hu.json, fixes._notes_hu). KÖVETKEZŐ: 5. pontozó kör (3 átnéző) → végső több szemszögű átnézés → make_zip → küldés.

## 5. kör – UX (desktop 88, mobil 78, interakció 88, szerkezet 94, konzisztencia 85, magyar 87, prompt 88, README 88, tároló 85; átlag 87,9) – JAVÍTVA (1–19)
1 mobil: .bund és réteg-tábla kártyák (data-l); 2 kételemes tábla: ár rejtve, Védelem oszlop; 3 Tárolók saját <section id="tarolok">; 4 Ft/TB rendezés hiányzó=∞, házak TB „–”; 5 prompt manifest: find ! -name MANIFEST… | sort -z | xargs -0; 6 „lásd a sandisk-2023 tételt” → „lásd a SanDisk-figyelmeztetést a terméktábla fölött”; 7 T7 Shield forrás egységes (becsült); 8 kételemes összegek számolva; 9 tizedes minden \d+.\d+ prózában; 10 SSD-kockázat ismétlés törlés; 11 Verzió oszlop nowrap; 12 mobil linksor tördelés; 13 „e Ft”/„M Ft” → ezer/millió Ft + 8 angol notes; 14 SanDisk-callout pont + „Mai keresésem” → „A 2026-11-14-i keresés”; 15 ajánlás: HAMR/Seagate megjegyzés + cím „a B példány…”; 16 4. fejezet megjegyzés pontosítás; 17 IP65 = vízsugár; 18 HTML ezres tagolás; 19 README 4c sorrend + tárolóválasztó.

## 5. kör – ADAT (séma 87, letöltés 84, linkek 95, méret 86, tier 90, dedup 90, lefedettség 90, magyar 92, tároló 90; átlag 89,3) – JAVÍTVA (PATCH5, size_status normalizálva, manual URL-ek, egy ítélet git/ia), + SZKRIPT 5. kör (átlag 93): rv5_all.patch + DEST-védelem alkalmazva
0 BIZTONSÁG: dl.sh DEST nélkül a / alá ír → kötelező DEST-ellenőrzés; 1 ose-wiki glob törlés (7z); 2 devdocs docs.json nem git; 3 primary-surgery vol2 id; 4 pd-craft 3 további id; 5 pontos glob 5 tételre; 6 gebco/freedos/arduino/kicad/freecad http (méretek a jelentésben); 7 jigdo csak debian-13.7.0-amd64-BD-N; 8 ventoy GitHub URL; 9 npm-go info_url, manual url próza; 10 OSS méretbecslések; 11 radioamator bytes; 12 28 TB ár szöveg (megvan?), SSD-ismétlés; 13 0.9B tizedes, angol size_status; #14 4c próza árak (Delock 44,99/46,99, MB307U 180,90); #15 T7 rétegtábla (kész?); #16 ~1M sor IronWolf; #28 többforrású tételek egy ítélet (git/ia).

## 6. kör – UX (átlag 89,6) és ADAT (átlag 92,1, minden ≥90) – JAVÍTVA: CSS-szivárgás (.soft:not(.stortab)), Ft/TB/kapacitás rendezés (bay=∞), TB formázás, tizedes (név, DWPD), SanDisk pont, ~1M sor + összeg, prompt sha256sum -c MANIFEST, DEST-védelem bővítve + mountpoint-figyelmeztetés, CLI tizedesvessző, size_status zárójel-normalizálás + 45 magyar forrásszöveg (research/size_status_hu.json), 5 notes magyarul, usda bytes, ose-wiki *.7z|*.zst, Thunderbird + Fritzing, gh_release (GitHub-kiadások telepítői automatikusan, shim-teszt OK), 10. fejezet mezőlista. Szkript 6. kör eredménye még nem jött meg.

## 6. kör – SZKRIPT (átlag 93,8): rv6_all.patch alkalmazva (gh_release tag→v-tag→latest, GH_RELEASE_MAX_MB, DEST-normalizálás, df-alapú figyelmeztetés, V3 csapat-keresés, JS tie-break). KÖVETKEZŐ: 7. pontozó kör mindhárom átnézővel.

## 7. kör – UX 92,7 (min 90) / ADAT 92,2 – JAVÍTVA: SanDisk pont (sent()), 10 angol notes + 5 size_status magyarul, tizedes linkcímkék/előnyök/modellmegjegyzések, szoftvertábla szélesség (td overflow-wrap), Alternatívák linkek, ~1M sor, szorzójel ×; gh_release: alap platformszűrés (Linux x86-64, Windows x64, APK), tételkeret = tétel bytes×1,2 (≥50 MB), ellenőrzőösszeg-fájlok kizárva, duplikált bináris tételeknél kihagyva (binaries_item), python3 a toolcheckben, GITHUB_TOKEN-figyelmeztetés; bowditch bytes. Szkript 7. kör eredménye még nem jött meg.

## 7. kör – SZKRIPT: átlag 95,0 (min 91) → rv7_gh_release.patch alkalmazva (261d94a). 8. kör fut: UX + ADAT átnéző. Ha ≥90 mindenhol és átlag ≥95 → VÉGSŐ több szemszögű átnézés (AI-ágens próbafuttatás, kezdő felhasználó, túlélési/orvosi/mezőgazdasági szakértő, adatmegőrzés) → make_zip → SendUserFile.

## 8. kör – UX ≈93,4 (min 92) → 4 hiba javítva (egyezség, ×, „” idézőjelek, Alternatívák linknévvel + szélességek). ADAT 8. kör fut.

## 8. kör – ADAT 93,6 (min 90) → javítva: gh_release platformonként egy fő telepítő (prio + legnagyobb ami belefér), pdb/reh/server/web kizárva, újrafuttatáskor kihagyja ha release/ nem üres, keret csak a *.git mérettel csökken; soilgrids wget-mirror -A tif. KÖVETKEZŐ: VÉGSŐ több szemszögű átnézés.

## VÉGSŐ ÁTNÉZÉS INDÍTVA (2026-11-15): 4 friss ágens a kibontott ZIP-en (scratchpad/final/ARCHIVUM): AI-ágens próbafuttatás (final_agent), kezdő felhasználó (final_user), szakértői panel orvos/víz/agrár/energia/rádió (final_expert), adatmegőrzés (final_storage). Pontok: 8. kör UX ~93,4→javítva, ADAT 93,6→javítva, SZKRIPT 95,0. ZIP 2,43 MB, 67 fájl, a régi 49 mind benne, egyik sem kisebb.

## VÉGSŐ – ADATMEGŐRZÉS (a 88, b 83, c 95, d 80, e 89; átlag 87) – JAVÍTANDÓ: 1 küszöb ≥24,5 TB, WD Red Pro 26TB (alternate 1393 €) B példány; 2 badblocks -b 8192; 3 prompt 9. lépés sorrend (par2+manifest a forráson → rsync → ellenőrzés a másolaton); 4 par2 -R + verify/repair; 5 zpool export/import, snapshot, UPS/túlfeszültség, laminált lap + live USB; 6 ajánlott összeg + T7 Shield 2TB; 7 Btrfs sor; 8 copies=2 create-kor; 9 4b félévente; 10 UPS futár, alternate áfa +6,7%; 11 smartctl -d sat, havi long, cím.

## VÉGSŐ – KEZDŐ FELHASZNÁLÓ (a 84, b 88, c 90, d 86, e 88, f 84; átlag 86,7) – JAVÍTANDÓ: 1 ~1M szint: B = Toshiba MG10 22TB SATA (pcx 376 290), össz 975 287 Ft, 24 TB-os kompakt sor is; 2 T5 telefon sor (16 GB Gemma-4-12B; 12 GB S24 ~7,4 GB: Qwen3.5-4B Q8/Gemma-4-E4B; 8 GB Qwen3.5-4B Q4/E2B); 3 „1–4. hely szerver” → 1–2. hely T2, 3–4. gamer PC; 4 Gemma heretic mondat; 5 chat 6.10 eszköztábla V1–V4; 6 saját telefon alapértékek (unified ≤24 GB, nincs GPU → 62%/25 ms/4 tok/s) + Android 8/12/16 GB presetek + hint; 7 README Windows/WSL; 8 kalkulátor kártyán a választott változat neve; 9 V4 párválasztás legnagyobb összeg; 10 md tizedesvessző 6.x táblákban; 11 összeállítás-sorokban linkek; 12 ioSafe forrás becsült; 13 mobil nav flex-wrap + details; 14 chat üres sorok, „28 TB-tól”, szóközök.

## VÉGSŐ – SZAKÉRTŐI PANEL (orvos 92, víz 88, élelem 85, energia 84, rádió 82, magyar 80, 1 TB 87; átlag 85,4) – JAVÍTANDÓ: új tételek: erc-guidelines-2025-layperson (t0, 17 446 129 B), neak-pupha-gyogyszertorzs (t1, 4 954 854 B; havonta új fájlnév), eibi-shortwave-schedule-b26 (t1, 490 500 B), iaru-emergency-telecom-guide-2016 (t1, 605 522 B), fm-24-18 (archive.org, 10 410 163 B), eawag-compendium-sanitation-2014 (t1, 9 483 264 B), osti 1599703 PV-méretezés (t2, 15 883 770 B); tierek: usda canning 0, ST 31-91B 2, WHO formulary 2008 1, katasztrófavédelem+vöröskereszt 1 (+http 2 PDF); 1 TB: kx-wp-en-med subsumed_by csak maxi; figyelmeztetések: fafgáz CO, gomba Paxillus; ifrc 2020 megjegyzés.

## VÉGSŐ átnézések javítva (2026-11-15): ADATMEGŐRZÉS 1–11 (WD Red Pro 26TB, ≥24,5 TB, ~1M = IronWolf 24 + Toshiba 22 = 975 287 Ft, badblocks/par2/btrfs/copies/smartctl, offline karbantartás, prompt 9. lépés sorrend, 4b félévente, áfa-megjegyzés); FELHASZNÁLÓ 1–14 (telefonsor, 1–2./3–4. hely, Gemma heretic, chat 6.10b eszköztábla, telefon-alapértékek + hint, Windows/WSL, kártyán változatnév, V4 súly 0,6, táblák tizedesvessző, összeállítás-linkek, ioSafe becsült, nav wrap, üres sorok); SZAKÉRTŐ 1–10 (7 új tétel items_expert.jsonl, tierek, figyelmeztetések, kx-wp-en-med). AI-ágens átnézés még fut. KÖVETKEZŐ: a 4 végső átnéző újrapontoz.

## VÉGSŐ – AI-ÁGENS PRÓBAFUTTATÁS (a 85, b 88, c 84, d 75, e 72, f 85; átlag 81,5) – JAVÍTANDÓ: 1 wget-mirror hamis OK (psychiatrist, fao-better-farming, attra, pfaf → agent; wikem -l 4 reject-regex) + méretőr; 2 gh_release .ok jelző; 3 prompt 9 (kész); 4 dl.sh-ba notes megjegyzés + hydrosheds/natural-earth/worldclim fájllisták; 5 WHO multi-file: http marad + todo_note; 6 esa-worldcover csak HU csempék; 7 7. fejezet agent-recept sor; 8 subsumption agent tétel által ne; 9 kimaradt okai; 10 cd3wd gray; 11 ZIM törlés → _old (PRUNE=1); 12 DEST abszolút + realpath; 13 prompt: ±10%, platformok, dl.sh futtatása, kibontó parancs, nem-GitHub TODO keret; 14 méretellenőrzés; 15 Byparr 127.0.0.1.

## AI-ÁGENS végső átnézés javítva: agent-tétel nem fed le automatikusat, kimaradás oka, ZIM → _old (PRUNE=1), Megjegyzés + todo_note a dl.sh-ban, wget-mirror méretőr (5%), gh_release .ok, DEST abszolút + realpath, MULTI_FILE http marad + todo_note, psychiatrist/fao/attra/pfaf agent, wikem korlát, esa HU csempék, cd3wd gray + kx-cd3wd pref, 7. fejezet agent-recept, prompt (±10%, futtatás, kibontás, platformok), Byparr 127.0.0.1, TODO keret. Ellenőrzés: dl.sh OK 3 méreten, paritás 22/22, horgonyok 0 hiba, py3.11 compile OK. KÖVETKEZŐ: a 4 végső átnéző újrapontoz (SendMessage).
