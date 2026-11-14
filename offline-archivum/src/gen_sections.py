#!/usr/bin/env python3
"""A 6. (LLM), 8. (kézi beszerzés) és 9. (webes hozzáférés) fejezet generálása a tételekből és a kutatási YAML-okból."""
import json, glob, sys
sys.path.insert(0, ".")
from llm_parse import load_blocks
from convert_research import load_yaml
from build import cut


OPUS = 59.1        # Claude Opus 5.5 (max) – AA Intelligence Index v5.0.1, 2026-11-12
FABLE = 64.6       # Claude Fable 5.2 (max) – az index csúcsa ugyanekkor
CODE = {"opus": 46, "deepseek-v4-1": 28}   # FrontierCode 2.0 (AA v5 kódolási kategória), %


def pct(aa):
    return f"{100 * aa / OPUS:.0f}%"


def esc(s):
    return str(s or "").replace("|", "\\|").replace("\n", " ")


def all_items():
    import fixes
    out = []
    for f in sorted(glob.glob("items_*.jsonl")):
        out += [json.loads(l) for l in open(f, encoding="utf-8") if l.strip()]
    return fixes.apply(out)


def gb(b):
    return f"{b / 1e12:.2f} TB" if b >= 1e12 else f"{b / 1e9:.1f} GB"


def llm_tables(items):
    llm = [i for i in items if i["cat"].startswith("ai_models") and "llm_aa" in i]
    groups = {}
    for v in llm:
        groups.setdefault(v["group"], []).append(v)
    rows, details = [], []
    order = sorted(groups.values(), key=lambda g: (g[0]["cat"] != "ai_models", -max(v["llm_aa"] for v in g)))
    for g in order:
        g.sort(key=lambda v: v["bytes"])
        h = g[0]
        name = h["name"].split(" · ")[0]
        aa = max(v["llm_aa"] for v in g)
        est = "~" if any(v.get("llm_aa_est") for v in g) else ""
        plats = ", ".join(sorted({v["platform"] for v in g}))
        tiers = sorted({t for v in g for t in v["hw_tiers"]}, key=lambda t: -int(t[1]))
        kind = "cenzúrázatlan" if h["cat"] == "ai_models_uncensored" else "alap"
        rows.append(f"| {esc(name)} | {kind} | {esc(cut(h.get('released'), 10))} | {est}{aa} | {est}{pct(aa)} | {esc(cut(h.get('license'), 24))} | "
                    f"{gb(g[0]['bytes'])} – {gb(g[-1]['bytes'])} | {len(g)} | {plats} | {tiers[0]}–{tiers[-1]} | `{h['group']}` |")
        det = [f"<details><summary><b>{esc(name)}</b> – {len(g)} változat</summary>\n",
               "| id | Fájl / repó | Méret | Bit | Min. memória (≈×1,15) | HW | Platform | Letöltés |", "|---|---|---|---|---|---|---|---|"]
        for v in g:
            d = v["download"]
            cmd = (f"`hf download {d['repo']}" + "".join(f' --include "{p}"' for p in d.get("include") or []) + "`") if d["method"] == "hf" \
                else f"`ollama pull {d.get('tag')}`"
            det.append(f"| `{v['id']}` | {esc(v['name'].split(' · ', 1)[1])} | {gb(v['bytes'])} | {v['llm_bits']} | {v['bytes'] * 1.15 / 1e9:.0f} GB | "
                       f"{','.join(v['hw_tiers'])} | {v['platform']} | {cmd} |")
        details.append("\n".join(det) + "\n</details>\n")
    head = ("| Modell | Típus | Kiadva | AA v5 | % Opus 5.5 | Licenc | Méret (min–max) | Változat | Platform | HW | group |\n"
            "|---|---|---|---|---|---|---|---|---|---|---|")
    return head + "\n" + "\n".join(rows), "\n".join(details)


def timeline():
    fr = load_blocks("research/llm_frontier.md.txt")[0]
    rows = ["| Gyártó | Legújabb nyílt modell | Kiadva (HF) | Paraméter (össz./aktív) | Kontextus | Licenc |", "|---|---|---|---|---|---|"]
    for m in fr:
        rows.append(f"| {esc(m.get('org'))} | [{esc(m.get('name'))}]({m.get('hf_repo')}) | {esc(cut(m.get('released'), 22))} | "
                    f"{esc(cut(m.get('params_total'), 40))} / {esc(cut(m.get('params_active'), 20))} | {esc(m.get('context'))} | {esc(cut(m.get('license'), 20))} |")
    return "\n".join(rows)


def runtimes():
    u = load_blocks("research/llm_uncensored_runtimes.md.txt")
    rts = next(b["runtimes"] for b in u[1:] if isinstance(b, dict) and "runtimes" in b)
    rows = ["| Runtime | Repó / forrás | Verzió | HW-szint | Megjegyzés |", "|---|---|---|---|---|"]
    for r in rts:
        tiers = r.get("tiers")
        tiers = ", ".join(map(str, tiers)) if isinstance(tiers, list) else esc(tiers)
        rows.append(f"| **{esc(r.get('name'))}** | {esc(cut(r.get('repo'), 90))} | {esc(cut(r.get('version'), 50))} | {tiers} | {esc(cut(r.get('notes'), 160))} |")
    return "\n".join(rows)


