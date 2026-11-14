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
