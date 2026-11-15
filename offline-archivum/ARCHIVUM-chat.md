# ARCHIVUM – chat-összefoglaló (2026-11-15)

> Ez a rövid változat chatbe tölthető. A teljes katalógus (1270 tétel, letöltési receptek, szkriptek) az `ARCHIVUM.md`-ben, az interaktív kalkulátor és SSD-tervező az `ARCHIVUM-LLM.html`-ben van. Ha a chat-AI kérdez, ezekre hivatkozz.

## 0. Hogyan használd ezt a fájlt

- **Ez a chat-változat** döntéshez és tervezéshez való: mit érdemes letölteni, melyik SSD kell, melyik AI-modell fut a gépeiden.
- **A letöltéshez** a teljes `ARCHIVUM.md` kell egy parancsot futtatni tudó AI-ágensnek (Claude Code, Codex stb.); annak 1. fejezetében van a kész prompt, a 11. fejezetben a `select_items.py`.
- **Interaktív kalkulátor, modelltábla, szoftverkönyvtár és SSD-tervező:** `ARCHIVUM-LLM.html` (böngészőben, internet nélkül).
- **Kérdezz rá bátran:** pl. „mi férjen fel egy 2 TB-os SSD-re, ha az orvoslás és a mezőgazdaság a fontos?” vagy „melyik cenzúrázatlan modell fut a 128 GB RAM-os gamer PC-men?”

## 3. Pontozási rendszer

Minden elem 6 szempontból kap **0–10** pontot (`scores` mező):

| Kód | Szempont | 10 pont példa | 1–2 pont példa |
|---|---|---|---|
| **S** | Túlélés: életben tartás az első 1–5 évben | Where There Is No Doctor, víztisztítás | TED előadások |
| **R** | Újjáépítés: technológia és intézmények hosszú távú visszaépítése | Machinery's Handbook, kémia-tankönyvek, Debian forrás | túrázós Q&A |
| **A** | Gyakorlatiasság: lépésről lépésre eljárás | katonai terepi kézikönyv, iFixit | lexikon |
| **U** | Pótolhatatlanság: más elem nem fedi le | CD3WD, Survivor Library | a Wikipedia egy részhalmaza |
| **Q** | Megbízhatóság: szakmai hitelesség | WHO, MSF, LibreTexts | videócsatorna, LLM |
| **O** | Offline kényelem: gyenge, áramtakarékos gépen is megy | PDF, ZIM | 70B+ LLM, adatbázis-szerver |

**Összpontszám** = súlyozott átlag (0–10), profil szerint:

| Profil | S | R | A | U | Q | O | Kinek |
|---|---|---|---|---|---|---|---|
| `balanced` | .30 | .25 | .15 | .15 | .10 | .05 | alapértelmezett |
| `survival` | .45 | .10 | .20 | .10 | .10 | .05 | rövid távú túlélés, család |
| `rebuild` | .15 | .40 | .15 | .15 | .10 | .05 | közösség, ipar visszaépítése |
| `education` | .10 | .35 | .10 | .15 | .20 | .10 | gyerekek, következő generáció oktatása |
| `computing` | .05 | .40 | .20 | .15 | .10 | .10 | IT-infrastruktúra újraépítése |

A `--focus medicine=2` megszorozza egy kategória pontjait.

**Tier (prioritási szint) – a letöltés sorrendje:**

| Tier | Jelentés |
|---|---|
| 0 | Életmentő: orvoslás, víz, élelem, katasztrófa-kézikönyvek. Kicsi, mindig bent van. |
| 1 | Alap tudásbázis és gyakorlati javítás: Wikipedia, iFixit, megfelelő technológia, szakképzés. |
| 2 | Tudomány és mérnöki tudás: tankönyvek, Q&A, kézikönyvek, térképek, alap LLM. |
| 3 | Szakmai mélység: forráskód, OS-tükör, nagy könyvtárak, nagyobb LLM-ek. |
| 4 | Oktatás és kultúra nagy méretben: Khan Academy, Gutenberg, StackOverflow. |
| 5 | Kényelmi elemek: TED, nagy médiatartalmak. |

## 4b. Hány TB-os SSD kell? – csomagok 1, 2, 4, 8, 16, 32, 64 és 128 TB-ra

A `select_items.py` az alábbi beállítással számolt minden méretre: **balanced** profil, magyar + angol + többnyelvű anyag, ingyenes és regisztrációs források. LLM-ek: **1–32 TB-ig T2-es gép, ~300 GB LLM-memória** (2× MS-S1, vagy RTX 6090 + RTX Pro), legfeljebb 4 modell; **64 és 128 TB-nál T1 szerver, ~2 TB LLM-memória, legfeljebb 8 modell**. Alap és cenzúrázatlan modell is (1–2 TB-on legfeljebb 1 cenzúrázatlan); az LLM legfeljebb a keret 35%-át foglalhatja (1 TB-on 25%-át); szerverformátum is (`--platform server`). **A nagyobb méret a kisebb teljes tudásanyagát megtartja**, csak bővít vagy jobb változatra cserél. Az LLM-ek kivételek: azok a hardverszinthez és a cenzúrázatlan-korláthoz igazodva cserélődhetnek (pl. 2 TB-on a 29 GB-os cenzúrázatlan modell helyére a 188 GB-os erősebb kerül). A címkén szereplő TB decimális (10¹² bájt), és 8% tartalék marad a fájlrendszernek.

### Összefoglaló

| SSD | Felhasználva | Elemek | LLM | Életmentő | Mezőgazd./energia | Lexikon | Mérnöki | Tudomány/oktatás | Magyar | Térkép | Szoftver/OS | Nyílt szoftverek | AI-modellek, adatok | Olvasók, eszközök |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **1TB** | 920 GB | 343 | 229 GB | 26 GB | 33,2 GB | 144 GB | 31,6 GB | 270 GB | 67,8 GB | 947 MB | 6,61 GB | 58,7 GB | 35,2 GB | 17 GB |
| **2TB** | 1,84 TB | 440 | 615 GB | 29,8 GB | 34,4 GB | 144 GB | 36,4 GB | 485 GB | 72,8 GB | 114 GB | 154 GB | 83,6 GB | 49,6 GB | 21,7 GB |
| **4TB** | 3,6 TB | 536 | 615 GB | 29,8 GB | 34,4 GB | 160 GB | 54,9 GB | 637 GB | 73,9 GB | 988 GB | 588 GB | 104 GB | 267 GB | 51,1 GB |
| **8TB** | 7,34 TB | 542 | 615 GB | 29,8 GB | 34,4 GB | 160 GB | 54,9 GB | 728 GB | 73,9 GB | 988 GB | 3,81 TB | 104 GB | 694 GB | 51,1 GB |
| **16TB** | 13,5 TB | 543 | 615 GB | 29,8 GB | 34,4 GB | 160 GB | 54,9 GB | 1,54 TB | 1,01 TB | 988 GB | 8,26 TB | 104 GB | 694 GB | 51,1 GB |
| **32TB** | 22,4 TB | 543 | 615 GB | 29,8 GB | 34,4 GB | 160 GB | 54,9 GB | 1,54 TB | 1,01 TB | 988 GB | 17,1 TB | 104 GB | 694 GB | 51,1 GB |
| **64TB** | 27,6 TB | 547 | 5,81 TB | 29,8 GB | 34,4 GB | 160 GB | 54,9 GB | 1,54 TB | 1,01 TB | 988 GB | 17,1 TB | 104 GB | 694 GB | 51,1 GB |
| **128TB** | 79,1 TB | 548 | 5,81 TB | 29,8 GB | 34,4 GB | 160 GB | 54,9 GB | 1,54 TB | 1,01 TB | 988 GB | 68,6 TB | 104 GB | 694 GB | 51,1 GB |

### Melyik méret mire elég – mi jön be az előző mérethez képest

- **1TB** – összesen 343 tétel; **új: 343**. Legnagyobb új tételek: Survivor Library full mirror on Internet Archive… (218 GB); Qwen3.8-Flash-Next · Qwen3.8-Flash-Next-GGUF · Q8_0 (GGUF) (167 GB); wikipedia_en_all_maxi_2026-08 (127 GB); MEK szakmai válogatás… (60 GB); Open Textbook Library (University of Minnesota) (40 GB); Qwen3.8-27B abliterated (huihui) / heretic-ara… (29 GB); CD3WD – Collection of Development Documents… (27,9 GB); Qwen3.8-27B (dense) · Qwen3.8-27B-i1-GGUF · Q5_K_M (GGUF) (19,5 GB). Életmentő (0. szintű) anyag: mind a 39 tétel bent van.
- **2TB** – összesen 440 tétel; **új: 99**, jobb változatra cserélt: 2. Legnagyobb új tételek: MiniMax-M3.1-Flash · MiniMax-M3.1-Flash-Quark-MXFP4… (240 GB); Qwen3.8-Flash-Next abliterated v2 (huihui GGUF)… (188 GB); khanacademy_en_all_2023-03 (180 GB); MIT OpenCourseWare (per-course ZIP downloads) (30 GB); SoilGrids 2.0 aggregated 1000 m (ISRIC) (13,4 GB); TeX Live (6,78 GB); Ubuntu 26.04.1 LTS Desktop amd64 ISO (6,48 GB); Project N.O.M.A.D. v1.35.1 (Crosstalk Solutions) (5 GB). Feljavítva: Debian 13.7.0 (trixie) amd64 full Blu-ray set… (130 GB); OpenStreetMap planet (teljes Föld, .osm.pbf) (95,8 GB). Életmentő (0. szintű) anyag: mind a 39 tétel bent van.
- **4TB** – összesen 536 tétel; **új: 96**, jobb változatra cserélt: 2. Legnagyobb új tételek: Copernicus DEM GLO-30 / GLO-90 (AWS Open Data) (725 GB); gutenberg_mul_all_2025-11 (253 GB); Protomaps daily planet basemap (PMTiles) (140 GB); Debian 13.7.0 source Blu-ray set (jigdo, 5 images) (126 GB); stackoverflow.com_en_all_2026-07 (115 GB); FineWeb-2 – magyar (hun_Latn) (98,5 GB); Linked OpenStreetMap × Wikidata × Wikipedia × Wikivoyage… (37,9 GB); Pl@ntNet-300K képadatkészlet (Zenodo) (31,7 GB). Feljavítva: Kolibri v0.19.5 + Khan Academy… (186 GB); Argos Translate / LibreTranslate + en-hu, hu-en… (9,13 GB). Életmentő (0. szintű) anyag: mind a 39 tétel bent van.
- **8TB** – összesen 542 tétel; **új: 6**. Legnagyobb új tételek: RACHEL (World Possible) offline content modules (1,75 TB); OpenAlex snapshot (scholarly metadata, CC0) (756 GB); The Stack v2 (BigCode) – csak megjegyzés (427 GB); CRAN full mirror (R packages, rsync) (410 GB); Wikidata full entity dump (JSON) / truthy N-Triples (304 GB); ted_mul_all_2026-09 (91,2 GB). Életmentő (0. szintű) anyag: mind a 39 tétel bent van.
- **16TB** – összesen 543 tétel; **új: 1**, jobb változatra cserélt: 2. Legnagyobb új tételek: F-Droid main repository mirror (rsync) (4,46 TB). Feljavítva: MEK – Magyar Elektronikus Könyvtár (OSZK) (1 TB); Project Gutenberg full mirror (rsync) (1,06 TB). Életmentő (0. szintű) anyag: mind a 39 tétel bent van.
- **32TB** – összesen 543 tétel; **új: 0**, jobb változatra cserélt: 1. Feljavítva: Debian full archive mirror (ftpsync / archvsync) (9,01 TB). Életmentő (0. szintű) anyag: mind a 39 tétel bent van.
- **64TB** – összesen 547 tétel; **új: 7**. Legnagyobb új tételek: Kimi K3.1 Pro · moonshotai.Kimi-K3.1-Pro-GGUF · MXFP4_MOE… (1,51 TB); Qwen3.8-2.4T-A95B (a hostolt „Qwen3.8-Max” alapja)… (1,31 TB); Hy4 preview (Hunyuan) · Hy4-preview-FP8 · FP8 (FP8) (814 GB); GLM-5.3 · GLM-5.3 · FP8 (FP8(native)) (756 GB); DeepSeek-V4.1-Flash-1017 · DeepSeek-V4.1-Flash-1017-GGUF… (508 GB); DeepSeek-V4.1-Flash-1017 abliterated (huihui GGUF)… (508 GB); Inkling 2 Small · Inkling-2-Small-GGUF · UD-Q8_K_XL (GGUF) (387 GB). Életmentő (0. szintű) anyag: mind a 39 tétel bent van.
- **128TB** – összesen 548 tétel; **új: 1**. Legnagyobb új tételek: PyPI full mirror (bandersnatch) (51,5 TB). Életmentő (0. szintű) anyag: mind a 39 tétel bent van.