LLM_TEXT = """---

## 6. Helyi LLM-ek

**A fejezet tartalma:**
[6.1 Rangsor és kiadási idővonal](#61-kiadási-idővonal-mi-a-legújabb-gyártónként) ·
[6.2 Hardverszintek](#62-melyik-gépre-mi-kerüljön-hardverszintek) ·
[6.3 Az összes modell](#63-az-összes-modell-alap-és-cenzúrázatlan) ·
[6.4 Kvantok linkkel](#64-minden-kvantált-változat-linkkel-és-letöltési-paranccsal) ·
[6.5 Cenzúrázatlan modellek, rangsor, gépigény](#65-cenzúrázatlan-uncensored-változatok-mi-ez-és-mennyit-veszít) ·
[6.6 Futtatók](#66-futtatókörnyezetek-runtime-ok) ·
[6.7 Nulláról a chatig](#67-nulláról-a-chatig-szintenként) ·
[6.8 RAG](#68-offline-tudásbázis--llm-rag-hogy-az-llm-ne-találjon-ki-dolgokat) ·
[6.9 Kihagyott modellek](#69-kihagyott-régi-vagy-gyenge-modellek) ·
[6.10 Eszköz-kalkulátor](#610-eszköz-kalkulátor-mi-a-legokosabb-ami-elfér-és-elfut-4-változat) ·
[6.11 GeForce-feloldás](#611-geforce-ai-korlátozások-és-feloldásuk-rtx-30--60)

**Állapot:** 2026-11-14.
- **Csak a legújabb generáció:** gyártónként a legfrissebb nyílt súlyú kiadás van bent. A régi és felváltott modellek (Kimi K2/K3, DeepSeek V3/V4-Pro, Qwen3.5/3.6 nagyok, GLM-5.2, Llama 4, gpt-oss stb.) nem kerültek a katalógusba. Kivétel néhány cenzúrázatlan változat (Kimi-K3 abliterated, gpt-oss heretic, Qwen3.6-35B heretic), ahol újabb alapból még nincs ilyen. A teljes lista a 6.9 pontban van.
- **Forrás:** a repók, a dátumok és a méretek a Hugging Face API-ból és az Ollama registry-ből jönnek (mért adat).
- **Intelligencia:** Artificial Analysis Intelligence Index v5.0.1 (2026-11-12). A `~` jelű értékek becslések.

### 6.1 Kiadási idővonal: mi a legújabb gyártónként

{TIMELINE}

**Viszonyítási pont – Claude Opus 5.5 (max): 59,1 pont = 100%** (AA Intelligence Index v5.0.1, 2026-11-12). Az index csúcsa ugyanekkor a Claude Fable 5.2 (64,6 = 109%).

{COMBINED}

Az alapmodellek pontjai (csak alap, mért):

| Nyílt modell | AA v5.0.1 | % Opus 5.5 |
|---|---|---|
| Kimi K3.1 Pro | 46.5 | 79% |
| Hy4 (a végleges; mi a preview-t archiváljuk) | 34.6 | 59% |
| Qwen3.8 2.4T (becslés a Qwen3.8-Max API 33,7-es pontjából) | ~33.7 | ~57% |
| DeepSeek-V4.1-Flash-1017 | 32.6 | 55% |
| GLM-5.3 | 31.7 | 54% |
| Inkling 2 Small | 30.6 | 52% |
| MiMo-V2.6-Pro | 29.9 | 51% |
| Ling-3.1-flash | 29.6 | 50% |
| MiniMax-M3.1-Flash | 29.1 | 49% |
| Qwen3.8-Flash-Next | 28.6 | 48% |
| Step-5 Preview | 28.5 | 48% |
| GLM-5.3-Flash | 27.8 | 47% |
| MiMo-V2.6-Flash | 26.7 | 45% |
| Mistral Large 4 | 25.3 | 43% |
| Muse Spark Open | 24.9 | 42% |
| Qwen3.8-27B | 20.1 | 34% |
| Kimi K3 | 17.4 | 29% |
| Nemotron 3.5 Super VL | 13.6 | 23% |
| Muse Glimmer 30B | 6.3 | 11% |
| Nemotron 3.5 Lightning | 5.5 | 9% |
| Gemma 4 31B | 4.4 | 7% |
| gpt-oss-120b | 3.8 | 6% |

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
| **T5** | Telefon 8–16 GB RAM | 12–16 GB: Gemma-4-12B QAT q4_0 (7 GB). 8 GB: Gemma-4-E4B / E2B QAT (5,2 / 3,4 GB) | Qwen3.5-4B Q4_K_M (2,7 GB), LFM3-1.7B (1,1 GB) |

- **Ökölszabály:** a modellfájl mérete + 10–20% (KV cache) férjen el a memóriában.
- **Kódban:** `--hw T3 --mem 160GB` szűr, a `--platform mac|server` engedi az MLX vagy a vLLM-formátumokat. Alapból csak a mindenhol futó GGUF és Ollama formátum szerepel.
- **Magyar nyelv:** a Mistral Large 4 az egyetlen nagy modell, amelynek a kártyája kifejezetten az EU-nyelveket célozza. Kisebb gépen a Gemma 4 és a Qwen3.8-27B jó magyarul (becslés, magyar benchmark nincs).

### 6.3 Az összes modell (alap és cenzúrázatlan)

Az AA-index a modell legjobb változatára vonatkozik. A HW oszlop azt mutatja, mely hardverszinteken fut legalább egy változata.

{TABLE}

### 6.4 Minden kvantált változat linkkel és letöltési paranccsal

Kattints egy modellre a lenyitáshoz. A `hf download` parancsok változtatás nélkül futtathatók. A `--include` minta egy kvantot tölt le. Letöltés előtt a fájllistát érdemes ellenőrizni: `curl -s https://huggingface.co/api/models/<repo>/tree/main?recursive=true`.

{DETAILS}

### 6.5 Cenzúrázatlan („uncensored”) változatok: mi ez és mennyit veszít

- **Abliteration:** a modell aktivációiból kiszámolt „elutasítási irányt” kivetítik a súlyokból. Gyors, nem kell hozzá tanítás. Fő készítők: huihui-ai, mrfakename.
- **Heretic** (`p-e-w/heretic`, PyPI `heretic-llm`): automatikusan hangolt abliteration (ARA). Úgy minimalizálja az elutasítást, hogy közben az eredeti viselkedéstől való eltérés (KL) kicsi maradjon. **Offline is futtatható bármely modellen**, így egy új alapmodellből magad is készíthetsz cenzúrázatlant. Az ehhez kellő adathalmazok (`mlabonne/harmful_behaviors`, `mlabonne/harmless_alpaca`) kicsik, töltsd le őket előre.
- **Intelligenciaveszteség** (UGI NatInt mérések): nagy modellen (gemma-4-26B/31B, gpt-oss-120b, Qwen3.6-35B) ~0–2 pont, kicsin (9B–20B) akár 5–11 pont. Kis gépre ezért legyen meg az eredeti modell is.
- **Ajánlott párosítás:** egy alapmodell + egy cenzúrázatlan változat ugyanabból a családból. A szkript alapból ezt választja (`--uncensored also`). Csak cenzúrázatlan: `only`. Kihagyás: `no`.
- **A cenzúrázatlan modell nem megbízhatóbb.** Kevesebbet utasít el, de ugyanúgy hallucinál. Életveszélyes témában (gyógyszer, vegyi anyag, robbanóanyag, statika) a forrásdokumentum dönt.

{UNCRANK}

### 6.6 Futtatókörnyezetek (runtime-ok)

{RUNTIMES}

### 6.7 Nulláról a chatig, szintenként

Közös előkészület (online gépen, egyszer):
```bash
pip install -U huggingface_hub hf_xet            # a CLI neve: hf (a huggingface-cli megszűnt)
pip download open-webui -d wheels/               # Python 3.11-hez; offline: pip install --no-index -f wheels open-webui
git clone --mirror https://github.com/ggml-org/llama.cpp && git clone --mirror https://github.com/ikawrakow/ik_llama.cpp
# + a llama.cpp kész binárisai a platformodra (Releases oldal), a CUDA-runtime csomaggal együtt
```

**T1 – szerver**
1. `hf download moonshotai/Kimi-K3.1-Pro --local-dir /m/kimi` (natív INT4), vagy `deepseek-ai/DeepSeek-V4.1-Flash-1017` (510 GB).
2. `vllm serve /m/ds41 --tensor-parallel-size 8 --max-model-len 131072` (vagy SGLang). A wheeleket előre töltsd le: `pip download vllm -d wheels/`.
3. CPU-szerveren GGUF + llama.cpp:
   ```bash
   llama-server -m <első-shard>.gguf -c 65536 --jinja -fa on
   ```
4. Felület: Open WebUI `OFFLINE_MODE=true`, `OPENAI_API_BASE_URL=http://127.0.0.1:8080/v1`.

**T2 – workstation (Mac Studio 512 GB, 2× Mac, EPYC + GPU)**
1. Mac:
   ```bash
   hf download mlx-community/DeepSeek-V4.1-Flash-1017-oQ4e-mtp --local-dir /m/ds41
   mlx_lm.server --model /m/ds41 --port 8080
   ```
2. Több Mac: `exo` app (dashboard: `localhost:52415`), vagy `mlx.launch --backend jaccl --hostfile hosts.json …`.
3. EPYC + GPU: ik_llama.cpp vagy KTransformers, a MoE-szakértők a RAM-ban, a figyelem a GPU-n (`--n-cpu-moe N`, `-ot`).

**T3 – gamer PC**
1. Teljesen GPU-n (24 GB):
   ```bash
   hf download unsloth/Qwen3.8-27B-GGUF --include "*UD-Q4_K_XL*"
   llama-server -m Qwen3.8-27B-UD-Q4_K_XL.gguf -ngl 99 -c 32768 --jinja -fa on
   ```
2. Nagy MoE hibrid (128–192 GB RAM):
   ```bash
   hf download unsloth/Qwen3.8-Flash-Next-GGUF --include "*UD-Q4_K_XL*"
   llama-server -m <első-shard> -ngl 99 --n-cpu-moe 40 -c 32768 --jinja -fa on
   ```
   Az `--n-cpu-moe` értékét addig csökkentsd, amíg a VRAM még elég.
3. Grafikus felület: KoboldCpp (egyetlen exe), LM Studio vagy Jan.

**T4 – laptop**
- Mac: `mlx-community/Qwen3.8-27B-4bit` (16 GB) vagy 8bit (29,5 GB, 64 GB-os gépen), vagy LM Studio.
- Windows/Linux 16 GB VRAM: `Qwen3.8-27B UD-Q3_K_XL` (13 GB) vagy `Gemma-4-26B-A4B` QAT (14,4 GB, MoE, gyors).
- Beszéd:
  - whisper.cpp `large-v3-turbo-q5_0` (574 MB, magyarul is jó) beszédfelismeréshez;
  - Piper `hu_HU-anna-medium` (63 MB) felolvasáshoz.

**T5 – telefon**
- Android:
  - Telepítsd a PocketPal AI vagy a ChatterUI APK-t, másold a GGUF fájlt a telefonra, majd *Add local model*. Javasolt modell: Gemma-4-E4B QAT, 12B QAT vagy Qwen3.5-4B Q4_K_M.
  - A Google AI Edge Gallery a LiteRT (`.litertlm`) formátumot futtatja.
- iOS: PocketPal, LLM Farm, Locally AI (MLX). Mindegyik GGUF-ot vagy MLX-et tölt a Files appból.

### 6.8 Offline tudásbázis + LLM (RAG): hogy az LLM ne találjon ki dolgokat

1. `kiwix-serve --port 8888 /archivum/**/*.zim`: böngészőből olvasható a teljes ZIM-tár.
2. MCP-szerver a ZIM-ekhez (pl. `openzim-mcp`, PyPI): az LLM ebből keres és idéz.
3. Embedding-modell a PDF-ekhez:
   - `bge-m3` (GGUF Q8_0 0,63 GB, többnyelvű, magyarul is jó);
   - vagy `Qwen3-Embedding` 0.6B/4B/8B;
   - vagy `EmbeddingGemma 2`.
4. Open WebUI *Knowledge*: töltsd fel a 0. szintű PDF-eket (Hesperian, MSF, WHO), és a válaszok forráshivatkozással jönnek.

### 6.9 Kihagyott (régi vagy gyenge) modellek

- **Felváltott generációk:** Kimi-K3 és K2.x, DeepSeek-V4-Pro-0813 és V3.x, GLM-5.2 és korábbiak, MiniMax-M3 és M2.x, Qwen3.6/3.5 nagy modellek, Step-3.7, MiMo-V2.5, Ling-3.0, Hy3, Llama 4.
- **Gyenge az AA v5-ön:** gpt-oss-120b/20b (az alapmodell AA-pontja 3,8), Nemotron-3-Ultra, Command A+, Granite 4.2, Phi-4. Az ERNIE-5.5-ből csak base modell van.
- **Archívumcélra maradt bent:** a gpt-oss heretic-változata, mert kicsi, Apache-licencű és gyors.
"""

