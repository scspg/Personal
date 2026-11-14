---

## 6. Helyi LLM-ek

**Állapot:** 2026-11-14.
- **Csak a legújabb generáció:** gyártónként a legfrissebb nyílt súlyú kiadás van bent. A régi és felváltott modellek (Kimi K2/K3, DeepSeek V3/V4-Pro, Qwen3.5/3.6 nagyok, GLM-5.2, Llama 4, gpt-oss stb.) nem kerültek a katalógusba (lista a 6.9 pontban).
- **Forrás:** a repók, a dátumok és a méretek a Hugging Face API-ból és az Ollama registry-ből jönnek (mért adat).
- **Intelligencia:** Artificial Analysis Intelligence Index v5.0.1 (2026-11-12). A `~` jelű értékek becslések.

### 6.1 Kiadási idővonal: mi a legújabb gyártónként

| Gyártó | Legújabb nyílt modell | Kiadva (HF) | Paraméter (össz./aktív) | Kontextus | Licenc |
|---|---|---|---|---|---|
| Moonshot AI | [Kimi K3.1 Pro](https://huggingface.co/moonshotai/Kimi-K3.1-Pro) | 2026-11-02 | 2.8T / 104B | 1048576 | Kimi K3.1 Pro Licens |
| DeepSeek | [DeepSeek-V4.1-Flash-1017](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017) | 2026-10-17 | 552B backbone + 196B Engram memória (763 / ~16B (harmadik fél,  | 1000000 | MIT |
| Zhipu AI (Z.ai) | [GLM-5.3](https://huggingface.co/zai-org/GLM-5.3) | 2026-08-25 | 753B / ~40B (harmadik fél) | 1M (eval-beállítások és harmadik fél alapján) | GLM-5.3 custom licen |
| Zhipu AI | [GLM-5.3-Flash](https://huggingface.co/zai-org/GLM-5.3-Flash) | 2026-08-25 | 320B (321.3B) / 18B | ~1M (eval 1M kontextussal; a kártyán nincs explicit tábla) | MIT |
| Xiaomi | [MiMo-V2.6-Pro (RL és MOPD változat) + MiMo-V2.6-Flash](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro-RL) | 2026-09-21 (RL), 2026- | Pro 1.02T; Flash 309B / Pro 42B; Flash 15B | 1000000 | MIT |
| inclusionAI (Ant Group) | [Ling-3.1-flash-1019](https://huggingface.co/inclusionAI/Ling-3.1-flash-1019) | 2026-10-27 | 560B (572B tárolt) / 25B | 1000000 | MIT |
| MiniMax | [MiniMax-M3.1-Flash](https://huggingface.co/MiniMaxAI/MiniMax-M3.1-Flash) | 2026-10-17 | ~428B / 23B | 1000000 | MiniMax Community Li |
| Alibaba Qwen | [Qwen3.8-Flash-Next](https://huggingface.co/Qwen/Qwen3.8-Flash-Next) | 2026-08-24 | 180B = 125B MoE + 51B n-gram embedding + / 6B | 262144 natív, 1M-ig bővíthető | Qwen Community Licen |
| Alibaba Qwen | [Qwen3.8-2.4T-A95B (a hostolt „Qwen3.8-Max” alapja)](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B) | 2026-08-08 | 2.4T / 95B | 262144 natív, 1,010,000-ig bővíthető | Qwen3.8-Max license  |
| StepFun | [Step 5 Preview](https://huggingface.co/stepfun-ai/Step-5-Preview) | 2026-09-20 | 600B / 27B | 1M-ig | StepFun Model Licens |
| Thinking Machines Lab | [Inkling 2 Small](https://huggingface.co/thinkingmachines/Inkling-2-Small) | 2026-11-04 | 594B / 17B | 1000000 | Apache-2.0 |
| Tencent | [Hy4 preview (Hunyuan)](https://huggingface.co/tencent/Hy4-preview) | 2026-08-27 | 770B (+10B MTP) / 49B | 1000000 | Apache-2.0 |
| Mistral AI | [Mistral Large 4 (1T-A52B)](https://huggingface.co/mistralai/Mistral-Large-4-1T-A52B) | 2026-09-30 | ~1T / 49B (52B embeddingek | 1000000 | Mistral Ecosystem Op |
| Meta (meta-models) | [Muse Spark Open (816B-A42B)](https://huggingface.co/meta-models/Muse-Spark-Open-816B-A42B) | 2026-09-15 (HF repó);  | 816B / 42B | 1000000 | Muse Model License;  |
| Alibaba Qwen | [Qwen3.8-27B (dense)](https://huggingface.co/Qwen/Qwen3.8-27B) | 2026-08-05 | 27.8B / 27.8B (dense) | 262144 natív, 1M-ig bővíthető | Apache-2.0 |
| Meta | [Muse Glimmer 30B](https://huggingface.co/meta-models/Muse-Glimmer-30B) | 2026-08-09 | 29.6B (dense, vision encoderrel együtt) / 29.6B | 131072+ | Apache-2.0 |
| Google DeepMind | [Gemma 4 (31B, 26B-A4B, 12B, E4B, E2B)](https://huggingface.co/google/gemma-4-31B-it) | E2B/E4B 2026-03-02; 26 | 31B dense (30.7B); 26B MoE (A4B); 11.95B / 31B; ~4B; 12B; 4.5B; | 256K (12B/26B/31B), 128K (E2B/E4B) | Apache-2.0 |
| NVIDIA | [NVIDIA Nemotron 3.5 (Super-VL-120B-A12B, Lightning-30B-A3B, Bolt-E4B)](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-BF16) | Super-VL 2026-10-12; B | 124B; 31.6B; 8B (4B eff., Gemma 4 alapú) / 12B; 3B; 4B | Super-VL: [nem ellenőrzött]; Lightning: 1M-ig (H100-on 256K); Bolt-E4B: 64K | OpenMDW-1.1 (nyílt s |
| Alibaba Qwen / Xiaomi | [Qwen3.5-4B / Qwen3.5-9B (+ MiMo-V2.6-Distill-Qwen-9B)](https://huggingface.co/Qwen/Qwen3.5-4B) | 2026-02-27 (Qwen3.5);  | 4B; 9B / dense | [nem ellenőrzött] | Apache-2.0 (Qwen3.5) |
| Meituan | [LongCat-2.5 (csak megjegyzésként)](https://huggingface.co/meituan-longcat/LongCat-2.5) | 2026-11-04 | 1.6T (1.78T tárolt) / ~48B | [nem ellenőrzött] | MIT |

**Viszonyítási pont – Claude Opus 5.5 (max): 59,1 pont = 100%** (AA Intelligence Index v5.0.1, 2026-11-12). Az index csúcsa ugyanekkor a Claude Fable 5.2 (64,6 = 109%).

| # | Modell | Típus | AA v5 | % Opus 5.5 | Forrás / számítás |
|---|---|---|---|---|---|
| – | *Claude Fable 5.2 (zárt, viszonyítás)* | zárt | 64.6 | 109% | mért |
| – | *Claude Opus 5.5 (zárt, viszonyítás)* | zárt | 59.1 | 100% | mért |
| 1 | Kimi K3.1 Pro | alap | 46.5 | 79% | mért AA v5 |
| 2 | Hy4 preview (Hunyuan) | alap | ~34.6 | ~59% | becslés |
| 3 | Qwen3.8-2.4T-A95B (a hostolt „Qwen3.8-Max” alapja) | alap | ~33.7 | ~57% | becslés |
| 4 | DeepSeek-V4.1-Flash-1017 | alap | 32.6 | 55% | mért AA v5 |
| 5 | GLM-5.3 | alap | 31.7 | 54% | mért AA v5 |
| 6 | DeepSeek-V4.1-Flash-1017 abliterated (cenz.-mentes) | **cenzúrázatlan** | ~31.6 | ~53% | alap 32.6 × 0.97 – B: abliteration, KL 0,067 (kicsi eltérés), nagy MoE |
| 7 | Inkling 2 Small | alap | 30.6 | 52% | mért AA v5 |
| 8 | GLM-5.3 abliterated (cenz.-mentes) | **cenzúrázatlan** | ~30.1 | ~51% | alap 31.7 × 0.95 – B: abliteration (patch), nagy MoE |
| 9 | LongCat-2.5 (csak megjegyzésként) | alap | ~30.0 | ~51% | becslés |
| 10 | MiMo-V2.6-Pro | alap | 29.9 | 51% | mért AA v5 |
| 11 | Ling-3.1-flash-1019 | alap | 29.6 | 50% | mért AA v5 |
| 12 | MiniMax-M3.1-Flash | alap | 29.1 | 49% | mért AA v5 |
| 13 | Qwen3.8-Flash-Next | alap | 28.6 | 48% | mért AA v5 |
| 14 | Step 5 Preview | alap | 28.5 | 48% | mért AA v5 |
| 15 | GLM-5.3-Flash | alap | 27.8 | 47% | mért AA v5 |
| 16 | Qwen3.8-Flash-Next abliterated v2 (cenz.-mentes) | **cenzúrázatlan** | ~27.2 | ~46% | alap 28.6 × 0.95 – B: abliteration v2, nagy MoE |
| 17 | MiniMax-M3.1-Flash abliterated (cenz.-mentes) | **cenzúrázatlan** | ~27.1 | ~46% | alap 29.1 × 0.93 – B: közösségi abliteration, nem ellenőrzött |
| 18 | MiMo-V2.6-Flash | alap | 26.7 | 45% | mért AA v5 |
| 19 | GLM-5.3-Flash abliterated (cenz.-mentes) | **cenzúrázatlan** | ~26.4 | ~45% | alap 27.8 × 0.95 – B: abliteration, nagy MoE |
| 20 | Mistral Large 4 (1T-A52B) | alap | 25.3 | 43% | mért AA v5 |
| 21 | Muse Spark Open (816B-A42B) | alap | 24.9 | 42% | mért AA v5 |
| 22 | Qwen3.8-27B (dense) | alap | 20.1 | 34% | mért AA v5 |
| 23 | NousResearch Arete-27B (cenz.-mentes) | **cenzúrázatlan** | ~19.0 | ~32% | alap 19.0 × 1 – B: SFT, csak propaganda-szűrés |
| 24 | Qwen3.8-27B abliterated (cenz.-mentes) | **cenzúrázatlan** | ~18.7 | ~32% | alap 20.1 × 0.93 – B: abliteration, közepes dense |
| 25 | Kimi-K3 Abliterated V1 (cenz.-mentes) | **cenzúrázatlan** | ~16.2 | ~27% | alap 17.4 × 0.93 – B: közösségi abliteration, minőség nem ellenőrzött |
| 26 | Nemotron-3.5-Super-VL-120B | alap | 13.6 | 23% | mért AA v5 |
| 27 | Qwen3.6-35B-A3B uncensored-heretic (cenz.-mentes) | **cenzúrázatlan** | ~8.0 | ~14% | alap 8.0 × 1 – M: NatInt 31,03→31,62 (nincs veszteség) |
| 28 | Mistral-Small-4-119B-2603 heretic (cenz.-mentes) | **cenzúrázatlan** | ~7.6 | ~13% | alap 8.0 × 0.95 – B: heretic, MoE |
| 29 | Muse Glimmer 30B | alap | 6.3 | 11% | mért AA v5 |
| 30 | Nemotron-3.5-Lightning-30B | alap | 5.5 | 9% | mért AA v5 |
| 31 | Gemma-4-31B | alap | 4.4 | 7% | mért AA v5 |
| 32 | gemma-4-31B-it heretic (cenz.-mentes) | **cenzúrázatlan** | 4.1 | 7% | alap 4.4 × 0.939 – M: NatInt 38,91→36,53 |
| 33 | gpt-oss-120b heretic (cenz.-mentes) | **cenzúrázatlan** | 3.6 | 6% | alap 3.8 × 0.958 – M: NatInt 33,68→32,25 |
| 34 | Gemma-4-26B-A4B | alap | ~3.5 | ~6% | becslés (nincs AA-pont) |
| 35 | gemma-4-26B-A4B-it ultra-uncensored-heretic (cenz.-mentes) | **cenzúrázatlan** | ~3.5 | ~6% | alap 3.5 × 1 – M: NatInt 34,44→35,71 (nincs veszteség) |
| 36 | Gemma-4-12B | alap | ~3.0 | ~5% | becslés (nincs AA-pont) |
| 37 | Qwen3.5-9B | alap | ~3.0 | ~5% | becslés (nincs AA-pont) |
| 38 | gemma-4-12B-it uncensored-heretic (cenz.-mentes) | **cenzúrázatlan** | ~2.8 | ~5% | alap 3.0 × 0.93 – B: heretic, kis dense |
| 39 | Gemma-4-E4B | alap | ~2.5 | ~4% | becslés (nincs AA-pont) |
| 40 | Nemotron-3.5-Bolt-E4B | alap | ~2.5 | ~4% | becslés (nincs AA-pont) |
| 41 | gemma-4-E4B-it heretic (cenz.-mentes) | **cenzúrázatlan** | ~2.5 | ~4% | alap 2.5 × 1 – M: NatInt 18,21→18,73 (nincs veszteség) |
| 42 | Qwen3.5-9B heretic-v2 (cenz.-mentes) | **cenzúrázatlan** | ~2.3 | ~4% | alap 3.0 × 0.781 – M: NatInt 30,98→24,2 |
| 43 | gpt-oss-20b heretic (cenz.-mentes) | **cenzúrázatlan** | ~2.1 | ~4% | alap 2.5 × 0.829 – M: NatInt 27,18→22,52 |
| 44 | Qwen3.5-4B | alap | ~2.0 | ~3% | becslés (nincs AA-pont) |
| 45 | Qwen3.5-4B heretic-2.0 (cenz.-mentes) | **cenzúrázatlan** | ~1.9 | ~3% | alap 2.0 × 0.936 – M: NatInt 23,88→22,35 (SOMPOA-változat) |
| 46 | Gemma-4-E2B | alap | ~1.5 | ~3% | becslés (nincs AA-pont) |
| 47 | gemma-4-E2B-it ultra-uncensored-heretic (cenz.-mentes) | **cenzúrázatlan** | ~1.4 | ~2% | alap 1.5 × 0.93 – B: heretic, nagyon kis modell |

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
| **T2** | 400–1000 GB unified/RAM (Mac Studio 512 GB, 2× Mac exo, EPYC 768 GB + GPU, DGX Station) | 512 GB Mac: DeepSeek-V4.1-Flash MLX oQ4e (432 GB). 2× Mac / 768 GB+: Kimi K3.1 Pro KLX-IQ2_XXS (710 GB) | GLM-5.3 MLX 4bit (418 GB); MiniMax-M3.1-Flash oQ4e (249 GB) |
| **T3** | Gamer PC 24–32 GB VRAM + 64–192 GB RAM | 128–192 GB RAM: Qwen3.8-Flash-Next UD-Q4_K_XL (111 GB) MoE-offloaddal. Csak GPU: Qwen3.8-27B Q4/Q5 (17–20 GB) | GLM-5.3-Flash UD-Q3_K_XL (148 GB); Gemma-4-31B QAT (17,7 GB) |
| **T4** | Laptop: MacBook 36–128 GB, vagy Windows 8–16 GB VRAM | 64 GB Mac: Qwen3.8-27B MLX 8bit (29,5 GB). 16 GB VRAM: Qwen3.8-27B UD-Q3_K_XL (13 GB) | Gemma-4-26B-A4B (gyors MoE), Gemma-4-12B QAT (7 GB) |
| **T5** | Telefon 8–16 GB RAM | 12–16 GB: Gemma-4-12B QAT q4_0 (7 GB). 8 GB: Gemma-4-E4B / E2B QAT (5,2 / 3,4 GB) | Qwen3.5-4B Q4_K_M (2,7 GB), LFM3-1.7B (1,1 GB) |

- **Ökölszabály:** a modellfájl mérete + 10–20% (KV cache) férjen el a memóriában.
- **Kódban:** `--hw T3 --mem 160GB` szűr, a `--platform mac|server` engedi az MLX vagy a vLLM-formátumokat. Alapból csak a mindenhol futó GGUF és Ollama formátum szerepel.
- **Magyar nyelv:** a Mistral Large 4 az egyetlen nagy modell, amelynek a kártyája kifejezetten az EU-nyelveket célozza. Kisebb gépen a Gemma 4 és a Qwen3.8-27B jó magyarul (becslés, magyar benchmark nincs).

### 6.3 Az összes modell (alap és cenzúrázatlan)

Az AA-index a modell legjobb változatára vonatkozik. A HW oszlop azt mutatja, mely hardverszinteken fut legalább egy változata.

| Modell | Típus | Kiadva | AA v5 | % Opus 5.5 | Licenc | Méret (min–max) | Változat | Platform | HW | group |
|---|---|---|---|---|---|---|---|---|---|---|
| Kimi K3.1 Pro | alap | 2026-11-02 | 46.5 | 79% | Kimi K3.1 Pro License (c | 592.7 GB – 1.61 TB | 9 | any, mac, server | T2–T1 | `llm-kimi-k3-1-pro` |
| Hy4 preview (Hunyuan) | alap | 2026-08-27 | ~34.6 | ~59% | Apache-2.0 | 229.4 GB – 1.56 TB | 6 | any, mac, server | T2–T1 | `llm-hy4-preview` |
| Qwen3.8-2.4T-A95B (a hostolt „Qwen3.8-Max” alapja) | alap | 2026-08-08 | ~33.7 | ~57% | Qwen3.8-Max license (oth | 397.3 GB – 4.89 TB | 12 | any, server | T2–T1 | `llm-qwen3-8-2-4t-a95b` |
| DeepSeek-V4.1-Flash-1017 | alap | 2026-10-17 | 32.6 | 55% | MIT | 120.7 GB – 510.3 GB | 23 | any, mac, server | T3–T1 | `llm-deepseek-v4-1-flash-1017` |
| GLM-5.3 | alap | 2026-08-25 | 31.7 | 54% | GLM-5.3 custom license ( | 211.1 GB – 1.51 TB | 25 | any, mac, server | T3–T1 | `llm-glm-5-3` |
| Inkling 2 Small | alap | 2026-11-04 | 30.6 | 52% | Apache-2.0 | 341.5 GB – 968.8 GB | 13 | any, mac, server | T2–T1 | `llm-inkling-2-small` |
| LongCat-2.5 (csak megjegyzésként) | alap | 2026-11-04 | ~30.0 | ~51% | MIT | 1.34 TB – 1.34 TB | 1 | server | T1–T1 | `llm-longcat-2-5` |
| MiMo-V2.6-Pro (RL és MOPD változat) + MiMo-V2.6-Flash | alap | 2026-09-21 | 29.9 | 51% | MIT | 126.4 GB – 617.9 GB | 18 | any, mac, server | T3–T1 | `llm-mimo-v2-6-pro` |
| Ling-3.1-flash-1019 | alap | 2026-10-27 | 29.6 | 50% | MIT | 131.0 GB – 608.4 GB | 18 | any, mac, server | T3–T1 | `llm-ling-3-1-flash-1019` |
| MiniMax-M3.1-Flash | alap | 2026-10-17 | 29.1 | 49% | MiniMax Community Licens | 129.4 GB – 302.9 GB | 16 | any, mac, server | T3–T1 | `llm-minimax-m3-1-flash` |
| Qwen3.8-Flash-Next | alap | 2026-08-24 | 28.6 | 48% | Qwen Community License 1 | 66.4 GB – 360.0 GB | 57 | any, mac, server | T4–T1 | `llm-qwen3-8-flash-next` |
| Step 5 Preview | alap | 2026-09-20 | 28.5 | 48% | StepFun Model License (o | 182.5 GB – 1.21 TB | 8 | any, server | T3–T1 | `llm-step-5-preview` |
| GLM-5.3-Flash | alap | 2026-08-25 | 27.8 | 47% | MIT | 74.8 GB – 642.7 GB | 44 | any, mac, server | T3–T1 | `llm-glm-5-3-flash` |
| Mistral Large 4 (1T-A52B) | alap | 2026-09-30 | 25.3 | 43% | Mistral Ecosystem Open-W | 233.0 GB – 2.10 TB | 21 | any, mac, server | T2–T1 | `llm-mistral-large-4` |
| Muse Spark Open (816B-A42B) | alap | 2026-09-15 | 24.9 | 42% | Muse Model License; GATE | 175.6 GB – 1.64 TB | 17 | any, mac, server | T3–T1 | `llm-muse-spark-open` |
| Qwen3.8-27B (dense) | alap | 2026-08-05 | 20.1 | 34% | Apache-2.0 | 6.2 GB – 55.6 GB | 58 | any, mac, server | T4–T1 | `llm-qwen3-8-27b` |
| NVIDIA Nemotron 3.5 (Super-VL-120B-A12B, Lightning-30B-A3B, Bolt-E4B) | alap | Super-VL 2 | ~13.6 | ~23% | OpenMDW-1.1 (nyílt súlyo | 3.5 GB – 241.5 GB | 45 | any, mac, server | T5–T1 | `llm-nemotron-3-5` |
| Muse Glimmer 30B | alap | 2026-08-09 | 6.3 | 11% | Apache-2.0 | 6.5 GB – 57.1 GB | 33 | any, mac, server | T4–T1 | `llm-muse-glimmer-30b` |
| Gemma 4 (31B, 26B-A4B, 12B, E4B, E2B) | alap | E2B/E4B 20 | ~4.4 | ~7% | Apache-2.0 | 2.3 GB – 62.6 GB | 100 | android, any, mac, server | T5–T1 | `llm-gemma-4` |
| Qwen3.5-4B / Qwen3.5-9B (+ MiMo-V2.6-Distill-Qwen-9B) | alap | 2026-02-27 | ~3.0 | ~5% | Apache-2.0 (Qwen3.5); MI | 1.8 GB – 10.4 GB | 22 | any | T5–T1 | `llm-qwen3-5-small` |
| DeepSeek-V4.1-Flash-1017 abliterated (huihui GGUF) / heretic (pqhaz) / abliterated (mrfakename) | cenz.-mentes | 2026-10-17 | ~31.6 | ~53% | MIT | 233.0 GB – 510.3 GB | 5 | any, mac, server | T2–T1 | `llm-deepseek-v4-1-flash-1017-abliterated-hui` |
| GLM-5.3 abliterated (huihui GGUF) | cenz.-mentes | 2026-08-25 | ~30.1 | ~51% | other (glm-5.3) | 216.7 GB – 216.7 GB | 1 | any | T2–T1 | `llm-glm-5-3-abliterated-huihui-gguf` |
| Qwen3.8-Flash-Next abliterated v2 (huihui GGUF) | cenz.-mentes | 2026-08-24 | ~27.2 | ~46% | other (qwen-community-1. | 68.2 GB – 188.2 GB | 9 | any, mac | T3–T1 | `llm-qwen3-8-flash-next-abliterated-v2-huihui` |
| MiniMax-M3.1-Flash abliterated (orcarouter GGUF) | cenz.-mentes | 2026-10-17 | ~27.1 | ~46% | other (minimax-community | 111.9 GB – 111.9 GB | 1 | any | T3–T1 | `llm-minimax-m3-1-flash-abliterated-orcaroute` |
| GLM-5.3-Flash abliterated (huihui GGUF) | cenz.-mentes | 2026-08-25 | ~26.4 | ~45% | MIT | 93.1 GB – 291.8 GB | 10 | any, mac | T3–T1 | `llm-glm-5-3-flash-abliterated-huihui-gguf` |
| NousResearch Arete-27B (a "R1-1776 utód") | cenz.-mentes | 2026-08-05 | ~19.0 | ~32% | Apache-2.0 | 15.2 GB – 17.2 GB | 2 | any | T4–T1 | `llm-nousresearch-arete-27b-a-r1-1776-ut-d` |
| Qwen3.8-27B abliterated (huihui) / heretic-ara (trohrbaugh) | cenz.-mentes | 2026-08-05 | ~18.7 | ~32% | Apache-2.0 | 10.9 GB – 29.1 GB | 6 | any, mac | T4–T1 | `llm-qwen3-8-27b-abliterated-huihui-heretic-a` |
| Kimi-K3 Abliterated V1 (Uniboshi) | cenz.-mentes | 2026-06-13 | ~16.2 | ~27% | other (kimi-k3) | 1.51 TB – 1.51 TB | 1 | any | T1–T1 | `llm-kimi-k3-abliterated-v1-uniboshi` |
| Qwen3.6-35B-A3B uncensored-heretic (llmfan46) / abliterated-MTP (huihui) | cenz.-mentes | 2026-04-15 | ~8.0 | ~14% | Apache-2.0 | 16.9 GB – 21.2 GB | 2 | any | T4–T1 | `llm-qwen3-6-35b-a3b-uncensored-heretic-llmfa` |
| Mistral-Small-4-119B-2603 heretic (darkc0de, GGUF: Rioky) | cenz.-mentes | 2026-01-23 | ~7.6 | ~13% | Apache-2.0 (bázis); a he | 43.4 GB – 126.5 GB | 6 | any | T3–T1 | `llm-mistral-small-4-119b-2603-heretic-darkc0` |
| gemma-4-31B-it heretic (coder3101) / uncensored-heretic (llmfan46) | cenz.-mentes | 2026-03-11 | 4.1 | 7% | Apache-2.0, NEM gated | 16.9 GB – 25.2 GB | 4 | any, mac | T4–T1 | `llm-gemma-4-31b-it-heretic-coder3101-uncenso` |
| gpt-oss-120b heretic (MuXodious tainted-heresy / kldzj heretic) | cenz.-mentes | 2025-08-04 | 3.6 | 6% | Apache-2.0 | 62.2 GB – 63.4 GB | 3 | any, mac | T4–T1 | `llm-gpt-oss-120b-heretic-muxodious-tainted-h` |
| gemma-4-26B-A4B-it ultra-uncensored-heretic (llmfan46) | cenz.-mentes | 2026-03-11 | ~3.5 | ~6% | Apache-2.0 | 13.3 GB – 16.8 GB | 2 | any | T4–T1 | `llm-gemma-4-26b-a4b-it-ultra-uncensored-here` |
| gemma-4-12B-it uncensored-heretic (llmfan46) / abliterated QAT (huihui) | cenz.-mentes | 2026-05-23 | ~2.8 | ~5% | Apache-2.0 | 8.5 GB – 8.5 GB | 1 | any | T4–T1 | `llm-gemma-4-12b-it-uncensored-heretic-llmfan` |
| gemma-4-E4B-it heretic (coder3101; GGUF Abiray) / ultra-uncensored (llmfan46) | cenz.-mentes | 2026-03-02 | ~2.5 | ~4% | Apache-2.0 | 5.3 GB – 5.3 GB | 1 | any | T5–T1 | `llm-gemma-4-e4b-it-heretic-coder3101-gguf-ab` |
| Qwen3.5-9B heretic-v2 (trohrbaugh) | cenz.-mentes | 2026-02-27 | ~2.3 | ~4% | Apache-2.0 | 5.6 GB – 9.5 GB | 2 | any | T5–T1 | `llm-qwen3-5-9b-heretic-v2-trohrbaugh` |
| gpt-oss-20b heretic (MuXodious RichardErkhov-heresy / p-e-w heretic) | cenz.-mentes | 2025-08-04 | ~2.1 | ~4% | Apache-2.0 | 12.7 GB – 12.7 GB | 1 | any | T4–T1 | `llm-gpt-oss-20b-heretic-muxodious-richarderk` |
| Qwen3.5-4B heretic-2.0 (p-e-w) / SOMPOA-heresy-v2 (MuXodious) | cenz.-mentes | 2026-02-27 | ~1.9 | ~3% | Apache-2.0 | 2.5 GB – 4.5 GB | 4 | any | T5–T1 | `llm-qwen3-5-4b-heretic-2-0-p-e-w-sompoa-here` |
| gemma-4-E2B-it ultra-uncensored-heretic (llmfan46) | cenz.-mentes | 2026-03-02 | ~1.4 | ~2% | Apache-2.0 | 3.4 GB – 3.6 GB | 2 | any | T5–T1 | `llm-gemma-4-e2b-it-ultra-uncensored-heretic-` |

### 6.4 Minden kvantált változat linkkel és letöltési paranccsal

Kattints egy modellre a lenyitáshoz. A `hf download` parancsok változtatás nélkül futtathatók. A `--include` minta egy kvantot tölt le. Letöltés előtt a fájllistát érdemes ellenőrizni: `curl -s https://huggingface.co/api/models/<repo>/tree/main?recursive=true`.

<details><summary><b>Kimi K3.1 Pro</b> – 9 változat</summary>

| id | Fájl / repó | Méret | Bit | Min. memória (≈×1,15) | HW | Platform | Letöltés |
|---|---|---|---|---|---|---|---|
| `llm-kimi-k3-1-pro-gguf-klx-iq1-s` | Kimi-K3.1-Pro-GGUF · KLX-IQ1_S (GGUF) | 592.7 GB | 1.7 | 682 GB | T1 | any | `hf download KarLexAI/Kimi-K3.1-Pro-GGUF --include "*KLX-IQ1_S*"` |
| `llm-kimi-k3-1-pro-gguf-klx-iq1-m` | Kimi-K3.1-Pro-GGUF · KLX-IQ1_M (GGUF) | 647.9 GB | 1.7 | 745 GB | T1,T2 | any | `hf download KarLexAI/Kimi-K3.1-Pro-GGUF --include "*KLX-IQ1_M*"` |
| `llm-kimi-k3-1-pro-gguf-klx-iq2-xxs` | Kimi-K3.1-Pro-GGUF · KLX-IQ2_XXS (GGUF) | 709.9 GB | 2.6 | 816 GB | T1,T2 | any | `hf download KarLexAI/Kimi-K3.1-Pro-GGUF --include "*KLX-IQ2_XXS*"` |
| `llm-kimi-k3-1-pro-exl3-2bit` | Kimi-K3.1-Pro-EXL3-2bit · 2bit (EXL3) | 797.0 GB | 2.5 | 917 GB | T1 | server | `hf download local-inference-lab/Kimi-K3.1-Pro-EXL3-2bit` |
| `llm-kimi-k3-1-pro-gguf-q2-k` | moonshotai.Kimi-K3.1-Pro-GGUF · Q2_K (GGUF) | 1.01 TB | 2.6 | 1161 GB | T1 | any | `hf download DevQuasar/moonshotai.Kimi-K3.1-Pro-GGUF --include "*Q2_K*"` |
| `llm-kimi-k3-1-pro-gguf-mxfp4-moe` | moonshotai.Kimi-K3.1-Pro-GGUF · MXFP4_MOE (GGUF) | 1.51 TB | 4.5 | 1735 GB | T1 | any | `hf download DevQuasar/moonshotai.Kimi-K3.1-Pro-GGUF --include "*MXFP4_MOE*"` |
| `llm-kimi-k3-1-pro-mlx-mlxse` | Kimi-K3.1-Pro-MLXse · MLXse (MLX) | 1.56 TB | 4.5 | 1795 GB | T1 | mac | `hf download inferencerlabs/Kimi-K3.1-Pro-MLXse` |
| `llm-kimi-k3-1-pro-safetensors-int4-native-native` | Kimi-K3.1-Pro · native (safetensors-INT4(native)) | 1.56 TB | 4.5 | 1796 GB | T1 | server | `hf download moonshotai/Kimi-K3.1-Pro` |
| `llm-kimi-k3-1-pro-nvfp4-nvfp4` | Kimi-K3.1-Pro-NVFP4 · NVFP4 (NVFP4) | 1.61 TB | 4.5 | 1846 GB | T1 | server | `hf download nvidia/Kimi-K3.1-Pro-NVFP4` |
</details>

<details><summary><b>Hy4 preview (Hunyuan)</b> – 6 változat</summary>

| id | Fájl / repó | Méret | Bit | Min. memória (≈×1,15) | HW | Platform | Letöltés |
|---|---|---|---|---|---|---|---|
| `llm-hy4-preview-gguf-tq1-0` | Hy4-preview-GGUF · TQ1_0 (GGUF) | 229.4 GB | 1.7 | 264 GB | T1,T2 | any | `hf download AngelSlim/Hy4-preview-GGUF --include "*TQ1_0*"` |
| `llm-hy4-preview-gguf-ud-iq1-m` | Hy4-preview-GGUF · UD-IQ1_M (GGUF) | 235.3 GB | 1.7 | 271 GB | T1,T2 | any | `hf download AngelSlim/Hy4-preview-GGUF --include "*UD-IQ1_M*"` |
| `llm-hy4-preview-mlx-4bit` | Hy4-preview-4bit · 4bit (MLX) | 433.4 GB | 4.5 | 498 GB | T1,T2 | mac | `hf download mlx-community/Hy4-preview-4bit` |
| `llm-hy4-preview-gguf-q4-k-m` | Hy4-preview-GGUF · Q4_K_M (GGUF) | 467.3 GB | 4.5 | 537 GB | T1,T2 | any | `hf download AngelSlim/Hy4-preview-GGUF --include "*Q4_K_M*"` |
| `llm-hy4-preview-fp8-fp8` | Hy4-preview-FP8 · FP8 (FP8) | 813.8 GB | 8.5 | 936 GB | T1 | server | `hf download tencent/Hy4-preview-FP8` |
| `llm-hy4-preview-bf16-bf16` | Hy4-preview · BF16 (BF16) | 1.56 TB | 16 | 1794 GB | T1 | server | `hf download tencent/Hy4-preview` |
</details>

<details><summary><b>Qwen3.8-2.4T-A95B (a hostolt „Qwen3.8-Max” alapja)</b> – 12 változat</summary>

| id | Fájl / repó | Méret | Bit | Min. memória (≈×1,15) | HW | Platform | Letöltés |
|---|---|---|---|---|---|---|---|
| `llm-qwen3-8-2-4t-a95b-gguf-ud-q1-0` | Qwen3.8-2.4T-A95B-GGUF · UD-Q1_0 (GGUF) | 397.3 GB | 1.7 | 457 GB | T1,T2 | any | `hf download unsloth/Qwen3.8-2.4T-A95B-GGUF --include "*UD-Q1_0*"` |
| `llm-qwen3-8-2-4t-a95b-gguf-ud-iq1-s` | Qwen3.8-2.4T-A95B-GGUF · UD-IQ1_S (GGUF) | 508.4 GB | 1.7 | 585 GB | T1,T2 | any | `hf download unsloth/Qwen3.8-2.4T-A95B-GGUF --include "*UD-IQ1_S*"` |
| `llm-qwen3-8-2-4t-a95b-gguf-ud-iq1-m` | Qwen3.8-2.4T-A95B-GGUF · UD-IQ1_M (GGUF) | 564.0 GB | 1.7 | 649 GB | T1,T2 | any | `hf download unsloth/Qwen3.8-2.4T-A95B-GGUF --include "*UD-IQ1_M*"` |
| `llm-qwen3-8-2-4t-a95b-gguf-ud-iq2-xxs` | Qwen3.8-2.4T-A95B-GGUF · UD-IQ2_XXS (GGUF) | 656.6 GB | 2.6 | 755 GB | T1,T2 | any | `hf download unsloth/Qwen3.8-2.4T-A95B-GGUF --include "*UD-IQ2_XXS*"` |
| `llm-qwen3-8-2-4t-a95b-gguf-ud-iq2-xs` | Qwen3.8-2.4T-A95B-GGUF · UD-IQ2_XS (GGUF) | 730.6 GB | 2.6 | 840 GB | T1,T2 | any | `hf download unsloth/Qwen3.8-2.4T-A95B-GGUF --include "*UD-IQ2_XS*"` |
| `llm-qwen3-8-2-4t-a95b-gguf-ud-iq3-xxs` | Qwen3.8-2.4T-A95B-GGUF · UD-IQ3_XXS (GGUF) | 955.5 GB | 3.5 | 1099 GB | T1 | any | `hf download unsloth/Qwen3.8-2.4T-A95B-GGUF --include "*UD-IQ3_XXS*"` |
| `llm-qwen3-8-2-4t-a95b-gguf-ud-iq4-xs` | Qwen3.8-2.4T-A95B-GGUF · UD-IQ4_XS (GGUF) | 1.31 TB | 4.5 | 1508 GB | T1 | any | `hf download unsloth/Qwen3.8-2.4T-A95B-GGUF --include "*UD-IQ4_XS*"` |
| `llm-qwen3-8-2-4t-a95b-nvfp4-nvfp4` | Qwen3.8-2.4T-A95B-NVFP4 · NVFP4 (NVFP4) | 1.43 TB | 4.5 | 1639 GB | T1 | server | `hf download RedHatAI/Qwen3.8-2.4T-A95B-NVFP4` |
| `llm-qwen3-8-2-4t-a95b-nvfp4-nvfp4-2` | Qwen3.8-2.4T-A95B-NVFP4 · NVFP4 (NVFP4) | 1.44 TB | 4.5 | 1661 GB | T1 | server | `hf download nvidia/Qwen3.8-2.4T-A95B-NVFP4` |
| `llm-qwen3-8-2-4t-a95b-fp8-fp8` | Qwen3.8-2.4T-A95B-FP8 · FP8 (FP8) | 2.50 TB | 8.5 | 2871 GB | T1 | server | `hf download Qwen/Qwen3.8-2.4T-A95B-FP8` |
| `llm-qwen3-8-2-4t-a95b-gguf-q8-0` | Qwen3.8-2.4T-A95B-GGUF · Q8_0 (GGUF) | 2.60 TB | 8.5 | 2990 GB | T1 | any | `hf download unsloth/Qwen3.8-2.4T-A95B-GGUF --include "*Q8_0*"` |
| `llm-qwen3-8-2-4t-a95b-gguf-bf16` | Qwen3.8-2.4T-A95B-GGUF · BF16 (GGUF) | 4.89 TB | 16 | 5627 GB | T1 | any | `hf download unsloth/Qwen3.8-2.4T-A95B-GGUF --include "*BF16*"` |
</details>

<details><summary><b>DeepSeek-V4.1-Flash-1017</b> – 23 változat</summary>

| id | Fájl / repó | Méret | Bit | Min. memória (≈×1,15) | HW | Platform | Letöltés |
|---|---|---|---|---|---|---|---|
| `llm-deepseek-v4-1-flash-1017-gguf-iq1-m` | DeepSeek-V4.1-Flash-1017-GSQ-RCO-GGUF · IQ1_M (GGUF) | 120.7 GB | 1.7 | 139 GB | T1,T2,T3 | any | `hf download ISTA-DASLab/DeepSeek-V4.1-Flash-1017-GSQ-RCO-GGUF --include "*IQ1_M*"` |
| `llm-deepseek-v4-1-flash-1017-gguf-iq2-xxs` | DeepSeek-V4.1-Flash-1017-GSQ-RCO-GGUF · IQ2_XXS (GGUF) | 138.2 GB | 2.6 | 159 GB | T1,T2,T3 | any | `hf download ISTA-DASLab/DeepSeek-V4.1-Flash-1017-GSQ-RCO-GGUF --include "*IQ2_XXS*"` |
| `llm-deepseek-v4-1-flash-1017-gguf-iq2-xs` | DeepSeek-V4.1-Flash-1017-GSQ-RCO-GGUF · IQ2_XS (+ külön Engram IQ4_NL 110.6GB) (GGUF) | 155.2 GB | 2.6 | 179 GB | T1,T2,T3 | any | `hf download ISTA-DASLab/DeepSeek-V4.1-Flash-1017-GSQ-RCO-GGUF --include "*IQ2_XS*"` |
| `llm-deepseek-v4-1-flash-1017-gguf-ud-iq1-s` | DeepSeek-V4.1-Flash-1017-GGUF · UD-IQ1_S (GGUF) | 233.0 GB | 1.7 | 268 GB | T1,T2,T3 | any | `hf download unsloth/DeepSeek-V4.1-Flash-1017-GGUF --include "*UD-IQ1_S*"` |
| `llm-deepseek-v4-1-flash-1017-gguf-ud-iq1-m` | DeepSeek-V4.1-Flash-1017-GGUF · UD-IQ1_M (GGUF) | 250.4 GB | 1.7 | 288 GB | T1,T2 | any | `hf download unsloth/DeepSeek-V4.1-Flash-1017-GGUF --include "*UD-IQ1_M*"` |
| `llm-deepseek-v4-1-flash-1017-gguf-q2-k-s` | DeepSeek-V4.1-Flash-1017-GGUF · Q2_K_S (GGUF) | 298.0 GB | 2.6 | 343 GB | T1,T2 | any | `hf download ggml-org/DeepSeek-V4.1-Flash-1017-GGUF --include "*Q2_K_S*"` |
| `llm-deepseek-v4-1-flash-1017-gguf-ud-iq2-xxs` | DeepSeek-V4.1-Flash-1017-GGUF · UD-IQ2_XXS (GGUF) | 300.5 GB | 2.6 | 346 GB | T1,T2 | any | `hf download unsloth/DeepSeek-V4.1-Flash-1017-GGUF --include "*UD-IQ2_XXS*"` |
| `llm-deepseek-v4-1-flash-1017-mlx-oq2e-mtp` | DeepSeek-V4.1-Flash-1017-oQ2e-mtp · oQ2e-mtp (MLX) | 313.3 GB | 2.5 | 360 GB | T1,T2 | mac | `hf download mlx-community/DeepSeek-V4.1-Flash-1017-oQ2e-mtp` |
| `llm-deepseek-v4-1-flash-1017-gguf-ud-q2-k-xl` | DeepSeek-V4.1-Flash-1017-GGUF · UD-Q2_K_XL (GGUF) | 334.8 GB | 2.6 | 385 GB | T1,T2 | any | `hf download unsloth/DeepSeek-V4.1-Flash-1017-GGUF --include "*UD-Q2_K_XL*"` |
| `llm-deepseek-v4-1-flash-1017-gguf-q2-k` | DeepSeek-V4.1-Flash-1017-GGUF · Q2_K (GGUF) | 334.8 GB | 2.6 | 385 GB | T1,T2 | any | `hf download ggml-org/DeepSeek-V4.1-Flash-1017-GGUF --include "*Q2_K*"` |
| `llm-deepseek-v4-1-flash-1017-mlx-oq2-5e-mtp` | DeepSeek-V4.1-Flash-1017-oQ2.5e-mtp · oQ2.5e-mtp (MLX) | 342.7 GB | 3.0 | 394 GB | T1,T2 | mac | `hf download mlx-community/DeepSeek-V4.1-Flash-1017-oQ2.5e-mtp` |
| `llm-deepseek-v4-1-flash-1017-gguf-q2-k-imatrix` | deepseek-v4.1-flash-gguf · Q2_K-imatrix (GGUF) | 365.7 GB | 2.6 | 421 GB | T1,T2 | any | `hf download antirez/deepseek-v4.1-flash-gguf --include "*Q2_K-imatrix*"` |
| `llm-deepseek-v4-1-flash-1017-mlx-oq3e-mtp` | DeepSeek-V4.1-Flash-1017-oQ3e-mtp · oQ3e-mtp (MLX) | 381.2 GB | 3.5 | 438 GB | T1,T2 | mac | `hf download mlx-community/DeepSeek-V4.1-Flash-1017-oQ3e-mtp` |
| `llm-deepseek-v4-1-flash-1017-gguf-ud-iq3-xxs` | DeepSeek-V4.1-Flash-1017-GGUF · UD-IQ3_XXS (GGUF) | 394.7 GB | 3.5 | 454 GB | T1,T2 | any | `hf download unsloth/DeepSeek-V4.1-Flash-1017-GGUF --include "*UD-IQ3_XXS*"` |
| `llm-deepseek-v4-1-flash-1017-gguf-ud-iq3-s` | DeepSeek-V4.1-Flash-1017-GGUF · UD-IQ3_S (GGUF) | 423.6 GB | 3.5 | 487 GB | T1,T2 | any | `hf download unsloth/DeepSeek-V4.1-Flash-1017-GGUF --include "*UD-IQ3_S*"` |
| `llm-deepseek-v4-1-flash-1017-nvfp4-nvfp4` | DeepSeek-V4.1-Flash-1017-NVFP4 · NVFP4 (NVFP4) | 429.0 GB | 4.5 | 493 GB | T1,T2 | server | `hf download nvidia/DeepSeek-V4.1-Flash-1017-NVFP4` |
| `llm-deepseek-v4-1-flash-1017-mlx-oq4e-mtp` | DeepSeek-V4.1-Flash-1017-oQ4e-mtp · oQ4e-mtp (MLX) | 432.0 GB | 4.5 | 497 GB | T1,T2 | mac | `hf download mlx-community/DeepSeek-V4.1-Flash-1017-oQ4e-mtp` |
| `llm-deepseek-v4-1-flash-1017-gguf-ud-q3-k-xl` | DeepSeek-V4.1-Flash-1017-GGUF · UD-Q3_K_XL (GGUF) | 485.1 GB | 3.5 | 558 GB | T1,T2 | any | `hf download unsloth/DeepSeek-V4.1-Flash-1017-GGUF --include "*UD-Q3_K_XL*"` |
| `llm-deepseek-v4-1-flash-1017-gguf-ud-q4-k-xl` | DeepSeek-V4.1-Flash-1017-GGUF · UD-Q4_K_XL (GGUF) | 500.7 GB | 4.5 | 576 GB | T1,T2 | any | `hf download unsloth/DeepSeek-V4.1-Flash-1017-GGUF --include "*UD-Q4_K_XL*"` |
| `llm-deepseek-v4-1-flash-1017-gguf-mxfp4-experts` | deepseek-v4.1-flash-gguf · MXFP4-experts (V4.1-Flash, nem 1017) (GGUF) | 501.6 GB | 4.5 | 577 GB | T1,T2 | any | `hf download antirez/deepseek-v4.1-flash-gguf --include "*MXFP4-experts*"` |
| `llm-deepseek-v4-1-flash-1017-mlx-mlxs` | DeepSeek-V4.1-Flash-1017-MLXs · MLXs (MLX) | 502.8 GB | 4.5 | 578 GB | T1,T2 | mac | `hf download inferencerlabs/DeepSeek-V4.1-Flash-1017-MLXs` |
| `llm-deepseek-v4-1-flash-1017-gguf-ud-q8-k-xl` | DeepSeek-V4.1-Flash-1017-GGUF · UD-Q8_K_XL (GGUF) | 508.4 GB | 8.5 | 585 GB | T1,T2 | any | `hf download unsloth/DeepSeek-V4.1-Flash-1017-GGUF --include "*UD-Q8_K_XL*"` |
| `llm-deepseek-v4-1-flash-1017-safetensors-native-fp8-int8` | DeepSeek-V4.1-Flash-1017 · FP8/INT8 native (safetensors(native)) | 510.3 GB | 8.5 | 587 GB | T1 | server | `hf download deepseek-ai/DeepSeek-V4.1-Flash-1017` |
</details>

<details><summary><b>GLM-5.3</b> – 25 változat</summary>

| id | Fájl / repó | Méret | Bit | Min. memória (≈×1,15) | HW | Platform | Letöltés |
|---|---|---|---|---|---|---|---|
| `llm-glm-5-3-gguf-ud-iq2-xxs` | glm-5.3-gguf · UD-IQ2_XXS mix (GGUF) | 211.1 GB | 2.6 | 243 GB | T1,T2 | any | `hf download antirez/glm-5.3-gguf --include "*UD-IQ2_XXS*"` |
| `llm-glm-5-3-gguf-ud-iq1-s` | GLM-5.3-GGUF · UD-IQ1_S (GGUF) | 216.7 GB | 1.7 | 249 GB | T1,T2,T3 | any | `hf download unsloth/GLM-5.3-GGUF --include "*UD-IQ1_S*"` |
| `llm-glm-5-3-gguf-ud-iq1-m` | GLM-5.3-GGUF · UD-IQ1_M (GGUF) | 228.5 GB | 1.7 | 263 GB | T1,T2 | any | `hf download unsloth/GLM-5.3-GGUF --include "*UD-IQ1_M*"` |
| `llm-glm-5-3-gguf-ud-iq2-m` | GLM-5.3-GGUF · UD-IQ2_M (GGUF) | 238.6 GB | 2.6 | 274 GB | T1,T2 | any | `hf download unsloth/GLM-5.3-GGUF --include "*UD-IQ2_M*"` |
| `llm-glm-5-3-gguf-ud-q2-k-xl` | GLM-5.3-GGUF · UD-Q2_K_XL (GGUF) | 253.9 GB | 2.6 | 292 GB | T1,T2 | any | `hf download unsloth/GLM-5.3-GGUF --include "*UD-Q2_K_XL*"` |
| `llm-glm-5-3-gguf-iq2-s` | GLM-5.3-GGUF · IQ2_S (GGUF) | 259.1 GB | 2.6 | 298 GB | T1,T2 | any | `hf download AesSedai/GLM-5.3-GGUF --include "*IQ2_S*"` |
| `llm-glm-5-3-gguf-ud-iq3-xxs` | GLM-5.3-GGUF · UD-IQ3_XXS (GGUF) | 281.7 GB | 3.5 | 324 GB | T1,T2 | any | `hf download unsloth/GLM-5.3-GGUF --include "*UD-IQ3_XXS*"` |
| `llm-glm-5-3-gguf-iq3-s` | GLM-5.3-GGUF · IQ3_S (GGUF) | 285.6 GB | 3.5 | 328 GB | T1,T2 | any | `hf download AesSedai/GLM-5.3-GGUF --include "*IQ3_S*"` |
| `llm-glm-5-3-gguf-ud-q3-k-xl` | GLM-5.3-GGUF · UD-Q3_K_XL (GGUF) | 343.0 GB | 3.5 | 394 GB | T1,T2 | any | `hf download unsloth/GLM-5.3-GGUF --include "*UD-Q3_K_XL*"` |
| `llm-glm-5-3-gguf-ud-iq4-xs` | GLM-5.3-GGUF · UD-IQ4_XS (GGUF) | 365.3 GB | 4.5 | 420 GB | T1,T2 | any | `hf download unsloth/GLM-5.3-GGUF --include "*UD-IQ4_XS*"` |
| `llm-glm-5-3-gguf-iq4-xs` | GLM-5.3-GGUF · IQ4_XS (GGUF) | 367.2 GB | 4.5 | 422 GB | T1,T2 | any | `hf download AesSedai/GLM-5.3-GGUF --include "*IQ4_XS*"` |
| `llm-glm-5-3-mxfp4-mxfp4` | GLM-5.3-MXFP4 · MXFP4 (MXFP4) | 403.4 GB | 4.5 | 464 GB | T1 | server | `hf download RedHatAI/GLM-5.3-MXFP4` |
| `llm-glm-5-3-mlx-4bit` | GLM-5.3-4bit · 4bit (MLX) | 418.3 GB | 4.5 | 481 GB | T1,T2 | mac | `hf download mlx-community/GLM-5.3-4bit` |
| `llm-glm-5-3-mlx-mixed` | GLM-5.3-mixed-4_5bit · mixed 4/5bit (MLX) | 450.7 GB | 5.5 | 518 GB | T1,T2 | mac | `hf download mlx-community/GLM-5.3-mixed-4_5bit` |
| `llm-glm-5-3-nvfp4-nvfp4` | GLM-5.3-NVFP4 · NVFP4 (NVFP4) | 464.2 GB | 4.5 | 534 GB | T1,T2 | server | `hf download nvidia/GLM-5.3-NVFP4` |
| `llm-glm-5-3-gguf-ud-q4-k-xl` | GLM-5.3-GGUF · UD-Q4_K_XL (GGUF) | 467.3 GB | 4.5 | 537 GB | T1,T2 | any | `hf download unsloth/GLM-5.3-GGUF --include "*UD-Q4_K_XL*"` |
| `llm-glm-5-3-gguf-q4-k-m` | GLM-5.3-GGUF · Q4_K_M (GGUF) | 469.2 GB | 4.5 | 540 GB | T1,T2 | any | `hf download AesSedai/GLM-5.3-GGUF --include "*Q4_K_M*"` |
| `llm-glm-5-3-awq-awq-int4` | GLM-5.3-AWQ-INT4 · AWQ-INT4 (AWQ) | 488.2 GB | 4.5 | 561 GB | T1 | server | `hf download cyankiwi/GLM-5.3-AWQ-INT4` |
| `llm-glm-5-3-gguf-q5-k-m` | GLM-5.3-GGUF · Q5_K_M (GGUF) | 561.6 GB | 5.5 | 646 GB | T1,T2 | any | `hf download AesSedai/GLM-5.3-GGUF --include "*Q5_K_M*"` |
| `llm-glm-5-3-gguf-ud-q5-k-xl` | GLM-5.3-GGUF · UD-Q5_K_XL (GGUF) | 562.5 GB | 5.5 | 647 GB | T1,T2 | any | `hf download unsloth/GLM-5.3-GGUF --include "*UD-Q5_K_XL*"` |
| `llm-glm-5-3-gguf-ud-q6-k-xl` | GLM-5.3-GGUF · UD-Q6_K_XL (GGUF) | 684.4 GB | 6.5 | 787 GB | T1,T2 | any | `hf download unsloth/GLM-5.3-GGUF --include "*UD-Q6_K_XL*"` |
| `llm-glm-5-3-fp8-native-fp8` | GLM-5.3 · FP8 (FP8(native)) | 755.7 GB | 8.5 | 869 GB | T1 | server | `hf download zai-org/GLM-5.3` |
| `llm-glm-5-3-gguf-q8-0` | GLM-5.3-GGUF · Q8_0 (GGUF) | 801.4 GB | 8.5 | 922 GB | T1,T2 | any | `hf download unsloth/GLM-5.3-GGUF --include "*Q8_0*"` |
| `llm-glm-5-3-bf16-bf16` | GLM-5.3-BF16 · BF16 (BF16) | 1.51 TB | 16 | 1733 GB | T1 | server | `hf download zai-org/GLM-5.3-BF16` |
| `llm-glm-5-3-gguf-bf16` | GLM-5.3-GGUF · BF16 (GGUF) | 1.51 TB | 16 | 1734 GB | T1,T2 | any | `hf download unsloth/GLM-5.3-GGUF --include "*BF16*"` |
</details>

<details><summary><b>Inkling 2 Small</b> – 13 változat</summary>

| id | Fájl / repó | Méret | Bit | Min. memória (≈×1,15) | HW | Platform | Letöltés |
|---|---|---|---|---|---|---|---|
| `llm-inkling-2-small-mlx-oq4e` | Inkling-2-Small-oQ4e · oQ4e (MLX) | 341.5 GB | 4.5 | 393 GB | T1,T2 | mac | `hf download mlx-community/Inkling-2-Small-oQ4e` |
| `llm-inkling-2-small-gguf-ud-iq1-s` | Inkling-2-Small-GGUF · UD-IQ1_S (GGUF) | 343.5 GB | 1.7 | 395 GB | T1,T2 | any | `hf download unsloth/Inkling-2-Small-GGUF --include "*UD-IQ1_S*"` |
| `llm-inkling-2-small-gguf-ud-iq1-m` | Inkling-2-Small-GGUF · UD-IQ1_M (GGUF) | 357.1 GB | 1.7 | 411 GB | T1,T2 | any | `hf download unsloth/Inkling-2-Small-GGUF --include "*UD-IQ1_M*"` |
| `llm-inkling-2-small-mlx-4bit` | Inkling-2-Small-4bit · 4bit (MLX) | 380.8 GB | 4.5 | 438 GB | T1,T2 | mac | `hf download mlx-community/Inkling-2-Small-4bit` |
| `llm-inkling-2-small-gguf-ud-iq2-xxs` | Inkling-2-Small-GGUF · UD-IQ2_XXS (GGUF) | 381.2 GB | 2.6 | 438 GB | T1,T2 | any | `hf download unsloth/Inkling-2-Small-GGUF --include "*UD-IQ2_XXS*"` |
| `llm-inkling-2-small-native-native` | Inkling-2-Small · native ~4bit (native) | 393.5 GB | 4.5 | 453 GB | T1,T2 | server | `hf download thinkingmachines/Inkling-2-Small` |
| `llm-inkling-2-small-gguf-ud-q2-k-xl` | Inkling-2-Small-GGUF · UD-Q2_K_XL (GGUF) | 409.9 GB | 2.6 | 471 GB | T1,T2 | any | `hf download unsloth/Inkling-2-Small-GGUF --include "*UD-Q2_K_XL*"` |
| `llm-inkling-2-small-gguf-ud-iq3-xxs` | Inkling-2-Small-GGUF · UD-IQ3_XXS (GGUF) | 452.0 GB | 3.5 | 520 GB | T1,T2 | any | `hf download unsloth/Inkling-2-Small-GGUF --include "*UD-IQ3_XXS*"` |
| `llm-inkling-2-small-gguf-ud-q3-k-xl` | Inkling-2-Small-GGUF · UD-Q3_K_XL (GGUF) | 570.3 GB | 3.5 | 656 GB | T1,T2 | any | `hf download unsloth/Inkling-2-Small-GGUF --include "*UD-Q3_K_XL*"` |
| `llm-inkling-2-small-mxfp8-mxfp8` | Inkling-2-Small-MXFP8 · MXFP8 (MXFP8) | 622.8 GB | 8.5 | 716 GB | T1 | server | `hf download thinkingmachines/Inkling-2-Small-MXFP8` |
| `llm-inkling-2-small-gguf-ud-q4-k-xl` | Inkling-2-Small-GGUF · UD-Q4_K_XL (GGUF) | 708.3 GB | 4.5 | 815 GB | T1,T2 | any | `hf download unsloth/Inkling-2-Small-GGUF --include "*UD-Q4_K_XL*"` |
| `llm-inkling-2-small-gguf-ud-q8-k-xl` | Inkling-2-Small-GGUF · UD-Q8_K_XL (GGUF) | 773.0 GB | 8.5 | 889 GB | T1,T2 | any | `hf download unsloth/Inkling-2-Small-GGUF --include "*UD-Q8_K_XL*"` |
| `llm-inkling-2-small-gguf-bf16` | Inkling-2-Small-GGUF · BF16 (GGUF) | 968.8 GB | 16 | 1114 GB | T1,T2 | any | `hf download unsloth/Inkling-2-Small-GGUF --include "*BF16*"` |
</details>

<details><summary><b>LongCat-2.5 (csak megjegyzésként)</b> – 1 változat</summary>

| id | Fájl / repó | Méret | Bit | Min. memória (≈×1,15) | HW | Platform | Letöltés |
|---|---|---|---|---|---|---|---|
| `llm-longcat-2-5-w4a4-w4a4` | LongCat-2.5-W4A4 · W4A4 (FlatQuant) (W4A4) | 1.34 TB | 4.5 | 1536 GB | T1 | server | `hf download meituan-longcat/LongCat-2.5-W4A4` |
</details>

<details><summary><b>MiMo-V2.6-Pro (RL és MOPD változat) + MiMo-V2.6-Flash</b> – 18 változat</summary>

| id | Fájl / repó | Méret | Bit | Min. memória (≈×1,15) | HW | Platform | Letöltés |
|---|---|---|---|---|---|---|---|
| `llm-mimo-v2-6-pro-gguf-flash-q2-k` | MiMo-V2.6-Flash-RL-GGUF · Q2_K (GGUF(Flash)) | 126.4 GB | 2.6 | 145 GB | T1,T2,T3 | any | `hf download ggml-org/MiMo-V2.6-Flash-RL-GGUF --include "*Q2_K*"` |
| `llm-mimo-v2-6-pro-mlx-flash-mxfp4-q8` | MiMo-V2.6-Flash-RL-mxfp4-q8 · mxfp4-q8 (MLX(Flash)) | 167.3 GB | 4.5 | 192 GB | T1,T2 | mac | `hf download mlx-community/MiMo-V2.6-Flash-RL-mxfp4-q8` |
| `llm-mimo-v2-6-pro-gguf-flash-mxfp4` | MiMo-V2.6-Flash-RL-GGUF · MXFP4 (GGUF(Flash)) | 167.4 GB | 4.5 | 192 GB | T1,T2,T3 | any | `hf download ggml-org/MiMo-V2.6-Flash-RL-GGUF --include "*MXFP4*"` |
| `llm-mimo-v2-6-pro-gguf-bpw2-0` | MiMo-V2.6-Pro-MOPD-GGUF · BPW2.0 (GGUF) | 255.8 GB | 2.5 | 294 GB | T1,T2 | any | `hf download AesSedai/MiMo-V2.6-Pro-MOPD-GGUF --include "*BPW2.0*"` |
| `llm-mimo-v2-6-pro-gguf-bpw2-5` | MiMo-V2.6-Pro-MOPD-GGUF · BPW2.5 (GGUF) | 319.6 GB | 3.0 | 368 GB | T1,T2 | any | `hf download AesSedai/MiMo-V2.6-Pro-MOPD-GGUF --include "*BPW2.5*"` |
| `llm-mimo-v2-6-pro-gguf-q2-k` | XiaomiMiMo.MiMo-V2.6-Pro-RL-GGUF · Q2_K (GGUF) | 373.5 GB | 2.6 | 430 GB | T1,T2 | any | `hf download DevQuasar/XiaomiMiMo.MiMo-V2.6-Pro-RL-GGUF --include "*Q2_K*"` |
| `llm-mimo-v2-6-pro-gguf-bpw3-0` | MiMo-V2.6-Pro-MOPD-GGUF · BPW3.0 (GGUF) | 383.4 GB | 3.5 | 441 GB | T1,T2 | any | `hf download AesSedai/MiMo-V2.6-Pro-MOPD-GGUF --include "*BPW3.0*"` |
| `llm-mimo-v2-6-pro-gguf-q2-k-2` | MiMo-V2.6-Pro-MOPD-GGUF · Q2_K (GGUF) | 418.8 GB | 2.6 | 482 GB | T1,T2 | any | `hf download ggml-org/MiMo-V2.6-Pro-MOPD-GGUF --include "*Q2_K*"` |
| `llm-mimo-v2-6-pro-gguf-bpw3-5` | MiMo-V2.6-Pro-MOPD-GGUF · BPW3.5 (GGUF) | 447.5 GB | 4.0 | 515 GB | T1,T2 | any | `hf download AesSedai/MiMo-V2.6-Pro-MOPD-GGUF --include "*BPW3.5*"` |
| `llm-mimo-v2-6-pro-gguf-q5-k-m` | XiaomiMiMo.MiMo-V2.6-Pro-RL-GGUF · Q5_K_M (GGUF) | 489.3 GB | 5.5 | 563 GB | T1,T2 | any | `hf download DevQuasar/XiaomiMiMo.MiMo-V2.6-Pro-RL-GGUF --include "*Q5_K_M*"` |
| `llm-mimo-v2-6-pro-mlx-mxfp4-q8` | MiMo-V2.6-Pro-RL-mxfp4-q8 · mxfp4-q8 (MLX) | 553.9 GB | 4.5 | 637 GB | T1,T2 | mac | `hf download mlx-community/MiMo-V2.6-Pro-RL-mxfp4-q8` |
| `llm-mimo-v2-6-pro-gguf-mxfp4` | MiMo-V2.6-Pro-MOPD-GGUF · MXFP4 (GGUF) | 554.2 GB | 4.5 | 637 GB | T1,T2 | any | `hf download ggml-org/MiMo-V2.6-Pro-MOPD-GGUF --include "*MXFP4*"` |
| `llm-mimo-v2-6-pro-gguf-mxfp4-moe` | XiaomiMiMo.MiMo-V2.6-Pro-RL-GGUF · MXFP4_MOE (GGUF) | 554.2 GB | 4.5 | 637 GB | T1,T2 | any | `hf download DevQuasar/XiaomiMiMo.MiMo-V2.6-Pro-RL-GGUF --include "*MXFP4_MOE*"` |
| `llm-mimo-v2-6-pro-mlx-q9` | MiMo-V2.6-Pro-RL-MLX-Q9 · Q9 (MLX) | 556.7 GB | 4.5 | 640 GB | T1,T2 | mac | `hf download inferencerlabs/MiMo-V2.6-Pro-RL-MLX-Q9` |
| `llm-mimo-v2-6-pro-safetensors-native-native` | MiMo-V2.6-Pro-RL · native (safetensors(native)) | 573.5 GB | 16 | 660 GB | T1 | server | `hf download XiaomiMiMo/MiMo-V2.6-Pro-RL` |
| `llm-mimo-v2-6-pro-safetensors-native-native-2` | MiMo-V2.6-Pro-MOPD · native (safetensors(native)) | 573.5 GB | 16 | 660 GB | T1 | server | `hf download XiaomiMiMo/MiMo-V2.6-Pro-MOPD` |
| `llm-mimo-v2-6-pro-gguf-mxfp4-2` | MiMo-V2.6-Pro-MOPD-GGUF · MXFP4 (GGUF) | 577.7 GB | 4.5 | 664 GB | T1,T2 | any | `hf download AesSedai/MiMo-V2.6-Pro-MOPD-GGUF --include "*MXFP4*"` |
| `llm-mimo-v2-6-pro-gguf-q4-k-m` | XiaomiMiMo.MiMo-V2.6-Pro-RL-GGUF · Q4_K_M (GGUF) | 617.9 GB | 4.5 | 711 GB | T1,T2 | any | `hf download DevQuasar/XiaomiMiMo.MiMo-V2.6-Pro-RL-GGUF --include "*Q4_K_M*"` |
</details>

<details><summary><b>Ling-3.1-flash-1019</b> – 18 változat</summary>

| id | Fájl / repó | Méret | Bit | Min. memória (≈×1,15) | HW | Platform | Letöltés |
|---|---|---|---|---|---|---|---|
| `llm-ling-3-1-flash-1019-gguf-iq1-s` | Ling-3.1-flash-1019-GGUF · IQ1_S (GGUF) | 131.0 GB | 1.7 | 151 GB | T1,T2,T3 | any | `hf download bartowski/Ling-3.1-flash-1019-GGUF --include "*IQ1_S*"` |
| `llm-ling-3-1-flash-1019-gguf-iq1-m` | Ling-3.1-flash-1019-GGUF · IQ1_M (GGUF) | 145.1 GB | 1.7 | 167 GB | T1,T2,T3 | any | `hf download bartowski/Ling-3.1-flash-1019-GGUF --include "*IQ1_M*"` |
| `llm-ling-3-1-flash-1019-gguf-iq2-xxs` | Ling-3.1-flash-1019-GGUF · IQ2_XXS (GGUF) | 170.8 GB | 2.6 | 196 GB | T1,T2,T3 | any | `hf download bartowski/Ling-3.1-flash-1019-GGUF --include "*IQ2_XXS*"` |
| `llm-ling-3-1-flash-1019-mlx-oq2e-mtp` | Ling-3.1-flash-1019-oQ2e-mtp · oQ2e-mtp (MLX) | 193.2 GB | 2.5 | 222 GB | T1,T2 | mac | `hf download mlx-community/Ling-3.1-flash-1019-oQ2e-mtp` |
| `llm-ling-3-1-flash-1019-gguf-iq2-m` | Ling-3.1-flash-1019-GGUF · IQ2_M (GGUF) | 213.0 GB | 2.6 | 245 GB | T1,T2,T3 | any | `hf download bartowski/Ling-3.1-flash-1019-GGUF --include "*IQ2_M*"` |
| `llm-ling-3-1-flash-1019-gguf-q2-k` | Ling-3.1-flash-1019-GGUF · Q2_K (GGUF) | 219.2 GB | 2.6 | 252 GB | T1,T2,T3 | any | `hf download bartowski/Ling-3.1-flash-1019-GGUF --include "*Q2_K*"` |
| `llm-ling-3-1-flash-1019-mlx-oq2-5e-mtp` | Ling-3.1-flash-1019-oQ2.5e-mtp · oQ2.5e-mtp (MLX) | 224.0 GB | 3.0 | 258 GB | T1,T2 | mac | `hf download mlx-community/Ling-3.1-flash-1019-oQ2.5e-mtp` |
| `llm-ling-3-1-flash-1019-gguf-iq3-xxs` | Ling-3.1-flash-1019-GGUF · IQ3_XXS (GGUF) | 247.4 GB | 3.5 | 284 GB | T1,T2 | any | `hf download bartowski/Ling-3.1-flash-1019-GGUF --include "*IQ3_XXS*"` |
| `llm-ling-3-1-flash-1019-mlx-oq3e-mtp` | Ling-3.1-flash-1019-oQ3e-mtp · oQ3e-mtp (MLX) | 261.6 GB | 3.5 | 301 GB | T1,T2 | mac | `hf download mlx-community/Ling-3.1-flash-1019-oQ3e-mtp` |
| `llm-ling-3-1-flash-1019-gguf-q3-k-m` | Ling-3.1-flash-1019-GGUF · Q3_K_M (GGUF) | 275.1 GB | 3.5 | 316 GB | T1,T2 | any | `hf download bartowski/Ling-3.1-flash-1019-GGUF --include "*Q3_K_M*"` |
| `llm-ling-3-1-flash-1019-gguf-iq3-m` | Ling-3.1-flash-1019-GGUF · IQ3_M (GGUF) | 297.3 GB | 3.5 | 342 GB | T1,T2 | any | `hf download bartowski/Ling-3.1-flash-1019-GGUF --include "*IQ3_M*"` |
| `llm-ling-3-1-flash-1019-gguf-iq4-xs` | Ling-3.1-flash-1019-GGUF · IQ4_XS (GGUF) | 317.1 GB | 4.5 | 365 GB | T1,T2 | any | `hf download bartowski/Ling-3.1-flash-1019-GGUF --include "*IQ4_XS*"` |
| `llm-ling-3-1-flash-1019-mlx-oq4e-mtp` | Ling-3.1-flash-1019-oQ4e-mtp · oQ4e-mtp (MLX) | 330.1 GB | 4.5 | 380 GB | T1,T2 | mac | `hf download mlx-community/Ling-3.1-flash-1019-oQ4e-mtp` |
| `llm-ling-3-1-flash-1019-gguf-q4-k-m` | Ling-3.1-flash-1019-GGUF · Q4_K_M (GGUF) | 358.0 GB | 4.5 | 412 GB | T1,T2 | any | `hf download bartowski/Ling-3.1-flash-1019-GGUF --include "*Q4_K_M*"` |
| `llm-ling-3-1-flash-1019-gguf-q5-k-m` | Ling-3.1-flash-1019-GGUF · Q5_K_M (GGUF) | 436.3 GB | 5.5 | 502 GB | T1,T2 | any | `hf download bartowski/Ling-3.1-flash-1019-GGUF --include "*Q5_K_M*"` |
| `llm-ling-3-1-flash-1019-gguf-q6-k` | Ling-3.1-flash-1019-GGUF · Q6_K (GGUF) | 501.6 GB | 6.5 | 577 GB | T1,T2 | any | `hf download bartowski/Ling-3.1-flash-1019-GGUF --include "*Q6_K*"` |
| `llm-ling-3-1-flash-1019-fp8-native-fp8` | Ling-3.1-flash-1019 · FP8 (FP8(native)) | 573.8 GB | 8.5 | 660 GB | T1 | server | `hf download inclusionAI/Ling-3.1-flash-1019` |
| `llm-ling-3-1-flash-1019-gguf-q8-0` | Ling-3.1-flash-1019-GGUF · Q8_0 (GGUF) | 608.4 GB | 8.5 | 700 GB | T1,T2 | any | `hf download bartowski/Ling-3.1-flash-1019-GGUF --include "*Q8_0*"` |
</details>

<details><summary><b>MiniMax-M3.1-Flash</b> – 16 változat</summary>

| id | Fájl / repó | Méret | Bit | Min. memória (≈×1,15) | HW | Platform | Letöltés |
|---|---|---|---|---|---|---|---|
| `llm-minimax-m3-1-flash-gguf-ud-iq1-m` | MiniMax-M3.1-Flash-GGUF · UD-IQ1_M (GGUF) | 129.4 GB | 1.7 | 149 GB | T1,T2,T3 | any | `hf download unsloth/MiniMax-M3.1-Flash-GGUF --include "*UD-IQ1_M*"` |
| `llm-minimax-m3-1-flash-gguf-ud-iq2-xxs` | MiniMax-M3.1-Flash-GGUF · UD-IQ2_XXS (GGUF) | 134.9 GB | 2.6 | 155 GB | T1,T2,T3 | any | `hf download unsloth/MiniMax-M3.1-Flash-GGUF --include "*UD-IQ2_XXS*"` |
| `llm-minimax-m3-1-flash-gguf-ud-q2-k-xl` | MiniMax-M3.1-Flash-GGUF · UD-Q2_K_XL (GGUF) | 143.9 GB | 2.6 | 165 GB | T1,T2,T3 | any | `hf download unsloth/MiniMax-M3.1-Flash-GGUF --include "*UD-Q2_K_XL*"` |
| `llm-minimax-m3-1-flash-gguf-q2-k` | MiniMaxAI.MiniMax-M3.1-Flash-GGUF · Q2_K (GGUF) | 156.0 GB | 2.6 | 179 GB | T1,T2,T3 | any | `hf download DevQuasar/MiniMaxAI.MiniMax-M3.1-Flash-GGUF --include "*Q2_K*"` |
| `llm-minimax-m3-1-flash-gguf-ud-iq3-xxs` | MiniMax-M3.1-Flash-GGUF · UD-IQ3_XXS (GGUF) | 160.1 GB | 3.5 | 184 GB | T1,T2,T3 | any | `hf download unsloth/MiniMax-M3.1-Flash-GGUF --include "*UD-IQ3_XXS*"` |
| `llm-minimax-m3-1-flash-gguf-ud-iq3-s` | MiniMax-M3.1-Flash-GGUF · UD-IQ3_S (GGUF) | 175.4 GB | 3.5 | 202 GB | T1,T2,T3 | any | `hf download unsloth/MiniMax-M3.1-Flash-GGUF --include "*UD-IQ3_S*"` |
| `llm-minimax-m3-1-flash-mlx-3bit` | MiniMax-M3.1-Flash-Text-3bit · 3bit (text-only) (MLX) | 186.5 GB | 3.5 | 214 GB | T1,T2 | mac | `hf download mlx-community/MiniMax-M3.1-Flash-Text-3bit` |
| `llm-minimax-m3-1-flash-gguf-ud-q3-k-xl` | MiniMax-M3.1-Flash-GGUF · UD-Q3_K_XL (GGUF) | 193.9 GB | 3.5 | 223 GB | T1,T2,T3 | any | `hf download unsloth/MiniMax-M3.1-Flash-GGUF --include "*UD-Q3_K_XL*"` |
| `llm-minimax-m3-1-flash-mlx-oq3e-mtp` | MiniMax-M3.1-Flash-oQ3e-mtp · oQ3e-mtp (MLX) | 196.2 GB | 3.5 | 226 GB | T1,T2 | mac | `hf download mlx-community/MiniMax-M3.1-Flash-oQ3e-mtp` |
| `llm-minimax-m3-1-flash-gguf-q3-k-m` | MiniMaxAI.MiniMax-M3.1-Flash-GGUF · Q3_K_M (GGUF) | 203.5 GB | 3.5 | 234 GB | T1,T2,T3 | any | `hf download DevQuasar/MiniMaxAI.MiniMax-M3.1-Flash-GGUF --include "*Q3_K_M*"` |
| `llm-minimax-m3-1-flash-mlx-oq3-5e-mtp` | MiniMax-M3.1-Flash-oQ3.5e-mtp · oQ3.5e-mtp (MLX) | 213.4 GB | 4.0 | 245 GB | T1,T2 | mac | `hf download mlx-community/MiniMax-M3.1-Flash-oQ3.5e-mtp` |
| `llm-minimax-m3-1-flash-mxfp4-mxfp4` | MiniMax-M3.1-Flash-Quark-MXFP4 · MXFP4 (MXFP4) | 239.5 GB | 4.5 | 275 GB | T1,T2 | server | `hf download amd/MiniMax-M3.1-Flash-Quark-MXFP4` |
| `llm-minimax-m3-1-flash-mlx-4bit` | MiniMax-M3.1-Flash-Text-4bit · 4bit (text-only) (MLX) | 248.4 GB | 4.5 | 286 GB | T1,T2 | mac | `hf download mlx-community/MiniMax-M3.1-Flash-Text-4bit` |
| `llm-minimax-m3-1-flash-mlx-oq4e-mtp` | MiniMax-M3.1-Flash-oQ4e-mtp · oQ4e-mtp (MLX) | 248.8 GB | 4.5 | 286 GB | T1,T2 | mac | `hf download mlx-community/MiniMax-M3.1-Flash-oQ4e-mtp` |
| `llm-minimax-m3-1-flash-safetensors-native-native` | MiniMax-M3.1-Flash · native ~4bit (safetensors(native)) | 252.4 GB | 4.5 | 290 GB | T1,T2 | server | `hf download MiniMaxAI/MiniMax-M3.1-Flash` |
| `llm-minimax-m3-1-flash-gguf-q5-k-m` | MiniMaxAI.MiniMax-M3.1-Flash-GGUF · Q5_K_M (GGUF) | 302.9 GB | 5.5 | 348 GB | T1,T2,T3 | any | `hf download DevQuasar/MiniMaxAI.MiniMax-M3.1-Flash-GGUF --include "*Q5_K_M*"` |
</details>

<details><summary><b>Qwen3.8-Flash-Next</b> – 57 változat</summary>

| id | Fájl / repó | Méret | Bit | Min. memória (≈×1,15) | HW | Platform | Letöltés |
|---|---|---|---|---|---|---|---|
| `llm-qwen3-8-flash-next-gguf-ud-iq1-s` | Qwen3.8-Flash-Next-GGUF · UD-IQ1_S (GGUF) | 66.4 GB | 1.7 | 76 GB | T1,T2,T3,T4 | any | `hf download unsloth/Qwen3.8-Flash-Next-GGUF --include "*UD-IQ1_S*"` |
| `llm-qwen3-8-flash-next-gguf-q2-0` | Qwen3.8-Flash-Next-GSQ-RCO-GGUF · Q2_0 (GGUF) | 66.4 GB | 2.6 | 76 GB | T1,T2,T3 | any | `hf download ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF --include "*Q2_0*"` |
| `llm-qwen3-8-flash-next-gguf-ud-iq1-m` | Qwen3.8-Flash-Next-GGUF · UD-IQ1_M (GGUF) | 68.0 GB | 1.7 | 78 GB | T1,T2,T3,T4 | any | `hf download unsloth/Qwen3.8-Flash-Next-GGUF --include "*UD-IQ1_M*"` |
| `llm-qwen3-8-flash-next-gguf-iq2-xs` | Qwen3.8-Flash-Next-GSQ-RCO-GGUF · IQ2_XS (GGUF) | 68.0 GB | 2.6 | 78 GB | T1,T2,T3 | any | `hf download ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF --include "*IQ2_XS*"` |
| `llm-qwen3-8-flash-next-gguf-iq1-s` | Qwen3.8-Flash-Next-GGUF · IQ1_S (GGUF) | 70.1 GB | 1.7 | 81 GB | T1,T2,T3 | any | `hf download bartowski/Qwen3.8-Flash-Next-GGUF --include "*IQ1_S*"` |
| `llm-qwen3-8-flash-next-gguf-ud-q2-0` | Qwen3.8-Flash-Next-GGUF · UD-Q2_0 (GGUF) | 70.5 GB | 2.6 | 81 GB | T1,T2,T3,T4 | any | `hf download unsloth/Qwen3.8-Flash-Next-GGUF --include "*UD-Q2_0*"` |
| `llm-qwen3-8-flash-next-gguf-ud-iq2-xs` | Qwen3.8-Flash-Next-GGUF · UD-IQ2_XS (GGUF) | 75.8 GB | 2.6 | 87 GB | T1,T2,T3,T4 | any | `hf download unsloth/Qwen3.8-Flash-Next-GGUF --include "*UD-IQ2_XS*"` |
| `llm-qwen3-8-flash-next-gguf-iq3-xxs` | Qwen3.8-Flash-Next-GSQ-RCO-GGUF · IQ3_XXS (GGUF) | 75.8 GB | 3.5 | 87 GB | T1,T2,T3 | any | `hf download ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF --include "*IQ3_XXS*"` |
| `llm-qwen3-8-flash-next-gguf-ud-q2-k-xl` | Qwen3.8-Flash-Next-GGUF · UD-Q2_K_XL (GGUF) | 79.6 GB | 2.6 | 92 GB | T1,T2,T3,T4 | any | `hf download unsloth/Qwen3.8-Flash-Next-GGUF --include "*UD-Q2_K_XL*"` |
| `llm-qwen3-8-flash-next-gguf-iq2-m` | Qwen3.8-Flash-Next-GGUF · IQ2_M (GGUF) | 80.4 GB | 2.6 | 92 GB | T1,T2,T3 | any | `hf download bartowski/Qwen3.8-Flash-Next-GGUF --include "*IQ2_M*"` |
| `llm-qwen3-8-flash-next-gguf-i1-q2-k` | Qwen3.8-Flash-Next-i1-GGUF · i1-Q2_K (GGUF) | 80.5 GB | 2.6 | 93 GB | T1,T2,T3 | any | `hf download mradermacher/Qwen3.8-Flash-Next-i1-GGUF --include "*i1-Q2_K*"` |
| `llm-qwen3-8-flash-next-gguf-q2-k` | Qwen3.8-Flash-Next-GGUF · Q2_K (GGUF) | 80.5 GB | 2.6 | 93 GB | T1,T2,T3 | any | `hf download mradermacher/Qwen3.8-Flash-Next-GGUF --include "*Q2_K*"` |
| `llm-qwen3-8-flash-next-mlx-optiq-2bit` | Qwen3.8-Flash-Next-OptiQ-2bit · OptiQ-2bit (MLX) | 80.8 GB | 2.5 | 93 GB | T1,T2,T3,T4 | mac | `hf download mlx-community/Qwen3.8-Flash-Next-OptiQ-2bit` |
| `llm-qwen3-8-flash-next-gguf-q2-k-2` | Qwen3.8-Flash-Next-GGUF · Q2_K (GGUF) | 80.9 GB | 2.6 | 93 GB | T1,T2,T3 | any | `hf download bartowski/Qwen3.8-Flash-Next-GGUF --include "*Q2_K*"` |
| `llm-qwen3-8-flash-next-gguf-q2-k-3` | Qwen3.8-Flash-Next-GGUF · Q2_K (GGUF) | 83.1 GB | 2.6 | 96 GB | T1,T2,T3 | any | `hf download ggml-org/Qwen3.8-Flash-Next-GGUF --include "*Q2_K*"` |
| `llm-qwen3-8-flash-next-gguf-iq3-s` | Qwen3.8-Flash-Next-GSQ-RCO-GGUF · IQ3_S (GGUF) | 83.6 GB | 3.5 | 96 GB | T1,T2,T3 | any | `hf download ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF --include "*IQ3_S*"` |
| `llm-qwen3-8-flash-next-gguf-ud-iq3-xxs` | Qwen3.8-Flash-Next-GGUF · UD-IQ3_XXS (GGUF) | 83.6 GB | 3.5 | 96 GB | T1,T2,T3 | any | `hf download unsloth/Qwen3.8-Flash-Next-GGUF --include "*UD-IQ3_XXS*"` |
| `llm-qwen3-8-flash-next-gguf-q4-0` | Qwen3.8-Flash-Next-GGUF · Q4_0 (GGUF) | 85.7 GB | 4.5 | 99 GB | T1,T2,T3 | any | `hf download AesSedai/Qwen3.8-Flash-Next-GGUF --include "*Q4_0*"` |
| `llm-qwen3-8-flash-next-gguf-ud-q3-k-xl` | Qwen3.8-Flash-Next-GGUF · UD-Q3_K_XL (GGUF) | 89.5 GB | 3.5 | 103 GB | T1,T2,T3 | any | `hf download unsloth/Qwen3.8-Flash-Next-GGUF --include "*UD-Q3_K_XL*"` |
| `llm-qwen3-8-flash-next-gguf-i1-iq3-m` | Qwen3.8-Flash-Next-i1-GGUF · i1-IQ3_M (GGUF) | 89.5 GB | 3.5 | 103 GB | T1,T2,T3 | any | `hf download mradermacher/Qwen3.8-Flash-Next-i1-GGUF --include "*i1-IQ3_M*"` |
| `llm-qwen3-8-flash-next-gguf-iq3-m` | Qwen3.8-Flash-Next-GGUF · IQ3_M (GGUF) | 93.2 GB | 3.5 | 107 GB | T1,T2,T3 | any | `hf download bartowski/Qwen3.8-Flash-Next-GGUF --include "*IQ3_M*"` |
| `llm-qwen3-8-flash-next-gguf-ud-iq4-xs` | Qwen3.8-Flash-Next-GGUF · UD-IQ4_XS (GGUF) | 93.7 GB | 4.5 | 108 GB | T1,T2,T3 | any | `hf download unsloth/Qwen3.8-Flash-Next-GGUF --include "*UD-IQ4_XS*"` |
| `llm-qwen3-8-flash-next-gguf-i1-iq4-xs` | Qwen3.8-Flash-Next-i1-GGUF · i1-IQ4_XS (GGUF) | 97.5 GB | 4.5 | 112 GB | T1,T2,T3 | any | `hf download mradermacher/Qwen3.8-Flash-Next-i1-GGUF --include "*i1-IQ4_XS*"` |
| `llm-qwen3-8-flash-next-gguf-iq4-xs` | Qwen3.8-Flash-Next-GGUF · IQ4_XS (GGUF) | 97.7 GB | 4.5 | 112 GB | T1,T2,T3 | any | `hf download bartowski/Qwen3.8-Flash-Next-GGUF --include "*IQ4_XS*"` |
| `llm-qwen3-8-flash-next-gguf-iq4-nl` | Qwen3.8-Flash-Next-GGUF · IQ4_NL (GGUF) | 102.0 GB | 4.5 | 117 GB | T1,T2,T3 | any | `hf download ggml-org/Qwen3.8-Flash-Next-GGUF --include "*IQ4_NL*"` |
| `llm-qwen3-8-flash-next-ollama-ollama` |  · ollama qwen3.8-flash-next:125b-a6b-nvfp4 (ollama) | 104.8 GB | 4.5 | 121 GB | T1,T2,T3 | any | `ollama pull qwen3.8-flash-next:125b-a6b-nvfp4 / 125b-mlx` |
| `llm-qwen3-8-flash-next-gguf-ud-q4-k-xl` | Qwen3.8-Flash-Next-GGUF · UD-Q4_K_XL (GGUF) | 111.3 GB | 4.5 | 128 GB | T1,T2,T3 | any | `hf download unsloth/Qwen3.8-Flash-Next-GGUF --include "*UD-Q4_K_XL*"` |
| `llm-qwen3-8-flash-next-mlx-4bit` | Qwen3.8-Flash-Next-4bit · 4bit (MLX) | 111.5 GB | 4.5 | 128 GB | T1,T2,T3,T4 | mac | `hf download mlx-community/Qwen3.8-Flash-Next-4bit` |
| `llm-qwen3-8-flash-next-gguf-q4-k-m` | Qwen3.8-Flash-Next-GGUF · Q4_K_M (GGUF) | 119.2 GB | 4.5 | 137 GB | T1,T2,T3 | any | `hf download lmstudio-community/Qwen3.8-Flash-Next-GGUF --include "*Q4_K_M*"` |
| `llm-qwen3-8-flash-next-gguf-i1-q4-k-m` | Qwen3.8-Flash-Next-i1-GGUF · i1-Q4_K_M (GGUF) | 119.2 GB | 4.5 | 137 GB | T1,T2,T3 | any | `hf download mradermacher/Qwen3.8-Flash-Next-i1-GGUF --include "*i1-Q4_K_M*"` |
| `llm-qwen3-8-flash-next-gguf-q4-k-m-2` | Qwen3.8-Flash-Next-GGUF · Q4_K_M (GGUF) | 119.2 GB | 4.5 | 137 GB | T1,T2,T3 | any | `hf download mradermacher/Qwen3.8-Flash-Next-GGUF --include "*Q4_K_M*"` |
| `llm-qwen3-8-flash-next-gguf-q4-k-m-3` | Qwen3.8-Flash-Next-GGUF · Q4_K_M (GGUF) | 119.6 GB | 4.5 | 138 GB | T1,T2,T3 | any | `hf download bartowski/Qwen3.8-Flash-Next-GGUF --include "*Q4_K_M*"` |
| `llm-qwen3-8-flash-next-ollama-ollama-2` |  · ollama qwen3.8-flash-next:125b-a6b-q4_K_ (ollama) | 120.1 GB | 4.5 | 138 GB | T1,T2,T3 | any | `ollama pull qwen3.8-flash-next:125b-a6b-q4_K_M` |
| `llm-qwen3-8-flash-next-nvfp4-nvfp4` | Qwen3.8-Flash-Next-NVFP4 · NVFP4 (NVFP4) | 132.7 GB | 4.5 | 153 GB | T1,T2,T3 | server | `hf download nvidia/Qwen3.8-Flash-Next-NVFP4` |
| `llm-qwen3-8-flash-next-gguf-i1-q5-k-m` | Qwen3.8-Flash-Next-i1-GGUF · i1-Q5_K_M (GGUF) | 134.1 GB | 5.5 | 154 GB | T1,T2,T3 | any | `hf download mradermacher/Qwen3.8-Flash-Next-i1-GGUF --include "*i1-Q5_K_M*"` |
| `llm-qwen3-8-flash-next-gguf-q5-k-m` | Qwen3.8-Flash-Next-GGUF · Q5_K_M (GGUF) | 134.7 GB | 5.5 | 155 GB | T1,T2,T3 | any | `hf download bartowski/Qwen3.8-Flash-Next-GGUF --include "*Q5_K_M*"` |
| `llm-qwen3-8-flash-next-mlx-oq6e-mtp` | Qwen3.8-Flash-Next-oQ6e-mtp · oQ6e-mtp (MLX) | 150.5 GB | 6.5 | 173 GB | T1,T2 | mac | `hf download mlx-community/Qwen3.8-Flash-Next-oQ6e-mtp` |
| `llm-qwen3-8-flash-next-gguf-ud-q5-k-xl` | Qwen3.8-Flash-Next-GGUF · UD-Q5_K_XL (GGUF) | 158.3 GB | 5.5 | 182 GB | T1,T2,T3 | any | `hf download unsloth/Qwen3.8-Flash-Next-GGUF --include "*UD-Q5_K_XL*"` |
| `llm-qwen3-8-flash-next-gguf-q8-0` | Qwen3.8-Flash-Next-GGUF · Q8_0 (GGUF) | 162.6 GB | 8.5 | 187 GB | T1,T2,T3 | any | `hf download ggml-org/Qwen3.8-Flash-Next-GGUF --include "*Q8_0*"` |
| `llm-qwen3-8-flash-next-gguf-q5-k-m-2` | Qwen3.8-Flash-Next-GGUF · Q5_K_M (GGUF) | 164.4 GB | 5.5 | 189 GB | T1,T2,T3 | any | `hf download AesSedai/Qwen3.8-Flash-Next-GGUF --include "*Q5_K_M*"` |
| `llm-qwen3-8-flash-next-gguf-q6-k` | Qwen3.8-Flash-Next-GGUF · Q6_K (GGUF) | 167.6 GB | 6.5 | 193 GB | T1,T2,T3 | any | `hf download lmstudio-community/Qwen3.8-Flash-Next-GGUF --include "*Q6_K*"` |
| `llm-qwen3-8-flash-next-gguf-i1-q6-k` | Qwen3.8-Flash-Next-i1-GGUF · i1-Q6_K (GGUF) | 167.6 GB | 6.5 | 193 GB | T1,T2,T3 | any | `hf download mradermacher/Qwen3.8-Flash-Next-i1-GGUF --include "*i1-Q6_K*"` |
| `llm-qwen3-8-flash-next-gguf-q6-k-2` | Qwen3.8-Flash-Next-GGUF · Q6_K (GGUF) | 168.1 GB | 6.5 | 193 GB | T1,T2,T3 | any | `hf download bartowski/Qwen3.8-Flash-Next-GGUF --include "*Q6_K*"` |
| `llm-qwen3-8-flash-next-gguf-ud-q6-k-xl` | Qwen3.8-Flash-Next-GGUF · UD-Q6_K_XL (GGUF) | 169.2 GB | 6.5 | 195 GB | T1,T2,T3 | any | `hf download unsloth/Qwen3.8-Flash-Next-GGUF --include "*UD-Q6_K_XL*"` |
| `llm-qwen3-8-flash-next-autoround-w4a16` | Qwen3.8-Flash-Next-W4A16-AutoRound · W4A16 (AutoRound) | 181.2 GB | 4.5 | 208 GB | T1,T2 | server | `hf download Intel/Qwen3.8-Flash-Next-W4A16-AutoRound` |
| `llm-qwen3-8-flash-next-fp8-fp8` | Qwen3.8-Flash-Next-FP8 · FP8 (FP8) | 185.6 GB | 8.5 | 213 GB | T1,T2 | server | `hf download Qwen/Qwen3.8-Flash-Next-FP8` |
| `llm-qwen3-8-flash-next-nvfp4-nvfp4-2` | Qwen3.8-Flash-Next-NVFP4 · NVFP4 (NVFP4) | 186.4 GB | 4.5 | 214 GB | T1,T2 | server | `hf download RedHatAI/Qwen3.8-Flash-Next-NVFP4` |
| `llm-qwen3-8-flash-next-gguf-q8-0-2` | Qwen3.8-Flash-Next-GGUF · Q8_0 (GGUF) | 188.2 GB | 8.5 | 216 GB | T1,T2,T3 | any | `hf download lmstudio-community/Qwen3.8-Flash-Next-GGUF --include "*Q8_0*"` |
| `llm-qwen3-8-flash-next-gguf-q8-0-3` | Qwen3.8-Flash-Next-GGUF · Q8_0 (GGUF) | 188.2 GB | 8.5 | 216 GB | T1,T2,T3 | any | `hf download mradermacher/Qwen3.8-Flash-Next-GGUF --include "*Q8_0*"` |
| `llm-qwen3-8-flash-next-gguf-q8-0-4` | Qwen3.8-Flash-Next-GGUF · Q8_0 (GGUF) | 188.2 GB | 8.5 | 216 GB | T1,T2,T3 | any | `hf download unsloth/Qwen3.8-Flash-Next-GGUF --include "*Q8_0*"` |
| `llm-qwen3-8-flash-next-gguf-q8-0-5` | Qwen3.8-Flash-Next-GGUF · Q8_0 (GGUF) | 188.3 GB | 8.5 | 216 GB | T1,T2,T3 | any | `hf download bartowski/Qwen3.8-Flash-Next-GGUF --include "*Q8_0*"` |
| `llm-qwen3-8-flash-next-awq-awq-int4` | Qwen3.8-Flash-Next-AWQ-INT4 · AWQ-INT4 (AWQ) | 188.3 GB | 4.5 | 217 GB | T1,T2 | server | `hf download cyankiwi/Qwen3.8-Flash-Next-AWQ-INT4` |
| `llm-qwen3-8-flash-next-ollama-ollama-3` |  · ollama qwen3.8-flash-next:125b-a6b-q8_0 (ollama) | 189.1 GB | 8.5 | 217 GB | T1,T2,T3 | any | `ollama pull qwen3.8-flash-next:125b-a6b-q8_0` |
| `llm-qwen3-8-flash-next-mlx-oq8e-mtp` | Qwen3.8-Flash-Next-oQ8e-mtp · oQ8e-mtp (MLX) | 194.9 GB | 8.5 | 224 GB | T1,T2 | mac | `hf download mlx-community/Qwen3.8-Flash-Next-oQ8e-mtp` |
| `llm-qwen3-8-flash-next-gguf-bf16` | Qwen3.8-Flash-Next-GGUF · BF16 (GGUF) | 354.0 GB | 16 | 407 GB | T1,T2,T3 | any | `hf download unsloth/Qwen3.8-Flash-Next-GGUF --include "*BF16*"` |
| `llm-qwen3-8-flash-next-ollama-ollama-4` |  · ollama qwen3.8-flash-next:125b-a6b-bf16 (ollama) | 354.9 GB | 16 | 408 GB | T1,T2,T3 | any | `ollama pull qwen3.8-flash-next:125b-a6b-bf16` |
| `llm-qwen3-8-flash-next-ollama-ollama-5` |  · ollama qwen3.8-flash-next:125b-a6b-mlx-b (ollama) | 360.0 GB | 16 | 414 GB | T1,T2,T3 | any | `ollama pull qwen3.8-flash-next:125b-a6b-mlx-bf16` |
</details>

<details><summary><b>Step 5 Preview</b> – 8 változat</summary>

| id | Fájl / repó | Méret | Bit | Min. memória (≈×1,15) | HW | Platform | Letöltés |
|---|---|---|---|---|---|---|---|
| `llm-step-5-preview-gguf-q2-k` | Step-5-Preview-GGUF · Q2_K (GGUF) | 182.5 GB | 2.6 | 210 GB | T1,T2,T3 | any | `hf download smalinin/Step-5-Preview-GGUF --include "*Q2_K*"` |
| `llm-step-5-preview-gguf-ik-smol-iq3-ks-mix-b` | Step-5-Preview-GGUF · smol-IQ3_KS-mix-B (GGUF(ik)) | 248.8 GB | 3.5 | 286 GB | T1,T2 | any | `hf download L-Alchemyst/Step-5-Preview-GGUF --include "*smol-IQ3_KS-mix-B*"` |
| `llm-step-5-preview-gguf-iq3-m` | Step-5-Preview-GGUF · IQ3_M (+mmproj BF16 4.4) (GGUF) | 271.6 GB | 3.5 | 312 GB | T1,T2,T3 | any | `hf download smalinin/Step-5-Preview-GGUF --include "*IQ3_M*"` |
| `llm-step-5-preview-gguf-ik-iq3-ks-mix` | Step-5-Preview-GGUF · IQ3_KS-mix (GGUF(ik)) | 275.2 GB | 3.5 | 316 GB | T1,T2 | any | `hf download L-Alchemyst/Step-5-Preview-GGUF --include "*IQ3_KS-mix*"` |
| `llm-step-5-preview-gguf-ik-iq4-ks-mix` | Step-5-Preview-GGUF · IQ4_KS-mix (GGUF(ik)) | 333.0 GB | 4.5 | 383 GB | T1,T2 | any | `hf download L-Alchemyst/Step-5-Preview-GGUF --include "*IQ4_KS-mix*"` |
| `llm-step-5-preview-nvfp4-nvfp4` | Step-5-Preview-NVFP4 · NVFP4 (NVFP4) | 394.2 GB | 4.5 | 453 GB | T1,T2 | server | `hf download stepfun-ai/Step-5-Preview-NVFP4` |
| `llm-step-5-preview-native-native` | Step-5-Preview · native (native) | 650.3 GB | 16 | 748 GB | T1 | server | `hf download stepfun-ai/Step-5-Preview` |
| `llm-step-5-preview-bf16-bf16` | Step-5-Preview-BF16 · BF16 (BF16) | 1.21 TB | 16 | 1397 GB | T1 | server | `hf download stepfun-ai/Step-5-Preview-BF16` |
</details>

<details><summary><b>GLM-5.3-Flash</b> – 44 változat</summary>

| id | Fájl / repó | Méret | Bit | Min. memória (≈×1,15) | HW | Platform | Letöltés |
|---|---|---|---|---|---|---|---|
| `llm-glm-5-3-flash-gguf-iq1-s` | GLM-5.3-Flash-BF16-GGUF · IQ1_S (GGUF) | 74.8 GB | 1.7 | 86 GB | T1,T2,T3 | any | `hf download bartowski/GLM-5.3-Flash-BF16-GGUF --include "*IQ1_S*"` |
| `llm-glm-5-3-flash-gguf-ud-iq1-s` | GLM-5.3-Flash-GGUF · UD-IQ1_S (GGUF) | 93.1 GB | 1.7 | 107 GB | T1,T2,T3 | any | `hf download unsloth/GLM-5.3-Flash-GGUF --include "*UD-IQ1_S*"` |
| `llm-glm-5-3-flash-gguf-ud-iq1-m` | GLM-5.3-Flash-GGUF · UD-IQ1_M (GGUF) | 97.6 GB | 1.7 | 112 GB | T1,T2,T3 | any | `hf download unsloth/GLM-5.3-Flash-GGUF --include "*UD-IQ1_M*"` |
| `llm-glm-5-3-flash-gguf-ud-iq2-xxs` | GLM-5.3-Flash-GGUF · UD-IQ2_XXS (GGUF) | 101.8 GB | 2.6 | 117 GB | T1,T2,T3 | any | `hf download unsloth/GLM-5.3-Flash-GGUF --include "*UD-IQ2_XXS*"` |
| `llm-glm-5-3-flash-gguf-ud-q2-k-xl` | GLM-5.3-Flash-GGUF · UD-Q2_K_XL (GGUF) | 108.7 GB | 2.6 | 125 GB | T1,T2,T3 | any | `hf download unsloth/GLM-5.3-Flash-GGUF --include "*UD-Q2_K_XL*"` |
| `llm-glm-5-3-flash-gguf-iq2-s` | GLM-5.3-Flash-GGUF · IQ2_S (GGUF) | 113.6 GB | 2.6 | 131 GB | T1,T2,T3 | any | `hf download AesSedai/GLM-5.3-Flash-GGUF --include "*IQ2_S*"` |
| `llm-glm-5-3-flash-gguf-i1-q2-k` | GLM-5.3-Flash-i1-GGUF · i1-Q2_K (GGUF) | 117.9 GB | 2.6 | 136 GB | T1,T2,T3 | any | `hf download mradermacher/GLM-5.3-Flash-i1-GGUF --include "*i1-Q2_K*"` |
| `llm-glm-5-3-flash-gguf-q2-k` | GLM-5.3-Flash-GGUF · Q2_K (GGUF) | 117.9 GB | 2.6 | 136 GB | T1,T2,T3 | any | `hf download mradermacher/GLM-5.3-Flash-GGUF --include "*Q2_K*"` |
| `llm-glm-5-3-flash-gguf-ud-iq3-xxs` | GLM-5.3-Flash-GGUF · UD-IQ3_XXS (GGUF) | 120.4 GB | 3.5 | 138 GB | T1,T2,T3 | any | `hf download unsloth/GLM-5.3-Flash-GGUF --include "*UD-IQ3_XXS*"` |
| `llm-glm-5-3-flash-gguf-iq2-m` | GLM-5.3-Flash-BF16-GGUF · IQ2_M (GGUF) | 120.6 GB | 2.6 | 139 GB | T1,T2,T3 | any | `hf download bartowski/GLM-5.3-Flash-BF16-GGUF --include "*IQ2_M*"` |
| `llm-glm-5-3-flash-gguf-iq3-s` | GLM-5.3-Flash-GGUF · IQ3_S (GGUF) | 124.7 GB | 3.5 | 143 GB | T1,T2,T3 | any | `hf download AesSedai/GLM-5.3-Flash-GGUF --include "*IQ3_S*"` |
| `llm-glm-5-3-flash-gguf-i1-iq3-m` | GLM-5.3-Flash-i1-GGUF · i1-IQ3_M (GGUF) | 140.4 GB | 3.5 | 161 GB | T1,T2,T3 | any | `hf download mradermacher/GLM-5.3-Flash-i1-GGUF --include "*i1-IQ3_M*"` |
| `llm-glm-5-3-flash-gguf-ud-q3-k-xl` | GLM-5.3-Flash-GGUF · UD-Q3_K_XL (GGUF) | 147.5 GB | 3.5 | 170 GB | T1,T2,T3 | any | `hf download unsloth/GLM-5.3-Flash-GGUF --include "*UD-Q3_K_XL*"` |
| `llm-glm-5-3-flash-gguf-q3-k-m` | GLM-5.3-Flash-GGUF · Q3_K_M (GGUF) | 153.7 GB | 3.5 | 177 GB | T1,T2,T3 | any | `hf download mradermacher/GLM-5.3-Flash-GGUF --include "*Q3_K_M*"` |
| `llm-glm-5-3-flash-gguf-q3-k-m-2` | GLM-5.3-Flash-BF16-GGUF · Q3_K_M (GGUF) | 155.0 GB | 3.5 | 178 GB | T1,T2,T3 | any | `hf download bartowski/GLM-5.3-Flash-BF16-GGUF --include "*Q3_K_M*"` |
| `llm-glm-5-3-flash-gguf-ud-iq4-xs` | GLM-5.3-Flash-GGUF · UD-IQ4_XS (GGUF) | 156.8 GB | 4.5 | 180 GB | T1,T2,T3 | any | `hf download unsloth/GLM-5.3-Flash-GGUF --include "*UD-IQ4_XS*"` |
| `llm-glm-5-3-flash-gguf-iq4-xs` | GLM-5.3-Flash-GGUF · IQ4_XS (GGUF) | 159.2 GB | 4.5 | 183 GB | T1,T2,T3 | any | `hf download AesSedai/GLM-5.3-Flash-GGUF --include "*IQ4_XS*"` |
| `llm-glm-5-3-flash-gguf-i1-iq4-xs` | GLM-5.3-Flash-i1-GGUF · i1-IQ4_XS (GGUF) | 171.8 GB | 4.5 | 198 GB | T1,T2,T3 | any | `hf download mradermacher/GLM-5.3-Flash-i1-GGUF --include "*i1-IQ4_XS*"` |
| `llm-glm-5-3-flash-autoround-w4a16` | GLM-5.3-Flash-W4A16-AutoRound · W4A16 (AutoRound) | 181.5 GB | 4.5 | 209 GB | T1,T2 | server | `hf download Intel/GLM-5.3-Flash-W4A16-AutoRound` |
| `llm-glm-5-3-flash-gguf-i1-q4-k-m` | GLM-5.3-Flash-i1-GGUF · i1-Q4_K_M (GGUF) | 193.8 GB | 4.5 | 223 GB | T1,T2,T3 | any | `hf download mradermacher/GLM-5.3-Flash-i1-GGUF --include "*i1-Q4_K_M*"` |
| `llm-glm-5-3-flash-gguf-q4-k-m` | GLM-5.3-Flash-GGUF · Q4_K_M (GGUF) | 193.8 GB | 4.5 | 223 GB | T1,T2,T3 | any | `hf download mradermacher/GLM-5.3-Flash-GGUF --include "*Q4_K_M*"` |
| `llm-glm-5-3-flash-awq-awq-int4` | GLM-5.3-Flash-AWQ-INT4 · AWQ-INT4 (AWQ) | 197.2 GB | 4.5 | 227 GB | T1,T2 | server | `hf download cyankiwi/GLM-5.3-Flash-AWQ-INT4` |
| `llm-glm-5-3-flash-nvfp4-nvfp4` | GLM-5.3-Flash-NVFP4 · NVFP4 (NVFP4) | 197.9 GB | 4.5 | 228 GB | T1,T2 | server | `hf download RedHatAI/GLM-5.3-Flash-NVFP4` |
| `llm-glm-5-3-flash-gguf-ud-q4-k-xl` | GLM-5.3-Flash-GGUF · UD-Q4_K_XL (GGUF) | 199.7 GB | 4.5 | 230 GB | T1,T2 | any | `hf download unsloth/GLM-5.3-Flash-GGUF --include "*UD-Q4_K_XL*"` |
| `llm-glm-5-3-flash-gguf-q4-k-m-2` | GLM-5.3-Flash-BF16-GGUF · Q4_K_M (GGUF) | 200.8 GB | 4.5 | 231 GB | T1,T2,T3 | any | `hf download bartowski/GLM-5.3-Flash-BF16-GGUF --include "*Q4_K_M*"` |
| `llm-glm-5-3-flash-gguf-q4-k-m-3` | GLM-5.3-Flash-GGUF · Q4_K_M (GGUF) | 202.0 GB | 4.5 | 232 GB | T1,T2,T3 | any | `hf download AesSedai/GLM-5.3-Flash-GGUF --include "*Q4_K_M*"` |
| `llm-glm-5-3-flash-mlx-4bit` | GLM-5.3-Flash-4bit · 4bit (MLX) | 204.0 GB | 4.5 | 235 GB | T1,T2 | mac | `hf download mlx-community/GLM-5.3-Flash-4bit` |
| `llm-glm-5-3-flash-nvfp4-nvfp4-2` | GLM-5.3-Flash-NVFP4 · NVFP4 (NVFP4) | 204.5 GB | 4.5 | 235 GB | T1,T2 | server | `hf download nvidia/GLM-5.3-Flash-NVFP4` |
| `llm-glm-5-3-flash-gguf-i1-q5-k-m` | GLM-5.3-Flash-i1-GGUF · i1-Q5_K_M (GGUF) | 227.9 GB | 5.5 | 262 GB | T1,T2,T3 | any | `hf download mradermacher/GLM-5.3-Flash-i1-GGUF --include "*i1-Q5_K_M*"` |
| `llm-glm-5-3-flash-gguf-q5-k-m` | GLM-5.3-Flash-GGUF · Q5_K_M (GGUF) | 227.9 GB | 5.5 | 262 GB | T1,T2,T3 | any | `hf download mradermacher/GLM-5.3-Flash-GGUF --include "*Q5_K_M*"` |
| `llm-glm-5-3-flash-gguf-ud-q5-k-xl` | GLM-5.3-Flash-GGUF · UD-Q5_K_XL (GGUF) | 240.3 GB | 5.5 | 276 GB | T1,T2 | any | `hf download unsloth/GLM-5.3-Flash-GGUF --include "*UD-Q5_K_XL*"` |
| `llm-glm-5-3-flash-gguf-q5-k-m-2` | GLM-5.3-Flash-GGUF · Q5_K_M (GGUF) | 240.8 GB | 5.5 | 277 GB | T1,T2,T3 | any | `hf download AesSedai/GLM-5.3-Flash-GGUF --include "*Q5_K_M*"` |
| `llm-glm-5-3-flash-gguf-q5-k-m-3` | GLM-5.3-Flash-BF16-GGUF · Q5_K_M (GGUF) | 243.7 GB | 5.5 | 280 GB | T1,T2,T3 | any | `hf download bartowski/GLM-5.3-Flash-BF16-GGUF --include "*Q5_K_M*"` |
| `llm-glm-5-3-flash-gguf-i1-q6-k` | GLM-5.3-Flash-i1-GGUF · i1-Q6_K (GGUF) | 264.0 GB | 6.5 | 304 GB | T1,T2,T3 | any | `hf download mradermacher/GLM-5.3-Flash-i1-GGUF --include "*i1-Q6_K*"` |
| `llm-glm-5-3-flash-gguf-q6-k` | GLM-5.3-Flash-GGUF · Q6_K (GGUF) | 264.0 GB | 6.5 | 304 GB | T1,T2,T3 | any | `hf download mradermacher/GLM-5.3-Flash-GGUF --include "*Q6_K*"` |
| `llm-glm-5-3-flash-gguf-q6-k-2` | GLM-5.3-Flash-BF16-GGUF · Q6_K (GGUF) | 281.0 GB | 6.5 | 323 GB | T1,T2,T3 | any | `hf download bartowski/GLM-5.3-Flash-BF16-GGUF --include "*Q6_K*"` |
| `llm-glm-5-3-flash-gguf-ud-q6-k-xl` | GLM-5.3-Flash-GGUF · UD-Q6_K_XL (GGUF) | 291.8 GB | 6.5 | 336 GB | T1,T2 | any | `hf download unsloth/GLM-5.3-Flash-GGUF --include "*UD-Q6_K_XL*"` |
| `llm-glm-5-3-flash-fp8-native-fp8` | GLM-5.3-Flash · FP8 (FP8(native)) | 328.4 GB | 8.5 | 378 GB | T1,T2 | server | `hf download zai-org/GLM-5.3-Flash` |
| `llm-glm-5-3-flash-fp8-fp8` | GLM-5.3-Flash-FP8 · FP8 (FP8) | 328.4 GB | 8.5 | 378 GB | T1 | server | `hf download unsloth/GLM-5.3-Flash-FP8` |
| `llm-glm-5-3-flash-gguf-q8-0` | GLM-5.3-Flash-GGUF · Q8_0 (GGUF) | 341.0 GB | 8.5 | 392 GB | T1,T2 | any | `hf download unsloth/GLM-5.3-Flash-GGUF --include "*Q8_0*"` |
| `llm-glm-5-3-flash-gguf-q8-0-2` | GLM-5.3-Flash-GGUF · Q8_0 (GGUF) | 341.5 GB | 8.5 | 393 GB | T1,T2,T3 | any | `hf download mradermacher/GLM-5.3-Flash-GGUF --include "*Q8_0*"` |
| `llm-glm-5-3-flash-gguf-q8-0-3` | GLM-5.3-Flash-BF16-GGUF · Q8_0 (GGUF) | 341.5 GB | 8.5 | 393 GB | T1,T2,T3 | any | `hf download bartowski/GLM-5.3-Flash-BF16-GGUF --include "*Q8_0*"` |
| `llm-glm-5-3-flash-gguf-bf16` | GLM-5.3-Flash-GGUF · BF16 (GGUF) | 641.6 GB | 16 | 738 GB | T1,T2 | any | `hf download unsloth/GLM-5.3-Flash-GGUF --include "*BF16*"` |
| `llm-glm-5-3-flash-bf16-bf16` | GLM-5.3-Flash-BF16 · BF16 (BF16) | 642.7 GB | 16 | 739 GB | T1 | server | `hf download zai-org/GLM-5.3-Flash-BF16` |
</details>

<details><summary><b>Mistral Large 4 (1T-A52B)</b> – 21 változat</summary>

| id | Fájl / repó | Méret | Bit | Min. memória (≈×1,15) | HW | Platform | Letöltés |
|---|---|---|---|---|---|---|---|
| `llm-mistral-large-4-gguf-ud-iq1-s` | Mistral-Large-4-1T-A52B-GGUF · UD-IQ1_S (GGUF) | 233.0 GB | 1.7 | 268 GB | T1,T2 | any | `hf download unsloth/Mistral-Large-4-1T-A52B-GGUF --include "*UD-IQ1_S*"` |
| `llm-mistral-large-4-gguf-ud-iq1-m` | Mistral-Large-4-1T-A52B-GGUF · UD-IQ1_M (GGUF) | 259.6 GB | 1.7 | 299 GB | T1,T2 | any | `hf download unsloth/Mistral-Large-4-1T-A52B-GGUF --include "*UD-IQ1_M*"` |
| `llm-mistral-large-4-gguf-iq2-xxs` | Mistral-Large-4-1T-A52B-GGUF · IQ2_XXS (GGUF) | 297.7 GB | 2.6 | 342 GB | T1,T2 | any | `hf download ggml-org/Mistral-Large-4-1T-A52B-GGUF --include "*IQ2_XXS*"` |
| `llm-mistral-large-4-gguf-ud-iq2-xxs` | Mistral-Large-4-1T-A52B-GGUF · UD-IQ2_XXS (GGUF) | 302.5 GB | 2.6 | 348 GB | T1,T2 | any | `hf download unsloth/Mistral-Large-4-1T-A52B-GGUF --include "*UD-IQ2_XXS*"` |
| `llm-mistral-large-4-mlx-2bit` | Mistral-Large-4-1T-A52B-Text-2bit · 2bit text-only (MLX) | 338.2 GB | 2.5 | 389 GB | T1,T2 | mac | `hf download mlx-community/Mistral-Large-4-1T-A52B-Text-2bit` |
| `llm-mistral-large-4-gguf-ud-q2-k-xl` | Mistral-Large-4-1T-A52B-GGUF · UD-Q2_K_XL (GGUF) | 378.2 GB | 2.6 | 435 GB | T1,T2 | any | `hf download unsloth/Mistral-Large-4-1T-A52B-GGUF --include "*UD-Q2_K_XL*"` |
| `llm-mistral-large-4-gguf-q2-k` | Mistral-Large-4-1T-A52B-GGUF · Q2_K (GGUF) | 380.7 GB | 2.6 | 438 GB | T1,T2 | any | `hf download ggml-org/Mistral-Large-4-1T-A52B-GGUF --include "*Q2_K*"` |
| `llm-mistral-large-4-gguf-ud-iq3-xxs` | Mistral-Large-4-1T-A52B-GGUF · UD-IQ3_XXS (GGUF) | 423.5 GB | 3.5 | 487 GB | T1,T2 | any | `hf download unsloth/Mistral-Large-4-1T-A52B-GGUF --include "*UD-IQ3_XXS*"` |
| `llm-mistral-large-4-mlx-3bit` | Mistral-Large-4-1T-A52B-Text-3bit · 3bit text-only (MLX) | 459.3 GB | 3.5 | 528 GB | T1,T2 | mac | `hf download mlx-community/Mistral-Large-4-1T-A52B-Text-3bit` |
| `llm-mistral-large-4-gguf-ud-q3-k-xl` | Mistral-Large-4-1T-A52B-GGUF · UD-Q3_K_XL (GGUF) | 492.8 GB | 3.5 | 567 GB | T1,T2 | any | `hf download unsloth/Mistral-Large-4-1T-A52B-GGUF --include "*UD-Q3_K_XL*"` |
| `llm-mistral-large-4-mlx-4bit` | Mistral-Large-4-1T-A52B-Text-4bit · 4bit text-only (MLX) | 590.4 GB | 4.5 | 679 GB | T1,T2 | mac | `hf download mlx-community/Mistral-Large-4-1T-A52B-Text-4bit` |
| `llm-mistral-large-4-gguf-ud-q4-k-xl` | Mistral-Large-4-1T-A52B-GGUF · UD-Q4_K_XL (GGUF) | 604.8 GB | 4.5 | 696 GB | T1,T2 | any | `hf download unsloth/Mistral-Large-4-1T-A52B-GGUF --include "*UD-Q4_K_XL*"` |
| `llm-mistral-large-4-nvfp4-nvfp4` | Mistral-Large-4-1T-A52B-NVFP4 · NVFP4 (NVFP4) | 610.1 GB | 4.5 | 702 GB | T1,T2 | server | `hf download mistralai/Mistral-Large-4-1T-A52B-NVFP4` |
| `llm-mistral-large-4-gguf-q4-k-m` | Mistral-Large-4-1T-A52B-GGUF · Q4_K_M (GGUF) | 634.8 GB | 4.5 | 730 GB | T1,T2 | any | `hf download ggml-org/Mistral-Large-4-1T-A52B-GGUF --include "*Q4_K_M*"` |
| `llm-mistral-large-4-gguf-ud-q5-k-xl` | Mistral-Large-4-1T-A52B-GGUF · UD-Q5_K_XL (GGUF) | 783.8 GB | 5.5 | 901 GB | T1,T2 | any | `hf download unsloth/Mistral-Large-4-1T-A52B-GGUF --include "*UD-Q5_K_XL*"` |
| `llm-mistral-large-4-gguf-ud-q6-k-xl` | Mistral-Large-4-1T-A52B-GGUF · UD-Q6_K_XL (GGUF) | 890.5 GB | 6.5 | 1024 GB | T1,T2 | any | `hf download unsloth/Mistral-Large-4-1T-A52B-GGUF --include "*UD-Q6_K_XL*"` |
| `llm-mistral-large-4-fp8-native-fp8` | Mistral-Large-4-1T-A52B · FP8 (FP8(native)) | 1.06 TB | 8.5 | 1220 GB | T1 | server | `hf download mistralai/Mistral-Large-4-1T-A52B` |
| `llm-mistral-large-4-gguf-q8-0` | Mistral-Large-4-1T-A52B-GGUF · Q8_0 (GGUF) | 1.12 TB | 8.5 | 1282 GB | T1,T2 | any | `hf download unsloth/Mistral-Large-4-1T-A52B-GGUF --include "*Q8_0*"` |
| `llm-mistral-large-4-gguf-q8-0-2` | Mistral-Large-4-1T-A52B-GGUF · Q8_0 (GGUF) | 1.12 TB | 8.5 | 1282 GB | T1,T2 | any | `hf download ggml-org/Mistral-Large-4-1T-A52B-GGUF --include "*Q8_0*"` |
| `llm-mistral-large-4-gguf-bf16` | Mistral-Large-4-1T-A52B-GGUF · BF16 (GGUF) | 2.10 TB | 16 | 2414 GB | T1,T2 | any | `hf download unsloth/Mistral-Large-4-1T-A52B-GGUF --include "*BF16*"` |
| `llm-mistral-large-4-gguf-bf16-2` | Mistral-Large-4-1T-A52B-GGUF · BF16 (GGUF) | 2.10 TB | 16 | 2414 GB | T1,T2 | any | `hf download ggml-org/Mistral-Large-4-1T-A52B-GGUF --include "*BF16*"` |
</details>

<details><summary><b>Muse Spark Open (816B-A42B)</b> – 17 változat</summary>

| id | Fájl / repó | Méret | Bit | Min. memória (≈×1,15) | HW | Platform | Letöltés |
|---|---|---|---|---|---|---|---|
| `llm-muse-spark-open-gguf-ud-iq1-s` | Muse-Spark-Open-816B-A42B-GGUF · UD-IQ1_S (GGUF) | 175.6 GB | 1.7 | 202 GB | T1,T2,T3 | any | `hf download unsloth/Muse-Spark-Open-816B-A42B-GGUF --include "*UD-IQ1_S*"` |
| `llm-muse-spark-open-gguf-ud-iq1-m` | Muse-Spark-Open-816B-A42B-GGUF · UD-IQ1_M (GGUF) | 208.9 GB | 1.7 | 240 GB | T1,T2,T3 | any | `hf download unsloth/Muse-Spark-Open-816B-A42B-GGUF --include "*UD-IQ1_M*"` |
| `llm-muse-spark-open-gguf-ud-iq2-xxs` | Muse-Spark-Open-816B-A42B-GGUF · UD-IQ2_XXS (GGUF) | 225.6 GB | 2.6 | 259 GB | T1,T2,T3 | any | `hf download unsloth/Muse-Spark-Open-816B-A42B-GGUF --include "*UD-IQ2_XXS*"` |
| `llm-muse-spark-open-gguf-ud-iq2-s` | Muse-Spark-Open-816B-A42B-GGUF · UD-IQ2_S (GGUF) | 275.5 GB | 2.6 | 317 GB | T1,T2,T3 | any | `hf download unsloth/Muse-Spark-Open-816B-A42B-GGUF --include "*UD-IQ2_S*"` |
| `llm-muse-spark-open-gguf-q2-k` | Muse-Spark-Open-816B-A42B-GGUF · Q2_K (GGUF) | 304.1 GB | 2.6 | 350 GB | T1,T2 | any | `hf download ggml-org/Muse-Spark-Open-816B-A42B-GGUF --include "*Q2_K*"` |
| `llm-muse-spark-open-gguf-ud-q2-k-xl` | Muse-Spark-Open-816B-A42B-GGUF · UD-Q2_K_XL (GGUF) | 311.2 GB | 2.6 | 358 GB | T1,T2,T3 | any | `hf download unsloth/Muse-Spark-Open-816B-A42B-GGUF --include "*UD-Q2_K_XL*"` |
| `llm-muse-spark-open-gguf-ud-iq3-xxs` | Muse-Spark-Open-816B-A42B-GGUF · UD-IQ3_XXS (GGUF) | 340.4 GB | 3.5 | 391 GB | T1,T2 | any | `hf download unsloth/Muse-Spark-Open-816B-A42B-GGUF --include "*UD-IQ3_XXS*"` |
| `llm-muse-spark-open-gguf-ud-q3-k-xl` | Muse-Spark-Open-816B-A42B-GGUF · UD-Q3_K_XL (GGUF) | 401.5 GB | 3.5 | 462 GB | T1,T2 | any | `hf download unsloth/Muse-Spark-Open-816B-A42B-GGUF --include "*UD-Q3_K_XL*"` |
| `llm-muse-spark-open-mlx-3bit` | Muse-Spark-Open-816B-A42B-3bit · 3bit (MLX) | 436.2 GB | 3.5 | 502 GB | T1,T2 | mac | `hf download mlx-community/Muse-Spark-Open-816B-A42B-3bit` |
| `llm-muse-spark-open-gguf-q4-k-s` | Muse-Spark-Open-816B-A42B-GGUF · Q4_K_S (GGUF) | 470.1 GB | 4.5 | 541 GB | T1,T2 | any | `hf download ggml-org/Muse-Spark-Open-816B-A42B-GGUF --include "*Q4_K_S*"` |
| `llm-muse-spark-open-gguf-ud-q4-k-xl` | Muse-Spark-Open-816B-A42B-GGUF · UD-Q4_K_XL (+mmproj BF16 4.1) (GGUF) | 505.5 GB | 4.5 | 581 GB | T1,T2 | any | `hf download unsloth/Muse-Spark-Open-816B-A42B-GGUF --include "*UD-Q4_K_XL*"` |
| `llm-muse-spark-open-mxfp4-mxfp4` | Muse-Spark-Open-816B-A42B-Quark-MXFP4 · MXFP4 (MXFP4) | 508.9 GB | 4.5 | 585 GB | T1 | server | `hf download amd/Muse-Spark-Open-816B-A42B-Quark-MXFP4` |
| `llm-muse-spark-open-mlx-4bit` | Muse-Spark-Open-816B-A42B-4bit · 4bit (MLX) | 532.8 GB | 4.5 | 613 GB | T1,T2 | mac | `hf download mlx-community/Muse-Spark-Open-816B-A42B-4bit` |
| `llm-muse-spark-open-nvfp4-nvfp4` | Muse-Spark-Open-816B-A42B-NVFP4 · NVFP4 (NVFP4) | 533.0 GB | 4.5 | 613 GB | T1 | server | `hf download meta-models/Muse-Spark-Open-816B-A42B-NVFP4` |
| `llm-muse-spark-open-gguf-q8-0` | Muse-Spark-Open-816B-A42B-GGUF · Q8_0 (GGUF) | 871.6 GB | 8.5 | 1002 GB | T1,T2 | any | `hf download ggml-org/Muse-Spark-Open-816B-A42B-GGUF --include "*Q8_0*"` |
| `llm-muse-spark-open-gguf-bf16` | Muse-Spark-Open-816B-A42B-GGUF · BF16 (GGUF) | 1.64 TB | 16 | 1886 GB | T1,T2 | any | `hf download ggml-org/Muse-Spark-Open-816B-A42B-GGUF --include "*BF16*"` |
| `llm-muse-spark-open-bf16-bf16` | Muse-Spark-Open-816B-A42B · BF16 (BF16) | 1.64 TB | 16 | 1891 GB | T1 | server | `hf download meta-models/Muse-Spark-Open-816B-A42B` |
</details>

<details><summary><b>Qwen3.8-27B (dense)</b> – 58 változat</summary>

| id | Fájl / repó | Méret | Bit | Min. memória (≈×1,15) | HW | Platform | Letöltés |
|---|---|---|---|---|---|---|---|
| `llm-qwen3-8-27b-gguf-ud-iq1-s` | Qwen3.8-27B-GGUF · UD-IQ1_S (GGUF) | 6.2 GB | 1.7 | 7 GB | T1,T2,T3,T4 | any | `hf download unsloth/Qwen3.8-27B-GGUF --include "*UD-IQ1_S*"` |
| `llm-qwen3-8-27b-gguf-ud-iq2-xxs` | Qwen3.8-27B-GGUF · UD-IQ2_XXS (GGUF) | 7.2 GB | 2.6 | 8 GB | T1,T2,T3,T4 | any | `hf download unsloth/Qwen3.8-27B-GGUF --include "*UD-IQ2_XXS*"` |
| `llm-qwen3-8-27b-gguf-ud-iq2-s` | Qwen3.8-27B-GGUF · UD-IQ2_S (GGUF) | 8.4 GB | 2.6 | 10 GB | T1,T2,T3,T4 | any | `hf download unsloth/Qwen3.8-27B-GGUF --include "*UD-IQ2_S*"` |
| `llm-qwen3-8-27b-gguf-iq2-xs` | Qwen3.8-27B-GSQ-RCO-GGUF · IQ2_XS (GGUF) | 8.4 GB | 2.6 | 10 GB | T1,T2,T3,T4 | any | `hf download ISTA-DASLab/Qwen3.8-27B-GSQ-RCO-GGUF --include "*IQ2_XS*"` |
| `llm-qwen3-8-27b-gguf-iq2-xxs` | Qwen3.8-27B-GGUF · IQ2_XXS (GGUF) | 8.9 GB | 2.6 | 10 GB | T1,T2,T3,T4 | any | `hf download bartowski/Qwen3.8-27B-GGUF --include "*IQ2_XXS*"` |
| `llm-qwen3-8-27b-gguf-iq2-s` | Qwen3.8-27B-GSQ-RCO-GGUF · IQ2_S (GGUF) | 9.3 GB | 2.6 | 11 GB | T1,T2,T3,T4 | any | `hf download ISTA-DASLab/Qwen3.8-27B-GSQ-RCO-GGUF --include "*IQ2_S*"` |
| `llm-qwen3-8-27b-gguf-ud-q2-k-xl` | Qwen3.8-27B-GGUF · UD-Q2_K_XL (GGUF) | 9.9 GB | 2.6 | 11 GB | T1,T2,T3,T4 | any | `hf download unsloth/Qwen3.8-27B-GGUF --include "*UD-Q2_K_XL*"` |
| `llm-qwen3-8-27b-gguf-iq3-xxs` | Qwen3.8-27B-GSQ-RCO-GGUF · IQ3_XXS (GGUF) | 10.1 GB | 3.5 | 12 GB | T1,T2,T3,T4 | any | `hf download ISTA-DASLab/Qwen3.8-27B-GSQ-RCO-GGUF --include "*IQ3_XXS*"` |
| `llm-qwen3-8-27b-gguf-q2-k` | Qwen3.8-27B-GGUF · Q2_K (GGUF) | 10.8 GB | 2.6 | 12 GB | T1,T2,T3,T4 | any | `hf download bartowski/Qwen3.8-27B-GGUF --include "*Q2_K*"` |
| `llm-qwen3-8-27b-gguf-q2-k-2` | Qwen3.8-27B-i1-GGUF · Q2_K (GGUF) | 10.9 GB | 2.6 | 12 GB | T1,T2,T3,T4 | any | `hf download mradermacher/Qwen3.8-27B-i1-GGUF --include "*Q2_K*"` |
| `llm-qwen3-8-27b-gguf-ud-iq3-xxs` | Qwen3.8-27B-GGUF · UD-IQ3_XXS (GGUF) | 10.9 GB | 3.5 | 13 GB | T1,T2,T3,T4 | any | `hf download unsloth/Qwen3.8-27B-GGUF --include "*UD-IQ3_XXS*"` |
| `llm-qwen3-8-27b-gguf-iq3-s` | Qwen3.8-27B-GSQ-RCO-GGUF · IQ3_S (GGUF) | 11.8 GB | 3.5 | 14 GB | T1,T2,T3,T4 | any | `hf download ISTA-DASLab/Qwen3.8-27B-GSQ-RCO-GGUF --include "*IQ3_S*"` |
| `llm-qwen3-8-27b-gguf-ud-iq3-s` | Qwen3.8-27B-GGUF · UD-IQ3_S (GGUF) | 12.0 GB | 3.5 | 14 GB | T1,T2,T3,T4 | any | `hf download unsloth/Qwen3.8-27B-GGUF --include "*UD-IQ3_S*"` |
| `llm-qwen3-8-27b-gguf-iq3-m` | Qwen3.8-27B-i1-GGUF · IQ3_M (GGUF) | 12.8 GB | 3.5 | 15 GB | T1,T2,T3,T4 | any | `hf download mradermacher/Qwen3.8-27B-i1-GGUF --include "*IQ3_M*"` |
| `llm-qwen3-8-27b-gguf-ud-q3-k-xl` | Qwen3.8-27B-GGUF · UD-Q3_K_XL (GGUF) | 13.2 GB | 3.5 | 15 GB | T1,T2,T3,T4 | any | `hf download unsloth/Qwen3.8-27B-GGUF --include "*UD-Q3_K_XL*"` |
| `llm-qwen3-8-27b-gguf-ud-iq4-xs` | Qwen3.8-27B-GGUF · UD-IQ4_XS (GGUF) | 14.3 GB | 4.5 | 17 GB | T1,T2,T3,T4 | any | `hf download unsloth/Qwen3.8-27B-GGUF --include "*UD-IQ4_XS*"` |
| `llm-qwen3-8-27b-gguf-iq3-m-2` | Qwen3.8-27B-GGUF · IQ3_M (GGUF) | 14.9 GB | 3.5 | 17 GB | T1,T2,T3,T4 | any | `hf download bartowski/Qwen3.8-27B-GGUF --include "*IQ3_M*"` |
| `llm-qwen3-8-27b-gguf-iq4-xs` | Qwen3.8-27B-i1-GGUF · IQ4_XS (GGUF) | 15.3 GB | 4.5 | 18 GB | T1,T2,T3,T4 | any | `hf download mradermacher/Qwen3.8-27B-i1-GGUF --include "*IQ4_XS*"` |
| `llm-qwen3-8-27b-gguf-iq4-xs-2` | Qwen3.8-27B-GGUF · IQ4_XS (GGUF) | 15.5 GB | 4.5 | 18 GB | T1,T2,T3,T4 | any | `hf download bartowski/Qwen3.8-27B-GGUF --include "*IQ4_XS*"` |
| `llm-qwen3-8-27b-mlx-4bit` | Qwen3.8-27B-4bit · 4bit (MLX) | 16.1 GB | 4.5 | 18 GB | T1,T2,T3,T4 | mac | `hf download mlx-community/Qwen3.8-27B-4bit` |
| `llm-qwen3-8-27b-mlx-4bit-2` | Qwen3.8-27B-MLX-4bit · 4bit (MLX) | 16.1 GB | 4.5 | 18 GB | T1,T2,T3,T4 | mac | `hf download lmstudio-community/Qwen3.8-27B-MLX-4bit` |
| `llm-qwen3-8-27b-gguf-ud-q4-k-m` | Qwen3.8-27B-GGUF · UD-Q4_K_M (GGUF) | 16.6 GB | 4.5 | 19 GB | T1,T2,T3,T4 | any | `hf download unsloth/Qwen3.8-27B-GGUF --include "*UD-Q4_K_M*"` |
| `llm-qwen3-8-27b-gguf-q4-k-m` | Qwen3.8-27B-GGUF · Q4_K_M (GGUF) | 16.8 GB | 4.5 | 19 GB | T1,T2,T3,T4 | any | `hf download lmstudio-community/Qwen3.8-27B-GGUF --include "*Q4_K_M*"` |
| `llm-qwen3-8-27b-gguf-q4-k-m-2` | Qwen3.8-27B-i1-GGUF · Q4_K_M (GGUF) | 16.8 GB | 4.5 | 19 GB | T1,T2,T3,T4 | any | `hf download mradermacher/Qwen3.8-27B-i1-GGUF --include "*Q4_K_M*"` |
| `llm-qwen3-8-27b-gguf-ik-iq4-ks` | Qwen3.8-27B-GGUF · IQ4_KS (+MTP) (GGUF(ik)) | 16.9 GB | 4.5 | 19 GB | T1,T2,T3 | any | `hf download ubergarm/Qwen3.8-27B-GGUF --include "*IQ4_KS*"` |
| `llm-qwen3-8-27b-gguf-q4-k-m-3` | Qwen3.8-27B-GGUF · Q4_K_M (GGUF) | 17.4 GB | 4.5 | 20 GB | T1,T2,T3,T4 | any | `hf download bartowski/Qwen3.8-27B-GGUF --include "*Q4_K_M*"` |
| `llm-qwen3-8-27b-gguf-ud-q4-k-xl` | Qwen3.8-27B-GGUF · UD-Q4_K_XL (GGUF) | 17.7 GB | 4.5 | 20 GB | T1,T2,T3,T4 | any | `hf download unsloth/Qwen3.8-27B-GGUF --include "*UD-Q4_K_XL*"` |
| `llm-qwen3-8-27b-ollama-ollama` |  · ollama qwen3.8:27b / :latest / :27b-q4_K (ollama) | 17.7 GB | 4.5 | 20 GB | T1,T2,T3,T4 | any | `ollama pull qwen3.8:27b / :latest / :27b-q4_K_M / :27b-mtp-q4_K_M` |
| `llm-qwen3-8-27b-ollama-ollama-2` |  · ollama qwen3.8:27b-nvfp4 / :27b-mlx (ollama) | 18.2 GB | 4.5 | 21 GB | T1,T2,T3,T4 | any | `ollama pull qwen3.8:27b-nvfp4 / :27b-mlx` |
| `llm-qwen3-8-27b-gguf-q4-k-m-4` | Qwen3.8-27B-GGUF · Q4_K_M (GGUF) | 19.4 GB | 4.5 | 22 GB | T1,T2,T3 | any | `hf download ggml-org/Qwen3.8-27B-GGUF --include "*Q4_K_M*"` |
| `llm-qwen3-8-27b-mlx-5bit` | Qwen3.8-27B-MLX-5bit · 5bit (MLX) | 19.4 GB | 5.5 | 22 GB | T1,T2,T3,T4 | mac | `hf download lmstudio-community/Qwen3.8-27B-MLX-5bit` |
| `llm-qwen3-8-27b-gptq-int4-w4a16` | Qwen3.8-27B-INT4 · W4A16 (GPTQ/INT4) | 19.5 GB | 4.5 | 22 GB | T1,T2,T3 | server | `hf download RedHatAI/Qwen3.8-27B-INT4` |
| `llm-qwen3-8-27b-gguf-q5-k-m` | Qwen3.8-27B-i1-GGUF · Q5_K_M (GGUF) | 19.5 GB | 5.5 | 22 GB | T1,T2,T3,T4 | any | `hf download mradermacher/Qwen3.8-27B-i1-GGUF --include "*Q5_K_M*"` |
| `llm-qwen3-8-27b-gguf-q5-k-m-2` | Qwen3.8-27B-GGUF · Q5_K_M (GGUF) | 20.9 GB | 5.5 | 24 GB | T1,T2,T3,T4 | any | `hf download bartowski/Qwen3.8-27B-GGUF --include "*Q5_K_M*"` |
| `llm-qwen3-8-27b-gguf-ud-q5-k-xl` | Qwen3.8-27B-GGUF · UD-Q5_K_XL (GGUF) | 21.0 GB | 5.5 | 24 GB | T1,T2,T3,T4 | any | `hf download unsloth/Qwen3.8-27B-GGUF --include "*UD-Q5_K_XL*"` |
| `llm-qwen3-8-27b-awq-awq-int4` | Qwen3.8-27B-AWQ-INT4 · AWQ-INT4 (AWQ) | 21.0 GB | 4.5 | 24 GB | T1,T2,T3 | server | `hf download cyankiwi/Qwen3.8-27B-AWQ-INT4` |
| `llm-qwen3-8-27b-nvfp4-nvfp4` | Qwen3.8-27B-NVFP4 · NVFP4 (NVFP4) | 21.9 GB | 4.5 | 25 GB | T1,T2,T3 | server | `hf download nvidia/Qwen3.8-27B-NVFP4` |
| `llm-qwen3-8-27b-gguf-q6-k` | Qwen3.8-27B-GGUF · Q6_K (GGUF) | 22.4 GB | 6.5 | 26 GB | T1,T2,T3,T4 | any | `hf download lmstudio-community/Qwen3.8-27B-GGUF --include "*Q6_K*"` |
| `llm-qwen3-8-27b-gguf-q6-k-2` | Qwen3.8-27B-i1-GGUF · Q6_K (GGUF) | 22.4 GB | 6.5 | 26 GB | T1,T2,T3,T4 | any | `hf download mradermacher/Qwen3.8-27B-i1-GGUF --include "*Q6_K*"` |
| `llm-qwen3-8-27b-mlx-6bit` | Qwen3.8-27B-MLX-6bit · 6bit (MLX) | 22.8 GB | 6.5 | 26 GB | T1,T2,T3,T4 | mac | `hf download lmstudio-community/Qwen3.8-27B-MLX-6bit` |
| `llm-qwen3-8-27b-nvfp4-nvfp4-2` | Qwen3.8-27B-NVFP4 · NVFP4 (NVFP4) | 23.4 GB | 4.5 | 27 GB | T1,T2,T3 | server | `hf download unsloth/Qwen3.8-27B-NVFP4` |
| `llm-qwen3-8-27b-gguf-q6-k-3` | Qwen3.8-27B-GGUF · Q6_K (GGUF) | 23.9 GB | 6.5 | 27 GB | T1,T2,T3,T4 | any | `hf download bartowski/Qwen3.8-27B-GGUF --include "*Q6_K*"` |
| `llm-qwen3-8-27b-gguf-ud-q6-k-xl` | Qwen3.8-27B-GGUF · UD-Q6_K_XL (GGUF) | 25.3 GB | 6.5 | 29 GB | T1,T2,T3,T4 | any | `hf download unsloth/Qwen3.8-27B-GGUF --include "*UD-Q6_K_XL*"` |
| `llm-qwen3-8-27b-gguf-q8-0` | Qwen3.8-27B-GGUF · Q8_0 (GGUF) | 28.6 GB | 8.5 | 33 GB | T1,T2,T3 | any | `hf download ggml-org/Qwen3.8-27B-GGUF --include "*Q8_0*"` |
| `llm-qwen3-8-27b-gguf-q8-0-2` | Qwen3.8-27B-GGUF · Q8_0 (GGUF) | 29.1 GB | 8.5 | 33 GB | T1,T2,T3,T4 | any | `hf download unsloth/Qwen3.8-27B-GGUF --include "*Q8_0*"` |
| `llm-qwen3-8-27b-gguf-q8-0-3` | Qwen3.8-27B-GGUF · Q8_0 (GGUF) | 29.1 GB | 8.5 | 33 GB | T1,T2,T3,T4 | any | `hf download lmstudio-community/Qwen3.8-27B-GGUF --include "*Q8_0*"` |
| `llm-qwen3-8-27b-gguf-q8-0-4` | Qwen3.8-27B-GGUF · Q8_0 (GGUF) | 29.1 GB | 8.5 | 33 GB | T1,T2,T3,T4 | any | `hf download bartowski/Qwen3.8-27B-GGUF --include "*Q8_0*"` |
| `llm-qwen3-8-27b-mlx-8bit` | Qwen3.8-27B-8bit · 8bit (MLX) | 29.5 GB | 8.5 | 34 GB | T1,T2,T3,T4 | mac | `hf download mlx-community/Qwen3.8-27B-8bit` |
| `llm-qwen3-8-27b-mlx-8bit-2` | Qwen3.8-27B-MLX-8bit · 8bit (MLX) | 29.5 GB | 8.5 | 34 GB | T1,T2,T3,T4 | mac | `hf download lmstudio-community/Qwen3.8-27B-MLX-8bit` |
| `llm-qwen3-8-27b-ollama-ollama-3` |  · ollama qwen3.8:27b-q8_0 / :27b-mtp-q8_0 (ollama) | 30.0 GB | 8.5 | 34 GB | T1,T2,T3,T4 | any | `ollama pull qwen3.8:27b-q8_0 / :27b-mtp-q8_0` |
| `llm-qwen3-8-27b-ollama-ollama-4` |  · ollama qwen3.8:27b-mxfp8 (ollama) | 30.4 GB | 8.5 | 35 GB | T1,T2,T3,T4 | any | `ollama pull qwen3.8:27b-mxfp8` |
| `llm-qwen3-8-27b-fp8-fp8` | Qwen3.8-27B-FP8 · FP8 (FP8) | 30.9 GB | 8.5 | 36 GB | T1,T2,T3 | server | `hf download Qwen/Qwen3.8-27B-FP8` |
| `llm-qwen3-8-27b-fp8-fp8-2` | Qwen3.8-27B-FP8 · FP8 (FP8) | 30.9 GB | 8.5 | 36 GB | T1,T2,T3 | server | `hf download RedHatAI/Qwen3.8-27B-FP8` |
| `llm-qwen3-8-27b-gguf-ud-q8-k-xl` | Qwen3.8-27B-GGUF · UD-Q8_K_XL (GGUF) | 31.5 GB | 8.5 | 36 GB | T1,T2,T3,T4 | any | `hf download unsloth/Qwen3.8-27B-GGUF --include "*UD-Q8_K_XL*"` |
| `llm-qwen3-8-27b-gguf-bf16` | Qwen3.8-27B-GGUF · BF16 (+MTP, DFlash draft) (GGUF) | 53.8 GB | 16 | 62 GB | T1,T2,T3 | any | `hf download ggml-org/Qwen3.8-27B-GGUF --include "*BF16*"` |
| `llm-qwen3-8-27b-gguf-bf16-2` | Qwen3.8-27B-GGUF · BF16 (GGUF) | 54.7 GB | 16 | 63 GB | T1,T2,T3,T4 | any | `hf download unsloth/Qwen3.8-27B-GGUF --include "*BF16*"` |
| `llm-qwen3-8-27b-mlx-bf16` | Qwen3.8-27B-bf16 · bf16 (MLX) | 54.7 GB | 16 | 63 GB | T1,T2,T3,T4 | mac | `hf download mlx-community/Qwen3.8-27B-bf16` |
| `llm-qwen3-8-27b-ollama-ollama-5` |  · ollama qwen3.8:27b-bf16 (ollama) | 55.6 GB | 16 | 64 GB | T1,T2,T3,T4 | any | `ollama pull qwen3.8:27b-bf16` |
</details>

<details><summary><b>NVIDIA Nemotron 3.5 (Super-VL-120B-A12B, Lightning-30B-A3B, Bolt-E4B)</b> – 45 változat</summary>

| id | Fájl / repó | Méret | Bit | Min. memória (≈×1,15) | HW | Platform | Letöltés |
|---|---|---|---|---|---|---|---|
| `llm-nemotron-3-5-gguf-ud-iq2-m` | NVIDIA-Nemotron-3.5-Bolt-E4B-GGUF · UD-IQ2_M (GGUF) | 3.5 GB | 2.6 | 4 GB | T1,T2,T3,T4,T5 | any | `hf download unsloth/NVIDIA-Nemotron-3.5-Bolt-E4B-GGUF --include "*UD-IQ2_M*"` |
| `llm-nemotron-3-5-gguf-ud-q3-k-xl` | NVIDIA-Nemotron-3.5-Bolt-E4B-GGUF · UD-Q3_K_XL (GGUF) | 4.2 GB | 3.5 | 5 GB | T1,T2,T3,T4,T5 | any | `hf download unsloth/NVIDIA-Nemotron-3.5-Bolt-E4B-GGUF --include "*UD-Q3_K_XL*"` |
| `llm-nemotron-3-5-gguf-ud-q4-k-xl` | NVIDIA-Nemotron-3.5-Bolt-E4B-GGUF · UD-Q4_K_XL (GGUF) | 5.1 GB | 4.5 | 6 GB | T1,T2,T3,T4,T5 | any | `hf download unsloth/NVIDIA-Nemotron-3.5-Bolt-E4B-GGUF --include "*UD-Q4_K_XL*"` |
| `llm-nemotron-3-5-gguf-official-q4-k-m` | NVIDIA-Nemotron-3.5-Bolt-E4B-4GB · Q4_K_M (GGUF(official)) | 6.2 GB | 4.5 | 7 GB | T1,T2,T3,T4,T5 | any | `hf download nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-4GB --include "*Q4_K_M*"` |
| `llm-nemotron-3-5-ollama-ollama` |  · ollama nemotron-3.5-bolt:e4b-nvfp4 (ollama) | 7.2 GB | 4.5 | 8 GB | T1,T2,T3,T4 | any | `ollama pull nemotron-3.5-bolt:e4b-nvfp4` |
| `llm-nemotron-3-5-gguf-ud-q6-k-xl` | NVIDIA-Nemotron-3.5-Bolt-E4B-GGUF · UD-Q6_K_XL (GGUF) | 7.3 GB | 6.5 | 8 GB | T1,T2,T3,T4,T5 | any | `hf download unsloth/NVIDIA-Nemotron-3.5-Bolt-E4B-GGUF --include "*UD-Q6_K_XL*"` |
| `llm-nemotron-3-5-ollama-ollama-2` |  · ollama nemotron-3.5-bolt:e4b / :e4b-q4_K (ollama) | 7.9 GB | 4.5 | 9 GB | T1,T2,T3,T4 | any | `ollama pull nemotron-3.5-bolt:e4b / :e4b-q4_K_M` |
| `llm-nemotron-3-5-gguf-ud-q8-k-xl` | NVIDIA-Nemotron-3.5-Bolt-E4B-GGUF · UD-Q8_K_XL (GGUF) | 8.2 GB | 8.5 | 9 GB | T1,T2,T3,T4,T5 | any | `hf download unsloth/NVIDIA-Nemotron-3.5-Bolt-E4B-GGUF --include "*UD-Q8_K_XL*"` |
| `llm-nemotron-3-5-gguf-bf16` | NVIDIA-Nemotron-3.5-Bolt-E4B-GGUF · BF16 (GGUF) | 15.1 GB | 16 | 17 GB | T1,T2,T3,T4,T5 | any | `hf download unsloth/NVIDIA-Nemotron-3.5-Bolt-E4B-GGUF --include "*BF16*"` |
| `llm-nemotron-3-5-mlx-4bit` | NVIDIA-Nemotron-3.5-Lightning-30B-A3B-4bit · 4bit (8bit 33.58 GB) (MLX) | 17.8 GB | 4.5 | 20 GB | T1,T2,T3,T4 | mac | `hf download mlx-community/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-4bit` |
| `llm-nemotron-3-5-gguf-iq2-xxs` | NVIDIA-Nemotron-3.5-Lightning-30B-A3B-GGUF · IQ2_XXS (GGUF) | 18.8 GB | 2.6 | 22 GB | T1,T2,T3,T4 | any | `hf download bartowski/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-GGUF --include "*IQ2_XXS*"` |
| `llm-nemotron-3-5-gguf-q4-0` | NVIDIA-Nemotron-3.5-Lightning-30B-A3B-GGUF · Q4_0 (GGUF) | 18.9 GB | 4.5 | 22 GB | T1,T2,T3,T4 | any | `hf download ggml-org/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-GGUF --include "*Q4_0*"` |
| `llm-nemotron-3-5-ollama-ollama-3` |  · ollama nemotron-3.5-lightning:30b-a3b-nv (ollama) | 19.1 GB | 4.5 | 22 GB | T1,T2,T3,T4 | any | `ollama pull nemotron-3.5-lightning:30b-a3b-nvfp4 / :30b-mlx` |
| `llm-nemotron-3-5-gguf-ud-iq2-xxs` | NVIDIA-Nemotron-3.5-Lightning-30B-A3B-GGUF · UD-IQ2_XXS (GGUF) | 19.4 GB | 2.6 | 22 GB | T1,T2,T3,T4 | any | `hf download unsloth/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-GGUF --include "*UD-IQ2_XXS*"` |
| `llm-nemotron-3-5-gguf-ud-q3-k-xl-2` | NVIDIA-Nemotron-3.5-Lightning-30B-A3B-GGUF · UD-Q3_K_XL (GGUF) | 21.2 GB | 3.5 | 24 GB | T1,T2,T3,T4 | any | `hf download unsloth/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-GGUF --include "*UD-Q3_K_XL*"` |
| `llm-nemotron-3-5-nvfp4-nvfp4` | NVIDIA-Nemotron-3.5-Lightning-30B-A3B-NVFP4 · NVFP4 (NVFP4) | 21.6 GB | 4.5 | 25 GB | T1,T2,T3 | server | `hf download nvidia/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-NVFP4` |
| `llm-nemotron-3-5-gguf-mxfp4-moe` | NVIDIA-Nemotron-3.5-Lightning-30B-A3B-GGUF · MXFP4_MOE (GGUF) | 23.2 GB | 4.5 | 27 GB | T1,T2,T3,T4 | any | `hf download unsloth/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-GGUF --include "*MXFP4_MOE*"` |
| `llm-nemotron-3-5-ollama-ollama-4` |  · ollama nemotron-3.5-bolt:74b-a9b / :late (ollama) | 24.8 GB | 2.6 | 28 GB | T1,T2,T3,T4 | any | `ollama pull nemotron-3.5-bolt:74b-a9b / :latest (iq2)` |
| `llm-nemotron-3-5-ollama-ollama-5` |  · ollama nemotron-3.5-lightning:30b / :30b (ollama) | 25.4 GB | 4.5 | 29 GB | T1,T2,T3,T4 | any | `ollama pull nemotron-3.5-lightning:30b / :30b-a3b-q4_K_M` |
| `llm-nemotron-3-5-gguf-q4-k-m` | NVIDIA-Nemotron-3.5-Lightning-30B-A3B-GGUF · Q4_K_M (GGUF) | 25.5 GB | 4.5 | 29 GB | T1,T2,T3,T4 | any | `hf download bartowski/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-GGUF --include "*Q4_K_M*"` |
| `llm-nemotron-3-5-gguf-ud-q4-k-xl-2` | NVIDIA-Nemotron-3.5-Lightning-30B-A3B-GGUF · UD-Q4_K_XL (GGUF) | 25.5 GB | 4.5 | 29 GB | T1,T2,T3,T4 | any | `hf download unsloth/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-GGUF --include "*UD-Q4_K_XL*"` |
| `llm-nemotron-3-5-fp8-fp8` | NVIDIA-Nemotron-3.5-Lightning-30B-A3B-FP8 · FP8 (FP8) | 32.3 GB | 8.5 | 37 GB | T1,T2,T3 | server | `hf download RedHatAI/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-FP8` |
| `llm-nemotron-3-5-gguf-q8-0` | NVIDIA-Nemotron-3.5-Lightning-30B-A3B-GGUF · Q8_0 (GGUF) | 33.6 GB | 8.5 | 39 GB | T1,T2,T3,T4 | any | `hf download ggml-org/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-GGUF --include "*Q8_0*"` |
| `llm-nemotron-3-5-gguf-ud-q6-k-xl-2` | NVIDIA-Nemotron-3.5-Lightning-30B-A3B-GGUF · UD-Q6_K_XL (GGUF) | 35.0 GB | 6.5 | 40 GB | T1,T2,T3,T4 | any | `hf download unsloth/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-GGUF --include "*UD-Q6_K_XL*"` |
| `llm-nemotron-3-5-gguf-q8-0-2` | NVIDIA-Nemotron-3.5-Lightning-30B-A3B-GGUF · Q8_0 (GGUF) | 35.0 GB | 8.5 | 40 GB | T1,T2,T3,T4 | any | `hf download bartowski/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-GGUF --include "*Q8_0*"` |
| `llm-nemotron-3-5-ollama-ollama-6` |  · ollama nemotron-3.5-lightning:30b-a3b-q8 (ollama) | 35.0 GB | 8.5 | 40 GB | T1,T2,T3,T4 | any | `ollama pull nemotron-3.5-lightning:30b-a3b-q8_0` |
| `llm-nemotron-3-5-gguf-ud-iq1-m` | NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-GGUF · UD-IQ1_M (GGUF) | 46.1 GB | 1.7 | 53 GB | T1,T2,T3,T4 | any | `hf download unsloth/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-GGUF --include "*UD-IQ1_M*"` |
| `llm-nemotron-3-5-gguf-ud-iq2-xxs-2` | NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-GGUF · UD-IQ2_XXS (GGUF) | 51.1 GB | 2.6 | 59 GB | T1,T2,T3,T4 | any | `hf download unsloth/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-GGUF --include "*UD-IQ2_XXS*"` |
| `llm-nemotron-3-5-gguf-ud-q2-k-xl` | NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-GGUF · UD-Q2_K_XL (GGUF) | 57.8 GB | 2.6 | 66 GB | T1,T2,T3,T4 | any | `hf download unsloth/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-GGUF --include "*UD-Q2_K_XL*"` |
| `llm-nemotron-3-5-gguf-bf16-2` | NVIDIA-Nemotron-3.5-Lightning-30B-A3B-GGUF · BF16 (GGUF) | 63.2 GB | 16 | 73 GB | T1,T2,T3,T4 | any | `hf download ggml-org/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-GGUF --include "*BF16*"` |
| `llm-nemotron-3-5-gguf-ud-q3-k-xl-3` | NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-GGUF · UD-Q3_K_XL (GGUF) | 65.8 GB | 3.5 | 76 GB | T1,T2,T3,T4 | any | `hf download unsloth/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-GGUF --include "*UD-Q3_K_XL*"` |
| `llm-nemotron-3-5-gguf-bf16-3` | NVIDIA-Nemotron-3.5-Lightning-30B-A3B-GGUF · BF16 (GGUF) | 65.8 GB | 16 | 76 GB | T1,T2,T3,T4 | any | `hf download unsloth/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-GGUF --include "*BF16*"` |
| `llm-nemotron-3-5-gguf-q4-0-2` | NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-GGUF · Q4_0 (GGUF) | 72.1 GB | 4.5 | 83 GB | T1,T2,T3,T4 | any | `hf download ggml-org/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-GGUF --include "*Q4_0*"` |
| `llm-nemotron-3-5-nvfp4-nvfp4-2` | NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-NVFP4 · NVFP4 (NVFP4) | 75.1 GB | 4.5 | 86 GB | T1,T2,T3,T4 | server | `hf download nvidia/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-NVFP4` |
| `llm-nemotron-3-5-gguf-nvfp4` | NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-GGUF · NVFP4 (GGUF) | 78.3 GB | 4.5 | 90 GB | T1,T2,T3,T4 | any | `hf download ggml-org/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-GGUF --include "*NVFP4*"` |
| `llm-nemotron-3-5-ollama-ollama-7` |  · ollama nemotron-3.5-super:120b-a12b-nvfp (ollama) | 79.6 GB | 4.5 | 91 GB | T1,T2,T3 | any | `ollama pull nemotron-3.5-super:120b-a12b-nvfp4` |
| `llm-nemotron-3-5-gguf-ud-q4-k-xl-3` | NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-GGUF · UD-Q4_K_XL (GGUF) | 86.9 GB | 4.5 | 100 GB | T1,T2,T3,T4 | any | `hf download unsloth/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-GGUF --include "*UD-Q4_K_XL*"` |
| `llm-nemotron-3-5-ollama-ollama-8` |  · ollama nemotron-3.5-super:120b / :120b-a (ollama) | 90.2 GB | 4.5 | 104 GB | T1,T2,T3 | any | `ollama pull nemotron-3.5-super:120b / :120b-a12b-q4_K_M` |
| `llm-nemotron-3-5-gguf-ud-q5-k-xl` | NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-GGUF · UD-Q5_K_XL (GGUF) | 110.7 GB | 5.5 | 127 GB | T1,T2,T3,T4 | any | `hf download unsloth/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-GGUF --include "*UD-Q5_K_XL*"` |
| `llm-nemotron-3-5-gguf-ud-q6-k-xl-3` | NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-GGUF · UD-Q6_K_XL (GGUF) | 121.0 GB | 6.5 | 139 GB | T1,T2,T3,T4 | any | `hf download unsloth/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-GGUF --include "*UD-Q6_K_XL*"` |
| `llm-nemotron-3-5-gguf-q8-0-3` | NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-GGUF · Q8_0 (GGUF) | 128.5 GB | 8.5 | 148 GB | T1,T2,T3,T4 | any | `hf download ggml-org/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-GGUF --include "*Q8_0*"` |
| `llm-nemotron-3-5-fp8-fp8-2` | NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-FP8 · FP8 (FP8) | 128.8 GB | 8.5 | 148 GB | T1,T2 | server | `hf download RedHatAI/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-FP8` |
| `llm-nemotron-3-5-gguf-q8-0-4` | NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-GGUF · Q8_0 (GGUF) | 131.6 GB | 8.5 | 151 GB | T1,T2,T3,T4 | any | `hf download unsloth/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-GGUF --include "*Q8_0*"` |
| `llm-nemotron-3-5-ollama-ollama-9` |  · ollama nemotron-3.5-super:120b-a12b-q8_0 (ollama) | 133.3 GB | 8.5 | 153 GB | T1,T2,T3 | any | `ollama pull nemotron-3.5-super:120b-a12b-q8_0` |
| `llm-nemotron-3-5-gguf-bf16-4` | NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-GGUF · BF16 (GGUF) | 241.5 GB | 16 | 278 GB | T1,T2,T3,T4 | any | `hf download ggml-org/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-GGUF --include "*BF16*"` |
</details>

<details><summary><b>Muse Glimmer 30B</b> – 33 változat</summary>

| id | Fájl / repó | Méret | Bit | Min. memória (≈×1,15) | HW | Platform | Letöltés |
|---|---|---|---|---|---|---|---|
| `llm-muse-glimmer-30b-gguf-iq1-s` | Muse-Glimmer-30B-i1-GGUF · IQ1_S (GGUF) | 6.5 GB | 1.7 | 8 GB | T1,T2,T3,T4 | any | `hf download mradermacher/Muse-Glimmer-30B-i1-GGUF --include "*IQ1_S*"` |
| `llm-muse-glimmer-30b-gguf-iq2-xxs` | Muse-Glimmer-30B-GGUF · IQ2_XXS (GGUF) | 8.9 GB | 2.6 | 10 GB | T1,T2,T3,T4 | any | `hf download bartowski/Muse-Glimmer-30B-GGUF --include "*IQ2_XXS*"` |
| `llm-muse-glimmer-30b-gguf-ud-iq2-xxs` | Muse-Glimmer-30B-GGUF · UD-IQ2_XXS (GGUF) | 10.8 GB | 2.6 | 12 GB | T1,T2,T3,T4 | any | `hf download unsloth/Muse-Glimmer-30B-GGUF --include "*UD-IQ2_XXS*"` |
| `llm-muse-glimmer-30b-gguf-ud-q2-k-xl` | Muse-Glimmer-30B-GGUF · UD-Q2_K_XL (GGUF) | 12.4 GB | 2.6 | 14 GB | T1,T2,T3,T4 | any | `hf download unsloth/Muse-Glimmer-30B-GGUF --include "*UD-Q2_K_XL*"` |
| `llm-muse-glimmer-30b-gguf-iq3-m` | Muse-Glimmer-30B-GGUF · IQ3_M (GGUF) | 13.1 GB | 3.5 | 15 GB | T1,T2,T3,T4 | any | `hf download bartowski/Muse-Glimmer-30B-GGUF --include "*IQ3_M*"` |
| `llm-muse-glimmer-30b-gguf-ud-iq3-m` | Muse-Glimmer-30B-GGUF · UD-IQ3_M (GGUF) | 14.1 GB | 3.5 | 16 GB | T1,T2,T3,T4 | any | `hf download unsloth/Muse-Glimmer-30B-GGUF --include "*UD-IQ3_M*"` |
| `llm-muse-glimmer-30b-gguf-iq4-xs` | Muse-Glimmer-30B-GGUF · IQ4_XS (GGUF) | 15.4 GB | 4.5 | 18 GB | T1,T2,T3,T4 | any | `hf download bartowski/Muse-Glimmer-30B-GGUF --include "*IQ4_XS*"` |
| `llm-muse-glimmer-30b-gguf-ud-q4-k-xl` | Muse-Glimmer-30B-GGUF · UD-Q4_K_XL (GGUF) | 15.9 GB | 4.5 | 18 GB | T1,T2,T3,T4 | any | `hf download unsloth/Muse-Glimmer-30B-GGUF --include "*UD-Q4_K_XL*"` |
| `llm-muse-glimmer-30b-gguf-official-q4-k-m` | Muse-Glimmer-30B-GGUF · Q4_K_M (GGUF(official)) | 16.8 GB | 4.5 | 19 GB | T1,T2,T3,T4 | any | `hf download meta-models/Muse-Glimmer-30B-GGUF --include "*Q4_K_M*"` |
| `llm-muse-glimmer-30b-gguf-q4-k-m` | Muse-Glimmer-30B-GGUF · Q4_K_M (GGUF) | 16.8 GB | 4.5 | 19 GB | T1,T2,T3,T4 | any | `hf download lmstudio-community/Muse-Glimmer-30B-GGUF --include "*Q4_K_M*"` |
| `llm-muse-glimmer-30b-gguf-q4-k-m-2` | Muse-Glimmer-30B-i1-GGUF · Q4_K_M (GGUF) | 16.9 GB | 4.5 | 19 GB | T1,T2,T3,T4 | any | `hf download mradermacher/Muse-Glimmer-30B-i1-GGUF --include "*Q4_K_M*"` |
| `llm-muse-glimmer-30b-ollama-ollama` |  · ollama muse-glimmer:30b-nvfp4 (ollama) | 17.3 GB | 4.5 | 20 GB | T1,T2,T3,T4 | any | `ollama pull muse-glimmer:30b-nvfp4` |
| `llm-muse-glimmer-30b-gguf-q4-k-m-3` | Muse-Glimmer-30B-GGUF · Q4_K_M (GGUF) | 17.3 GB | 4.5 | 20 GB | T1,T2,T3,T4 | any | `hf download bartowski/Muse-Glimmer-30B-GGUF --include "*Q4_K_M*"` |
| `llm-muse-glimmer-30b-ollama-ollama-2` |  · ollama muse-glimmer:30b / :latest / :30b (ollama) | 18.2 GB | 4.5 | 21 GB | T1,T2,T3,T4 | any | `ollama pull muse-glimmer:30b / :latest / :30b-q4_K_M` |
| `llm-muse-glimmer-30b-ollama-ollama-3` |  · ollama muse-glimmer:30b-mlx (ollama) | 19.1 GB | 4.5 | 22 GB | T1,T2,T3,T4 | any | `ollama pull muse-glimmer:30b-mlx` |
| `llm-muse-glimmer-30b-mlx-4bit` | Muse-Glimmer-30B-4bit · 4bit (MLX) | 19.4 GB | 4.5 | 22 GB | T1,T2,T3,T4 | mac | `hf download mlx-community/Muse-Glimmer-30B-4bit` |
| `llm-muse-glimmer-30b-gguf-official-q4-k-xl` | Muse-Glimmer-30B-GGUF · Q4_K_XL (+mmproj 1.4, DFlash 1.63) (GGUF(official)) | 19.6 GB | 4.5 | 23 GB | T1,T2,T3,T4 | any | `hf download meta-models/Muse-Glimmer-30B-GGUF --include "*Q4_K_XL*"` |
| `llm-muse-glimmer-30b-gguf-q5-k-m` | Muse-Glimmer-30B-GGUF · Q5_K_M (GGUF) | 20.1 GB | 5.5 | 23 GB | T1,T2,T3,T4 | any | `hf download bartowski/Muse-Glimmer-30B-GGUF --include "*Q5_K_M*"` |
| `llm-muse-glimmer-30b-gguf-ud-q5-k-xl` | Muse-Glimmer-30B-GGUF · UD-Q5_K_XL (GGUF) | 21.8 GB | 5.5 | 25 GB | T1,T2,T3,T4 | any | `hf download unsloth/Muse-Glimmer-30B-GGUF --include "*UD-Q5_K_XL*"` |
| `llm-muse-glimmer-30b-int4-w4a16` | Muse-Glimmer-30B-INT4 · W4A16 (INT4) | 22.2 GB | 4.5 | 26 GB | T1,T2,T3 | server | `hf download RedHatAI/Muse-Glimmer-30B-INT4` |
| `llm-muse-glimmer-30b-gguf-q6-k` | Muse-Glimmer-30B-i1-GGUF · Q6_K (GGUF) | 22.9 GB | 6.5 | 26 GB | T1,T2,T3,T4 | any | `hf download mradermacher/Muse-Glimmer-30B-i1-GGUF --include "*Q6_K*"` |
| `llm-muse-glimmer-30b-gguf-q6-k-2` | Muse-Glimmer-30B-GGUF · Q6_K (GGUF) | 23.4 GB | 6.5 | 27 GB | T1,T2,T3,T4 | any | `hf download bartowski/Muse-Glimmer-30B-GGUF --include "*Q6_K*"` |
| `llm-muse-glimmer-30b-awq-awq-int4` | Muse-Glimmer-30B-AWQ-INT4 · AWQ-INT4 (AWQ) | 24.0 GB | 4.5 | 28 GB | T1,T2,T3 | server | `hf download cyankiwi/Muse-Glimmer-30B-AWQ-INT4` |
| `llm-muse-glimmer-30b-nvfp4-nvfp4` | Muse-Glimmer-30B-NVFP4 · NVFP4 (NVFP4) | 24.7 GB | 4.5 | 28 GB | T1,T2,T3 | server | `hf download nvidia/Muse-Glimmer-30B-NVFP4` |
| `llm-muse-glimmer-30b-gguf-ud-q6-k-xl` | Muse-Glimmer-30B-GGUF · UD-Q6_K_XL (GGUF) | 26.3 GB | 6.5 | 30 GB | T1,T2,T3,T4 | any | `hf download unsloth/Muse-Glimmer-30B-GGUF --include "*UD-Q6_K_XL*"` |
| `llm-muse-glimmer-30b-mlx-6bit` | Muse-Glimmer-30B-6bit · 6bit (MLX) | 26.4 GB | 6.5 | 30 GB | T1,T2,T3,T4 | mac | `hf download mlx-community/Muse-Glimmer-30B-6bit` |
| `llm-muse-glimmer-30b-gguf-q8-0` | Muse-Glimmer-30B-GGUF · Q8_0 (GGUF) | 29.6 GB | 8.5 | 34 GB | T1,T2,T3,T4 | any | `hf download unsloth/Muse-Glimmer-30B-GGUF --include "*Q8_0*"` |
| `llm-muse-glimmer-30b-gguf-q8-0-2` | Muse-Glimmer-30B-GGUF · Q8_0 (GGUF) | 29.6 GB | 8.5 | 34 GB | T1,T2,T3,T4 | any | `hf download bartowski/Muse-Glimmer-30B-GGUF --include "*Q8_0*"` |
| `llm-muse-glimmer-30b-ollama-ollama-4` |  · ollama muse-glimmer:30b-q8_0 (ollama) | 31.0 GB | 8.5 | 36 GB | T1,T2,T3,T4 | any | `ollama pull muse-glimmer:30b-q8_0` |
| `llm-muse-glimmer-30b-mlx-8bit` | Muse-Glimmer-30B-8bit · 8bit (MLX) | 33.4 GB | 8.5 | 38 GB | T1,T2,T3,T4 | mac | `hf download mlx-community/Muse-Glimmer-30B-8bit` |
| `llm-muse-glimmer-30b-fp8-fp8` | Muse-Glimmer-30B-FP8-block · FP8 (FP8) | 34.4 GB | 8.5 | 40 GB | T1,T2,T3 | server | `hf download RedHatAI/Muse-Glimmer-30B-FP8-block` |
| `llm-muse-glimmer-30b-gguf-bf16` | Muse-Glimmer-30B-GGUF · BF16 (GGUF) | 55.7 GB | 16 | 64 GB | T1,T2,T3,T4 | any | `hf download unsloth/Muse-Glimmer-30B-GGUF --include "*BF16*"` |
| `llm-muse-glimmer-30b-ollama-ollama-5` |  · ollama muse-glimmer:30b-bf16 (ollama) | 57.1 GB | 16 | 66 GB | T1,T2,T3,T4 | any | `ollama pull muse-glimmer:30b-bf16` |
</details>

<details><summary><b>Gemma 4 (31B, 26B-A4B, 12B, E4B, E2B)</b> – 100 változat</summary>

| id | Fájl / repó | Méret | Bit | Min. memória (≈×1,15) | HW | Platform | Letöltés |
|---|---|---|---|---|---|---|---|
| `llm-gemma-4-gguf-ud-iq2-m` | gemma-4-E2B-it-GGUF · UD-IQ2_M (GGUF) | 2.3 GB | 2.6 | 3 GB | T1,T2,T3,T4,T5 | any | `hf download unsloth/gemma-4-E2B-it-GGUF --include "*UD-IQ2_M*"` |
| `llm-gemma-4-gguf-q4-k-m` | gemma-4-E2B-it-GGUF · Q4_K_M (GGUF) | 3.1 GB | 4.5 | 4 GB | T1,T2,T3,T4,T5 | any | `hf download unsloth/gemma-4-E2B-it-GGUF --include "*Q4_K_M*"` |
| `llm-gemma-4-gguf-ud-q4-k-xl` | gemma-4-E2B-it-GGUF · UD-Q4_K_XL (GGUF) | 3.2 GB | 4.5 | 4 GB | T1,T2,T3,T4,T5 | any | `hf download unsloth/gemma-4-E2B-it-GGUF --include "*UD-Q4_K_XL*"` |
| `llm-gemma-4-gguf-qat-official-q4-0` | gemma-4-E2B-it-qat-q4_0-gguf · q4_0 QAT (+mmproj 0.99) (GGUF(QAT official)) | 3.4 GB | 4.5 | 4 GB | T1,T2,T3,T4,T5 | any | `hf download google/gemma-4-E2B-it-qat-q4_0-gguf --include "*q4_0*"` |
| `llm-gemma-4-gguf-q4-k-m-2` | gemma-4-E2B-it-GGUF · Q4_K_M (GGUF) | 3.4 GB | 4.5 | 4 GB | T1,T2,T3,T4,T5 | any | `hf download lmstudio-community/gemma-4-E2B-it-GGUF --include "*Q4_K_M*"` |
| `llm-gemma-4-gguf-ud-iq2-m-2` | gemma-4-E4B-it-GGUF · UD-IQ2_M (GGUF) | 3.5 GB | 2.6 | 4 GB | T1,T2,T3,T4,T5 | any | `hf download unsloth/gemma-4-E4B-it-GGUF --include "*UD-IQ2_M*"` |
| `llm-gemma-4-gguf-q6-k` | gemma-4-E2B-it-GGUF · Q6_K (GGUF) | 3.9 GB | 6.5 | 4 GB | T1,T2,T3,T4,T5 | any | `hf download lmstudio-community/gemma-4-E2B-it-GGUF --include "*Q6_K*"` |
| `llm-gemma-4-gguf-iq2-m` | google_gemma-4-E4B-it-GGUF · IQ2_M (GGUF) | 4.0 GB | 2.6 | 5 GB | T1,T2,T3,T4,T5 | any | `hf download bartowski/google_gemma-4-E4B-it-GGUF --include "*IQ2_M*"` |
| `llm-gemma-4-gguf-ud-iq2-m-3` | gemma-4-12b-it-GGUF · UD-IQ2_M (GGUF) | 4.2 GB | 2.6 | 5 GB | T1,T2,T3,T4 | any | `hf download unsloth/gemma-4-12b-it-GGUF --include "*UD-IQ2_M*"` |
| `llm-gemma-4-ollama-ollama` |  · ollama gemma4:e2b-it-qat (ollama) | 4.3 GB | 4.5 | 5 GB | T1,T2,T3,T4 | any | `ollama pull gemma4:e2b-it-qat` |
| `llm-gemma-4-gguf-ud-q3-k-xl` | gemma-4-E4B-it-GGUF · UD-Q3_K_XL (GGUF) | 4.6 GB | 3.5 | 5 GB | T1,T2,T3,T4,T5 | any | `hf download unsloth/gemma-4-E4B-it-GGUF --include "*UD-Q3_K_XL*"` |
| `llm-gemma-4-ollama-ollama-2` |  · ollama gemma4:e2b / :e2b-it-q4_K_M (ollama) | 4.6 GB | 4.5 | 5 GB | T1,T2,T3,T4 | any | `ollama pull gemma4:e2b / :e2b-it-q4_K_M` |
| `llm-gemma-4-gguf-iq2-s` | gemma-4-12B-it-GGUF · IQ2_S (GGUF) | 4.7 GB | 2.6 | 5 GB | T1,T2,T3,T4 | any | `hf download bartowski/gemma-4-12B-it-GGUF --include "*IQ2_S*"` |
| `llm-gemma-4-gguf-q8-0` | gemma-4-E2B-it-GGUF · Q8_0 (GGUF) | 5.0 GB | 8.5 | 6 GB | T1,T2,T3,T4,T5 | any | `hf download lmstudio-community/gemma-4-E2B-it-GGUF --include "*Q8_0*"` |
| `llm-gemma-4-gguf-q4-k-m-3` | gemma-4-E4B-it-GGUF · Q4_K_M (GGUF) | 5.0 GB | 4.5 | 6 GB | T1,T2,T3,T4,T5 | any | `hf download unsloth/gemma-4-E4B-it-GGUF --include "*Q4_K_M*"` |
| `llm-gemma-4-gguf-q8-0-2` | gemma-4-E2B-it-GGUF · Q8_0 (GGUF) | 5.0 GB | 8.5 | 6 GB | T1,T2,T3,T4,T5 | any | `hf download unsloth/gemma-4-E2B-it-GGUF --include "*Q8_0*"` |
| `llm-gemma-4-gguf-ud-q4-k-xl-2` | gemma-4-E4B-it-GGUF · UD-Q4_K_XL (GGUF) | 5.1 GB | 4.5 | 6 GB | T1,T2,T3,T4,T5 | any | `hf download unsloth/gemma-4-E4B-it-GGUF --include "*UD-Q4_K_XL*"` |
| `llm-gemma-4-gguf-qat-official-q4-0-2` | gemma-4-E4B-it-qat-q4_0-gguf · q4_0 QAT (+mmproj 0.99) (GGUF(QAT official)) | 5.2 GB | 4.5 | 6 GB | T1,T2,T3,T4,T5 | any | `hf download google/gemma-4-E4B-it-qat-q4_0-gguf --include "*q4_0*"` |
| `llm-gemma-4-gguf-q4-k-m-4` | gemma-4-E4B-it-GGUF · Q4_K_M (GGUF) | 5.3 GB | 4.5 | 6 GB | T1,T2,T3,T4,T5 | any | `hf download lmstudio-community/gemma-4-E4B-it-GGUF --include "*Q4_K_M*"` |
| `llm-gemma-4-gguf-q4-k-m-5` | google_gemma-4-E4B-it-GGUF · Q4_K_M (GGUF) | 5.4 GB | 4.5 | 6 GB | T1,T2,T3,T4,T5 | any | `hf download bartowski/google_gemma-4-E4B-it-GGUF --include "*Q4_K_M*"` |
| `llm-gemma-4-ollama-ollama-3` |  · ollama gemma4:e2b-it-q8_0 (ollama) | 6.0 GB | 8.5 | 7 GB | T1,T2,T3,T4 | any | `ollama pull gemma4:e2b-it-q8_0` |
| `llm-gemma-4-gguf-ud-q3-k-xl-2` | gemma-4-12b-it-GGUF · UD-Q3_K_XL (GGUF) | 6.0 GB | 3.5 | 7 GB | T1,T2,T3,T4 | any | `hf download unsloth/gemma-4-12b-it-GGUF --include "*UD-Q3_K_XL*"` |
| `llm-gemma-4-ollama-ollama-4` |  · ollama gemma4:e4b-it-qat (ollama) | 6.2 GB | 4.5 | 7 GB | T1,T2,T3,T4 | any | `ollama pull gemma4:e4b-it-qat` |
| `llm-gemma-4-gguf-q6-k-2` | gemma-4-E4B-it-GGUF · Q6_K (GGUF) | 6.2 GB | 6.5 | 7 GB | T1,T2,T3,T4,T5 | any | `hf download lmstudio-community/gemma-4-E4B-it-GGUF --include "*Q6_K*"` |
| `llm-gemma-4-ollama-ollama-5` |  · ollama gemma4:e4b / :latest / :e4b-it-q4 (ollama) | 6.6 GB | 4.5 | 8 GB | T1,T2,T3,T4 | any | `ollama pull gemma4:e4b / :latest / :e4b-it-q4_K_M` |
| `llm-gemma-4-mlx-4bit` | gemma-4-12B-it-MLX-4bit · 4bit (8bit 12.75 GB) (MLX) | 6.8 GB | 4.5 | 8 GB | T1,T2,T3,T4 | mac | `hf download lmstudio-community/gemma-4-12B-it-MLX-4bit` |
| `llm-gemma-4-mlx-4bit-2` | gemma-4-E4B-it-MLX-4bit · 4bit (MLX) | 6.9 GB | 4.5 | 8 GB | T1,T2,T3,T4,T5 | mac | `hf download lmstudio-community/gemma-4-E4B-it-MLX-4bit` |
| `llm-gemma-4-gguf-qat-official-q4-0-3` | gemma-4-12B-it-qat-q4_0-gguf · q4_0 QAT (+mmproj 0.18) (GGUF(QAT official)) | 7.0 GB | 4.5 | 8 GB | T1,T2,T3,T4,T5 | any | `hf download google/gemma-4-12B-it-qat-q4_0-gguf --include "*q4_0*"` |
| `llm-gemma-4-gguf-q6-k-3` | gemma-4-E4B-it-GGUF · Q6_K (GGUF) | 7.1 GB | 6.5 | 8 GB | T1,T2,T3,T4,T5 | any | `hf download unsloth/gemma-4-E4B-it-GGUF --include "*Q6_K*"` |
| `llm-gemma-4-gguf-q4-k-m-6` | gemma-4-12b-it-GGUF · Q4_K_M (GGUF) | 7.1 GB | 4.5 | 8 GB | T1,T2,T3,T4 | any | `hf download unsloth/gemma-4-12b-it-GGUF --include "*Q4_K_M*"` |
| `llm-gemma-4-ollama-ollama-6` |  · ollama gemma4:12b-it-qat (ollama) | 7.2 GB | 4.5 | 8 GB | T1,T2,T3,T4 | any | `ollama pull gemma4:12b-it-qat` |
| `llm-gemma-4-gguf-ud-q4-k-xl-3` | gemma-4-12b-it-GGUF · UD-Q4_K_XL (GGUF) | 7.4 GB | 4.5 | 8 GB | T1,T2,T3,T4 | any | `hf download unsloth/gemma-4-12b-it-GGUF --include "*UD-Q4_K_XL*"` |
| `llm-gemma-4-gguf-q4-k-m-7` | gemma-4-12B-it-GGUF · Q4_K_M (GGUF) | 7.4 GB | 4.5 | 8 GB | T1,T2,T3,T4 | any | `hf download lmstudio-community/gemma-4-12B-it-GGUF --include "*Q4_K_M*"` |
| `llm-gemma-4-gguf-q4-k-m-8` | gemma-4-12B-it-GGUF · Q4_K_M (GGUF) | 7.7 GB | 4.5 | 9 GB | T1,T2,T3,T4 | any | `hf download bartowski/gemma-4-12B-it-GGUF --include "*Q4_K_M*"` |
| `llm-gemma-4-ollama-ollama-7` |  · ollama gemma4:12b / :12b-it-q4_K_M (ollama) | 8.0 GB | 4.5 | 9 GB | T1,T2,T3,T4 | any | `ollama pull gemma4:12b / :12b-it-q4_K_M` |
| `llm-gemma-4-gguf-q8-0-3` | google_gemma-4-E4B-it-GGUF · Q8_0 (GGUF) | 8.0 GB | 8.5 | 9 GB | T1,T2,T3,T4,T5 | any | `hf download bartowski/google_gemma-4-E4B-it-GGUF --include "*Q8_0*"` |
| `llm-gemma-4-gguf-q8-0-4` | gemma-4-E4B-it-GGUF · Q8_0 (GGUF) | 8.0 GB | 8.5 | 9 GB | T1,T2,T3,T4,T5 | any | `hf download lmstudio-community/gemma-4-E4B-it-GGUF --include "*Q8_0*"` |
| `llm-gemma-4-gguf-q8-0-5` | gemma-4-E4B-it-GGUF · Q8_0 (GGUF) | 8.2 GB | 8.5 | 9 GB | T1,T2,T3,T4,T5 | any | `hf download unsloth/gemma-4-E4B-it-GGUF --include "*Q8_0*"` |
| `llm-gemma-4-gguf-ud-iq2-xxs` | gemma-4-31B-it-GGUF · UD-IQ2_XXS (GGUF) | 8.5 GB | 2.6 | 10 GB | T1,T2,T3,T4 | any | `hf download unsloth/gemma-4-31B-it-GGUF --include "*UD-IQ2_XXS*"` |
| `llm-gemma-4-ollama-ollama-8` |  · ollama gemma4:e4b-it-q8_0 (ollama) | 9.0 GB | 8.5 | 10 GB | T1,T2,T3,T4 | any | `ollama pull gemma4:e4b-it-q8_0` |
| `llm-gemma-4-gguf-bf16` | gemma-4-E2B-it-GGUF · BF16 (GGUF) | 9.3 GB | 16 | 11 GB | T1,T2,T3,T4,T5 | any | `hf download unsloth/gemma-4-E2B-it-GGUF --include "*BF16*"` |
| `llm-gemma-4-gguf-iq2-xxs` | google_gemma-4-26B-A4B-it-GGUF · IQ2_XXS (GGUF) | 9.7 GB | 2.6 | 11 GB | T1,T2,T3,T4 | any | `hf download bartowski/google_gemma-4-26B-A4B-it-GGUF --include "*IQ2_XXS*"` |
| `llm-gemma-4-gguf-q6-k-4` | gemma-4-12B-it-GGUF · Q6_K (GGUF) | 9.8 GB | 6.5 | 11 GB | T1,T2,T3,T4 | any | `hf download lmstudio-community/gemma-4-12B-it-GGUF --include "*Q6_K*"` |
| `llm-gemma-4-gguf-ud-iq2-xxs-2` | gemma-4-26B-A4B-it-GGUF · UD-IQ2_XXS (GGUF) | 9.9 GB | 2.6 | 11 GB | T1,T2,T3,T4 | any | `hf download unsloth/gemma-4-26B-A4B-it-GGUF --include "*UD-IQ2_XXS*"` |
| `llm-gemma-4-gguf-iq1-m` | google_gemma-4-31B-it-GGUF · IQ1_M (GGUF) | 10.1 GB | 1.7 | 12 GB | T1,T2,T3,T4 | any | `hf download bartowski/google_gemma-4-31B-it-GGUF --include "*IQ1_M*"` |
| `llm-gemma-4-gguf-q6-k-5` | gemma-4-12B-it-GGUF · Q6_K (GGUF) | 10.2 GB | 6.5 | 12 GB | T1,T2,T3,T4 | any | `hf download bartowski/gemma-4-12B-it-GGUF --include "*Q6_K*"` |
| `llm-gemma-4-gguf-ud-q6-k-xl` | gemma-4-12b-it-GGUF · UD-Q6_K_XL (GGUF) | 10.7 GB | 6.5 | 12 GB | T1,T2,T3,T4 | any | `hf download unsloth/gemma-4-12b-it-GGUF --include "*UD-Q6_K_XL*"` |
| `llm-gemma-4-gguf-ud-q2-k-xl` | gemma-4-31B-it-GGUF · UD-Q2_K_XL (GGUF) | 11.8 GB | 2.6 | 14 GB | T1,T2,T3,T4 | any | `hf download unsloth/gemma-4-31B-it-GGUF --include "*UD-Q2_K_XL*"` |
| `llm-gemma-4-gguf-q8-0-6` | gemma-4-12b-it-GGUF · Q8_0 (GGUF) | 12.7 GB | 8.5 | 15 GB | T1,T2,T3,T4 | any | `hf download unsloth/gemma-4-12b-it-GGUF --include "*Q8_0*"` |
| `llm-gemma-4-gguf-q8-0-7` | gemma-4-12B-it-GGUF · Q8_0 (GGUF) | 12.7 GB | 8.5 | 15 GB | T1,T2,T3,T4 | any | `hf download bartowski/gemma-4-12B-it-GGUF --include "*Q8_0*"` |
| `llm-gemma-4-gguf-q8-0-8` | gemma-4-12B-it-GGUF · Q8_0 (GGUF) | 12.7 GB | 8.5 | 15 GB | T1,T2,T3,T4 | any | `hf download lmstudio-community/gemma-4-12B-it-GGUF --include "*Q8_0*"` |
| `llm-gemma-4-ollama-ollama-9` |  · ollama gemma4:12b-it-q8_0 (ollama) | 12.8 GB | 8.5 | 15 GB | T1,T2,T3,T4 | any | `ollama pull gemma4:12b-it-q8_0` |
| `llm-gemma-4-litert-lm-t-bb` | gemma-4-E4B-it-litert-lm · több .litertlm változat (LiteRT-LM) | 12.9 GB | 4.5 | 15 GB | T1,T2,T3,T4,T5 | android | `hf download litert-community/gemma-4-E4B-it-litert-lm` |
| `llm-gemma-4-gguf-ud-q3-k-xl-3` | gemma-4-26B-A4B-it-GGUF · UD-Q3_K_XL (GGUF) | 12.9 GB | 3.5 | 15 GB | T1,T2,T3,T4 | any | `hf download unsloth/gemma-4-26B-A4B-it-GGUF --include "*UD-Q3_K_XL*"` |
| `llm-gemma-4-gguf-ud-iq4-xs` | gemma-4-26B-A4B-it-GGUF · UD-IQ4_XS (GGUF) | 13.6 GB | 4.5 | 16 GB | T1,T2,T3,T4 | any | `hf download unsloth/gemma-4-26B-A4B-it-GGUF --include "*UD-IQ4_XS*"` |
| `llm-gemma-4-gguf-qat-official-q4-0-4` | gemma-4-26B-A4B-it-qat-q4_0-gguf · q4_0 QAT (GGUF(QAT official)) | 14.4 GB | 4.5 | 17 GB | T1,T2,T3,T4 | any | `hf download google/gemma-4-26B-A4B-it-qat-q4_0-gguf --include "*q4_0*"` |
| `llm-gemma-4-gguf-bf16-2` | gemma-4-E4B-it-GGUF · BF16 (GGUF) | 15.1 GB | 16 | 17 GB | T1,T2,T3,T4,T5 | any | `hf download unsloth/gemma-4-E4B-it-GGUF --include "*BF16*"` |
| `llm-gemma-4-gguf-ud-q3-k-xl-4` | gemma-4-31B-it-GGUF · UD-Q3_K_XL (GGUF) | 15.4 GB | 3.5 | 18 GB | T1,T2,T3,T4 | any | `hf download unsloth/gemma-4-31B-it-GGUF --include "*UD-Q3_K_XL*"` |
| `llm-gemma-4-ollama-ollama-10` |  · ollama gemma4:26b-a4b-it-qat (ollama) | 15.6 GB | 4.5 | 18 GB | T1,T2,T3,T4 | any | `ollama pull gemma4:26b-a4b-it-qat` |
| `llm-gemma-4-mlx-4bit-3` | gemma-4-26B-A4B-it-MLX-4bit · 4bit (8bit: 27.99 GB a -MLX-8bit repóban (MLX) | 15.6 GB | 4.5 | 18 GB | T1,T2,T3,T4 | mac | `hf download lmstudio-community/gemma-4-26B-A4B-it-MLX-4bit` |
| `llm-gemma-4-gguf-mxfp4-moe` | gemma-4-26B-A4B-it-GGUF · MXFP4_MOE (GGUF) | 16.6 GB | 4.5 | 19 GB | T1,T2,T3,T4 | any | `hf download unsloth/gemma-4-26B-A4B-it-GGUF --include "*MXFP4_MOE*"` |
| `llm-gemma-4-gguf-q4-k-m-9` | gemma-4-26B-A4B-it-GGUF · Q4_K_M (GGUF) | 16.8 GB | 4.5 | 19 GB | T1,T2,T3,T4 | any | `hf download lmstudio-community/gemma-4-26B-A4B-it-GGUF --include "*Q4_K_M*"` |
| `llm-gemma-4-gguf-ud-q4-k-xl-4` | gemma-4-26B-A4B-it-GGUF · UD-Q4_K_XL (GGUF) | 17.0 GB | 4.5 | 20 GB | T1,T2,T3,T4 | any | `hf download unsloth/gemma-4-26B-A4B-it-GGUF --include "*UD-Q4_K_XL*"` |
| `llm-gemma-4-gguf-q4-k-m-10` | google_gemma-4-26B-A4B-it-GGUF · Q4_K_M (GGUF) | 17.0 GB | 4.5 | 20 GB | T1,T2,T3,T4 | any | `hf download bartowski/google_gemma-4-26B-A4B-it-GGUF --include "*Q4_K_M*"` |
| `llm-gemma-4-awq-awq-4bit` | gemma-4-26B-A4B-it-AWQ-4bit · AWQ-4bit (AWQ) | 17.2 GB | 4.5 | 20 GB | T1,T2,T3 | server | `hf download cyankiwi/gemma-4-26B-A4B-it-AWQ-4bit` |
| `llm-gemma-4-gguf-qat-official-q4-0-5` | gemma-4-31B-it-qat-q4_0-gguf · q4_0 QAT (+mmproj 1.2) (GGUF(QAT official)) | 17.6 GB | 4.5 | 20 GB | T1,T2,T3,T4 | any | `hf download google/gemma-4-31B-it-qat-q4_0-gguf --include "*q4_0*"` |
| `llm-gemma-4-ollama-ollama-11` |  · ollama gemma4:26b-a4b-it-q4_K_M (ollama) | 18.0 GB | 4.5 | 21 GB | T1,T2,T3,T4 | any | `ollama pull gemma4:26b-a4b-it-q4_K_M` |
| `llm-gemma-4-gguf-q4-k-m-11` | gemma-4-31B-it-GGUF · Q4_K_M (GGUF) | 18.3 GB | 4.5 | 21 GB | T1,T2,T3,T4 | any | `hf download unsloth/gemma-4-31B-it-GGUF --include "*Q4_K_M*"` |
| `llm-gemma-4-mlx-4bit-4` | gemma-4-31B-it-MLX-4bit · 4bit (6bit 26.12, 8bit 33.8 a -MLX-6bit/ (MLX) | 18.4 GB | 4.5 | 21 GB | T1,T2,T3,T4 | mac | `hf download lmstudio-community/gemma-4-31B-it-MLX-4bit` |
| `llm-gemma-4-gguf-q4-k-m-12` | gemma-4-31B-it-GGUF · Q4_K_M (GGUF) | 18.7 GB | 4.5 | 21 GB | T1,T2,T3,T4 | any | `hf download lmstudio-community/gemma-4-31B-it-GGUF --include "*Q4_K_M*"` |
| `llm-gemma-4-ollama-ollama-12` |  · ollama gemma4:26b / :26b-a4b / :26b-a4b- (ollama) | 18.7 GB | 4.5 | 22 GB | T1,T2,T3,T4 | any | `ollama pull gemma4:26b / :26b-a4b / :26b-a4b-it-mtp-q4_K_M` |
| `llm-gemma-4-gguf-ud-q4-k-xl-5` | gemma-4-31B-it-GGUF · UD-Q4_K_XL (GGUF) | 18.8 GB | 4.5 | 22 GB | T1,T2,T3,T4 | any | `hf download unsloth/gemma-4-31B-it-GGUF --include "*UD-Q4_K_XL*"` |
| `llm-gemma-4-nvfp4-nvfp4` | Gemma-4-26B-A4B-NVFP4 · NVFP4 (NVFP4) | 18.8 GB | 4.5 | 22 GB | T1,T2,T3 | server | `hf download nvidia/Gemma-4-26B-A4B-NVFP4` |
| `llm-gemma-4-ollama-ollama-13` |  · ollama gemma4:31b-it-qat (ollama) | 18.9 GB | 4.5 | 22 GB | T1,T2,T3,T4 | any | `ollama pull gemma4:31b-it-qat` |
| `llm-gemma-4-ollama-ollama-14` |  · ollama gemma4:31b-nvfp4 / :31b-mlx (ollama) | 19.4 GB | 4.5 | 22 GB | T1,T2,T3,T4 | any | `ollama pull gemma4:31b-nvfp4 / :31b-mlx` |
| `llm-gemma-4-gguf-q4-k-m-13` | google_gemma-4-31B-it-GGUF · Q4_K_M (GGUF) | 19.6 GB | 4.5 | 23 GB | T1,T2,T3,T4 | any | `hf download bartowski/google_gemma-4-31B-it-GGUF --include "*Q4_K_M*"` |
| `llm-gemma-4-ollama-ollama-15` |  · ollama gemma4:31b / :31b-it-q4_K_M (ollama) | 20.4 GB | 4.5 | 23 GB | T1,T2,T3,T4 | any | `ollama pull gemma4:31b / :31b-it-q4_K_M` |
| `llm-gemma-4-awq-awq` | gemma-4-31B-it-AWQ · AWQ (AWQ) | 20.5 GB | 4.5 | 24 GB | T1,T2,T3 | server | `hf download QuantTrio/gemma-4-31B-it-AWQ` |
| `llm-gemma-4-gguf-ud-q5-k-xl` | gemma-4-26B-A4B-it-GGUF · UD-Q5_K_XL (GGUF) | 21.2 GB | 5.5 | 24 GB | T1,T2,T3,T4 | any | `hf download unsloth/gemma-4-26B-A4B-it-GGUF --include "*UD-Q5_K_XL*"` |
| `llm-gemma-4-gguf-ud-q5-k-xl-2` | gemma-4-31B-it-GGUF · UD-Q5_K_XL (GGUF) | 21.9 GB | 5.5 | 25 GB | T1,T2,T3,T4 | any | `hf download unsloth/gemma-4-31B-it-GGUF --include "*UD-Q5_K_XL*"` |
| `llm-gemma-4-gguf-q6-k-6` | gemma-4-26B-A4B-it-GGUF · Q6_K (GGUF) | 22.6 GB | 6.5 | 26 GB | T1,T2,T3,T4 | any | `hf download lmstudio-community/gemma-4-26B-A4B-it-GGUF --include "*Q6_K*"` |
| `llm-gemma-4-gguf-ud-q6-k-xl-2` | gemma-4-26B-A4B-it-GGUF · UD-Q6_K_XL (GGUF) | 23.3 GB | 6.5 | 27 GB | T1,T2,T3,T4 | any | `hf download unsloth/gemma-4-26B-A4B-it-GGUF --include "*UD-Q6_K_XL*"` |
| `llm-gemma-4-gguf-bf16-3` | gemma-4-12b-it-GGUF · BF16 (GGUF) | 23.8 GB | 16 | 27 GB | T1,T2,T3,T4 | any | `hf download unsloth/gemma-4-12b-it-GGUF --include "*BF16*"` |
| `llm-gemma-4-gguf-q6-k-7` | gemma-4-31B-it-GGUF · Q6_K (GGUF) | 25.2 GB | 6.5 | 29 GB | T1,T2,T3,T4 | any | `hf download lmstudio-community/gemma-4-31B-it-GGUF --include "*Q6_K*"` |
| `llm-gemma-4-gguf-q6-k-8` | google_gemma-4-31B-it-GGUF · Q6_K (GGUF) | 26.7 GB | 6.5 | 31 GB | T1,T2,T3,T4 | any | `hf download bartowski/google_gemma-4-31B-it-GGUF --include "*Q6_K*"` |
| `llm-gemma-4-litert-lm-t-bb-2` | gemma-4-E2B-it-litert-lm · több .litertlm változat (LiteRT-LM) | 26.9 GB | 4.5 | 31 GB | T1,T2,T3,T4,T5 | android | `hf download litert-community/gemma-4-E2B-it-litert-lm` |
| `llm-gemma-4-gguf-q8-0-9` | gemma-4-26B-A4B-it-GGUF · Q8_0 (GGUF) | 26.9 GB | 8.5 | 31 GB | T1,T2,T3,T4 | any | `hf download unsloth/gemma-4-26B-A4B-it-GGUF --include "*Q8_0*"` |
| `llm-gemma-4-gguf-q8-0-10` | google_gemma-4-26B-A4B-it-GGUF · Q8_0 (GGUF) | 26.9 GB | 8.5 | 31 GB | T1,T2,T3,T4 | any | `hf download bartowski/google_gemma-4-26B-A4B-it-GGUF --include "*Q8_0*"` |
| `llm-gemma-4-gguf-q8-0-11` | gemma-4-26B-A4B-it-GGUF · Q8_0 (GGUF) | 26.9 GB | 8.5 | 31 GB | T1,T2,T3,T4 | any | `hf download lmstudio-community/gemma-4-26B-A4B-it-GGUF --include "*Q8_0*"` |
| `llm-gemma-4-gguf-ud-q6-k-xl-3` | gemma-4-31B-it-GGUF · UD-Q6_K_XL (GGUF) | 27.5 GB | 6.5 | 32 GB | T1,T2,T3,T4 | any | `hf download unsloth/gemma-4-31B-it-GGUF --include "*UD-Q6_K_XL*"` |
| `llm-gemma-4-ollama-ollama-16` |  · ollama gemma4:26b-a4b-it-q8_0 (ollama) | 28.1 GB | 8.5 | 32 GB | T1,T2,T3,T4 | any | `ollama pull gemma4:26b-a4b-it-q8_0` |
| `llm-gemma-4-fp8-fp8` | gemma-4-26B-A4B-it-FP8-dynamic · FP8 (FP8) | 28.7 GB | 8.5 | 33 GB | T1,T2,T3 | server | `hf download RedHatAI/gemma-4-26B-A4B-it-FP8-dynamic` |
| `llm-gemma-4-gguf-q8-0-12` | gemma-4-31B-it-GGUF · Q8_0 (GGUF) | 32.6 GB | 8.5 | 38 GB | T1,T2,T3,T4 | any | `hf download unsloth/gemma-4-31B-it-GGUF --include "*Q8_0*"` |
| `llm-gemma-4-gguf-q8-0-13` | google_gemma-4-31B-it-GGUF · Q8_0 (GGUF) | 32.6 GB | 8.5 | 38 GB | T1,T2,T3,T4 | any | `hf download bartowski/google_gemma-4-31B-it-GGUF --include "*Q8_0*"` |
| `llm-gemma-4-gguf-q8-0-14` | gemma-4-31B-it-GGUF · Q8_0 (GGUF) | 32.6 GB | 8.5 | 38 GB | T1,T2,T3,T4 | any | `hf download lmstudio-community/gemma-4-31B-it-GGUF --include "*Q8_0*"` |
| `llm-gemma-4-nvfp4-nvfp4-2` | Gemma-4-31B-IT-NVFP4 · NVFP4 (NVFP4) | 32.7 GB | 4.5 | 38 GB | T1,T2,T3 | server | `hf download nvidia/Gemma-4-31B-IT-NVFP4` |
| `llm-gemma-4-fp8-fp8-2` | gemma-4-31B-it-FP8-block · FP8 (FP8) | 33.3 GB | 8.5 | 38 GB | T1,T2,T3 | server | `hf download RedHatAI/gemma-4-31B-it-FP8-block` |
| `llm-gemma-4-ollama-ollama-17` |  · ollama gemma4:31b-it-q8_0 (ollama) | 33.8 GB | 8.5 | 39 GB | T1,T2,T3,T4 | any | `ollama pull gemma4:31b-it-q8_0` |
| `llm-gemma-4-gguf-bf16-4` | gemma-4-31B-it-GGUF · BF16 (GGUF) | 61.4 GB | 16 | 71 GB | T1,T2,T3,T4 | any | `hf download unsloth/gemma-4-31B-it-GGUF --include "*BF16*"` |
| `llm-gemma-4-ollama-ollama-18` |  · ollama gemma4:31b-it-bf16 (ollama) | 62.6 GB | 16 | 72 GB | T1,T2,T3 | any | `ollama pull gemma4:31b-it-bf16` |
</details>

<details><summary><b>Qwen3.5-4B / Qwen3.5-9B (+ MiMo-V2.6-Distill-Qwen-9B)</b> – 22 változat</summary>

| id | Fájl / repó | Méret | Bit | Min. memória (≈×1,15) | HW | Platform | Letöltés |
|---|---|---|---|---|---|---|---|
| `llm-qwen3-5-small-gguf-ud-iq2-m` | Qwen3.5-4B-GGUF · UD-IQ2_M (GGUF) | 1.8 GB | 2.6 | 2 GB | T1,T2,T3,T4,T5 | any | `hf download unsloth/Qwen3.5-4B-GGUF --include "*UD-IQ2_M*"` |
| `llm-qwen3-5-small-gguf-ud-q3-k-xl` | Qwen3.5-4B-GGUF · UD-Q3_K_XL (GGUF) | 2.4 GB | 3.5 | 3 GB | T1,T2,T3,T4,T5 | any | `hf download unsloth/Qwen3.5-4B-GGUF --include "*UD-Q3_K_XL*"` |
| `llm-qwen3-5-small-gguf-q4-k-m` | Qwen3.5-4B-GGUF · Q4_K_M (GGUF) | 2.7 GB | 4.5 | 3 GB | T1,T2,T3,T4,T5 | any | `hf download unsloth/Qwen3.5-4B-GGUF --include "*Q4_K_M*"` |
| `llm-qwen3-5-small-gguf-ud-q4-k-xl` | Qwen3.5-4B-GGUF · UD-Q4_K_XL (GGUF) | 2.9 GB | 4.5 | 3 GB | T1,T2,T3,T4,T5 | any | `hf download unsloth/Qwen3.5-4B-GGUF --include "*UD-Q4_K_XL*"` |
| `llm-qwen3-5-small-ollama-ollama` |  · ollama qwen3.5:4b (ollama) | 3.3 GB | 4.5 | 4 GB | T1,T2,T3,T4 | any | `ollama pull qwen3.5:4b` |
| `llm-qwen3-5-small-gguf-q6-k` | Qwen3.5-4B-GGUF · Q6_K (GGUF) | 3.5 GB | 6.5 | 4 GB | T1,T2,T3,T4,T5 | any | `hf download unsloth/Qwen3.5-4B-GGUF --include "*Q6_K*"` |
| `llm-qwen3-5-small-gguf-q8-0` | Qwen3.5-4B-GGUF · Q8_0 (GGUF) | 4.5 GB | 8.5 | 5 GB | T1,T2,T3,T4,T5 | any | `hf download unsloth/Qwen3.5-4B-GGUF --include "*Q8_0*"` |
| `llm-qwen3-5-small-gguf-iq3-m` | MiMo-V2.6-Distill-Qwen-9B-GGUF · IQ3_M (GGUF) | 4.8 GB | 3.5 | 6 GB | T1,T2,T3,T4,T5 | any | `hf download bartowski/MiMo-V2.6-Distill-Qwen-9B-GGUF --include "*IQ3_M*"` |
| `llm-qwen3-5-small-gguf-ud-q3-k-xl-2` | Qwen3.5-9B-GGUF · UD-Q3_K_XL (GGUF) | 5.0 GB | 3.5 | 6 GB | T1,T2,T3,T4,T5 | any | `hf download unsloth/Qwen3.5-9B-GGUF --include "*UD-Q3_K_XL*"` |
| `llm-qwen3-5-small-ollama-ollama-2` |  · ollama qwen3.5:4b-q8_0 (ollama) | 5.2 GB | 8.5 | 6 GB | T1,T2,T3,T4 | any | `ollama pull qwen3.5:4b-q8_0` |
| `llm-qwen3-5-small-gguf-q4-k-m-2` | Qwen3.5-9B-GGUF · Q4_K_M (GGUF) | 5.7 GB | 4.5 | 7 GB | T1,T2,T3,T4,T5 | any | `hf download unsloth/Qwen3.5-9B-GGUF --include "*Q4_K_M*"` |
| `llm-qwen3-5-small-gguf-q4-k-m-3` | MiMo-V2.6-Distill-Qwen-9B-GGUF · Q4_K_M (GGUF) | 5.8 GB | 4.5 | 7 GB | T1,T2,T3,T4,T5 | any | `hf download bartowski/MiMo-V2.6-Distill-Qwen-9B-GGUF --include "*Q4_K_M*"` |
| `llm-qwen3-5-small-gguf-ud-q4-k-xl-2` | Qwen3.5-9B-GGUF · UD-Q4_K_XL (GGUF) | 6.0 GB | 4.5 | 7 GB | T1,T2,T3,T4,T5 | any | `hf download unsloth/Qwen3.5-9B-GGUF --include "*UD-Q4_K_XL*"` |
| `llm-qwen3-5-small-ollama-ollama-3` |  · ollama qwen3.5:9b (ollama) | 6.5 GB | 4.5 | 8 GB | T1,T2,T3,T4 | any | `ollama pull qwen3.5:9b` |
| `llm-qwen3-5-small-ollama-ollama-4` |  · ollama mimo-v2.6:9b / :9b-q4_K_M (ollama) | 6.5 GB | 4.5 | 8 GB | T1,T2,T3,T4 | any | `ollama pull mimo-v2.6:9b / :9b-q4_K_M` |
| `llm-qwen3-5-small-gguf-q5-k-m` | MiMo-V2.6-Distill-Qwen-9B-GGUF · Q5_K_M (GGUF) | 6.9 GB | 5.5 | 8 GB | T1,T2,T3,T4,T5 | any | `hf download bartowski/MiMo-V2.6-Distill-Qwen-9B-GGUF --include "*Q5_K_M*"` |
| `llm-qwen3-5-small-gguf-q6-k-2` | Qwen3.5-9B-GGUF · Q6_K (GGUF) | 7.5 GB | 6.5 | 9 GB | T1,T2,T3,T4,T5 | any | `hf download unsloth/Qwen3.5-9B-GGUF --include "*Q6_K*"` |
| `llm-qwen3-5-small-gguf-q6-k-3` | MiMo-V2.6-Distill-Qwen-9B-GGUF · Q6_K (GGUF) | 7.8 GB | 6.5 | 9 GB | T1,T2,T3,T4,T5 | any | `hf download bartowski/MiMo-V2.6-Distill-Qwen-9B-GGUF --include "*Q6_K*"` |
| `llm-qwen3-5-small-gguf-q8-0-2` | Qwen3.5-9B-GGUF · Q8_0 (GGUF) | 9.5 GB | 8.5 | 11 GB | T1,T2,T3,T4,T5 | any | `hf download unsloth/Qwen3.5-9B-GGUF --include "*Q8_0*"` |
| `llm-qwen3-5-small-gguf-q8-0-3` | MiMo-V2.6-Distill-Qwen-9B-GGUF · Q8_0 (GGUF) | 9.6 GB | 8.5 | 11 GB | T1,T2,T3,T4,T5 | any | `hf download bartowski/MiMo-V2.6-Distill-Qwen-9B-GGUF --include "*Q8_0*"` |
| `llm-qwen3-5-small-ollama-ollama-5` |  · ollama qwen3.5:9b-q8_0 (ollama) | 10.4 GB | 8.5 | 12 GB | T1,T2,T3,T4 | any | `ollama pull qwen3.5:9b-q8_0` |
| `llm-qwen3-5-small-ollama-ollama-6` |  · ollama mimo-v2.6:9b-q8_0 (ollama) | 10.4 GB | 8.5 | 12 GB | T1,T2,T3,T4 | any | `ollama pull mimo-v2.6:9b-q8_0` |
</details>

<details><summary><b>DeepSeek-V4.1-Flash-1017 abliterated (huihui GGUF) / heretic (pqhaz) / abliterated (mrfakename)</b> – 5 változat</summary>

| id | Fájl / repó | Méret | Bit | Min. memória (≈×1,15) | HW | Platform | Letöltés |
|---|---|---|---|---|---|---|---|
| `llm-deepseek-v4-1-flash-1017-abliterated-hui-gguf-ud-iq1-s` | Huihui-DeepSeek-V4.1-Flash-1017-abliterated-GGUF · UD-IQ1_S (GGUF) | 233.0 GB | 1.7 | 268 GB | T1,T2 | any | `hf download huihui-ai/Huihui-DeepSeek-V4.1-Flash-1017-abliterated-GGUF --include "*UD-IQ1_S*"` |
| `llm-deepseek-v4-1-flash-1017-abliterated-hui-gguf-ud-iq1-m` | Huihui-DeepSeek-V4.1-Flash-1017-abliterated-GGUF · UD-IQ1_M (GGUF) | 250.4 GB | 1.7 | 288 GB | T1,T2 | any | `hf download huihui-ai/Huihui-DeepSeek-V4.1-Flash-1017-abliterated-GGUF --include "*UD-IQ1_M*"` |
| `llm-deepseek-v4-1-flash-1017-abliterated-hui-mlx-n-a` | DeepSeek-V4.1-Flash-1017-Abliterated-MLX · n/a (heretic alapú) (MLX) | 422.6 GB | 4.5 | 486 GB | T1,T2 | mac | `hf download apetersson/DeepSeek-V4.1-Flash-1017-Abliterated-MLX` |
| `llm-deepseek-v4-1-flash-1017-abliterated-hui-gguf-q8-0` | DeepSeek-V4.1-Flash-1017-heretic-GGUF · Q8_0 (GGUF) | 507.9 GB | 8.5 | 584 GB | T1 | any | `hf download pqhaz/DeepSeek-V4.1-Flash-1017-heretic-GGUF --include "*Q8_0*"` |
| `llm-deepseek-v4-1-flash-1017-abliterated-hui-safetensors-fp8-original` | DeepSeek-V4.1-Flash-1017-abliterated · original FP8 (safetensors FP8) | 510.3 GB | 8.5 | 587 GB | T1 | server | `hf download mrfakename/DeepSeek-V4.1-Flash-1017-abliterated` |
</details>

<details><summary><b>GLM-5.3 abliterated (huihui GGUF)</b> – 1 változat</summary>

| id | Fájl / repó | Méret | Bit | Min. memória (≈×1,15) | HW | Platform | Letöltés |
|---|---|---|---|---|---|---|---|
| `llm-glm-5-3-abliterated-huihui-gguf-gguf-ud-iq1-s` | Huihui-GLM-5.3-abliterated-GGUF · UD-IQ1_S (GGUF) | 216.7 GB | 1.7 | 249 GB | T1,T2 | any | `hf download huihui-ai/Huihui-GLM-5.3-abliterated-GGUF --include "*UD-IQ1_S*"` |
</details>

<details><summary><b>Qwen3.8-Flash-Next abliterated v2 (huihui GGUF)</b> – 9 változat</summary>

| id | Fájl / repó | Méret | Bit | Min. memória (≈×1,15) | HW | Platform | Letöltés |
|---|---|---|---|---|---|---|---|
| `llm-qwen3-8-flash-next-abliterated-v2-huihui-gguf-swift` | Huihui-Qwen3.8-Flash-Next-abliterated-v2-GGUF · Swift GSQ-RCO IQ2_XS (GGUF) | 68.2 GB | 2.6 | 78 GB | T1,T2,T3 | any | `hf download huihui-ai/Huihui-Qwen3.8-Flash-Next-abliterated-v2-GGUF --include "*Swift*"` |
| `llm-qwen3-8-flash-next-abliterated-v2-huihui-gguf-swift-2` | Huihui-Qwen3.8-Flash-Next-abliterated-v2-GGUF · Swift IQ3_XXS (GGUF) | 76.0 GB | 3.5 | 87 GB | T1,T2,T3 | any | `hf download huihui-ai/Huihui-Qwen3.8-Flash-Next-abliterated-v2-GGUF --include "*Swift*"` |
| `llm-qwen3-8-flash-next-abliterated-v2-huihui-gguf-swift-3` | Huihui-Qwen3.8-Flash-Next-abliterated-v2-GGUF · Swift IQ3_S (GGUF) | 83.7 GB | 3.5 | 96 GB | T1,T2,T3 | any | `hf download huihui-ai/Huihui-Qwen3.8-Flash-Next-abliterated-v2-GGUF --include "*Swift*"` |
| `llm-qwen3-8-flash-next-abliterated-v2-huihui-gguf-unsloth-ud-iq4-xs` | Huihui-Qwen3.8-Flash-Next-abliterated-v2-GGUF · unsloth-UD-IQ4_XS (GGUF) | 93.7 GB | 4.5 | 108 GB | T1,T2,T3 | any | `hf download huihui-ai/Huihui-Qwen3.8-Flash-Next-abliterated-v2-GGUF --include "*unsloth-UD-IQ4_XS*"` |
| `llm-qwen3-8-flash-next-abliterated-v2-huihui-gguf-unsloth-ud-q4-k-xl` | Huihui-Qwen3.8-Flash-Next-abliterated-v2-GGUF · unsloth-UD-Q4_K_XL (GGUF) | 111.3 GB | 4.5 | 128 GB | T1,T2,T3 | any | `hf download huihui-ai/Huihui-Qwen3.8-Flash-Next-abliterated-v2-GGUF --include "*unsloth-UD-Q4_K_XL*"` |
| `llm-qwen3-8-flash-next-abliterated-v2-huihui-mlx-oq5e-mtp` | Qwen3.8-Flash-Next-Uncensored-oQ5e-mtp · oQ5e-mtp (MLX) | 128.6 GB | 5.5 | 148 GB | T1,T2 | mac | `hf download mlx-community/Qwen3.8-Flash-Next-Uncensored-oQ5e-mtp` |
| `llm-qwen3-8-flash-next-abliterated-v2-huihui-gguf-ud-q5-k-xl` | Huihui-Qwen3.8-Flash-Next-abliterated-v2-GGUF · UD-Q5_K_XL (GGUF) | 158.3 GB | 5.5 | 182 GB | T1,T2 | any | `hf download huihui-ai/Huihui-Qwen3.8-Flash-Next-abliterated-v2-GGUF --include "*UD-Q5_K_XL*"` |
| `llm-qwen3-8-flash-next-abliterated-v2-huihui-gguf-ud-q6-k-xl` | Huihui-Qwen3.8-Flash-Next-abliterated-v2-GGUF · UD-Q6_K_XL (GGUF) | 169.2 GB | 6.5 | 195 GB | T1,T2 | any | `hf download huihui-ai/Huihui-Qwen3.8-Flash-Next-abliterated-v2-GGUF --include "*UD-Q6_K_XL*"` |
| `llm-qwen3-8-flash-next-abliterated-v2-huihui-gguf-q8-0` | Huihui-Qwen3.8-Flash-Next-abliterated-v2-GGUF · Q8_0 (GGUF) | 188.2 GB | 8.5 | 216 GB | T1,T2 | any | `hf download huihui-ai/Huihui-Qwen3.8-Flash-Next-abliterated-v2-GGUF --include "*Q8_0*"` |
</details>

<details><summary><b>MiniMax-M3.1-Flash abliterated (orcarouter GGUF)</b> – 1 változat</summary>

| id | Fájl / repó | Méret | Bit | Min. memória (≈×1,15) | HW | Platform | Letöltés |
|---|---|---|---|---|---|---|---|
| `llm-minimax-m3-1-flash-abliterated-orcaroute-gguf-mix-128g` | MiniMax-M3.1-Flash-abliterated-GGUF · Mix-128G (GGUF) | 111.9 GB | 4.5 | 129 GB | T1,T2,T3 | any | `hf download orcarouter/MiniMax-M3.1-Flash-abliterated-GGUF --include "*Mix-128G*"` |
</details>

<details><summary><b>GLM-5.3-Flash abliterated (huihui GGUF)</b> – 10 változat</summary>

| id | Fájl / repó | Méret | Bit | Min. memória (≈×1,15) | HW | Platform | Letöltés |
|---|---|---|---|---|---|---|---|
| `llm-glm-5-3-flash-abliterated-huihui-gguf-gguf-ud-iq1-s` | Huihui-GLM-5.3-Flash-abliterated-GGUF · UD-IQ1_S (GGUF) | 93.1 GB | 1.7 | 107 GB | T1,T2,T3 | any | `hf download huihui-ai/Huihui-GLM-5.3-Flash-abliterated-GGUF --include "*UD-IQ1_S*"` |
| `llm-glm-5-3-flash-abliterated-huihui-gguf-gguf-ud-iq2-xxs` | Huihui-GLM-5.3-Flash-abliterated-GGUF · UD-IQ2_XXS (GGUF) | 101.8 GB | 2.6 | 117 GB | T1,T2,T3 | any | `hf download huihui-ai/Huihui-GLM-5.3-Flash-abliterated-GGUF --include "*UD-IQ2_XXS*"` |
| `llm-glm-5-3-flash-abliterated-huihui-gguf-gguf-ud-q2-k-xl` | Huihui-GLM-5.3-Flash-abliterated-GGUF · UD-Q2_K_XL (GGUF) | 108.7 GB | 2.6 | 125 GB | T1,T2,T3 | any | `hf download huihui-ai/Huihui-GLM-5.3-Flash-abliterated-GGUF --include "*UD-Q2_K_XL*"` |
| `llm-glm-5-3-flash-abliterated-huihui-gguf-gguf-ud-iq3-xxs` | Huihui-GLM-5.3-Flash-abliterated-GGUF · UD-IQ3_XXS (GGUF) | 120.4 GB | 3.5 | 138 GB | T1,T2,T3 | any | `hf download huihui-ai/Huihui-GLM-5.3-Flash-abliterated-GGUF --include "*UD-IQ3_XXS*"` |
| `llm-glm-5-3-flash-abliterated-huihui-gguf-gguf-ud-q3-k-xl` | Huihui-GLM-5.3-Flash-abliterated-GGUF · UD-Q3_K_XL (GGUF) | 147.5 GB | 3.5 | 170 GB | T1,T2 | any | `hf download huihui-ai/Huihui-GLM-5.3-Flash-abliterated-GGUF --include "*UD-Q3_K_XL*"` |
| `llm-glm-5-3-flash-abliterated-huihui-gguf-gguf-ud-iq4-xs` | Huihui-GLM-5.3-Flash-abliterated-GGUF · UD-IQ4_XS (GGUF) | 156.8 GB | 4.5 | 180 GB | T1,T2 | any | `hf download huihui-ai/Huihui-GLM-5.3-Flash-abliterated-GGUF --include "*UD-IQ4_XS*"` |
| `llm-glm-5-3-flash-abliterated-huihui-gguf-mlx-4bit` | GLM-5.3-Flash-Abliterated-MLX-4bit · 4bit (MLX) | 185.9 GB | 4.5 | 214 GB | T1,T2 | mac | `hf download grant-ai/GLM-5.3-Flash-Abliterated-MLX-4bit` |
| `llm-glm-5-3-flash-abliterated-huihui-gguf-gguf-ud-q4-k-xl` | Huihui-GLM-5.3-Flash-abliterated-GGUF · UD-Q4_K_XL (GGUF) | 199.7 GB | 4.5 | 230 GB | T1,T2 | any | `hf download huihui-ai/Huihui-GLM-5.3-Flash-abliterated-GGUF --include "*UD-Q4_K_XL*"` |
| `llm-glm-5-3-flash-abliterated-huihui-gguf-gguf-ud-q5-k-xl` | Huihui-GLM-5.3-Flash-abliterated-GGUF · UD-Q5_K_XL (GGUF) | 240.3 GB | 5.5 | 276 GB | T1,T2 | any | `hf download huihui-ai/Huihui-GLM-5.3-Flash-abliterated-GGUF --include "*UD-Q5_K_XL*"` |
| `llm-glm-5-3-flash-abliterated-huihui-gguf-gguf-ud-q6-k-xl` | Huihui-GLM-5.3-Flash-abliterated-GGUF · UD-Q6_K_XL (GGUF) | 291.8 GB | 6.5 | 336 GB | T1,T2 | any | `hf download huihui-ai/Huihui-GLM-5.3-Flash-abliterated-GGUF --include "*UD-Q6_K_XL*"` |
</details>

<details><summary><b>NousResearch Arete-27B (a "R1-1776 utód")</b> – 2 változat</summary>

| id | Fájl / repó | Méret | Bit | Min. memória (≈×1,15) | HW | Platform | Letöltés |
|---|---|---|---|---|---|---|---|
| `llm-nousresearch-arete-27b-a-r1-1776-ut-d-gguf-iq4-xs` | NousResearch_Arete-27B-GGUF · IQ4_XS (GGUF) | 15.2 GB | 4.5 | 18 GB | T1,T2,T3,T4 | any | `hf download bartowski/NousResearch_Arete-27B-GGUF --include "*IQ4_XS*"` |
| `llm-nousresearch-arete-27b-a-r1-1776-ut-d-gguf-q4-k-m` | NousResearch_Arete-27B-GGUF · Q4_K_M (GGUF) | 17.2 GB | 4.5 | 20 GB | T1,T2,T3 | any | `hf download bartowski/NousResearch_Arete-27B-GGUF --include "*Q4_K_M*"` |
</details>

<details><summary><b>Qwen3.8-27B abliterated (huihui) / heretic-ara (trohrbaugh)</b> – 6 változat</summary>

| id | Fájl / repó | Méret | Bit | Min. memória (≈×1,15) | HW | Platform | Letöltés |
|---|---|---|---|---|---|---|---|
| `llm-qwen3-8-27b-abliterated-huihui-heretic-a-gguf-q2-k` | Huihui-Qwen3.8-27B-abliterated-GGUF · Q2_K (GGUF) | 10.9 GB | 2.6 | 12 GB | T1,T2,T3,T4 | any | `hf download huihui-ai/Huihui-Qwen3.8-27B-abliterated-GGUF --include "*Q2_K*"` |
| `llm-qwen3-8-27b-abliterated-huihui-heretic-a-gguf-ud-iq4-xs` | Huihui-Qwen3.8-27B-abliterated-GGUF · UD-IQ4_XS (GGUF) | 14.4 GB | 4.5 | 17 GB | T1,T2,T3,T4 | any | `hf download huihui-ai/Huihui-Qwen3.8-27B-abliterated-GGUF --include "*UD-IQ4_XS*"` |
| `llm-qwen3-8-27b-abliterated-huihui-heretic-a-gguf-ud-dw-q4-k-m` | Huihui-Qwen3.8-27B-abliterated-GGUF · UD-DW-Q4_K_M (GGUF) | 16.6 GB | 4.5 | 19 GB | T1,T2,T3 | any | `hf download huihui-ai/Huihui-Qwen3.8-27B-abliterated-GGUF --include "*UD-DW-Q4_K_M*"` |
| `llm-qwen3-8-27b-abliterated-huihui-heretic-a-mlx-optiq-4bit` | Qwen3.8-27B-Uncensored-OptiQ-4bit · OptiQ-4bit (MLX) | 19.8 GB | 4.5 | 23 GB | T1,T2,T3,T4 | mac | `hf download mlx-community/Qwen3.8-27B-Uncensored-OptiQ-4bit` |
| `llm-qwen3-8-27b-abliterated-huihui-heretic-a-gguf-q6-k` | Huihui-Qwen3.8-27B-abliterated-GGUF · Q6_K (GGUF) | 22.4 GB | 6.5 | 26 GB | T1,T2,T3 | any | `hf download huihui-ai/Huihui-Qwen3.8-27B-abliterated-GGUF --include "*Q6_K*"` |
| `llm-qwen3-8-27b-abliterated-huihui-heretic-a-gguf-q8-0` | Huihui-Qwen3.8-27B-abliterated-GGUF · Q8_0 (GGUF) | 29.1 GB | 8.5 | 33 GB | T1,T2,T3 | any | `hf download huihui-ai/Huihui-Qwen3.8-27B-abliterated-GGUF --include "*Q8_0*"` |
</details>

<details><summary><b>Kimi-K3 Abliterated V1 (Uniboshi)</b> – 1 változat</summary>

| id | Fájl / repó | Méret | Bit | Min. memória (≈×1,15) | HW | Platform | Letöltés |
|---|---|---|---|---|---|---|---|
| `llm-kimi-k3-abliterated-v1-uniboshi-gguf-mxfp4-moe` | Kimi-K3-Abliterated-V1-GGUF · MXFP4_MOE (GGUF) | 1.51 TB | 4.5 | 1735 GB | T1 | any | `hf download Uniboshi/Kimi-K3-Abliterated-V1-GGUF --include "*MXFP4_MOE*"` |
</details>

<details><summary><b>Qwen3.6-35B-A3B uncensored-heretic (llmfan46) / abliterated-MTP (huihui)</b> – 2 változat</summary>

| id | Fájl / repó | Méret | Bit | Min. memória (≈×1,15) | HW | Platform | Letöltés |
|---|---|---|---|---|---|---|---|
| `llm-qwen3-6-35b-a3b-uncensored-heretic-llmfa-gguf-q3-k-m` | Qwen3.6-35B-A3B-uncensored-heretic-GGUF · Q3_K_M (GGUF) | 16.9 GB | 3.5 | 19 GB | T1,T2,T3,T4 | any | `hf download llmfan46/Qwen3.6-35B-A3B-uncensored-heretic-GGUF --include "*Q3_K_M*"` |
| `llm-qwen3-6-35b-a3b-uncensored-heretic-llmfa-gguf-q4-k-m` | Qwen3.6-35B-A3B-uncensored-heretic-GGUF · Q4_K_M (GGUF) | 21.2 GB | 4.5 | 24 GB | T1,T2,T3,T4 | any | `hf download llmfan46/Qwen3.6-35B-A3B-uncensored-heretic-GGUF --include "*Q4_K_M*"` |
</details>

<details><summary><b>Mistral-Small-4-119B-2603 heretic (darkc0de, GGUF: Rioky)</b> – 6 változat</summary>

| id | Fájl / repó | Méret | Bit | Min. memória (≈×1,15) | HW | Platform | Letöltés |
|---|---|---|---|---|---|---|---|
| `llm-mistral-small-4-119b-2603-heretic-darkc0-gguf-q2-k` | Mistral-Small-4-119B-2603-heretic-gguf · Q2_K (GGUF) | 43.4 GB | 2.6 | 50 GB | T1,T2,T3 | any | `hf download Rioky/Mistral-Small-4-119B-2603-heretic-gguf --include "*Q2_K*"` |
| `llm-mistral-small-4-119b-2603-heretic-darkc0-gguf-q3-k-m` | Mistral-Small-4-119B-2603-heretic-gguf · Q3_K_M (GGUF) | 56.9 GB | 3.5 | 65 GB | T1,T2,T3 | any | `hf download Rioky/Mistral-Small-4-119B-2603-heretic-gguf --include "*Q3_K_M*"` |
| `llm-mistral-small-4-119b-2603-heretic-darkc0-gguf-q4-k-s` | Mistral-Small-4-119B-2603-heretic-gguf · Q4_K_S (GGUF) | 67.7 GB | 4.5 | 78 GB | T1,T2,T3 | any | `hf download Rioky/Mistral-Small-4-119B-2603-heretic-gguf --include "*Q4_K_S*"` |
| `llm-mistral-small-4-119b-2603-heretic-darkc0-gguf-q4-k-m` | Mistral-Small-4-119B-2603-heretic-gguf · Q4_K_M (GGUF) | 72.2 GB | 4.5 | 83 GB | T1,T2,T3 | any | `hf download Rioky/Mistral-Small-4-119B-2603-heretic-gguf --include "*Q4_K_M*"` |
| `llm-mistral-small-4-119b-2603-heretic-darkc0-gguf-q5-k-m` | Mistral-Small-4-119B-2603-heretic-gguf · Q5_K_M (GGUF) | 84.5 GB | 5.5 | 97 GB | T1,T2 | any | `hf download Rioky/Mistral-Small-4-119B-2603-heretic-gguf --include "*Q5_K_M*"` |
| `llm-mistral-small-4-119b-2603-heretic-darkc0-gguf-q8-0` | Mistral-Small-4-119B-2603-heretic-gguf · Q8_0 (GGUF) | 126.5 GB | 8.5 | 145 GB | T1,T2 | any | `hf download Rioky/Mistral-Small-4-119B-2603-heretic-gguf --include "*Q8_0*"` |
</details>

<details><summary><b>gemma-4-31B-it heretic (coder3101) / uncensored-heretic (llmfan46)</b> – 4 változat</summary>

| id | Fájl / repó | Méret | Bit | Min. memória (≈×1,15) | HW | Platform | Letöltés |
|---|---|---|---|---|---|---|---|
| `llm-gemma-4-31b-it-heretic-coder3101-uncenso-gguf-iq4-xs` | gemma-4-31B-it-heretic-GGUF · IQ4_XS (GGUF) | 16.9 GB | 4.5 | 19 GB | T1,T2,T3,T4 | any | `hf download mradermacher/gemma-4-31B-it-heretic-GGUF --include "*IQ4_XS*"` |
| `llm-gemma-4-31b-it-heretic-coder3101-uncenso-mlx-4bit` | gemma-4-31B-it-uncensored-heretic-4bit · 4bit (MLX) | 17.3 GB | 4.5 | 20 GB | T1,T2,T3,T4 | mac | `hf download mlx-community/gemma-4-31B-it-uncensored-heretic-4bit` |
| `llm-gemma-4-31b-it-heretic-coder3101-uncenso-gguf-q4-k-m` | gemma-4-31B-it-heretic-GGUF · Q4_K_M (GGUF) | 18.7 GB | 4.5 | 21 GB | T1,T2,T3 | any | `hf download mradermacher/gemma-4-31B-it-heretic-GGUF --include "*Q4_K_M*"` |
| `llm-gemma-4-31b-it-heretic-coder3101-uncenso-gguf-q6-k` | gemma-4-31B-it-heretic-GGUF · Q6_K (GGUF) | 25.2 GB | 6.5 | 29 GB | T1,T2,T3 | any | `hf download mradermacher/gemma-4-31B-it-heretic-GGUF --include "*Q6_K*"` |
</details>

<details><summary><b>gpt-oss-120b heretic (MuXodious tainted-heresy / kldzj heretic)</b> – 3 változat</summary>

| id | Fájl / repó | Méret | Bit | Min. memória (≈×1,15) | HW | Platform | Letöltés |
|---|---|---|---|---|---|---|---|
| `llm-gpt-oss-120b-heretic-muxodious-tainted-h-mlx-mxfp4` | gpt-oss-120b-tainted-heresy-mlx-MXFP4 · MXFP4 (MLX) | 62.2 GB | 4.5 | 71 GB | T1,T2,T3,T4 | mac | `hf download MuXodious/gpt-oss-120b-tainted-heresy-mlx-MXFP4` |
| `llm-gpt-oss-120b-heretic-muxodious-tainted-h-gguf-mxfp4-moe` | gpt-oss-120b-tainted-heresy-GGUF · MXFP4_MoE (GGUF) | 63.4 GB | 4.5 | 73 GB | T1,T2,T3 | any | `hf download MuXodious/gpt-oss-120b-tainted-heresy-GGUF --include "*MXFP4_MoE*"` |
| `llm-gpt-oss-120b-heretic-muxodious-tainted-h-gguf-mxfp4-moe-2` | kldzj_gpt-oss-120b-heretic-GGUF · MXFP4_MOE (GGUF) | 63.4 GB | 4.5 | 73 GB | T1,T2,T3 | any | `hf download bartowski/kldzj_gpt-oss-120b-heretic-GGUF --include "*MXFP4_MOE*"` |
</details>

<details><summary><b>gemma-4-26B-A4B-it ultra-uncensored-heretic (llmfan46)</b> – 2 változat</summary>

| id | Fájl / repó | Méret | Bit | Min. memória (≈×1,15) | HW | Platform | Letöltés |
|---|---|---|---|---|---|---|---|
| `llm-gemma-4-26b-a4b-it-ultra-uncensored-here-gguf-q3-k-m` | gemma-4-26B-A4B-it-ultra-uncensored-heretic-GGUF · Q3_K_M (GGUF) | 13.3 GB | 3.5 | 15 GB | T1,T2,T3,T4 | any | `hf download llmfan46/gemma-4-26B-A4B-it-ultra-uncensored-heretic-GGUF --include "*Q3_K_M*"` |
| `llm-gemma-4-26b-a4b-it-ultra-uncensored-here-gguf-q4-k-m` | gemma-4-26B-A4B-it-ultra-uncensored-heretic-GGUF · Q4_K_M (GGUF) | 16.8 GB | 4.5 | 19 GB | T1,T2,T3,T4 | any | `hf download llmfan46/gemma-4-26B-A4B-it-ultra-uncensored-heretic-GGUF --include "*Q4_K_M*"` |
</details>

<details><summary><b>gemma-4-12B-it uncensored-heretic (llmfan46) / abliterated QAT (huihui)</b> – 1 változat</summary>

| id | Fájl / repó | Méret | Bit | Min. memória (≈×1,15) | HW | Platform | Letöltés |
|---|---|---|---|---|---|---|---|
| `llm-gemma-4-12b-it-uncensored-heretic-llmfan-gguf-q4-k-m` | gemma-4-12B-it-uncensored-heretic-GGUF · Q4_K_M (GGUF) | 8.5 GB | 4.5 | 10 GB | T1,T2,T3,T4 | any | `hf download llmfan46/gemma-4-12B-it-uncensored-heretic-GGUF --include "*Q4_K_M*"` |
</details>

<details><summary><b>gemma-4-E4B-it heretic (coder3101; GGUF Abiray) / ultra-uncensored (llmfan46)</b> – 1 változat</summary>

| id | Fájl / repó | Méret | Bit | Min. memória (≈×1,15) | HW | Platform | Letöltés |
|---|---|---|---|---|---|---|---|
| `llm-gemma-4-e4b-it-heretic-coder3101-gguf-ab-gguf-q4-k-m` | gemma-4-E4B-it-heretic-GGUF · Q4_K_M (GGUF) | 5.3 GB | 4.5 | 6 GB | T1,T2,T3,T4,T5 | any | `hf download Abiray/gemma-4-E4B-it-heretic-GGUF --include "*Q4_K_M*"` |
</details>

<details><summary><b>Qwen3.5-9B heretic-v2 (trohrbaugh)</b> – 2 változat</summary>

| id | Fájl / repó | Méret | Bit | Min. memória (≈×1,15) | HW | Platform | Letöltés |
|---|---|---|---|---|---|---|---|
| `llm-qwen3-5-9b-heretic-v2-trohrbaugh-gguf-q4-k-m` | Qwen3.5-9B-heretic-v2-GGUF · Q4_K_M (GGUF) | 5.6 GB | 4.5 | 6 GB | T1,T2,T3,T4,T5 | any | `hf download filvyb/Qwen3.5-9B-heretic-v2-GGUF --include "*Q4_K_M*"` |
| `llm-qwen3-5-9b-heretic-v2-trohrbaugh-gguf-q8-0` | Qwen3.5-9B-heretic-v2-GGUF · Q8_0 (GGUF) | 9.5 GB | 8.5 | 11 GB | T1,T2,T3,T4 | any | `hf download filvyb/Qwen3.5-9B-heretic-v2-GGUF --include "*Q8_0*"` |
</details>

<details><summary><b>gpt-oss-20b heretic (MuXodious RichardErkhov-heresy / p-e-w heretic)</b> – 1 változat</summary>

| id | Fájl / repó | Méret | Bit | Min. memória (≈×1,15) | HW | Platform | Letöltés |
|---|---|---|---|---|---|---|---|
| `llm-gpt-oss-20b-heretic-muxodious-richarderk-gguf-mxfp4-moe` | gpt-oss-20b-RichardErkhov-heresy-GGUF · MXFP4_MoE (GGUF) | 12.7 GB | 4.5 | 15 GB | T1,T2,T3,T4 | any | `hf download MuXodious/gpt-oss-20b-RichardErkhov-heresy-GGUF --include "*MXFP4_MoE*"` |
</details>

<details><summary><b>Qwen3.5-4B heretic-2.0 (p-e-w) / SOMPOA-heresy-v2 (MuXodious)</b> – 4 változat</summary>

| id | Fájl / repó | Méret | Bit | Min. memória (≈×1,15) | HW | Platform | Letöltés |
|---|---|---|---|---|---|---|---|
| `llm-qwen3-5-4b-heretic-2-0-p-e-w-sompoa-here-gguf-iq4-xs` | Qwen3.5-4B-heretic-2.0-GGUF · IQ4_XS (GGUF) | 2.5 GB | 4.5 | 3 GB | T1,T2,T3,T4,T5 | any | `hf download mradermacher/Qwen3.5-4B-heretic-2.0-GGUF --include "*IQ4_XS*"` |
| `llm-qwen3-5-4b-heretic-2-0-p-e-w-sompoa-here-gguf-q4-k-m` | Qwen3.5-4B-heretic-2.0-GGUF · Q4_K_M (GGUF) | 2.7 GB | 4.5 | 3 GB | T1,T2,T3,T4,T5 | any | `hf download mradermacher/Qwen3.5-4B-heretic-2.0-GGUF --include "*Q4_K_M*"` |
| `llm-qwen3-5-4b-heretic-2-0-p-e-w-sompoa-here-gguf-q6-k` | Qwen3.5-4B-heretic-2.0-GGUF · Q6_K (GGUF) | 3.5 GB | 6.5 | 4 GB | T1,T2,T3,T4,T5 | any | `hf download mradermacher/Qwen3.5-4B-heretic-2.0-GGUF --include "*Q6_K*"` |
| `llm-qwen3-5-4b-heretic-2-0-p-e-w-sompoa-here-gguf-q8-0` | Qwen3.5-4B-heretic-2.0-GGUF · Q8_0 (GGUF) | 4.5 GB | 8.5 | 5 GB | T1,T2,T3,T4,T5 | any | `hf download mradermacher/Qwen3.5-4B-heretic-2.0-GGUF --include "*Q8_0*"` |
</details>

<details><summary><b>gemma-4-E2B-it ultra-uncensored-heretic (llmfan46)</b> – 2 változat</summary>

| id | Fájl / repó | Méret | Bit | Min. memória (≈×1,15) | HW | Platform | Letöltés |
|---|---|---|---|---|---|---|---|
| `llm-gemma-4-e2b-it-ultra-uncensored-heretic--gguf-q4-k-m` | gemma-4-E2B-it-ultra-uncensored-heretic-GGUF · Q4_K_M (GGUF) | 3.4 GB | 4.5 | 4 GB | T1,T2,T3,T4,T5 | any | `hf download llmfan46/gemma-4-E2B-it-ultra-uncensored-heretic-GGUF --include "*Q4_K_M*"` |
| `llm-gemma-4-e2b-it-ultra-uncensored-heretic--gguf-q5-k-m` | gemma-4-E2B-it-ultra-uncensored-heretic-GGUF · Q5_K_M (GGUF) | 3.6 GB | 5.5 | 4 GB | T1,T2,T3,T4,T5 | any | `hf download llmfan46/gemma-4-E2B-it-ultra-uncensored-heretic-GGUF --include "*Q5_K_M*"` |
</details>


### 6.5 Cenzúrázatlan („uncensored”) változatok: mi ez és mennyit veszít

- **Abliteration:** a modell aktivációiból kiszámolt „elutasítási irányt” kivetítik a súlyokból. Gyors, nem kell hozzá tanítás. Fő gyártók: huihui-ai, mrfakename.
- **Heretic** (`p-e-w/heretic`, PyPI `heretic-llm`): automatikusan hangolt abliteration (ARA). Úgy minimalizálja az elutasítást, hogy közben az eredeti viselkedéstől való eltérés (KL) kicsi maradjon. **Offline is futtatható bármely modellen**, így egy új alapmodellből magad is készíthetsz cenzúrázatlant. Az ehhez kellő adathalmazok (`mlabonne/harmful_behaviors`, `mlabonne/harmless_alpaca`) kicsik, töltsd le őket előre.
- **Intelligenciaveszteség** (UGI NatInt mérések): nagy modellen (gemma-4-26B/31B, gpt-oss-120b, Qwen3.6-35B) ~0–2 pont, kicsin (9B–20B) akár 5–11 pont. Kis gépre ezért legyen meg az eredeti modell is.
- **Ajánlott párosítás:** egy alapmodell + egy cenzúrázatlan változat ugyanabból a családból. A szkript alapból ezt választja (`--uncensored also`). Csak cenzúrázatlan: `only`. Kihagyás: `no`.
- **A cenzúrázatlan modell nem megbízhatóbb.** Kevesebbet utasít el, de ugyanúgy hallucinál. Életveszélyes témában (gyógyszer, vegyi anyag, robbanóanyag, statika) a forrásdokumentum dönt.

#### Rangsor: cenzúrázatlan modellek

- **Sorrend:** a cenzúrázatlan változat *számolt* intelligenciája szerint (AA v5 skálán).
- **Számolt pont:** az alapmodell AA v5 pontja × (cenzúrázatlan/alap) arány. Az arány „M” jelnél a UGI ranglista NatInt-méréséből jön. „B” jelnél becslés: nagy MoE abliteration 0,95–0,97, közösségi és nem ellenőrzött 0,93, kis dense 0,93.
- **% Opus 5.5:** a számolt pont / 59,1 (Claude Opus 5.5 max, AA v5.0.1).
- **„Cenz.” és „HU” oszlop:** 0–10-es kutatói becslés.
- **`~` jel az AA oszlopban:** az alapmodellnek nincs AA v5 pontja, az érték becslés.
- **UGI NatInt:** a természetes intelligencia mérése az Uncensored General Intelligence ranglistán, az alap → cenzúrázatlan változás.
- **„Leggyengébb gép”:** az a legkisebb hardverszint, amelyen még fut GGUF-változat.
- **Méretek:** a Hugging Face API-ból (2026-11-14).

| # | Pontos név (repó) | Alapmodell (kiadva) | Paraméter | AA v5 alap | **AA v5 cenz.-mentes (számolt)** | **% Opus 5.5** | Számítás | Módszer | Cenz. | HU | UGI / NatInt | Változat | Méret min–max | Leggyengébb gép | Licenc |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **[huihui-ai/Huihui-DeepSeek-V4.1-Flash-1017-abliterated-GGUF](https://huggingface.co/huihui-ai/Huihui-DeepSeek-V4.1-Flash-1017-abliterated-GGUF)** | `deepseek-ai/DeepSeek-V4.1-Flash-1017` (2026-10-17) | 763.2B total (safetensors); 384 routed expert | 32.6 | **~31.6** | **~53%** | × 0.97 (B: abliteration, KL 0,067 (kicsi eltérés), nagy MoE) | Abliteration (huihui: 18 attn_output tenzor) + Heretic (pqhaz) + Abliteration FP8 (mrfakename) | 9 | 8 | elutasítás 97→4% chat, 98→9% think; KL 0,067 (mrfakename kártya) | 5 | 233.0 GB – 510.3 GB | T2: `huihui-ai/Huihui-DeepSeek-V4.1-Flash-1017-abliterated-GGUF` ['*UD-IQ1_S*'] (233.0 GB) | MIT |
| 2 | **[huihui-ai/Huihui-GLM-5.3-abliterated-GGUF](https://huggingface.co/huihui-ai/Huihui-GLM-5.3-abliterated-GGUF)** | `zai-org/GLM-5.3` (2026-08-25) | 753.3B (safetensors); ctx 1M | 31.7 | **~30.1** | **~51%** | × 0.95 (B: abliteration (patch), nagy MoE) | Abliteration (huihui patch-GGUF az unsloth kvantra) | 8.5 | 7.5 | nincs mérés | 1 | 216.7 GB – 216.7 GB | T2: `huihui-ai/Huihui-GLM-5.3-abliterated-GGUF` ['*UD-IQ1_S*'] (216.7 GB) | other (glm-5.3) |
| 3 | **[huihui-ai/Huihui-Qwen3.8-Flash-Next-abliterated-v2-GGUF](https://huggingface.co/huihui-ai/Huihui-Qwen3.8-Flash-Next-abliterated-v2-GGUF)** | `Qwen/Qwen3.8-Flash-Next` (2026-08-24) | 125B, ebből 6B aktív + 51B n-gram embedding + | 28.6 | **~27.2** | **~46%** | × 0.95 (B: abliteration v2, nagy MoE) | Abliteration v2 (huihui) | 9 | 8.5 | nincs mérés (Qwen3.8 még nincs az UGI-n) | 9 | 68.2 GB – 188.2 GB | T3: `huihui-ai/Huihui-Qwen3.8-Flash-Next-abliterated-v2-GGUF` ['*unsloth-UD-IQ4_XS*'] (93.7 GB) | other (qwen-community-1.0) |
| 4 | **[orcarouter/MiniMax-M3.1-Flash-abliterated-GGUF](https://huggingface.co/orcarouter/MiniMax-M3.1-Flash-abliterated-GGUF)** | `MiniMaxAI/MiniMax-M3.1-Flash` (2026-10-17) | kb. 428B / 23B active (kártya); ctx 1M | 29.1 | **~27.1** | **~46%** | × 0.93 (B: közösségi abliteration, nem ellenőrzött) | Abliteration (orcarouter) | 7 | 6.5 | minőség nem ellenőrzött; gated:auto | 1 | 111.9 GB – 111.9 GB | T3: `orcarouter/MiniMax-M3.1-Flash-abliterated-GGUF` ['*Mix-128G*'] (111.9 GB) | other (minimax-community) |
| 5 | **[huihui-ai/Huihui-GLM-5.3-Flash-abliterated-GGUF](https://huggingface.co/huihui-ai/Huihui-GLM-5.3-Flash-abliterated-GGUF)** | `zai-org/GLM-5.3-Flash` (2026-08-25) | 320B total / 18B active (kártya); VL; ctx 1M | 27.8 | **~26.4** | **~45%** | × 0.95 (B: abliteration, nagy MoE) | Abliteration (huihui) | 8.5 | 7.5 | nincs mérés | 10 | 93.1 GB – 291.8 GB | T3: `huihui-ai/Huihui-GLM-5.3-Flash-abliterated-GGUF` ['*UD-IQ3_XXS*'] (120.4 GB) | MIT |
| 6 | **[NousResearch/Arete-27B](https://huggingface.co/NousResearch/Arete-27B)** | `Qwen/Qwen3.8-27B` (2026-08-05) | 27.4B | ~19.0 | **~19.0** | **~32%** | × 1 (B: SFT, csak propaganda-szűrés) | SFT (propaganda-keretezés eltávolítása, az R1-1776 utódja) | 4 | 8 | NEM általános elutasítás-eltávolító; propaganda 22%→0,9% | 2 | 15.2 GB – 17.2 GB | T4: `bartowski/NousResearch_Arete-27B-GGUF` ['*IQ4_XS*'] (15.2 GB) | Apache-2.0 |
| 7 | **[huihui-ai/Huihui-Qwen3.8-27B-abliterated-GGUF](https://huggingface.co/huihui-ai/Huihui-Qwen3.8-27B-abliterated-GGUF)** | `Qwen/Qwen3.8-27B` (2026-08-05) | 27.8B dense; VL; ctx 262k → 1M | 20.1 | **~18.7** | **~32%** | × 0.93 (B: abliteration, közepes dense) | Abliteration (huihui) / Heretic-ARA (trohrbaugh) | 8.5 | 8.5 | nincs mérés | 6 | 10.9 GB – 29.1 GB | T4: `huihui-ai/Huihui-Qwen3.8-27B-abliterated-GGUF` ['*UD-IQ4_XS*'] (14.4 GB) | Apache-2.0 |
| 8 | **[Uniboshi/Kimi-K3-Abliterated-V1](https://huggingface.co/Uniboshi/Kimi-K3-Abliterated-V1)** | `moonshotai/Kimi-K3` (2026-06-13) | 2.8T total / 104B active (kártya); ctx 1M | 17.4 | **~16.2** | **~27%** | × 0.93 (B: közösségi abliteration, minőség nem ellenőrzött) | Abliteration (közösségi, Uniboshi) | 7 | 8 | minőség nem ellenőrzött; gated:auto | 1 | 1.51 TB – 1.51 TB | T1: `Uniboshi/Kimi-K3-Abliterated-V1-GGUF` ['*MXFP4_MOE*'] (1.51 TB) | other (kimi-k3) |
| 9 | **[llmfan46/Qwen3.6-35B-A3B-uncensored-heretic-GGUF](https://huggingface.co/llmfan46/Qwen3.6-35B-A3B-uncensored-heretic-GGUF)** | `Qwen/Qwen3.6-35B-A3B` (2026-04-15) | 36B MoE, 3B aktív; VL; ctx 262k | ~8.0 | **~8.0** | **~14%** | × 1 (M: NatInt 31,03→31,62 (nincs veszteség)) | Heretic (llmfan46) / Abliteration-MTP (huihui) | 10 | 8 | UGI 50,9; NatInt 31,03→31,62 (+0,6) | 2 | 16.9 GB – 21.2 GB | T4: `llmfan46/Qwen3.6-35B-A3B-uncensored-heretic-GGUF` ['*Q4_K_M*'] (21.2 GB) | Apache-2.0 |
| 10 | **[darkc0de/Mistral-Small-4-119B-2603-heretic](https://huggingface.co/darkc0de/Mistral-Small-4-119B-2603-heretic)** | `mistralai/Mistral-Small-4-119B-2603` (2026-01-23) | 119.4B MoE; VL; ctx 1M (GGUF metadata) | ~8.0 | **~7.6** | **~13%** | × 0.95 (B: heretic, MoE) | Heretic (darkc0de) | 8 | 8 | az alap is engedékeny (UGI W10 4,5) | 6 | 43.4 GB – 126.5 GB | T3: `Rioky/Mistral-Small-4-119B-2603-heretic-gguf` ['*Q4_K_S*'] (67.7 GB) | Apache-2.0 (bázis); a hereti |
| 11 | **[coder3101/gemma-4-31B-it-heretic](https://huggingface.co/coder3101/gemma-4-31B-it-heretic)** | `google/gemma-4-31B-it` (2026-03-11) | 31.3B dense; VL; ctx 256k | 4.4 | **4.1** | **7%** | × 0.939 (M: NatInt 38,91→36,53) | Heretic (coder3101 / llmfan46) | 10 | 8.5 | UGI 65,69 (legjobb 40B alatt); NatInt 38,91→36,53 (−2,4) | 4 | 16.9 GB – 25.2 GB | T4: `mradermacher/gemma-4-31B-it-heretic-GGUF` ['*IQ4_XS*'] (16.9 GB) | Apache-2.0, NEM gated |
| 12 | **[MuXodious/gpt-oss-120b-tainted-heresy](https://huggingface.co/MuXodious/gpt-oss-120b-tainted-heresy)** | `openai/gpt-oss-120b` (2025-08-04) | 116.8B; az aktív kb. 5.1B (OpenAI release, it | 3.8 | **3.6** | **6%** | × 0.958 (M: NatInt 33,68→32,25) | Heretic (MuXodious tainted-heresy / kldzj) | 8.5 | 6 | UGI 53,81; NatInt 33,68→32,25 (−1,4) | 3 | 62.2 GB – 63.4 GB | T3: `MuXodious/gpt-oss-120b-tainted-heresy-GGUF` ['*MXFP4_MoE*'] (63.4 GB) | Apache-2.0 |
| 13 | **[llmfan46/gemma-4-26B-A4B-it-ultra-uncensored-heretic-GGUF](https://huggingface.co/llmfan46/gemma-4-26B-A4B-it-ultra-uncensored-heretic-GGUF)** | `google/gemma-4-26B-A4B-it` (2026-03-11) | 25.8B MoE, kb. 4B aktív; VL | ~3.5 | **~3.5** | **~6%** | × 1 (M: NatInt 34,44→35,71 (nincs veszteség)) | Heretic, ultra (llmfan46) | 10 | 8 | UGI 52,39; NatInt 34,44→35,71 (+1,3) | 2 | 13.3 GB – 16.8 GB | T4: `llmfan46/gemma-4-26B-A4B-it-ultra-uncensored-heretic-GGUF` ['*Q4_K_M*'] (16.8 GB) | Apache-2.0 |
| 14 | **[llmfan46/gemma-4-12B-it-uncensored-heretic-GGUF](https://huggingface.co/llmfan46/gemma-4-12B-it-uncensored-heretic-GGUF)** | `google/gemma-4-12B-it` (2026-05-23) | 11.96B; any-to-any | ~3.0 | **~2.8** | **~5%** | × 0.93 (B: heretic, kis dense) | Heretic (llmfan46) / Abliteration QAT (huihui) | 9 | 8 | nincs mérés | 1 | 8.5 GB – 8.5 GB | T4: `llmfan46/gemma-4-12B-it-uncensored-heretic-GGUF` ['*Q4_K_M*'] (8.5 GB) | Apache-2.0 |
| 15 | **[coder3101/gemma-4-E4B-it-heretic](https://huggingface.co/coder3101/gemma-4-E4B-it-heretic)** | `google/gemma-4-E4B-it` (2026-03-02) | 8B összesen / kb. 4.5B effektív; any-to-any ( | ~2.5 | **~2.5** | **~4%** | × 1 (M: NatInt 18,21→18,73 (nincs veszteség)) | Heretic (coder3101 / p-e-w) | 9.5 | 7.5 | NatInt 18,21→18,73 (+0,5) | 1 | 5.3 GB – 5.3 GB | T5: `Abiray/gemma-4-E4B-it-heretic-GGUF` ['*Q4_K_M*'] (5.3 GB) | Apache-2.0 |
| 16 | **[trohrbaugh/Qwen3.5-9B-heretic-v2](https://huggingface.co/trohrbaugh/Qwen3.5-9B-heretic-v2)** | `Qwen/Qwen3.5-9B` (2026-02-27) | 9.4–9.65B; VL | ~3.0 | **~2.3** | **~4%** | × 0.781 (M: NatInt 30,98→24,2) | Heretic v2 (trohrbaugh) | 9.5 | 7.5 | NatInt 30,98→24,2 (−6,8); huihui-változat: 19,8 (−11,2) | 2 | 5.6 GB – 9.5 GB | T5: `filvyb/Qwen3.5-9B-heretic-v2-GGUF` ['*Q4_K_M*'] (5.6 GB) | Apache-2.0 |
| 17 | **[MuXodious/gpt-oss-20b-RichardErkhov-heresy](https://huggingface.co/MuXodious/gpt-oss-20b-RichardErkhov-heresy)** | `openai/gpt-oss-20b` (2025-08-04) | 20.9B MoE (az aktív kb. 3.6B, itt nem API-ból | ~2.5 | **~2.1** | **~4%** | × 0.829 (M: NatInt 27,18→22,52) | Heretic (MuXodious / p-e-w ARA) | 9.5 | 5 | UGI 46,67; NatInt 27,18→22,52 (−4,7) | 1 | 12.7 GB – 12.7 GB | T4: `MuXodious/gpt-oss-20b-RichardErkhov-heresy-GGUF` ['*MXFP4_MoE*'] (12.7 GB) | Apache-2.0 |
| 18 | **[p-e-w/Qwen3.5-4B-heretic-2.0](https://huggingface.co/p-e-w/Qwen3.5-4B-heretic-2.0)** | `Qwen/Qwen3.5-4B` (2026-02-27) | 4.5–4.66B; VL | ~2.0 | **~1.9** | **~3%** | × 0.936 (M: NatInt 23,88→22,35 (SOMPOA-változat)) | Heretic 2.0 (p-e-w) / SOMPOA (MuXodious) | 9.5 | 6.5 | SOMPOA: UGI 44,73; NatInt 23,88→22,35 (−1,5) | 4 | 2.5 GB – 4.5 GB | T5: `mradermacher/Qwen3.5-4B-heretic-2.0-GGUF` ['*Q8_0*'] (4.5 GB) | Apache-2.0 |
| 19 | **[llmfan46/gemma-4-E2B-it-ultra-uncensored-heretic-GGUF](https://huggingface.co/llmfan46/gemma-4-E2B-it-ultra-uncensored-heretic-GGUF)** | `google/gemma-4-E2B-it` (2026-03-02) | 5.1B összesen (kb. 2B effektív) | ~1.5 | **~1.4** | **~2%** | × 0.93 (B: heretic, nagyon kis modell) | Heretic, ultra (llmfan46) | 9 | 6.5 | nincs mérés | 2 | 3.4 GB – 3.6 GB | T5: `llmfan46/gemma-4-E2B-it-ultra-uncensored-heretic-GGUF` ['*Q5_K_M*'] (3.6 GB) | Apache-2.0 |

**Hogyan olvasd:**
- **Okosság:** az 1–4. hely a legokosabb, de ehhez szerver vagy nagy workstation kell.
- **Gamer PC:** a legjobb választás a 4. (Qwen3.8-Flash-Next abliterated v2, 94–111 GB) és a 6. (Qwen3.8-27B abliterated, 14–29 GB). Egyetlen videokártyán a 6. fut.
- **Laptop, telefon:** a Gemma-4 heretic változatai mért veszteség nélkül érhetők el.
- **Arete-27B:** nem általános cenzúramentesítés, csak a propaganda-keretezést távolítja el.
- **Kimi K3.1 Pro-ból nincs cenzúrázatlan változat.** A Kimi-K3 abliterated régebbi és gyengébb alapra épül (AA 17,4), a minősége nem ellenőrzött.


#### Gépigény: cenzúrázatlan modellek

A számok **becslések** az alábbi szabályokkal:
- **Memória:** fájlméret × 1,15 (KV cache ~16–32k kontextusig, futtatói overhead).
- **Hibrid MoE:** a figyelmi rétegek és a KV cache a videokártyán, a szakértők a RAM-ban (`--n-cpu-moe`).
- **Sebesség (generálás, 1 felhasználó):** tokenenként az aktív paraméterek bájtjait kell beolvasni. Képlet: tok/s ≈ 1 / (aktív bájt / (0,6 × sávszélesség) + fix többletidő). A többletidő GPU-n 5–6 ms, Macen 9, CPU-n 12, telefonon 25 ms.
- **Sávszélességek:** RTX 4090 1008 GB/s, RTX 5090 1792, M3 Ultra 819, EPYC 12 csatornás DDR5 460, otthoni PC DDR5 kétcsatornás 90, telefon LPDDR5X 70.
- **Mért adat:** nem mértem. A valós érték prompt-feldolgozáskor és hosszú kontextusnál alacsonyabb, MTP/speculative decodinggal magasabb lehet.
- **Mac:** a macOS alapból a unified memória kb. 75%-át adja a GPU-nak. Ez emelhető: `sudo sysctl iogpu.wired_limit_mb=<MB>`.

| # | Modell | Ajánlott GGUF-kvant (méret) | Archit. (aktív) | Csak GPU | Hibrid MoE (GPU+RAM) | Mac | Csak CPU | tok/s GPU | tok/s hibrid (DDR5 PC) | tok/s M3 Ultra | tok/s EPYC | tok/s telefon | Legkisebb kvant → min. memória | Egyéb formátum |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **DeepSeek-V4.1-Flash-1017 abliterated** | `*UD-IQ1_S*` 233.0 GB (1.7 bit) | MoE, 16B aktív | 268 GB VRAM (pl. 4×80 GB) | 32 GB VRAM + 244 GB RAM | 281 GB unified | 276 GB RAM | – | ~21 | ~63 | ~41 | – | `*UD-IQ1_S*` 233.0 GB → 268 GB | MLX: 422.6 GB (4.5 bit); szerver (vLLM/SGLang): 510.3 GB (8.5 bit) |
| 2 | **GLM-5.3 abliterated** | `*UD-IQ1_S*` 216.7 GB (1.7 bit) | MoE, 40B aktív | 249 GB VRAM (pl. 4×80 GB) | 32 GB VRAM + 225 GB RAM | 262 GB unified | 257 GB RAM | – | ~9 | ~38 | ~23 | – | `*UD-IQ1_S*` 216.7 GB → 249 GB | – |
| 3 | **MiniMax-M3.1-Flash abliterated** | `*Mix-128G*` 111.9 GB (4.5 bit) | MoE, 23B aktív | 129 GB VRAM (pl. 2×80 GB) | 19 GB VRAM + 117 GB RAM | 135 GB unified | 137 GB RAM | – | ~6 | ~28 | ~17 | – | `*Mix-128G*` 111.9 GB → 129 GB | – |
| 4 | **Qwen3.8-Flash-Next abliterated v2** | `*unsloth-UD-Q4_K_XL*` 111.3 GB (4.5 bit) | MoE, 6B aktív | 128 GB VRAM (pl. 2×80 GB) | 19 GB VRAM + 117 GB RAM | 134 GB unified | 136 GB RAM | – | ~21 | ~63 | ~41 | – | `*Swift*` 68.2 GB → 78 GB | MLX: 128.6 GB (5.5 bit) |
| 5 | **GLM-5.3-Flash abliterated** | `*UD-Q4_K_XL*` 199.7 GB (4.5 bit) | MoE, 18B aktív | 230 GB VRAM (pl. 3×80 GB) | 30 GB VRAM + 208 GB RAM | 241 GB unified | 238 GB RAM | – | ~8 | ~34 | ~21 | – | `*UD-IQ1_S*` 93.1 GB → 107 GB | MLX: 185.9 GB (4.5 bit) |
| 6 | **Qwen3.8-27B abliterated** | `*UD-DW-Q4_K_M*` 16.6 GB (4.5 bit) | dense, 27.8B aktív | 19 GB VRAM (1 kártya) | dense: nem ajánlott (lassú) | 20 GB unified | 27 GB RAM | ~31 | – | ~24 | ~15 | – | `*Q2_K*` 10.9 GB → 12 GB | MLX: 19.8 GB (4.5 bit) |
| 7 | **NousResearch Arete-27B** | `*Q4_K_M*` 17.2 GB (4.5 bit) | dense, 27.4B aktív | 20 GB VRAM (1 kártya) | dense: nem ajánlott (lassú) | 21 GB unified | 28 GB RAM | ~32 | – | ~25 | ~15 | – | `*IQ4_XS*` 15.2 GB → 18 GB | – |
| 8 | **Kimi-K3 Abliterated V1** | `*MXFP4_MOE*` 1.51 TB (4.5 bit) | MoE, 104B aktív | 1735 GB VRAM (pl. 22×80 GB) | 32 GB VRAM + 1711 GB RAM | 1821 GB unified (2× Mac, exo) | 1743 GB RAM | – | ~1.5 | ~5 (2× Mac) | ~4 | – | `*MXFP4_MOE*` 1.51 TB → 1735 GB | – |
| 9 | **Qwen3.6-35B-A3B uncensored-heretic** | `*Q4_K_M*` 21.2 GB (4.5 bit) | MoE, 3B aktív | 24 GB VRAM (1 kártya) | 12 GB VRAM + 20 GB RAM | 26 GB unified | 32 GB RAM | ~152 (5090) | ~37 | ~80 | ~55 | – | `*Q3_K_M*` 16.9 GB → 19 GB | – |
| 10 | **Mistral-Small-4-119B-2603 heretic** | `*Q4_K_M*` 72.2 GB (4.5 bit) | MoE, ?B aktív | 83 GB VRAM (pl. 2×80 GB) | 15 GB VRAM + 76 GB RAM | 87 GB unified | 91 GB RAM | – | – | – | – | – | `*Q2_K*` 43.4 GB → 50 GB | – |
| 11 | **gemma-4-31B-it heretic** | `*Q4_K_M*` 18.7 GB (4.5 bit) | dense, 31.3B aktív | 21 GB VRAM (1 kártya) | dense: nem ajánlott (lassú) | 23 GB unified | 29 GB RAM | ~28 | – | ~22 | ~13 | – | `*IQ4_XS*` 16.9 GB → 19 GB | MLX: 17.3 GB (4.5 bit) |
| 12 | **gpt-oss-120b heretic** | `*MXFP4_MoE*` 63.4 GB (4.5 bit) | MoE, 5.1B aktív | 73 GB VRAM (pl. 1×80 GB) | 14 GB VRAM + 67 GB RAM | 77 GB unified | 81 GB RAM | – | ~25 | ~67 | ~45 | – | `*MXFP4_MoE*` 63.4 GB → 73 GB | MLX: 62.2 GB (4.5 bit) |
| 13 | **gemma-4-26B-A4B-it ultra-uncensored-heretic** | `*Q4_K_M*` 16.8 GB (4.5 bit) | MoE, 4B aktív | 19 GB VRAM (1 kártya) | 12 GB VRAM + 15 GB RAM | 20 GB unified | 27 GB RAM | ~103 | ~30 | ~74 | ~50 | – | `*Q3_K_M*` 13.3 GB → 15 GB | – |
| 14 | **Qwen3.5-9B heretic-v2** | `*Q4_K_M*` 5.6 GB (4.5 bit) | dense, 9.5B aktív | 6 GB VRAM (1 kártya) | dense: nem ajánlott (lassú) | 16 GB unified | 14 GB RAM | ~67 | – | ~50 | ~32 | ~7 | `*Q4_K_M*` 5.6 GB → 6 GB | – |
| 15 | **gemma-4-12B-it uncensored-heretic** | `*Q4_K_M*` 8.5 GB (4.5 bit) | dense, 12B aktív | 10 GB VRAM (1 kártya) | dense: nem ajánlott (lassú) | 16 GB unified | 18 GB RAM | ~58 | – | ~44 | ~27 | ~5 | `*Q4_K_M*` 8.5 GB → 10 GB | – |
| 16 | **gpt-oss-20b heretic** | `*MXFP4_MoE*` 12.7 GB (4.5 bit) | MoE, 3.6B aktív | 15 GB VRAM (1 kártya) | 12 GB VRAM + 11 GB RAM | 16 GB unified | 23 GB RAM | ~107 | ~32 | ~76 | ~52 | – | `*MXFP4_MoE*` 12.7 GB → 15 GB | – |
| 17 | **gemma-4-E4B-it heretic** | `*Q4_K_M*` 5.3 GB (4.5 bit) | dense, 4.5B aktív | 6 GB VRAM (1 kártya) | dense: nem ajánlott (lassú) | 16 GB unified | 14 GB RAM | ~98 | – | ~71 | ~47 | ~12 | `*Q4_K_M*` 5.3 GB → 6 GB | – |
| 18 | **Qwen3.5-4B heretic-2.0** | `*Q4_K_M*` 2.7 GB (4.5 bit) | dense, 4.6B aktív | 3 GB VRAM (1 kártya) | dense: nem ajánlott (lassú) | 16 GB unified | 11 GB RAM | ~97 | – | ~70 | ~47 | ~12 | `*IQ4_XS*` 2.5 GB → 3 GB | – |
| 19 | **gemma-4-E2B-it ultra-uncensored-heretic** | `*Q4_K_M*` 3.4 GB (4.5 bit) | dense, 2B aktív | 4 GB VRAM (1 kártya) | dense: nem ajánlott (lassú) | 16 GB unified | 12 GB RAM | ~127 | – | ~89 | ~62 | ~19 | `*Q4_K_M*` 3.4 GB → 4 GB | – |

**Gyakorlati gépkonfigurációk:**

| Gép | Memória | Mi fut rajta jól (cenzúrázatlan) |
|---|---|---|
| Telefon 8 GB | ~5 GB használható | Qwen3.5-4B heretic Q4_K_M (2,7 GB), Gemma-4-E2B heretic (3,4 GB) |
| Telefon 12–16 GB | ~8–10 GB | Gemma-4-E4B heretic (5,3 GB), Qwen3.5-9B heretic Q4 (5,6 GB), Gemma-4-12B heretic (8,5 GB, 16 GB-on) |
| Laptop 16 GB RAM + 8 GB VRAM | 24 GB | Gemma-4-26B-A4B heretic Q3_K_M (13,3 GB, MoE, gyors), gpt-oss-20b heresy (12,7 GB) |
| MacBook 36–48 GB | 27–36 GB a GPU-nak | Gemma-4-31B heretic IQ4_XS (16,9 GB), Qwen3.8-27B abliterated Q4 (16,6 GB), Qwen3.6-35B-A3B heretic (21 GB) |
| Gamer PC 24 GB VRAM + 64 GB RAM | 88 GB | Qwen3.8-27B abliterated Q6_K (22,4 GB, csak GPU), gpt-oss-120b heresy (63 GB, hibrid) |
| Gamer PC 24–32 GB VRAM + 128 GB RAM | 152–160 GB | **Qwen3.8-Flash-Next abliterated v2 UD-IQ4_XS / UD-Q4_K_XL (94–111 GB, hibrid, 6B aktív → gyors)**; MiniMax-M3.1 abliterated (112 GB) |
| Gamer PC 32 GB VRAM + 192 GB RAM | 224 GB | Qwen3.8-Flash-Next abliterated Q8_0 (188 GB) vagy GLM-5.3-Flash abliterated UD-Q4_K_XL (200 GB) |
| Mac Studio 256 GB | ~240 GB (sysctl után) | GLM-5.3-Flash abliterated UD-Q4_K_XL (200 GB), Qwen3.8-Flash-Next abliterated Q8_0 (188 GB) |
| Mac Studio 512 GB | ~490 GB | **DeepSeek-V4.1-Flash abliterated MLX (423 GB)**, GLM-5.3 abliterated (217 GB) |
| EPYC 768 GB RAM + 1–2 GPU | 768+ GB | DeepSeek-V4.1-Flash heretic Q8_0 (508 GB), ik_llama.cpp vagy KTransformers |
| 8×H100 (640 GB VRAM) | 640 GB | DeepSeek-V4.1-Flash abliterated FP8 (510 GB, vLLM/SGLang, a leggyorsabb) |
| ≥1,6 TB RAM szerver | 1,6 TB+ | Kimi-K3 abliterated MXFP4 (1,51 TB); gyengébb, mint a DeepSeek-V4.1 |


### 6.6 Futtatókörnyezetek (runtime-ok)

| Runtime | Repó / forrás | Verzió | HW-szint | Megjegyzés |
|---|---|---|---|---|
| **llama.cpp** | https://github.com/ggml-org/llama.cpp | b12387 (legutolsó nightly tag); v1.0.0 'release' 2 | T1, T2, T3, T4, T5(Termux) | Forrásból ellenőrzött flagek: -ngl/--n-gpu-layers, -ncmoe/--n-cpu-moe, -cmoe/--cpu-moe, -ot/--override-tensor, --jinja (default: enabled), -fa/--flash-attn [on\ |
| **ik_llama.cpp** | https://github.com/ikawrakow/ik_llama.cpp | nincs release tag (csak 't0002'); HEAD 2026-11-14; | T1, T2, T3 | Flagek forrásból ellenőrizve: -rtr, -mla, -amb, -ot, --n-cpu-moe, -ger, --jinja, -fa, -ctk, -sm. A -fmoe nem található (valószínűleg default lett, unverified).  |
| **Ollama** | https://github.com/ollama/ollama | v0.40.16 stable (v0.40.17-rc0) | T3, T4 | A docs/import.mdx-ben ellenőrizve: FROM .gguf és a split wildcard. A vision mmproj és a legújabb architektúrák támogatása gyakran késik a llama.cpp-hez képest. |
| **LM Studio (+ llmster headless, lms CLI)** | https://lmstudio.ai (zárt forrás); CLI: https://github.com/lmstudio-ai/lms | 0.4.28 (lmstudio.ai/download) | T3, T4 | Mac-en MLX és GGUF backend. |
| **KTransformers (kt-kernel + SGLang)** | https://github.com/kvcache-ai/ktransformers | v0.7.2 (PyPI 2026-10-15) | T1, T2, T3 | Natív támogatás: DeepSeek-V4-Flash, GLM-5.3-Flash (FP8 kb. 306 GiB, legalább 350 GB RAM), MiniMax-M3, Kimi K2.x. Az abliterated safetensors (mrfakename/pqhaz De |
| **vLLM** | https://github.com/vllm-project/vllm | 0.33.0 (PyPI 2026-11-02); rc v0.34.0rc4 | T1 | A CLI-t nem ellenőriztem a forrásból (ismert használat). Safetensors/FP8 kell (pl. mrfakename DeepSeek-V4.1 abliterated 510 GB). |
| **SGLang** | https://github.com/sgl-project/sglang | v0.5.23 (PyPI 2026-10-30) | T1 |  |
| **MLX-LM (+ mlx.distributed)** | https://github.com/ml-explore/mlx-lm | mlx-lm 0.32.2 (PyPI 2026-10-16), mlx v0.32.4 | T2, T4 | A jaccl backend RDMA over Thunderbolt 5-öt használ (lásd exo: macOS 26.2+). Ellenőrizve a mlx-lm/examples/sharded_generate.py-ban. |
| **exo** | https://github.com/exo-explore/exo | v1.0.71 (EXO-1.0.71.dmg 394 MB) | T2 | Tensor parallel RDMA TB5-ön (macOS 26.2+). Mac és Linux nem csatlakozik egymáshoz (eltérő MLX build). |
| **llamafile** | https://github.com/mozilla-ai/llamafile (a Mozilla-Ocho/llamafile ugyanaz a HEAD) | 0.10.6 | T3, T4 | Egyetlen fájl, minden OS-en fut, ezért archívumba ideális. A Windows 4 GB-os exe-limitje miatt a GGUF-ot külön -m-mel add meg. |
| **Jan** | https://github.com/janhq/jan | v0.8.8 | T3, T4 |  |
| **Open WebUI** | https://github.com/open-webui/open-webui | v0.13.3 (PyPI 2026-11-08), Python 3.11–3.12 | T1, T2, T3, T4 | Az env változók nevét a backend/open_webui/env.py és config.py forrásban ellenőriztem. Knowledge → dokumentumok feltöltése → #knowledge a chatben. |
| **AnythingLLM** | https://github.com/Mintplex-Labs/anything-llm | v1.19.0 | T3, T4 | Desktop app beépített RAG-gal és workspace-ekkel; a release asset-eket nem ellenőriztem. |
| **KoboldCpp** | https://github.com/LostRuins/koboldcpp | v1.124.2 | T3, T4 | Egyetlen bináris, kiváló offline; GGUF + whisper + TTS + képgenerálás. |
| **PocketPal AI** | https://github.com/a-ghorbani/pocketpal-ai | v1.23.0 (app-prod-release.apk 263 MB) | T5 |  |
| **MLC LLM / MLC Chat** | https://github.com/mlc-ai/mlc-llm | tag v0.26.dev0 | T5, T4 | Saját (MLC) formátumot használ, nem GGUF-ot; a modelleket előre le kell fordítani vagy letölteni. |
| **Google AI Edge Gallery** | https://github.com/google-ai-edge/gallery | 1.0.23 | T5 | LiteRT-LM (.litertlm) modelleket futtat (pl. litert-community/...), GGUF-ot nem; Gemma 4 E2B/E4B mobil QAT. |
| **ChatterUI** | https://github.com/Vali-98/ChatterUI | v0.11.0-beta1 (ChatterUI_ChatterUI_v0.11.0-beta1.a | T5 | Android, llama.cpp alapú, helyi GGUF-ot futtat. |
| **LLMFarm (iOS/macOS)** | https://github.com/guinmoon/LLMFarm | tag 1.4.3 | T5 | Az App Store/TestFlight elérhetőség unverified. |
| **Locally AI (iOS/macOS, MLX) és Apollo (Liquid AI, iOS)** | zárt forrás, csak App Store |  | T5 | Forrás: web search (App Store oldalak). Locally AI: iOS 18+, MLX, offline a modell letöltése után. Apollo: iOS 17.6+, LEAP/LFM modellek, saját szerverhez is kap |
| **Heretic (decensoring tool)** | https://github.com/p-e-w/heretic | v2.1.0 / PyPI heretic-llm 2.1.0 | T3 (≤30B bnb_4bit), T1/T2 (nagy modellek) |  |
| **Kiwix + LLM** | kiwix-tools: https://github.com/kiwix/kiwix-tools (3.8.2); MCP: https://github.com/cameron |  |  | A WikiChat saját indexet épít (nehéz). Az Open WebUI MCP vagy OpenAPI tool integrációját nem ellenőriztem. |

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

### 6.10 Eszköz-kalkulátor: mi a legokosabb, ami elfér és elfut (4 változat)

A `llm_calc.py` (11. fejezet után, a **12. fejezetben**) bármely eszközre kiszámolja a négy változatot:
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

**Saját eszközre:**
```bash
sed -n '/^```python llm_calc.py$/,/^```$/p' ARCHIVUM.md | sed '1d;$d' > llm_calc.py
python3 llm_calc.py ARCHIVUM.md --name "Saját PC" --gpu 24:1008 --ram 128 --ram-bw 90 --formats any,server --md
python3 llm_calc.py ARCHIVUM.md --name "Mac Studio" --unified 512 --unified-usable 0.92 --unified-bw 819 --formats any,mac
python3 llm_calc.py ARCHIVUM.md --preset all --md      # minden alábbi profil
```

**Hardveradatok és feltételezések:**
- **MS-S1 MAX-P495 és ZBook Ultra G3a:** 192 GB LPDDR5X; a GPU-nak legfeljebb 160 GB adható (gyártói adat). A ~256–273 GB/s sávszélességet a memóriasebességből és a 256 bites buszból számoltam.
- **RTX 6090:** még nincs bejelentve. A pletykák szerint 32 GB GDDR7 és ~1,79 TB/s.
- **Következő generációs RTX Pro:** semmilyen hivatalos adat nincs róla, ezért három forgatókönyvvel számolok: 96, 128 és 192 GB.
- **Pavilion 15-bc504ur:** az i5-9300H + GTX 1050 4 GB a bc504TX testvérmodell adatlapjából jön.
- **Telefonok:** a modellnek jutó memória becslés (az OS és az appok levonva).
- **Klaszter (2 vagy 4 MS-S1):** llama.cpp RPC vagy exo pipeline-párhuzamosítás USB4 v2 (80 Gbps) gyűrűn. A kapacitás összeadódik, a sebesség nagyjából egy gépé, plusz ~3 ms hálózati késleltetés gépenként.

#### Telefonok

#### Samsung Galaxy S24 Ultra (12 GB, Snapdragon 8 Gen 3)

*Modellnek jutó memória: ~7 GB · Android: PocketPal / ChatterUI (GGUF). Kb. 7,5 GB jut a modellnek. Sávszélesség ~68 GB/s (LPDDR5X, becslés).*

| Változat | Modell(ek) – kvant, méret, becsült sebesség, elhelyezés, letöltés |
|---|---|
| **V1 legokosabb cenzúrázatlan** | gemma-4-E4B-it heretic (coder3101; GGUF Abiray) / ultra-uncensored (llmfan46) [AA v5 ~2.5 = ~4% Opus 5.5 · 4.5 bit, 5.3 GB, ~11 tok/s, unified] – egyedül – `Abiray/gemma-4-E4B-it-heretic-GGUF *Q4_K_M*` |
| **V2 legokosabb alap (cenzúrázott)** | Qwen3.5-4B / Qwen3.5-9B (+ MiMo-V2.6-Distill-Qwen-9B) [AA v5 ~3.0 = ~5% Opus 5.5 · 8.5 bit, 4.5 GB, ~7 tok/s, unified] – egyedül – `unsloth/Qwen3.5-4B-GGUF *Q8_0*` |
| **V3 csapat (alap modellek)** | Qwen3.5-4B / Qwen3.5-9B (+ MiMo-V2.6-Distill-Qwen-9B) [AA v5 ~3.0 = ~5% Opus 5.5 · 8.5 bit, 4.5 GB, ~7 tok/s, unified] – fő modell (váltva) – `unsloth/Qwen3.5-4B-GGUF *Q8_0*`<br>Gemma 4 (31B, 26B-A4B, 12B, E4B, E2B) [AA v5 ~1.5 = ~3% Opus 5.5 · 4.5 bit, 3.1 GB, ~19 tok/s, unified] – gyors segéd, váltva – egyszerre csak egy fér a memóriába, a tárhelyen mindkettő ott van – `unsloth/gemma-4-E2B-it-GGUF *Q4_K_M*`<br>+ RAG-embedding: `gpustack/bge-m3-GGUF *Q8_0*` (0,6 GB). Összesen ~12 GB |
| **V4 vegyes csapat (alap + cenzúrázatlan)** | Qwen3.5-4B / Qwen3.5-9B (+ MiMo-V2.6-Distill-Qwen-9B) [AA v5 ~3.0 = ~5% Opus 5.5 · 8.5 bit, 4.5 GB, ~7 tok/s, unified] – fő modell (váltva) – `unsloth/Qwen3.5-4B-GGUF *Q8_0*`<br>gemma-4-E4B-it heretic (coder3101; GGUF Abiray) / ultra-uncensored (llmfan46) [AA v5 ~2.5 = ~4% Opus 5.5 · 4.5 bit, 5.3 GB, ~11 tok/s, unified] – partner, váltva – egyszerre csak egy fér a memóriába, a tárhelyen mindkettő ott van – `Abiray/gemma-4-E4B-it-heretic-GGUF *Q4_K_M*`<br>+ RAG-embedding: `gpustack/bge-m3-GGUF *Q8_0*` (0,6 GB). Összesen ~14 GB |

#### iPhone 15 Pro (8 GB, A17 Pro)

*Modellnek jutó memória: ~5 GB · iOS: PocketPal / LLM Farm (GGUF), Locally AI (MLX). Kb. 5 GB jut a modellnek (iOS app-memórialimit).*

| Változat | Modell(ek) – kvant, méret, becsült sebesség, elhelyezés, letöltés |
|---|---|
| **V1 legokosabb cenzúrázatlan** | Qwen3.5-4B heretic-2.0 (p-e-w) / SOMPOA-heresy-v2 (MuXodious) [AA v5 ~1.9 = ~3% Opus 5.5 · 4.5 bit, 2.5 GB, ~9 tok/s, unified] – egyedül – `mradermacher/Qwen3.5-4B-heretic-2.0-GGUF *IQ4_XS*` |
| **V2 legokosabb alap (cenzúrázott)** | Qwen3.5-4B / Qwen3.5-9B (+ MiMo-V2.6-Distill-Qwen-9B) [AA v5 ~2.0 = ~3% Opus 5.5 · 4.5 bit, 2.7 GB, ~9 tok/s, unified] – egyedül – `unsloth/Qwen3.5-4B-GGUF *Q4_K_M*` |
| **V3 csapat (alap modellek)** | Qwen3.5-4B / Qwen3.5-9B (+ MiMo-V2.6-Distill-Qwen-9B) [AA v5 ~2.0 = ~3% Opus 5.5 · 4.5 bit, 2.7 GB, ~9 tok/s, unified] – fő modell (váltva) – `unsloth/Qwen3.5-4B-GGUF *Q4_K_M*`<br>Gemma 4 (31B, 26B-A4B, 12B, E4B, E2B) [AA v5 ~1.5 = ~3% Opus 5.5 · 4.5 bit, 3.1 GB, ~16 tok/s, unified] – gyors segéd, váltva – egyszerre csak egy fér a memóriába, a tárhelyen mindkettő ott van – `unsloth/gemma-4-E2B-it-GGUF *Q4_K_M*`<br>+ RAG-embedding: `gpustack/bge-m3-GGUF *Q8_0*` (0,6 GB). Összesen ~10 GB |
| **V4 vegyes csapat (alap + cenzúrázatlan)** | Qwen3.5-4B / Qwen3.5-9B (+ MiMo-V2.6-Distill-Qwen-9B) [AA v5 ~2.0 = ~3% Opus 5.5 · 4.5 bit, 2.7 GB, ~9 tok/s, unified] – fő modell (váltva) – `unsloth/Qwen3.5-4B-GGUF *Q4_K_M*`<br>Qwen3.5-4B heretic-2.0 (p-e-w) / SOMPOA-heresy-v2 (MuXodious) [AA v5 ~1.9 = ~3% Opus 5.5 · 4.5 bit, 2.5 GB, ~9 tok/s, unified] – partner, váltva – egyszerre csak egy fér a memóriába, a tárhelyen mindkettő ott van – `mradermacher/Qwen3.5-4B-heretic-2.0-GGUF *IQ4_XS*`<br>+ RAG-embedding: `gpustack/bge-m3-GGUF *Q8_0*` (0,6 GB). Összesen ~9 GB |

#### Laptopok

#### HP Pavilion 15-bc504ur (8 GB DDR4, GTX 1050 4 GB) – mostani

*Modellnek jutó memória: ~9 GB · i5-9300H + GTX 1050 4 GB (a bc504TX testvérmodell adatai alapján). Egycsatornás DDR4-2666 ~21 GB/s.*

| Változat | Modell(ek) – kvant, méret, becsült sebesség, elhelyezés, letöltés |
|---|---|
| **V1 legokosabb cenzúrázatlan** | gemma-4-E4B-it heretic (coder3101; GGUF Abiray) / ultra-uncensored (llmfan46) [AA v5 ~2.5 = ~4% Opus 5.5 · 4.5 bit, 5.3 GB, ~6 tok/s, hibrid GPU+RAM (dense)] – egyedül – `Abiray/gemma-4-E4B-it-heretic-GGUF *Q4_K_M*` |
| **V2 legokosabb alap (cenzúrázott)** | NVIDIA Nemotron 3.5 (Super-VL-120B-A12B, Lightning-30B-A3B, Bolt-E4B) [AA v5 ~2.5 = ~4% Opus 5.5 · 4.5 bit, 5.1 GB, ~7 tok/s, hibrid GPU+RAM (dense)] – egyedül – `unsloth/NVIDIA-Nemotron-3.5-Bolt-E4B-GGUF *UD-Q4_K_XL*`<br>Gemma 4 (31B, 26B-A4B, 12B, E4B, E2B) [AA v5 ~2.5 = ~4% Opus 5.5 · 6.5 bit, 6.2 GB, ~4 tok/s, hibrid GPU+RAM (dense)] – közel azonos alternatíva – `lmstudio-community/gemma-4-E4B-it-GGUF *Q6_K*`<br>+ RAG-embedding: `gpustack/bge-m3-GGUF *Q8_0*` (0,6 GB). Összesen ~16 GB |
| **V3 csapat (alap modellek)** | Gemma 4 (31B, 26B-A4B, 12B, E4B, E2B) [AA v5 ~1.5 = ~3% Opus 5.5 · 2.6 bit, 2.3 GB, ~41 tok/s, csak GPU] – fő modell – `unsloth/gemma-4-E2B-it-GGUF *UD-IQ2_M*`<br>Qwen3.5-4B / Qwen3.5-9B (+ MiMo-V2.6-Distill-Qwen-9B) [AA v5 ~2.0 = ~3% Opus 5.5 · 3.5 bit, 2.4 GB, ~22 tok/s, csak GPU] – gyors segéd / router – `unsloth/Qwen3.5-4B-GGUF *UD-Q3_K_XL*`<br>+ RAG-embedding: `gpustack/bge-m3-GGUF *Q8_0*` (0,6 GB). Összesen ~8 GB |
| **V4 vegyes csapat (alap + cenzúrázatlan)** | Qwen3.5-4B heretic-2.0 (p-e-w) / SOMPOA-heresy-v2 (MuXodious) [AA v5 ~1.9 = ~3% Opus 5.5 · 4.5 bit, 2.5 GB, ~19 tok/s, csak GPU] – fő modell – `mradermacher/Qwen3.5-4B-heretic-2.0-GGUF *IQ4_XS*`<br>Qwen3.5-4B / Qwen3.5-9B (+ MiMo-V2.6-Distill-Qwen-9B) [AA v5 ~2.0 = ~3% Opus 5.5 · 3.5 bit, 2.4 GB, ~22 tok/s, csak GPU] – partner (alap) – `unsloth/Qwen3.5-4B-GGUF *UD-Q3_K_XL*`<br>+ RAG-embedding: `gpustack/bge-m3-GGUF *Q8_0*` (0,6 GB). Összesen ~9 GB |

#### HP Pavilion 15-bc504ur (16 GB DDR4 dual channel, GTX 1050 4 GB)

*Modellnek jutó memória: ~16 GB · +8 GB → kétcsatornás DDR4-2666 ~42 GB/s. A gyors SSD a modell betöltését gyorsítja, a futást nem.*

| Változat | Modell(ek) – kvant, méret, becsült sebesség, elhelyezés, letöltés |
|---|---|
| **V1 legokosabb cenzúrázatlan** | gemma-4-E4B-it heretic (coder3101; GGUF Abiray) / ultra-uncensored (llmfan46) [AA v5 ~2.5 = ~4% Opus 5.5 · 4.5 bit, 5.3 GB, ~10 tok/s, hibrid GPU+RAM (dense)] – egyedül – `Abiray/gemma-4-E4B-it-heretic-GGUF *Q4_K_M*` |
| **V2 legokosabb alap (cenzúrázott)** | Gemma 4 (31B, 26B-A4B, 12B, E4B, E2B) [AA v5 ~3.5 = ~6% Opus 5.5 · 3.5 bit, 12.9 GB, ~15 tok/s, hibrid GPU+RAM] – egyedül – `unsloth/gemma-4-26B-A4B-it-GGUF *UD-Q3_K_XL*` |
| **V3 csapat (alap modellek)** | Gemma 4 (31B, 26B-A4B, 12B, E4B, E2B) [AA v5 ~3.0 = ~5% Opus 5.5 · 4.5 bit, 7.0 GB, ~4 tok/s, hibrid GPU+RAM (dense)] – fő modell – `google/gemma-4-12B-it-qat-q4_0-gguf *q4_0*`<br>Qwen3.5-4B / Qwen3.5-9B (+ MiMo-V2.6-Distill-Qwen-9B) [AA v5 ~2.0 = ~3% Opus 5.5 · 4.5 bit, 2.7 GB, ~12 tok/s, hibrid GPU+RAM (dense)] – gyors segéd / router – `unsloth/Qwen3.5-4B-GGUF *Q4_K_M*`<br>+ RAG-embedding: `gpustack/bge-m3-GGUF *Q8_0*` (0,6 GB). Összesen ~14 GB |
| **V4 vegyes csapat (alap + cenzúrázatlan)** | Qwen3.5-4B / Qwen3.5-9B (+ MiMo-V2.6-Distill-Qwen-9B) [AA v5 ~3.0 = ~5% Opus 5.5 · 8.5 bit, 4.5 GB, ~6 tok/s, hibrid GPU+RAM (dense)] – fő modell – `unsloth/Qwen3.5-4B-GGUF *Q8_0*`<br>gemma-4-E4B-it heretic (coder3101; GGUF Abiray) / ultra-uncensored (llmfan46) [AA v5 ~2.5 = ~4% Opus 5.5 · 4.5 bit, 5.3 GB, ~10 tok/s, hibrid GPU+RAM (dense)] – partner (cenzúrázatlan) – `Abiray/gemma-4-E4B-it-heretic-GGUF *Q4_K_M*`<br>+ RAG-embedding: `gpustack/bge-m3-GGUF *Q8_0*` (0,6 GB). Összesen ~14 GB |

#### HP ZBook Ultra G3a (192 GB unified, Ryzen AI Max+ PRO 495)

*Modellnek jutó memória: ~159 GB · A GPU-nak max. 160 GB adható (HP). LPDDR5X-8000 × 256 bit ≈ 256 GB/s (számolt). Linux + llama.cpp Vulkan/ROCm ajánlott.*

| Változat | Modell(ek) – kvant, méret, becsült sebesség, elhelyezés, letöltés |
|---|---|
| **V1 legokosabb cenzúrázatlan** | Qwen3.8-Flash-Next abliterated v2 (huihui GGUF) [AA v5 ~27.2 = ~46% Opus 5.5 · 4.5 bit, 93.7 GB, ~31 tok/s, unified] – egyedül – `huihui-ai/Huihui-Qwen3.8-Flash-Next-abliterated-v2-GGUF *unsloth-UD-IQ4_XS*` |
| **V2 legokosabb alap (cenzúrázott)** | Qwen3.8-Flash-Next [AA v5 28.6 = 48% Opus 5.5 · 5.5 bit, 134.1 GB, ~27 tok/s, unified] – egyedül – `mradermacher/Qwen3.8-Flash-Next-i1-GGUF *i1-Q5_K_M*` |
| **V3 csapat (alap modellek)** | Qwen3.8-Flash-Next [AA v5 28.6 = 48% Opus 5.5 · 4.5 bit, 97.5 GB, ~31 tok/s, unified] – fő modell – `mradermacher/Qwen3.8-Flash-Next-i1-GGUF *i1-IQ4_XS*`<br>NVIDIA Nemotron 3.5 (Super-VL-120B-A12B, Lightning-30B-A3B, Bolt-E4B) [AA v5 5.5 = 9% Opus 5.5 · 8.5 bit, 33.6 GB, ~33 tok/s, unified] – gyors segéd / router – `ggml-org/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-GGUF *Q8_0*`<br>+ RAG-embedding: `gpustack/bge-m3-GGUF *Q8_0*` (0,6 GB). Összesen ~154 GB |
| **V4 vegyes csapat (alap + cenzúrázatlan)** | Qwen3.8-Flash-Next [AA v5 28.6 = 48% Opus 5.5 · 4.5 bit, 97.5 GB, ~31 tok/s, unified] – fő modell – `mradermacher/Qwen3.8-Flash-Next-i1-GGUF *i1-IQ4_XS*`<br>NousResearch Arete-27B (a "R1-1776 utód") [AA v5 ~19.0 = ~32% Opus 5.5 · 4.5 bit, 15.2 GB, ~9 tok/s, unified] – partner (cenzúrázatlan) – `bartowski/NousResearch_Arete-27B-GGUF *IQ4_XS*`<br>Qwen3.6-35B-A3B uncensored-heretic (llmfan46) / abliterated-MTP (huihui) [AA v5 ~8.0 = ~14% Opus 5.5 · 4.5 bit, 21.2 GB, ~48 tok/s, unified] – gyors segéd / router – `llmfan46/Qwen3.6-35B-A3B-uncensored-heretic-GGUF *Q4_K_M*`<br>+ RAG-embedding: `gpustack/bge-m3-GGUF *Q8_0*` (0,6 GB). Összesen ~158 GB |

#### AI workstation – MINISFORUM MS-S1 MAX-P495 (1, 2, 4 gép)

#### 1× MINISFORUM MS-S1 MAX-P495 (192 GB)

*Modellnek jutó memória: ~159 GB · LPDDR5X-8533 × 256 bit ≈ 273 GB/s (számolt); GPU-ra max. 160 GB.*

| Változat | Modell(ek) – kvant, méret, becsült sebesség, elhelyezés, letöltés |
|---|---|
| **V1 legokosabb cenzúrázatlan** | Qwen3.8-Flash-Next abliterated v2 (huihui GGUF) [AA v5 ~27.2 = ~46% Opus 5.5 · 4.5 bit, 93.7 GB, ~33 tok/s, unified] – egyedül – `huihui-ai/Huihui-Qwen3.8-Flash-Next-abliterated-v2-GGUF *unsloth-UD-IQ4_XS*` |
| **V2 legokosabb alap (cenzúrázott)** | Qwen3.8-Flash-Next [AA v5 28.6 = 48% Opus 5.5 · 5.5 bit, 134.1 GB, ~28 tok/s, unified] – egyedül – `mradermacher/Qwen3.8-Flash-Next-i1-GGUF *i1-Q5_K_M*` |
| **V3 csapat (alap modellek)** | Qwen3.8-Flash-Next [AA v5 28.6 = 48% Opus 5.5 · 4.5 bit, 97.5 GB, ~33 tok/s, unified] – fő modell – `mradermacher/Qwen3.8-Flash-Next-i1-GGUF *i1-IQ4_XS*`<br>NVIDIA Nemotron 3.5 (Super-VL-120B-A12B, Lightning-30B-A3B, Bolt-E4B) [AA v5 5.5 = 9% Opus 5.5 · 8.5 bit, 33.6 GB, ~34 tok/s, unified] – gyors segéd / router – `ggml-org/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-GGUF *Q8_0*`<br>+ RAG-embedding: `gpustack/bge-m3-GGUF *Q8_0*` (0,6 GB). Összesen ~154 GB |
| **V4 vegyes csapat (alap + cenzúrázatlan)** | Qwen3.8-Flash-Next [AA v5 28.6 = 48% Opus 5.5 · 4.5 bit, 97.5 GB, ~33 tok/s, unified] – fő modell – `mradermacher/Qwen3.8-Flash-Next-i1-GGUF *i1-IQ4_XS*`<br>NousResearch Arete-27B (a "R1-1776 utód") [AA v5 ~19.0 = ~32% Opus 5.5 · 4.5 bit, 15.2 GB, ~10 tok/s, unified] – partner (cenzúrázatlan) – `bartowski/NousResearch_Arete-27B-GGUF *IQ4_XS*`<br>Qwen3.6-35B-A3B uncensored-heretic (llmfan46) / abliterated-MTP (huihui) [AA v5 ~8.0 = ~14% Opus 5.5 · 4.5 bit, 21.2 GB, ~49 tok/s, unified] – gyors segéd / router – `llmfan46/Qwen3.6-35B-A3B-uncensored-heretic-GGUF *Q4_K_M*`<br>+ RAG-embedding: `gpustack/bge-m3-GGUF *Q8_0*` (0,6 GB). Összesen ~158 GB |

#### 2× MS-S1 MAX-P495 (2×192 GB, USB4 v2 80 Gbps)

*Modellnek jutó memória: ~319 GB · llama.cpp RPC / exo pipeline-párhuzamosítás: a kapacitás összeadódik, a sebesség ~1 gépé + hálózati késleltetés.*

| Változat | Modell(ek) – kvant, méret, becsült sebesség, elhelyezés, letöltés |
|---|---|
| **V1 legokosabb cenzúrázatlan** | Qwen3.8-Flash-Next abliterated v2 (huihui GGUF) [AA v5 ~27.2 = ~46% Opus 5.5 · 5.5 bit, 158.3 GB, ~26 tok/s, unified ×2] – egyedül – `huihui-ai/Huihui-Qwen3.8-Flash-Next-abliterated-v2-GGUF *UD-Q5_K_XL*` |
| **V2 legokosabb alap (cenzúrázott)** | Qwen3.8-Flash-Next [AA v5 28.6 = 48% Opus 5.5 · 5.5 bit, 134.1 GB, ~26 tok/s, unified ×2] – egyedül – `mradermacher/Qwen3.8-Flash-Next-i1-GGUF *i1-Q5_K_M*` |
| **V3 csapat (alap modellek)** | Qwen3.8-Flash-Next [AA v5 28.6 = 48% Opus 5.5 · 5.5 bit, 134.1 GB, ~26 tok/s, unified ×2] – fő modell – `mradermacher/Qwen3.8-Flash-Next-i1-GGUF *i1-Q5_K_M*`<br>NVIDIA Nemotron 3.5 (Super-VL-120B-A12B, Lightning-30B-A3B, Bolt-E4B) [AA v5 5.5 = 9% Opus 5.5 · 8.5 bit, 33.6 GB, ~31 tok/s, unified ×2] – gyors segéd / router – `ggml-org/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-GGUF *Q8_0*`<br>+ RAG-embedding: `gpustack/bge-m3-GGUF *Q8_0*` (0,6 GB). Összesen ~196 GB |
| **V4 vegyes csapat (alap + cenzúrázatlan)** | Qwen3.8-Flash-Next [AA v5 28.6 = 48% Opus 5.5 · 5.5 bit, 134.1 GB, ~26 tok/s, unified ×2] – fő modell – `mradermacher/Qwen3.8-Flash-Next-i1-GGUF *i1-Q5_K_M*`<br>MiniMax-M3.1-Flash abliterated (orcarouter GGUF) [AA v5 ~27.1 = ~46% Opus 5.5 · 4.5 bit, 111.9 GB, ~11 tok/s, unified ×2] – partner (cenzúrázatlan) – `orcarouter/MiniMax-M3.1-Flash-abliterated-GGUF *Mix-128G*`<br>Qwen3.6-35B-A3B uncensored-heretic (llmfan46) / abliterated-MTP (huihui) [AA v5 ~8.0 = ~14% Opus 5.5 · 4.5 bit, 21.2 GB, ~43 tok/s, unified ×2] – gyors segéd / router – `llmfan46/Qwen3.6-35B-A3B-uncensored-heretic-GGUF *Q4_K_M*`<br>+ RAG-embedding: `gpustack/bge-m3-GGUF *Q8_0*` (0,6 GB). Összesen ~311 GB |

#### 4× MS-S1 MAX-P495 (4×192 GB, USB4 v2 gyűrű)

*Modellnek jutó memória: ~637 GB · Gépenként 2 db USB4 v2 port → gyűrű topológia; alternatíva 2×10GbE. 640 GB GPU-memória összesen.*

| Változat | Modell(ek) – kvant, méret, becsült sebesség, elhelyezés, letöltés |
|---|---|
| **V1 legokosabb cenzúrázatlan** | DeepSeek-V4.1-Flash-1017 abliterated (huihui GGUF) / heretic (pqhaz) / abliterated (mrfakename) [AA v5 ~31.6 = ~53% Opus 5.5 · 8.5 bit, 507.9 GB, ~8 tok/s, unified ×4] – egyedül – `pqhaz/DeepSeek-V4.1-Flash-1017-heretic-GGUF *Q8_0*` |
| **V2 legokosabb alap (cenzúrázott)** | DeepSeek-V4.1-Flash-1017 [AA v5 32.6 = 55% Opus 5.5 · 8.5 bit, 508.4 GB, ~8 tok/s, unified ×4] – egyedül – `unsloth/DeepSeek-V4.1-Flash-1017-GGUF *UD-Q8_K_XL*`<br>Hy4 preview (Hunyuan) [AA v5 ~34.6 = ~59% Opus 5.5 · 4.5 bit, 467.3 GB, ~5 tok/s, unified ×4] – közel azonos alternatíva – `AngelSlim/Hy4-preview-GGUF *Q4_K_M*`<br>+ RAG-embedding: `gpustack/bge-m3-GGUF *Q8_0*` (0,6 GB). Összesen ~1125 GB |
| **V3 csapat (alap modellek)** | DeepSeek-V4.1-Flash-1017 [AA v5 32.6 = 55% Opus 5.5 · 8.5 bit, 508.4 GB, ~8 tok/s, unified ×4] – fő modell – `unsloth/DeepSeek-V4.1-Flash-1017-GGUF *UD-Q8_K_XL*`<br>NVIDIA Nemotron 3.5 (Super-VL-120B-A12B, Lightning-30B-A3B, Bolt-E4B) [AA v5 5.5 = 9% Opus 5.5 · 8.5 bit, 33.6 GB, ~26 tok/s, unified ×4] – gyors segéd / router – `ggml-org/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-GGUF *Q8_0*`<br>+ RAG-embedding: `gpustack/bge-m3-GGUF *Q8_0*` (0,6 GB). Összesen ~626 GB |
| **V4 vegyes csapat (alap + cenzúrázatlan)** | Hy4 preview (Hunyuan) [AA v5 ~34.6 = ~59% Opus 5.5 · 4.5 bit, 467.3 GB, ~5 tok/s, unified ×4] – fő modell – `AngelSlim/Hy4-preview-GGUF *Q4_K_M*`<br>Qwen3.8-Flash-Next abliterated v2 (huihui GGUF) [AA v5 ~27.2 = ~46% Opus 5.5 · 3.5 bit, 76.0 GB, ~29 tok/s, unified ×4] – partner (cenzúrázatlan) – `huihui-ai/Huihui-Qwen3.8-Flash-Next-abliterated-v2-GGUF *Swift*`<br>Qwen3.5-4B / Qwen3.5-9B (+ MiMo-V2.6-Distill-Qwen-9B) [AA v5 ~3.0 = ~5% Opus 5.5 · 8.5 bit, 4.5 GB, ~20 tok/s, unified ×4] – gyors segéd / router – `unsloth/Qwen3.5-4B-GGUF *Q8_0*`<br>+ RAG-embedding: `gpustack/bge-m3-GGUF *Q8_0*` (0,6 GB). Összesen ~634 GB |

#### Gamer PC – RTX 6090 + RAM-változatok

#### Gamer PC – RTX 6090 32 GB + 96 GB DDR5-6000

*Modellnek jutó memória: ~114 GB · RTX 6090 adatai nem hivatalosak (pletyka). 2 DIMM DDR5-6000 kétcsatornás ≈ 96 GB/s.*

| Változat | Modell(ek) – kvant, méret, becsült sebesség, elhelyezés, letöltés |
|---|---|
| **V1 legokosabb cenzúrázatlan** | Qwen3.8-Flash-Next abliterated v2 (huihui GGUF) [AA v5 ~27.2 = ~46% Opus 5.5 · 4.5 bit, 93.7 GB, ~27 tok/s, hibrid GPU+RAM] – egyedül – `huihui-ai/Huihui-Qwen3.8-Flash-Next-abliterated-v2-GGUF *unsloth-UD-IQ4_XS*` |
| **V2 legokosabb alap (cenzúrázott)** | Qwen3.8-Flash-Next [AA v5 28.6 = 48% Opus 5.5 · 4.5 bit, 85.7 GB, ~28 tok/s, hibrid GPU+RAM] – egyedül – `AesSedai/Qwen3.8-Flash-Next-GGUF *Q4_0*` |
| **V3 csapat (alap modellek)** | Qwen3.8-Flash-Next [AA v5 28.6 = 48% Opus 5.5 · 4.5 bit, 85.7 GB, ~28 tok/s, hibrid GPU+RAM] – fő modell – `AesSedai/Qwen3.8-Flash-Next-GGUF *Q4_0*`<br>Qwen3.8-27B (dense) [AA v5 20.1 = 34% Opus 5.5 · 3.5 bit, 10.1 GB, ~58 tok/s, csak GPU] – gyors segéd / router – `ISTA-DASLab/Qwen3.8-27B-GSQ-RCO-GGUF *IQ3_XXS*`<br>+ RAG-embedding: `gpustack/bge-m3-GGUF *Q8_0*` (0,6 GB). Összesen ~113 GB |
| **V4 vegyes csapat (alap + cenzúrázatlan)** | Qwen3.8-Flash-Next [AA v5 28.6 = 48% Opus 5.5 · 3.5 bit, 75.8 GB, ~35 tok/s, hibrid GPU+RAM] – fő modell – `ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF *IQ3_XXS*`<br>NousResearch Arete-27B (a "R1-1776 utód") [AA v5 ~19.0 = ~32% Opus 5.5 · 4.5 bit, 15.2 GB, ~49 tok/s, csak GPU] – partner (cenzúrázatlan) – `bartowski/NousResearch_Arete-27B-GGUF *IQ4_XS*`<br>NVIDIA Nemotron 3.5 (Super-VL-120B-A12B, Lightning-30B-A3B, Bolt-E4B) [AA v5 ~2.5 = ~4% Opus 5.5 · 3.5 bit, 4.2 GB, ~131 tok/s, csak GPU] – gyors segéd / router – `unsloth/NVIDIA-Nemotron-3.5-Bolt-E4B-GGUF *UD-Q3_K_XL*`<br>+ RAG-embedding: `gpustack/bge-m3-GGUF *Q8_0*` (0,6 GB). Összesen ~113 GB |

#### Gamer PC – RTX 6090 32 GB + 128 GB DDR5

*Modellnek jutó memória: ~143 GB · 2×64 GB, DDR5-6000 feltételezve.*

| Változat | Modell(ek) – kvant, méret, becsült sebesség, elhelyezés, letöltés |
|---|---|
| **V1 legokosabb cenzúrázatlan** | Qwen3.8-Flash-Next abliterated v2 (huihui GGUF) [AA v5 ~27.2 = ~46% Opus 5.5 · 4.5 bit, 93.7 GB, ~27 tok/s, hibrid GPU+RAM] – egyedül – `huihui-ai/Huihui-Qwen3.8-Flash-Next-abliterated-v2-GGUF *unsloth-UD-IQ4_XS*` |
| **V2 legokosabb alap (cenzúrázott)** | Qwen3.8-Flash-Next [AA v5 28.6 = 48% Opus 5.5 · 4.5 bit, 85.7 GB, ~28 tok/s, hibrid GPU+RAM] – egyedül – `AesSedai/Qwen3.8-Flash-Next-GGUF *Q4_0*` |
| **V3 csapat (alap modellek)** | Qwen3.8-Flash-Next [AA v5 28.6 = 48% Opus 5.5 · 4.5 bit, 85.7 GB, ~28 tok/s, hibrid GPU+RAM] – fő modell – `AesSedai/Qwen3.8-Flash-Next-GGUF *Q4_0*`<br>Qwen3.8-27B (dense) [AA v5 20.1 = 34% Opus 5.5 · 5.5 bit, 19.5 GB, ~42 tok/s, csak GPU] – gyors segéd / router – `mradermacher/Qwen3.8-27B-i1-GGUF *Q5_K_M*`<br>+ RAG-embedding: `gpustack/bge-m3-GGUF *Q8_0*` (0,6 GB). Összesen ~124 GB |
| **V4 vegyes csapat (alap + cenzúrázatlan)** | Qwen3.8-Flash-Next [AA v5 28.6 = 48% Opus 5.5 · 4.5 bit, 85.7 GB, ~28 tok/s, hibrid GPU+RAM] – fő modell – `AesSedai/Qwen3.8-Flash-Next-GGUF *Q4_0*`<br>NousResearch Arete-27B (a "R1-1776 utód") [AA v5 ~19.0 = ~32% Opus 5.5 · 4.5 bit, 15.2 GB, ~49 tok/s, csak GPU] – partner (cenzúrázatlan) – `bartowski/NousResearch_Arete-27B-GGUF *IQ4_XS*`<br>Qwen3.8-27B (dense) [AA v5 20.1 = 34% Opus 5.5 · 5.5 bit, 19.5 GB, ~42 tok/s, csak GPU] – gyors segéd / router – `mradermacher/Qwen3.8-27B-i1-GGUF *Q5_K_M*`<br>+ RAG-embedding: `gpustack/bge-m3-GGUF *Q8_0*` (0,6 GB). Összesen ~142 GB |

#### Gamer PC – RTX 6090 32 GB + 192 GB DDR5

*Modellnek jutó memória: ~205 GB · 4×48 GB → kb. DDR5-5400 (4 DIMM-mel lassabb) ≈ 86 GB/s.*

| Változat | Modell(ek) – kvant, méret, becsült sebesség, elhelyezés, letöltés |
|---|---|
| **V1 legokosabb cenzúrázatlan** | Qwen3.8-Flash-Next abliterated v2 (huihui GGUF) [AA v5 ~27.2 = ~46% Opus 5.5 · 5.5 bit, 158.3 GB, ~18 tok/s, hibrid GPU+RAM] – egyedül – `huihui-ai/Huihui-Qwen3.8-Flash-Next-abliterated-v2-GGUF *UD-Q5_K_XL*` |
| **V2 legokosabb alap (cenzúrázott)** | Qwen3.8-Flash-Next [AA v5 28.6 = 48% Opus 5.5 · 5.5 bit, 134.1 GB, ~19 tok/s, hibrid GPU+RAM] – egyedül – `mradermacher/Qwen3.8-Flash-Next-i1-GGUF *i1-Q5_K_M*` |
| **V3 csapat (alap modellek)** | Qwen3.8-Flash-Next [AA v5 28.6 = 48% Opus 5.5 · 5.5 bit, 134.1 GB, ~19 tok/s, hibrid GPU+RAM] – fő modell – `mradermacher/Qwen3.8-Flash-Next-i1-GGUF *i1-Q5_K_M*`<br>Qwen3.8-27B (dense) [AA v5 20.1 = 34% Opus 5.5 · 5.5 bit, 19.5 GB, ~42 tok/s, csak GPU] – gyors segéd / router – `mradermacher/Qwen3.8-27B-i1-GGUF *Q5_K_M*`<br>+ RAG-embedding: `gpustack/bge-m3-GGUF *Q8_0*` (0,6 GB). Összesen ~179 GB |
| **V4 vegyes csapat (alap + cenzúrázatlan)** | Qwen3.8-Flash-Next [AA v5 28.6 = 48% Opus 5.5 · 5.5 bit, 134.1 GB, ~19 tok/s, hibrid GPU+RAM] – fő modell – `mradermacher/Qwen3.8-Flash-Next-i1-GGUF *i1-Q5_K_M*`<br>NousResearch Arete-27B (a "R1-1776 utód") [AA v5 ~19.0 = ~32% Opus 5.5 · 4.5 bit, 15.2 GB, ~49 tok/s, csak GPU] – partner (cenzúrázatlan) – `bartowski/NousResearch_Arete-27B-GGUF *IQ4_XS*`<br>Qwen3.8-27B (dense) [AA v5 20.1 = 34% Opus 5.5 · 5.5 bit, 19.5 GB, ~42 tok/s, csak GPU] – gyors segéd / router – `mradermacher/Qwen3.8-27B-i1-GGUF *Q5_K_M*`<br>+ RAG-embedding: `gpustack/bge-m3-GGUF *Q8_0*` (0,6 GB). Összesen ~198 GB |

#### Gamer PC – RTX 6090 32 GB + 256 GB DDR5

*Modellnek jutó memória: ~262 GB · 4×64 GB (AM5 maximum) → kb. DDR5-5200 ≈ 83 GB/s.*

| Változat | Modell(ek) – kvant, méret, becsült sebesség, elhelyezés, letöltés |
|---|---|
| **V1 legokosabb cenzúrázatlan** | Qwen3.8-Flash-Next abliterated v2 (huihui GGUF) [AA v5 ~27.2 = ~46% Opus 5.5 · 5.5 bit, 158.3 GB, ~18 tok/s, hibrid GPU+RAM] – egyedül – `huihui-ai/Huihui-Qwen3.8-Flash-Next-abliterated-v2-GGUF *UD-Q5_K_XL*` |
| **V2 legokosabb alap (cenzúrázott)** | Qwen3.8-Flash-Next [AA v5 28.6 = 48% Opus 5.5 · 5.5 bit, 134.1 GB, ~18 tok/s, hibrid GPU+RAM] – egyedül – `mradermacher/Qwen3.8-Flash-Next-i1-GGUF *i1-Q5_K_M*` |
| **V3 csapat (alap modellek)** | Qwen3.8-Flash-Next [AA v5 28.6 = 48% Opus 5.5 · 5.5 bit, 134.1 GB, ~18 tok/s, hibrid GPU+RAM] – fő modell – `mradermacher/Qwen3.8-Flash-Next-i1-GGUF *i1-Q5_K_M*`<br>Qwen3.8-27B (dense) [AA v5 20.1 = 34% Opus 5.5 · 5.5 bit, 19.5 GB, ~42 tok/s, csak GPU] – gyors segéd / router – `mradermacher/Qwen3.8-27B-i1-GGUF *Q5_K_M*`<br>+ RAG-embedding: `gpustack/bge-m3-GGUF *Q8_0*` (0,6 GB). Összesen ~179 GB |
| **V4 vegyes csapat (alap + cenzúrázatlan)** | Qwen3.8-Flash-Next [AA v5 28.6 = 48% Opus 5.5 · 4.5 bit, 85.7 GB, ~25 tok/s, hibrid GPU+RAM] – fő modell – `AesSedai/Qwen3.8-Flash-Next-GGUF *Q4_0*`<br>MiniMax-M3.1-Flash abliterated (orcarouter GGUF) [AA v5 ~27.1 = ~46% Opus 5.5 · 4.5 bit, 111.9 GB, ~7 tok/s, hibrid GPU+RAM] – partner (cenzúrázatlan) – `orcarouter/MiniMax-M3.1-Flash-abliterated-GGUF *Mix-128G*`<br>Qwen3.8-27B (dense) [AA v5 20.1 = 34% Opus 5.5 · 5.5 bit, 19.5 GB, ~42 tok/s, csak GPU] – gyors segéd / router – `mradermacher/Qwen3.8-27B-i1-GGUF *Q5_K_M*`<br>+ RAG-embedding: `gpustack/bge-m3-GGUF *Q8_0*` (0,6 GB). Összesen ~254 GB |

#### Gamer PC – RTX 6090 + következő generációs RTX Pro (két kártya)

#### Gamer PC – RTX 6090 32 GB + köv. gen. RTX Pro 96 GB (A: konzervatív) + 256 GB DDR5

*Modellnek jutó memória: ~358 GB · A: az utód a mostani RTX PRO 6000 Blackwell szintjén (96 GB, ~1,8 TB/s). Összesen 128 GB VRAM.*

| Változat | Modell(ek) – kvant, méret, becsült sebesség, elhelyezés, letöltés |
|---|---|
| **V1 legokosabb cenzúrázatlan** | Qwen3.8-Flash-Next abliterated v2 (huihui GGUF) [AA v5 ~27.2 = ~46% Opus 5.5 · 4.5 bit, 93.7 GB, ~99 tok/s, csak GPU] – egyedül – `huihui-ai/Huihui-Qwen3.8-Flash-Next-abliterated-v2-GGUF *unsloth-UD-IQ4_XS*`<br>MiniMax-M3.1-Flash abliterated (orcarouter GGUF) [AA v5 ~27.1 = ~46% Opus 5.5 · 4.5 bit, 111.9 GB, ~42 tok/s, hibrid GPU+RAM] – közel azonos alternatíva – `orcarouter/MiniMax-M3.1-Flash-abliterated-GGUF *Mix-128G*`<br>+ RAG-embedding: `gpustack/bge-m3-GGUF *Q8_0*` (0,6 GB). Összesen ~239 GB |
| **V2 legokosabb alap (cenzúrázott)** | Qwen3.8-Flash-Next [AA v5 28.6 = 48% Opus 5.5 · 4.5 bit, 97.5 GB, ~99 tok/s, csak GPU] – egyedül – `mradermacher/Qwen3.8-Flash-Next-i1-GGUF *i1-IQ4_XS*` |
| **V3 csapat (alap modellek)** | Qwen3.8-Flash-Next [AA v5 28.6 = 48% Opus 5.5 · 4.5 bit, 97.5 GB, ~99 tok/s, csak GPU] – fő modell – `mradermacher/Qwen3.8-Flash-Next-i1-GGUF *i1-IQ4_XS*`<br>Qwen3.8-27B (dense) [AA v5 20.1 = 34% Opus 5.5 · 5.5 bit, 19.5 GB, ~40 tok/s, csak GPU] – gyors segéd / router – `mradermacher/Qwen3.8-27B-i1-GGUF *Q5_K_M*`<br>+ RAG-embedding: `gpustack/bge-m3-GGUF *Q8_0*` (0,6 GB). Összesen ~137 GB |
| **V4 vegyes csapat (alap + cenzúrázatlan)** | Qwen3.8-Flash-Next [AA v5 28.6 = 48% Opus 5.5 · 4.5 bit, 97.5 GB, ~99 tok/s, csak GPU] – fő modell – `mradermacher/Qwen3.8-Flash-Next-i1-GGUF *i1-IQ4_XS*`<br>MiniMax-M3.1-Flash abliterated (orcarouter GGUF) [AA v5 ~27.1 = ~46% Opus 5.5 · 4.5 bit, 111.9 GB, ~42 tok/s, hibrid GPU+RAM] – partner (cenzúrázatlan) – `orcarouter/MiniMax-M3.1-Flash-abliterated-GGUF *Mix-128G*`<br>+ RAG-embedding: `gpustack/bge-m3-GGUF *Q8_0*` (0,6 GB). Összesen ~244 GB |

#### Gamer PC – RTX 6090 32 GB + köv. gen. RTX Pro 128 GB (B: valószínű) + 256 GB DDR5

*Modellnek jutó memória: ~390 GB · B: 128 GB, ~2,3 TB/s (becslés). Összesen 160 GB VRAM.*

| Változat | Modell(ek) – kvant, méret, becsült sebesség, elhelyezés, letöltés |
|---|---|
| **V1 legokosabb cenzúrázatlan** | Qwen3.8-Flash-Next abliterated v2 (huihui GGUF) [AA v5 ~27.2 = ~46% Opus 5.5 · 5.5 bit, 158.3 GB, ~56 tok/s, hibrid GPU+RAM] – egyedül – `huihui-ai/Huihui-Qwen3.8-Flash-Next-abliterated-v2-GGUF *UD-Q5_K_XL*`<br>MiniMax-M3.1-Flash abliterated (orcarouter GGUF) [AA v5 ~27.1 = ~46% Opus 5.5 · 4.5 bit, 111.9 GB, ~59 tok/s, csak GPU] – közel azonos alternatíva – `orcarouter/MiniMax-M3.1-Flash-abliterated-GGUF *Mix-128G*`<br>+ RAG-embedding: `gpustack/bge-m3-GGUF *Q8_0*` (0,6 GB). Összesen ~314 GB |
| **V2 legokosabb alap (cenzúrázott)** | Qwen3.8-Flash-Next [AA v5 28.6 = 48% Opus 5.5 · 5.5 bit, 134.1 GB, ~98 tok/s, csak GPU] – egyedül – `mradermacher/Qwen3.8-Flash-Next-i1-GGUF *i1-Q5_K_M*` |
| **V3 csapat (alap modellek)** | Qwen3.8-Flash-Next [AA v5 28.6 = 48% Opus 5.5 · 5.5 bit, 134.1 GB, ~98 tok/s, csak GPU] – fő modell – `mradermacher/Qwen3.8-Flash-Next-i1-GGUF *i1-Q5_K_M*`<br>Qwen3.8-27B (dense) [AA v5 20.1 = 34% Opus 5.5 · 5.5 bit, 19.5 GB, ~46 tok/s, csak GPU] – gyors segéd / router – `mradermacher/Qwen3.8-27B-i1-GGUF *Q5_K_M*`<br>+ RAG-embedding: `gpustack/bge-m3-GGUF *Q8_0*` (0,6 GB). Összesen ~179 GB |
| **V4 vegyes csapat (alap + cenzúrázatlan)** | Qwen3.8-Flash-Next [AA v5 28.6 = 48% Opus 5.5 · 5.5 bit, 134.1 GB, ~98 tok/s, csak GPU] – fő modell – `mradermacher/Qwen3.8-Flash-Next-i1-GGUF *i1-Q5_K_M*`<br>MiniMax-M3.1-Flash abliterated (orcarouter GGUF) [AA v5 ~27.1 = ~46% Opus 5.5 · 4.5 bit, 111.9 GB, ~59 tok/s, csak GPU] – partner (cenzúrázatlan) – `orcarouter/MiniMax-M3.1-Flash-abliterated-GGUF *Mix-128G*`<br>+ RAG-embedding: `gpustack/bge-m3-GGUF *Q8_0*` (0,6 GB). Összesen ~286 GB |

#### Gamer PC – RTX 6090 32 GB + köv. gen. RTX Pro 192 GB (C: optimista) + 256 GB DDR5

*Modellnek jutó memória: ~454 GB · C: 192 GB, ~2,8 TB/s (optimista becslés). Összesen 224 GB VRAM.*

| Változat | Modell(ek) – kvant, méret, becsült sebesség, elhelyezés, letöltés |
|---|---|
| **V1 legokosabb cenzúrázatlan** | Qwen3.8-Flash-Next abliterated v2 (huihui GGUF) [AA v5 ~27.2 = ~46% Opus 5.5 · 8.5 bit, 188.2 GB, ~90 tok/s, csak GPU] – egyedül – `huihui-ai/Huihui-Qwen3.8-Flash-Next-abliterated-v2-GGUF *Q8_0*` |
| **V2 legokosabb alap (cenzúrázott)** | Qwen3.8-Flash-Next [AA v5 28.6 = 48% Opus 5.5 · 8.5 bit, 185.6 GB, ~90 tok/s, csak GPU] – egyedül – `Qwen/Qwen3.8-Flash-Next-FP8` |
| **V3 csapat (alap modellek)** | Qwen3.8-Flash-Next [AA v5 28.6 = 48% Opus 5.5 · 8.5 bit, 185.6 GB, ~90 tok/s, csak GPU] – fő modell – `Qwen/Qwen3.8-Flash-Next-FP8`<br>Qwen3.8-27B (dense) [AA v5 20.1 = 34% Opus 5.5 · 8.5 bit, 30.9 GB, ~38 tok/s, csak GPU] – gyors segéd / router – `Qwen/Qwen3.8-27B-FP8`<br>+ RAG-embedding: `gpustack/bge-m3-GGUF *Q8_0*` (0,6 GB). Összesen ~252 GB |
| **V4 vegyes csapat (alap + cenzúrázatlan)** | Qwen3.8-Flash-Next [AA v5 28.6 = 48% Opus 5.5 · 8.5 bit, 185.6 GB, ~90 tok/s, csak GPU] – fő modell – `Qwen/Qwen3.8-Flash-Next-FP8`<br>MiniMax-M3.1-Flash abliterated (orcarouter GGUF) [AA v5 ~27.1 = ~46% Opus 5.5 · 4.5 bit, 111.9 GB, ~65 tok/s, csak GPU] – partner (cenzúrázatlan) – `orcarouter/MiniMax-M3.1-Flash-abliterated-GGUF *Mix-128G*`<br>+ RAG-embedding: `gpustack/bge-m3-GGUF *Q8_0*` (0,6 GB). Összesen ~345 GB |

#### Linux szerverek

#### Linux szerver – EPYC 12 csatornás DDR5 768 GB + 1× RTX 6090 32 GB

*Modellnek jutó memória: ~739 GB · ik_llama.cpp / KTransformers: MoE-szakértők RAM-ban, figyelem a GPU-n.*

| Változat | Modell(ek) – kvant, méret, becsült sebesség, elhelyezés, letöltés |
|---|---|
| **V1 legokosabb cenzúrázatlan** | DeepSeek-V4.1-Flash-1017 abliterated (huihui GGUF) / heretic (pqhaz) / abliterated (mrfakename) [AA v5 ~31.6 = ~53% Opus 5.5 · 8.5 bit, 507.9 GB, ~18 tok/s, hibrid GPU+RAM] – egyedül – `pqhaz/DeepSeek-V4.1-Flash-1017-heretic-GGUF *Q8_0*` |
| **V2 legokosabb alap (cenzúrázott)** | DeepSeek-V4.1-Flash-1017 [AA v5 32.6 = 55% Opus 5.5 · 8.5 bit, 508.4 GB, ~18 tok/s, hibrid GPU+RAM] – egyedül – `unsloth/DeepSeek-V4.1-Flash-1017-GGUF *UD-Q8_K_XL*`<br>Hy4 preview (Hunyuan) [AA v5 ~34.6 = ~59% Opus 5.5 · 4.5 bit, 467.3 GB, ~12 tok/s, hibrid GPU+RAM] – közel azonos alternatíva – `AngelSlim/Hy4-preview-GGUF *Q4_K_M*`<br>+ RAG-embedding: `gpustack/bge-m3-GGUF *Q8_0*` (0,6 GB). Összesen ~1125 GB |
| **V3 csapat (alap modellek)** | DeepSeek-V4.1-Flash-1017 [AA v5 32.6 = 55% Opus 5.5 · 8.5 bit, 508.4 GB, ~18 tok/s, hibrid GPU+RAM] – fő modell – `unsloth/DeepSeek-V4.1-Flash-1017-GGUF *UD-Q8_K_XL*`<br>Qwen3.8-27B (dense) [AA v5 20.1 = 34% Opus 5.5 · 5.5 bit, 19.5 GB, ~39 tok/s, csak GPU] – gyors segéd / router – `mradermacher/Qwen3.8-27B-i1-GGUF *Q5_K_M*`<br>+ RAG-embedding: `gpustack/bge-m3-GGUF *Q8_0*` (0,6 GB). Összesen ~610 GB |
| **V4 vegyes csapat (alap + cenzúrázatlan)** | DeepSeek-V4.1-Flash-1017 [AA v5 32.6 = 55% Opus 5.5 · 8.5 bit, 508.4 GB, ~18 tok/s, hibrid GPU+RAM] – fő modell – `unsloth/DeepSeek-V4.1-Flash-1017-GGUF *UD-Q8_K_XL*`<br>Qwen3.8-Flash-Next abliterated v2 (huihui GGUF) [AA v5 ~27.2 = ~46% Opus 5.5 · 4.5 bit, 93.7 GB, ~64 tok/s, hibrid GPU+RAM] – partner (cenzúrázatlan) – `huihui-ai/Huihui-Qwen3.8-Flash-Next-abliterated-v2-GGUF *unsloth-UD-IQ4_XS*`<br>Qwen3.8-27B (dense) [AA v5 20.1 = 34% Opus 5.5 · 5.5 bit, 19.5 GB, ~39 tok/s, csak GPU] – gyors segéd / router – `mradermacher/Qwen3.8-27B-i1-GGUF *Q5_K_M*`<br>+ RAG-embedding: `gpustack/bge-m3-GGUF *Q8_0*` (0,6 GB). Összesen ~719 GB |

#### Linux szerver – 8× H200 141 GB (tensor parallel)

*Modellnek jutó memória: ~2050 GB · vLLM/SGLang TP=8; az összesített sávszélesség ~60%-át számolom (kommunikációs veszteség).*

| Változat | Modell(ek) – kvant, méret, becsült sebesség, elhelyezés, letöltés |
|---|---|
| **V1 legokosabb cenzúrázatlan** | DeepSeek-V4.1-Flash-1017 abliterated (huihui GGUF) / heretic (pqhaz) / abliterated (mrfakename) [AA v5 ~31.6 = ~53% Opus 5.5 · 8.5 bit, 507.9 GB, ~108 tok/s, csak GPU] – egyedül – `pqhaz/DeepSeek-V4.1-Flash-1017-heretic-GGUF *Q8_0*` |
| **V2 legokosabb alap (cenzúrázott)** | Kimi K3.1 Pro [AA v5 46.5 = 79% Opus 5.5 · 4.5 bit, 1508.9 GB, ~16 tok/s, hibrid GPU+RAM] – egyedül – `DevQuasar/moonshotai.Kimi-K3.1-Pro-GGUF *MXFP4_MOE*` |
| **V3 csapat (alap modellek)** | Kimi K3.1 Pro [AA v5 46.5 = 79% Opus 5.5 · 4.5 bit, 1508.9 GB, ~16 tok/s, hibrid GPU+RAM] – fő modell – `DevQuasar/moonshotai.Kimi-K3.1-Pro-GGUF *MXFP4_MOE*`<br>Qwen3.8-27B (dense) [AA v5 20.1 = 34% Opus 5.5 · 8.5 bit, 30.9 GB, ~99 tok/s, csak GPU] – gyors segéd / router – `Qwen/Qwen3.8-27B-FP8`<br>+ RAG-embedding: `gpustack/bge-m3-GGUF *Q8_0*` (0,6 GB). Összesen ~1774 GB |
| **V4 vegyes csapat (alap + cenzúrázatlan)** | Kimi K3.1 Pro [AA v5 46.5 = 79% Opus 5.5 · 4.5 bit, 1508.9 GB, ~16 tok/s, hibrid GPU+RAM] – fő modell – `DevQuasar/moonshotai.Kimi-K3.1-Pro-GGUF *MXFP4_MOE*`<br>Qwen3.8-Flash-Next abliterated v2 (huihui GGUF) [AA v5 ~27.2 = ~46% Opus 5.5 · 8.5 bit, 188.2 GB, ~118 tok/s, csak GPU] – partner (cenzúrázatlan) – `huihui-ai/Huihui-Qwen3.8-Flash-Next-abliterated-v2-GGUF *Q8_0*`<br>Qwen3.8-27B (dense) [AA v5 20.1 = 34% Opus 5.5 · 8.5 bit, 30.9 GB, ~99 tok/s, csak GPU] – gyors segéd / router – `Qwen/Qwen3.8-27B-FP8`<br>+ RAG-embedding: `gpustack/bge-m3-GGUF *Q8_0*` (0,6 GB). Összesen ~1991 GB |

**Gyakorlati tanácsok a csapathoz:**
- **Futtatás:** minden modell külön `llama-server` példányként fut, külön porton (pl. 8080 = fő, 8081 = partner, 8082 = segéd, 8083 = embedding).
- **Közös felület:** az Open WebUI mindet egy felületen kezeli, és modellenként választható. Router-logika: egyszerű kérdés → gyors segéd; nehéz → fő modell; elutasított vagy érzékeny téma → cenzúrázatlan partner.
- **Ellenőrzés:** a fontos válaszokat érdemes a másik modellel is ellenőriztetni („második vélemény”). Orvosi, vegyi és szerkezeti témában a RAG-forrásdokumentum dönt.
- **Klaszter:** gépenként `rpc-server`, a fő gépen pedig `llama-server --rpc host2:50052,host3:50052 …`. A gépek USB4 v2 (Thunderbolt-hálózat) vagy 10GbE kapcsolaton át kommunikálnak.
- **Két különböző videokártya:**
  - Rétegenként osztja szét a modellt a `-ts 32,96` (tensor-split, a VRAM arányában) és a `-sm layer` kapcsoló.
  - A nagyobb kártya legyen a `--main-gpu`.
  - A két kártya nem kell, hogy azonos generációjú legyen (CUDA mindkettő).

### 6.9 Kihagyott (régi vagy gyenge) modellek

- **Felváltott generációk:** Kimi-K3 és K2.x, DeepSeek-V4-Pro-0813 és V3.x, GLM-5.2 és korábbiak, MiniMax-M3 és M2.x, Qwen3.6/3.5 nagy modellek, Step-3.7, MiMo-V2.5, Ling-3.0, Hy3, Llama 4.
- **Gyenge az AA v5-ön:** gpt-oss-120b/20b (3,8), Nemotron-3-Ultra, Command A+, Granite 4.2, Phi-4. Az ERNIE-5.5-ből csak base modell van.
- **Archívumcélra maradt bent:** a gpt-oss heretic-változata, mert kicsi, Apache-licencű és gyors.