**Ajánlás:**
- **1 TB** a minimum: minden életmentő és gyakorlati anyag, a lexikonok, a Survivor Library és egy erős LLM-páros.
- **2 TB:** 440 tétel – a nagy oktatási anyagok (Khan Academy, MIT OCW), a világtérkép és egy második erős LLM is befér.
- **4 TB** a teljes tudásanyaghoz: 536 tétel a lehetséges 548-ből (domborzati modell, teljes Gutenberg, Stack Overflow, magyar webkorpusz).
- **8–32 TB:** főleg nagy nyers adathalmazok és tükrök (Debian, F-Droid, CRAN, Wikidata, OpenAlex) jönnek. **A katalógus teljes automatikusan letölthető tartalma kb. 22,4 TB** – ez a „minden egyben” méret.
- **64 TB:** ugyanez + szerverszintű LLM-készlet (pl. a Kimi K3.1 Pro és a DeepSeek-V4.1 nagy kvantjai), hogy a jövőbeli erősebb géphez is meglegyen a legjobb modell.
- **128 TB:** + a teljes PyPI-tükör (51,5 TB) – csak ha Python-fejlesztés internet nélkül is fontos. Érdemi tudásanyag ezen felül már nincs.

### Melyik meghajtót vedd

- **Munkameghajtó (a gépben):** NVMe SSD, TLC NAND, DRAM-cache-sel, magas TBW-értékkel. A gyors SSD a modellek **betöltését** gyorsítja, a futásukat nem.
- **Archív példány (fiókban):** az SSD áram nélkül 1–3 évig tartja megbízhatóan az adatot (gyártófüggő, becslés). **Hosszú távra HDD** (CMR, nem SMR) vagy **M-DISC** kell. A HDD-t félévente (legalább évente) kapcsold be és olvasd végig (lásd 4c).
- **3-2-1 szabály:** 3 példány, 2 különböző adathordozón, 1 máshol tárolva. Javasolt összeállítás:
  - 1 NVMe a gépben;
  - 1 külső SSD vagy HDD otthon, fémdobozban (EMP és villám ellen);
  - 1 HDD máshol;
  - a 0. szint kinyomtatva.
- **Fájlrendszer:** exFAT (minden gép olvassa) vagy ext4. **FAT32-t ne használj**, mert 4 GB fölötti fájlt nem kezel.
- **Ellenőrzés:** minden fájl SHA-256 összegét mentsd egy `manifest`-be. Félévente futtasd le a `sha256sum -c` ellenőrzést, és cseréld ki a hibás példányt.

## 4c. Tárolók: mit vegyél, és hogyan oszd szét, hogy soha ne vesszen el

> **Kutatás dátuma:** 2026-11-14. **Árak:** ipon.hu, pcx.hu, aqua.hu, senetic.hu, alternate.de, amazon.de – „mért” = a bolt oldalán látott ár, „becsült” = keresőtalálat vagy számítás. Az arukereso.hu, az alza.hu, az emag.hu, az edigital.hu és a mediamarkt.hu az ellenőrzéskor blokkolta az automatikus lekérést – vásárlás előtt ott is nézd meg az árat. Árfolyam: 1 EUR = 365,60 Ft (EKB, 2026-11-13). Az alternate.de-s árak 19%-os német áfával; magyar szállításnál kb. +6,7%.
> **Piaci helyzet:** 2025 vége óta az AI-adatközpontok miatt hiány van; az SSD-k a 2025-ös ár 2–4-szeresébe, a HDD-k kb. +50%-ba kerülnek. Az árak gyorsan változnak.

### A lényeg – egy mondatban

**A teljes archívum (22,4 TB) egyetlen 26–32 TB-os HDD-re ráfér (8% tartalékkal ≥24,5 TB kell; 24 TB kevés, 26 TB már elég) – ez a „minden egyben” fizikai minimum. De egyetlen példány 10 év alatt kb. 13–22% eséllyel elvész; egy második, offline, más gyártótól származó példánnyal ez kb. 0,1–0,3%-ra csökken (~70×). Ezért a logikus, legkompaktabb megoldás: 2 db 26–32 TB-os HDD két különböző gyártótól (egy használatban, egy Faraday-tasakban, lőszerládában, másik helyen) + egy kicsi, strapabíró SSD a létfontosságú maggal.**

> **Kifejezések röviden:** *ZFS / Btrfs* = fájlrendszer, amely minden blokkhoz ellenőrzőösszeget ír, és észreveszi a sérülést · *scrub* = a teljes lemez végigolvasása és ellenőrzése · *pool* = a ZFS-ben egy vagy több lemezből álló tároló · *JBOD* = lemezek egyszerűen egymás mellett, RAID nélkül · *SMART* = a lemez saját állapotjelentése · *CMR* = hagyományos (archívumra alkalmas) HDD-írásmód · *HAMR* = új, hővel segített írású nagy HDD · *par2* = javítóadat, amellyel a kisebb sérülés helyreállítható · *Faraday-tasak* = fémhálós zsák villám és EMP ellen.

### Mi hova kerüljön – rétegek

| Réteg | Mi kerül rá | Méret (32 TB-os terv) | Ajánlott eszköz | Miért |
|---|---|---|---|---|
| **1. Mag** (mindig nálad, bármikor olvasható) | 0–1. szintű tudás: orvoslás, víz, élelem, túlélés, alapkönyvtár + 1 kis LLM | ~1,4 TB | strapabíró SSD 2–4 TB, alapajánlat: **Samsung T7 Shield 4TB** (IP65, 3 m esés, ~317 ezer Ft, becsült; a 2 TB-os ipon 198 391 Ft, mért) **és** a legfontosabb ~0,5 TB M-DISC BDXL lemezeken; olcsóbb HDD-s változat: LaCie Rugged 5TB (nem vízálló) vagy ADATA HD710 Pro (IP68) | telefonról, laptopról is olvasható, víz- és ütésálló; az M-DISC áram, mágnes és zsarolóvírus ellen véd |
| **2. Munka** (gyors, a gépben) | az LLM-modellek + amit naponta használsz | ~0,6 TB + tartalék | NVMe PCIe 5.0 SSD 4–8 TB a gamer PC-ben | a modell betöltése 8 TB-os Gen5-ről ~50 s; ez NEM archívum, mindenről van másolat |
| **3. Teljes archívum** (A példány, használatban) | minden: 2–5. szint, nagy tükrök, térképek, lexikonok | ~22,4 TB | 1 db 26–32 TB HDD (CMR) dokkolóban, ZFS-sel | a legolcsóbb TB-ár, havi ellenőrzéssel önjavító |
| **4. Offline másolat** (B példány) | ugyanaz, mint a 3. | ~22,4 TB | 1 db 26–32 TB HDD, **más gyártótól** (pl. Exos M 28TB + WD Red Pro 26TB), antisztatikus tasak + Faraday-tasak + tömített acél lőszerláda + szilikagél, **másik épületben** | tűz, víz, lopás, villám, EMP, zsarolóvírus, rossz parancs ellen; félévente be kell kapcsolni és végigolvasni |
| **5. (opcionális) 30 éves réteg** | a teljes archívum harmadik példánya | 22–128 TB | LTO-9 szalag (kazetta ~2 000 Ft/TB) | csak ~260 TB felett vagy 3+ másolatnál éri meg a ~4 M Ft-os meghajtó miatt; a meghajtót is meg kell őrizni |

### Ajánlott összeállítások árszintenként

