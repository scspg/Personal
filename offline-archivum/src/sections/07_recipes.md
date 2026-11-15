---

## 7. Letöltési receptek

A `download.method` mező szerint. Mindegyik újraindítható.

| method | Parancs-sablon | Ellenőrzés |
|---|---|---|
| `kiwix` | `curl -fsSL "https://library.kiwix.org/catalog/v2/entries?name=<book>&count=50"`: az `<entry>`-k közül a `<flavour>` egyezik, a legnagyobb dátumú `…zim.meta4` link a jó. Utána `aria2c -c --seed-time=0 <url>.meta4` (vagy `wget -c <url>`). | `curl -fsSL <url>.sha256 \| sha256sum -c -`; opcionálisan `zimcheck -A file.zim` |
| `http` | `aria2c -c -x8 -s8 <url>` vagy `wget -c <url>` | méret = Content-Length; sha256, ha a forrás közli |
| `wget-mirror` | `wget -m -np -k -E -c -e robots=off --wait=1 <url>` (HTML-gyűjtemény, PDF-könyvtár) | darabszám és hibalista (`grep -c ERROR wget.log`) |
| `rsync` | `rsync -avP --partial <rsync://…> <cél>/` | az rsync maga ellenőriz (`--checksum` a második körben) |
| `git` | alapból sekély klón csak ágakkal és tagekkel (a GitHub `refs/pull/*` nélkül): `git init --bare X.git` → `git -C X.git fetch --depth 1 origin refs/tags/<tag>:refs/tags/<tag>`; teljes történet: `GIT_FULL=1`; egyfájlos másolat: `BUNDLE=1` (`git bundle create X.bundle --all`, csak teljes történettel). GitHub-projekteknél a kiadás telepítőit a `gh_release` függvény tölti le a `release/` mappába (szűrés: `GH_ASSET_RE`, méretkorlát: `GH_ASSET_MAX_MB`, alap 1500 MB; API-limit esetén `GITHUB_TOKEN`) | `git -C X.git fsck`; tag megléte (`git tag`) |
| `hf` | `pip install -U huggingface_hub` → `hf download <owner/repo> --include "<minta>" --local-dir <cél>` (a dl.sh mintánként külön hívást ír, mert a régi `huggingface-cli` ismételt `--include` esetén csak az utolsót veszi figyelembe). Gated repóhoz előbb `hf auth login`. Gyorsítás: `pip install hf_xet` (alapértelmezett backend), vagy `HF_HUB_ENABLE_HF_TRANSFER=1` régebbi verzióknál. | a HF API `lfs.oid` = sha256: `curl -s https://huggingface.co/api/models/<repo>/tree/main?recursive=true` |
| `ollama` | a dl.sh `ollama_pull` függvénye ideiglenes szervert indít `OLLAMA_MODELS=<cél>` beállítással, így a modell a meghajtóra kerül (nem a gép saját könyvtárába) | `ollama list` ugyanazzal az `OLLAMA_MODELS`-szel |
| `archive.org` | `pip install internetarchive` → `ia download <identifier> --glob="*.pdf" --destdir <cél>`. A fájllista és a méretek: `https://archive.org/metadata/<identifier>`. | md5/sha1 a metadata JSON-ban |
| `torrent` | `aria2c -c --seed-time=0 <magnet vagy .torrent>`. Ha lehet, seedeld tovább. | a torrent beépített hash-ellenőrzése |
| `jigdo` | automatikus: a dl.sh a könyvtár összes `.jigdo` fájlján lefuttatja a `jigdo-lite --noask <url>` parancsot (csomag: `jigdo-file`); a Debian BD/DVD-képeket a tükörből rakja össze | a `.iso` sha256/sha512 a `SHA256SUMS`/`SHA512SUMS` fájlból |
| `s3` | `aws s3 sync s3://… <cél> --request-payer requester`. **Fizetős adatforgalom** (pl. arXiv bulk), ezért előbb költségbecslés. | ETag / manifest |
| `agent` | AI-feladat – a dl.sh `# Megjegyzés:` és `TODO` sora mondja meg, mit kell gyűjteni. Tipikus receptek: **DSpace/IRIS** (WHO): `/server/api/core/items/<uuid>/bundles` → bitstreamek → `/content`; **OAI-PMH** (MEK, EPA): `?verb=ListRecords&metadataPrefix=oai_dc`, `resumptionToken`-nel lapozva; **WordPress**: `/wp-json/wp/v2/media?per_page=100&page=N`; **GitHub-kiadás**: `gh_release owner/repo tag <mappa> <MB>`; **S3**: `aws s3 sync … --no-sign-request` szűrőkkel. Szabály: maradj a tétel `# ---` fejlécében szereplő méreten belül, és a letöltés után írd be a naplóba (OK/FAIL). | méret a fejléchez képest; sha256, ha a forrás közli |
| `manual` / `purchase` | Az AI nem csinálja meg. Listázza a linkkel és árral, az ember dönt. | — |

### Olvasók és futtatók (a `tool-*` elemek, mindig kerüljenek a meghajtóra)

- **ZIM:**
  - Kiwix Desktop (Windows/Linux AppImage/macOS): <https://download.kiwix.org/release/kiwix-desktop/>
  - Kiwix Android (F-Droid / APK): <https://download.kiwix.org/release/kiwix-android/>
  - `kiwix-serve` (kiwix-tools, egy Raspberry Pi kiszolgálja az egész LAN-t, böngészőből érhető el): <https://download.kiwix.org/release/kiwix-tools/>
  - Indítás: `kiwix-serve --port 8888 /archivum/**/*.zim`, utána `http://<ip>:8888`.
- **PDF / EPUB:** SumatraPDF (Windows), Okular/Evince (Linux), KOReader (e-ink, Android), Calibre (könyvtárkezelés).
- **Videó:** VLC (minden platformra, a telepítőt is mentsd le).
- **Térkép:** Organic Maps / OsmAnd APK + offline térképfájlok, QGIS a nyers OSM/DEM adatokhoz.
- **LLM:** lásd a 6. fejezetet (llama.cpp binárisok, Ollama, LM Studio, PocketPal).
