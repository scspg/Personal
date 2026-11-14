---

## 9. Webes hozzáférés az AI-nak: captcha- és blokkmentes keresés és letöltés

Egyes forrásoldalak (pl. ECHO, Peace Corps, Sphere, RepRap-wiki) Cloudflare-rel blokkolják a sima `curl`-t. Az alábbi eszközökkel az AI-ágens ezeket is le tudja tölteni, és API-n keres, nem Google-scrape-pel. A verziókat és a dátumokat a PyPI és az npm registry, valamint `git ls-remote` alapján ellenőrzött (2026-11-14).

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

### 9.2 Eszközök

#### Stealth böngésző / könyvtár

| Eszköz | Verzió (dátum) | Hozzáférés / ár | Karbantartott | Telepítés | Mire jó |
|---|---|---|---|---|---|
| **[Camoufox](https://github.com/daijro/camoufox)** | python/npm camoufox 0.5.9 (2026-11-01); browser… | free: 0 (a README-t proxy-szolgáltatók szponzorálják) | yes – utolsó commit 2026-11-14; a… | `pip install -U "camoufox[geoip]" && camoufox fetch   \|  npm install camoufox…` | Erős fingerprint-konzisztencia; geoip=True a proxy kilépő IP-jéhez igazítja a timezone/locale/WebRTC értékeket; humanize=True… |
| **[Patchright](https://github.com/Kaliiiiiiiiii-Vinyzu/patchright)** | PyPI 1.64.4 (2026-11-02); npm 1.64.3… | free: 0 | yes – utolsó commit 2026-11-12… | `pip install patchright && patchright install chrome…` | Ha már van Playwright-kódunk, csak az importot kell cserélni. Saját állítása szerint átmegy Cloudflare, Kasada, Akamai, Datadome és CreepJS… |
| **[rebrowser-patches / rebrowser-playwright / rebrowser-puppeteer](https://github.com/rebrowser/rebrowser-patches)** | patches 1.1.3 (npm, 2026-11-02)… | free: 0 | yes – utolsó commit 2026-11-02 | `pip install rebrowser-playwright (import: rebrowser_playwright)  \|  npm…` | npm alias-szal kódváltoztatás nélkül beköthető; Puppeteerhez is van; saját bot-detector tesztoldal. |
| **[nodriver](https://github.com/ultrafunkamsterdam/nodriver)** | 0.50.99 | free: 0 | yes – utolsó commit 2026-10-26; az… | `pip install nodriver` | Valódi Chrome-ot használ, nincs webdriver-lenyomat; 1–2 soros indítás; okos tab.find(text) elemkeresés; cookie mentése és betöltése. |
| **[Zendriver](https://github.com/cdpdriver/zendriver)** | 0.17.1 | free: 0 | yes – utolsó commit 2026-10-01… | `pip install zendriver` | Jobb dokumentáció és közösség, mint a nodrivernél; Docker-támogatás. |
| **[undetected-chromedriver](https://github.com/ultrafunkamsterdam/undetected-chromedriver)** | 3.5.5 | free: 0 | stale – PyPI utoljára 2024-02, utolsó… | `pip install undetected-chromedriver` | Rengeteg régi példa és tutorial; a FlareSolverr erre épül. |
| **[SeleniumBase (UC Mode / CDP Mode / Stealthy Playwright Mode)](https://github.com/seleniumbase/SeleniumBase)** | 4.57.1 | free: 0 | yes – utolsó commit 2026-11-13, nagyon… | `pip install seleniumbase` | Nagyon sok kész Cloudflare-bypass példa (examples/cdp_mode); pytest-integráció; aktív fejlesztő. |
| **[Botasaurus](https://github.com/omkarcloud/botasaurus)** | botasaurus 4.0.97 (2026-01-06)… | free: 0 | yes – utolsó repo-commit 2026-11-13… | `python -m pip install --upgrade botasaurus` | All-in-one: cache, párhuzamosítás, UI és API generálás; HTTP- és böngészőmód is van. |
| **[playwright-stealth (Python) / puppeteer-extra-plugin-stealth (Node)](https://github.com/Mattwmaster58/playwright_stealth)** | playwright-stealth 2.0.3 (PyPI, 2026-04-04)… | free: 0 | playwright-stealth: low… | `pip install playwright-stealth  \|  npm i puppeteer-extra…` | Könnyű ráhúzni meglévő kódra. |
| **[Scrapling (Fetcher / StealthyFetcher / DynamicFetcher)](https://github.com/D4Vinci/Scrapling)** | 0.5.1 | free: 0 | yes – utolsó commit 2026-11-11 | `pip install "scrapling[fetchers]" && scrapling install…` | Egy könyvtárban van a sima letöltés és a böngészős bypass; beépített MCP szerver AI agentnek; kész Docker image. |
| **[Kameleo / Multilogin / GoLogin / AdsPower / Octo Browser / Dolphin{anty}](kameleo.io,)** | n/a | free-tier (a legtöbbnél) / paid: Kameleo: Free (2 párhuzamos böngésző, 300 perc), Startup… | True | `desktop app + lokális REST API…` | GUI, profil-perzisztencia, csapatmegosztás; erős fingerprint. |

#### TLS-utánzás (böngésző nélkül)

| Eszköz | Verzió (dátum) | Hozzáférés / ár | Karbantartott | Telepítés | Mire jó |
|---|---|---|---|---|---|
| **[curl_cffi (+ curl-impersonate)](https://github.com/lexiforest/curl_cffi)** | curl_cffi 0.17.0 (PyPI 2026-10-26)… | free: 0 (opcionális kereskedelmi fingerprint-DB: impersonate.pro) | yes – utolsó commit 2026-10-27; a… | `pip install curl_cffi --upgrade` | Gyors és könnyű, JS nem kell. Streamelt letöltés (stream=True + iter_content). Async, WebSocket, proxy. Sok '403 curl-ra, de böngészőben megy'… |
| **[hrequests](https://github.com/daijro/hrequests)** | 0.9.2 | free: 0 | stale – utolsó commit 2024-11-30 | `pip install hrequests` | Kényelmes API volt. |

#### Challenge-feloldó proxy

| Eszköz | Verzió (dátum) | Hozzáférés / ár | Karbantartott | Telepítés | Mire jó |
|---|---|---|---|---|---|
| **[cloudscraper](https://github.com/VeNoMouS/cloudscraper)** | PyPI 1.2.71 (2023-04-25); a repóban van '3.0.0'… | free: 0 | stale – utolsó commit 2025-06-10; a… | `pip install cloudscraper` | Régi, egyszerű oldalakon néha még működik. |
| **[FlareSolverr](https://github.com/FlareSolverr/FlareSolverr)** | v3.5.2 (tag commit 2026-09-12) | free: 0 | yes – utolsó commit 2026-10-24 | `docker run -d --name=flaresolverr -p 127.0.0.1:8191:8191 -e LOG_LEVEL=info…` | Nyelvfüggetlen; kész Docker image (amd64/arm64/arm7); a *arr ökoszisztéma bevett eszköze. |
| **[Byparr](https://github.com/ThePhaseless/Byparr)** | v3.1.1 (tag commit 2026-11-05) | free: 0 | yes – utolsó commit 2026-11-09 | `docker run -p 8191:8191 ghcr.io/thephaseless/byparr:latest` | Modernebb böngésző-alap; drop-in a FlareSolverr helyére; proxy per request (X-Proxy-Server header). |

#### Crawl / agent keretrendszer

| Eszköz | Verzió (dátum) | Hozzáférés / ár | Karbantartott | Telepítés | Mire jó |
|---|---|---|---|---|---|
| **[Crawl4AI](https://github.com/unclecode/crawl4ai)** | 0.9.5 | free: 0 | yes – utolsó commit 2026-11-04 | `pip install -U crawl4ai && crawl4ai-setup` | Offline archívumhoz kiváló: tiszta Markdown, link-gráf, cache-mód, deep crawl. |
| **[Browser Use](https://github.com/browser-use/browser-use)** | PyPI 1.0.4 (2026-11-13); a gitben van 1.0.5 tag… | free (OSS) + paid cloud (cloud.browser-use.com): OSS 0; Cloud: UNVERIFIED | yes – utolsó commit 2026-11-14 | `pip install browser-use   (Python >=3.11)` | Interaktív, többlépéses feladatokra jó (űrlap, lapozás, bejelentkezés). |
| **[Steel Browser](https://github.com/steel-dev/steel-browser)** | v0.5.5-beta (tag 2026-10-31); steel-sdk PyPI és… | free (self-host) + paid cloud: Cloud Launch: $0/hó + használat, $30 egyszeri kredit… | yes – utolsó commit 2026-11-13 | `docker run -p 3000:3000 -p 9223:9223 ghcr.io/steel-dev/steel-browser   \|  pip…` | Saját infrán futtatható 'Browserbase'; agentekhez tervezték. |
| **[Lightpanda](https://github.com/lightpanda-io/browser)** | repo-tag v0.2.6 (2026-03-14) + nightly buildek… | free: 0 (van cloud is: UNVERIFIED ár) | yes – aktív | `curl -L -o lightpanda https://github.com/lightpanda-io/browser/releases/downloa…` | Nagy tömegű JS-renderelésre és Markdown-dumpra nagyon olcsó. |
| **[Firecrawl](https://github.com/firecrawl/firecrawl)** | firecrawl-py 4.57.0 (2026-11-12); npm firecrawl… | free-tier (cloud) + self-host: Free: 1 000 kredit/hó; Hobby $19/hó 5 000; Standard $99/hó… | yes – utolsó commit 2026-11-13 | `pip install firecrawl-py ; self-host: docker compose (SELF_HOST.md)` | Search és scrape egy hívásban; agent-integrációk (MCP, skills). |

#### Saját keresőszerver

| Eszköz | Verzió (dátum) | Hozzáférés / ár | Karbantartott | Telepítés | Mire jó |
|---|---|---|---|---|---|
| **[SearXNG](https://github.com/searxng/searxng)** | rolling release (nincsenek git tagek); utolsó… | free: 0 | yes – nagyon aktív | `mkdir -p searxng/config searxng/data && cd searxng && docker run --name…` | Ingyenes, kulcs nélküli; a saját példányon a limiter kikapcsolható; motoronként hangolható. |

#### Kereső API

| Eszköz | Verzió (dátum) | Hozzáférés / ár | Karbantartott | Telepítés | Mire jó |
|---|---|---|---|---|---|
| **[ddgs (korábban duckduckgo_search)](https://github.com/deedy5/ddgs)** | ddgs 9.16.1 (2026-10-23); a régi… | free: 0, kulcs nélkül | yes – utolsó commit 2026-10-24 | `pip install -U ddgs   (ddgs[api] = FastAPI szerver, ddgs[mcp] = MCP szerver)` | Nulla setup; filetype:pdf operátor; extract() is van; MCP szerverként agentbe köthető. |
| **[Brave Search API](https://brave.com/search/api/)** | n/a | free-tier: Search: $5/1 000 kérés, havi $5 ingyen kredit… | True | `REST; header: X-Subscription-Token` | Saját index (nem Google vagy Bing proxy); stabil; agentekben bevett. |
| **[Tavily](https://tavily.com)** | tavily-python 0.8.5 | free-tier: 1 000 kredit/hó ingyen; PAYG $0.008/kredit; basic search 1… | yes | `pip install tavily-python` | Agent-keretrendszerekben (LangChain stb.) alapértelmezett; az extract endpoint letöltést is spórol. |
| **[Exa](https://exa.ai)** | exa-py 2.28.0 | free-tier: $10 ingyen kredit, minden hónap 1-jén visszaáll… | yes | `pip install exa-py` | Kutatási jellegű, dokumentum-típusú keresésre (PDF-ek, reportok) jó. |
| **[Jina Reader (r.jina.ai) / Search (s.jina.ai)](https://jina.ai/reader/)** | n/a | free-tier: r.jina.ai: kulcs nélkül 20 RPM, ingyen kulccsal 500 RPM… | yes | `curl https://r.jina.ai/https://example.org   \|  curl -H 'Authorization: Bearer…` | Egyetlen URL-prefix, setup nélkül; néha átjut ott, ahol a saját IP-nk blokkolva van (más IP-ről kér). |
| **[Kagi Search API](https://kagi.com/api/docs)** | v1 (POST /search); a v0 legacy | paid: $12/1 000 kérés (pay-as-you-go) | True | `REST; Authorization: Bearer $KAGI_API_KEY` | Magas minőség, hirdetés- és SEO-spam-szűrés. |
| **[SerpApi](https://serpapi.com)** | n/a | free-tier: Free 250 keresés/hó; Starter $25/1 000 (= $25/1k)… | True | `pip install google-search-results (UNVERIFIED csomagnév) vagy REST` | Pontos Google-eredmények; sok motor és vertikális (Scholar, Images stb.). |
| **[Serper.dev](https://serper.dev)** | n/a | free-tier: 2 500 ingyen query (kártya nélkül); Starter $50/50k… | True | `REST POST https://google.serper.dev/search, X-API-KEY header…` | A legolcsóbb Google-SERP API. |
| **[Mojeek Search API](https://www.mojeek.com/services/search/web-search-api/)** | n/a | paid: £2/1k (Startup: 5 QPS, 10 találat/kérés), £3/1k… | True | `REST` | Olcsó, privacy-fókuszú, független index. |
| **[Marginalia Search API](https://about.marginalia-search.com/article/api/)** | új endpoint: https://api2.marginalia-search.com/s… | free: Ingyenes nem kereskedelmi kulcs e-mailben kérhető; a… | True | `GET …/search?query=…  header: API-Key` | Ingyenes; régi, dokumentum-jellegű oldalakra meglepően jó. |
| **[Google Custom Search JSON API (Programmable Search)](https://developers.google.com/custom-search/v1/overview)** | n/a | free-tier (csak meglévő ügyfeleknek): 100 query/nap ingyen, utána $5/1k, napi plafon 10 000 | KIVEZETÉS ALATT – 'closed to new… | `REST (key + cx)` | Hivatalos Google-forrás. |
| **[Bing Search API](https://learn.microsoft.com/en-us/lifecycle/announcements/bing-search-api-retirement)** | n/a | megszűnt: n/a | no – 2025-08-11-én nyugdíjazták… | `n/a` | - |
| **[Perplexity Search API / Sonar](https://docs.perplexity.ai)** | Search API (POST /search); a Sonar Chat… | paid: Search API: $5/1k kérés, Fast Search $1/1k… | yes, de a Sonar éppen átalakul | `REST` | A Fast Search $1/1k-s ára nagyon olcsó. |

#### Felhős unblocker

| Eszköz | Verzió (dátum) | Hozzáférés / ár | Karbantartott | Telepítés | Mire jó |
|---|---|---|---|---|---|
| **[Browserbase](https://www.browserbase.com/pricing)** | n/a | free-tier: Free: 1 browser-óra; Developer $20/hó, 100 óra… | True | `SDK + CDP-csatlakozás (Playwright/Puppeteer); Stagehand framework` | Agentekhez épült; session-rögzítés; skálázható. |
| **[Bright Data Web Unlocker / Browser API (Scraping Browser)](https://brightdata.com/pricing/web-unlocker)** | n/a | free-tier: Web Unlocker: 5k kérés/hó ingyen, PAYG $1.5/1k… | True | `proxy-endpoint (HTTP proxy-ként) vagy CDP wss endpoint` | Iparági csúcs a nehéz célpontokon; csak a sikeres kérést számlázza. |
| **[ZenRows](https://www.zenrows.com/pricing)** | n/a | free-tier: Free: 5 000 kredit/hó (kártya nélkül); Build $19/hó 45k… | True | `REST API vagy proxy-mód` | Egyszerű URL-wrapper; nagylelkű free tier. |
| **[ScrapingBee](https://www.scrapingbee.com/pricing/)** | n/a | free-tier: 1 000 ingyen kredit; Hobby $19/hó 75k, Freelance $49/hó… | True | `REST` | Egyszerű és olcsó belépő. |
| **[Scrapfly](https://scrapfly.io/pricing)** | n/a | free-tier: 1 000 ingyen kredit; Discovery $30/hó 200k; Pro $100/hó… | True | `REST / Python SDK` | Átlátható költségbecslés hívás előtt. |
| **[Oxylabs Web Unblocker](https://oxylabs.io/products/web-unblocker)** | n/a | paid: GB-alapú: $7.2/GB (legfeljebb 2 GB) … $3/GB (833+ GB)… | True | `proxy-endpoint` | Proxyként transzparens, minden klienssel működik. |
| **[Zyte API](https://www.zyte.com/pricing/)** | n/a | free-tier: $5 ingyen kredit, 30 napos trial; HTTP PAYG $0.13–$1.27/1k… | True | `REST / Scrapy plugin (scrapy-zyte-api)` | Könnyű oldalakon nagyon olcsó; Scrapy-natív. |
| **[Hyperbrowser](https://www.hyperbrowser.ai/pricing)** | n/a | free-tier: Free: 5 000 kredit, 1 párhuzamos session; Startup $30/hó… | True | `SDK + CDP` | Olcsó óradíj; agent-integrációk. |

#### CAPTCHA-feloldó szolgáltatás

| Eszköz | Verzió (dátum) | Hozzáférés / ár | Karbantartott | Telepítés | Mire jó |
|---|---|---|---|---|---|
| **[2Captcha / CapSolver / Anti-Captcha / CapMonster Cloud / NopeCHA](2captcha.com,)** | n/a | paid: 2Captcha: image $0.5–1, reCAPTCHA v2 $1–2.99, v3… | True | `REST API / SDK / böngésző-extension (pl. playwright-captcha integráció)` | Ott is működik, ahol a stealth böngésző elakad. |

### 9.3 Minimális kódminták (Python)

```python
# 1) curl_cffi – böngésző-TLS-t utánzó letöltés (pip install -U curl_cffi)
import curl_cffi
with curl_cffi.Session(impersonate="chrome") as s:
    r = s.get(URL, stream=True, timeout=120, headers={"Referer": ORIGIN})
    if r.status_code == 403 and r.headers.get("cf-mitigated") == "challenge":
        raise SystemExit("JS challenge -> Camoufox / Patchright / Byparr")
    r.raise_for_status()
    with open(OUT, "wb") as f:
        for chunk in r.iter_content():
            f.write(chunk)
```

```python
# 2) Camoufox – patchelt Firefox, Playwright API (pip install -U "camoufox[geoip]" && camoufox fetch)
from camoufox.sync_api import Camoufox
with Camoufox(headless=True, humanize=True) as browser:   # Linuxon headless="virtual" még jobb
    page = browser.new_page()
    page.goto(PAGE_URL, wait_until="domcontentloaded", timeout=90_000)
    page.wait_for_load_state("networkidle")
    with page.expect_download(timeout=120_000) as dl:
        try: page.goto(FILE_URL)
        except Exception: pass
    dl.value.save_as(OUT_DIR / dl.value.suggested_filename)
```

```python
# 3) Patchright – Playwright-kompatibilis, javított Chromium (pip install patchright && patchright install chrome)
from patchright.sync_api import sync_playwright
with sync_playwright() as p:
    ctx = p.chromium.launch_persistent_context("./profile", channel="chrome", headless=False, no_viewport=True, accept_downloads=True)
    page = ctx.new_page(); page.goto(ORIGIN, wait_until="networkidle")   # szerveren: xvfb-run
```

```python
# 4) Keresés: saját SearXNG (settings.yml: search.formats: [html, json]) vagy ddgs
import requests
r = requests.get("http://localhost:8888/search", params={"q": "sphere handbook filetype:pdf", "format": "json"}, timeout=30)
urls = [x["url"] for x in r.json()["results"]]

from ddgs import DDGS          # pip install -U ddgs
hits = DDGS(timeout=10).text("peace corps manual filetype:pdf", max_results=20)
```

A kódminták a projektek README-je és forráskódja alapján készültek, élesben nem futtak. Verzióváltáskor ellenőrizd az API-t.
