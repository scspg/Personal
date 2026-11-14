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