| Keret | Összeállítás | Kapacitás | Ár | Mit bír ki | Megjegyzés / alternatíva |
|---|---|---|---|---|---|
| **~150–170 ezer Ft – „mag-archívum” ≤5 TB** | 1. példány: meglévő PC-lemez (vagy a mag egy belső SSD-n)<br>2. példány: [LaCie Rugged USB-C 5TB](https://www.amazon.de/dp/B079H7JVL3) – amazon.de 81 309 Ft (mért)<br>3. példány (offsite, más médium): 5x Verbatim [M-DISC BDXL](https://www.amazon.de/dp/B01E0CUU1C) 100GB – 24 111 Ft (mért) + Verbatim Slimline [BD-író](https://ipon.hu/shop/termek/verbatim-external-slimline-usb-30-blu-ray-writer-fekete/1530529) 65 689 Ft (ipon, mért), rajta a legfontosabb ~500 GB par2-vel | 5 TB HDD + 0,5 TB M-DISC | 171 109 Ft | lemezhiba (2 példány); a mag víz, EMP és zsarolóvírus ellen is (M-DISC) | 2x LaCie Rugged 5TB (162 618 Ft): két offline HDD két helyen, M-DISC nélkül |
| **~400 ezer Ft – 8 TB teljes redundanciával** | 2x Seagate IronWolf Pro 8TB – pcx 2× 157 390 = 314 780 Ft (becsült; a pcx-oldal nem volt újra ellenőrizhető)<br>[ICY BOX IB-RD3621U3](https://www.amazon.de/dp/B01N6AJUEI) dokkoló – 21 040 Ft (amazon.de, mért)<br>Faraday Defense [NEST-Z](https://www.amazon.de/dp/B07QXDDYTQ) – 27 797 Ft (mért) + [MFH .50 cal lőszerláda](https://military.eu/hu/p/mfh/mfh-us-ammo-box-m2a1-50-cal-loszeres-doboz-black-1247366) ~11 570 Ft (becsült)<br>3. példány: a meglévő PC/laptop, vagy később M-DISC mag | 2 × 8 TB | ~375 187 Ft | 1 lemezhiba; ha a B példány máshol van: tűz, víz, lopás; Faraday: EMP | A 2026-os HDD-árakon 400 ezer Ft-ból 22 TB-ot csak egy példányban lehet venni (Toshiba MG10 22TB, 376 290 Ft) – ez NEM 3-2-1, csak ha a mag (≤5 TB) külön rugged lemezre is kerül. |
| **~1 millió Ft – 22–24 TB, két gyártó, M-DISC mag (a 16 TB-os tervhez)** | 1. (használatban): [Seagate IronWolf Pro 24TB](https://www.pcx.hu/seagate-3-5-hdd-sata-iii-24tb-7200rpm-512mb-cache-ironwolf-pro-st24000nt002-216061) – pcx 448 790 Ft, ICY BOX dokkolóban (21 040 Ft), ZFS<br>2. (offline, másik helyen): [Toshiba MG10](https://www.pcx.hu/toshiba-22tb-7200rpm-sata-600-512mb-mg-series-mg10afa22te-203943)AFA22TE 22TB SATA – pcx 376 290 Ft (más gyártó, ugyanabba a dokkolóba); védelem: [NEST-Z](https://www.amazon.de/dp/B07QXDDYTQ) (27 797 Ft) + [lőszerláda](https://military.eu/hu/p/mfh/mfh-us-ammo-box-m2a1-50-cal-loszeres-doboz-black-1247366) (~11 570 Ft)<br>3. (más médium, mag): [Verbatim BD-író](https://ipon.hu/shop/termek/verbatim-external-slimline-usb-30-blu-ray-writer-fekete/1530529) (65 689 Ft) + 5× [M-DISC BDXL](https://www.amazon.de/dp/B01E0CUU1C) (24 111 Ft) | 24 + 22 TB + 0,5 TB M-DISC (a 16 TB-os tervhez) | 975 287 Ft | 1 lemezhiba, tűz/víz/lopás (külön helyszín), EMP (Faraday), zsarolóvírus (offline); a mag 3. médiumon is | A 16 TB-os tervhez (13,5 TB). A teljes 22,4 TB-hoz a 26–32 TB-os kételemes változat kell (~1,18 M Ft). |
| **~3–3,7 millió Ft – 64–66 TB, NAS + offline szett** | 1. (online, ZFS RAIDZ1): [UGREEN DXP4800 Plus](https://ipon.hu/shop/termek/ugreen-nasync-dxp4800-plus/2402913) (262 691 Ft) + 4x [Toshiba MG10 22TB](https://www.pcx.hu/toshiba-22tb-7200rpm-sata-600-512mb-mg-series-mg10afa22te-203943) (1 505 160 Ft) = 66 TB hasznos, TrueNAS SCALE, havi scrub<br>2. (offline, offsite): 3x [Seagate Exos M 28TB](https://ipon.hu/shop/termek/seagate-exos-m-28tb-35-7200rpm-512mb-sata-st28000nm003k/2397452) (3 × 578 590 = 1 735 770 Ft) = 84 TB, SnapRAID nélkül JBOD-ként, ZFS/lemez + SHA256 manifest, 2 lőszerládában, Faraday-tasakban (2x(27 797 + 11 570) = 78 734 Ft)<br>3. (mag): [M-DISC BDXL](https://www.amazon.de/dp/B01E0CUU1C) 10 db (48 222 Ft) + [BD-író](https://ipon.hu/shop/termek/verbatim-external-slimline-usb-30-blu-ray-writer-fekete/1530529) (65 689 Ft) | 66 TB NAS + 84 TB offline | ~3 696 266 Ft | 1 lemezhiba a NAS-ban + teljes offline másolat másik helyen | – |
| **Extrém 128 TB (~6–8 millió Ft)** | 1. [Synology DS1825+](https://ipon.hu/shop/termek/synology-diskstation-ds1825-8gb/2393648) + 8x [Toshiba MG10 22TB](https://www.pcx.hu/toshiba-22tb-7200rpm-sata-600-512mb-mg-series-mg10afa22te-203943) RAID6 = 132 TB hasznos – 3 631 110 Ft<br>2a. Offline HDD-szett: 6x MG10 22TB = 132 TB, 2 lőszerládában – 2 257 740 Ft (összesen ~5,9 millió Ft), VAGY<br>2b. LTO-9: [Quantum TC-L93CN-AR](https://ipon.hu/shop/termek/quantum-lto-9-tape-drive-tc-l93cn-ar/2235783) (3 967 890 Ft) + SAS HBA (becsült ~50–100 ezer Ft) + másolatonként 8 kazetta (8 × 36 690 = 293 520 Ft). 2 szalagmásolattal ~8,3 millió Ft; minden további 128 TB-os másolat csak ~294 ezer Ft (HDD-n ~2,26 millió Ft). | 132 TB + 132 TB (HDD vagy LTO) | ~5,9 M Ft (HDD-másolattal) / ~8,3 M Ft (LTO-val) | 2 lemezhiba a NAS-ban + teljes offline másolat; LTO-val 30 év bekapcsolás nélkül | A szalag 3+ másolatnál, vagy ha a 30 éves, bekapcsolás nélküli tárolás a cél, előzi meg a HDD-t. Ilyenkor a meghajtót is őrizd meg tartaléknak. |

### A legkompaktabb kételemes megoldás (a „minden egyben” kérésre; a B példány vizet, EMP-t és – habban, kikapcsolva – mérsékelt ütést is túlél)

| Változat | 1. eszköz | 2. eszköz (offline) | Védelem | Összesen |
|---|---|---|---|---|
| **26–32 TB – a teljes archívumhoz (ajánlott)** | [Seagate Exos M 28TB](https://ipon.hu/shop/termek/seagate-exos-m-28tb-35-7200rpm-512mb-sata-st28000nm003k/2397452) (ipon, 578 590 Ft, mért, előrendelés) dokkolóban; ZFS, havi scrub | [WD Red Pro 26TB](https://www.alternate.de/WD/Red-Pro-NAS-Festplatte-26-TB/html/product/100126007) (alternate.de 1393 €, magyar áfával ~543 403 Ft) – MÁS GYÁRTÓ, nem HAMR; antisztatikus tasak + hab + Faraday-tasak + tömített [lőszerláda](https://military.eu/hu/p/mfh/mfh-us-ammo-box-m2a1-50-cal-loszeres-doboz-black-1247366) + szilikagél, másik épületben | 1 lemezhiba, tűz/víz/lopás (külön helyszín), EMP, zsarolóvírus; gyártó- és technológia-diverzitás (HAMR + nem HAMR). A HAMR új technológia (itt az A példány, Exos M), ezért az A-n a havi scrubot és a SMART-figyelést ne hagyd ki; a B példányt félévente végig kell olvasni. Ha nincs készleten: 2× Toshiba MG10 22TB és a 9 TB-os Debian-tükör nélküli archívum (~13,5 TB). | ~1 182 400 Ft; a maggal (Samsung T7 Shield 2TB, ipon 198 391 Ft) ~1 380 791 Ft; M-DISC-kel ~1 470 591 Ft |
| **24 TB – két gyártó, a 16 TB-os tervhez** | [Seagate IronWolf Pro 24TB](https://www.pcx.hu/seagate-3-5-hdd-sata-iii-24tb-7200rpm-512mb-cache-ironwolf-pro-st24000nt002-216061) (pcx, 448 790 Ft, mért) [ICY BOX IB-RD3621U3](https://www.amazon.de/dp/B01N6AJUEI) dokkolóban (21 040 Ft); ZFS egylemezes pool, havi scrub | [Toshiba MG10](https://www.pcx.hu/toshiba-22tb-7200rpm-sata-600-512mb-mg-series-mg10afa22te-203943)AFA22TE 22TB SATA (pcx, 376 290 Ft, mért) – MÁS GYÁRTÓ, ugyanabba az USB-dokkolóba; Faraday-tasak + [lőszerláda](https://military.eu/hu/p/mfh/mfh-us-ammo-box-m2a1-50-cal-loszeres-doboz-black-1247366), másik épületben | 1 lemezhiba, tűz/víz/lopás/villám (ha a B példány máshol van), EMP (Faraday), zsarolóvírus (offline). A 16 TB-os tervhez (13,5 TB) – a teljes 22,4 TB-hoz ≥24,5 TB kell. | ~885 487 Ft |
| **32 TB – a legkisebb térfogat a teljes archívumhoz** | [Seagate Exos M 32TB](https://ipon.hu/shop/termek/seagate-exos-m-32tb-35-7200rpm-512mb-sata-st32000nm004k/2469374) (ipon, 784 390 Ft) | [Seagate IronWolf Pro 32TB](https://www.amazon.de/dp/B0FY75NDYC) (alza snapshot 575 890 Ft, becsült) – azonos gyártó, de más termékcsalád és gyártási sorozat (32 TB-ban ma nincs WD/Toshiba) | ugyanaz: NEST-Z + lőszerláda + szilikagél + külön helyszín | ~1 420 000 Ft (becsült, az IronWolf Pro ára nem ellenőrzött); csak ipon-ról: 2x Exos M 32TB = 1 568 780 Ft + kb. 60 ezer Ft tartozék |
| **5 TB-os mag – zsebméret** | [LaCie Rugged USB-C 5TB](https://www.amazon.de/dp/B079H7JVL3) (81 309 Ft) | ADATA HD710 Pro 4-5TB IP68 (119 741 Ft, 4 TB) – vagy egy második LaCie Rugged | ütés (rugged HDD-nél csak kikapcsolva), víz: csak az IP68-as ADATA; 2 példány | ~201 000 Ft |

*Miért nem egy RAID1-es doboz?* A RAID1 egy dobozban a lemezhibát túléli, de a tüzet, vizet, lopást, túlfeszültséget és EMP-t nem, ha a doboz csatlakoztatva van. Két külön, egymástól távol tárolt eszköz ugyanakkora térfogatban mindezt lefedi.

### A leggyorsabb, legprofibb (SSD) ág

- **Gamer PC munkameghajtó (LLM-ek):**
  - *profi:* Samsung 9100 PRO 8TB (hűtőbordás MZ-VAP8T0CW), ipon 868 089 Ft (mért); vagy alternate.de ajánlatkéréssel kb. 706 600 Ft + szállítás (UPS futár) (becsült, magyar áfával). A CPU-ra kötött Gen5 M.2_1 slotba kerüljön. Egy 700GB-os modell kb. 50 s alatt töltődik be. A meglévő Kingston 4TB marad második meghajtónak.
  - *közép:* Crucial T705 4TB, ipon 301 890 Ft (75 473 Ft/TB, mért), vagy Samsung 9100 PRO 4TB hűtőbordás 319 990 Ft. A meglévő Kingston 4TB-tal együtt 8TB Gen5, két különböző gyártótól.
  - *megjegyzés:* A modellek olvasás-túlsúlyosak, így a TBW mellékes. A munkameghajtó NEM archívum, mindenről legyen külső másolat.
- **Gyors hordozható másolat:**
  - *profi:* 8TB M.2 (pl. 9100 PRO 8TB) + OWC Express 1M2 USB4: kb. 924 700 Ft (ipon, mért), kb. 3,8 GB/s a PC és a ZBook USB4 portján. Strapabíró alternatíva: SanDisk Extreme PRO V2 4TB, 426 890 Ft (IP65, 2 GB/s).
  - *közép / olcsó:* SanDisk Extreme 8TB, ipon 565 589 Ft (70 699 Ft/TB, IP65, 3 m). A telefonokhoz elég (iPhone 15 Pro 10 Gbps, kb. 1 GB/s; S24 Ultra 5 Gbps, kb. 450 MB/s). Vásárlás után azonnal firmware-frissítés. Legolcsóbb kis tétel: Kingston XS2000 2TB, 109 090 Ft.
- **Vállalati all-flash, 30–120 TB:**
  - *olcsóbb (QLC):* Solidigm D5-P5336 30,72TB U.2 (senetic.hu ajánlatkérés; listaár 1 921 854 Ft/db, nincs raktáron, a valós ár valószínűleg magasabb). 4 db = 122,88TB, kb. 7,7 M Ft listaáron. Bekötés: Delock PCIe x16 → U.2 kártya (44,99 EUR, akciós) / M.2 → U.2 adapter (46,99 EUR, akciós), vagy HighPoint Rocket 1628A (1 679 EUR), ventilátorral. Hordozható: ICY DOCK MB307U-1VB (180,90 EUR, akciós).
  - *profi (TLC):* Kioxia CD8-P 15,36TB (ipon, rendelhető, 4 137 890 Ft/db, mért): 2 db = 30,72TB, kb. 8,3 M Ft; 8 db = 122,88TB, kb. 33,1 M Ft. TLC + PLP + Gen5, de ZFS RAIDZ/tükör és ventilátoros ház kell.
  - *őszinte értékelés:* 2026 novemberében az all-flash 30TB fölött TB-onként a fogyasztói Gen5 2,5-szerese, a HDD-nek pedig a sokszorosa. Ajánlás: 8TB Gen5 forró réteg + HDD tömegtár + második offline másolat. All-flash csak akkor, ha a költségvetés ezt indokolja.

*A teljes terméktábla linkekkel és az adatmegőrzési gyakorlat: `ARCHIVUM.md` 4c fejezet.*

## 5b. Mindenre a legjobb nyílt forráskódú szoftver és modell (tömören)

> Kategóriánként a legfontosabbak, prioritási sorrendben. Repólink, verzió, licenc, méret és alternatívák: `ARCHIVUM.md` 5b fejezet, illetve a HTML „Szoftverek és modellek” füle.

- **Szoftver: automatizálás, energia:** pvlib-python + NREL SAM, OpenEMS, Home Assistant, Node-RED, OpenPLC Runtime v3, Eclipse Mosquitto, mpp-solar, Frigate NVR (+3)
- **Szoftver: biztonság, titkosítás:** OpenSSH, GnuPG, KeePassXC, Nmap, cryptsetup, Vaultwarden, VeraCrypt, Tor (+1)
- **Szoftver: CAD/CAM, mérnöki:** EPANET, LinuxCNC, FreeCAD, grblHAL, pcb2gcode, LibreCAD, Universal G-code Sender, Seamly2D (+3)
- **Szoftver: egészségügy:** Community Health Toolkit, OpenMRS 3, OpenEMR, GNU Health, DHIS2, OpenELIS Global, openFDA, Orthanc DICOM szerver (+2)
- **Szoftver: elektronika, beágyazott:** KiCad, MicroPython, ESPHome, Arduino IDE, PlatformIO Core, ESP-IDF, ngspice, sigrok / PulseView (+2)
- **Szoftver: fejlesztés:** Eclipse Temurin JDK 25 LTS, Git, GCC, SQLite, CPython, Zeal, VSCodium, Rust toolchain (+2)
- **Szoftver: fordítás, OCR, beszéd, keresés:** GoldenDict-ng, Hunspell + magyarispell, Tesseract OCR, LibreTranslate, whisper.cpp, Piper TTS, Meilisearch, SearXNG
- **Szoftver: hálózat:** OpenWrt, Samba, Syncthing, OPNsense, rsync, WireGuard, Pi-hole, gpsd + chrony (+2)
- **Szoftver: iroda, dokumentumok:** MuPDF, LibreOffice, paperless-ngx, calibre, Thunderbird, KOReader, Pandoc, OCRmyPDF (+3)
- **Szoftver: kommunikáció, mesh:** Meshtastic, Reticulum Network Stack, Briar, Matrix Synapse + Element, Asterisk, ejabberd + Conversations, Mumble, Delta Chat (+2)
- **Szoftver: mezőgazdaság:** farmOS, OpenSprinkler firmware, WeeWX, FarmBot, Grocy
- **Szoftver: média, grafika:** yt-dlp, ImageMagick, FFmpeg, VLC media player, Jellyfin, Kodi, Krita, Inkscape (+7)
- **Szoftver: oktatás:** Anki, GCompris, Scratch 3
- **Szoftver: operációs rendszer, rendszereszközök:** Debian GNU/Linux, Firefox ESR, 7-Zip, memtest86+ és smartmontools, Ventoy, CUPS, Alpine Linux, SystemRescue (+7)
- **Szoftver: rádió, SDR:** CHIRP, Pat, fldigi, JS8Call, Dire Wolf, rtl-sdr, FreeDV, GNU Radio (+2)
- **Szoftver: szerver, virtualizáció:** Proxmox VE, Forgejo, QEMU/KVM, Caddy, PostgreSQL, Podman
- **Szoftver: tárolás, mentés:** OpenZFS, restic, TrueNAS SCALE, rclone, par2cmdline, Nextcloud, TestDisk & PhotoRec
- **Szoftver: térkép, navigáció:** OsmAnd, Organic Maps, QGIS, GDAL/OGR, osmium-tool, GPSBabel, Planetiler, GraphHopper (+2)
- **Szoftver: tudásszerverek, wiki:** kiwix-tools, Kolibri, Internet-in-a-Box, MediaWiki, Moodle, zimit + mwoffliner, BookStack
- **Szoftver: tudomány, adat:** Qalculate!, Miniforge + SciPy stack, Zotero, Fiji, GNU Octave, R + RStudio Desktop, Stellarium, Cantera (+3)
- **Szoftver: üzlet, közösség:** ODK, InvenTree, Ushahidi Platform, GnuCash, ERPNext, Koha ILS, Decidim, Gibbon (+2)
- **Szoftver: 3D-nyomtatás:** OpenSCAD, PrusaSlicer, Klipper, OrcaSlicer, OctoPrint, Mainsail
- **Adathalmazok:** Magyar Wikipédia parquet, Angol Wikipédia parquet, OpenStax tankönyvek szövege, PlantVillage növénybetegség-képek, Pl@ntNet-300K képadatkészlet, Wikiforrás magyar + angol, FineWeb-Edu sample-10BT, FineWeb-2 (+8)
- **Gyűjtőlisták (awesome):** awesome-open-hardware, awesome-selfhosted, sindresorhus/awesome, awesome-sysadmin, awesome-public-datasets
- **Modellek: beszéd (STT/TTS):** whisper.cpp ggml, Piper TTS magyar hangok, NVIDIA Parakeet-TDT 0.6B v3, faster-whisper large-v3-turbo, Qwen3-ASR 0.6B, Coqui XTTS-v2
- **Modellek: embedding, RAG:** BAAI bge-m3, EmbeddingGemma 2, Qwen3-Embedding 0.6B, BAAI bge-reranker-v2-m3
- **Modellek: fordítás:** NLLB-200 distilled 600M, MADLAD-400 3B MT, OPUS-MT tc-big hu→en, Argos Translate en↔hu csomagok
- **Modellek: hang:** BirdNET v2.4, Silero VAD, Demucs v4 hangforrás-szétválasztás
- **Modellek: képfelismerés:** BioCLIP 2, Pl@ntNet PlantCLEF2024 ViT-B DINOv2, FungiTastic gombahatározó ViT-B/16, RF-DETR Medium, SAM 2.1 Hiera-Large, Microsoft Florence-2 base, Depth Anything 3
- **Modellek: képgenerálás:** Real-ESRGAN ncnn-vulkan, FLUX.2 [klein] 4B
- **Modellek: OCR, dokumentum:** Tesseract tessdata_best, Datalab Indra OCR, PaddleOCR-VL 1.6, Docling layout + TableFormer modellek, GLM-OCR
- **Modellek: orvosi képelemzés:** TorchXRayVision, Google MedSigLIP-448, SkinTag SigLIP bőrelváltozás-osztályozó, Fundus diabéteszes retinopátia osztályozó
- **Platformok, gyűjtőhelyek:** Zenodo, Instructables, OSHWA Open Source Hardware tanúsított lista, Hackaday.io, Kaggle Datasets, Codeberg és GitLab.com, ModelScope, SourceForge (+1)
- **3D-nyomtatható tárgyak:** e-NABLE Hub, Printables, NIH 3D, Thingiverse, MyMiniFactory

## 6. Helyi LLM-ek (offline AI)

### 6.1 Kiadási idővonal: mi a legújabb gyártónként

| Gyártó | Legújabb nyílt modell | Kiadva (HF) | Paraméter (össz./aktív) | Kontextus | Licenc |
|---|---|---|---|---|---|
| Moonshot AI | [Kimi K3.1 Pro](https://huggingface.co/moonshotai/Kimi-K3.1-Pro) | 2026-11-02 | 2.8T / 104B | 1048576 | Kimi K3.1 Pro… |
| DeepSeek | [DeepSeek-V4.1-Flash-1017](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017) | 2026-10-17 | 552B backbone + 196B Engram memória… / ~16B… | 1000000 | MIT |
| Zhipu AI (Z.ai) | [GLM-5.3](https://huggingface.co/zai-org/GLM-5.3) | 2026-08-25 | 753B / ~40B (harmadik fél) | 1M (eval-beállítások és harmadik fél alapján) | GLM-5.3 custom… |
| Zhipu AI | [GLM-5.3-Flash](https://huggingface.co/zai-org/GLM-5.3-Flash) | 2026-08-25 | 320B (321,3B) / 18B | ~1M (eval 1M kontextussal; a kártyán nincs explicit tábla) | MIT |
| Xiaomi | [MiMo-V2.6-Pro (RL és MOPD változat) + MiMo-V2.6-Flash](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL) | 2026-09-21 (RL)… | Pro 1.02T; Flash 309B / Pro 42B; Flash 15B | 1000000 | MIT |
| inclusionAI (Ant Group) | [Ling-3.1-flash-1019](https://huggingface.co/inclusionAI/Ling-3.1-flash-1019) | 2026-10-27 | 560B (572B tárolt) / 25B | 1000000 | MIT |
| MiniMax | [MiniMax-M3.1-Flash](https://huggingface.co/MiniMaxAI/MiniMax-M3.1-Flash) | 2026-10-17 | ~428B / 23B | 1000000 | MiniMax Community… |
| Alibaba Qwen | [Qwen3.8-Flash-Next](https://huggingface.co/Qwen/Qwen3.8-Flash-Next) | 2026-08-24 | 180B = 125B MoE + 51B n-gram embedding… / 6B | 262144 natív, 1M-ig bővíthető | Qwen Community… |
| Alibaba Qwen | [Qwen3.8-2.4T-A95B (a hostolt „Qwen3.8-Max” alapja)](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B) | 2026-08-08 | 2.4T / 95B | 262144 natív, 1,010,000-ig bővíthető | Qwen3.8-Max… |
| StepFun | [Step 5 Preview](https://huggingface.co/stepfun-ai/Step-5-Preview) | 2026-09-20 | 600B / 27B | 1M-ig | StepFun Model… |
| Thinking Machines Lab | [Inkling 2 Small](https://huggingface.co/thinkingmachines/Inkling-2-Small) | 2026-11-04 | 594B / 17B | 1000000 | Apache-2.0 |
| Tencent | [Hy4 preview (Hunyuan)](https://huggingface.co/tencent/Hy4-preview) | 2026-08-27 | 770B (+10B MTP) / 49B | 1000000 | Apache-2.0 |
| Mistral AI | [Mistral Large 4 (1T-A52B)](https://huggingface.co/mistralai/Mistral-Large-4-1T-A52B) | 2026-09-30 | ~1T / 49B… | 1000000 | Mistral Ecosystem… |
| Meta (meta-models) | [Muse Spark Open (816B-A42B)](https://huggingface.co/meta-models/Muse-Spark-Open-816B-A42B) | 2026-09-15… | 816B / 42B | 1000000 | Muse Model… |
| Alibaba Qwen | [Qwen3.8-27B (dense)](https://huggingface.co/Qwen/Qwen3.8-27B) | 2026-08-05 | 27,8B / 27,8B (dense) | 262144 natív, 1M-ig bővíthető | Apache-2.0 |
| Meta | [Muse Glimmer 30B](https://huggingface.co/meta-models/Muse-Glimmer-30B) | 2026-08-09 | 29,6B (dense, vision encoderrel együtt) / 29,6B | 131072+ | Apache-2.0 |
| Google DeepMind | [Gemma 4 (31B, 26B-A4B, 12B, E4B, E2B)](https://huggingface.co/google/gemma-4-31B-it) | E2B/E4B 2026-03-02… | 31B dense (30,7B); 26B MoE (A4B)… / 31B; ~4B; 12B… | 256K (12B/26B/31B), 128K (E2B/E4B) | Apache-2.0 |
| NVIDIA | [NVIDIA Nemotron 3,5 (Super-VL-120B-A12B, Lightning-30B-A3B, Bolt-E4B)](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-BF16) | Super-VL 2026-10-12… | 124B; 31,6B; 8B (4B eff., Gemma 4 alapú) / 12B; 3B; 4B | Super-VL: [nem ellenőrzött]; Lightning: 1M-ig (H100-on 256K); Bolt-E4B: 64K | OpenMDW-1.1… |
| Alibaba Qwen / Xiaomi | [Qwen3.5-4B / Qwen3.5-9B (+ MiMo-V2.6-Distill-Qwen-9B)](https://huggingface.co/Qwen/Qwen3.5-4B) | 2026-02-27 (Qwen3.5)… | 4B; 9B / dense | [nem ellenőrzött] | Apache-2.0… |
| Meituan | [LongCat-2.5 (csak megjegyzésként)](https://huggingface.co/meituan-longcat/LongCat-2.5) | 2026-11-04 | 1.6T (1.78T tárolt) / ~48B | [nem ellenőrzött] | MIT |

**Viszonyítási pont – Claude Opus 5.5 (max): 59,1 pont = 100%** (AA Intelligence Index v5.0.1, 2026-11-12). Az index csúcsa ugyanekkor a Claude Fable 5.2 (64,6 = 109%).

| # | Modell | Típus | AA v5 | % Opus 5,5 | Forrás / számítás |
|---|---|---|---|---|---|
| – | *Claude Fable 5,2 (zárt, viszonyítás)* | zárt | 64,6 | 109% | mért |
| – | *Claude Opus 5,5 (zárt, viszonyítás)* | zárt | 59,1 | 100% | mért |
| 1 | Kimi K3.1 Pro | alap | 46,5 | 79% | mért AA v5 |
| 2 | Hy4 preview (Hunyuan) | alap | ~34,6 | ~59% | becslés |
| 3 | Qwen3.8-2.4T-A95B (a hostolt „Qwen3.8-Max” alapja) | alap | ~33,7 | ~57% | becslés |
| 4 | DeepSeek-V4.1-Flash-1017 | alap | 32,6 | 55% | mért AA v5 |
| 5 | GLM-5.3 | alap | 31,7 | 54% | mért AA v5 |
| 6 | DeepSeek-V4.1-Flash-1017 abliterated | **cenzúrázatlan** | ~31,6 | ~53% | alap 32,6 × 0,97 – B: abliteration, KL 0,067 (kicsi eltérés), nagy MoE |
| 7 | Inkling 2 Small | alap | 30,6 | 52% | mért AA v5 |
| 8 | GLM-5.3 abliterated | **cenzúrázatlan** | ~30,1 | ~51% | alap 31,7 × 0,95 – B: abliteration (patch), nagy MoE |
| 9 | LongCat-2.5 (csak megjegyzésként) | alap | ~30,0 | ~51% | becslés |
| 10 | MiMo-V2.6-Pro | alap | 29,9 | 51% | mért AA v5 |
| 11 | Ling-3.1-flash-1019 | alap | 29,6 | 50% | mért AA v5 |
| 12 | MiniMax-M3.1-Flash | alap | 29,1 | 49% | mért AA v5 |
| 13 | Qwen3.8-Flash-Next | alap | 28,6 | 48% | mért AA v5 |
| 14 | Step 5 Preview | alap | 28,5 | 48% | mért AA v5 |
| 15 | GLM-5.3-Flash | alap | 27,8 | 47% | mért AA v5 |
| 16 | Qwen3.8-Flash-Next abliterated v2 | **cenzúrázatlan** | ~27,2 | ~46% | alap 28,6 × 0,95 – B: abliteration v2, nagy MoE |
| 17 | MiniMax-M3.1-Flash abliterated | **cenzúrázatlan** | ~27,1 | ~46% | alap 29,1 × 0,93 – B: közösségi abliteration, nem ellenőrzött |
| 18 | MiMo-V2.6-Flash | alap | 26,7 | 45% | mért AA v5 |
| 19 | GLM-5.3-Flash abliterated | **cenzúrázatlan** | ~26,4 | ~45% | alap 27,8 × 0,95 – B: abliteration, nagy MoE |
| 20 | Mistral Large 4 (1T-A52B) | alap | 25,3 | 43% | mért AA v5 |
| 21 | Muse Spark Open (816B-A42B) | alap | 24,9 | 42% | mért AA v5 |
| 22 | Qwen3.8-27B (dense) | alap | 20,1 | 34% | mért AA v5 |
| 23 | NousResearch Arete-27B | **cenzúrázatlan** | ~19,0 | ~32% | alap 19,0 × 1 – B: SFT, csak propaganda-szűrés |
| 24 | Qwen3.8-27B abliterated | **cenzúrázatlan** | ~18,7 | ~32% | alap 20,1 × 0,93 – B: abliteration, közepes dense |
| 25 | Kimi-K3 Abliterated V1 | **cenzúrázatlan** | ~16,2 | ~27% | alap 17,4 × 0,93 – B: közösségi abliteration, minőség nem ellenőrzött |
| 26 | Nemotron-3.5-Super-VL-120B | alap | 13,6 | 23% | mért AA v5 |
| 27 | Qwen3.6-35B-A3B uncensored-heretic | **cenzúrázatlan** | ~8,0 | ~14% | alap 8,0 × 1 – M: NatInt 31,03→31,62 (nincs veszteség) |
| 28 | Mistral-Small-4-119B-2603 heretic | **cenzúrázatlan** | ~7,6 | ~13% | alap 8,0 × 0,95 – B: heretic, MoE |
| 29 | Muse Glimmer 30B | alap | 6,3 | 11% | mért AA v5 |
| 30 | Nemotron-3.5-Lightning-30B | alap | 5,5 | 9% | mért AA v5 |
| 31 | Gemma-4-31B | alap | 4,4 | 7% | mért AA v5 |
| 32 | gemma-4-31B-it heretic | **cenzúrázatlan** | 4,1 | 7% | alap 4,4 × 0,939 – M: NatInt 38,91→36,53 |
| 33 | gpt-oss-120b heretic | **cenzúrázatlan** | 3,6 | 6% | alap 3,8 × 0,958 – M: NatInt 33,68→32,25 |
| 34 | Gemma-4-26B-A4B | alap | ~3,5 | ~6% | becslés (nincs AA-pont) |
| 35 | gemma-4-26B-A4B-it ultra-uncensored-heretic | **cenzúrázatlan** | ~3,5 | ~6% | alap 3,5 × 1 – M: NatInt 34,44→35,71 (nincs veszteség) |
| 36 | Gemma-4-12B | alap | ~3,0 | ~5% | becslés (nincs AA-pont) |
| 37 | Qwen3.5-9B | alap | ~3,0 | ~5% | becslés (nincs AA-pont) |
| 38 | gemma-4-12B-it uncensored-heretic | **cenzúrázatlan** | ~2,8 | ~5% | alap 3,0 × 0,93 – B: heretic, kis dense |
| 39 | Gemma-4-E4B | alap | ~2,5 | ~4% | becslés (nincs AA-pont) |
| 40 | Nemotron-3.5-Bolt-E4B | alap | ~2,5 | ~4% | becslés (nincs AA-pont) |
| 41 | gemma-4-E4B-it heretic | **cenzúrázatlan** | ~2,5 | ~4% | alap 2,5 × 1 – M: NatInt 18,21→18,73 (nincs veszteség) |
| 42 | Qwen3.5-9B heretic-v2 | **cenzúrázatlan** | ~2,3 | ~4% | alap 3,0 × 0,781 – M: NatInt 30,98→24,2 |
| 43 | gpt-oss-20b heretic | **cenzúrázatlan** | ~2,1 | ~4% | alap 2,5 × 0,829 – M: NatInt 27,18→22,52 |
| 44 | Qwen3.5-4B | alap | ~2,0 | ~3% | becslés (nincs AA-pont) |
| 45 | Qwen3.5-4B heretic-2.0 | **cenzúrázatlan** | ~1,9 | ~3% | alap 2,0 × 0,936 – M: NatInt 23,88→22,35 (SOMPOA-változat) |
| 46 | Gemma-4-E2B | alap | ~1,5 | ~3% | becslés (nincs AA-pont) |
| 47 | gemma-4-E2B-it ultra-uncensored-heretic | **cenzúrázatlan** | ~1,4 | ~2% | alap 1,5 × 0,93 – B: heretic, nagyon kis modell |

Az alapmodellek pontjai (csak alap, mért):

| Nyílt modell | AA v5.0.1 | % Opus 5,5 |
|---|---|---|
| Kimi K3.1 Pro | 46,5 | 79% |
| Hy4 (a végleges; mi a preview-t archiváljuk) | 34,6 | 59% |
| Qwen3.8 2.4T (becslés a Qwen3.8-Max API 33,7-es pontjából) | ~33,7 | ~57% |
| DeepSeek-V4.1-Flash-1017 | 32,6 | 55% |
| GLM-5.3 | 31,7 | 54% |
| Inkling 2 Small | 30,6 | 52% |
| MiMo-V2.6-Pro | 29,9 | 51% |
| Ling-3.1-flash | 29,6 | 50% |
| MiniMax-M3.1-Flash | 29,1 | 49% |
| Qwen3.8-Flash-Next | 28,6 | 48% |
| Step-5 Preview | 28,5 | 48% |
| GLM-5.3-Flash | 27,8 | 47% |
| MiMo-V2.6-Flash | 26,7 | 45% |
| Mistral Large 4 | 25,3 | 43% |
| Muse Spark Open | 24,9 | 42% |
| Qwen3.8-27B | 20,1 | 34% |
| Kimi K3 | 17,4 | 29% |
| Nemotron 3,5 Super VL | 13,6 | 23% |
| Muse Glimmer 30B | 6,3 | 11% |
| Nemotron 3,5 Lightning | 5,5 | 9% |
| Gemma 4 31B | 4,4 | 7% |
| gpt-oss-120b | 3,8 | 6% |

**Kódolás:** az AA a v5-ben megszüntette a külön Coding Indexet. A kódolási kategória (az index 25%-a) két mérésből áll: FrontierCode 2.0 (15%) és Terminal-Bench 4.0 (10%). Modellenkénti adat csak részben nyilvános:
- **FrontierCode 2.0:** Opus 5.5 46% (első), DeepSeek-V4.1-Flash 28%. Ez a legjobb nyílt modell, és az Opus **~61%-a**.
- **Terminal-Bench 4.0:** a Kimi K3.1 Pro 67%-kal első. Az Opus értéke nem nyilvános.
- A többi nyílt modell kódolási pontja nem elérhető, ezért a táblákban az összesített index százaléka szerepel.

**Mit jelent a százalék:** az összesített pontszám aránya, nem a „tudás” lineáris mértéke. Az index nehéz, részben privát feladatokból áll. 50% azt jelenti, hogy a modell a feladatok kb. felénél teljesít annyit, mint az Opus 5.5; a könnyű, hétköznapi feladatokon a különbség jóval kisebb. Az alacsony pontú kis modellek (Gemma 4, gpt-oss) egyszerű kérdésekre jól válaszolnak, de a nehéz, többlépéses feladatokban messze elmaradnak.

**A Kimi K3.1 létezik, de csak `moonshotai/Kimi-K3.1-Pro` néven** (2026-11-02, 2,8T összes / 104B aktív paraméter).
- A GGUF-változata kísérleti: új `kimi_k31` architektúra, egyes kvantokhoz llama.cpp-fork kell.
- Szerveren a natív INT4 (1,56 TB) vagy az NVFP4 a stabil út.

### 6.2 Melyik gépre mi kerüljön: hardverszintek

| Szint | Hardver | Legokosabb, ami elfér | Alternatíva / tartalék |
|---|---|---|---|
| **T1** | 8×H100/H200/B200 vagy ≥1,5 TB RAM | Kimi K3.1 Pro natív INT4 (1,56 TB) vagy MXFP4_MOE GGUF (1,51 TB) | DeepSeek-V4.1-Flash natív (510 GB, vLLM/SGLang, stabil); GLM-5.3 FP8 |
| **T2** | 256–1000 GB unified/RAM/VRAM (2× Strix Halo / MS-S1, Mac Studio 512 GB, 2× Mac exo, EPYC 768 GB + GPU, DGX Station, 6090 + RTX Pro) | 512 GB Mac: DeepSeek-V4.1-Flash MLX oQ4e (432 GB). 2× Mac / 768 GB+: Kimi K3.1 Pro KLX-IQ2_XXS (710 GB) | GLM-5.3 MLX 4bit (418 GB); MiniMax-M3.1-Flash oQ4e (249 GB) |
| **T3** | Gamer PC 24–32 GB VRAM + 64–192 GB RAM | 128–192 GB RAM: Qwen3.8-Flash-Next UD-Q4_K_XL (111 GB) MoE-offloaddal. Csak GPU: Qwen3.8-27B Q4/Q5 (17–20 GB) | GLM-5.3-Flash UD-Q3_K_XL (148 GB); Gemma-4-31B QAT (17,7 GB) |
| **T4** | Laptop: MacBook 36–128 GB, vagy Windows 8–16 GB VRAM | 64 GB Mac: Qwen3.8-27B MLX 8bit (29,5 GB). 16 GB VRAM: Qwen3.8-27B UD-Q3_K_XL (13 GB) | Gemma-4-26B-A4B (gyors MoE), Gemma-4-12B QAT (7 GB) |
| **T5** | Telefon 8–16 GB RAM | 16 GB: Gemma-4-12B QAT q4_0 (7 GB). 12 GB (pl. S24 Ultra, ~7,4 GB jut a modellnek): Qwen3.5-4B Q8 / Gemma-4-E4B. 8 GB: Qwen3.5-4B Q4 / Gemma-4-E2B QAT (3,4 GB) | Qwen3.5-4B Q4_K_M (2,7 GB), LFM3-1.7B (1,1 GB) |

- **Ökölszabály:** a modellfájl mérete + 10–20% (KV cache) férjen el a memóriában.
- **Kódban:** `--hw T3 --mem 160GB` szűr, a `--platform mac|server` engedi az MLX vagy a vLLM-formátumokat. Alapból csak a mindenhol futó GGUF és Ollama formátum szerepel.
- **Magyar nyelv:** a Mistral Large 4 az egyetlen nagy modell, amelynek a kártyája kifejezetten az EU-nyelveket célozza. Kisebb gépen a Gemma 4 és a Qwen3.8-27B jó magyarul (becslés, magyar benchmark nincs).

### 6.5 Cenzúrázatlan modellek

#### Rangsor: cenzúrázatlan modellek

- **Sorrend:** a cenzúrázatlan változat *számolt* intelligenciája szerint (AA v5 skálán).
- **Számolt pont:** az alapmodell AA v5 pontja × (cenzúrázatlan/alap) arány. Az arány „M” jelnél a UGI ranglista NatInt-méréséből jön. „B” jelnél becslés: nagy MoE abliteration 0,95–0,97, közösségi és nem ellenőrzött 0,93, kis dense 0,93.
- **% Opus 5.5:** a számolt pont / 59,1 (Claude Opus 5.5 max, AA v5.0.1).
- **„Cenz.” és „HU” oszlop:** 0–10-es kutatói becslés.
- **`~` jel az AA oszlopban:** az alapmodellnek nincs AA v5 pontja, az érték becslés.
- **UGI NatInt:** a természetes intelligencia mérése az Uncensored General Intelligence ranglistán, az alap → cenzúrázatlan változás.
- **„Leggyengébb gép”:** az a legkisebb hardverszint, amelyen még fut GGUF-változat.
- **Méretek:** a Hugging Face API-ból (2026-11-14).

| # | Pontos név (repó) | Alapmodell (kiadva) | Paraméter | AA v5 alap | **AA v5 cenzúrázatlan (számolt)** | **% Opus 5,5** | Számítás | Módszer | Cenz. | HU | UGI / NatInt | Változat | Méret min–max | Leggyengébb gép | Licenc |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **[huihui-ai/Huihui-DeepSeek-V4.1-Flash-1017-abliterated-GGUF](https://huggingface.co/huihui-ai/Huihui-DeepSeek-V4.1-Flash-1017-abliterated-GGUF)** | `deepseek-ai/DeepSeek-V4.1-Flash-1017` (2026-10-17) | 763,2B total (safetensors); 384 routed… | 32,6 | **~31,6** | **~53%** | × 0,97 (B: abliteration, KL 0,067 (kicsi eltérés), nagy MoE) | Abliteration (huihui: 18 attn_output tenzor) + Heretic (pqhaz) + Abliteration FP8 (mrfakename) | 9 | 8 | elutasítás 97→4% chat, 98→9% think; KL 0,067 (mrfakename kártya) | 5 | 233,0 GB – 510,3 GB | T2: `huihui-ai/Huihui-DeepSeek-V4.1-Flash-1017-abliterated-GGUF` ['UD-IQ1_S/*'] (233,0 GB) | MIT |
| 2 | **[huihui-ai/Huihui-GLM-5.3-abliterated-GGUF](https://huggingface.co/huihui-ai/Huihui-GLM-5.3-abliterated-GGUF)** | `zai-org/GLM-5.3` (2026-08-25) | 753,3B (safetensors); ctx 1M | 31,7 | **~30,1** | **~51%** | × 0,95 (B: abliteration (patch), nagy MoE) | Abliteration (huihui patch-GGUF az unsloth kvantra) | 8,5 | 7,5 | nincs mérés | 1 | 216,7 GB – 216,7 GB | T2: `huihui-ai/Huihui-GLM-5.3-abliterated-GGUF` ['UD-IQ1_S/*'] (216,7 GB) | other (glm-5.3) |
| 3 | **[huihui-ai/Huihui-Qwen3.8-Flash-Next-abliterated-v2-GGUF](https://huggingface.co/huihui-ai/Huihui-Qwen3.8-Flash-Next-abliterated-v2-GGUF)** | `Qwen/Qwen3.8-Flash-Next` (2026-08-24) | 125B, ebből 6B aktív + 51B n-gram embedding… | 28,6 | **~27,2** | **~46%** | × 0,95 (B: abliteration v2, nagy MoE) | Abliteration v2 (huihui) | 9 | 8,5 | nincs mérés (Qwen3.8 még nincs az UGI-n) | 9 | 68,2 GB – 188,2 GB | T3: `huihui-ai/Huihui-Qwen3.8-Flash-Next-abliterated-v2-GGUF` ['unsloth-UD-IQ4_XS/*'] (93,7 GB) | other (qwen-community-1.0) |
| 4 | **[orcarouter/MiniMax-M3.1-Flash-abliterated-GGUF](https://huggingface.co/orcarouter/MiniMax-M3.1-Flash-abliterated-GGUF)** | `MiniMaxAI/MiniMax-M3.1-Flash` (2026-10-17) | kb. 428B / 23B active (kártya); ctx 1M | 29,1 | **~27,1** | **~46%** | × 0,93 (B: közösségi abliteration, nem ellenőrzött) | Abliteration (orcarouter) | 7 | 6,5 | minőség nem ellenőrzött; gated:auto | 1 | 111,9 GB – 111,9 GB | T3: `orcarouter/MiniMax-M3.1-Flash-abliterated-GGUF` ['Mix-128G/*'] (111,9 GB) | other (minimax-community) |
| 5 | **[huihui-ai/Huihui-GLM-5.3-Flash-abliterated-GGUF](https://huggingface.co/huihui-ai/Huihui-GLM-5.3-Flash-abliterated-GGUF)** | `zai-org/GLM-5.3-Flash` (2026-08-25) | 320B total / 18B active (kártya); VL; ctx 1M | 27,8 | **~26,4** | **~45%** | × 0,95 (B: abliteration, nagy MoE) | Abliteration (huihui) | 8,5 | 7,5 | nincs mérés | 10 | 93,1 GB – 291,8 GB | T3: `huihui-ai/Huihui-GLM-5.3-Flash-abliterated-GGUF` ['UD-IQ3_XXS/*'] (120,4 GB) | MIT |
| 6 | **[NousResearch/Arete-27B](https://huggingface.co/NousResearch/Arete-27B)** | `Qwen/Qwen3.8-27B` (2026-08-05) | 27,4B | ~19,0 | **~19,0** | **~32%** | × 1 (B: SFT, csak propaganda-szűrés) | SFT (propaganda-keretezés eltávolítása, az R1-1776 utódja) | 4 | 8 | NEM általános elutasítás-eltávolító; propaganda 22%→0,9% | 2 | 15,2 GB – 17,2 GB | T4: `bartowski/NousResearch_Arete-27B-GGUF` ['NousResearch_Arete-27B-IQ4_XS.gguf'] (15,2 GB) | Apache-2.0 |
| 7 | **[huihui-ai/Huihui-Qwen3.8-27B-abliterated-GGUF](https://huggingface.co/huihui-ai/Huihui-Qwen3.8-27B-abliterated-GGUF)** | `Qwen/Qwen3.8-27B` (2026-08-05) | 27,8B dense; VL; ctx 262k → 1M | 20,1 | **~18,7** | **~32%** | × 0,93 (B: abliteration, közepes dense) | Abliteration (huihui) / Heretic-ARA (trohrbaugh) | 8,5 | 8,5 | nincs mérés | 6 | 10,9 GB – 29,0 GB | T4: `huihui-ai/Huihui-Qwen3.8-27B-abliterated-GGUF` ['Huihui-Qwen3.8-27B-abliterated-UD-IQ4_XS.gguf'] (14,4 GB) | Apache-2.0 |
| 8 | **[Uniboshi/Kimi-K3-Abliterated-V1](https://huggingface.co/Uniboshi/Kimi-K3-Abliterated-V1)** | `moonshotai/Kimi-K3` (2026-06-13) | 2.8T total / 104B active (kártya); ctx 1M | 17,4 | **~16,2** | **~27%** | × 0,93 (B: közösségi abliteration, minőség nem ellenőrzött) | Abliteration (közösségi, Uniboshi) | 7 | 8 | minőség nem ellenőrzött; gated:auto | 1 | 1,51 TB – 1,51 TB | T1: `Uniboshi/Kimi-K3-Abliterated-V1-GGUF` ['MXFP4_MOE/*'] (1,51 TB) | other (kimi-k3) |
| 9 | **[llmfan46/Qwen3.6-35B-A3B-uncensored-heretic-GGUF](https://huggingface.co/llmfan46/Qwen3.6-35B-A3B-uncensored-heretic-GGUF)** | `Qwen/Qwen3.6-35B-A3B` (2026-04-15) | 36B MoE, 3B aktív; VL; ctx 262k | ~8,0 | **~8,0** | **~14%** | × 1 (M: NatInt 31,03→31,62 (nincs veszteség)) | Heretic (llmfan46) / Abliteration-MTP (huihui) | 10 | 8 | UGI 50,9; NatInt 31,03→31,62 (+0,6) | 2 | 16,9 GB – 21,2 GB | T4: `llmfan46/Qwen3.6-35B-A3B-uncensored-heretic-GGUF` ['Qwen3.6-35B-A3B-uncensored-heretic-Q4_K_M.gguf'] (21,2 GB) | Apache-2.0 |
| 10 | **[darkc0de/Mistral-Small-4-119B-2603-heretic](https://huggingface.co/darkc0de/Mistral-Small-4-119B-2603-heretic)** | `mistralai/Mistral-Small-4-119B-2603` (2026-01-23) | 119,4B MoE; VL; ctx 1M (GGUF metadata) | ~8,0 | **~7,6** | **~13%** | × 0,95 (B: heretic, MoE) | Heretic (darkc0de) | 8 | 8 | az alap is engedékeny (UGI W10 4,5) | 6 | 43,4 GB – 126,5 GB | T3: `Rioky/Mistral-Small-4-119B-2603-heretic-gguf` ['Mistral-Small-4-119B-2603-heretic-Q4_K_S.gguf'] (67,7 GB) | Apache-2.0 (bázis); a… |
| 11 | **[coder3101/gemma-4-31B-it-heretic](https://huggingface.co/coder3101/gemma-4-31B-it-heretic)** | `google/gemma-4-31B-it` (2026-03-11) | 31,3B dense; VL; ctx 256k | 4,4 | **4,1** | **7%** | × 0,939 (M: NatInt 38,91→36,53) | Heretic (coder3101 / llmfan46) | 10 | 8,5 | UGI 65,69 (legjobb 40B alatt); NatInt 38,91→36,53 (−2,4) | 4 | 16,9 GB – 25,2 GB | T4: `mradermacher/gemma-4-31B-it-heretic-GGUF` ['gemma-4-31B-it-heretic.IQ4_XS.gguf'] (16,9 GB) | Apache-2.0, NEM gated |
| 12 | **[MuXodious/gpt-oss-120b-tainted-heresy](https://huggingface.co/MuXodious/gpt-oss-120b-tainted-heresy)** | `openai/gpt-oss-120b` (2025-08-04) | 116,8B; az aktív kb. 5,1B… | 3,8 | **3,6** | **6%** | × 0,958 (M: NatInt 33,68→32,25) | Heretic (MuXodious tainted-heresy / kldzj) | 8,5 | 6 | UGI 53,81; NatInt 33,68→32,25 (−1,4) | 3 | 62,2 GB – 63,4 GB | T3: `MuXodious/gpt-oss-120b-tainted-heresy-GGUF` ['gpt-oss-120B-tainted-heresy-MXFP4_MoE.gguf'] (63,4 GB) | Apache-2.0 |
| 13 | **[llmfan46/gemma-4-26B-A4B-it-ultra-uncensored-heretic-GGUF](https://huggingface.co/llmfan46/gemma-4-26B-A4B-it-ultra-uncensored-heretic-GGUF)** | `google/gemma-4-26B-A4B-it` (2026-03-11) | 25,8B MoE, kb. 4B aktív; VL | ~3,5 | **~3,5** | **~6%** | × 1 (M: NatInt 34,44→35,71 (nincs veszteség)) | Heretic, ultra (llmfan46) | 10 | 8 | UGI 52,39; NatInt 34,44→35,71 (+1,3) | 2 | 13,3 GB – 16,8 GB | T4: `llmfan46/gemma-4-26B-A4B-it-ultra-uncensored-heretic-GGUF` ['gemma-4-26B-A4B-it-ultra-uncensored-heretic-Q4_K_M.gguf'] (16,8 GB) | Apache-2.0 |
| 14 | **[llmfan46/gemma-4-12B-it-uncensored-heretic-GGUF](https://huggingface.co/llmfan46/gemma-4-12B-it-uncensored-heretic-GGUF)** | `google/gemma-4-12B-it` (2026-05-23) | 11,96B; any-to-any | ~3,0 | **~2,8** | **~5%** | × 0,93 (B: heretic, kis dense) | Heretic (llmfan46) / Abliteration QAT (huihui) | 9 | 8 | nincs mérés | 1 | 8,5 GB – 8,5 GB | T4: `llmfan46/gemma-4-12B-it-uncensored-heretic-GGUF` ['gemma-4-12B-it-uncensored-heretic-Q4_K_M.gguf'] (8,5 GB) | Apache-2.0 |
| 15 | **[coder3101/gemma-4-E4B-it-heretic](https://huggingface.co/coder3101/gemma-4-E4B-it-heretic)** | `google/gemma-4-E4B-it` (2026-03-02) | 8B összesen / kb. 4,5B effektív; any-to-any… | ~2,5 | **~2,5** | **~4%** | × 1 (M: NatInt 18,21→18,73 (nincs veszteség)) | Heretic (coder3101 / p-e-w) | 9,5 | 7,5 | NatInt 18,21→18,73 (+0,5) | 1 | 5,3 GB – 5,3 GB | T5: `Abiray/gemma-4-E4B-it-heretic-GGUF` ['gemma-4-E4B-it-heretic-Q4_K_M.gguf'] (5,3 GB) | Apache-2.0 |
| 16 | **[trohrbaugh/Qwen3.5-9B-heretic-v2](https://huggingface.co/trohrbaugh/Qwen3.5-9B-heretic-v2)** | `Qwen/Qwen3.5-9B` (2026-02-27) | 9,4–9,65B; VL | ~3,0 | **~2,3** | **~4%** | × 0,781 (M: NatInt 30,98→24,2) | Heretic v2 (trohrbaugh) | 9,5 | 7,5 | NatInt 30,98→24,2 (−6,8); huihui-változat: 19,8 (−11,2) | 2 | 5,6 GB – 9,5 GB | T5: `filvyb/Qwen3.5-9B-heretic-v2-GGUF` ['Qwen3.5-9B-heretic-v2-Q4_K_M.gguf'] (5,6 GB) | Apache-2.0 |
| 17 | **[MuXodious/gpt-oss-20b-RichardErkhov-heresy](https://huggingface.co/MuXodious/gpt-oss-20b-RichardErkhov-heresy)** | `openai/gpt-oss-20b` (2025-08-04) | 20,9B MoE… | ~2,5 | **~2,1** | **~4%** | × 0,829 (M: NatInt 27,18→22,52) | Heretic (MuXodious / p-e-w ARA) | 9,5 | 5 | UGI 46,67; NatInt 27,18→22,52 (−4,7) | 1 | 12,7 GB – 12,7 GB | T4: `MuXodious/gpt-oss-20b-RichardErkhov-heresy-GGUF` ['gpt-oss-20B-RichardErkhov-heresy-MXFP4_MoE.gguf'] (12,7 GB) | Apache-2.0 |
| 18 | **[p-e-w/Qwen3.5-4B-heretic-2.0](https://huggingface.co/p-e-w/Qwen3.5-4B-heretic-2.0)** | `Qwen/Qwen3.5-4B` (2026-02-27) | 4,5–4,66B; VL | ~2,0 | **~1,9** | **~3%** | × 0,936 (M: NatInt 23,88→22,35 (SOMPOA-változat)) | Heretic 2,0 (p-e-w) / SOMPOA (MuXodious) | 9,5 | 6,5 | SOMPOA: UGI 44,73; NatInt 23,88→22,35 (−1,5) | 4 | 2,5 GB – 4,5 GB | T5: `mradermacher/Qwen3.5-4B-heretic-2.0-GGUF` ['Qwen3.5-4B-heretic-2.0.Q8_0.gguf'] (4,5 GB) | Apache-2.0 |
| 19 | **[llmfan46/gemma-4-E2B-it-ultra-uncensored-heretic-GGUF](https://huggingface.co/llmfan46/gemma-4-E2B-it-ultra-uncensored-heretic-GGUF)** | `google/gemma-4-E2B-it` (2026-03-02) | 5,1B összesen (kb. 2B effektív) | ~1,5 | **~1,4** | **~2%** | × 0,93 (B: heretic, nagyon kis modell) | Heretic, ultra (llmfan46) | 9 | 6,5 | nincs mérés | 2 | 3,4 GB – 3,6 GB | T5: `llmfan46/gemma-4-E2B-it-ultra-uncensored-heretic-GGUF` ['gemma-4-E2B-it-ultra-uncensored-heretic-Q5_K_M.gguf'] (3,6 GB) | Apache-2.0 |

**Hogyan olvasd:**
- **Okosság:** az 1–2. helyhez ≥256 GB memória (T2) kell; a 3–4. hely már 128 GB RAM-os gamer PC-n is fut.
- **Gamer PC:** a legjobb választás a Qwen3.8-Flash-Next abliterated v2 (94–111 GB) és a Qwen3.8-27B abliterated (14–29 GB). Egyetlen videokártyán a Qwen3.8-27B abliterated fut.
- **Laptop, telefon:** a Gemma-4-26B-A4B és -E4B heretic mérten veszteség nélküli; a 31B-é mért −6%, a 12B és E2B becsült −7%.
- **Arete-27B:** nem általános cenzúramentesítés, csak a propaganda-keretezést távolítja el.
- **Kimi K3.1 Pro-ból nincs cenzúrázatlan változat.** A Kimi-K3 abliterated régebbi és gyengébb alapra épül (AA 17,4), a minősége nem ellenőrzött.

#### Gépigény: cenzúrázatlan modellek

A számok **becslések** az alábbi szabályokkal:
- **Memória:** fájlméret × 1,15 (KV cache ~16–32k kontextusig, futtatói overhead).
- **Hibrid MoE:** a figyelmi rétegek és a KV cache a videokártyán, a szakértők a RAM-ban (`--n-cpu-moe`).
- **Sebesség (generálás, 1 felhasználó):** tokenenként az aktív paraméterek bájtjait kell beolvasni. Képlet: tok/s ≈ 1 / (aktív bájt / (0,6 × sávszélesség) + fix többletidő). A többletidő GPU-n 5–6 ms, Macen 9, CPU-n 12, telefonon 25 ms.
- **Sávszélességek:** RTX 4090 1008 GB/s, RTX 5090 1792, M3 Ultra 819, EPYC 12 csatornás DDR5 460, otthoni PC DDR5 kétcsatornás 90, telefon LPDDR5X 70.
- **Mért adat:** nincs, ezek számolt értékek. A valós érték prompt-feldolgozáskor és hosszú kontextusnál alacsonyabb, MTP/speculative decodinggal magasabb lehet.
- **Mac:** a macOS alapból a unified memória kb. 75%-át adja a GPU-nak. Ez emelhető: `sudo sysctl iogpu.wired_limit_mb=<MB>`.

| # | Modell | Ajánlott GGUF-kvant (méret) | Archit. (aktív) | Csak GPU | Hibrid MoE (GPU+RAM) | Mac | Csak CPU | tok/s GPU | tok/s hibrid (DDR5 PC) | tok/s M3 Ultra | tok/s EPYC | tok/s telefon | Legkisebb kvant → min. memória | Egyéb formátum |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **DeepSeek-V4.1-Flash-1017 abliterated** | `UD-IQ1_S/*` 233,0 GB (1,7 bit) | MoE, 16B aktív | 268 GB VRAM (pl. 4×80 GB) | 32 GB VRAM + 244 GB RAM | 281 GB unified | 276 GB RAM | – | ~21 | ~63 | ~41 | – | `UD-IQ1_S/*` 233,0 GB → 268 GB | MLX: 422,6 GB (4,5 bit); szerver (vLLM/SGLang): 510,3 GB (8,5 bit) |
| 2 | **GLM-5.3 abliterated** | `UD-IQ1_S/*` 216,7 GB (1,7 bit) | MoE, 40B aktív | 249 GB VRAM (pl. 4×80 GB) | 32 GB VRAM + 225 GB RAM | 262 GB unified | 257 GB RAM | – | ~9 | ~38 | ~23 | – | `UD-IQ1_S/*` 216,7 GB → 249 GB | – |
| 3 | **MiniMax-M3.1-Flash abliterated** | `Mix-128G/*` 111,9 GB (4,5 bit) | MoE, 23B aktív | 129 GB VRAM (pl. 2×80 GB) | 19 GB VRAM + 117 GB RAM | 135 GB unified | 137 GB RAM | – | ~6 | ~28 | ~17 | – | `Mix-128G/*` 111,9 GB → 129 GB | – |
| 4 | **Qwen3.8-Flash-Next abliterated v2** | `unsloth-UD-Q4_K_XL/*` 111,3 GB (4,5 bit) | MoE, 6B aktív | 128 GB VRAM (pl. 2×80 GB) | 19 GB VRAM + 117 GB RAM | 134 GB unified | 136 GB RAM | – | ~21 | ~63 | ~41 | – | `swift-IQ2_XS/*` 68,2 GB → 78 GB | MLX: 128,6 GB (5,5 bit) |
| 5 | **GLM-5.3-Flash abliterated** | `UD-Q4_K_XL/*` 199,7 GB (4,5 bit) | MoE, 18B aktív | 230 GB VRAM (pl. 3×80 GB) | 30 GB VRAM + 208 GB RAM | 241 GB unified | 238 GB RAM | – | ~8 | ~34 | ~21 | – | `UD-IQ1_S/*` 93,1 GB → 107 GB | MLX: 185,9 GB (4,5 bit) |
| 6 | **Qwen3.8-27B abliterated** | `Huihui-Qwen3.8-27B-abliterated-UD-DW-Q4_K_M.gguf` 16,6 GB (4,5 bit) | dense, 27,8B aktív | 19 GB VRAM (1 kártya) | dense: nem ajánlott (lassú) | 20 GB unified | 27 GB RAM | ~31 | – | ~24 | ~15 | – | `Huihui-Qwen3.8-27B-abliterated-Q2_K.gguf` 10,9 GB → 12 GB | MLX: 19,8 GB (4,5 bit) |
| 7 | **NousResearch Arete-27B** | `NousResearch_Arete-27B-Q4_K_M.gguf` 17,2 GB (4,5 bit) | dense, 27,4B aktív | 20 GB VRAM (1 kártya) | dense: nem ajánlott (lassú) | 21 GB unified | 28 GB RAM | ~32 | – | ~25 | ~15 | – | `NousResearch_Arete-27B-IQ4_XS.gguf` 15,2 GB → 18 GB | – |
| 8 | **Kimi-K3 Abliterated V1** | `MXFP4_MOE/*` 1,51 TB (4,5 bit) | MoE, 104B aktív | 1735 GB VRAM (pl. 22×80 GB) | 32 GB VRAM + 1711 GB RAM | 1821 GB unified (2× Mac, exo) | 1743 GB RAM | – | ~1,5 | ~5 (2× Mac) | ~4 | – | `MXFP4_MOE/*` 1,51 TB → 1735 GB | – |
| 9 | **Qwen3.6-35B-A3B uncensored-heretic** | `Qwen3.6-35B-A3B-uncensored-heretic-Q4_K_M.gguf` 21,2 GB (4,5 bit) | MoE, 3B aktív | 24 GB VRAM (1 kártya) | 12 GB VRAM + 20 GB RAM | 26 GB unified | 32 GB RAM | ~152 (5090) | ~37 | ~80 | ~55 | – | `Qwen3.6-35B-A3B-uncensored-heretic-Q3_K_M.gguf` 16,9 GB → 19 GB | – |
| 10 | **Mistral-Small-4-119B-2603 heretic** | `Mistral-Small-4-119B-2603-heretic-Q4_K_M.gguf` 72,2 GB (4,5 bit) | MoE, ?B aktív | 83 GB VRAM (pl. 2×80 GB) | 15 GB VRAM + 76 GB RAM | 87 GB unified | 91 GB RAM | – | – | – | – | – | `Mistral-Small-4-119B-2603-heretic-Q2_K.gguf` 43,4 GB → 50 GB | – |
| 11 | **gemma-4-31B-it heretic** | `gemma-4-31B-it-heretic.Q4_K_M.gguf` 18,7 GB (4,5 bit) | dense, 31,3B aktív | 21 GB VRAM (1 kártya) | dense: nem ajánlott (lassú) | 23 GB unified | 29 GB RAM | ~28 | – | ~22 | ~13 | – | `gemma-4-31B-it-heretic.IQ4_XS.gguf` 16,9 GB → 19 GB | MLX: 17,3 GB (4,5 bit) |
| 12 | **gpt-oss-120b heretic** | `kldzj_gpt-oss-120b-heretic-MXFP4_MOE/*` 63,4 GB (4,5 bit) | MoE, 5,1B aktív | 73 GB VRAM (pl. 1×80 GB) | 14 GB VRAM + 67 GB RAM | 77 GB unified | 81 GB RAM | – | ~25 | ~67 | ~45 | – | `gpt-oss-120B-tainted-heresy-MXFP4_MoE.gguf` 63,4 GB → 73 GB | MLX: 62,2 GB (4,5 bit) |
| 13 | **gemma-4-26B-A4B-it ultra-uncensored-heretic** | `gemma-4-26B-A4B-it-ultra-uncensored-heretic-Q4_K_M.gguf` 16,8 GB (4,5 bit) | MoE, 4B aktív | 19 GB VRAM (1 kártya) | 12 GB VRAM + 15 GB RAM | 20 GB unified | 27 GB RAM | ~103 | ~30 | ~74 | ~50 | – | `gemma-4-26B-A4B-it-ultra-uncensored-heretic-Q3_K_M.gguf` 13,3 GB → 15 GB | – |
| 14 | **Qwen3.5-9B heretic-v2** | `Qwen3.5-9B-heretic-v2-Q4_K_M.gguf` 5,6 GB (4,5 bit) | dense, 9,5B aktív | 6 GB VRAM (1 kártya) | dense: nem ajánlott (lassú) | 16 GB unified | 14 GB RAM | ~67 | – | ~50 | ~32 | ~7 | `Qwen3.5-9B-heretic-v2-Q4_K_M.gguf` 5,6 GB → 6 GB | – |
| 15 | **gemma-4-12B-it uncensored-heretic** | `gemma-4-12B-it-uncensored-heretic-Q4_K_M.gguf` 8,5 GB (4,5 bit) | dense, 12B aktív | 10 GB VRAM (1 kártya) | dense: nem ajánlott (lassú) | 16 GB unified | 18 GB RAM | ~58 | – | ~44 | ~27 | ~5 | `gemma-4-12B-it-uncensored-heretic-Q4_K_M.gguf` 8,5 GB → 10 GB | – |
| 16 | **gpt-oss-20b heretic** | `gpt-oss-20B-RichardErkhov-heresy-MXFP4_MoE.gguf` 12,7 GB (4,5 bit) | MoE, 3,6B aktív | 15 GB VRAM (1 kártya) | 12 GB VRAM + 11 GB RAM | 16 GB unified | 23 GB RAM | ~107 | ~32 | ~76 | ~52 | – | `gpt-oss-20B-RichardErkhov-heresy-MXFP4_MoE.gguf` 12,7 GB → 15 GB | – |
| 17 | **gemma-4-E4B-it heretic** | `gemma-4-E4B-it-heretic-Q4_K_M.gguf` 5,3 GB (4,5 bit) | dense, 4,5B aktív | 6 GB VRAM (1 kártya) | dense: nem ajánlott (lassú) | 16 GB unified | 14 GB RAM | ~98 | – | ~71 | ~47 | ~12 | `gemma-4-E4B-it-heretic-Q4_K_M.gguf` 5,3 GB → 6 GB | – |
| 18 | **Qwen3.5-4B heretic-2.0** | `Qwen3.5-4B-heretic-2.0.Q4_K_M.gguf` 2,7 GB (4,5 bit) | dense, 4,6B aktív | 3 GB VRAM (1 kártya) | dense: nem ajánlott (lassú) | 16 GB unified | 11 GB RAM | ~97 | – | ~70 | ~47 | ~12 | `Qwen3.5-4B-heretic-2.0.IQ4_XS.gguf` 2,5 GB → 3 GB | – |
| 19 | **gemma-4-E2B-it ultra-uncensored-heretic** | `gemma-4-E2B-it-ultra-uncensored-heretic-Q4_K_M.gguf` 3,4 GB (4,5 bit) | dense, 2B aktív | 4 GB VRAM (1 kártya) | dense: nem ajánlott (lassú) | 16 GB unified | 12 GB RAM | ~127 | – | ~89 | ~62 | ~19 | `gemma-4-E2B-it-ultra-uncensored-heretic-Q4_K_M.gguf` 3,4 GB → 4 GB | – |

### 6.10 Eszköz-kalkulátor: mi a legokosabb, ami elfér és elfut (4 változat)

A `llm_calc.py` (**12. fejezet**) bármely eszközre kiszámolja a négy változatot:
- **V1:** a legokosabb **cenzúrázatlan** modell, ami épp elfér és elfut.
- **V2:** a legokosabb **alap (cenzúrázott)** modell, ami épp elfér és elfut.
- **V3 – csapat alap modellekből:** egy nagy fő modell és egy kicsi, gyors segéd egyszerre a memóriában. A segéd routerként, gyors válaszolóként vagy draftként dolgozik. Mellettük egy RAG-embedding is fut (bge-m3).
- **V4 – vegyes csapat:** egy alap és egy cenzúrázatlan modell együtt. Ha még befér, egy gyors segéd és a RAG-embedding is.

**Ha két modell nem fér el egyszerre** (például telefonon), a kalkulátor *váltott csapatot* ad: a tárhelyen mindkét modell ott van, és mindig az éppen szükséges töltődik be (néhány másodperc).

**Becslés, nem mérés:**
- **Memória:** fájl × 1,15 + 1 GB.
- **Sebesség:** a memória-sávszélességből és az aktív paraméterszámból (lásd 6.5).
- **„Okosság”:** az AA v5 index × a kvantminőség szorzója. A dense modelleket 2,5 bit alatt kizárja.
- **Döntés:** a legokosabb modell nyer, kis sebesség-bónusszal (legfeljebb +20%).
- **„Elfut”:** legalább 5 tok/s (telefonon és régi laptopon 4).
- **Közel azonos alternatíva:** a legjobb pontszám ≥95%-a, más modellcsaládból.

### 6.10b Mi fut a gépeiden – a 4 változat tömören

> V1 = legokosabb cenzúrázatlan · V2 = legokosabb alap · V3 = alap csapat · V4 = alap + cenzúrázatlan csapat. % = az AA v5 pont az Opus 5.5-höz (59,1) képest. Becslés, nem mérés.

| Eszköz | V1 | V2 | V3 | V4 |
|---|---|---|---|---|
| **Samsung Galaxy S24 Ultra (12 GB, Snapdragon 8 Gen 3)** | gemma-4-E4B-it-heretic-GGUF (~4%, ~11 tok/s) | Qwen3.5-4B-GGUF (~5%, ~7 tok/s) | Qwen3.5-4B-GGUF (~5%, ~7 tok/s)<br>gemma-4-E2B-it-GGUF (~3%, ~19 tok/s) | Qwen3.5-4B-GGUF (~5%, ~7 tok/s)<br>gemma-4-E4B-it-heretic-GGUF (~4%, ~11 tok/s) |
| **iPhone 15 Pro (8 GB, A17 Pro)** | Qwen3.5-4B-heretic-2.0-GGUF (~3%, ~9 tok/s) | Qwen3.5-4B-GGUF (~3%, ~9 tok/s) | Qwen3.5-4B-GGUF (~3%, ~9 tok/s)<br>gemma-4-E2B-it-GGUF (~3%, ~16 tok/s) | Qwen3.5-4B-GGUF (~3%, ~9 tok/s)<br>Qwen3.5-4B-heretic-2.0-GGUF (~3%, ~9 tok/s) |
| **HP Pavilion 15-bc504ur (16 GB DDR4 dual channel, GTX 1050 4 GB)** | gemma-4-E4B-it-heretic-GGUF (~4%, ~10 tok/s) | gemma-4-26B-A4B-it-GGUF (~6%, ~15 tok/s) | gemma-4-12B-it-qat-q4_0-gguf (~5%, ~4 tok/s)<br>Qwen3.5-4B-GGUF (~3%, ~11 tok/s) | Qwen3.5-4B-GGUF (~5%, ~6 tok/s)<br>gemma-4-E4B-it-heretic-GGUF (~4%, ~9 tok/s) |
| **HP ZBook Ultra G3a (192 GB unified, Ryzen AI Max+ PRO 495)** | Huihui-Qwen3.8-Flash-Next-abliterated-v2… (~46%, ~31 tok/s) | Qwen3.8-Flash-Next-i1-GGUF (48%, ~27 tok/s) | Qwen3.8-Flash-Next-i1-GGUF (48%, ~31 tok/s)<br>NVIDIA-Nemotron-3.5-Lightning-30B-A3B-GGUF (9%, ~48 tok/s) | Qwen3.8-Flash-Next-i1-GGUF (48%, ~31 tok/s)<br>NousResearch_Arete-27B-GGUF (~32%, ~9 tok/s)<br>Qwen3.6-35B-A3B-uncensored-heretic-GGUF (~14%, ~48 tok/s) |
| **2× MS-S1 MAX-P495 (2×192 GB, USB4 v2 80 Gbps)** | Huihui-Qwen3.8-Flash-Next-abliterated-v2… (~46%, ~26 tok/s) | Qwen3.8-Flash-Next-i1-GGUF (48%, ~28 tok/s) | Qwen3.8-Flash-Next-i1-GGUF (48%, ~28 tok/s)<br>NVIDIA-Nemotron-3.5-Lightning-30B-A3B-GGUF (9%, ~49 tok/s) | Qwen3.8-Flash-Next-i1-GGUF (48%, ~28 tok/s)<br>MiniMax-M3.1-Flash-abliterated-GGUF (~46%, ~11 tok/s)<br>Qwen3.6-35B-A3B-uncensored-heretic-GGUF (~14%, ~49 tok/s) |
| **Gamer PC – RTX 6090 32 GB + 128 GB DDR5** | Huihui-Qwen3.8-Flash-Next-abliterated-v2… (~46%, ~27 tok/s) | Qwen3.8-Flash-Next-GGUF (48%, ~27 tok/s) | Qwen3.8-Flash-Next-GGUF (48%, ~27 tok/s)<br>NVIDIA-Nemotron-3.5-Lightning-30B-A3B-GGUF (9%, ~35 tok/s) | Qwen3.8-27B-i1-GGUF (34%, ~42 tok/s)<br>Huihui-Qwen3.8-Flash-Next-abliterated-v2… (~46%, ~22 tok/s) |
| **Gamer PC – RTX 6090 32 GB + köv. gen. RTX Pro 128 GB (B: valószínű) + 256 GB DDR5** | Huihui-Qwen3.8-Flash-Next-abliterated-v2… (~46%, ~56 tok/s) | Qwen3.8-Flash-Next-i1-GGUF (48%, ~98 tok/s) | Qwen3.8-Flash-Next-i1-GGUF (48%, ~98 tok/s)<br>gemma-4-E2B-it-GGUF (~3%, ~127 tok/s) | Qwen3.8-Flash-Next-i1-GGUF (48%, ~98 tok/s)<br>MiniMax-M3.1-Flash-abliterated-GGUF (~46%, ~5 tok/s) |
| **Linux szerver – EPYC 12 csatornás DDR5 768 GB + 1× RTX 6090 32 GB** | DeepSeek-V4.1-Flash-1017-heretic-GGUF (~53%, ~18 tok/s) | DeepSeek-V4.1-Flash-1017-GGUF (55%, ~18 tok/s) | Hy4-preview-GGUF (~59%, ~12 tok/s)<br>Qwen3.8-27B-GGUF (34%, ~15 tok/s) | DeepSeek-V4.1-Flash-1017-GGUF (55%, ~18 tok/s)<br>Huihui-Qwen3.8-Flash-Next-abliterated-v2… (~46%, ~49 tok/s)<br>Qwen3.6-35B-A3B-uncensored-heretic-GGUF (~14%, ~71 tok/s) |

### 6.11 GeForce-korlátozások és feloldásuk – a lényeg

**A lényeg:**
1. **Decode (egy felhasználó, szöveggenerálás):** a memória-sávszélesség korlátozza, nem a letiltott számítási teljesítmény. Erre egyik feloldás sem ad sokat:
   - memória-túlhajtás: **+5–10%** [B];
   - P2P két kártyánál: **~+3%** (mért: 2× RTX 5090, vLLM TP=2, átlag +2,7%).
2. **FP16/BF16 FP32-akkumulálás felezésének feloldása:** **2026 szeptember–októberétől létezik.**
   - RTX 30: stabil.
   - RTX 40: kísérleti.
   - **RTX 50 (Blackwell): nem működik**, a fejlesztő szerint „unlikely to happen”.
   - Ezért az **RTX 6090-re (Rubin) ezzel ne számolj**.
   - Ahol működik, ott a prompt-feldolgozás (prefill) és a finomhangolás gyorsul: +25–55%.
3. **P2P feloldás:** RTX 30/40/50-en működik, **RTX 5090 ↔ RTX PRO 6000 Blackwell között is**. Ez a legvalószínűbben átvihető feloldás az RTX 6090 + következő RTX Pro párosra [B]. Két kártyánál kicsi a nyereség, 4–8 kártyánál nagyobb (all-reduce sávszélesség +42%, késleltetés 11,7 → 1,2 µs).
4. **A tényleges szűk keresztmetszet a VRAM mérete.** Szoftveresen nem bővíthető. Hardvermod létezik (48 GB-os RTX 4090), RTX 6090-re nincs.
5. **A két kártya párhuzamos futtatása (tensor parallel) nem feloldás, hanem szoftverbeállítás.**
   - vLLM TP vagy llama.cpp `-sm row`.
   - P2P nélkül is működik (~80% hatásfok [B]); a P2P ehhez ad ~+3%-ot.
   - A kalkulátor alap profiljai rétegenkénti felosztással számolnak (llama.cpp alapbeállítás). A „FELOLDVA” profilok TP + P2P + memória-túlhajtás együttesével.

## 9. Captcha-mentes webes keresés és letöltés

### 9.1 Lépcsőzetes stratégia: mindig a legolcsóbb működő réteggel kezdj

1. **Diagnózis:**
   - Ha nincs `cf-mitigated: challenge` header, a gond a TLS-ujjlenyomat: **curl_cffi** `impersonate="chrome"`.
   - Ha van challenge ("Just a moment…"), böngésző kell: **Camoufox** vagy **Patchright**.
   - Ha minden 403, az IP a gond: residential proxy kell.
2. Sok fájl ugyanarról a védett oldalról: **Byparr / FlareSolverr** (Docker, csak 127.0.0.1-re kötve) ad egy cookie-t és User-Agentet, ezekkel a curl_cffi tölt le. A cookie UA-hoz és IP-hez kötött.
3. **Keresés:**
   - saját **SearXNG** példány (JSON API) vagy **ddgs** (kulcs nélküli);
   - megbízhatóbb, fizetős: **Brave Search API**, **Serper**, **Exa**, **Tavily**.
   - A Bing Search API 2025-08-ban megszűnt, a Google Custom Search új ügyfélnek zárva van.
4. **Megkerülés előtt alternatív forrás:**
   - hivatalos tükör, kiadói repó, archive.org;
   - `web.archive.org/web/2id_/<URL>`: az `id_` utótag a nyers eredeti fájlt adja.
5. Csak végső esetben: felhős unblocker (Zyte, Bright Data, ZenRows, Scrapfly) vagy CAPTCHA-feloldó. Ez pénzbe kerül, harmadik fél látja az URL-eket, és ÁSZF-kockázatot jelent.
6. **Udvariasság:**
   - domainenként 1–2 kapcsolat, 2–10 s véletlen szünet;
   - 429 / `Retry-After` esetén backoff;
   - ugyanazt ne töltsd le kétszer;
   - naplózd a forrást, a dátumot, a SHA-256-ot és a licencet.
7. **Elavult, modern Cloudflare ellen nem működik:** cloudscraper, puppeteer-extra-plugin-stealth, undetected-chromedriver, playwright-stealth, hrequests.
8. **MITM (TLS-t bontó) vállalati proxy mögött** a TLS-utánzás hatástalan. Ilyenkor böngésző vagy másik hálózat kell.
