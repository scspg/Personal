# ARCHIVUM – Offline tudásarchívum blackout és összeomlás esetére

> **Verzió:** 2026-11-14 · **Elemek:** 100 (96 mért méretű) · **Minden ellenőrizhető méretet mértem** (Kiwix OPDS, HTTP Content-Length, Hugging Face API, Ollama registry). A státuszt minden elem `size_status` / `url_status` mezője mutatja.
> **Cél:** ezt az egy fájlt egy eszközhasználó AI-ágensnek (Claude Code, Codex, Open Interpreter, aider stb.) beadva az ágens kiválasztja a tárhelyhez illő csomagot, és letölti, ellenőrzi és rendszerezi.

## Tartalom
0. [Gyorsindítás embernek](#0-gyorsindítás-embernek)
1. [AGENT PROMPT – ezt másold be az AI-nak](#1-agent-prompt)
2. [Szabályok és buktatók – mire figyeljen az AI](#2-szabályok-és-buktatók)
3. [Pontozási rendszer](#3-pontozási-rendszer)
4. [Előre számolt csomagok tárhely szerint](#4-előre-számolt-csomagok)
5. [Katalógus kategóriánként (emberi nézet)](#5-katalógus-kategóriánként)
6. [NAGY FEJEZET: helyi, nyílt súlyú LLM-ek](#6-helyi-llm-ek)
7. [Letöltési receptek módszerenként](#7-letöltési-receptek)
8. [Fizetős, regisztrációs és fizikai beszerzések](#8-fizetős-regisztrációs-és-fizikai-beszerzések)
9. [Gépi katalógus (JSONL) – a szkript ezt olvassa](#9-gépi-katalógus)
10. [select_items.py – kiválasztó és letöltő-generátor](#10-select_itemspy)

---

## 0. Gyorsindítás embernek

1. Szerezz egy meghajtót. Ajánlott: **exFAT** (Windows/Mac/Linux mind olvassa) vagy **ext4** (csak Linux). **FAT32-t ne használj**, mert nem kezel 4 GB-nál nagyobb fájlt, a Wikipedia ZIM pedig 127 GB.
2. Add ezt a fájlt egy olyan AI-ágensnek, amely parancsot tud futtatni. Írd mellé például ezt: *„Van egy 1 TB-os meghajtóm a /media/usb alatt, RTX 4090 + 128 GB RAM gépem, magyar és angol anyag kell, főleg orvosi és mezőgazdasági. Csináld meg.”*
3. Ha kézzel csinálnád:
   ```bash
   # a 9. és 10. fejezet blokkjai alapján a szkript magát az .md fájlt is tudja olvasni:
   sed -n '/^```python select_items.py$/,/^```$/p' ARCHIVUM.md | sed '1d;$d' > select_items.py
   python3 select_items.py ARCHIVUM.md --budget 1TB --profile balanced --langs hu,en,multi --hw T3 --emit-sh dl.sh
   less dl.sh && DEST=/media/usb/archivum bash dl.sh
   ```
4. **Fontos:**
   - Két példány legyen, két külön helyen.
   - A 0. szint (orvoslás, víz) **legyen kinyomtatva** is.
   - Az olvasóprogramok telepítői (Kiwix, VLC, PDF-olvasó, llama.cpp) is kerüljenek fel a meghajtóra (a `tool-*` elemek).


---

## 1. AGENT PROMPT

> Másold be a teljes blokkot az AI-ágensnek, a `<<…>>` részeket töltsd ki. Ha valamit üresen hagysz, az ágens rákérdez.

```text
SZEREP: Offline-archívum építő ágens vagy. A mellékelt ARCHIVUM.md katalógus alapján letöltöd,
ellenőrzöd és rendszerezed a tudásanyagot egy meghajtóra, a felhasználó kereteihez igazítva.

FELHASZNÁLÓI KERETEK (töltsd ki / kérdezz rá, ha hiányzik):
- Cél meghajtó / könyvtár: <<pl. /media/usb/archivum>>
- Tárhely-keret: <<pl. 512GB>>  (ha nincs megadva: mérd meg `df -B1`-gyel, és a szabad hely 92%-át használd)
- Hardver az LLM-hez: <<T1 szerver | T2 400-1000 GB unified memória | T3 gamer PC 24-32 GB VRAM | T4 laptop | T5 telefon | nincs>>
- Profil: <<balanced | survival | rebuild | education | computing>>
- Fókusz (kategória=szorzó): <<pl. medicine=2,agriculture=1.5,hungarian=1.5>>
- Nyelvek: <<hu,en,multi>>
- Hozzáférés: <<free,free-registration,donation>>  (+paid ha vásárolni is hajlandó, +gray csak kifejezett kérésre)
- Kizárások / kötelezők: <<id-k>>

MUNKAMENET:
1. Olvasd be az ARCHIVUM.md 2. (szabályok) és 3. (pontozás) fejezetét. Ezek kötelezők.
2. Bontsd ki a 10. fejezetből a select_items.py-t, és futtasd a kerettel:
   python3 select_items.py ARCHIVUM.md --budget <keret> --profile <p> --langs <l> --access <a> --hw <T> --focus <f> --emit-sh dl.sh --dest <cél>
3. Mutasd meg a tervet az embernek: elemek, összméret, kimaradt fontos elemek, KÉZI TEENDŐK listája.
   Kérj jóváhagyást. Módosíts, ha kéri (--include / --exclude / --focus).
4. Előellenőrzés:
   a) szabad hely (`df -B1 <cél>`) ≥ terv + 5%;
   b) a fájlrendszer NEM FAT32 (`df -T` / `lsblk -f`). Ha az, állj meg és szólj;
   c) eszközök: curl, wget vagy aria2c (ajánlott), sha256sum, git; LLM-hez `hf` (pip install -U huggingface_hub) vagy ollama; archive.org-hoz `ia` (pip install internetarchive).
5. Letöltés PRIORITÁSI SORRENDBEN (tier 0 → 5), hogy egy megszakadt letöltés után is a legfontosabb anyag legyen meg.
   Minden fájl újraindítható legyen (-c / aria2c). Párhuzamosan max. 2-3 nagy letöltés fusson.
6. Minden elem után ellenőrizz:
   - sha256, ha van (.sha256 a Kiwixnél; LFS oid a Hugging Face-nél);
   - méret ±2%;
   - ZIM-nél opcionálisan `zimcheck -A`;
   - PDF-nél `pdfinfo` vagy a fájl első bájtjai (%PDF).
   Hibánál 3 újrapróbálkozás, más tükörszerverről. Utána FAIL a naplóba, és menj tovább.
7. Rendszerezés: <cél>/<kategória>/<id>/... Írj egy <cél>/INDEX.md és <cél>/index.html fájlt
   (id, név, mire jó, hogyan nyitható meg, méret, sha256), plusz egy manifest.json-t.
   Másold a meghajtóra az ARCHIVUM.md-t és a select_items.py-t is.
8. Olvasóprogramok: töltsd le a tool-* elemeket (Kiwix desktop/Android, kiwix-tools, VLC, PDF-olvasó,
   llama.cpp binárisok, Ollama telepítő, Organic Maps APK stb.) a <cél>/_tools alá, Windows/macOS/Linux/Android változatban.
9. Zárójelentés:
   - mi jött le (OK), mi bukott (FAIL), mennyi hely maradt;
   - a KÉZI TEENDŐK listája linkkel és árral (fizetős, regisztrációs, fizikai könyv);
   - a következő frissítés ajánlott ideje.

TILOS:
- a keretet túllépni;
- gray (kalóz) forrást letölteni, ha az ember külön nem kérte;
- regisztrációt vagy vásárlást az ember helyett elvégezni;
- letöltött szkriptet vagy telepítőt ellenőrzés nélkül futtatni;
- meglévő fájlt törölni a célkönyvtárban jóváhagyás nélkül.
KÉTSÉG ESETÉN: kérdezz röviden, és addig haladj a biztos elemekkel.
```


---

## 2. Szabályok és buktatók

| # | Buktató | Mit csináljon az AI |
|---|---|---|
| 1 | **FAT32: legfeljebb 4 GB-os fájl** | exFAT vagy ext4 kell. NTFS is jó Windowson, de Macen csak olvasható. |
| 2 | **GB és GiB** | A katalógus decimális GB-ot használ (10⁹), mint a meghajtók címkéje. A `df -h` GiB-ot mutat: 1 TB ≈ 931 GiB. |
| 3 | **Változó fájlnevek** | A Kiwix havonta új snapshotot ad ki (`…_ÉÉÉÉ-HH.zim`). Mindig az OPDS-katalógusból kell feloldani (`kiwix_latest()` a szkriptben). A katalógusban szereplő URL csak tartalék. |
| 4 | **A méret is változik** | A mért méret 2026-11-14-i. ±10% eltérés normális. Ha egy elem 25%-nál többet nőtt, jelezd. |
| 5 | **Tükörszerverek** | A `lb.download.kiwix.org` automatikusan tükörre irányít. Lassúság vagy hiba esetén jobb a `.torrent` / `.meta4` (aria2c). Hugging Face-nél a `hf download` folytatja a megszakított letöltést. |
| 6 | **Daraboló GGUF-ok** | A nagy modellek `-00001-of-0000N.gguf` darabokban jönnek. Mind kell. A llama.cpp az első darabbal elindul, összefűzni nem kell. Csak a régi eszközök igénylik a `llama-gguf-split --merge`-et. |
| 7 | **Gated modellek** | Llama, Gemma és egyes Mistral modellekhez HF-fiók, licencelfogadás és token kell (`hf auth login`). Ez kézi teendő. |
| 8 | **Licenc és jog** | A `gray` elemek (Anna's Archive, LibGen, Sci-Hub) letöltése és megosztása Magyarországon és az EU-ban szerzői jogi jogsértés lehet. Alapból ki vannak zárva, csak kifejezett kérésre. |
| 9 | **Rate limit / robots** | `wget-mirror` esetén `--wait=1`. Archive.org-on maximum néhány párhuzamos kapcsolat. Fiók nélkül ne kérj túl sokat egyszerre. |
| 10 | **Letöltött kód futtatása** | Telepítőt és szkriptet csak hivatalos forrásból és ellenőrzött checksummal futtass. Ellenőrizetlen bináris ne fusson. |
| 11 | **Áramellátás** | Egy archívum annyit ér, amennyi az olvasóeszköz. Kell egy alacsony fogyasztású gép (Raspberry Pi 5 kb. 5–10 W, laptop, Android) és napelem. Az elektronika tönkremehet, ezért kell a papír is. |
| 12 | **Redundancia** | 3-2-1 elv: 3 példány, 2 különböző adathordozón, 1 máshol tárolva. HDD-t évente meg kell járatni. Hosszú távra M-DISC vagy szalag. Az SSD áram nélkül 1–3 évig tartja megbízhatóan az adatot (gyártófüggő, **becsült**). |
| 13 | **Nem minden eljárásleírás** | A Wikipedia leír, de nem tanít meg. A tier 0–2 gyakorlati anyagok (CD3WD, FAS, Hesperian, NAVEDTRA, Survivor Library) adják a „hogyan”-t, ezeket nem szabad a lexikon miatt kihagyni. |
| 14 | **Az LLM hallucinál** | Az offline LLM keresésre, magyarázatra és fordításra jó. Orvosi, vegyi és szerkezeti kérdésben **mindig a forrásdokumentum dönt**. Ha lehet, RAG kell a ZIM/PDF anyagra. |
| 15 | **Frissítés** | Évente egyszer érdemes újragenerálni: ugyanezzel a szkripttel, az új snapshotok az OPDS-ből jönnek. |


---

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

**Kiválasztási algoritmus** (`select_items.py`):
1. Szűrés nyelvre, hozzáférésre, hardverszintre és kizárásokra.
2. Tierenként haladva: először minden csoport (pl. `wp-en` = Wikipedia-változatok) **legkisebb** változata kerül be. Utána feljavít az **ajánlott** (`pref`) változatig. Csak ezután jön a következő tier.
3. Ha marad hely, **luxus-feljavítás**, pl. képes Wikipedia.
4. Átfedések kiszűrése (`subsumed_by`): például a Wikipedia orvosi részhalmaza kiesik, ha a teljes Wikipedia bent van. A felszabadult hely újratöltődik.
5. Az LLM-súlyok alapból legfeljebb a keret **35%-át** foglalhatják (`--llm-max`).
6. Tartalék: a keret 8%-a (`--reserve`).


---

## 4. Előre számolt csomagok

`select_items.py --budget <X> --hw <T>`, `balanced` profil, nyelv: hu, en, multi, hozzáférés: free, free-registration, donation. Ez csak tájékoztató, a pontos tervet az ágens futtatja a saját keretével.

| Keret | Tipikus eszköz | LLM-szint | Elemek | Felhasznált | LLM | 4 legnagyobb tartalmi elem |
|---|---|---|---|---|---|---|
| **32GB** | pendrive / telefon | – | 29 | 29.42 GB | – | kx-wp-en-top-maxi, kx-wp-hu-nopic, kx-ifixit, kx-mdwiki |
| **128GB** | telefon + kis SSD | T5 | 59 | 117.59 GB | – | kx-wp-en-nopic, kx-wp-hu-maxi, kx-wikibooks-en, kx-se-electronics |
| **512GB** | laptop SSD | T4 | 74 | 460.43 GB | – | kx-khan, kx-stackoverflow, kx-wp-en-nopic, kx-wiktionary-en |
| **1TB** | gamer PC | T3 | 77 | 907.13 GB | – | kx-gutenberg-mul, kx-khan, kx-wp-en-maxi, kx-stackoverflow |
| **2TB** | gamer PC + nagy SSD | T3 | 77 | 907.13 GB | – | kx-gutenberg-mul, kx-khan, kx-wp-en-maxi, kx-stackoverflow |
| **4TB** | AI workstation | T2 | 77 | 907.13 GB | – | kx-gutenberg-mul, kx-khan, kx-wp-en-maxi, kx-stackoverflow |
| **8TB** | workstation + HDD | T2 | 77 | 907.13 GB | – | kx-gutenberg-mul, kx-khan, kx-wp-en-maxi, kx-stackoverflow |
| **20TB** | szerver / NAS | T1 | 77 | 907.13 GB | – | kx-gutenberg-mul, kx-khan, kx-wp-en-maxi, kx-stackoverflow |


---

## 5. Katalógus kategóriánként

> Pont = `balanced` összpontszám (0–10). T = tier. Méret: **M** = mért, **H** = hivatalos, **B** = becsült. A teljes adat (letöltési mód, licenc, megjegyzések) a 9. fejezet JSONL-jében van.


### Olvasók, futtatók (kötelező) (`tools`) – 6 elem

| T | Pont | id | Mi ez, mire jó | Méret | Hozzáférés | Link |
|---|---|---|---|---|---|---|
| 0 | 8.8 | `tool-kiwix` | **Kiwix olvasók (Desktop Win/Linux, Android APK, kiwix-tools szerver x86_64+ARM64)** – A ZIM-fájlok olvasója. A kiwix-serve egy Raspberry Pi-ről a teljes helyi hálózatnak kiszolgálja az archívumot böngészőn át. | 603.73 MB M | free | [link](https://kiwix.org/en/applications/) |
| 0 | 5.8 | `tool-vlc` | **VLC médialejátszó (Win64, macOS, forrás)** – Videók és hangfájlok lejátszása (videós ZIM-ek, oktatóvideók, LibriVox). | ~200 MB B | free | [link](https://www.videolan.org/vlc/) |
| 1 | 6.15 | `tool-fdroid-repo-apks` | **Android alapalkalmazások (F-Droid): F-Droid, VLC, Organic Maps, KOReader** – Android telefonra/tabletre offline telepíthető APK-k: térkép, e-könyv olvasó, médialejátszó. | ~300 MB B | free | [link](https://f-droid.org/) |
| 1 | 5.1 | `tool-sumatra` | **SumatraPDF (Windows, hordozható)** – Kis, gyors PDF/EPUB/DjVu olvasó Windowsra, telepítés nélkül. | ~20 MB B | free | [link](https://www.sumatrapdfreader.org/download-free-pdf-viewer) |
| 2 | 5.75 | `tool-ollama-installers` | **Ollama telepítők (Windows, macOS, Linux install.sh)** – Egyszerű helyi LLM-futtató. A telepítőket internet nélküli újratelepítéshez mentsd el. | 2.09 GB M | free | [link](https://ollama.com/download) |
| 2 | 4.5 | `tool-calibre` | **Calibre e-könyv kezelő** – E-könyv-könyvtár kezelése, konvertálás (EPUB/MOBI/PDF), keresés nagy gyűjteményekben. | ~600 MB (Win+Mac+Linux) B | free | [link](https://calibre-ebook.com/download) |

### Megfelelő technológia (`appropriate_tech`) – 4 elem

| T | Pont | id | Mi ez, mire jó | Méret | Hozzáférés | Link |
|---|---|---|---|---|---|---|
| 0 | 7.95 | `kx-cd3wd` | **cd3wdproject.org_en_all_2026-11** – CD3WD: fejlődő országoknak készült több ezer technológiai kézikönyv (mezőgazdaság, víz, építés, kisipar, egészség). | 572.64 MB M | free | [link](https://lb.download.kiwix.org/zim/zimit/cd3wdproject.org_en_all_2026-11.zim) |
| 1 | 6.7 | `kx-appropedia` | **appropedia_en_all_maxi_2026-02** – Appropedia: megfelelő technológia, fenntartható építés, víz, energia, egészség. | 581.64 MB M | free | [link](https://lb.download.kiwix.org/zim/other/appropedia_en_all_maxi_2026-02.zim) |
| 2 | 5.9 | `kx-lowtech` | **solar.lowtechmagazine.com_mul_all_2025-01** – Low-tech Magazine: áram nélküli és régi technológiák, energiatakarékos megoldások. | 700.56 MB M | free | [link](https://lb.download.kiwix.org/zim/zimit/solar.lowtechmagazine.com_mul_all_2025-01.zim) |
| 3 | 4.15 | `kx-se-sustainability` | **sustainability.stackexchange.com_en_all_2026-10** – Fenntarthatóság Q&A. | 27.69 MB M | free | [link](https://lb.download.kiwix.org/zim/stack_exchange/sustainability.stackexchange.com_en_all_2026-10.zim) |

### Túlélés, katasztrófa (`survival`) – 5 elem

| T | Pont | id | Mi ez, mire jó | Méret | Hozzáférés | Link |
|---|---|---|---|---|---|---|
| 0 | 7.9 | `kx-post-disaster` | **zimgit-post-disaster_en_2024-05** – Katasztrófa utáni kézikönyv-gyűjtemény (menedék, víz, egészség, újjáépítés) – rendezett PDF/HTML anyagok. | 644.67 MB M | free | [link](https://lb.download.kiwix.org/zim/other/zimgit-post-disaster_en_2024-05.zim) |
| 1 | 5.6 | `kx-knots` | **zimgit-knots_en_2024-08** – Csomókötés animált útmutatókkal (kötélmunka, emelés, hajózás). | 27.95 MB M | free | [link](https://lb.download.kiwix.org/zim/other/zimgit-knots_en_2024-08.zim) |
| 2 | 5.85 | `kx-learn-self-reliance` | **lrnselfreliance_en_all_2026-09** – Learn Self Reliance videócsatorna: önellátás, tartósítás, kézművesség (videó). | 3.97 GB M | free | [link](https://lb.download.kiwix.org/zim/videos/lrnselfreliance_en_all_2026-09.zim) |
| 2 | 5.1 | `kx-se-outdoors` | **outdoors.stackexchange.com_en_all_2026-10** – Szabadtéri túlélés, túrázás Q&A. | 141.82 MB M | free | [link](https://lb.download.kiwix.org/zim/stack_exchange/outdoors.stackexchange.com_en_all_2026-10.zim) |
| 3 | 4.65 | `kx-urban-prepper` | **urban-prepper_en_all_2026-08** – Urban Prepper videócsatorna (felkészülés, felszerelés; videó). | 2.25 GB M | free | [link](https://lb.download.kiwix.org/zim/videos/urban-prepper_en_all_2026-08.zim) |

### Orvoslás (`medicine`) – 10 elem

| T | Pont | id | Mi ez, mire jó | Méret | Hozzáférés | Link |
|---|---|---|---|---|---|---|
| 0 | 7.85 | `kx-fas-milmed` | **irp.fas.org_en_military-medicine_2026-10** – US katonai orvosi kézikönyvek (FAS gyűjtés): trauma, sebellátás, terepi sebészet, járványügy. | 64.99 MB M | free | [link](https://lb.download.kiwix.org/zim/zimit/irp.fas.org_en_military-medicine_2026-10.zim) |
| 0 | 7.25 | `kx-mdwiki` | **mdwiki_en_all_maxi_2025-11** – WikiProjectMed orvosi enciklopédia (betegségek, gyógyszerek, eljárások), képekkel; laikus és szakmai szinten is használható. | 2.30 GB M | free | [link](https://lb.download.kiwix.org/zim/other/mdwiki_en_all_maxi_2025-11.zim) |
| 0 | 6.65 | `kx-zimgit-medicine` | **zimgit-medicine_en_2024-08** – Válogatott terepi orvosi kézikönyvek (elsősegély, orvos nélküli ellátás). | 70.18 MB M | free | [link](https://lb.download.kiwix.org/zim/other/zimgit-medicine_en_2024-08.zim) |
| 0 | 6.25 | `kx-wp-en-med` | **wikipedia_en_medicine_maxi_2026-10** – Wikipedia összes orvosi cikke képekkel (önálló, ha nincs teljes WP). | 1.86 GB M | free | [link](https://lb.download.kiwix.org/zim/wikipedia/wikipedia_en_medicine_maxi_2026-10.zim) |
| 0 | 6.25 | `kx-wp-en-med-nopic` | **wikipedia_en_medicine_nopic_2026-10** – Wikipedia orvosi cikkek képek nélkül. | 1.05 GB M | free | [link](https://lb.download.kiwix.org/zim/wikipedia/wikipedia_en_medicine_nopic_2026-10.zim) |
| 0 | 6.0 | `kx-nhs-medicines` | **nhs.uk_en_medicines_2026-09b** – NHS gyógyszer-adatlapok: adagolás, mellékhatás, kölcsönhatás – egyszerű nyelven. | 15.32 MB M | free | [link](https://lb.download.kiwix.org/zim/zimit/nhs.uk_en_medicines_2026-09b.zim) |
| 1 | 7.15 | `kx-lt-med` | **libretexts.org_en_med_2025-01** – LibreTexts orvosi/ápolási egyetemi tankönyvek (anatómia, ápolás, farmakológia). | 1.19 GB M | free | [link](https://lb.download.kiwix.org/zim/libretexts/libretexts.org_en_med_2025-01.zim) |
| 1 | 5.4 | `kx-cdc` | **wwwnc.cdc.gov_en_all_2024-11** – CDC Travel Health: fertőző betegségek, oltások, megelőzés országonként. | 178.33 MB M | free | [link](https://lb.download.kiwix.org/zim/zimit/wwwnc.cdc.gov_en_all_2024-11.zim) |
| 2 | 5.6 | `kx-qg-medicine` | **quickguidesformedicine_en_all_2026-06** – Orvosi gyorsreferencia videók (videólejátszás kell). | 527.71 MB M | free | [link](https://lb.download.kiwix.org/zim/videos/quickguidesformedicine_en_all_2026-06.zim) |
| 2 | 4.75 | `kx-se-medsci` | **medicalsciences.stackexchange.com_en_all_2026-10** – Orvostudomány Q&A. | 60.66 MB M | free | [link](https://lb.download.kiwix.org/zim/stack_exchange/medicalsciences.stackexchange.com_en_all_2026-10.zim) |

### Víz és higiénia (`water_sanitation`) – 1 elem

| T | Pont | id | Mi ez, mire jó | Méret | Hozzáférés | Link |
|---|---|---|---|---|---|---|
| 0 | 7.35 | `kx-water` | **zimgit-water_en_2024-08** – Víztisztítás, kutak, szűrők, fertőtlenítés gyakorlati anyagai. | 20.93 MB M | free | [link](https://lb.download.kiwix.org/zim/other/zimgit-water_en_2024-08.zim) |

### Élelmiszer, tartósítás (`food`) – 3 elem

| T | Pont | id | Mi ez, mire jó | Méret | Hozzáférés | Link |
|---|---|---|---|---|---|---|
| 0 | 6.2 | `kx-food-prep` | **zimgit-food-preparation_en_2025-04** – Élelmiszer-feldolgozás és -tartósítás (szárítás, befőzés, füstölés) útmutatói. | 97.82 MB M | free | [link](https://lb.download.kiwix.org/zim/other/zimgit-food-preparation_en_2025-04.zim) |
| 2 | 5.2 | `kx-se-cooking` | **cooking.stackexchange.com_en_all_2026-10** – Főzés és élelmiszerbiztonság Q&A. | 238.10 MB M | free | [link](https://lb.download.kiwix.org/zim/stack_exchange/cooking.stackexchange.com_en_all_2026-10.zim) |
| 3 | 4.6 | `kx-se-homebrew` | **homebrew.stackexchange.com_en_all_2026-10** – Erjesztés, sörfőzés (fertőtlenítő alkohol, tartósítás) Q&A. | 37.37 MB M | free | [link](https://lb.download.kiwix.org/zim/stack_exchange/homebrew.stackexchange.com_en_all_2026-10.zim) |

### Lexikonok, szótárak (`reference`) – 14 elem

| T | Pont | id | Mi ez, mire jó | Méret | Hozzáférés | Link |
|---|---|---|---|---|---|---|
| 1 | 7.25 | `kx-wp-en-maxi` | **wikipedia_en_all_maxi_2026-08** – Teljes angol Wikipedia képekkel (6,9M+ cikk). A tudásbázis gerince. | 127.42 GB M | free | [link](https://lb.download.kiwix.org/zim/wikipedia/wikipedia_en_all_maxi_2026-08.zim) |
| 1 | 7.25 | `kx-wp-en-nopic` | **wikipedia_en_all_nopic_2026-06** – Teljes angol Wikipedia képek nélkül – legjobb tudás/GB arány. | 52.69 GB M | free | [link](https://lb.download.kiwix.org/zim/wikipedia/wikipedia_en_all_nopic_2026-06.zim) |
| 1 | 6.85 | `kx-wp-en-top1m` | **wikipedia_en_top1m_nopic_2026-04** – A legolvasottabb 1 millió angol cikk, képek nélkül. | 17.13 GB M | free | [link](https://lb.download.kiwix.org/zim/wikipedia/wikipedia_en_top1m_nopic_2026-04.zim) |
| 1 | 6.6 | `kx-wp-hu-maxi` | **wikipedia_hu_all_maxi_2026-06** – Teljes magyar Wikipédia képekkel. | 12.02 GB M | free | [link](https://lb.download.kiwix.org/zim/wikipedia/wikipedia_hu_all_maxi_2026-06.zim) |
| 1 | 6.6 | `kx-wp-hu-nopic` | **wikipedia_hu_all_nopic_2026-10** – Teljes magyar Wikipédia képek nélkül. | 4.25 GB M | free | [link](https://lb.download.kiwix.org/zim/wikipedia/wikipedia_hu_all_nopic_2026-10.zim) |
| 1 | 6.15 | `kx-wp-en-mini` | **wikipedia_en_all_mini_2026-09** – Összes angol cikk, de csak bevezető + infobox. | 14.39 GB M | free | [link](https://lb.download.kiwix.org/zim/wikipedia/wikipedia_en_all_mini_2026-09.zim) |
| 1 | 5.6 | `kx-wp-en-top-maxi` | **wikipedia_en_top_maxi_2026-09** – Top ~50 ezer angol cikk képekkel. | 6.99 GB M | free | [link](https://lb.download.kiwix.org/zim/wikipedia/wikipedia_en_top_maxi_2026-09.zim) |
| 1 | 5.6 | `kx-wp-en-top-nopic` | **wikipedia_en_top_nopic_2026-09** – Top ~50 ezer angol cikk képek nélkül (kis tárhelyre). | 2.75 GB M | free | [link](https://lb.download.kiwix.org/zim/wikipedia/wikipedia_en_top_nopic_2026-09.zim) |
| 1 | 5.5 | `kx-wp-hu-top` | **wikipedia_hu_top_maxi_2026-10** – A legfontosabb magyar cikkek képekkel. | 2.24 GB M | free | [link](https://lb.download.kiwix.org/zim/wikipedia/wikipedia_hu_top_maxi_2026-10.zim) |
| 1 | 5.5 | `kx-wp-hu-mini` | **wikipedia_hu_all_mini_2026-10** – Összes magyar cikk, csak bevezetővel. | 1.16 GB M | free | [link](https://lb.download.kiwix.org/zim/wikipedia/wikipedia_hu_all_mini_2026-10.zim) |
| 2 | 6.35 | `kx-wikibooks-en` | **wikibooks_en_all_maxi_2026-10** – Wikibooks: nyílt tankönyvek és kézikönyvek (kémia, elektronika, programozás, főzés). | 4.74 GB M | free | [link](https://lb.download.kiwix.org/zim/wikibooks/wikibooks_en_all_maxi_2026-10.zim) |
| 3 | 4.45 | `kx-wiktionary-en` | **wiktionary_en_all_nopic_2026-11** – Angol Wiktionary (többnyelvű szótár). | 14.85 GB M | free | [link](https://lb.download.kiwix.org/zim/wiktionary/wiktionary_en_all_nopic_2026-11.zim) |
| 3 | 4.2 | `kx-wp-en-geo` | **wikipedia_en_geography_maxi_2026-10** – Wikipedia földrajz részhalmaz. | 1.23 GB M | free | [link](https://lb.download.kiwix.org/zim/wikipedia/wikipedia_en_geography_maxi_2026-10.zim) |
| 4 | 3.65 | `kx-wikivoyage` | **wikivoyage_en_all_maxi_2026-09** – Wikivoyage: régiók, útvonalak, helyi infó. | 1.07 GB M | free | [link](https://lb.download.kiwix.org/zim/wikivoyage/wikivoyage_en_all_maxi_2026-09.zim) |

### Gyártás, megmunkálás (`manufacturing`) – 3 elem

| T | Pont | id | Mi ez, mire jó | Méret | Hozzáférés | Link |
|---|---|---|---|---|---|---|
| 1 | 7.0 | `kx-lt-workforce` | **libretexts.org_en_workforce_2026-01** – LibreTexts szakképzés: hegesztés, villanyszerelés, HVAC, építőipar, gépészet. | 513.66 MB M | free | [link](https://lb.download.kiwix.org/zim/libretexts/libretexts.org_en_workforce_2026-01.zim) |
| 2 | 5.5 | `kx-se-woodworking` | **woodworking.stackexchange.com_en_all_2026-10** – Famegmunkálás Q&A. | 106.66 MB M | free | [link](https://lb.download.kiwix.org/zim/stack_exchange/woodworking.stackexchange.com_en_all_2026-10.zim) |
| 3 | 4.5 | `kx-se-3dprint` | **3dprinting.stackexchange.com_en_all_2026-10** – 3D-nyomtatás Q&A. | 120.34 MB M | free | [link](https://lb.download.kiwix.org/zim/stack_exchange/3dprinting.stackexchange.com_en_all_2026-10.zim) |

### Javítás (`repair`) – 3 elem

| T | Pont | id | Mi ez, mire jó | Méret | Hozzáférés | Link |
|---|---|---|---|---|---|---|
| 1 | 6.8 | `kx-ifixit` | **ifixit_en_all_2025-12** – iFixit: lépésről lépésre javítási útmutatók eszközökhöz, járművekhez, elektronikához. | 3.57 GB M | free | [link](https://lb.download.kiwix.org/zim/ifixit/ifixit_en_all_2025-12.zim) |
| 2 | 5.95 | `kx-se-mechanics` | **mechanics.stackexchange.com_en_all_2026-10** – Gépjármű-javítás Q&A. | 341.67 MB M | free | [link](https://lb.download.kiwix.org/zim/stack_exchange/mechanics.stackexchange.com_en_all_2026-10.zim) |
| 2 | 5.3 | `kx-se-bicycles` | **bicycles.stackexchange.com_en_all_2026-10** – Kerékpár-javítás Q&A (áram nélküli közlekedés). | 499.26 MB M | free | [link](https://lb.download.kiwix.org/zim/stack_exchange/bicycles.stackexchange.com_en_all_2026-10.zim) |

### Mezőgazdaság (`agriculture`) – 1 elem

| T | Pont | id | Mi ez, mire jó | Méret | Hozzáférés | Link |
|---|---|---|---|---|---|---|
| 1 | 6.6 | `kx-se-gardening` | **gardening.stackexchange.com_en_all_2026-10** – Kertészet, növényvédelem, termesztés Q&A. | 933.10 MB M | free | [link](https://lb.download.kiwix.org/zim/stack_exchange/gardening.stackexchange.com_en_all_2026-10.zim) |

### Építés (`construction`) – 1 elem

| T | Pont | id | Mi ez, mire jó | Méret | Hozzáférés | Link |
|---|---|---|---|---|---|---|
| 1 | 6.55 | `kx-se-diy` | **diy.stackexchange.com_en_all_2026-10** – Házfelújítás, villany-, víz-, fűtésszerelés kérdés-válasz formában. | 2.09 GB M | free | [link](https://lb.download.kiwix.org/zim/stack_exchange/diy.stackexchange.com_en_all_2026-10.zim) |

### Energia (`energy`) – 1 elem

| T | Pont | id | Mi ez, mire jó | Méret | Hozzáférés | Link |
|---|---|---|---|---|---|---|
| 1 | 6.35 | `kx-energypedia` | **energypedia_en_all_maxi_2026-06** – Energypedia: kisléptékű energia (napelem, biogáz, mikro-víz, főzőkályhák). | 799.71 MB M | free | [link](https://lb.download.kiwix.org/zim/other/energypedia_en_all_maxi_2026-06.zim) |

### Mérnöki tudás (`engineering`) – 2 elem

| T | Pont | id | Mi ez, mire jó | Méret | Hozzáférés | Link |
|---|---|---|---|---|---|---|
| 2 | 6.75 | `kx-lt-eng` | **libretexts.org_en_eng_2025-01** – LibreTexts mérnöki tankönyvek (gépész, villamos, építő, anyagtudomány). | 678.39 MB M | free | [link](https://lb.download.kiwix.org/zim/libretexts/libretexts.org_en_eng_2025-01.zim) |
| 2 | 5.45 | `kx-se-engineering` | **engineering.stackexchange.com_en_all_2026-10** – Mérnöki Q&A. | 258.56 MB M | free | [link](https://lb.download.kiwix.org/zim/stack_exchange/engineering.stackexchange.com_en_all_2026-10.zim) |

### Kémia (`chemistry`) – 3 elem

| T | Pont | id | Mi ez, mire jó | Méret | Hozzáférés | Link |
|---|---|---|---|---|---|---|
| 2 | 6.45 | `kx-lt-chem` | **libretexts.org_en_chem_2025-01** – LibreTexts kémia tankönyvek (általános, szerves, analitikai, ipari). | 2.18 GB M | free | [link](https://lb.download.kiwix.org/zim/libretexts/libretexts.org_en_chem_2025-01.zim) |
| 2 | 5.45 | `kx-se-chemistry` | **chemistry.stackexchange.com_en_all_2026-10** – Kémia Q&A. | 419.96 MB M | free | [link](https://lb.download.kiwix.org/zim/stack_exchange/chemistry.stackexchange.com_en_all_2026-10.zim) |
| 2 | 4.7 | `kx-wp-en-chem` | **wikipedia_en_chemistry_maxi_2026-10** – Wikipedia kémia-tematikus részhalmaz (kis tárhelyre). | 383.97 MB M | free | [link](https://lb.download.kiwix.org/zim/wikipedia/wikipedia_en_chemistry_maxi_2026-10.zim) |

### Elektronika (`electronics`) – 3 elem

| T | Pont | id | Mi ez, mire jó | Méret | Hozzáférés | Link |
|---|---|---|---|---|---|---|
| 2 | 6.3 | `kx-se-electronics` | **electronics.stackexchange.com_en_all_2026-10** – Elektronika Q&A: áramkörtervezés, tápegységek, javítás. | 4.26 GB M | free | [link](https://lb.download.kiwix.org/zim/stack_exchange/electronics.stackexchange.com_en_all_2026-10.zim) |
| 3 | 4.75 | `kx-se-arduino` | **arduino.stackexchange.com_en_all_2026-10** – Arduino/mikrokontroller Q&A. | 259.58 MB M | free | [link](https://lb.download.kiwix.org/zim/stack_exchange/arduino.stackexchange.com_en_all_2026-10.zim) |
| 4 | 4.05 | `kx-se-robotics` | **robotics.stackexchange.com_en_all_2026-10** – Robotika Q&A. | 243.38 MB M | free | [link](https://lb.download.kiwix.org/zim/stack_exchange/robotics.stackexchange.com_en_all_2026-10.zim) |

### Kommunikáció, rádió (`communications`) – 1 elem

| T | Pont | id | Mi ez, mire jó | Méret | Hozzáférés | Link |
|---|---|---|---|---|---|---|
| 2 | 6.25 | `kx-se-ham` | **ham.stackexchange.com_en_all_2026-10** – Rádióamatőr Q&A: antennák, adó-vevők, terjedés. | 77.11 MB M | free | [link](https://lb.download.kiwix.org/zim/stack_exchange/ham.stackexchange.com_en_all_2026-10.zim) |

### Tudomány (`science`) – 12 elem

| T | Pont | id | Mi ez, mire jó | Méret | Hozzáférés | Link |
|---|---|---|---|---|---|---|
| 2 | 6.2 | `kx-lt-bio` | **libretexts.org_en_bio_2025-01** – LibreTexts biológia (mikrobiológia, genetika, ökológia, botanika). | 2.24 GB M | free | [link](https://lb.download.kiwix.org/zim/libretexts/libretexts.org_en_bio_2025-01.zim) |
| 2 | 6.0 | `kx-lt-phys` | **libretexts.org_en_phys_2026-01** – LibreTexts fizika tankönyvek. | 559.55 MB M | free | [link](https://lb.download.kiwix.org/zim/libretexts/libretexts.org_en_phys_2026-01.zim) |
| 2 | 5.45 | `kx-lt-math` | **libretexts.org_en_math_2026-01** – LibreTexts matematika (algebra, analízis, lineáris algebra). | 830.65 MB M | free | [link](https://lb.download.kiwix.org/zim/libretexts/libretexts.org_en_math_2026-01.zim) |
| 3 | 5.1 | `kx-lt-geo` | **libretexts.org_en_geo_2026-01** – LibreTexts földtudományok (geológia, talajtan, meteorológia). | 1.19 GB M | free | [link](https://lb.download.kiwix.org/zim/libretexts/libretexts.org_en_geo_2026-01.zim) |
| 3 | 5.0 | `kx-se-physics` | **physics.stackexchange.com_en_all_2026-10** – Fizika Q&A. | 1.84 GB M | free | [link](https://lb.download.kiwix.org/zim/stack_exchange/physics.stackexchange.com_en_all_2026-10.zim) |
| 3 | 4.5 | `kx-lt-stats` | **libretexts.org_en_stats_2026-01** – LibreTexts statisztika. | 215.78 MB M | free | [link](https://lb.download.kiwix.org/zim/libretexts/libretexts.org_en_stats_2026-01.zim) |
| 3 | 4.5 | `kx-se-biology` | **biology.stackexchange.com_en_all_2026-10** – Biológia Q&A. | 425.07 MB M | free | [link](https://lb.download.kiwix.org/zim/stack_exchange/biology.stackexchange.com_en_all_2026-10.zim) |
| 3 | 4.4 | `kx-wp-en-phys` | **wikipedia_en_physics_maxi_2026-10** – Wikipedia fizika részhalmaz. | 911.98 MB M | free | [link](https://lb.download.kiwix.org/zim/wikipedia/wikipedia_en_physics_maxi_2026-10.zim) |
| 3 | 4.2 | `kx-se-earthsci` | **earthscience.stackexchange.com_en_all_2026-10** – Földtudomány Q&A. | 132.91 MB M | free | [link](https://lb.download.kiwix.org/zim/stack_exchange/earthscience.stackexchange.com_en_all_2026-10.zim) |
| 3 | 4.15 | `kx-wp-en-molcell` | **wikipedia_en_molcell_maxi_2026-10** – Wikipedia molekuláris és sejtbiológia részhalmaz. | 728.29 MB M | free | [link](https://lb.download.kiwix.org/zim/wikipedia/wikipedia_en_molcell_maxi_2026-10.zim) |
| 3 | 3.85 | `kx-wp-en-math` | **wikipedia_en_mathematics_maxi_2026-09** – Wikipedia matematika részhalmaz. | 996.19 MB M | free | [link](https://lb.download.kiwix.org/zim/wikipedia/wikipedia_en_mathematics_maxi_2026-09.zim) |
| 4 | 4.3 | `kx-se-math` | **math.stackexchange.com_en_all_2026-08** – Matematika Q&A (nagy). | 7.42 GB M | free | [link](https://lb.download.kiwix.org/zim/stack_exchange/math.stackexchange.com_en_all_2026-08.zim) |

### Számítástechnika (`computing`) – 7 elem

| T | Pont | id | Mi ez, mire jó | Méret | Hozzáférés | Link |
|---|---|---|---|---|---|---|
| 2 | 5.4 | `kx-archwiki` | **archlinux_en_all_maxi_2026-10** – ArchWiki: a legjobb Linux-rendszergazda tudásbázis. | 38.31 MB M | free | [link](https://lb.download.kiwix.org/zim/other/archlinux_en_all_maxi_2026-10.zim) |
| 3 | 5.35 | `kx-python-docs` | **docs.python.org_en_all_2026-08a** – Hivatalos Python dokumentáció. | 3.96 GB M | free | [link](https://lb.download.kiwix.org/zim/zimit/docs.python.org_en_all_2026-08a.zim) |
| 3 | 5.15 | `kx-se-unix` | **unix.stackexchange.com_en_all_2026-10** – Unix/Linux shell és rendszer Q&A. | 1.32 GB M | free | [link](https://lb.download.kiwix.org/zim/stack_exchange/unix.stackexchange.com_en_all_2026-10.zim) |
| 3 | 4.75 | `kx-se-askubuntu` | **askubuntu.com_en_all_2026-10** – Ubuntu/Linux Q&A. | 2.77 GB M | free | [link](https://lb.download.kiwix.org/zim/stack_exchange/askubuntu.com_en_all_2026-10.zim) |
| 3 | 3.85 | `kx-wp-en-computer` | **wikipedia_en_computer_maxi_2026-09** – Wikipedia számítástechnika részhalmaz. | 910.01 MB M | free | [link](https://lb.download.kiwix.org/zim/wikipedia/wikipedia_en_computer_maxi_2026-09.zim) |
| 4 | 5.7 | `kx-stackoverflow` | **stackoverflow.com_en_all_2026-07** – Teljes StackOverflow: programozási tudás (114 GB). | 114.86 GB M | free | [link](https://lb.download.kiwix.org/zim/stack_exchange/stackoverflow.com_en_all_2026-07.zim) |
| 4 | 4.35 | `kx-se-superuser` | **superuser.com_en_all_2026-10** – Számítógép-használat Q&A. | 4.01 GB M | free | [link](https://lb.download.kiwix.org/zim/stack_exchange/superuser.com_en_all_2026-10.zim) |

### Magyar források (`hungarian`) – 4 elem

| T | Pont | id | Mi ez, mire jó | Méret | Hozzáférés | Link |
|---|---|---|---|---|---|---|
| 2 | 5.25 | `kx-wikibooks-hu` | **wikibooks_hu_all_maxi_2026-10** – Magyar Wikikönyvek. | 471.05 MB M | free | [link](https://lb.download.kiwix.org/zim/wikibooks/wikibooks_hu_all_maxi_2026-10.zim) |
| 2 | 4.6 | `kx-wiktionary-hu` | **wiktionary_hu_all_nopic_2026-10** – Magyar Wikiszótár (fordításokkal) – idegen nyelvű anyagok értelmezéséhez. | 786.57 MB M | free | [link](https://lb.download.kiwix.org/zim/wiktionary/wiktionary_hu_all_nopic_2026-10.zim) |
| 3 | 3.85 | `kx-gutenberg-hu` | **gutenberg_hu_all_2026-01** – Project Gutenberg magyar nyelvű könyvei. | 1.02 GB M | free | [link](https://lb.download.kiwix.org/zim/gutenberg/gutenberg_hu_all_2026-01.zim) |
| 3 | 3.5 | `kx-wikisource-hu` | **wikisource_hu_all_maxi_2026-10** – Magyar Wikiforrás. | 84.61 MB M | free | [link](https://lb.download.kiwix.org/zim/wikisource/wikisource_hu_all_maxi_2026-10.zim) |

### Oktatás (`education`) – 8 elem

| T | Pont | id | Mi ez, mire jó | Méret | Hozzáférés | Link |
|---|---|---|---|---|---|---|
| 3 | 4.95 | `kx-lt-k12` | **libretexts.org_en_k12_2026-01** – LibreTexts közoktatási anyagok. | 369.81 MB M | free | [link](https://lb.download.kiwix.org/zim/libretexts/libretexts.org_en_k12_2026-01.zim) |
| 3 | 4.85 | `kx-wikiversity` | **wikiversity_en_all_maxi_2026-11** – Wikiversity kurzusok. | 2.11 GB M | free | [link](https://lb.download.kiwix.org/zim/wikiversity/wikiversity_en_all_maxi_2026-11.zim) |
| 3 | 4.7 | `kx-phet-hu` | **phet_hu_all_2026-08** – PhET interaktív fizika/kémia szimulációk magyarul (böngésző + JS kell). | 96.04 MB M | free | [link](https://lb.download.kiwix.org/zim/phet/phet_hu_all_2026-08.zim) |
| 3 | 4.45 | `kx-wp-simple` | **wikipedia_en-simple_all_maxi_2026-09** – Simple English Wikipedia – egyszerű angol, tanuláshoz/gyerekeknek. | 3.12 GB M | free | [link](https://lb.download.kiwix.org/zim/wikipedia/wikipedia_en-simple_all_maxi_2026-09.zim) |
| 4 | 5.8 | `kx-khan` | **khanacademy_en_all_2023-03** – Khan Academy teljes angol kurzusanyag videókkal (2023-as snapshot) – gyerekek/új generáció oktatása. | 180.01 GB M | free | [link](https://lb.download.kiwix.org/zim/other/khanacademy_en_all_2023-03.zim) |
| 4 | 4.25 | `kx-phet-en` | **phet_en_all_2026-08** – PhET szimulációk angolul. | 108.98 MB M | free | [link](https://lb.download.kiwix.org/zim/phet/phet_en_all_2026-08.zim) |
| 4 | 4.1 | `kx-crashcourse` | **crashcourse_en_all_2026-05** – CrashCourse oktatóvideók (tudomány, történelem). | 23.04 GB M | free | [link](https://lb.download.kiwix.org/zim/other/crashcourse_en_all_2026-05.zim) |
| 5 | 2.5 | `kx-ted` | **ted_mul_all_2026-09** – TED előadások videón. | 91.18 GB M | free | [link](https://lb.download.kiwix.org/zim/ted/ted_mul_all_2026-09.zim) |

### Könyvtárak (`library`) – 4 elem

| T | Pont | id | Mi ez, mire jó | Méret | Hozzáférés | Link |
|---|---|---|---|---|---|---|
| 3 | 4.6 | `kx-wikisource-en-nopic` | **wikisource_en_all_nopic_2026-09** – Wikisource: közkincs szövegek (pl. 1911-es Britannica, régi szakkönyvek). | 3.91 GB M | free | [link](https://lb.download.kiwix.org/zim/wikisource/wikisource_en_all_nopic_2026-09.zim) |
| 3 | 4.6 | `kx-wikisource-en-maxi` | **wikisource_en_all_maxi_2026-09** – Wikisource képekkel. | 8.62 GB M | free | [link](https://lb.download.kiwix.org/zim/wikisource/wikisource_en_all_maxi_2026-09.zim) |
| 4 | 4.55 | `kx-gutenberg-en` | **gutenberg_en_all_2025-11** – Project Gutenberg angol könyvek (~70e+ közkincs mű). | 221.25 GB M | free | [link](https://lb.download.kiwix.org/zim/gutenberg/gutenberg_en_all_2025-11.zim) |
| 4 | 4.55 | `kx-gutenberg-mul` | **gutenberg_mul_all_2025-11** – Project Gutenberg összes nyelv. | 253.06 GB M | free | [link](https://lb.download.kiwix.org/zim/gutenberg/gutenberg_mul_all_2025-11.zim) |

### Bölcsészet (`humanities`) – 4 elem

| T | Pont | id | Mi ez, mire jó | Méret | Hozzáférés | Link |
|---|---|---|---|---|---|---|
| 3 | 3.45 | `kx-wp-en-history` | **wikipedia_en_history_maxi_2026-10** – Wikipedia történelem részhalmaz. | 1.99 GB M | free | [link](https://lb.download.kiwix.org/zim/wikipedia/wikipedia_en_history_maxi_2026-10.zim) |
| 4 | 3.85 | `kx-lt-biz` | **libretexts.org_en_biz_2026-01** – LibreTexts üzlet/közgazdaság. | 839.75 MB M | free | [link](https://lb.download.kiwix.org/zim/libretexts/libretexts.org_en_biz_2026-01.zim) |
| 4 | 3.7 | `kx-lt-human` | **libretexts.org_en_human_2026-07** – LibreTexts bölcsészet. | 4.43 GB M | free | [link](https://lb.download.kiwix.org/zim/libretexts/libretexts.org_en_human_2026-07.zim) |
| 4 | 3.7 | `kx-lt-socialsci` | **libretexts.org_en_socialsci_2025-01** – LibreTexts társadalomtudományok. | 2.05 GB M | free | [link](https://lb.download.kiwix.org/zim/libretexts/libretexts.org_en_socialsci_2025-01.zim) |


---

## 6. Helyi LLM-ek

(készül)


---

## 7. Letöltési receptek

A `download.method` mező szerint. Mindegyik újraindítható.

| method | Parancs-sablon | Ellenőrzés |
|---|---|---|
| `kiwix` | `curl -fsSL "https://library.kiwix.org/catalog/v2/entries?name=<book>&count=50"`: az `<entry>`-k közül a `<flavour>` egyezik, a legnagyobb dátumú `…zim.meta4` link a jó. Utána `aria2c -c --seed-time=0 <url>.meta4` (vagy `wget -c <url>`). | `curl -fsSL <url>.sha256 \| sha256sum -c -`; opcionálisan `zimcheck -A file.zim` |
| `http` | `aria2c -c -x8 -s8 <url>` vagy `wget -c <url>` | méret = Content-Length; sha256, ha a forrás közli |
| `wget-mirror` | `wget -m -np -k -E -c -e robots=off --wait=1 <url>` (HTML-gyűjtemény, PDF-könyvtár) | darabszám és hibalista (`grep -c ERROR wget.log`) |
| `rsync` | `rsync -avP --partial <rsync://…> <cél>/` | az rsync maga ellenőriz (`--checksum` a második körben) |
| `git` | `git clone --mirror <repo> X.git && git -C X.git bundle create X.bundle --all` (a bundle egy fájl, git nélkül is másolható) | `git bundle verify X.bundle` |
| `hf` | `pip install -U huggingface_hub` → `hf download <owner/repo> --include "<minta>" --local-dir <cél>`. Gated repóhoz előbb `hf auth login`. Gyorsítás: `pip install hf_xet` (alapértelmezett backend), vagy `HF_HUB_ENABLE_HF_TRANSFER=1` régebbi verzióknál. | a HF API `lfs.oid` = sha256: `curl -s https://huggingface.co/api/models/<repo>/tree/main?recursive=true` |
| `ollama` | `ollama pull <tag>`. Offline átvitelhez másold az `~/.ollama/models` (Linux szerver: `/usr/share/ollama/.ollama/models`) könyvtárat, vagy állíts be `OLLAMA_MODELS=<meghajtó>`-t. | `ollama list`, `ollama show <tag>` |
| `archive.org` | `pip install internetarchive` → `ia download <identifier> --glob="*.pdf" --destdir <cél>`. A fájllista és a méretek: `https://archive.org/metadata/<identifier>`. | md5/sha1 a metadata JSON-ban |
| `torrent` | `aria2c -c --seed-time=0 <magnet vagy .torrent>`. Ha lehet, seedeld tovább. | a torrent beépített hash-ellenőrzése |
| `jigdo` | `apt install jigdo-file` → `jigdo-lite <url>.jigdo` (a Debian DVD/BD készletet a tükörből rakja össze) | a `.iso` sha256/sha512 a `SHA256SUMS` alapján |
| `s3` | `aws s3 sync s3://… <cél> --request-payer requester`. **Fizetős adatforgalom** (pl. arXiv bulk), ezért előbb költségbecslés. | ETag / manifest |
| `manual` / `purchase` | Az AI nem csinálja meg. Listázza a linkkel és árral, az ember dönt. | — |

### Olvasók és futtatók (a `tool-*` elemek, mindig kerüljenek a meghajtóra)

- **ZIM:**
  - Kiwix Desktop (Windows/Linux AppImage/macOS): <https://download.kiwix.org/release/kiwix-desktop/>
  - Kiwix Android (F-Droid / APK): <https://download.kiwix.org/release/kiwix-android/>
  - `kiwix-serve` (kiwix-tools, egy Raspberry Pi kiszolgálja az egész LAN-t, böngészőből érhető el): <https://download.kiwix.org/release/kiwix-tools/>
  - Indítás: `kiwix-serve --port 8080 /archivum/**/*.zim`, utána `http://<ip>:8080`.
- **PDF / EPUB:** SumatraPDF (Windows), Okular/Evince (Linux), KOReader (e-ink, Android), Calibre (könyvtárkezelés).
- **Videó:** VLC (minden platformra, a telepítőt is mentsd le).
- **Térkép:** Organic Maps / OsmAnd APK + offline térképfájlok, QGIS a nyers OSM/DEM adatokhoz.
- **LLM:** lásd a 6. fejezetet (llama.cpp binárisok, Ollama, LM Studio, PocketPal).


---

## 9. Gépi katalógus

Soronként egy JSON-objektum. Mezők: `id`, `name`, `cat`, `tier` (0–5), `group` (egymást kizáró változatok), `variant_rank`, `variant_role` (`pref` = ajánlott, `luxury`), `desc_hu`, `lang`, `access` (free | free-registration | donation | paid | gray | physical), `price`, `license`, `bytes` (mért vagy hivatalos), `bytes_est` (becsült), `size_status`, `format`, `info_url`, `download` {method, …}, `url_status`, `scores` {S,R,A,U,Q,O}, `requires`, `subsumed_by`, `hw_tiers` (LLM: T1–T5), `notes`.

```jsonl
{"id":"kx-cd3wd","name":"cd3wdproject.org_en_all_2026-11","cat":"appropriate_tech","tier":0,"desc_hu":"CD3WD: fejlődő országoknak készült több ezer technológiai kézikönyv (mezőgazdaság, víz, építés, kisipar, egészség).","lang":"en","access":"free","license":"CC-BY-SA / közkincs (ZIM metaadat)","bytes":572638208,"size_human":"572.64 MB","size_status":"measured:2026-11-14:kiwix-opds","format":"zim","download":{"method":"kiwix","book":"cd3wdproject.org_en_all","flavour":null,"url":"https://lb.download.kiwix.org/zim/zimit/cd3wdproject.org_en_all_2026-11.zim"},"url_status":"200 verified 2026-11-14","scores":{"S":8,"R":8,"A":8,"U":8,"Q":7,"O":9},"requires":["tool-kiwix"]}
{"id":"kx-food-prep","name":"zimgit-food-preparation_en_2025-04","cat":"food","tier":0,"desc_hu":"Élelmiszer-feldolgozás és -tartósítás (szárítás, befőzés, füstölés) útmutatói.","lang":"en","access":"free","license":"CC-BY-SA / közkincs (ZIM metaadat)","bytes":97822720,"size_human":"97.82 MB","size_status":"measured:2026-11-14:kiwix-opds","format":"zim","download":{"method":"kiwix","book":"zimgit-food-preparation_en","flavour":null,"url":"https://lb.download.kiwix.org/zim/other/zimgit-food-preparation_en_2025-04.zim"},"url_status":"200 verified 2026-11-14","scores":{"S":7,"R":4,"A":8,"U":5,"Q":7,"O":9},"requires":["tool-kiwix"]}
{"id":"kx-fas-milmed","name":"irp.fas.org_en_military-medicine_2026-10","cat":"medicine","tier":0,"desc_hu":"US katonai orvosi kézikönyvek (FAS gyűjtés): trauma, sebellátás, terepi sebészet, járványügy.","lang":"en","access":"free","license":"CC-BY-SA / közkincs (ZIM metaadat)","bytes":64986112,"size_human":"64.99 MB","size_status":"measured:2026-11-14:kiwix-opds","format":"zim","download":{"method":"kiwix","book":"irp.fas.org_en_military-medicine","flavour":null,"url":"https://lb.download.kiwix.org/zim/zimit/irp.fas.org_en_military-medicine_2026-10.zim"},"url_status":"200 verified 2026-11-14","scores":{"S":9,"R":5,"A":9,"U":8,"Q":9,"O":9},"requires":["tool-kiwix"]}
{"id":"kx-mdwiki","name":"mdwiki_en_all_maxi_2025-11","cat":"medicine","tier":0,"desc_hu":"WikiProjectMed orvosi enciklopédia (betegségek, gyógyszerek, eljárások), képekkel; laikus és szakmai szinten is használható.","lang":"en","access":"free","license":"CC-BY-SA / közkincs (ZIM metaadat)","bytes":2302838784,"size_human":"2.30 GB","size_status":"measured:2026-11-14:kiwix-opds","format":"zim","download":{"method":"kiwix","book":"mdwiki_en_all","flavour":"maxi","url":"https://lb.download.kiwix.org/zim/other/mdwiki_en_all_maxi_2025-11.zim"},"url_status":"200 verified 2026-11-14","scores":{"S":9,"R":6,"A":6,"U":6,"Q":8,"O":9},"requires":["tool-kiwix"]}
{"id":"kx-nhs-medicines","name":"nhs.uk_en_medicines_2026-09b","cat":"medicine","tier":0,"desc_hu":"NHS gyógyszer-adatlapok: adagolás, mellékhatás, kölcsönhatás – egyszerű nyelven.","lang":"en","access":"free","license":"CC-BY-SA / közkincs (ZIM metaadat)","bytes":15323136,"size_human":"15.32 MB","size_status":"measured:2026-11-14:kiwix-opds","format":"zim","download":{"method":"kiwix","book":"nhs.uk_en_medicines","flavour":null,"url":"https://lb.download.kiwix.org/zim/zimit/nhs.uk_en_medicines_2026-09b.zim"},"url_status":"200 verified 2026-11-14","scores":{"S":7,"R":3,"A":7,"U":5,"Q":9,"O":9},"requires":["tool-kiwix"]}
{"id":"kx-wp-en-med","name":"wikipedia_en_medicine_maxi_2026-10","cat":"medicine","tier":0,"group":"wp-en-med","variant_rank":2,"variant_role":"pref","desc_hu":"Wikipedia összes orvosi cikke képekkel (önálló, ha nincs teljes WP).","lang":"en","access":"free","license":"CC-BY-SA / közkincs (ZIM metaadat)","bytes":1864210432,"size_human":"1.86 GB","size_status":"measured:2026-11-14:kiwix-opds","format":"zim","download":{"method":"kiwix","book":"wikipedia_en_medicine","flavour":"maxi","url":"https://lb.download.kiwix.org/zim/wikipedia/wikipedia_en_medicine_maxi_2026-10.zim"},"url_status":"200 verified 2026-11-14","scores":{"S":8,"R":6,"A":4,"U":4,"Q":7,"O":9},"requires":["tool-kiwix"],"subsumed_by":["kx-wp-en-maxi","kx-wp-en-nopic"]}
{"id":"kx-wp-en-med-nopic","name":"wikipedia_en_medicine_nopic_2026-10","cat":"medicine","tier":0,"group":"wp-en-med","variant_rank":1,"desc_hu":"Wikipedia orvosi cikkek képek nélkül.","lang":"en","access":"free","license":"CC-BY-SA / közkincs (ZIM metaadat)","bytes":1047708672,"size_human":"1.05 GB","size_status":"measured:2026-11-14:kiwix-opds","format":"zim","download":{"method":"kiwix","book":"wikipedia_en_medicine","flavour":"nopic","url":"https://lb.download.kiwix.org/zim/wikipedia/wikipedia_en_medicine_nopic_2026-10.zim"},"url_status":"200 verified 2026-11-14","scores":{"S":8,"R":6,"A":4,"U":4,"Q":7,"O":9},"requires":["tool-kiwix"],"subsumed_by":["kx-wp-en-maxi","kx-wp-en-nopic"]}
{"id":"kx-zimgit-medicine","name":"zimgit-medicine_en_2024-08","cat":"medicine","tier":0,"desc_hu":"Válogatott terepi orvosi kézikönyvek (elsősegély, orvos nélküli ellátás).","lang":"en","access":"free","license":"CC-BY-SA / közkincs (ZIM metaadat)","bytes":70179840,"size_human":"70.18 MB","size_status":"measured:2026-11-14:kiwix-opds","format":"zim","download":{"method":"kiwix","book":"zimgit-medicine_en","flavour":null,"url":"https://lb.download.kiwix.org/zim/other/zimgit-medicine_en_2024-08.zim"},"url_status":"200 verified 2026-11-14","scores":{"S":8,"R":4,"A":8,"U":6,"Q":7,"O":9},"requires":["tool-kiwix"]}
{"id":"kx-post-disaster","name":"zimgit-post-disaster_en_2024-05","cat":"survival","tier":0,"desc_hu":"Katasztrófa utáni kézikönyv-gyűjtemény (menedék, víz, egészség, újjáépítés) – rendezett PDF/HTML anyagok.","lang":"en","access":"free","license":"CC-BY-SA / közkincs (ZIM metaadat)","bytes":644666368,"size_human":"644.67 MB","size_status":"measured:2026-11-14:kiwix-opds","format":"zim","download":{"method":"kiwix","book":"zimgit-post-disaster_en","flavour":null,"url":"https://lb.download.kiwix.org/zim/other/zimgit-post-disaster_en_2024-05.zim"},"url_status":"200 verified 2026-11-14","scores":{"S":9,"R":6,"A":9,"U":8,"Q":7,"O":9},"requires":["tool-kiwix"]}
{"id":"tool-kiwix","name":"Kiwix olvasók (Desktop Win/Linux, Android APK, kiwix-tools szerver x86_64+ARM64)","cat":"tools","tier":0,"desc_hu":"A ZIM-fájlok olvasója. A kiwix-serve egy Raspberry Pi-ről a teljes helyi hálózatnak kiszolgálja az archívumot böngészőn át.","lang":"multi","access":"free","license":"GPLv3","bytes":603726769,"size_human":"603.73 MB","size_status":"measured:2026-11-14:content-length","format":"zip/appimage/apk/tar.gz","info_url":"https://kiwix.org/en/applications/","download":{"method":"http","urls":["https://download.kiwix.org/release/kiwix-desktop/kiwix-desktop_windows_x64.zip","https://download.kiwix.org/release/kiwix-desktop/kiwix-desktop_x86_64.appimage","https://download.kiwix.org/release/kiwix-tools/kiwix-tools_linux-x86_64.tar.gz","https://download.kiwix.org/release/kiwix-tools/kiwix-tools_linux-aarch64.tar.gz","https://download.kiwix.org/release/kiwix-android/kiwix.apk"]},"url_status":"200 verified 2026-11-14","scores":{"S":8,"R":8,"A":10,"U":10,"Q":9,"O":10},"notes":"macOS: Mac App Store 'Kiwix' (vagy https://download.kiwix.org/release/kiwix-macos/). iOS: App Store. Indítás: kiwix-serve --port 8080 *.zim"}
{"id":"tool-vlc","name":"VLC médialejátszó (Win64, macOS, forrás)","cat":"tools","tier":0,"desc_hu":"Videók és hangfájlok lejátszása (videós ZIM-ek, oktatóvideók, LibriVox).","lang":"multi","access":"free","license":"GPLv2","bytes_est":200000000,"size_human":"~200 MB","size_status":"estimated:3 installer ~40-80 MB each","format":"exe/dmg/tar.xz","info_url":"https://www.videolan.org/vlc/","download":{"method":"http","urls":["https://get.videolan.org/vlc/last/win64/vlc-3.0.24-win64.exe","https://get.videolan.org/vlc/last/macosx/vlc-3.0.24-universal.dmg","https://get.videolan.org/vlc/last/vlc-3.0.24.tar.xz"]},"url_status":"directory listing verified 2026-11-14","scores":{"S":3,"R":5,"A":8,"U":7,"Q":9,"O":10},"notes":"A verziószám változik: a https://get.videolan.org/vlc/last/ listából vedd az aktuálisat. Android: F-Droid org.videolan.vlc."}
{"id":"kx-water","name":"zimgit-water_en_2024-08","cat":"water_sanitation","tier":0,"desc_hu":"Víztisztítás, kutak, szűrők, fertőtlenítés gyakorlati anyagai.","lang":"en","access":"free","license":"CC-BY-SA / közkincs (ZIM metaadat)","bytes":20925440,"size_human":"20.93 MB","size_status":"measured:2026-11-14:kiwix-opds","format":"zim","download":{"method":"kiwix","book":"zimgit-water_en","flavour":null,"url":"https://lb.download.kiwix.org/zim/other/zimgit-water_en_2024-08.zim"},"url_status":"200 verified 2026-11-14","scores":{"S":9,"R":5,"A":9,"U":6,"Q":7,"O":9},"requires":["tool-kiwix"]}
{"id":"kx-se-gardening","name":"gardening.stackexchange.com_en_all_2026-10","cat":"agriculture","tier":1,"desc_hu":"Kertészet, növényvédelem, termesztés Q&A.","lang":"en","access":"free","license":"CC-BY-SA / közkincs (ZIM metaadat)","bytes":933097472,"size_human":"933.10 MB","size_status":"measured:2026-11-14:kiwix-opds","format":"zim","download":{"method":"kiwix","book":"gardening.stackexchange.com_en_all","flavour":null,"url":"https://lb.download.kiwix.org/zim/stack_exchange/gardening.stackexchange.com_en_all_2026-10.zim"},"url_status":"200 verified 2026-11-14","scores":{"S":7,"R":5,"A":8,"U":6,"Q":7,"O":9},"requires":["tool-kiwix"]}
{"id":"kx-appropedia","name":"appropedia_en_all_maxi_2026-02","cat":"appropriate_tech","tier":1,"desc_hu":"Appropedia: megfelelő technológia, fenntartható építés, víz, energia, egészség.","lang":"en","access":"free","license":"CC-BY-SA / közkincs (ZIM metaadat)","bytes":581642240,"size_human":"581.64 MB","size_status":"measured:2026-11-14:kiwix-opds","format":"zim","download":{"method":"kiwix","book":"appropedia_en_all","flavour":"maxi","url":"https://lb.download.kiwix.org/zim/other/appropedia_en_all_maxi_2026-02.zim"},"url_status":"200 verified 2026-11-14","scores":{"S":6,"R":7,"A":7,"U":7,"Q":6,"O":9},"requires":["tool-kiwix"]}
{"id":"kx-se-diy","name":"diy.stackexchange.com_en_all_2026-10","cat":"construction","tier":1,"desc_hu":"Házfelújítás, villany-, víz-, fűtésszerelés kérdés-válasz formában.","lang":"en","access":"free","license":"CC-BY-SA / közkincs (ZIM metaadat)","bytes":2086025216,"size_human":"2.09 GB","size_status":"measured:2026-11-14:kiwix-opds","format":"zim","download":{"method":"kiwix","book":"diy.stackexchange.com_en_all","flavour":null,"url":"https://lb.download.kiwix.org/zim/stack_exchange/diy.stackexchange.com_en_all_2026-10.zim"},"url_status":"200 verified 2026-11-14","scores":{"S":5,"R":6,"A":9,"U":7,"Q":7,"O":9},"requires":["tool-kiwix"]}
{"id":"kx-energypedia","name":"energypedia_en_all_maxi_2026-06","cat":"energy","tier":1,"desc_hu":"Energypedia: kisléptékű energia (napelem, biogáz, mikro-víz, főzőkályhák).","lang":"en","access":"free","license":"CC-BY-SA / közkincs (ZIM metaadat)","bytes":799713280,"size_human":"799.71 MB","size_status":"measured:2026-11-14:kiwix-opds","format":"zim","download":{"method":"kiwix","book":"energypedia_en_all","flavour":"maxi","url":"https://lb.download.kiwix.org/zim/other/energypedia_en_all_maxi_2026-06.zim"},"url_status":"200 verified 2026-11-14","scores":{"S":5,"R":7,"A":6,"U":7,"Q":7,"O":9},"requires":["tool-kiwix"]}
{"id":"kx-lt-workforce","name":"libretexts.org_en_workforce_2026-01","cat":"manufacturing","tier":1,"desc_hu":"LibreTexts szakképzés: hegesztés, villanyszerelés, HVAC, építőipar, gépészet.","lang":"en","access":"free","license":"CC-BY-SA / közkincs (ZIM metaadat)","bytes":513664000,"size_human":"513.66 MB","size_status":"measured:2026-11-14:kiwix-opds","format":"zim","download":{"method":"kiwix","book":"libretexts.org_en_workforce","flavour":null,"url":"https://lb.download.kiwix.org/zim/libretexts/libretexts.org_en_workforce_2026-01.zim"},"url_status":"200 verified 2026-11-14","scores":{"S":5,"R":8,"A":8,"U":7,"Q":8,"O":9},"requires":["tool-kiwix"]}
{"id":"kx-cdc","name":"wwwnc.cdc.gov_en_all_2024-11","cat":"medicine","tier":1,"desc_hu":"CDC Travel Health: fertőző betegségek, oltások, megelőzés országonként.","lang":"en","access":"free","license":"CC-BY-SA / közkincs (ZIM metaadat)","bytes":178327552,"size_human":"178.33 MB","size_status":"measured:2026-11-14:kiwix-opds","format":"zim","download":{"method":"kiwix","book":"wwwnc.cdc.gov_en_all","flavour":null,"url":"https://lb.download.kiwix.org/zim/zimit/wwwnc.cdc.gov_en_all_2024-11.zim"},"url_status":"200 verified 2026-11-14","scores":{"S":6,"R":3,"A":5,"U":5,"Q":9,"O":9},"requires":["tool-kiwix"]}
{"id":"kx-lt-med","name":"libretexts.org_en_med_2025-01","cat":"medicine","tier":1,"desc_hu":"LibreTexts orvosi/ápolási egyetemi tankönyvek (anatómia, ápolás, farmakológia).","lang":"en","access":"free","license":"CC-BY-SA / közkincs (ZIM metaadat)","bytes":1192567808,"size_human":"1.19 GB","size_status":"measured:2026-11-14:kiwix-opds","format":"zim","download":{"method":"kiwix","book":"libretexts.org_en_med","flavour":null,"url":"https://lb.download.kiwix.org/zim/libretexts/libretexts.org_en_med_2025-01.zim"},"url_status":"200 verified 2026-11-14","scores":{"S":8,"R":7,"A":6,"U":5,"Q":9,"O":9},"requires":["tool-kiwix"]}
{"id":"kx-wp-en-maxi","name":"wikipedia_en_all_maxi_2026-08","cat":"reference","tier":1,"group":"wp-en","variant_rank":6,"variant_role":"luxury","desc_hu":"Teljes angol Wikipedia képekkel (6,9M+ cikk). A tudásbázis gerince.","lang":"en","access":"free","license":"CC-BY-SA / közkincs (ZIM metaadat)","bytes":127418088448,"size_human":"127.42 GB","size_status":"measured:2026-11-14:kiwix-opds","format":"zim","download":{"method":"kiwix","book":"wikipedia_en_all","flavour":"maxi","url":"https://lb.download.kiwix.org/zim/wikipedia/wikipedia_en_all_maxi_2026-08.zim"},"url_status":"200 verified 2026-11-14","scores":{"S":6,"R":9,"A":4,"U":9,"Q":8,"O":9},"requires":["tool-kiwix"]}
{"id":"kx-wp-en-mini","name":"wikipedia_en_all_mini_2026-09","cat":"reference","tier":1,"group":"wp-en","variant_rank":3,"desc_hu":"Összes angol cikk, de csak bevezető + infobox.","lang":"en","access":"free","license":"CC-BY-SA / közkincs (ZIM metaadat)","bytes":14386799616,"size_human":"14.39 GB","size_status":"measured:2026-11-14:kiwix-opds","format":"zim","download":{"method":"kiwix","book":"wikipedia_en_all","flavour":"mini","url":"https://lb.download.kiwix.org/zim/wikipedia/wikipedia_en_all_mini_2026-09.zim"},"url_status":"200 verified 2026-11-14","scores":{"S":5,"R":7,"A":3,"U":8,"Q":8,"O":9},"requires":["tool-kiwix"]}
{"id":"kx-wp-en-nopic","name":"wikipedia_en_all_nopic_2026-06","cat":"reference","tier":1,"group":"wp-en","variant_rank":5,"variant_role":"pref","desc_hu":"Teljes angol Wikipedia képek nélkül – legjobb tudás/GB arány.","lang":"en","access":"free","license":"CC-BY-SA / közkincs (ZIM metaadat)","bytes":52690707456,"size_human":"52.69 GB","size_status":"measured:2026-11-14:kiwix-opds","format":"zim","download":{"method":"kiwix","book":"wikipedia_en_all","flavour":"nopic","url":"https://lb.download.kiwix.org/zim/wikipedia/wikipedia_en_all_nopic_2026-06.zim"},"url_status":"200 verified 2026-11-14","scores":{"S":6,"R":9,"A":4,"U":9,"Q":8,"O":9},"requires":["tool-kiwix"]}
{"id":"kx-wp-en-top-maxi","name":"wikipedia_en_top_maxi_2026-09","cat":"reference","tier":1,"group":"wp-en","variant_rank":2,"desc_hu":"Top ~50 ezer angol cikk képekkel.","lang":"en","access":"free","license":"CC-BY-SA / közkincs (ZIM metaadat)","bytes":6991082496,"size_human":"6.99 GB","size_status":"measured:2026-11-14:kiwix-opds","format":"zim","download":{"method":"kiwix","book":"wikipedia_en_top","flavour":"maxi","url":"https://lb.download.kiwix.org/zim/wikipedia/wikipedia_en_top_maxi_2026-09.zim"},"url_status":"200 verified 2026-11-14","scores":{"S":5,"R":6,"A":3,"U":6,"Q":8,"O":9},"requires":["tool-kiwix"]}
{"id":"kx-wp-en-top-nopic","name":"wikipedia_en_top_nopic_2026-09","cat":"reference","tier":1,"group":"wp-en","variant_rank":1,"desc_hu":"Top ~50 ezer angol cikk képek nélkül (kis tárhelyre).","lang":"en","access":"free","license":"CC-BY-SA / közkincs (ZIM metaadat)","bytes":2745850880,"size_human":"2.75 GB","size_status":"measured:2026-11-14:kiwix-opds","format":"zim","download":{"method":"kiwix","book":"wikipedia_en_top","flavour":"nopic","url":"https://lb.download.kiwix.org/zim/wikipedia/wikipedia_en_top_nopic_2026-09.zim"},"url_status":"200 verified 2026-11-14","scores":{"S":5,"R":6,"A":3,"U":6,"Q":8,"O":9},"requires":["tool-kiwix"]}
{"id":"kx-wp-en-top1m","name":"wikipedia_en_top1m_nopic_2026-04","cat":"reference","tier":1,"group":"wp-en","variant_rank":4,"desc_hu":"A legolvasottabb 1 millió angol cikk, képek nélkül.","lang":"en","access":"free","license":"CC-BY-SA / közkincs (ZIM metaadat)","bytes":17134155776,"size_human":"17.13 GB","size_status":"measured:2026-11-14:kiwix-opds","format":"zim","download":{"method":"kiwix","book":"wikipedia_en_top1m","flavour":"nopic","url":"https://lb.download.kiwix.org/zim/wikipedia/wikipedia_en_top1m_nopic_2026-04.zim"},"url_status":"200 verified 2026-11-14","scores":{"S":6,"R":8,"A":4,"U":8,"Q":8,"O":9},"requires":["tool-kiwix"]}
{"id":"kx-wp-hu-maxi","name":"wikipedia_hu_all_maxi_2026-06","cat":"reference","tier":1,"group":"wp-hu","variant_rank":4,"variant_role":"pref","desc_hu":"Teljes magyar Wikipédia képekkel.","lang":"hu","access":"free","license":"CC-BY-SA / közkincs (ZIM metaadat)","bytes":12017786880,"size_human":"12.02 GB","size_status":"measured:2026-11-14:kiwix-opds","format":"zim","download":{"method":"kiwix","book":"wikipedia_hu_all","flavour":"maxi","url":"https://lb.download.kiwix.org/zim/wikipedia/wikipedia_hu_all_maxi_2026-06.zim"},"url_status":"200 verified 2026-11-14","scores":{"S":6,"R":8,"A":4,"U":7,"Q":7,"O":9},"requires":["tool-kiwix"]}
{"id":"kx-wp-hu-mini","name":"wikipedia_hu_all_mini_2026-10","cat":"reference","tier":1,"group":"wp-hu","variant_rank":1,"desc_hu":"Összes magyar cikk, csak bevezetővel.","lang":"hu","access":"free","license":"CC-BY-SA / közkincs (ZIM metaadat)","bytes":1158164480,"size_human":"1.16 GB","size_status":"measured:2026-11-14:kiwix-opds","format":"zim","download":{"method":"kiwix","book":"wikipedia_hu_all","flavour":"mini","url":"https://lb.download.kiwix.org/zim/wikipedia/wikipedia_hu_all_mini_2026-10.zim"},"url_status":"200 verified 2026-11-14","scores":{"S":5,"R":6,"A":3,"U":6,"Q":7,"O":9},"requires":["tool-kiwix"]}
{"id":"kx-wp-hu-nopic","name":"wikipedia_hu_all_nopic_2026-10","cat":"reference","tier":1,"group":"wp-hu","variant_rank":3,"desc_hu":"Teljes magyar Wikipédia képek nélkül.","lang":"hu","access":"free","license":"CC-BY-SA / közkincs (ZIM metaadat)","bytes":4247143424,"size_human":"4.25 GB","size_status":"measured:2026-11-14:kiwix-opds","format":"zim","download":{"method":"kiwix","book":"wikipedia_hu_all","flavour":"nopic","url":"https://lb.download.kiwix.org/zim/wikipedia/wikipedia_hu_all_nopic_2026-10.zim"},"url_status":"200 verified 2026-11-14","scores":{"S":6,"R":8,"A":4,"U":7,"Q":7,"O":9},"requires":["tool-kiwix"]}
{"id":"kx-wp-hu-top","name":"wikipedia_hu_top_maxi_2026-10","cat":"reference","tier":1,"group":"wp-hu","variant_rank":2,"desc_hu":"A legfontosabb magyar cikkek képekkel.","lang":"hu","access":"free","license":"CC-BY-SA / közkincs (ZIM metaadat)","bytes":2235771904,"size_human":"2.24 GB","size_status":"measured:2026-11-14:kiwix-opds","format":"zim","download":{"method":"kiwix","book":"wikipedia_hu_top","flavour":"maxi","url":"https://lb.download.kiwix.org/zim/wikipedia/wikipedia_hu_top_maxi_2026-10.zim"},"url_status":"200 verified 2026-11-14","scores":{"S":5,"R":6,"A":3,"U":6,"Q":7,"O":9},"requires":["tool-kiwix"]}
{"id":"kx-ifixit","name":"ifixit_en_all_2025-12","cat":"repair","tier":1,"desc_hu":"iFixit: lépésről lépésre javítási útmutatók eszközökhöz, járművekhez, elektronikához.","lang":"en","access":"free","license":"CC-BY-SA / közkincs (ZIM metaadat)","bytes":3570696192,"size_human":"3.57 GB","size_status":"measured:2026-11-14:kiwix-opds","format":"zim","download":{"method":"kiwix","book":"ifixit_en_all","flavour":null,"url":"https://lb.download.kiwix.org/zim/ifixit/ifixit_en_all_2025-12.zim"},"url_status":"200 verified 2026-11-14","scores":{"S":5,"R":6,"A":9,"U":8,"Q":8,"O":9},"requires":["tool-kiwix"]}
{"id":"kx-knots","name":"zimgit-knots_en_2024-08","cat":"survival","tier":1,"desc_hu":"Csomókötés animált útmutatókkal (kötélmunka, emelés, hajózás).","lang":"en","access":"free","license":"CC-BY-SA / közkincs (ZIM metaadat)","bytes":27945984,"size_human":"27.95 MB","size_status":"measured:2026-11-14:kiwix-opds","format":"zim","download":{"method":"kiwix","book":"zimgit-knots_en","flavour":null,"url":"https://lb.download.kiwix.org/zim/other/zimgit-knots_en_2024-08.zim"},"url_status":"200 verified 2026-11-14","scores":{"S":5,"R":3,"A":9,"U":5,"Q":8,"O":9},"requires":["tool-kiwix"]}
{"id":"tool-fdroid-repo-apks","name":"Android alapalkalmazások (F-Droid): F-Droid, VLC, Organic Maps, KOReader","cat":"tools","tier":1,"desc_hu":"Android telefonra/tabletre offline telepíthető APK-k: térkép, e-könyv olvasó, médialejátszó.","lang":"multi","access":"free","license":"FOSS","bytes_est":300000000,"size_human":"~300 MB","size_status":"estimated:4 APK","format":"apk","info_url":"https://f-droid.org/","download":{"method":"manual","note":"A pontos APK-fájlnév verziókódot tartalmaz: töltsd le az f-droid.org/packages/<pkg>/ oldalról: org.fdroid.fdroid, org.videolan.vlc, app.organicmaps, org.koreader.launcher.fdroid"},"url_status":"f-droid.org/repo 200 verified 2026-11-14","scores":{"S":5,"R":5,"A":8,"U":6,"Q":8,"O":10}}
{"id":"tool-sumatra","name":"SumatraPDF (Windows, hordozható)","cat":"tools","tier":1,"desc_hu":"Kis, gyors PDF/EPUB/DjVu olvasó Windowsra, telepítés nélkül.","lang":"multi","access":"free","license":"GPLv3","bytes_est":20000000,"size_human":"~20 MB","size_status":"estimated","format":"exe","info_url":"https://www.sumatrapdfreader.org/download-free-pdf-viewer","download":{"method":"manual","note":"64-bit portable .zip a letöltési oldalról"},"url_status":"200 verified 2026-11-14","scores":{"S":3,"R":4,"A":8,"U":4,"Q":9,"O":10}}
{"id":"kx-lowtech","name":"solar.lowtechmagazine.com_mul_all_2025-01","cat":"appropriate_tech","tier":2,"desc_hu":"Low-tech Magazine: áram nélküli és régi technológiák, energiatakarékos megoldások.","lang":"en","access":"free","license":"CC-BY-SA / közkincs (ZIM metaadat)","bytes":700556288,"size_human":"700.56 MB","size_status":"measured:2026-11-14:kiwix-opds","format":"zim","download":{"method":"kiwix","book":"solar.lowtechmagazine.com_mul_all","flavour":null,"url":"https://lb.download.kiwix.org/zim/zimit/solar.lowtechmagazine.com_mul_all_2025-01.zim"},"url_status":"200 verified 2026-11-14","scores":{"S":4,"R":7,"A":5,"U":7,"Q":7,"O":9},"requires":["tool-kiwix"]}
{"id":"kx-lt-chem","name":"libretexts.org_en_chem_2025-01","cat":"chemistry","tier":2,"desc_hu":"LibreTexts kémia tankönyvek (általános, szerves, analitikai, ipari).","lang":"en","access":"free","license":"CC-BY-SA / közkincs (ZIM metaadat)","bytes":2182917120,"size_human":"2.18 GB","size_status":"measured:2026-11-14:kiwix-opds","format":"zim","download":{"method":"kiwix","book":"libretexts.org_en_chem","flavour":null,"url":"https://lb.download.kiwix.org/zim/libretexts/libretexts.org_en_chem_2025-01.zim"},"url_status":"200 verified 2026-11-14","scores":{"S":4,"R":9,"A":5,"U":6,"Q":9,"O":9},"requires":["tool-kiwix"]}
{"id":"kx-se-chemistry","name":"chemistry.stackexchange.com_en_all_2026-10","cat":"chemistry","tier":2,"desc_hu":"Kémia Q&A.","lang":"en","access":"free","license":"CC-BY-SA / közkincs (ZIM metaadat)","bytes":419959808,"size_human":"419.96 MB","size_status":"measured:2026-11-14:kiwix-opds","format":"zim","download":{"method":"kiwix","book":"chemistry.stackexchange.com_en_all","flavour":null,"url":"https://lb.download.kiwix.org/zim/stack_exchange/chemistry.stackexchange.com_en_all_2026-10.zim"},"url_status":"200 verified 2026-11-14","scores":{"S":3,"R":7,"A":6,"U":5,"Q":7,"O":9},"requires":["tool-kiwix"]}
{"id":"kx-wp-en-chem","name":"wikipedia_en_chemistry_maxi_2026-10","cat":"chemistry","tier":2,"desc_hu":"Wikipedia kémia-tematikus részhalmaz (kis tárhelyre).","lang":"en","access":"free","license":"CC-BY-SA / közkincs (ZIM metaadat)","bytes":383968256,"size_human":"383.97 MB","size_status":"measured:2026-11-14:kiwix-opds","format":"zim","download":{"method":"kiwix","book":"wikipedia_en_chemistry","flavour":"maxi","url":"https://lb.download.kiwix.org/zim/wikipedia/wikipedia_en_chemistry_maxi_2026-10.zim"},"url_status":"200 verified 2026-11-14","scores":{"S":3,"R":7,"A":3,"U":3,"Q":7,"O":9},"requires":["tool-kiwix"],"subsumed_by":["kx-wp-en-maxi","kx-wp-en-nopic"]}
{"id":"kx-se-ham","name":"ham.stackexchange.com_en_all_2026-10","cat":"communications","tier":2,"desc_hu":"Rádióamatőr Q&A: antennák, adó-vevők, terjedés.","lang":"en","access":"free","license":"CC-BY-SA / közkincs (ZIM metaadat)","bytes":77109248,"size_human":"77.11 MB","size_status":"measured:2026-11-14:kiwix-opds","format":"zim","download":{"method":"kiwix","book":"ham.stackexchange.com_en_all","flavour":null,"url":"https://lb.download.kiwix.org/zim/stack_exchange/ham.stackexchange.com_en_all_2026-10.zim"},"url_status":"200 verified 2026-11-14","scores":{"S":5,"R":6,"A":7,"U":7,"Q":7,"O":9},"requires":["tool-kiwix"]}
{"id":"kx-archwiki","name":"archlinux_en_all_maxi_2026-10","cat":"computing","tier":2,"desc_hu":"ArchWiki: a legjobb Linux-rendszergazda tudásbázis.","lang":"en","access":"free","license":"CC-BY-SA / közkincs (ZIM metaadat)","bytes":38311936,"size_human":"38.31 MB","size_status":"measured:2026-11-14:kiwix-opds","format":"zim","download":{"method":"kiwix","book":"archlinux_en_all","flavour":"maxi","url":"https://lb.download.kiwix.org/zim/other/archlinux_en_all_maxi_2026-10.zim"},"url_status":"200 verified 2026-11-14","scores":{"S":1,"R":7,"A":8,"U":6,"Q":8,"O":9},"requires":["tool-kiwix"]}
{"id":"kx-se-electronics","name":"electronics.stackexchange.com_en_all_2026-10","cat":"electronics","tier":2,"desc_hu":"Elektronika Q&A: áramkörtervezés, tápegységek, javítás.","lang":"en","access":"free","license":"CC-BY-SA / közkincs (ZIM metaadat)","bytes":4261398528,"size_human":"4.26 GB","size_status":"measured:2026-11-14:kiwix-opds","format":"zim","download":{"method":"kiwix","book":"electronics.stackexchange.com_en_all","flavour":null,"url":"https://lb.download.kiwix.org/zim/stack_exchange/electronics.stackexchange.com_en_all_2026-10.zim"},"url_status":"200 verified 2026-11-14","scores":{"S":3,"R":8,"A":8,"U":7,"Q":7,"O":9},"requires":["tool-kiwix"]}
{"id":"kx-lt-eng","name":"libretexts.org_en_eng_2025-01","cat":"engineering","tier":2,"desc_hu":"LibreTexts mérnöki tankönyvek (gépész, villamos, építő, anyagtudomány).","lang":"en","access":"free","license":"CC-BY-SA / közkincs (ZIM metaadat)","bytes":678394880,"size_human":"678.39 MB","size_status":"measured:2026-11-14:kiwix-opds","format":"zim","download":{"method":"kiwix","book":"libretexts.org_en_eng","flavour":null,"url":"https://lb.download.kiwix.org/zim/libretexts/libretexts.org_en_eng_2025-01.zim"},"url_status":"200 verified 2026-11-14","scores":{"S":4,"R":9,"A":6,"U":7,"Q":9,"O":9},"requires":["tool-kiwix"]}
{"id":"kx-se-engineering","name":"engineering.stackexchange.com_en_all_2026-10","cat":"engineering","tier":2,"desc_hu":"Mérnöki Q&A.","lang":"en","access":"free","license":"CC-BY-SA / közkincs (ZIM metaadat)","bytes":258556928,"size_human":"258.56 MB","size_status":"measured:2026-11-14:kiwix-opds","format":"zim","download":{"method":"kiwix","book":"engineering.stackexchange.com_en_all","flavour":null,"url":"https://lb.download.kiwix.org/zim/stack_exchange/engineering.stackexchange.com_en_all_2026-10.zim"},"url_status":"200 verified 2026-11-14","scores":{"S":3,"R":7,"A":6,"U":5,"Q":7,"O":9},"requires":["tool-kiwix"]}
{"id":"kx-se-cooking","name":"cooking.stackexchange.com_en_all_2026-10","cat":"food","tier":2,"desc_hu":"Főzés és élelmiszerbiztonság Q&A.","lang":"en","access":"free","license":"CC-BY-SA / közkincs (ZIM metaadat)","bytes":238098432,"size_human":"238.10 MB","size_status":"measured:2026-11-14:kiwix-opds","format":"zim","download":{"method":"kiwix","book":"cooking.stackexchange.com_en_all","flavour":null,"url":"https://lb.download.kiwix.org/zim/stack_exchange/cooking.stackexchange.com_en_all_2026-10.zim"},"url_status":"200 verified 2026-11-14","scores":{"S":5,"R":3,"A":8,"U":4,"Q":7,"O":9},"requires":["tool-kiwix"]}
{"id":"kx-wikibooks-hu","name":"wikibooks_hu_all_maxi_2026-10","cat":"hungarian","tier":2,"desc_hu":"Magyar Wikikönyvek.","lang":"hu","access":"free","license":"CC-BY-SA / közkincs (ZIM metaadat)","bytes":471053312,"size_human":"471.05 MB","size_status":"measured:2026-11-14:kiwix-opds","format":"zim","download":{"method":"kiwix","book":"wikibooks_hu_all","flavour":"maxi","url":"https://lb.download.kiwix.org/zim/wikibooks/wikibooks_hu_all_maxi_2026-10.zim"},"url_status":"200 verified 2026-11-14","scores":{"S":3,"R":6,"A":6,"U":6,"Q":6,"O":9},"requires":["tool-kiwix"]}
{"id":"kx-wiktionary-hu","name":"wiktionary_hu_all_nopic_2026-10","cat":"hungarian","tier":2,"desc_hu":"Magyar Wikiszótár (fordításokkal) – idegen nyelvű anyagok értelmezéséhez.","lang":"hu","access":"free","license":"CC-BY-SA / közkincs (ZIM metaadat)","bytes":786565120,"size_human":"786.57 MB","size_status":"measured:2026-11-14:kiwix-opds","format":"zim","download":{"method":"kiwix","book":"wiktionary_hu_all","flavour":"nopic","url":"https://lb.download.kiwix.org/zim/wiktionary/wiktionary_hu_all_nopic_2026-10.zim"},"url_status":"200 verified 2026-11-14","scores":{"S":2,"R":6,"A":3,"U":6,"Q":7,"O":9},"requires":["tool-kiwix"]}
{"id":"kx-se-woodworking","name":"woodworking.stackexchange.com_en_all_2026-10","cat":"manufacturing","tier":2,"desc_hu":"Famegmunkálás Q&A.","lang":"en","access":"free","license":"CC-BY-SA / közkincs (ZIM metaadat)","bytes":106657792,"size_human":"106.66 MB","size_status":"measured:2026-11-14:kiwix-opds","format":"zim","download":{"method":"kiwix","book":"woodworking.stackexchange.com_en_all","flavour":null,"url":"https://lb.download.kiwix.org/zim/stack_exchange/woodworking.stackexchange.com_en_all_2026-10.zim"},"url_status":"200 verified 2026-11-14","scores":{"S":3,"R":6,"A":8,"U":5,"Q":7,"O":9},"requires":["tool-kiwix"]}
{"id":"kx-qg-medicine","name":"quickguidesformedicine_en_all_2026-06","cat":"medicine","tier":2,"desc_hu":"Orvosi gyorsreferencia videók (videólejátszás kell).","lang":"en","access":"free","license":"CC-BY-SA / közkincs (ZIM metaadat)","bytes":527712256,"size_human":"527.71 MB","size_status":"measured:2026-11-14:kiwix-opds","format":"zim","download":{"method":"kiwix","book":"quickguidesformedicine_en_all","flavour":null,"url":"https://lb.download.kiwix.org/zim/videos/quickguidesformedicine_en_all_2026-06.zim"},"url_status":"200 verified 2026-11-14","scores":{"S":6,"R":4,"A":7,"U":5,"Q":7,"O":6},"requires":["tool-kiwix"]}
{"id":"kx-se-medsci","name":"medicalsciences.stackexchange.com_en_all_2026-10","cat":"medicine","tier":2,"desc_hu":"Orvostudomány Q&A.","lang":"en","access":"free","license":"CC-BY-SA / közkincs (ZIM metaadat)","bytes":60660736,"size_human":"60.66 MB","size_status":"measured:2026-11-14:kiwix-opds","format":"zim","download":{"method":"kiwix","book":"medicalsciences.stackexchange.com_en_all","flavour":null,"url":"https://lb.download.kiwix.org/zim/stack_exchange/medicalsciences.stackexchange.com_en_all_2026-10.zim"},"url_status":"200 verified 2026-11-14","scores":{"S":5,"R":4,"A":4,"U":4,"Q":6,"O":9},"requires":["tool-kiwix"]}
{"id":"kx-wikibooks-en","name":"wikibooks_en_all_maxi_2026-10","cat":"reference","tier":2,"desc_hu":"Wikibooks: nyílt tankönyvek és kézikönyvek (kémia, elektronika, programozás, főzés).","lang":"en","access":"free","license":"CC-BY-SA / közkincs (ZIM metaadat)","bytes":4739740672,"size_human":"4.74 GB","size_status":"measured:2026-11-14:kiwix-opds","format":"zim","download":{"method":"kiwix","book":"wikibooks_en_all","flavour":"maxi","url":"https://lb.download.kiwix.org/zim/wikibooks/wikibooks_en_all_maxi_2026-10.zim"},"url_status":"200 verified 2026-11-14","scores":{"S":4,"R":8,"A":7,"U":7,"Q":6,"O":9},"requires":["tool-kiwix"]}
{"id":"kx-se-bicycles","name":"bicycles.stackexchange.com_en_all_2026-10","cat":"repair","tier":2,"desc_hu":"Kerékpár-javítás Q&A (áram nélküli közlekedés).","lang":"en","access":"free","license":"CC-BY-SA / közkincs (ZIM metaadat)","bytes":499255296,"size_human":"499.26 MB","size_status":"measured:2026-11-14:kiwix-opds","format":"zim","download":{"method":"kiwix","book":"bicycles.stackexchange.com_en_all","flavour":null,"url":"https://lb.download.kiwix.org/zim/stack_exchange/bicycles.stackexchange.com_en_all_2026-10.zim"},"url_status":"200 verified 2026-11-14","scores":{"S":4,"R":4,"A":8,"U":5,"Q":7,"O":9},"requires":["tool-kiwix"]}
{"id":"kx-se-mechanics","name":"mechanics.stackexchange.com_en_all_2026-10","cat":"repair","tier":2,"desc_hu":"Gépjármű-javítás Q&A.","lang":"en","access":"free","license":"CC-BY-SA / közkincs (ZIM metaadat)","bytes":341672960,"size_human":"341.67 MB","size_status":"measured:2026-11-14:kiwix-opds","format":"zim","download":{"method":"kiwix","book":"mechanics.stackexchange.com_en_all","flavour":null,"url":"https://lb.download.kiwix.org/zim/stack_exchange/mechanics.stackexchange.com_en_all_2026-10.zim"},"url_status":"200 verified 2026-11-14","scores":{"S":4,"R":6,"A":8,"U":6,"Q":7,"O":9},"requires":["tool-kiwix"]}
{"id":"kx-lt-bio","name":"libretexts.org_en_bio_2025-01","cat":"science","tier":2,"desc_hu":"LibreTexts biológia (mikrobiológia, genetika, ökológia, botanika).","lang":"en","access":"free","license":"CC-BY-SA / közkincs (ZIM metaadat)","bytes":2240947200,"size_human":"2.24 GB","size_status":"measured:2026-11-14:kiwix-opds","format":"zim","download":{"method":"kiwix","book":"libretexts.org_en_bio","flavour":null,"url":"https://lb.download.kiwix.org/zim/libretexts/libretexts.org_en_bio_2025-01.zim"},"url_status":"200 verified 2026-11-14","scores":{"S":4,"R":8,"A":5,"U":6,"Q":9,"O":9},"requires":["tool-kiwix"]}
{"id":"kx-lt-math","name":"libretexts.org_en_math_2026-01","cat":"science","tier":2,"desc_hu":"LibreTexts matematika (algebra, analízis, lineáris algebra).","lang":"en","access":"free","license":"CC-BY-SA / közkincs (ZIM metaadat)","bytes":830646272,"size_human":"830.65 MB","size_status":"measured:2026-11-14:kiwix-opds","format":"zim","download":{"method":"kiwix","book":"libretexts.org_en_math","flavour":null,"url":"https://lb.download.kiwix.org/zim/libretexts/libretexts.org_en_math_2026-01.zim"},"url_status":"200 verified 2026-11-14","scores":{"S":2,"R":8,"A":5,"U":5,"Q":9,"O":9},"requires":["tool-kiwix"]}
{"id":"kx-lt-phys","name":"libretexts.org_en_phys_2026-01","cat":"science","tier":2,"desc_hu":"LibreTexts fizika tankönyvek.","lang":"en","access":"free","license":"CC-BY-SA / közkincs (ZIM metaadat)","bytes":559554560,"size_human":"559.55 MB","size_status":"measured:2026-11-14:kiwix-opds","format":"zim","download":{"method":"kiwix","book":"libretexts.org_en_phys","flavour":null,"url":"https://lb.download.kiwix.org/zim/libretexts/libretexts.org_en_phys_2026-01.zim"},"url_status":"200 verified 2026-11-14","scores":{"S":3,"R":9,"A":5,"U":5,"Q":9,"O":9},"requires":["tool-kiwix"]}
{"id":"kx-learn-self-reliance","name":"lrnselfreliance_en_all_2026-09","cat":"survival","tier":2,"desc_hu":"Learn Self Reliance videócsatorna: önellátás, tartósítás, kézművesség (videó).","lang":"en","access":"free","license":"CC-BY-SA / közkincs (ZIM metaadat)","bytes":3974044672,"size_human":"3.97 GB","size_status":"measured:2026-11-14:kiwix-opds","format":"zim","download":{"method":"kiwix","book":"lrnselfreliance_en_all","flavour":null,"url":"https://lb.download.kiwix.org/zim/videos/lrnselfreliance_en_all_2026-09.zim"},"url_status":"200 verified 2026-11-14","scores":{"S":7,"R":4,"A":8,"U":5,"Q":5,"O":6},"requires":["tool-kiwix"]}
{"id":"kx-se-outdoors","name":"outdoors.stackexchange.com_en_all_2026-10","cat":"survival","tier":2,"desc_hu":"Szabadtéri túlélés, túrázás Q&A.","lang":"en","access":"free","license":"CC-BY-SA / közkincs (ZIM metaadat)","bytes":141820928,"size_human":"141.82 MB","size_status":"measured:2026-11-14:kiwix-opds","format":"zim","download":{"method":"kiwix","book":"outdoors.stackexchange.com_en_all","flavour":null,"url":"https://lb.download.kiwix.org/zim/stack_exchange/outdoors.stackexchange.com_en_all_2026-10.zim"},"url_status":"200 verified 2026-11-14","scores":{"S":6,"R":2,"A":7,"U":4,"Q":7,"O":9},"requires":["tool-kiwix"]}
{"id":"tool-calibre","name":"Calibre e-könyv kezelő","cat":"tools","tier":2,"desc_hu":"E-könyv-könyvtár kezelése, konvertálás (EPUB/MOBI/PDF), keresés nagy gyűjteményekben.","lang":"multi","access":"free","license":"GPLv3","bytes_est":600000000,"size_human":"~600 MB (Win+Mac+Linux)","size_status":"estimated","format":"installer","info_url":"https://calibre-ebook.com/download","download":{"method":"manual","note":"https://download.calibre-ebook.com/ → aktuális verzió könyvtára"},"url_status":"200 verified 2026-11-14","scores":{"S":1,"R":5,"A":6,"U":5,"Q":9,"O":8}}
{"id":"tool-ollama-installers","name":"Ollama telepítők (Windows, macOS, Linux install.sh)","cat":"tools","tier":2,"desc_hu":"Egyszerű helyi LLM-futtató. A telepítőket internet nélküli újratelepítéshez mentsd el.","lang":"multi","access":"free","license":"MIT","bytes":2087676234,"size_human":"2.09 GB","size_status":"measured:2026-11-14:content-length","format":"exe/dmg/sh","info_url":"https://ollama.com/download","download":{"method":"http","urls":["https://ollama.com/download/OllamaSetup.exe","https://ollama.com/download/Ollama.dmg","https://ollama.com/install.sh"]},"url_status":"200 verified 2026-11-14","scores":{"S":3,"R":7,"A":8,"U":5,"Q":8,"O":7},"notes":"Linuxon az install.sh letölt: offline telepítéshez a ollama-linux-amd64.tgz kell a GitHub releases oldalról (github.com/ollama/ollama/releases/latest).","hw_note":"LLM-ek nélkül felesleges"}
{"id":"kx-se-sustainability","name":"sustainability.stackexchange.com_en_all_2026-10","cat":"appropriate_tech","tier":3,"desc_hu":"Fenntarthatóság Q&A.","lang":"en","access":"free","license":"CC-BY-SA / közkincs (ZIM metaadat)","bytes":27687936,"size_human":"27.69 MB","size_status":"measured:2026-11-14:kiwix-opds","format":"zim","download":{"method":"kiwix","book":"sustainability.stackexchange.com_en_all","flavour":null,"url":"https://lb.download.kiwix.org/zim/stack_exchange/sustainability.stackexchange.com_en_all_2026-10.zim"},"url_status":"200 verified 2026-11-14","scores":{"S":3,"R":4,"A":4,"U":4,"Q":6,"O":9},"requires":["tool-kiwix"]}
{"id":"kx-python-docs","name":"docs.python.org_en_all_2026-08a","cat":"computing","tier":3,"desc_hu":"Hivatalos Python dokumentáció.","lang":"en","access":"free","license":"CC-BY-SA / közkincs (ZIM metaadat)","bytes":3959219200,"size_human":"3.96 GB","size_status":"measured:2026-11-14:kiwix-opds","format":"zim","download":{"method":"kiwix","book":"docs.python.org_en_all","flavour":null,"url":"https://lb.download.kiwix.org/zim/zimit/docs.python.org_en_all_2026-08a.zim"},"url_status":"200 verified 2026-11-14","scores":{"S":1,"R":7,"A":7,"U":6,"Q":9,"O":9},"requires":["tool-kiwix"]}
{"id":"kx-se-askubuntu","name":"askubuntu.com_en_all_2026-10","cat":"computing","tier":3,"desc_hu":"Ubuntu/Linux Q&A.","lang":"en","access":"free","license":"CC-BY-SA / közkincs (ZIM metaadat)","bytes":2767228928,"size_human":"2.77 GB","size_status":"measured:2026-11-14:kiwix-opds","format":"zim","download":{"method":"kiwix","book":"askubuntu.com_en_all","flavour":null,"url":"https://lb.download.kiwix.org/zim/stack_exchange/askubuntu.com_en_all_2026-10.zim"},"url_status":"200 verified 2026-11-14","scores":{"S":1,"R":6,"A":7,"U":5,"Q":7,"O":9},"requires":["tool-kiwix"]}
{"id":"kx-se-unix","name":"unix.stackexchange.com_en_all_2026-10","cat":"computing","tier":3,"desc_hu":"Unix/Linux shell és rendszer Q&A.","lang":"en","access":"free","license":"CC-BY-SA / közkincs (ZIM metaadat)","bytes":1316253696,"size_human":"1.32 GB","size_status":"measured:2026-11-14:kiwix-opds","format":"zim","download":{"method":"kiwix","book":"unix.stackexchange.com_en_all","flavour":null,"url":"https://lb.download.kiwix.org/zim/stack_exchange/unix.stackexchange.com_en_all_2026-10.zim"},"url_status":"200 verified 2026-11-14","scores":{"S":1,"R":7,"A":7,"U":6,"Q":7,"O":9},"requires":["tool-kiwix"]}
{"id":"kx-wp-en-computer","name":"wikipedia_en_computer_maxi_2026-09","cat":"computing","tier":3,"desc_hu":"Wikipedia számítástechnika részhalmaz.","lang":"en","access":"free","license":"CC-BY-SA / közkincs (ZIM metaadat)","bytes":910010368,"size_human":"910.01 MB","size_status":"measured:2026-11-14:kiwix-opds","format":"zim","download":{"method":"kiwix","book":"wikipedia_en_computer","flavour":"maxi","url":"https://lb.download.kiwix.org/zim/wikipedia/wikipedia_en_computer_maxi_2026-09.zim"},"url_status":"200 verified 2026-11-14","scores":{"S":1,"R":6,"A":3,"U":3,"Q":7,"O":9},"requires":["tool-kiwix"],"subsumed_by":["kx-wp-en-maxi","kx-wp-en-nopic"]}
{"id":"kx-lt-k12","name":"libretexts.org_en_k12_2026-01","cat":"education","tier":3,"desc_hu":"LibreTexts közoktatási anyagok.","lang":"en","access":"free","license":"CC-BY-SA / közkincs (ZIM metaadat)","bytes":369809408,"size_human":"369.81 MB","size_status":"measured:2026-11-14:kiwix-opds","format":"zim","download":{"method":"kiwix","book":"libretexts.org_en_k12","flavour":null,"url":"https://lb.download.kiwix.org/zim/libretexts/libretexts.org_en_k12_2026-01.zim"},"url_status":"200 verified 2026-11-14","scores":{"S":2,"R":6,"A":5,"U":5,"Q":9,"O":9},"requires":["tool-kiwix"]}
{"id":"kx-phet-hu","name":"phet_hu_all_2026-08","cat":"education","tier":3,"desc_hu":"PhET interaktív fizika/kémia szimulációk magyarul (böngésző + JS kell).","lang":"hu","access":"free","license":"CC-BY-SA / közkincs (ZIM metaadat)","bytes":96038912,"size_human":"96.04 MB","size_status":"measured:2026-11-14:kiwix-opds","format":"zim","download":{"method":"kiwix","book":"phet_hu_all","flavour":null,"url":"https://lb.download.kiwix.org/zim/phet/phet_hu_all_2026-08.zim"},"url_status":"200 verified 2026-11-14","scores":{"S":1,"R":6,"A":5,"U":6,"Q":9,"O":7},"requires":["tool-kiwix"]}
{"id":"kx-wikiversity","name":"wikiversity_en_all_maxi_2026-11","cat":"education","tier":3,"desc_hu":"Wikiversity kurzusok.","lang":"en","access":"free","license":"CC-BY-SA / közkincs (ZIM metaadat)","bytes":2110168064,"size_human":"2.11 GB","size_status":"measured:2026-11-14:kiwix-opds","format":"zim","download":{"method":"kiwix","book":"wikiversity_en_all","flavour":"maxi","url":"https://lb.download.kiwix.org/zim/wikiversity/wikiversity_en_all_maxi_2026-11.zim"},"url_status":"200 verified 2026-11-14","scores":{"S":3,"R":6,"A":5,"U":5,"Q":5,"O":9},"requires":["tool-kiwix"]}
{"id":"kx-wp-simple","name":"wikipedia_en-simple_all_maxi_2026-09","cat":"education","tier":3,"desc_hu":"Simple English Wikipedia – egyszerű angol, tanuláshoz/gyerekeknek.","lang":"en","access":"free","license":"CC-BY-SA / közkincs (ZIM metaadat)","bytes":3121061888,"size_human":"3.12 GB","size_status":"measured:2026-11-14:kiwix-opds","format":"zim","download":{"method":"kiwix","book":"wikipedia_en-simple_all","flavour":"maxi","url":"https://lb.download.kiwix.org/zim/wikipedia/wikipedia_en-simple_all_maxi_2026-09.zim"},"url_status":"200 verified 2026-11-14","scores":{"S":3,"R":5,"A":3,"U":4,"Q":8,"O":9},"requires":["tool-kiwix"]}
{"id":"kx-se-arduino","name":"arduino.stackexchange.com_en_all_2026-10","cat":"electronics","tier":3,"desc_hu":"Arduino/mikrokontroller Q&A.","lang":"en","access":"free","license":"CC-BY-SA / közkincs (ZIM metaadat)","bytes":259577856,"size_human":"259.58 MB","size_status":"measured:2026-11-14:kiwix-opds","format":"zim","download":{"method":"kiwix","book":"arduino.stackexchange.com_en_all","flavour":null,"url":"https://lb.download.kiwix.org/zim/stack_exchange/arduino.stackexchange.com_en_all_2026-10.zim"},"url_status":"200 verified 2026-11-14","scores":{"S":1,"R":6,"A":7,"U":5,"Q":7,"O":9},"requires":["tool-kiwix"]}
{"id":"kx-se-homebrew","name":"homebrew.stackexchange.com_en_all_2026-10","cat":"food","tier":3,"desc_hu":"Erjesztés, sörfőzés (fertőtlenítő alkohol, tartósítás) Q&A.","lang":"en","access":"free","license":"CC-BY-SA / közkincs (ZIM metaadat)","bytes":37374976,"size_human":"37.37 MB","size_status":"measured:2026-11-14:kiwix-opds","format":"zim","download":{"method":"kiwix","book":"homebrew.stackexchange.com_en_all","flavour":null,"url":"https://lb.download.kiwix.org/zim/stack_exchange/homebrew.stackexchange.com_en_all_2026-10.zim"},"url_status":"200 verified 2026-11-14","scores":{"S":3,"R":3,"A":7,"U":5,"Q":7,"O":9},"requires":["tool-kiwix"]}
{"id":"kx-wp-en-history","name":"wikipedia_en_history_maxi_2026-10","cat":"humanities","tier":3,"desc_hu":"Wikipedia történelem részhalmaz.","lang":"en","access":"free","license":"CC-BY-SA / közkincs (ZIM metaadat)","bytes":1991294976,"size_human":"1.99 GB","size_status":"measured:2026-11-14:kiwix-opds","format":"zim","download":{"method":"kiwix","book":"wikipedia_en_history","flavour":"maxi","url":"https://lb.download.kiwix.org/zim/wikipedia/wikipedia_en_history_maxi_2026-10.zim"},"url_status":"200 verified 2026-11-14","scores":{"S":1,"R":5,"A":2,"U":3,"Q":7,"O":9},"requires":["tool-kiwix"],"subsumed_by":["kx-wp-en-maxi","kx-wp-en-nopic"]}
{"id":"kx-gutenberg-hu","name":"gutenberg_hu_all_2026-01","cat":"hungarian","tier":3,"desc_hu":"Project Gutenberg magyar nyelvű könyvei.","lang":"hu","access":"free","license":"CC-BY-SA / közkincs (ZIM metaadat)","bytes":1023427584,"size_human":"1.02 GB","size_status":"measured:2026-11-14:kiwix-opds","format":"zim","download":{"method":"kiwix","book":"gutenberg_hu_all","flavour":null,"url":"https://lb.download.kiwix.org/zim/gutenberg/gutenberg_hu_all_2026-01.zim"},"url_status":"200 verified 2026-11-14","scores":{"S":1,"R":5,"A":2,"U":5,"Q":8,"O":9},"requires":["tool-kiwix"]}
{"id":"kx-wikisource-hu","name":"wikisource_hu_all_maxi_2026-10","cat":"hungarian","tier":3,"desc_hu":"Magyar Wikiforrás.","lang":"hu","access":"free","license":"CC-BY-SA / közkincs (ZIM metaadat)","bytes":84610048,"size_human":"84.61 MB","size_status":"measured:2026-11-14:kiwix-opds","format":"zim","download":{"method":"kiwix","book":"wikisource_hu_all","flavour":"maxi","url":"https://lb.download.kiwix.org/zim/wikisource/wikisource_hu_all_maxi_2026-10.zim"},"url_status":"200 verified 2026-11-14","scores":{"S":1,"R":4,"A":2,"U":5,"Q":7,"O":9},"requires":["tool-kiwix"]}
{"id":"kx-wikisource-en-maxi","name":"wikisource_en_all_maxi_2026-09","cat":"library","tier":3,"group":"wikisource-en","variant_rank":2,"variant_role":"luxury","desc_hu":"Wikisource képekkel.","lang":"en","access":"free","license":"CC-BY-SA / közkincs (ZIM metaadat)","bytes":8615937024,"size_human":"8.62 GB","size_status":"measured:2026-11-14:kiwix-opds","format":"zim","download":{"method":"kiwix","book":"wikisource_en_all","flavour":"maxi","url":"https://lb.download.kiwix.org/zim/wikisource/wikisource_en_all_maxi_2026-09.zim"},"url_status":"200 verified 2026-11-14","scores":{"S":2,"R":6,"A":3,"U":6,"Q":7,"O":9},"requires":["tool-kiwix"]}
{"id":"kx-wikisource-en-nopic","name":"wikisource_en_all_nopic_2026-09","cat":"library","tier":3,"group":"wikisource-en","variant_rank":1,"variant_role":"pref","desc_hu":"Wikisource: közkincs szövegek (pl. 1911-es Britannica, régi szakkönyvek).","lang":"en","access":"free","license":"CC-BY-SA / közkincs (ZIM metaadat)","bytes":3905589248,"size_human":"3.91 GB","size_status":"measured:2026-11-14:kiwix-opds","format":"zim","download":{"method":"kiwix","book":"wikisource_en_all","flavour":"nopic","url":"https://lb.download.kiwix.org/zim/wikisource/wikisource_en_all_nopic_2026-09.zim"},"url_status":"200 verified 2026-11-14","scores":{"S":2,"R":6,"A":3,"U":6,"Q":7,"O":9},"requires":["tool-kiwix"]}
{"id":"kx-se-3dprint","name":"3dprinting.stackexchange.com_en_all_2026-10","cat":"manufacturing","tier":3,"desc_hu":"3D-nyomtatás Q&A.","lang":"en","access":"free","license":"CC-BY-SA / közkincs (ZIM metaadat)","bytes":120338432,"size_human":"120.34 MB","size_status":"measured:2026-11-14:kiwix-opds","format":"zim","download":{"method":"kiwix","book":"3dprinting.stackexchange.com_en_all","flavour":null,"url":"https://lb.download.kiwix.org/zim/stack_exchange/3dprinting.stackexchange.com_en_all_2026-10.zim"},"url_status":"200 verified 2026-11-14","scores":{"S":1,"R":5,"A":7,"U":5,"Q":7,"O":9},"requires":["tool-kiwix"]}
{"id":"kx-wiktionary-en","name":"wiktionary_en_all_nopic_2026-11","cat":"reference","tier":3,"desc_hu":"Angol Wiktionary (többnyelvű szótár).","lang":"en","access":"free","license":"CC-BY-SA / közkincs (ZIM metaadat)","bytes":14847562752,"size_human":"14.85 GB","size_status":"measured:2026-11-14:kiwix-opds","format":"zim","download":{"method":"kiwix","book":"wiktionary_en_all","flavour":"nopic","url":"https://lb.download.kiwix.org/zim/wiktionary/wiktionary_en_all_nopic_2026-11.zim"},"url_status":"200 verified 2026-11-14","scores":{"S":2,"R":6,"A":2,"U":6,"Q":7,"O":9},"requires":["tool-kiwix"]}
{"id":"kx-wp-en-geo","name":"wikipedia_en_geography_maxi_2026-10","cat":"reference","tier":3,"desc_hu":"Wikipedia földrajz részhalmaz.","lang":"en","access":"free","license":"CC-BY-SA / közkincs (ZIM metaadat)","bytes":1232519168,"size_human":"1.23 GB","size_status":"measured:2026-11-14:kiwix-opds","format":"zim","download":{"method":"kiwix","book":"wikipedia_en_geography","flavour":"maxi","url":"https://lb.download.kiwix.org/zim/wikipedia/wikipedia_en_geography_maxi_2026-10.zim"},"url_status":"200 verified 2026-11-14","scores":{"S":3,"R":5,"A":3,"U":3,"Q":7,"O":9},"requires":["tool-kiwix"],"subsumed_by":["kx-wp-en-maxi","kx-wp-en-nopic"]}
{"id":"kx-lt-geo","name":"libretexts.org_en_geo_2026-01","cat":"science","tier":3,"desc_hu":"LibreTexts földtudományok (geológia, talajtan, meteorológia).","lang":"en","access":"free","license":"CC-BY-SA / közkincs (ZIM metaadat)","bytes":1188117504,"size_human":"1.19 GB","size_status":"measured:2026-11-14:kiwix-opds","format":"zim","download":{"method":"kiwix","book":"libretexts.org_en_geo","flavour":null,"url":"https://lb.download.kiwix.org/zim/libretexts/libretexts.org_en_geo_2026-01.zim"},"url_status":"200 verified 2026-11-14","scores":{"S":3,"R":6,"A":4,"U":5,"Q":9,"O":9},"requires":["tool-kiwix"]}
{"id":"kx-lt-stats","name":"libretexts.org_en_stats_2026-01","cat":"science","tier":3,"desc_hu":"LibreTexts statisztika.","lang":"en","access":"free","license":"CC-BY-SA / közkincs (ZIM metaadat)","bytes":215779328,"size_human":"215.78 MB","size_status":"measured:2026-11-14:kiwix-opds","format":"zim","download":{"method":"kiwix","book":"libretexts.org_en_stats","flavour":null,"url":"https://lb.download.kiwix.org/zim/libretexts/libretexts.org_en_stats_2026-01.zim"},"url_status":"200 verified 2026-11-14","scores":{"S":1,"R":6,"A":5,"U":4,"Q":9,"O":9},"requires":["tool-kiwix"]}
{"id":"kx-se-biology","name":"biology.stackexchange.com_en_all_2026-10","cat":"science","tier":3,"desc_hu":"Biológia Q&A.","lang":"en","access":"free","license":"CC-BY-SA / közkincs (ZIM metaadat)","bytes":425074688,"size_human":"425.07 MB","size_status":"measured:2026-11-14:kiwix-opds","format":"zim","download":{"method":"kiwix","book":"biology.stackexchange.com_en_all","flavour":null,"url":"https://lb.download.kiwix.org/zim/stack_exchange/biology.stackexchange.com_en_all_2026-10.zim"},"url_status":"200 verified 2026-11-14","scores":{"S":3,"R":5,"A":4,"U":4,"Q":7,"O":9},"requires":["tool-kiwix"]}
{"id":"kx-se-earthsci","name":"earthscience.stackexchange.com_en_all_2026-10","cat":"science","tier":3,"desc_hu":"Földtudomány Q&A.","lang":"en","access":"free","license":"CC-BY-SA / közkincs (ZIM metaadat)","bytes":132909056,"size_human":"132.91 MB","size_status":"measured:2026-11-14:kiwix-opds","format":"zim","download":{"method":"kiwix","book":"earthscience.stackexchange.com_en_all","flavour":null,"url":"https://lb.download.kiwix.org/zim/stack_exchange/earthscience.stackexchange.com_en_all_2026-10.zim"},"url_status":"200 verified 2026-11-14","scores":{"S":2,"R":5,"A":4,"U":4,"Q":7,"O":9},"requires":["tool-kiwix"]}
{"id":"kx-se-physics","name":"physics.stackexchange.com_en_all_2026-10","cat":"science","tier":3,"desc_hu":"Fizika Q&A.","lang":"en","access":"free","license":"CC-BY-SA / közkincs (ZIM metaadat)","bytes":1839301632,"size_human":"1.84 GB","size_status":"measured:2026-11-14:kiwix-opds","format":"zim","download":{"method":"kiwix","book":"physics.stackexchange.com_en_all","flavour":null,"url":"https://lb.download.kiwix.org/zim/stack_exchange/physics.stackexchange.com_en_all_2026-10.zim"},"url_status":"200 verified 2026-11-14","scores":{"S":2,"R":7,"A":5,"U":5,"Q":7,"O":9},"requires":["tool-kiwix"]}
{"id":"kx-wp-en-math","name":"wikipedia_en_mathematics_maxi_2026-09","cat":"science","tier":3,"desc_hu":"Wikipedia matematika részhalmaz.","lang":"en","access":"free","license":"CC-BY-SA / közkincs (ZIM metaadat)","bytes":996188160,"size_human":"996.19 MB","size_status":"measured:2026-11-14:kiwix-opds","format":"zim","download":{"method":"kiwix","book":"wikipedia_en_mathematics","flavour":"maxi","url":"https://lb.download.kiwix.org/zim/wikipedia/wikipedia_en_mathematics_maxi_2026-09.zim"},"url_status":"200 verified 2026-11-14","scores":{"S":1,"R":6,"A":3,"U":3,"Q":7,"O":9},"requires":["tool-kiwix"],"subsumed_by":["kx-wp-en-maxi","kx-wp-en-nopic"]}
{"id":"kx-wp-en-molcell","name":"wikipedia_en_molcell_maxi_2026-10","cat":"science","tier":3,"desc_hu":"Wikipedia molekuláris és sejtbiológia részhalmaz.","lang":"en","access":"free","license":"CC-BY-SA / közkincs (ZIM metaadat)","bytes":728293376,"size_human":"728.29 MB","size_status":"measured:2026-11-14:kiwix-opds","format":"zim","download":{"method":"kiwix","book":"wikipedia_en_molcell","flavour":"maxi","url":"https://lb.download.kiwix.org/zim/wikipedia/wikipedia_en_molcell_maxi_2026-10.zim"},"url_status":"200 verified 2026-11-14","scores":{"S":2,"R":6,"A":3,"U":3,"Q":7,"O":9},"requires":["tool-kiwix"],"subsumed_by":["kx-wp-en-maxi","kx-wp-en-nopic"]}
{"id":"kx-wp-en-phys","name":"wikipedia_en_physics_maxi_2026-10","cat":"science","tier":3,"desc_hu":"Wikipedia fizika részhalmaz.","lang":"en","access":"free","license":"CC-BY-SA / közkincs (ZIM metaadat)","bytes":911983616,"size_human":"911.98 MB","size_status":"measured:2026-11-14:kiwix-opds","format":"zim","download":{"method":"kiwix","book":"wikipedia_en_physics","flavour":"maxi","url":"https://lb.download.kiwix.org/zim/wikipedia/wikipedia_en_physics_maxi_2026-10.zim"},"url_status":"200 verified 2026-11-14","scores":{"S":2,"R":7,"A":3,"U":3,"Q":7,"O":9},"requires":["tool-kiwix"],"subsumed_by":["kx-wp-en-maxi","kx-wp-en-nopic"]}
{"id":"kx-urban-prepper","name":"urban-prepper_en_all_2026-08","cat":"survival","tier":3,"desc_hu":"Urban Prepper videócsatorna (felkészülés, felszerelés; videó).","lang":"en","access":"free","license":"CC-BY-SA / közkincs (ZIM metaadat)","bytes":2245235712,"size_human":"2.25 GB","size_status":"measured:2026-11-14:kiwix-opds","format":"zim","download":{"method":"kiwix","book":"urban-prepper_en_all","flavour":null,"url":"https://lb.download.kiwix.org/zim/videos/urban-prepper_en_all_2026-08.zim"},"url_status":"200 verified 2026-11-14","scores":{"S":6,"R":2,"A":7,"U":4,"Q":4,"O":6},"requires":["tool-kiwix"]}
{"id":"kx-se-superuser","name":"superuser.com_en_all_2026-10","cat":"computing","tier":4,"desc_hu":"Számítógép-használat Q&A.","lang":"en","access":"free","license":"CC-BY-SA / közkincs (ZIM metaadat)","bytes":4014454784,"size_human":"4.01 GB","size_status":"measured:2026-11-14:kiwix-opds","format":"zim","download":{"method":"kiwix","book":"superuser.com_en_all","flavour":null,"url":"https://lb.download.kiwix.org/zim/stack_exchange/superuser.com_en_all_2026-10.zim"},"url_status":"200 verified 2026-11-14","scores":{"S":1,"R":5,"A":7,"U":4,"Q":7,"O":9},"requires":["tool-kiwix"]}
{"id":"kx-stackoverflow","name":"stackoverflow.com_en_all_2026-07","cat":"computing","tier":4,"desc_hu":"Teljes StackOverflow: programozási tudás (114 GB).","lang":"en","access":"free","license":"CC-BY-SA / közkincs (ZIM metaadat)","bytes":114855633920,"size_human":"114.86 GB","size_status":"measured:2026-11-14:kiwix-opds","format":"zim","download":{"method":"kiwix","book":"stackoverflow.com_en_all","flavour":null,"url":"https://lb.download.kiwix.org/zim/stack_exchange/stackoverflow.com_en_all_2026-07.zim"},"url_status":"200 verified 2026-11-14","scores":{"S":1,"R":8,"A":7,"U":8,"Q":7,"O":9},"requires":["tool-kiwix"]}
{"id":"kx-crashcourse","name":"crashcourse_en_all_2026-05","cat":"education","tier":4,"desc_hu":"CrashCourse oktatóvideók (tudomány, történelem).","lang":"en","access":"free","license":"CC-BY-SA / közkincs (ZIM metaadat)","bytes":23035095040,"size_human":"23.04 GB","size_status":"measured:2026-11-14:kiwix-opds","format":"zim","download":{"method":"kiwix","book":"crashcourse_en_all","flavour":null,"url":"https://lb.download.kiwix.org/zim/other/crashcourse_en_all_2026-05.zim"},"url_status":"200 verified 2026-11-14","scores":{"S":1,"R":6,"A":4,"U":4,"Q":8,"O":6},"requires":["tool-kiwix"]}
{"id":"kx-khan","name":"khanacademy_en_all_2023-03","cat":"education","tier":4,"desc_hu":"Khan Academy teljes angol kurzusanyag videókkal (2023-as snapshot) – gyerekek/új generáció oktatása.","lang":"en","access":"free","license":"CC-BY-SA / közkincs (ZIM metaadat)","bytes":180007048192,"size_human":"180.01 GB","size_status":"measured:2026-11-14:kiwix-opds","format":"zim","download":{"method":"kiwix","book":"khanacademy_en_all","flavour":null,"url":"https://lb.download.kiwix.org/zim/other/khanacademy_en_all_2023-03.zim"},"url_status":"200 verified 2026-11-14","scores":{"S":2,"R":8,"A":6,"U":7,"Q":9,"O":7},"requires":["tool-kiwix"]}
{"id":"kx-phet-en","name":"phet_en_all_2026-08","cat":"education","tier":4,"desc_hu":"PhET szimulációk angolul.","lang":"en","access":"free","license":"CC-BY-SA / közkincs (ZIM metaadat)","bytes":108981248,"size_human":"108.98 MB","size_status":"measured:2026-11-14:kiwix-opds","format":"zim","download":{"method":"kiwix","book":"phet_en_all","flavour":null,"url":"https://lb.download.kiwix.org/zim/phet/phet_en_all_2026-08.zim"},"url_status":"200 verified 2026-11-14","scores":{"S":1,"R":6,"A":5,"U":3,"Q":9,"O":7},"requires":["tool-kiwix"],"subsumed_by":["kx-phet-hu"]}
{"id":"kx-se-robotics","name":"robotics.stackexchange.com_en_all_2026-10","cat":"electronics","tier":4,"desc_hu":"Robotika Q&A.","lang":"en","access":"free","license":"CC-BY-SA / közkincs (ZIM metaadat)","bytes":243377152,"size_human":"243.38 MB","size_status":"measured:2026-11-14:kiwix-opds","format":"zim","download":{"method":"kiwix","book":"robotics.stackexchange.com_en_all","flavour":null,"url":"https://lb.download.kiwix.org/zim/stack_exchange/robotics.stackexchange.com_en_all_2026-10.zim"},"url_status":"200 verified 2026-11-14","scores":{"S":1,"R":5,"A":5,"U":4,"Q":7,"O":9},"requires":["tool-kiwix"]}
{"id":"kx-lt-biz","name":"libretexts.org_en_biz_2026-01","cat":"humanities","tier":4,"desc_hu":"LibreTexts üzlet/közgazdaság.","lang":"en","access":"free","license":"CC-BY-SA / közkincs (ZIM metaadat)","bytes":839754752,"size_human":"839.75 MB","size_status":"measured:2026-11-14:kiwix-opds","format":"zim","download":{"method":"kiwix","book":"libretexts.org_en_biz","flavour":null,"url":"https://lb.download.kiwix.org/zim/libretexts/libretexts.org_en_biz_2026-01.zim"},"url_status":"200 verified 2026-11-14","scores":{"S":1,"R":4,"A":4,"U":4,"Q":9,"O":9},"requires":["tool-kiwix"]}
{"id":"kx-lt-human","name":"libretexts.org_en_human_2026-07","cat":"humanities","tier":4,"desc_hu":"LibreTexts bölcsészet.","lang":"en","access":"free","license":"CC-BY-SA / közkincs (ZIM metaadat)","bytes":4433683456,"size_human":"4.43 GB","size_status":"measured:2026-11-14:kiwix-opds","format":"zim","download":{"method":"kiwix","book":"libretexts.org_en_human","flavour":null,"url":"https://lb.download.kiwix.org/zim/libretexts/libretexts.org_en_human_2026-07.zim"},"url_status":"200 verified 2026-11-14","scores":{"S":1,"R":4,"A":3,"U":4,"Q":9,"O":9},"requires":["tool-kiwix"]}
{"id":"kx-lt-socialsci","name":"libretexts.org_en_socialsci_2025-01","cat":"humanities","tier":4,"desc_hu":"LibreTexts társadalomtudományok.","lang":"en","access":"free","license":"CC-BY-SA / közkincs (ZIM metaadat)","bytes":2046179328,"size_human":"2.05 GB","size_status":"measured:2026-11-14:kiwix-opds","format":"zim","download":{"method":"kiwix","book":"libretexts.org_en_socialsci","flavour":null,"url":"https://lb.download.kiwix.org/zim/libretexts/libretexts.org_en_socialsci_2025-01.zim"},"url_status":"200 verified 2026-11-14","scores":{"S":1,"R":4,"A":3,"U":4,"Q":9,"O":9},"requires":["tool-kiwix"]}
{"id":"kx-gutenberg-en","name":"gutenberg_en_all_2025-11","cat":"library","tier":4,"group":"gutenberg","variant_rank":1,"variant_role":"pref","desc_hu":"Project Gutenberg angol könyvek (~70e+ közkincs mű).","lang":"en","access":"free","license":"CC-BY-SA / közkincs (ZIM metaadat)","bytes":221251591168,"size_human":"221.25 GB","size_status":"measured:2026-11-14:kiwix-opds","format":"zim","download":{"method":"kiwix","book":"gutenberg_en_all","flavour":null,"url":"https://lb.download.kiwix.org/zim/gutenberg/gutenberg_en_all_2025-11.zim"},"url_status":"200 verified 2026-11-14","scores":{"S":1,"R":6,"A":3,"U":7,"Q":8,"O":9},"requires":["tool-kiwix"]}
{"id":"kx-gutenberg-mul","name":"gutenberg_mul_all_2025-11","cat":"library","tier":4,"group":"gutenberg","variant_rank":2,"variant_role":"luxury","desc_hu":"Project Gutenberg összes nyelv.","lang":"multi","access":"free","license":"CC-BY-SA / közkincs (ZIM metaadat)","bytes":253055617024,"size_human":"253.06 GB","size_status":"measured:2026-11-14:kiwix-opds","format":"zim","download":{"method":"kiwix","book":"gutenberg_mul_all","flavour":null,"url":"https://lb.download.kiwix.org/zim/gutenberg/gutenberg_mul_all_2025-11.zim"},"url_status":"200 verified 2026-11-14","scores":{"S":1,"R":6,"A":3,"U":7,"Q":8,"O":9},"requires":["tool-kiwix"]}
{"id":"kx-wikivoyage","name":"wikivoyage_en_all_maxi_2026-09","cat":"reference","tier":4,"desc_hu":"Wikivoyage: régiók, útvonalak, helyi infó.","lang":"en","access":"free","license":"CC-BY-SA / közkincs (ZIM metaadat)","bytes":1071169536,"size_human":"1.07 GB","size_status":"measured:2026-11-14:kiwix-opds","format":"zim","download":{"method":"kiwix","book":"wikivoyage_en_all","flavour":"maxi","url":"https://lb.download.kiwix.org/zim/wikivoyage/wikivoyage_en_all_maxi_2026-09.zim"},"url_status":"200 verified 2026-11-14","scores":{"S":3,"R":2,"A":4,"U":4,"Q":6,"O":9},"requires":["tool-kiwix"]}
{"id":"kx-se-math","name":"math.stackexchange.com_en_all_2026-08","cat":"science","tier":4,"desc_hu":"Matematika Q&A (nagy).","lang":"en","access":"free","license":"CC-BY-SA / közkincs (ZIM metaadat)","bytes":7417272320,"size_human":"7.42 GB","size_status":"measured:2026-11-14:kiwix-opds","format":"zim","download":{"method":"kiwix","book":"math.stackexchange.com_en_all","flavour":null,"url":"https://lb.download.kiwix.org/zim/stack_exchange/math.stackexchange.com_en_all_2026-08.zim"},"url_status":"200 verified 2026-11-14","scores":{"S":1,"R":6,"A":4,"U":5,"Q":7,"O":9},"requires":["tool-kiwix"]}
{"id":"kx-ted","name":"ted_mul_all_2026-09","cat":"education","tier":5,"desc_hu":"TED előadások videón.","lang":"multi","access":"free","license":"CC-BY-SA / közkincs (ZIM metaadat)","bytes":91175796736,"size_human":"91.18 GB","size_status":"measured:2026-11-14:kiwix-opds","format":"zim","download":{"method":"kiwix","book":"ted_mul_all","flavour":null,"url":"https://lb.download.kiwix.org/zim/ted/ted_mul_all_2026-09.zim"},"url_status":"200 verified 2026-11-14","scores":{"S":0,"R":3,"A":2,"U":3,"Q":7,"O":6},"requires":["tool-kiwix"]}
```


---

## 10. select_items.py

```python select_items.py
#!/usr/bin/env python3
"""
ARCHIVUM kiválasztó + letöltési terv generátor (csak Python stdlib, 3.9+).

Bemenet: ARCHIVUM.md (a ```jsonl blokkokat olvassa ki) vagy egy .jsonl katalógus.
Kimenet: kiválasztási terv (táblázat a képernyőre, plan.json, opcionálisan download.sh).

Példák:
  python3 select_items.py ARCHIVUM.md --budget 256GB
  python3 select_items.py ARCHIVUM.md --budget 2TB --profile survival --langs hu,en --hw T3 --emit-sh dl.sh
  python3 select_items.py ARCHIVUM.md --budget 64GB --focus medicine=2,agriculture=1.5 --exclude kx-ted
  python3 select_items.py ARCHIVUM.md --list            # teljes katalógus pontszámokkal
"""
import argparse, json, re, sys, shlex

PROFILES = {  # súlyok: S=túlélés R=újjáépítés A=gyakorlatiasság U=pótolhatatlanság Q=megbízhatóság O=offline-kényelem
    "balanced":  {"S": .30, "R": .25, "A": .15, "U": .15, "Q": .10, "O": .05},
    "survival":  {"S": .45, "R": .10, "A": .20, "U": .10, "Q": .10, "O": .05},
    "rebuild":   {"S": .15, "R": .40, "A": .15, "U": .15, "Q": .10, "O": .05},
    "education": {"S": .10, "R": .35, "A": .10, "U": .15, "Q": .20, "O": .10},
    "computing": {"S": .05, "R": .40, "A": .20, "U": .15, "Q": .10, "O": .10},
}
AUTO_METHODS = {"kiwix", "http", "wget-mirror", "rsync", "git", "hf", "ollama", "archive.org", "torrent", "jigdo", "s3"}
UNITS = {"B": 1, "KB": 1e3, "MB": 1e6, "GB": 1e9, "TB": 1e12, "PB": 1e15,
         "KIB": 2**10, "MIB": 2**20, "GIB": 2**30, "TIB": 2**40}


def parse_size(s):
    m = re.fullmatch(r"\s*([\d.]+)\s*([A-Za-z]*)\s*", s)
    if not m:
        sys.exit(f"Érvénytelen méret: {s}")
    return int(float(m.group(1)) * UNITS.get((m.group(2) or "B").upper(), 1))


def human(b):
    if b is None:
        return "?"
    for u, f in (("TB", 1e12), ("GB", 1e9), ("MB", 1e6), ("KB", 1e3)):
        if b >= f:
            return f"{b / f:.2f} {u}"
    return f"{b} B"


def load(path):
    text = open(path, encoding="utf-8").read()
    if path.endswith(".md"):
        blocks = re.findall(r"```jsonl\n(.*?)```", text, re.S)
        lines = [l for b in blocks for l in b.splitlines()]
    else:
        lines = text.splitlines()
    items, seen = [], set()
    for l in lines:
        l = l.strip()
        if not l or l.startswith("//"):
            continue
        it = json.loads(l)
        if it["id"] in seen:
            sys.exit(f"Duplikált id: {it['id']}")
        seen.add(it["id"])
        items.append(it)
    return items


def composite(it, w, focus):
    s = it.get("scores") or {}
    base = sum(w[k] * s.get(k, 0) for k in w)
    return round(base * focus.get(it.get("cat"), 1.0), 3)


def size_of(it):
    return it.get("bytes") or it.get("bytes_est")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("catalog")
    ap.add_argument("--budget", help="pl. 64GB, 512GB, 2TB (decimális egység, mint a meghajtók címkéje)")
    ap.add_argument("--reserve", type=float, default=0.08, help="tartalék hányad a fájlrendszernek / checksumoknak (alap 0.08)")
    ap.add_argument("--profile", default="balanced", choices=PROFILES)
    ap.add_argument("--langs", default="hu,en,multi", help="engedett nyelvek, vesszővel")
    ap.add_argument("--access", default="free,free-registration,donation",
                    help="engedett hozzáférés: free,free-registration,donation,paid,gray,physical")
    ap.add_argument("--hw", default=None, help="LLM hardverszint: T1..T5 (ha nincs megadva: nincs LLM, csak ha --llm-max>0 és --hw adott)")
    ap.add_argument("--llm-max", type=float, default=0.35, help="a keret max. ennyi hányada mehet LLM-súlyokra")
    ap.add_argument("--focus", default="", help="kategória-szorzók, pl. medicine=2,agriculture=1.5")
    ap.add_argument("--max-tier", type=int, default=5)
    ap.add_argument("--include", default="", help="kötelezően beveendő id-k (vesszővel)")
    ap.add_argument("--exclude", default="", help="kizárt id-k vagy kategóriák (cat:NAME)")
    ap.add_argument("--list", action="store_true", help="katalógus listázása pontszám szerint")
    ap.add_argument("--out", default="plan.json")
    ap.add_argument("--emit-sh", default=None, help="letöltő bash szkript írása ide")
    ap.add_argument("--dest", default="/mnt/archivum", help="célkönyvtár a szkriptben")
    a = ap.parse_args()

    items = load(a.catalog)
    w = PROFILES[a.profile]
    focus = {k: float(v) for k, v in (p.split("=") for p in a.focus.split(",") if p)}
    for it in items:
        it["_score"] = composite(it, w, focus)

    if a.list:
        for it in sorted(items, key=lambda x: (x["tier"], -x["_score"])):
            print(f"T{it['tier']} {it['_score']:5.2f} {human(size_of(it)):>10} {it['access']:<17} {it['cat']:<17} {it['id']}")
        return
    if not a.budget:
        sys.exit("--budget kötelező (vagy --list)")

    budget = int(parse_size(a.budget) * (1 - a.reserve))
    langs = set(a.langs.split(","))
    access = set(a.access.split(","))
    excl = set(x for x in a.exclude.split(",") if x)
    incl = set(x for x in a.include.split(",") if x)

    manual, skipped_unknown, eligible = [], [], []
    for it in items:
        if it["id"] in excl or f"cat:{it['cat']}" in excl:
            continue
        if it["tier"] > a.max_tier and it["id"] not in incl:
            continue
        if it.get("lang") not in langs and it["id"] not in incl:
            continue
        if it.get("access") not in access:
            continue
        if it["cat"] == "ai_models":
            if not a.hw or a.hw not in (it.get("hw_tiers") or []):
                continue
        method = (it.get("download") or {}).get("method")
        if method not in AUTO_METHODS or it.get("access") in ("paid", "physical"):
            manual.append(it)
            continue
        if size_of(it) is None:
            skipped_unknown.append(it)
            continue
        eligible.append(it)

    groups = {}
    for it in eligible:
        groups.setdefault(it.get("group") or it["id"], []).append(it)
    for g in groups.values():
        g.sort(key=lambda x: (x.get("variant_rank") or 0, size_of(x)))

    chosen, used = {}, 0
    llm_cap = int(budget * a.llm_max)

    def llm_used():
        return sum(size_of(v) for v in chosen.values() if v["cat"] == "ai_models")

    def fits(new, old=None):
        delta = size_of(new) - (size_of(old) if old else 0)
        if used + delta > budget:
            return False
        if new["cat"] == "ai_models" and llm_used() + delta > llm_cap:
            return False
        return True

    def pref_rank(g):
        for v in g:
            if v.get("variant_role") == "pref":
                return v.get("variant_rank") or 0
        return max((v.get("variant_rank") or 0) for v in g)

    order = sorted(groups.items(), key=lambda kv: (min(v["tier"] for v in kv[1]) if kv[0] not in
                                                   {v.get("group") or v["id"] for v in eligible if v["id"] in incl} else -1,
                                                   -max(v["_score"] for v in kv[1])))
    tiers = sorted({min(v["tier"] for v in g) for _, g in order} | {-1})

    def fill(tier_filter):
        nonlocal used
        sel = [(k, g) for k, g in order if tier_filter(k, g)]
        for k, g in sel:                       # 1) legkisebb változat
            if k in chosen:
                continue
            v = min(g, key=size_of)
            if fits(v):
                chosen[k] = v; used += size_of(v)
        for k, g in sel:                       # 2) feljavítás az ajánlott változatig
            if k not in chosen:
                continue
            pr = pref_rank(g)
            for v in sorted([x for x in g if (x.get("variant_rank") or 0) <= pr], key=size_of, reverse=True):
                if size_of(v) > size_of(chosen[k]) and fits(v, chosen[k]):
                    used += size_of(v) - size_of(chosen[k]); chosen[k] = v
                    break

    def tier_of(k, g):
        return -1 if any(v["id"] in incl for v in g) else min(v["tier"] for v in g)

    for t in tiers:
        fill(lambda k, g, t=t: tier_of(k, g) == t)
    # 3) luxus-feljavítások (pl. képes Wikipedia) pontszám szerint
    for k, g in sorted(groups.items(), key=lambda kv: -max(v["_score"] for v in kv[1])):
        if k in chosen:
            for v in sorted(g, key=size_of, reverse=True):
                if size_of(v) > size_of(chosen[k]) and fits(v, chosen[k]):
                    used += size_of(v) - size_of(chosen[k]); chosen[k] = v
                    break
    # 4) átfedések kiszűrése (pl. Wikipedia-orvosi részhalmaz, ha a teljes WP bent van), majd újratöltés
    ids = {v["id"] for v in chosen.values()}
    for k in [k for k, v in chosen.items() if set(v.get("subsumed_by") or []) & ids]:
        used -= size_of(chosen[k]); del chosen[k]
    ids = {v["id"] for v in chosen.values()}
    for t in tiers:
        fill(lambda k, g, t=t: tier_of(k, g) == t and not any(set(v.get("subsumed_by") or []) & ids for v in g))

    plan = sorted(chosen.values(), key=lambda x: (x["tier"], -x["_score"]))
    # szükséges olvasó/futtató eszközök (requires) – ha a katalógusban szerepelnek, mindig kerüljenek be
    need = {r for v in plan for r in (v.get("requires") or [])}
    byid = {it["id"]: it for it in items}
    tools = [byid[r] for r in sorted(need) if r in byid and r not in {v["id"] for v in plan}]
    for t in tools:
        if size_of(t):
            used += size_of(t)
    plan = tools + plan

    print(f"Profil: {a.profile} | keret: {a.budget} (használható {human(budget)}) | felhasználva: {human(used)} "
          f"| elemek: {len(plan)} | LLM: {human(llm_used())} (max {human(llm_cap)})\n")
    print(f"{'#':>3} {'T':>2} {'pont':>5} {'méret':>10}  {'mód':<11} id")
    for i, v in enumerate(plan, 1):
        print(f"{i:>3} {v['tier']:>2} {v['_score']:5.2f} {human(size_of(v)):>10}  {v['download']['method']:<11} {v['id']}"
              + ("  (becsült méret)" if not v.get("bytes") else ""))
    left = sorted([it for k, g in groups.items() if k not in chosen for it in g[:1]], key=lambda x: (x["tier"], -x["_score"]))
    if left:
        print(f"\nKimaradt (nem fért be) – első 15 a fontosság szerint:")
        for v in left[:15]:
            print(f"     T{v['tier']} {v['_score']:5.2f} {human(size_of(v)):>10}  {v['id']}")
    if manual:
        print(f"\nKÉZI TEENDŐK (fizetős / regisztrációs / fizikai / kézi letöltés) – emberi döntés kell:")
        for v in sorted(manual, key=lambda x: (x["tier"], -x["_score"])):
            print(f"     T{v['tier']} {v['_score']:5.2f} {v['access']:<17} {v.get('price') or '':<14} {v['id']}  {v.get('info_url')}")
    if skipped_unknown:
        print("\nIsmeretlen méret miatt kihagyva (ellenőrizd kézzel):", ", ".join(v["id"] for v in skipped_unknown))

    json.dump({"budget_bytes": budget, "used_bytes": used, "profile": a.profile,
               "items": [{k: v[k] for k in v if not k.startswith("_")} | {"score": v["_score"]} for v in plan],
               "manual": [v["id"] for v in manual]}, open(a.out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"\nTerv mentve: {a.out}")
    if a.emit_sh:
        write_sh(plan, a.emit_sh, a.dest)
        print(f"Letöltő szkript: {a.emit_sh}  (futtatás előtt nézd át!)")


def write_sh(plan, path, dest):
    q = shlex.quote
    L = ["#!/usr/bin/env bash", "# ARCHIVUM letöltő – generálva select_items.py által. Újraindítható (resume).",
         "set -uo pipefail", f"DEST=${{DEST:-{q(dest)}}}", 'LOG="$DEST/_log.txt"; mkdir -p "$DEST"',
         'have(){ command -v "$1" >/dev/null 2>&1; }',
         'fetch(){ # url outdir',
         '  if have aria2c; then aria2c -c -x8 -s8 --auto-file-renaming=false -d "$2" "$1"; else (cd "$2" && wget -c "$1"); fi; }',
         'kiwix_latest(){ # book flavour fallback_url -> legfrissebb URL az OPDS katalógusból',
         '  local u; u=$(curl -fsSL "https://library.kiwix.org/catalog/v2/entries?name=$1&count=50" 2>/dev/null \\',
         '    | tr "\\n" " " | sed "s#<entry>#\\n#g" | { if [ -n "$2" ]; then grep "<flavour>$2</flavour>"; else cat; fi; } \\',
         '    | grep -o "https://[^\\"]*\\.zim\\.meta4" | sed "s/\\.meta4$//" | sort | tail -1)',
         '  echo "${u:-$3}"; }',
         'ok(){ echo "OK   $1" | tee -a "$LOG"; }; fail(){ echo "FAIL $1" | tee -a "$LOG"; }', ""]
    for v in plan:
        d = v["download"]; m = d["method"]; sub = f'$DEST/{v["cat"]}/{v["id"]}'
        L.append(f"# --- {v['id']}  ({human(size_of(v))})  {v.get('name','')}")
        L.append(f'mkdir -p "{sub}"')
        if m == "kiwix":
            L.append(f'U=$(kiwix_latest {q(d["book"])} {q(d.get("flavour") or "")} {q(d.get("url") or "")}); F="{sub}/${{U##*/}}"')
            L.append(f'if have aria2c; then aria2c -c --auto-file-renaming=false --seed-time=0 -d "{sub}" "$U.meta4" || fetch "$U" "{sub}"; else fetch "$U" "{sub}"; fi')
            L.append(f'(cd "{sub}" && curl -fsSL "$U.sha256" | sha256sum -c -) && ok {q(v["id"])} || fail {q(v["id"])}')
        elif m in ("http", "jigdo"):
            for u in (d.get("urls") or [d.get("url")]):
                if u:
                    L.append(f'fetch {q(u)} "{sub}" && ok {q(v["id"])} || fail {q(v["id"])}')
        elif m == "wget-mirror":
            L.append(f'(cd "{sub}" && wget -m -np -k -E -c -e robots=off --wait=1 {d.get("wget_args","")} {q(d["url"])}) && ok {q(v["id"])} || fail {q(v["id"])}')
        elif m == "rsync":
            L.append(f'rsync -avP --partial {d.get("rsync_args","")} {q(d["url"])} "{sub}/" && ok {q(v["id"])} || fail {q(v["id"])}')
        elif m == "git":
            for u in (d.get("repos") or [d.get("url")]):
                n = u.rstrip("/").split("/")[-1]
                L.append(f'[ -d "{sub}/{n}.git" ] || git clone --mirror {q(u)} "{sub}/{n}.git"; '
                         f'git -C "{sub}/{n}.git" remote update && git -C "{sub}/{n}.git" bundle create "{sub}/{n}.bundle" --all && ok {q(v["id"])} || fail {q(v["id"])}')
        elif m == "hf":
            inc = " ".join(f"--include {q(p)}" for p in (d.get("include") or []))
            L.append(f'hf download {q(d["repo"])} {inc} --local-dir "{sub}" && ok {q(v["id"])} || fail {q(v["id"])}')
        elif m == "ollama":
            L.append(f'ollama pull {q(d["tag"])} && ok {q(v["id"])} || fail {q(v["id"])}   # tárolás: ~/.ollama/models (vagy $OLLAMA_MODELS)')
        elif m == "archive.org":
            for ident in (d.get("ids") or [d.get("id")]):
                glob = f' --glob={q(d["glob"])}' if d.get("glob") else ""
                L.append(f'ia download {q(ident)}{glob} --destdir "{sub}" && ok {q(v["id"])} || fail {q(v["id"])}')
        elif m == "torrent":
            L.append(f'aria2c -c --seed-time=0 -d "{sub}" {q(d.get("url") or d.get("magnet"))} && ok {q(v["id"])} || fail {q(v["id"])}')
        elif m == "s3":
            L.append(f'# S3: {d.get("note","")}\n# aws s3 sync {d.get("url")} "{sub}" {d.get("s3_args","")}')
        L.append("")
    L.append('echo "Kész. Napló: $LOG"; grep -c FAIL "$LOG" || true')
    open(path, "w").write("\n".join(L) + "\n")


if __name__ == "__main__":
    main()
```