UNC_META = {  # id: (módszer, UGI / NatInt megjegyzés)
 "A1": ("Abliteration (huihui: 18 attn_output tenzor) + Heretic (pqhaz) + Abliteration FP8 (mrfakename)", "elutasítás 97→4% chat, 98→9% think; KL 0,067 (mrfakename kártya)"),
 "A2": ("Abliteration (huihui patch-GGUF az unsloth kvantra)", "nincs mérés"),
 "A3": ("Abliteration (huihui)", "nincs mérés"),
 "A4": ("Abliteration v2 (huihui)", "nincs mérés (Qwen3.8 még nincs az UGI-n)"),
 "A5": ("Abliteration (közösségi, Uniboshi)", "minőség nem ellenőrzött; gated:auto"),
 "A6": ("Abliteration (orcarouter)", "minőség nem ellenőrzött; gated:auto"),
 "A7": ("Heretic (MuXodious tainted-heresy / kldzj)", "UGI 53,81; NatInt 33,68→32,25 (−1,4)"),
 "A8": ("Heretic (darkc0de)", "az alap is engedékeny (UGI W10 4,5)"),
 "A9": ("Abliteration (huihui) / Heretic-ARA (trohrbaugh)", "nincs mérés"),
 "A10": ("SFT (propaganda-keretezés eltávolítása, az R1-1776 utódja)", "NEM általános elutasítás-eltávolító; propaganda 22%→0,9%"),
 "A11": ("Heretic (coder3101 / llmfan46)", "UGI 65,69 (legjobb 40B alatt); NatInt 38,91→36,53 (−2,4)"),
 "A12": ("Heretic, ultra (llmfan46)", "UGI 52,39; NatInt 34,44→35,71 (+1,3)"),
 "A13": ("Heretic (llmfan46) / Abliteration-MTP (huihui)", "UGI 50,9; NatInt 31,03→31,62 (+0,6)"),
 "A14": ("Heretic (MuXodious / p-e-w ARA)", "UGI 46,67; NatInt 27,18→22,52 (−4,7)"),
 "A15": ("Heretic (llmfan46) / Abliteration QAT (huihui)", "nincs mérés"),
 "A16": ("Heretic v2 (trohrbaugh)", "NatInt 30,98→24,2 (−6,8); huihui-változat: 19,8 (−11,2)"),
 "A17": ("Heretic 2.0 (p-e-w) / SOMPOA (MuXodious)", "SOMPOA: UGI 44,73; NatInt 23,88→22,35 (−1,5)"),
 "A18": ("Heretic (coder3101 / p-e-w)", "NatInt 18,21→18,73 (+0,5)"),
 "A19": ("Heretic, ultra (llmfan46)", "nincs mérés"),
}


