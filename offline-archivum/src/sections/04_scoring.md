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