MEASURED = ("deepseek-v4-1", "glm-5-3", "qwen3-8-flash-next", "kimi-k3", "minimax-m3-1", "gpt-oss-120b", "qwen3-8-27b", "gemma-4-31b")


def uncensored_ranking(items):
    from llm_to_items import UNC_BASE, slug
    res = load_blocks("research/llm_uncensored_runtimes.md.txt")[0]
    llm = [i for i in items if i["cat"] == "ai_models_uncensored" and "llm_aa" in i]
    rows = []
    for m in res:
        vs = sorted([i for i in llm if i["name"].split(" · ")[0] == m["name"]], key=lambda v: v["bytes"])
        base_aa = next((v for k, v in UNC_BASE if k in slug(m["name"])), None)
        sc = m.get("scores") or {}
        meth, ugi = UNC_META.get(m["id"], ("?", ""))
        best = {}
        for v in vs:
            for t in v["hw_tiers"]:
                if v["platform"] == "any" and (t not in best or v["llm_bits"] > best[t]["llm_bits"] or
                                               (v["llm_bits"] == best[t]["llm_bits"] and v["bytes"] < best[t]["bytes"])):
                    best[t] = v
        lowest = max(best, key=lambda t: int(t[1])) if best else None
        from llm_to_items import unc_estimate
        u_aa, _b, ratio, why, u_est = unc_estimate(slug(m["name"]))
        rows.append(dict(m=m, vs=vs, aa=base_aa, sc=sc, meth=meth, ugi=ugi, lowest=lowest, best=best, uaa=u_aa, ratio=ratio, why=why, uest=u_est))
    rows.sort(key=lambda r: (-(r["uaa"] or 0), -float(str(r["sc"].get("uncensored") or 0))))
    out = ["#### Rangsor: cenzúrázatlan modellek", "",
           "- **Sorrend:** a cenzúrázatlan változat *számolt* intelligenciája szerint (AA v5 skálán).",
           "- **Számolt pont:** az alapmodell AA v5 pontja × (cenzúrázatlan/alap) arány. Az arány „M” jelnél a UGI ranglista NatInt-méréséből jön. „B” jelnél becslés: nagy MoE abliteration 0,95–0,97, közösségi és nem ellenőrzött 0,93, kis dense 0,93.",
           "- **% Opus 5.5:** a számolt pont / 59,1 (Claude Opus 5.5 max, AA v5.0.1).",
           "- **„Cenz.” és „HU” oszlop:** 0–10-es kutatói becslés.",
           "- **`~` jel az AA oszlopban:** az alapmodellnek nincs AA v5 pontja, az érték becslés.",
           "- **UGI NatInt:** a természetes intelligencia mérése az Uncensored General Intelligence ranglistán, az alap → cenzúrázatlan változás.",
           "- **„Leggyengébb gép”:** az a legkisebb hardverszint, amelyen még fut GGUF-változat.",
           "- **Méretek:** a Hugging Face API-ból (2026-11-14).", "",
           "| # | Pontos név (repó) | Alapmodell (kiadva) | Paraméter | AA v5 alap | **AA v5 cenzúrázatlan (számolt)** | **% Opus 5.5** | Számítás | Módszer | Cenz. | HU | UGI / NatInt | Változat | Méret min–max | Leggyengébb gép | Licenc |",
           "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for n, r in enumerate(rows, 1):
        m, vs = r["m"], r["vs"]
        repo = m.get("hf_repo") or ""
        rname = repo.split("huggingface.co/")[-1]
        size = f"{gb(vs[0]['bytes'])} – {gb(vs[-1]['bytes'])}" if vs else "–"
        low = r["lowest"]
        lowtxt = f"{low}: `{r['best'][low]['download'].get('repo','')}` {r['best'][low]['download'].get('include') or ''} ({gb(r['best'][low]['bytes'])})" if low else "csak szerver / MLX"
        out.append(f"| {n} | **[{esc(rname)}]({repo})** | `{esc(m.get('base'))}` ({esc(m.get('base_created'))}) | {esc(cut(m.get('params'), 45))} | "
                   f"{('' if any(k in slug(m['name']) for k in MEASURED) else '~')}{r['aa'] if r['aa'] is not None else '?'} | "
                   f"**{'~' if r['uest'] else ''}{r['uaa']}** | **{'~' if r['uest'] else ''}{pct(r['uaa'])}** | × {r['ratio']:.3g} ({esc(r['why'])}) | {esc(r['meth'])} | {esc(r['sc'].get('uncensored'))} | {esc(r['sc'].get('multilingual_hu'))} | "
                   f"{esc(r['ugi'])} | {len(vs)} | {size} | {esc(lowtxt)} | {esc(cut(m.get('license'), 28))} |")
    out += ["",
            "**Hogyan olvasd:**",
            "- **Okosság:** az 1–4. hely a legokosabb, de ehhez szerver vagy nagy workstation kell.",
            "- **Gamer PC:** a legjobb választás a Qwen3.8-Flash-Next abliterated v2 (94–111 GB) és a Qwen3.8-27B abliterated (14–29 GB). Egyetlen videokártyán a Qwen3.8-27B abliterated fut.",
            "- **Laptop, telefon:** a Gemma-4 heretic változatai mért veszteség nélkül érhetők el.",
            "- **Arete-27B:** nem általános cenzúramentesítés, csak a propaganda-keretezést távolítja el.",
            "- **Kimi K3.1 Pro-ból nincs cenzúrázatlan változat.** A Kimi-K3 abliterated régebbi és gyengébb alapra épül (AA 17,4), a minősége nem ellenőrzött.",
            ""]
    return "\n".join(out)

# --- gépigény-számítás (becslés: memória = fájl x 1,15 + kontextus; sebesség = sávszélesség / aktív bájt tokenenként) ---
ACTIVE = {  # aktív paraméter (milliárd) a modellkártyák / kutatás alapján; None = ismeretlen
 "A1": 16, "A2": 40, "A3": 18, "A4": 6, "A5": 104, "A6": 23, "A7": 5.1, "A8": None, "A9": 27.8, "A10": 27.4,
 "A11": 31.3, "A12": 4, "A13": 3, "A14": 3.6, "A15": 12, "A16": 9.5, "A17": 4.6, "A18": 4.5, "A19": 2}
MOE = {"A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8", "A12", "A13", "A14"}
BW = {"RTX 4090": 1008, "RTX 5090": 1792, "M3 Ultra": 819, "M4 Max": 546, "EPYC 12ch DDR5": 460, "PC DDR5 2ch": 90, "telefon LPDDR5X": 70}


OVERHEAD_MS = {"RTX 4090": 6, "RTX 5090": 5, "M3 Ultra": 9, "M4 Max": 10, "EPYC 12ch DDR5": 12, "PC DDR5 2ch": 12, "telefon LPDDR5X": 25}


def tps(bw, active_b, bits, dev=None):
    """tok/s ≈ 1 / (aktív bájt / (0,6 x sávszél.) + fix tokenenkénti többletidő) – becslés, nem mérés."""
    if not active_b:
        return None
    dev = dev or next((k for k, v in BW.items() if v == bw), None)
    t = (active_b * 1e9 * bits / 8) / (0.6 * bw * 1e9) + OVERHEAD_MS.get(dev, 10) / 1000
    return 1 / t


def fmt_tps(x):
    return "–" if x is None else (f"~{x:.0f}" if x >= 3 else f"~{x:.1f}")


def hardware_table(items):
    from llm_to_items import slug
    res = load_blocks("research/llm_uncensored_runtimes.md.txt")[0]
    llm = [i for i in items if i["cat"] == "ai_models_uncensored" and "llm_aa" in i]
    rows = []
    for m in res:
        vs = sorted([i for i in llm if i["name"].split(" · ")[0] == m["name"]], key=lambda v: v["bytes"])
        if not vs:
            continue
        gg = [v for v in vs if v["platform"] == "any"] or vs
        q4 = [v for v in gg if 4 <= v["llm_bits"] <= 5]
        rec = max(q4, key=lambda v: v["bytes"]) if q4 else min(gg, key=lambda v: (abs(v["llm_bits"] - 4.5), v["bytes"]))
        other = sorted({f"{v['platform'].replace('server', 'szerver (vLLM/SGLang)').replace('mac', 'MLX')}: {gb(v['bytes'])} ({v['llm_bits']} bit)"
                        for v in vs if v["platform"] != "any"})
        small = gg[0]
        a = ACTIVE.get(m["id"]); moe = m["id"] in MOE
        mem = rec["bytes"] * 1.15 / 1e9
        vram_h = max(12, min(32, 0.12 * rec["bytes"] / 1e9 + 6)) if moe else None
        ram_h = mem - vram_h + 8 if moe else None
        gpu = f"{mem:.0f} GB VRAM" + (" (1 kártya)" if mem <= 32 else f" (pl. {int(-(-mem // 80))}×80 GB)" if mem > 48 else " (2 kártya)")
        hyb = f"{vram_h:.0f} GB VRAM + {ram_h:.0f} GB RAM" if moe else "dense: nem ajánlott (lassú)"
        mac = f"{max(16, mem * 1.05):.0f} GB unified" + (" (2× Mac, exo)" if mem > 480 else "")
        cpu = f"{mem + 8:.0f} GB RAM"
        b = rec["llm_bits"]
        sp_gpu = fmt_tps(tps(BW["RTX 4090"], a, b)) if mem <= 24 else (fmt_tps(tps(BW["RTX 5090"], a, b)) + " (5090)" if mem <= 32 else "–")
        sp_hyb = fmt_tps(tps(BW["PC DDR5 2ch"], a, b) * 1.6) if moe and a else "–"   # ~40% az aktív súlyból GPU-n (figyelem, shared expert)
        sp_mac = fmt_tps(tps(BW["M3 Ultra"], a, b)) if mem <= 500 else fmt_tps(tps(BW["M3 Ultra"], a, b) * 0.6) + " (2× Mac)"
        sp_epyc = fmt_tps(tps(BW["EPYC 12ch DDR5"], a, b))
        sp_phone = fmt_tps(tps(BW["telefon LPDDR5X"], a, b)) if mem <= 12 else "–"
        sc = m.get("scores") or {}
        from llm_to_items import UNC_BASE
        base_aa = next((v for k, v in UNC_BASE if k in slug(m["name"])), 0)
        rows.append((m, rec, small, a, moe, mem, gpu, hyb, mac, cpu, sp_gpu, sp_hyb, sp_mac, sp_epyc, sp_phone, "; ".join(other) or "–",
                     (-base_aa, -float(str(sc.get("uncensored") or 0)))))
    rows.sort(key=lambda r: r[-1])
    out = ["#### Gépigény: cenzúrázatlan modellek", "",
           "A számok **becslések** az alábbi szabályokkal:",
           "- **Memória:** fájlméret × 1,15 (KV cache ~16–32k kontextusig, futtatói overhead).",
           "- **Hibrid MoE:** a figyelmi rétegek és a KV cache a videokártyán, a szakértők a RAM-ban (`--n-cpu-moe`).",
           "- **Sebesség (generálás, 1 felhasználó):** tokenenként az aktív paraméterek bájtjait kell beolvasni. Képlet: tok/s ≈ 1 / (aktív bájt / (0,6 × sávszélesség) + fix többletidő). A többletidő GPU-n 5–6 ms, Macen 9, CPU-n 12, telefonon 25 ms.",
           "- **Sávszélességek:** RTX 4090 1008 GB/s, RTX 5090 1792, M3 Ultra 819, EPYC 12 csatornás DDR5 460, otthoni PC DDR5 kétcsatornás 90, telefon LPDDR5X 70.",
           "- **Mért adat:** nincs, ezek számolt értékek. A valós érték prompt-feldolgozáskor és hosszú kontextusnál alacsonyabb, MTP/speculative decodinggal magasabb lehet.",
           "- **Mac:** a macOS alapból a unified memória kb. 75%-át adja a GPU-nak. Ez emelhető: `sudo sysctl iogpu.wired_limit_mb=<MB>`.", "",
           "| # | Modell | Ajánlott GGUF-kvant (méret) | Archit. (aktív) | Csak GPU | Hibrid MoE (GPU+RAM) | Mac | Csak CPU | tok/s GPU | tok/s hibrid (DDR5 PC) | tok/s M3 Ultra | tok/s EPYC | tok/s telefon | Legkisebb kvant → min. memória | Egyéb formátum |",
           "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    from_rank = {}
    for n, (m, rec, small, a, moe, mem, gpu, hyb, mac, cpu, s1, s2, s3, s4, s5, oth, _k) in enumerate(rows, 1):
        inc = (rec["download"].get("include") or [""])[0]
        out.append(f"| {n} | **{esc(m['name'].split(' (')[0])}** | `{esc(inc) or 'teljes repó'}` {gb(rec['bytes'])} ({rec['llm_bits']} bit) | "
                   f"{'MoE' if moe else 'dense'}, {a if a else '?'}B aktív | {gpu} | {hyb} | {mac} | {cpu} | {s1} | {s2} | {s3} | {s4} | {s5} | "
                   f"`{esc((small['download'].get('include') or ['?'])[0])}` {gb(small['bytes'])} → {small['bytes'] * 1.15 / 1e9:.0f} GB | {esc(oth)} |")
    out += ["",
            "**Gyakorlati gépkonfigurációk:**",
            "",
            "| Gép | Memória | Mi fut rajta jól (cenzúrázatlan) |",
            "|---|---|---|",
            "| Telefon 8 GB | ~5 GB használható | Qwen3.5-4B heretic Q4_K_M (2,7 GB), Gemma-4-E2B heretic (3,4 GB) |",
            "| Telefon 12–16 GB | ~8–10 GB | Gemma-4-E4B heretic (5,3 GB), Qwen3.5-9B heretic Q4 (5,6 GB), Gemma-4-12B heretic (8,5 GB, 16 GB-on) |",
            "| Laptop 16 GB RAM + 8 GB VRAM | 24 GB | Gemma-4-26B-A4B heretic Q3_K_M (13,3 GB, MoE, gyors), gpt-oss-20b heresy (12,7 GB) |",
            "| MacBook 36–48 GB | 27–36 GB a GPU-nak | Gemma-4-31B heretic IQ4_XS (16,9 GB), Qwen3.8-27B abliterated Q4 (16,6 GB), Qwen3.6-35B-A3B heretic (21 GB) |",
            "| Gamer PC 24 GB VRAM + 64 GB RAM | 88 GB | Qwen3.8-27B abliterated Q6_K (22,4 GB, csak GPU), gpt-oss-120b heresy (63 GB, hibrid) |",
            "| Gamer PC 24–32 GB VRAM + 128 GB RAM | 152–160 GB | **Qwen3.8-Flash-Next abliterated v2 UD-IQ4_XS / UD-Q4_K_XL (94–111 GB, hibrid, 6B aktív → gyors)**; MiniMax-M3.1 abliterated (112 GB) |",
            "| Gamer PC 32 GB VRAM + 192 GB RAM | 224 GB | Qwen3.8-Flash-Next abliterated Q8_0 (188 GB) vagy GLM-5.3-Flash abliterated UD-Q4_K_XL (200 GB) |",
            "| Mac Studio 256 GB | ~240 GB (sysctl után) | GLM-5.3-Flash abliterated UD-Q4_K_XL (200 GB), Qwen3.8-Flash-Next abliterated Q8_0 (188 GB) |",
            "| Mac Studio 512 GB | ~490 GB | **DeepSeek-V4.1-Flash abliterated MLX (423 GB)**, GLM-5.3 abliterated (217 GB) |",
            "| EPYC 768 GB RAM + 1–2 GPU | 768+ GB | DeepSeek-V4.1-Flash heretic Q8_0 (508 GB), ik_llama.cpp vagy KTransformers |",
            "| 8×H100 (640 GB VRAM) | 640 GB | DeepSeek-V4.1-Flash abliterated FP8 (510 GB, vLLM/SGLang, a leggyorsabb) |",
            "| ≥1,6 TB RAM szerver | 1,6 TB+ | Kimi-K3 abliterated MXFP4 (1,51 TB); gyengébb, mint a DeepSeek-V4.1 |",
            ""]
    return "\n".join(out)


def manual_section(items):
    man = [i for i in items if i.get("access") in ("paid", "physical", "free-registration") or (i.get("download") or {}).get("method") == "manual"]
    man = [i for i in man if not i["cat"].startswith("ai_models")]
    W = {"S": .30, "R": .25, "A": .15, "U": .15, "Q": .10, "O": .05}
    sc = lambda i: round(sum(W[k] * (i.get("scores") or {}).get(k, 0) for k in W), 2)
    out = ["---", "", "## 8. Fizetős, regisztrációs és fizikai beszerzések", "",
           "Ezeket az AI nem tölti le automatikusan. Listázza őket, a döntés és a vásárlás vagy regisztráció az emberé. "
           "**A 0–1. szintű fizikai könyveket érdemes megvenni**, mert áram nélkül is olvashatók.", ""]
    for acc, title in (("physical", "Nyomtatott könyvek (vásárlás)"), ("paid", "Fizetős digitális termékek és szolgáltatások"),
                       ("free-registration", "Ingyenes, de regisztráció vagy bejelentkezés kell"), ("free", "Ingyenes, de kézi letöltés kell (nincs gépi út)"),
                       ("donation", "Adomány-alapú"), ("gray", "Jogi szürke zóna (alapból kizárva)")):
        rows = sorted([i for i in man if i["access"] == acc], key=lambda i: (i["tier"], -sc(i)))
        if not rows:
            continue
        out += [f"### {title}", "", "| T | Pont | Név | Mire jó | Ár | Link |", "|---|---|---|---|---|---|"]
        for i in rows:
            out.append(f"| {i['tier']} | {sc(i)} | **{esc(i.get('name'))}** | {esc(cut(i.get('desc_hu'), 180))} | {esc(cut(i.get('price'), 40))} | "
                       f"[link]({i.get('info_url') or (i.get('download') or {}).get('url') or ''}) |")
        out.append("")
    return "\n".join(out)


def web_section():
    tools = load_yaml("research/stealth_search.md.txt")
    kinds = {"stealth_browser": "Stealth böngésző / könyvtár", "tls_impersonation": "TLS-utánzás (böngésző nélkül)",
             "challenge_solver": "Challenge-feloldó proxy", "agent_framework": "Crawl / agent keretrendszer",
             "search_selfhosted": "Saját keresőszerver", "search_api": "Kereső API", "cloud_unblocker": "Felhős unblocker",
             "anti_detect_browser": "Kereskedelmi anti-detect böngésző", "captcha_solver": "CAPTCHA-feloldó szolgáltatás"}
    out = ["---", "", "## 9. Webes hozzáférés az AI-nak: captcha- és blokkmentes keresés és letöltés", "",
           "Egyes forrásoldalak (pl. ECHO, Peace Corps, Sphere, RepRap-wiki) Cloudflare-rel blokkolják a sima `curl`-t. "
           "Az alábbi eszközökkel az AI-ágens ezeket is le tudja tölteni, és API-n keres, nem Google-scrape-pel. "
           "A verziókat és a dátumokat a PyPI és az npm registry, valamint `git ls-remote` alapján ellenőrzött (2026-11-14).", "",
           "### 9.1 Lépcsőzetes stratégia: mindig a legolcsóbb működő réteggel kezdj", "",
           "1. **Diagnózis:**\n"
           "   - Ha nincs `cf-mitigated: challenge` header, a gond a TLS-ujjlenyomat: **curl_cffi** `impersonate=\"chrome\"`.\n"
           "   - Ha van challenge (\"Just a moment…\"), böngésző kell: **Camoufox** vagy **Patchright**.\n"
           "   - Ha minden 403, az IP a gond: residential proxy kell.",
           "2. Sok fájl ugyanarról a védett oldalról: **Byparr / FlareSolverr** (Docker, csak 127.0.0.1-re kötve) ad egy cookie-t és User-Agentet, ezekkel a curl_cffi tölt le. A cookie UA-hoz és IP-hez kötött.",
           "3. **Keresés:**\n"
           "   - saját **SearXNG** példány (JSON API) vagy **ddgs** (kulcs nélküli);\n"
           "   - megbízhatóbb, fizetős: **Brave Search API**, **Serper**, **Exa**, **Tavily**.\n"
           "   - A Bing Search API 2025-08-ban megszűnt, a Google Custom Search új ügyfélnek zárva van.",
           "4. **Megkerülés előtt alternatív forrás:**\n"
           "   - hivatalos tükör, kiadói repó, archive.org;\n"
           "   - `web.archive.org/web/2id_/<URL>`: az `id_` utótag a nyers eredeti fájlt adja.",
           "5. Csak végső esetben: felhős unblocker (Zyte, Bright Data, ZenRows, Scrapfly) vagy CAPTCHA-feloldó. Ez pénzbe kerül, harmadik fél látja az URL-eket, és ÁSZF-kockázatot jelent.",
           "6. **Udvariasság:**\n"
           "   - domainenként 1–2 kapcsolat, 2–10 s véletlen szünet;\n"
           "   - 429 / `Retry-After` esetén backoff;\n"
           "   - ugyanazt ne töltsd le kétszer;\n"
           "   - naplózd a forrást, a dátumot, a SHA-256-ot és a licencet.",
           "7. **Elavult, modern Cloudflare ellen nem működik:** cloudscraper, puppeteer-extra-plugin-stealth, undetected-chromedriver, playwright-stealth, hrequests.",
           "8. **MITM (TLS-t bontó) vállalati proxy mögött** a TLS-utánzás hatástalan. Ilyenkor böngésző vagy másik hálózat kell.", "",
           "### 9.2 Eszközök", ""]
    by = {}
    for t in tools:
        by.setdefault(t.get("kind"), []).append(t)
    for k, ts in by.items():
        out += [f"#### {kinds.get(k, k)}", "", "| Eszköz | Verzió (dátum) | Hozzáférés / ár | Karbantartott | Telepítés | Mire jó |", "|---|---|---|---|---|---|"]
        for t in ts:
            out.append(f"| **[{esc(t.get('name'))}]({str(t.get('repo_or_url') or '').split()[0]})** | {esc(cut(t.get('latest_version'), 50))} | "
                       f"{esc(t.get('access'))}: {esc(cut(t.get('price'), 60))} | {esc(cut(t.get('maintained'), 40))} | `{esc(cut(t.get('install'), 80))}` | {esc(cut(t.get('strengths_hu'), 150))} |")
        out.append("")
    out += ["### 9.3 Minimális kódminták (Python)", "",
            "```python\n# 1) curl_cffi – böngésző-TLS-t utánzó letöltés (pip install -U curl_cffi)\nimport curl_cffi\n"
            "with curl_cffi.Session(impersonate=\"chrome\") as s:\n    r = s.get(URL, stream=True, timeout=120, headers={\"Referer\": ORIGIN})\n"
            "    if r.status_code == 403 and r.headers.get(\"cf-mitigated\") == \"challenge\":\n        raise SystemExit(\"JS challenge -> Camoufox / Patchright / Byparr\")\n"
            "    r.raise_for_status()\n    with open(OUT, \"wb\") as f:\n        for chunk in r.iter_content():\n            f.write(chunk)\n```", "",
            "```python\n# 2) Camoufox – patchelt Firefox, Playwright API (pip install -U \"camoufox[geoip]\" && camoufox fetch)\n"
            "from camoufox.sync_api import Camoufox\nwith Camoufox(headless=True, humanize=True) as browser:   # Linuxon headless=\"virtual\" még jobb\n"
            "    page = browser.new_page()\n    page.goto(PAGE_URL, wait_until=\"domcontentloaded\", timeout=90_000)\n    page.wait_for_load_state(\"networkidle\")\n"
            "    with page.expect_download(timeout=120_000) as dl:\n        try: page.goto(FILE_URL)\n        except Exception: pass\n"
            "    dl.value.save_as(OUT_DIR / dl.value.suggested_filename)\n```", "",
            "```python\n# 3) Patchright – Playwright-kompatibilis, javított Chromium (pip install patchright && patchright install chrome)\n"
            "from patchright.sync_api import sync_playwright\nwith sync_playwright() as p:\n"
            "    ctx = p.chromium.launch_persistent_context(\"./profile\", channel=\"chrome\", headless=False, no_viewport=True, accept_downloads=True)\n"
            "    page = ctx.new_page(); page.goto(ORIGIN, wait_until=\"networkidle\")   # szerveren: xvfb-run\n```", "",
            "```python\n# 4) Keresés: saját SearXNG (settings.yml: search.formats: [html, json]) vagy ddgs\nimport requests\n"
            "r = requests.get(\"http://localhost:8888/search\", params={\"q\": \"sphere handbook filetype:pdf\", \"format\": \"json\"}, timeout=30)\n"
            "urls = [x[\"url\"] for x in r.json()[\"results\"]]\n\nfrom ddgs import DDGS          # pip install -U ddgs\n"
            "hits = DDGS(timeout=10).text(\"peace corps manual filetype:pdf\", max_results=20)\n```", "",
            "A kódminták a projektek README-je és forráskódja alapján készültek, élesben nem futtak. Verzióváltáskor ellenőrizd az API-t.", ""]
    return "\n".join(out)


def device_section():
    import llm_calc
    vs = llm_calc.load("../ARCHIVUM.md")
    groups = [("Telefonok", ["s24-ultra", "iphone-15-pro"]),
              ("Laptopok", ["pavilion-8", "pavilion-16", "zbook-g3a-192"]),
              ("AI workstation – MINISFORUM MS-S1 MAX-P495 (1, 2, 4 gép)", ["ms-s1-x1", "ms-s1-x2", "ms-s1-x4"]),
              ("Gamer PC – RTX 6090 + RAM-változatok", ["gamer-pc-96", "gamer-pc-128", "gamer-pc-192", "gamer-pc-256"]),
              ("Gamer PC – RTX 6090 + következő generációs RTX Pro (két kártya)", ["gamer-2gpu-pro96", "gamer-2gpu-pro128", "gamer-2gpu-pro192"]),
              ("Gamer PC – FELOLDVA (memória-OC; két kártyánál P2P + tensor parallel) – lásd 6.11", ["gamer-pc-128-unl", "gamer-pc-256-unl", "gamer-2gpu-pro96-unl", "gamer-2gpu-pro128-unl", "gamer-2gpu-pro192-unl"]),
              ("Linux szerverek", ["srv-epyc", "srv-8xh200"])]
    out = ["### 6.10 Eszköz-kalkulátor: mi a legokosabb, ami elfér és elfut (4 változat)", "",
           "A `llm_calc.py` (**12. fejezet**) bármely eszközre kiszámolja a négy változatot:",
           "- **V1:** a legokosabb **cenzúrázatlan** modell, ami épp elfér és elfut.",
           "- **V2:** a legokosabb **alap (cenzúrázott)** modell, ami épp elfér és elfut.",
           "- **V3 – csapat alap modellekből:** egy nagy fő modell és egy kicsi, gyors segéd egyszerre a memóriában. A segéd routerként, gyors válaszolóként vagy draftként dolgozik. Mellettük egy RAG-embedding is fut (bge-m3).",
           "- **V4 – vegyes csapat:** egy alap és egy cenzúrázatlan modell együtt. Ha még befér, egy gyors segéd és a RAG-embedding is.",
           "",
           "**Ha két modell nem fér el egyszerre** (például telefonon), a kalkulátor *váltott csapatot* ad: a tárhelyen mindkét modell ott van, és mindig az éppen szükséges töltődik be (néhány másodperc).", "",
           "**Becslés, nem mérés:**",
           "- **Memória:** fájl × 1,15 + 1 GB.",
           "- **Sebesség:** a memória-sávszélességből és az aktív paraméterszámból (lásd 6.5).",
           "- **„Okosság”:** az AA v5 index × a kvantminőség szorzója. A dense modelleket 2,5 bit alatt kizárja.",
           "- **Döntés:** a legokosabb modell nyer, kis sebesség-bónusszal (legfeljebb +20%).",
           "- **„Elfut”:** legalább 5 tok/s (telefonon és régi laptopon 4).",
           "- **Közel azonos alternatíva:** a legjobb pontszám ≥95%-a, más modellcsaládból.", "",
           "**Saját eszközre:**",
           "```bash",
           "sed -n '/^```python llm_calc.py$/,/^```$/p' ARCHIVUM.md | sed '1d;$d' > llm_calc.py",
           "python3 llm_calc.py ARCHIVUM.md --name \"Saját PC\" --gpu 24:1008 --ram 128 --ram-bw 90 --formats any,server --md",
           "python3 llm_calc.py ARCHIVUM.md --name \"Mac Studio\" --unified 512 --unified-usable 0.92 --unified-bw 819 --formats any,mac",
           "python3 llm_calc.py ARCHIVUM.md --preset all --md      # minden alábbi profil",
           "```", "",
           "**Hardveradatok és feltételezések:**",
           "- **MS-S1 MAX-P495 és ZBook Ultra G3a:** 192 GB LPDDR5X; a GPU-nak legfeljebb 160 GB adható (gyártói adat). A ~256–273 GB/s sávszélességet a memóriasebességből és a 256 bites buszból számoltam.",
           "- **RTX 6090:** még nincs bejelentve. A pletykák szerint 32 GB GDDR7 és ~1,79 TB/s.",
           "- **Következő generációs RTX Pro:** semmilyen hivatalos adat nincs róla, ezért a kalkulátor három forgatókönyvvel számol: 96, 128 és 192 GB.",
           "- **Pavilion 15-bc504ur:** az i5-9300H + GTX 1050 4 GB a bc504TX testvérmodell adatlapjából jön.",
           "- **Telefonok:** a modellnek jutó memória becslés (az OS és az appok levonva).",
           "- **Klaszter (2 vagy 4 MS-S1):** llama.cpp RPC vagy exo pipeline-párhuzamosítás USB4 v2 (80 Gbps) gyűrűn. A kapacitás összeadódik, a sebesség nagyjából egy gépé, plusz ~3 ms hálózati késleltetés gépenként.", ""]
    for title, keys in groups:
        out.append(f"#### {title}\n")
        for k in keys:
            d = llm_calc.Device(**llm_calc.PRESETS[k])
            out.append(llm_calc.report(d, llm_calc.evaluate(d, vs), md=True))
    out += ["**Gyakorlati tanácsok a csapathoz:**",
            "- **Futtatás:** minden modell külön `llama-server` példányként fut, külön porton (pl. 8080 = fő, 8081 = partner, 8082 = segéd, 8083 = embedding).",
            "- **Közös felület:** az Open WebUI mindet egy felületen kezeli, és modellenként választható. Router-logika: egyszerű kérdés → gyors segéd; nehéz → fő modell; elutasított vagy érzékeny téma → cenzúrázatlan partner.",
            "- **Ellenőrzés:** a fontos válaszokat érdemes a másik modellel is ellenőriztetni („második vélemény”). Orvosi, vegyi és szerkezeti témában a RAG-forrásdokumentum dönt.",
            "- **Klaszter:** gépenként `rpc-server`, a fő gépen pedig `llama-server --rpc host2:50052,host3:50052 …`. A gépek USB4 v2 (Thunderbolt-hálózat) vagy 10GbE kapcsolaton át kommunikálnak.",
            "- **Két különböző videokártya:**\n"
            "  - Rétegenként osztja szét a modellt a `-ts 32,96` (tensor-split, a VRAM arányában) és a `-sm layer` kapcsoló.\n"
            "  - A nagyobb kártya legyen a `--main-gpu`.\n"
            "  - A két kártya nem kell, hogy azonos generációjú legyen (CUDA mindkettő).", ""]
    return "\n".join(out)


def combined_ranking():
    """6.1: közös rangsor – alap (mért AA) + cenzúrázatlan (számolt AA)."""
    from llm_to_items import unc_estimate, slug, AA, AA_EST
    fr = load_blocks("research/llm_frontier.md.txt")[0]
    un = load_blocks("research/llm_uncensored_runtimes.md.txt")[0]
    rows = []
    small = {"gemma-4": [("Gemma-4-31B", 4.4, False), ("Gemma-4-26B-A4B", 3.5, True), ("Gemma-4-12B", 3.0, True), ("Gemma-4-E4B", 2.5, True), ("Gemma-4-E2B", 1.5, True)],
             "nemotron-3-5": [("Nemotron-3.5-Super-VL-120B", 13.6, False), ("Nemotron-3.5-Lightning-30B", 5.5, False), ("Nemotron-3.5-Bolt-E4B", 2.5, True)],
             "qwen3-5-small": [("Qwen3.5-9B", 3.0, True), ("Qwen3.5-4B", 2.0, True)],
             "mimo-v2-6-pro": [("MiMo-V2.6-Pro", 29.9, False), ("MiMo-V2.6-Flash", 26.7, False)]}
    for m in fr:
        mid = slug(m.get("id"))
        if mid in small:
            for n, a, e in small[mid]:
                rows.append((a, e, n, "alap", "mért AA v5" if not e else "becslés (nincs AA-pont)"))
        elif mid in AA:
            rows.append((AA[mid], mid in AA_EST, m["name"], "alap", "mért AA v5" if mid not in AA_EST else "becslés"))
    for m in un:
        a, base, r, why, e = unc_estimate(slug(m["name"]))
        rows.append((a, e, m["name"].split(" (")[0], "**cenzúrázatlan**", f"alap {base} × {r:.3g} – {why}"))
    rows.sort(key=lambda x: -x[0])
    out = ["| # | Modell | Típus | AA v5 | % Opus 5.5 | Forrás / számítás |", "|---|---|---|---|---|---|",
           f"| – | *Claude Fable 5.2 (zárt, viszonyítás)* | zárt | 64.6 | 109% | mért |",
           f"| – | *Claude Opus 5.5 (zárt, viszonyítás)* | zárt | 59.1 | 100% | mért |"]
    for i, (a, e, n, t, src) in enumerate(rows, 1):
        out.append(f"| {i} | {esc(n)} | {t} | {'~' if e else ''}{a} | {'~' if e else ''}{pct(a)} | {esc(src)} |")
    return "\n".join(out)


def main():
    items = all_items()
    table, details = llm_tables(items)
    txt = LLM_TEXT.replace("{COMBINED}", combined_ranking()).replace("{TIMELINE}", timeline()).replace("{TABLE}", table).replace("{DETAILS}", details).replace("{RUNTIMES}", runtimes()).replace("{UNCRANK}", uncensored_ranking(items) + "\n\n" + hardware_table(items))
    txt = txt.rstrip() + "\n\n" + device_section()   # 6.10 a 6.9 után
    open("sections/06_llm.md", "w", encoding="utf-8").write(txt)
    open("sections/08_manual.md", "w", encoding="utf-8").write(manual_section(items))
    open("sections/09_web.md", "w", encoding="utf-8").write(web_section())
    print("OK: 06_llm.md, 08_manual.md, 09_web.md")


if __name__ == "__main__":
    main()
