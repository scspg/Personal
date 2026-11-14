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

**Rangsor (AA v5, nyílt modellek):**
- Kimi K3.1 Pro 46.5
- DeepSeek-V4.1-Flash 32.6
- GLM-5.3 31.7
- MiMo-V2.6-Pro 29.9
- Ling-3.1-flash 29.6
- MiniMax-M3.1-Flash 29.1
- Qwen3.8-Flash-Next 28.6
- Step-5 28.5
- GLM-5.3-Flash 27.8
- Muse Spark 24.9
- Qwen3.8-27B 20.1

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

| Modell | Típus | Kiadva | AA-index | Licenc | Méret (min–max) | Változat | Platform | HW | group |
|---|---|---|---|---|---|---|---|---|---|
| Kimi K3.1 Pro | alap | 2026-11-02 | 46.5 | Kimi K3.1 Pro License (c | 592.7 GB – 1.61 TB | 9 | any, mac, server | T2–T1 | `llm-kimi-k3-1-pro` |
| Qwen3.8-2.4T-A95B (a hostolt „Qwen3.8-Max” alapja) | alap | 2026-08-08 | ~40.0 | Qwen3.8-Max license (oth | 397.3 GB – 4.89 TB | 12 | any, server | T2–T1 | `llm-qwen3-8-2-4t-a95b` |
| DeepSeek-V4.1-Flash-1017 | alap | 2026-10-17 | 32.6 | MIT | 120.7 GB – 510.3 GB | 23 | any, mac, server | T3–T1 | `llm-deepseek-v4-1-flash-1017` |
| GLM-5.3 | alap | 2026-08-25 | 31.7 | GLM-5.3 custom license ( | 211.1 GB – 1.51 TB | 25 | any, mac, server | T3–T1 | `llm-glm-5-3` |
| Inkling 2 Small | alap | 2026-11-04 | 30.6 | Apache-2.0 | 341.5 GB – 968.8 GB | 13 | any, mac, server | T2–T1 | `llm-inkling-2-small` |
| Hy4 preview (Hunyuan) | alap | 2026-08-27 | ~30.0 | Apache-2.0 | 229.4 GB – 1.56 TB | 6 | any, mac, server | T2–T1 | `llm-hy4-preview` |
| LongCat-2.5 (csak megjegyzésként) | alap | 2026-11-04 | ~30.0 | MIT | 1.34 TB – 1.34 TB | 1 | server | T1–T1 | `llm-longcat-2-5` |
| MiMo-V2.6-Pro (RL és MOPD változat) + MiMo-V2.6-Flash | alap | 2026-09-21 | 29.9 | MIT | 126.4 GB – 617.9 GB | 18 | any, mac, server | T3–T1 | `llm-mimo-v2-6-pro` |
| Ling-3.1-flash-1019 | alap | 2026-10-27 | 29.6 | MIT | 131.0 GB – 608.4 GB | 18 | any, mac, server | T3–T1 | `llm-ling-3-1-flash-1019` |
| MiniMax-M3.1-Flash | alap | 2026-10-17 | 29.1 | MiniMax Community Licens | 129.4 GB – 302.9 GB | 16 | any, mac, server | T3–T1 | `llm-minimax-m3-1-flash` |
| Qwen3.8-Flash-Next | alap | 2026-08-24 | 28.6 | Qwen Community License 1 | 66.4 GB – 360.0 GB | 57 | any, mac, server | T4–T1 | `llm-qwen3-8-flash-next` |
| Step 5 Preview | alap | 2026-09-20 | 28.5 | StepFun Model License (o | 182.5 GB – 1.21 TB | 8 | any, server | T3–T1 | `llm-step-5-preview` |
| GLM-5.3-Flash | alap | 2026-08-25 | 27.8 | MIT | 74.8 GB – 642.7 GB | 44 | any, mac, server | T3–T1 | `llm-glm-5-3-flash` |
| Mistral Large 4 (1T-A52B) | alap | 2026-09-30 | ~27.0 | Mistral Ecosystem Open-W | 233.0 GB – 2.10 TB | 21 | any, mac, server | T2–T1 | `llm-mistral-large-4` |
| Muse Spark Open (816B-A42B) | alap | 2026-09-15 | 24.9 | Muse Model License; GATE | 175.6 GB – 1.64 TB | 17 | any, mac, server | T3–T1 | `llm-muse-spark-open` |
| Qwen3.8-27B (dense) | alap | 2026-08-05 | 20.1 | Apache-2.0 | 6.2 GB – 55.6 GB | 58 | any, mac, server | T4–T1 | `llm-qwen3-8-27b` |
| NVIDIA Nemotron 3.5 (Super-VL-120B-A12B, Lightning-30B-A3B, Bolt-E4B) | alap | Super-VL 2 | 13.6 | OpenMDW-1.1 (nyílt súlyo | 3.5 GB – 241.5 GB | 45 | any, mac, server | T5–T1 | `llm-nemotron-3-5` |
| Muse Glimmer 30B | alap | 2026-08-09 | 6.3 | Apache-2.0 | 6.5 GB – 57.1 GB | 33 | any, mac, server | T4–T1 | `llm-muse-glimmer-30b` |
| Gemma 4 (31B, 26B-A4B, 12B, E4B, E2B) | alap | E2B/E4B 20 | ~4.4 | Apache-2.0 | 2.3 GB – 62.6 GB | 100 | android, any, mac, server | T5–T1 | `llm-gemma-4` |
| Qwen3.5-4B / Qwen3.5-9B (+ MiMo-V2.6-Distill-Qwen-9B) | alap | 2026-02-27 | ~3.0 | Apache-2.0 (Qwen3.5); MI | 1.8 GB – 10.4 GB | 22 | any | T5–T1 | `llm-qwen3-5-small` |
| DeepSeek-V4.1-Flash-1017 abliterated (huihui GGUF) / heretic (pqhaz) / abliterated (mrfakename) | cenz.-mentes | 2026-10-17 | ~30.97 | MIT | 233.0 GB – 510.3 GB | 5 | any, mac, server | T2–T1 | `llm-deepseek-v4-1-flash-1017-abliterated-hui` |
| GLM-5.3 abliterated (huihui GGUF) | cenz.-mentes | 2026-08-25 | ~30.11 | other (glm-5.3) | 216.7 GB – 216.7 GB | 1 | any | T2–T1 | `llm-glm-5-3-abliterated-huihui-gguf` |
| MiniMax-M3.1-Flash abliterated (orcarouter GGUF) | cenz.-mentes | 2026-10-17 | ~27.64 | other (minimax-community | 111.9 GB – 111.9 GB | 1 | any | T3–T1 | `llm-minimax-m3-1-flash-abliterated-orcaroute` |
| Qwen3.8-Flash-Next abliterated v2 (huihui GGUF) | cenz.-mentes | 2026-08-24 | ~27.17 | other (qwen-community-1. | 68.2 GB – 188.2 GB | 9 | any, mac | T3–T1 | `llm-qwen3-8-flash-next-abliterated-v2-huihui` |
| GLM-5.3-Flash abliterated (huihui GGUF) | cenz.-mentes | 2026-08-25 | ~26.41 | MIT | 93.1 GB – 291.8 GB | 10 | any, mac | T3–T1 | `llm-glm-5-3-flash-abliterated-huihui-gguf` |
| Qwen3.8-27B abliterated (huihui) / heretic-ara (trohrbaugh) | cenz.-mentes | 2026-08-05 | ~19.09 | Apache-2.0 | 10.9 GB – 29.1 GB | 6 | any, mac | T4–T1 | `llm-qwen3-8-27b-abliterated-huihui-heretic-a` |
| NousResearch Arete-27B (a "R1-1776 utód") | cenz.-mentes | 2026-08-05 | ~18.05 | Apache-2.0 | 15.2 GB – 17.2 GB | 2 | any | T4–T1 | `llm-nousresearch-arete-27b-a-r1-1776-ut-d` |
| Kimi-K3 Abliterated V1 (Uniboshi) | cenz.-mentes | 2026-06-13 | ~16.53 | other (kimi-k3) | 1.51 TB – 1.51 TB | 1 | any | T1–T1 | `llm-kimi-k3-abliterated-v1-uniboshi` |
| Mistral-Small-4-119B-2603 heretic (darkc0de, GGUF: Rioky) | cenz.-mentes | 2026-01-23 | ~7.6 | Apache-2.0 (bázis); a he | 43.4 GB – 126.5 GB | 6 | any | T3–T1 | `llm-mistral-small-4-119b-2603-heretic-darkc0` |
| Qwen3.6-35B-A3B uncensored-heretic (llmfan46) / abliterated-MTP (huihui) | cenz.-mentes | 2026-04-15 | ~7.6 | Apache-2.0 | 16.9 GB – 21.2 GB | 2 | any | T4–T1 | `llm-qwen3-6-35b-a3b-uncensored-heretic-llmfa` |
| gemma-4-31B-it heretic (coder3101) / uncensored-heretic (llmfan46) | cenz.-mentes | 2026-03-11 | ~4.18 | Apache-2.0, NEM gated | 16.9 GB – 25.2 GB | 4 | any, mac | T4–T1 | `llm-gemma-4-31b-it-heretic-coder3101-uncenso` |
| gpt-oss-120b heretic (MuXodious tainted-heresy / kldzj heretic) | cenz.-mentes | 2025-08-04 | ~3.61 | Apache-2.0 | 62.2 GB – 63.4 GB | 3 | any, mac | T4–T1 | `llm-gpt-oss-120b-heretic-muxodious-tainted-h` |
| gemma-4-26B-A4B-it ultra-uncensored-heretic (llmfan46) | cenz.-mentes | 2026-03-11 | ~3.32 | Apache-2.0 | 13.3 GB – 16.8 GB | 2 | any | T4–T1 | `llm-gemma-4-26b-a4b-it-ultra-uncensored-here` |
| gemma-4-12B-it uncensored-heretic (llmfan46) / abliterated QAT (huihui) | cenz.-mentes | 2026-05-23 | ~2.85 | Apache-2.0 | 8.5 GB – 8.5 GB | 1 | any | T4–T1 | `llm-gemma-4-12b-it-uncensored-heretic-llmfan` |
| Qwen3.5-9B heretic-v2 (trohrbaugh) | cenz.-mentes | 2026-02-27 | ~2.85 | Apache-2.0 | 5.6 GB – 9.5 GB | 2 | any | T5–T1 | `llm-qwen3-5-9b-heretic-v2-trohrbaugh` |
| gpt-oss-20b heretic (MuXodious RichardErkhov-heresy / p-e-w heretic) | cenz.-mentes | 2025-08-04 | ~2.38 | Apache-2.0 | 12.7 GB – 12.7 GB | 1 | any | T4–T1 | `llm-gpt-oss-20b-heretic-muxodious-richarderk` |
| gemma-4-E4B-it heretic (coder3101; GGUF Abiray) / ultra-uncensored (llmfan46) | cenz.-mentes | 2026-03-02 | ~2.38 | Apache-2.0 | 5.3 GB – 5.3 GB | 1 | any | T5–T1 | `llm-gemma-4-e4b-it-heretic-coder3101-gguf-ab` |
| Qwen3.5-4B heretic-2.0 (p-e-w) / SOMPOA-heresy-v2 (MuXodious) | cenz.-mentes | 2026-02-27 | ~1.9 | Apache-2.0 | 2.5 GB – 4.5 GB | 4 | any | T5–T1 | `llm-qwen3-5-4b-heretic-2-0-p-e-w-sompoa-here` |
| gemma-4-E2B-it ultra-uncensored-heretic (llmfan46) | cenz.-mentes | 2026-03-02 | ~1.42 | Apache-2.0 | 3.4 GB – 3.6 GB | 2 | any | T5–T1 | `llm-gemma-4-e2b-it-ultra-uncensored-heretic-` |

### 6.4 Minden kvantált változat linkkel és letöltési paranccsal

Kattints egy modellre a lenyitáshoz. A `hf download` parancsok változtatás nélkül futtathatók. A `--include` minta egy kvantot tölt le. Letöltés előtt a fájllistát érdemes ellenőrizni: `curl -s https://huggingface.co/api/models/<repo>/tree/main?recursive=true`.

<details><summary><b>Kimi K3.1 Pro</b> – 9 változat</summary>

| id | Fájl / repó | Méret | Bit | HW | Platform | Letöltés |
|---|---|---|---|---|---|---|
| `llm-kimi-k3-1-pro-gguf-klx-iq1-s` | Kimi-K3.1-Pro-GGUF · KLX-IQ1_S (GGUF) | 592.7 GB | 1.7 | T1 | any | `hf download KarLexAI/Kimi-K3.1-Pro-GGUF --include "*KLX-IQ1_S*"` |
| `llm-kimi-k3-1-pro-gguf-klx-iq1-m` | Kimi-K3.1-Pro-GGUF · KLX-IQ1_M (GGUF) | 647.9 GB | 1.7 | T1,T2 | any | `hf download KarLexAI/Kimi-K3.1-Pro-GGUF --include "*KLX-IQ1_M*"` |
| `llm-kimi-k3-1-pro-gguf-klx-iq2-xxs` | Kimi-K3.1-Pro-GGUF · KLX-IQ2_XXS (GGUF) | 709.9 GB | 2.6 | T1,T2 | any | `hf download KarLexAI/Kimi-K3.1-Pro-GGUF --include "*KLX-IQ2_XXS*"` |
| `llm-kimi-k3-1-pro-exl3-2bit` | Kimi-K3.1-Pro-EXL3-2bit · 2bit (EXL3) | 797.0 GB | 2.5 | T1 | server | `hf download local-inference-lab/Kimi-K3.1-Pro-EXL3-2bit` |
| `llm-kimi-k3-1-pro-gguf-q2-k` | moonshotai.Kimi-K3.1-Pro-GGUF · Q2_K (GGUF) | 1.01 TB | 2.6 | T1 | any | `hf download DevQuasar/moonshotai.Kimi-K3.1-Pro-GGUF --include "*Q2_K*"` |
| `llm-kimi-k3-1-pro-gguf-mxfp4-moe` | moonshotai.Kimi-K3.1-Pro-GGUF · MXFP4_MOE (GGUF) | 1.51 TB | 4.5 | T1 | any | `hf download DevQuasar/moonshotai.Kimi-K3.1-Pro-GGUF --include "*MXFP4_MOE*"` |
| `llm-kimi-k3-1-pro-mlx-mlxse` | Kimi-K3.1-Pro-MLXse · MLXse (MLX) | 1.56 TB | 4.5 | T1 | mac | `hf download inferencerlabs/Kimi-K3.1-Pro-MLXse` |
| `llm-kimi-k3-1-pro-safetensors-int4-native-native` | Kimi-K3.1-Pro · native (safetensors-INT4(native)) | 1.56 TB | 4.5 | T1 | server | `hf download moonshotai/Kimi-K3.1-Pro` |
| `llm-kimi-k3-1-pro-nvfp4-nvfp4` | Kimi-K3.1-Pro-NVFP4 · NVFP4 (NVFP4) | 1.61 TB | 4.5 | T1 | server | `hf download nvidia/Kimi-K3.1-Pro-NVFP4` |
</details>

<details><summary><b>Qwen3.8-2.4T-A95B (a hostolt „Qwen3.8-Max” alapja)</b> – 12 változat</summary>

| id | Fájl / repó | Méret | Bit | HW | Platform | Letöltés |
|---|---|---|---|---|---|---|
| `llm-qwen3-8-2-4t-a95b-gguf-ud-q1-0` | Qwen3.8-2.4T-A95B-GGUF · UD-Q1_0 (GGUF) | 397.3 GB | 1.7 | T1,T2 | any | `hf download unsloth/Qwen3.8-2.4T-A95B-GGUF --include "*UD-Q1_0*"` |
| `llm-qwen3-8-2-4t-a95b-gguf-ud-iq1-s` | Qwen3.8-2.4T-A95B-GGUF · UD-IQ1_S (GGUF) | 508.4 GB | 1.7 | T1,T2 | any | `hf download unsloth/Qwen3.8-2.4T-A95B-GGUF --include "*UD-IQ1_S*"` |
| `llm-qwen3-8-2-4t-a95b-gguf-ud-iq1-m` | Qwen3.8-2.4T-A95B-GGUF · UD-IQ1_M (GGUF) | 564.0 GB | 1.7 | T1,T2 | any | `hf download unsloth/Qwen3.8-2.4T-A95B-GGUF --include "*UD-IQ1_M*"` |
| `llm-qwen3-8-2-4t-a95b-gguf-ud-iq2-xxs` | Qwen3.8-2.4T-A95B-GGUF · UD-IQ2_XXS (GGUF) | 656.6 GB | 2.6 | T1,T2 | any | `hf download unsloth/Qwen3.8-2.4T-A95B-GGUF --include "*UD-IQ2_XXS*"` |
| `llm-qwen3-8-2-4t-a95b-gguf-ud-iq2-xs` | Qwen3.8-2.4T-A95B-GGUF · UD-IQ2_XS (GGUF) | 730.6 GB | 2.6 | T1,T2 | any | `hf download unsloth/Qwen3.8-2.4T-A95B-GGUF --include "*UD-IQ2_XS*"` |
| `llm-qwen3-8-2-4t-a95b-gguf-ud-iq3-xxs` | Qwen3.8-2.4T-A95B-GGUF · UD-IQ3_XXS (GGUF) | 955.5 GB | 3.5 | T1 | any | `hf download unsloth/Qwen3.8-2.4T-A95B-GGUF --include "*UD-IQ3_XXS*"` |
| `llm-qwen3-8-2-4t-a95b-gguf-ud-iq4-xs` | Qwen3.8-2.4T-A95B-GGUF · UD-IQ4_XS (GGUF) | 1.31 TB | 4.5 | T1 | any | `hf download unsloth/Qwen3.8-2.4T-A95B-GGUF --include "*UD-IQ4_XS*"` |
| `llm-qwen3-8-2-4t-a95b-nvfp4-nvfp4` | Qwen3.8-2.4T-A95B-NVFP4 · NVFP4 (NVFP4) | 1.43 TB | 4.5 | T1 | server | `hf download RedHatAI/Qwen3.8-2.4T-A95B-NVFP4` |
| `llm-qwen3-8-2-4t-a95b-nvfp4-nvfp4-2` | Qwen3.8-2.4T-A95B-NVFP4 · NVFP4 (NVFP4) | 1.44 TB | 4.5 | T1 | server | `hf download nvidia/Qwen3.8-2.4T-A95B-NVFP4` |
| `llm-qwen3-8-2-4t-a95b-fp8-fp8` | Qwen3.8-2.4T-A95B-FP8 · FP8 (FP8) | 2.50 TB | 8.5 | T1 | server | `hf download Qwen/Qwen3.8-2.4T-A95B-FP8` |
| `llm-qwen3-8-2-4t-a95b-gguf-q8-0` | Qwen3.8-2.4T-A95B-GGUF · Q8_0 (GGUF) | 2.60 TB | 8.5 | T1 | any | `hf download unsloth/Qwen3.8-2.4T-A95B-GGUF --include "*Q8_0*"` |
| `llm-qwen3-8-2-4t-a95b-gguf-bf16` | Qwen3.8-2.4T-A95B-GGUF · BF16 (GGUF) | 4.89 TB | 16 | T1 | any | `hf download unsloth/Qwen3.8-2.4T-A95B-GGUF --include "*BF16*"` |
</details>

<details><summary><b>DeepSeek-V4.1-Flash-1017</b> – 23 változat</summary>

| id | Fájl / repó | Méret | Bit | HW | Platform | Letöltés |
|---|---|---|---|---|---|---|
| `llm-deepseek-v4-1-flash-1017-gguf-iq1-m` | DeepSeek-V4.1-Flash-1017-GSQ-RCO-GGUF · IQ1_M (GGUF) | 120.7 GB | 1.7 | T1,T2,T3 | any | `hf download ISTA-DASLab/DeepSeek-V4.1-Flash-1017-GSQ-RCO-GGUF --include "*IQ1_M*"` |
| `llm-deepseek-v4-1-flash-1017-gguf-iq2-xxs` | DeepSeek-V4.1-Flash-1017-GSQ-RCO-GGUF · IQ2_XXS (GGUF) | 138.2 GB | 2.6 | T1,T2,T3 | any | `hf download ISTA-DASLab/DeepSeek-V4.1-Flash-1017-GSQ-RCO-GGUF --include "*IQ2_XXS*"` |
| `llm-deepseek-v4-1-flash-1017-gguf-iq2-xs` | DeepSeek-V4.1-Flash-1017-GSQ-RCO-GGUF · IQ2_XS (+ külön Engram IQ4_NL 110.6GB) (GGUF) | 155.2 GB | 2.6 | T1,T2,T3 | any | `hf download ISTA-DASLab/DeepSeek-V4.1-Flash-1017-GSQ-RCO-GGUF --include "*IQ2_XS*"` |
| `llm-deepseek-v4-1-flash-1017-gguf-ud-iq1-s` | DeepSeek-V4.1-Flash-1017-GGUF · UD-IQ1_S (GGUF) | 233.0 GB | 1.7 | T1,T2,T3 | any | `hf download unsloth/DeepSeek-V4.1-Flash-1017-GGUF --include "*UD-IQ1_S*"` |
| `llm-deepseek-v4-1-flash-1017-gguf-ud-iq1-m` | DeepSeek-V4.1-Flash-1017-GGUF · UD-IQ1_M (GGUF) | 250.4 GB | 1.7 | T1,T2 | any | `hf download unsloth/DeepSeek-V4.1-Flash-1017-GGUF --include "*UD-IQ1_M*"` |
| `llm-deepseek-v4-1-flash-1017-gguf-q2-k-s` | DeepSeek-V4.1-Flash-1017-GGUF · Q2_K_S (GGUF) | 298.0 GB | 2.6 | T1,T2 | any | `hf download ggml-org/DeepSeek-V4.1-Flash-1017-GGUF --include "*Q2_K_S*"` |
| `llm-deepseek-v4-1-flash-1017-gguf-ud-iq2-xxs` | DeepSeek-V4.1-Flash-1017-GGUF · UD-IQ2_XXS (GGUF) | 300.5 GB | 2.6 | T1,T2 | any | `hf download unsloth/DeepSeek-V4.1-Flash-1017-GGUF --include "*UD-IQ2_XXS*"` |
| `llm-deepseek-v4-1-flash-1017-mlx-oq2e-mtp` | DeepSeek-V4.1-Flash-1017-oQ2e-mtp · oQ2e-mtp (MLX) | 313.3 GB | 2.5 | T1,T2 | mac | `hf download mlx-community/DeepSeek-V4.1-Flash-1017-oQ2e-mtp` |
| `llm-deepseek-v4-1-flash-1017-gguf-ud-q2-k-xl` | DeepSeek-V4.1-Flash-1017-GGUF · UD-Q2_K_XL (GGUF) | 334.8 GB | 2.6 | T1,T2 | any | `hf download unsloth/DeepSeek-V4.1-Flash-1017-GGUF --include "*UD-Q2_K_XL*"` |
| `llm-deepseek-v4-1-flash-1017-gguf-q2-k` | DeepSeek-V4.1-Flash-1017-GGUF · Q2_K (GGUF) | 334.8 GB | 2.6 | T1,T2 | any | `hf download ggml-org/DeepSeek-V4.1-Flash-1017-GGUF --include "*Q2_K*"` |
| `llm-deepseek-v4-1-flash-1017-mlx-oq2-5e-mtp` | DeepSeek-V4.1-Flash-1017-oQ2.5e-mtp · oQ2.5e-mtp (MLX) | 342.7 GB | 3.0 | T1,T2 | mac | `hf download mlx-community/DeepSeek-V4.1-Flash-1017-oQ2.5e-mtp` |
| `llm-deepseek-v4-1-flash-1017-gguf-q2-k-imatrix` | deepseek-v4.1-flash-gguf · Q2_K-imatrix (GGUF) | 365.7 GB | 2.6 | T1,T2 | any | `hf download antirez/deepseek-v4.1-flash-gguf --include "*Q2_K-imatrix*"` |
| `llm-deepseek-v4-1-flash-1017-mlx-oq3e-mtp` | DeepSeek-V4.1-Flash-1017-oQ3e-mtp · oQ3e-mtp (MLX) | 381.2 GB | 3.5 | T1,T2 | mac | `hf download mlx-community/DeepSeek-V4.1-Flash-1017-oQ3e-mtp` |
| `llm-deepseek-v4-1-flash-1017-gguf-ud-iq3-xxs` | DeepSeek-V4.1-Flash-1017-GGUF · UD-IQ3_XXS (GGUF) | 394.7 GB | 3.5 | T1,T2 | any | `hf download unsloth/DeepSeek-V4.1-Flash-1017-GGUF --include "*UD-IQ3_XXS*"` |
| `llm-deepseek-v4-1-flash-1017-gguf-ud-iq3-s` | DeepSeek-V4.1-Flash-1017-GGUF · UD-IQ3_S (GGUF) | 423.6 GB | 3.5 | T1,T2 | any | `hf download unsloth/DeepSeek-V4.1-Flash-1017-GGUF --include "*UD-IQ3_S*"` |
| `llm-deepseek-v4-1-flash-1017-nvfp4-nvfp4` | DeepSeek-V4.1-Flash-1017-NVFP4 · NVFP4 (NVFP4) | 429.0 GB | 4.5 | T1,T2 | server | `hf download nvidia/DeepSeek-V4.1-Flash-1017-NVFP4` |
| `llm-deepseek-v4-1-flash-1017-mlx-oq4e-mtp` | DeepSeek-V4.1-Flash-1017-oQ4e-mtp · oQ4e-mtp (MLX) | 432.0 GB | 4.5 | T1,T2 | mac | `hf download mlx-community/DeepSeek-V4.1-Flash-1017-oQ4e-mtp` |
| `llm-deepseek-v4-1-flash-1017-gguf-ud-q3-k-xl` | DeepSeek-V4.1-Flash-1017-GGUF · UD-Q3_K_XL (GGUF) | 485.1 GB | 3.5 | T1,T2 | any | `hf download unsloth/DeepSeek-V4.1-Flash-1017-GGUF --include "*UD-Q3_K_XL*"` |
| `llm-deepseek-v4-1-flash-1017-gguf-ud-q4-k-xl` | DeepSeek-V4.1-Flash-1017-GGUF · UD-Q4_K_XL (GGUF) | 500.7 GB | 4.5 | T1,T2 | any | `hf download unsloth/DeepSeek-V4.1-Flash-1017-GGUF --include "*UD-Q4_K_XL*"` |
| `llm-deepseek-v4-1-flash-1017-gguf-mxfp4-experts` | deepseek-v4.1-flash-gguf · MXFP4-experts (V4.1-Flash, nem 1017) (GGUF) | 501.6 GB | 4.5 | T1,T2 | any | `hf download antirez/deepseek-v4.1-flash-gguf --include "*MXFP4-experts*"` |
| `llm-deepseek-v4-1-flash-1017-mlx-mlxs` | DeepSeek-V4.1-Flash-1017-MLXs · MLXs (MLX) | 502.8 GB | 4.5 | T1,T2 | mac | `hf download inferencerlabs/DeepSeek-V4.1-Flash-1017-MLXs` |
| `llm-deepseek-v4-1-flash-1017-gguf-ud-q8-k-xl` | DeepSeek-V4.1-Flash-1017-GGUF · UD-Q8_K_XL (GGUF) | 508.4 GB | 8.5 | T1,T2 | any | `hf download unsloth/DeepSeek-V4.1-Flash-1017-GGUF --include "*UD-Q8_K_XL*"` |
| `llm-deepseek-v4-1-flash-1017-safetensors-native-fp8-int8` | DeepSeek-V4.1-Flash-1017 · FP8/INT8 native (safetensors(native)) | 510.3 GB | 8.5 | T1 | server | `hf download deepseek-ai/DeepSeek-V4.1-Flash-1017` |
</details>

<details><summary><b>GLM-5.3</b> – 25 változat</summary>

| id | Fájl / repó | Méret | Bit | HW | Platform | Letöltés |
|---|---|---|---|---|---|---|
| `llm-glm-5-3-gguf-ud-iq2-xxs` | glm-5.3-gguf · UD-IQ2_XXS mix (GGUF) | 211.1 GB | 2.6 | T1,T2 | any | `hf download antirez/glm-5.3-gguf --include "*UD-IQ2_XXS*"` |
| `llm-glm-5-3-gguf-ud-iq1-s` | GLM-5.3-GGUF · UD-IQ1_S (GGUF) | 216.7 GB | 1.7 | T1,T2,T3 | any | `hf download unsloth/GLM-5.3-GGUF --include "*UD-IQ1_S*"` |
| `llm-glm-5-3-gguf-ud-iq1-m` | GLM-5.3-GGUF · UD-IQ1_M (GGUF) | 228.5 GB | 1.7 | T1,T2 | any | `hf download unsloth/GLM-5.3-GGUF --include "*UD-IQ1_M*"` |
| `llm-glm-5-3-gguf-ud-iq2-m` | GLM-5.3-GGUF · UD-IQ2_M (GGUF) | 238.6 GB | 2.6 | T1,T2 | any | `hf download unsloth/GLM-5.3-GGUF --include "*UD-IQ2_M*"` |
| `llm-glm-5-3-gguf-ud-q2-k-xl` | GLM-5.3-GGUF · UD-Q2_K_XL (GGUF) | 253.9 GB | 2.6 | T1,T2 | any | `hf download unsloth/GLM-5.3-GGUF --include "*UD-Q2_K_XL*"` |
| `llm-glm-5-3-gguf-iq2-s` | GLM-5.3-GGUF · IQ2_S (GGUF) | 259.1 GB | 2.6 | T1,T2 | any | `hf download AesSedai/GLM-5.3-GGUF --include "*IQ2_S*"` |
| `llm-glm-5-3-gguf-ud-iq3-xxs` | GLM-5.3-GGUF · UD-IQ3_XXS (GGUF) | 281.7 GB | 3.5 | T1,T2 | any | `hf download unsloth/GLM-5.3-GGUF --include "*UD-IQ3_XXS*"` |
| `llm-glm-5-3-gguf-iq3-s` | GLM-5.3-GGUF · IQ3_S (GGUF) | 285.6 GB | 3.5 | T1,T2 | any | `hf download AesSedai/GLM-5.3-GGUF --include "*IQ3_S*"` |
| `llm-glm-5-3-gguf-ud-q3-k-xl` | GLM-5.3-GGUF · UD-Q3_K_XL (GGUF) | 343.0 GB | 3.5 | T1,T2 | any | `hf download unsloth/GLM-5.3-GGUF --include "*UD-Q3_K_XL*"` |
| `llm-glm-5-3-gguf-ud-iq4-xs` | GLM-5.3-GGUF · UD-IQ4_XS (GGUF) | 365.3 GB | 4.5 | T1,T2 | any | `hf download unsloth/GLM-5.3-GGUF --include "*UD-IQ4_XS*"` |
| `llm-glm-5-3-gguf-iq4-xs` | GLM-5.3-GGUF · IQ4_XS (GGUF) | 367.2 GB | 4.5 | T1,T2 | any | `hf download AesSedai/GLM-5.3-GGUF --include "*IQ4_XS*"` |
| `llm-glm-5-3-mxfp4-mxfp4` | GLM-5.3-MXFP4 · MXFP4 (MXFP4) | 403.4 GB | 4.5 | T1 | server | `hf download RedHatAI/GLM-5.3-MXFP4` |
| `llm-glm-5-3-mlx-4bit` | GLM-5.3-4bit · 4bit (MLX) | 418.3 GB | 4.5 | T1,T2 | mac | `hf download mlx-community/GLM-5.3-4bit` |
| `llm-glm-5-3-mlx-mixed` | GLM-5.3-mixed-4_5bit · mixed 4/5bit (MLX) | 450.7 GB | 5.5 | T1,T2 | mac | `hf download mlx-community/GLM-5.3-mixed-4_5bit` |
| `llm-glm-5-3-nvfp4-nvfp4` | GLM-5.3-NVFP4 · NVFP4 (NVFP4) | 464.2 GB | 4.5 | T1,T2 | server | `hf download nvidia/GLM-5.3-NVFP4` |
| `llm-glm-5-3-gguf-ud-q4-k-xl` | GLM-5.3-GGUF · UD-Q4_K_XL (GGUF) | 467.3 GB | 4.5 | T1,T2 | any | `hf download unsloth/GLM-5.3-GGUF --include "*UD-Q4_K_XL*"` |
| `llm-glm-5-3-gguf-q4-k-m` | GLM-5.3-GGUF · Q4_K_M (GGUF) | 469.2 GB | 4.5 | T1,T2 | any | `hf download AesSedai/GLM-5.3-GGUF --include "*Q4_K_M*"` |
| `llm-glm-5-3-awq-awq-int4` | GLM-5.3-AWQ-INT4 · AWQ-INT4 (AWQ) | 488.2 GB | 4.5 | T1 | server | `hf download cyankiwi/GLM-5.3-AWQ-INT4` |
| `llm-glm-5-3-gguf-q5-k-m` | GLM-5.3-GGUF · Q5_K_M (GGUF) | 561.6 GB | 5.5 | T1,T2 | any | `hf download AesSedai/GLM-5.3-GGUF --include "*Q5_K_M*"` |
| `llm-glm-5-3-gguf-ud-q5-k-xl` | GLM-5.3-GGUF · UD-Q5_K_XL (GGUF) | 562.5 GB | 5.5 | T1,T2 | any | `hf download unsloth/GLM-5.3-GGUF --include "*UD-Q5_K_XL*"` |
| `llm-glm-5-3-gguf-ud-q6-k-xl` | GLM-5.3-GGUF · UD-Q6_K_XL (GGUF) | 684.4 GB | 6.5 | T1,T2 | any | `hf download unsloth/GLM-5.3-GGUF --include "*UD-Q6_K_XL*"` |
| `llm-glm-5-3-fp8-native-fp8` | GLM-5.3 · FP8 (FP8(native)) | 755.7 GB | 8.5 | T1 | server | `hf download zai-org/GLM-5.3` |
| `llm-glm-5-3-gguf-q8-0` | GLM-5.3-GGUF · Q8_0 (GGUF) | 801.4 GB | 8.5 | T1,T2 | any | `hf download unsloth/GLM-5.3-GGUF --include "*Q8_0*"` |
| `llm-glm-5-3-bf16-bf16` | GLM-5.3-BF16 · BF16 (BF16) | 1.51 TB | 16 | T1 | server | `hf download zai-org/GLM-5.3-BF16` |
| `llm-glm-5-3-gguf-bf16` | GLM-5.3-GGUF · BF16 (GGUF) | 1.51 TB | 16 | T1,T2 | any | `hf download unsloth/GLM-5.3-GGUF --include "*BF16*"` |
</details>

<details><summary><b>Inkling 2 Small</b> – 13 változat</summary>

| id | Fájl / repó | Méret | Bit | HW | Platform | Letöltés |
|---|---|---|---|---|---|---|
| `llm-inkling-2-small-mlx-oq4e` | Inkling-2-Small-oQ4e · oQ4e (MLX) | 341.5 GB | 4.5 | T1,T2 | mac | `hf download mlx-community/Inkling-2-Small-oQ4e` |
| `llm-inkling-2-small-gguf-ud-iq1-s` | Inkling-2-Small-GGUF · UD-IQ1_S (GGUF) | 343.5 GB | 1.7 | T1,T2 | any | `hf download unsloth/Inkling-2-Small-GGUF --include "*UD-IQ1_S*"` |
| `llm-inkling-2-small-gguf-ud-iq1-m` | Inkling-2-Small-GGUF · UD-IQ1_M (GGUF) | 357.1 GB | 1.7 | T1,T2 | any | `hf download unsloth/Inkling-2-Small-GGUF --include "*UD-IQ1_M*"` |
| `llm-inkling-2-small-mlx-4bit` | Inkling-2-Small-4bit · 4bit (MLX) | 380.8 GB | 4.5 | T1,T2 | mac | `hf download mlx-community/Inkling-2-Small-4bit` |
| `llm-inkling-2-small-gguf-ud-iq2-xxs` | Inkling-2-Small-GGUF · UD-IQ2_XXS (GGUF) | 381.2 GB | 2.6 | T1,T2 | any | `hf download unsloth/Inkling-2-Small-GGUF --include "*UD-IQ2_XXS*"` |
| `llm-inkling-2-small-native-native` | Inkling-2-Small · native ~4bit (native) | 393.5 GB | 4.5 | T1,T2 | server | `hf download thinkingmachines/Inkling-2-Small` |
| `llm-inkling-2-small-gguf-ud-q2-k-xl` | Inkling-2-Small-GGUF · UD-Q2_K_XL (GGUF) | 409.9 GB | 2.6 | T1,T2 | any | `hf download unsloth/Inkling-2-Small-GGUF --include "*UD-Q2_K_XL*"` |
| `llm-inkling-2-small-gguf-ud-iq3-xxs` | Inkling-2-Small-GGUF · UD-IQ3_XXS (GGUF) | 452.0 GB | 3.5 | T1,T2 | any | `hf download unsloth/Inkling-2-Small-GGUF --include "*UD-IQ3_XXS*"` |
| `llm-inkling-2-small-gguf-ud-q3-k-xl` | Inkling-2-Small-GGUF · UD-Q3_K_XL (GGUF) | 570.3 GB | 3.5 | T1,T2 | any | `hf download unsloth/Inkling-2-Small-GGUF --include "*UD-Q3_K_XL*"` |
| `llm-inkling-2-small-mxfp8-mxfp8` | Inkling-2-Small-MXFP8 · MXFP8 (MXFP8) | 622.8 GB | 8.5 | T1 | server | `hf download thinkingmachines/Inkling-2-Small-MXFP8` |
| `llm-inkling-2-small-gguf-ud-q4-k-xl` | Inkling-2-Small-GGUF · UD-Q4_K_XL (GGUF) | 708.3 GB | 4.5 | T1,T2 | any | `hf download unsloth/Inkling-2-Small-GGUF --include "*UD-Q4_K_XL*"` |
| `llm-inkling-2-small-gguf-ud-q8-k-xl` | Inkling-2-Small-GGUF · UD-Q8_K_XL (GGUF) | 773.0 GB | 8.5 | T1,T2 | any | `hf download unsloth/Inkling-2-Small-GGUF --include "*UD-Q8_K_XL*"` |
| `llm-inkling-2-small-gguf-bf16` | Inkling-2-Small-GGUF · BF16 (GGUF) | 968.8 GB | 16 | T1,T2 | any | `hf download unsloth/Inkling-2-Small-GGUF --include "*BF16*"` |
</details>

<details><summary><b>Hy4 preview (Hunyuan)</b> – 6 változat</summary>

| id | Fájl / repó | Méret | Bit | HW | Platform | Letöltés |
|---|---|---|---|---|---|---|
| `llm-hy4-preview-gguf-tq1-0` | Hy4-preview-GGUF · TQ1_0 (GGUF) | 229.4 GB | 1.7 | T1,T2 | any | `hf download AngelSlim/Hy4-preview-GGUF --include "*TQ1_0*"` |
| `llm-hy4-preview-gguf-ud-iq1-m` | Hy4-preview-GGUF · UD-IQ1_M (GGUF) | 235.3 GB | 1.7 | T1,T2 | any | `hf download AngelSlim/Hy4-preview-GGUF --include "*UD-IQ1_M*"` |
| `llm-hy4-preview-mlx-4bit` | Hy4-preview-4bit · 4bit (MLX) | 433.4 GB | 4.5 | T1,T2 | mac | `hf download mlx-community/Hy4-preview-4bit` |
| `llm-hy4-preview-gguf-q4-k-m` | Hy4-preview-GGUF · Q4_K_M (GGUF) | 467.3 GB | 4.5 | T1,T2 | any | `hf download AngelSlim/Hy4-preview-GGUF --include "*Q4_K_M*"` |
| `llm-hy4-preview-fp8-fp8` | Hy4-preview-FP8 · FP8 (FP8) | 813.8 GB | 8.5 | T1 | server | `hf download tencent/Hy4-preview-FP8` |
| `llm-hy4-preview-bf16-bf16` | Hy4-preview · BF16 (BF16) | 1.56 TB | 16 | T1 | server | `hf download tencent/Hy4-preview` |
</details>

<details><summary><b>LongCat-2.5 (csak megjegyzésként)</b> – 1 változat</summary>

| id | Fájl / repó | Méret | Bit | HW | Platform | Letöltés |
|---|---|---|---|---|---|---|
| `llm-longcat-2-5-w4a4-w4a4` | LongCat-2.5-W4A4 · W4A4 (FlatQuant) (W4A4) | 1.34 TB | 4.5 | T1 | server | `hf download meituan-longcat/LongCat-2.5-W4A4` |
</details>

<details><summary><b>MiMo-V2.6-Pro (RL és MOPD változat) + MiMo-V2.6-Flash</b> – 18 változat</summary>

| id | Fájl / repó | Méret | Bit | HW | Platform | Letöltés |
|---|---|---|---|---|---|---|
| `llm-mimo-v2-6-pro-gguf-flash-q2-k` | MiMo-V2.6-Flash-RL-GGUF · Q2_K (GGUF(Flash)) | 126.4 GB | 2.6 | T1,T2,T3 | any | `hf download ggml-org/MiMo-V2.6-Flash-RL-GGUF --include "*Q2_K*"` |
| `llm-mimo-v2-6-pro-mlx-flash-mxfp4-q8` | MiMo-V2.6-Flash-RL-mxfp4-q8 · mxfp4-q8 (MLX(Flash)) | 167.3 GB | 4.5 | T1,T2 | mac | `hf download mlx-community/MiMo-V2.6-Flash-RL-mxfp4-q8` |
| `llm-mimo-v2-6-pro-gguf-flash-mxfp4` | MiMo-V2.6-Flash-RL-GGUF · MXFP4 (GGUF(Flash)) | 167.4 GB | 4.5 | T1,T2,T3 | any | `hf download ggml-org/MiMo-V2.6-Flash-RL-GGUF --include "*MXFP4*"` |
| `llm-mimo-v2-6-pro-gguf-bpw2-0` | MiMo-V2.6-Pro-MOPD-GGUF · BPW2.0 (GGUF) | 255.8 GB | 2.5 | T1,T2 | any | `hf download AesSedai/MiMo-V2.6-Pro-MOPD-GGUF --include "*BPW2.0*"` |
| `llm-mimo-v2-6-pro-gguf-bpw2-5` | MiMo-V2.6-Pro-MOPD-GGUF · BPW2.5 (GGUF) | 319.6 GB | 3.0 | T1,T2 | any | `hf download AesSedai/MiMo-V2.6-Pro-MOPD-GGUF --include "*BPW2.5*"` |
| `llm-mimo-v2-6-pro-gguf-q2-k` | XiaomiMiMo.MiMo-V2.6-Pro-RL-GGUF · Q2_K (GGUF) | 373.5 GB | 2.6 | T1,T2 | any | `hf download DevQuasar/XiaomiMiMo.MiMo-V2.6-Pro-RL-GGUF --include "*Q2_K*"` |
| `llm-mimo-v2-6-pro-gguf-bpw3-0` | MiMo-V2.6-Pro-MOPD-GGUF · BPW3.0 (GGUF) | 383.4 GB | 3.5 | T1,T2 | any | `hf download AesSedai/MiMo-V2.6-Pro-MOPD-GGUF --include "*BPW3.0*"` |
| `llm-mimo-v2-6-pro-gguf-q2-k-2` | MiMo-V2.6-Pro-MOPD-GGUF · Q2_K (GGUF) | 418.8 GB | 2.6 | T1,T2 | any | `hf download ggml-org/MiMo-V2.6-Pro-MOPD-GGUF --include "*Q2_K*"` |
| `llm-mimo-v2-6-pro-gguf-bpw3-5` | MiMo-V2.6-Pro-MOPD-GGUF · BPW3.5 (GGUF) | 447.5 GB | 4.0 | T1,T2 | any | `hf download AesSedai/MiMo-V2.6-Pro-MOPD-GGUF --include "*BPW3.5*"` |
| `llm-mimo-v2-6-pro-gguf-q5-k-m` | XiaomiMiMo.MiMo-V2.6-Pro-RL-GGUF · Q5_K_M (GGUF) | 489.3 GB | 5.5 | T1,T2 | any | `hf download DevQuasar/XiaomiMiMo.MiMo-V2.6-Pro-RL-GGUF --include "*Q5_K_M*"` |
| `llm-mimo-v2-6-pro-mlx-mxfp4-q8` | MiMo-V2.6-Pro-RL-mxfp4-q8 · mxfp4-q8 (MLX) | 553.9 GB | 4.5 | T1,T2 | mac | `hf download mlx-community/MiMo-V2.6-Pro-RL-mxfp4-q8` |
| `llm-mimo-v2-6-pro-gguf-mxfp4` | MiMo-V2.6-Pro-MOPD-GGUF · MXFP4 (GGUF) | 554.2 GB | 4.5 | T1,T2 | any | `hf download ggml-org/MiMo-V2.6-Pro-MOPD-GGUF --include "*MXFP4*"` |
| `llm-mimo-v2-6-pro-gguf-mxfp4-moe` | XiaomiMiMo.MiMo-V2.6-Pro-RL-GGUF · MXFP4_MOE (GGUF) | 554.2 GB | 4.5 | T1,T2 | any | `hf download DevQuasar/XiaomiMiMo.MiMo-V2.6-Pro-RL-GGUF --include "*MXFP4_MOE*"` |
| `llm-mimo-v2-6-pro-mlx-q9` | MiMo-V2.6-Pro-RL-MLX-Q9 · Q9 (MLX) | 556.7 GB | 4.5 | T1,T2 | mac | `hf download inferencerlabs/MiMo-V2.6-Pro-RL-MLX-Q9` |
| `llm-mimo-v2-6-pro-safetensors-native-native` | MiMo-V2.6-Pro-RL · native (safetensors(native)) | 573.5 GB | 16 | T1 | server | `hf download XiaomiMiMo/MiMo-V2.6-Pro-RL` |
| `llm-mimo-v2-6-pro-safetensors-native-native-2` | MiMo-V2.6-Pro-MOPD · native (safetensors(native)) | 573.5 GB | 16 | T1 | server | `hf download XiaomiMiMo/MiMo-V2.6-Pro-MOPD` |
| `llm-mimo-v2-6-pro-gguf-mxfp4-2` | MiMo-V2.6-Pro-MOPD-GGUF · MXFP4 (GGUF) | 577.7 GB | 4.5 | T1,T2 | any | `hf download AesSedai/MiMo-V2.6-Pro-MOPD-GGUF --include "*MXFP4*"` |
| `llm-mimo-v2-6-pro-gguf-q4-k-m` | XiaomiMiMo.MiMo-V2.6-Pro-RL-GGUF · Q4_K_M (GGUF) | 617.9 GB | 4.5 | T1,T2 | any | `hf download DevQuasar/XiaomiMiMo.MiMo-V2.6-Pro-RL-GGUF --include "*Q4_K_M*"` |
</details>

<details><summary><b>Ling-3.1-flash-1019</b> – 18 változat</summary>

| id | Fájl / repó | Méret | Bit | HW | Platform | Letöltés |
|---|---|---|---|---|---|---|
| `llm-ling-3-1-flash-1019-gguf-iq1-s` | Ling-3.1-flash-1019-GGUF · IQ1_S (GGUF) | 131.0 GB | 1.7 | T1,T2,T3 | any | `hf download bartowski/Ling-3.1-flash-1019-GGUF --include "*IQ1_S*"` |
| `llm-ling-3-1-flash-1019-gguf-iq1-m` | Ling-3.1-flash-1019-GGUF · IQ1_M (GGUF) | 145.1 GB | 1.7 | T1,T2,T3 | any | `hf download bartowski/Ling-3.1-flash-1019-GGUF --include "*IQ1_M*"` |
| `llm-ling-3-1-flash-1019-gguf-iq2-xxs` | Ling-3.1-flash-1019-GGUF · IQ2_XXS (GGUF) | 170.8 GB | 2.6 | T1,T2,T3 | any | `hf download bartowski/Ling-3.1-flash-1019-GGUF --include "*IQ2_XXS*"` |
| `llm-ling-3-1-flash-1019-mlx-oq2e-mtp` | Ling-3.1-flash-1019-oQ2e-mtp · oQ2e-mtp (MLX) | 193.2 GB | 2.5 | T1,T2 | mac | `hf download mlx-community/Ling-3.1-flash-1019-oQ2e-mtp` |
| `llm-ling-3-1-flash-1019-gguf-iq2-m` | Ling-3.1-flash-1019-GGUF · IQ2_M (GGUF) | 213.0 GB | 2.6 | T1,T2,T3 | any | `hf download bartowski/Ling-3.1-flash-1019-GGUF --include "*IQ2_M*"` |
| `llm-ling-3-1-flash-1019-gguf-q2-k` | Ling-3.1-flash-1019-GGUF · Q2_K (GGUF) | 219.2 GB | 2.6 | T1,T2,T3 | any | `hf download bartowski/Ling-3.1-flash-1019-GGUF --include "*Q2_K*"` |
| `llm-ling-3-1-flash-1019-mlx-oq2-5e-mtp` | Ling-3.1-flash-1019-oQ2.5e-mtp · oQ2.5e-mtp (MLX) | 224.0 GB | 3.0 | T1,T2 | mac | `hf download mlx-community/Ling-3.1-flash-1019-oQ2.5e-mtp` |
| `llm-ling-3-1-flash-1019-gguf-iq3-xxs` | Ling-3.1-flash-1019-GGUF · IQ3_XXS (GGUF) | 247.4 GB | 3.5 | T1,T2 | any | `hf download bartowski/Ling-3.1-flash-1019-GGUF --include "*IQ3_XXS*"` |
| `llm-ling-3-1-flash-1019-mlx-oq3e-mtp` | Ling-3.1-flash-1019-oQ3e-mtp · oQ3e-mtp (MLX) | 261.6 GB | 3.5 | T1,T2 | mac | `hf download mlx-community/Ling-3.1-flash-1019-oQ3e-mtp` |
| `llm-ling-3-1-flash-1019-gguf-q3-k-m` | Ling-3.1-flash-1019-GGUF · Q3_K_M (GGUF) | 275.1 GB | 3.5 | T1,T2 | any | `hf download bartowski/Ling-3.1-flash-1019-GGUF --include "*Q3_K_M*"` |
| `llm-ling-3-1-flash-1019-gguf-iq3-m` | Ling-3.1-flash-1019-GGUF · IQ3_M (GGUF) | 297.3 GB | 3.5 | T1,T2 | any | `hf download bartowski/Ling-3.1-flash-1019-GGUF --include "*IQ3_M*"` |
| `llm-ling-3-1-flash-1019-gguf-iq4-xs` | Ling-3.1-flash-1019-GGUF · IQ4_XS (GGUF) | 317.1 GB | 4.5 | T1,T2 | any | `hf download bartowski/Ling-3.1-flash-1019-GGUF --include "*IQ4_XS*"` |
| `llm-ling-3-1-flash-1019-mlx-oq4e-mtp` | Ling-3.1-flash-1019-oQ4e-mtp · oQ4e-mtp (MLX) | 330.1 GB | 4.5 | T1,T2 | mac | `hf download mlx-community/Ling-3.1-flash-1019-oQ4e-mtp` |
| `llm-ling-3-1-flash-1019-gguf-q4-k-m` | Ling-3.1-flash-1019-GGUF · Q4_K_M (GGUF) | 358.0 GB | 4.5 | T1,T2 | any | `hf download bartowski/Ling-3.1-flash-1019-GGUF --include "*Q4_K_M*"` |
| `llm-ling-3-1-flash-1019-gguf-q5-k-m` | Ling-3.1-flash-1019-GGUF · Q5_K_M (GGUF) | 436.3 GB | 5.5 | T1,T2 | any | `hf download bartowski/Ling-3.1-flash-1019-GGUF --include "*Q5_K_M*"` |
| `llm-ling-3-1-flash-1019-gguf-q6-k` | Ling-3.1-flash-1019-GGUF · Q6_K (GGUF) | 501.6 GB | 6.5 | T1,T2 | any | `hf download bartowski/Ling-3.1-flash-1019-GGUF --include "*Q6_K*"` |
| `llm-ling-3-1-flash-1019-fp8-native-fp8` | Ling-3.1-flash-1019 · FP8 (FP8(native)) | 573.8 GB | 8.5 | T1 | server | `hf download inclusionAI/Ling-3.1-flash-1019` |
| `llm-ling-3-1-flash-1019-gguf-q8-0` | Ling-3.1-flash-1019-GGUF · Q8_0 (GGUF) | 608.4 GB | 8.5 | T1,T2 | any | `hf download bartowski/Ling-3.1-flash-1019-GGUF --include "*Q8_0*"` |
</details>

<details><summary><b>MiniMax-M3.1-Flash</b> – 16 változat</summary>

| id | Fájl / repó | Méret | Bit | HW | Platform | Letöltés |
|---|---|---|---|---|---|---|
| `llm-minimax-m3-1-flash-gguf-ud-iq1-m` | MiniMax-M3.1-Flash-GGUF · UD-IQ1_M (GGUF) | 129.4 GB | 1.7 | T1,T2,T3 | any | `hf download unsloth/MiniMax-M3.1-Flash-GGUF --include "*UD-IQ1_M*"` |
| `llm-minimax-m3-1-flash-gguf-ud-iq2-xxs` | MiniMax-M3.1-Flash-GGUF · UD-IQ2_XXS (GGUF) | 134.9 GB | 2.6 | T1,T2,T3 | any | `hf download unsloth/MiniMax-M3.1-Flash-GGUF --include "*UD-IQ2_XXS*"` |
| `llm-minimax-m3-1-flash-gguf-ud-q2-k-xl` | MiniMax-M3.1-Flash-GGUF · UD-Q2_K_XL (GGUF) | 143.9 GB | 2.6 | T1,T2,T3 | any | `hf download unsloth/MiniMax-M3.1-Flash-GGUF --include "*UD-Q2_K_XL*"` |
| `llm-minimax-m3-1-flash-gguf-q2-k` | MiniMaxAI.MiniMax-M3.1-Flash-GGUF · Q2_K (GGUF) | 156.0 GB | 2.6 | T1,T2,T3 | any | `hf download DevQuasar/MiniMaxAI.MiniMax-M3.1-Flash-GGUF --include "*Q2_K*"` |
| `llm-minimax-m3-1-flash-gguf-ud-iq3-xxs` | MiniMax-M3.1-Flash-GGUF · UD-IQ3_XXS (GGUF) | 160.1 GB | 3.5 | T1,T2,T3 | any | `hf download unsloth/MiniMax-M3.1-Flash-GGUF --include "*UD-IQ3_XXS*"` |
| `llm-minimax-m3-1-flash-gguf-ud-iq3-s` | MiniMax-M3.1-Flash-GGUF · UD-IQ3_S (GGUF) | 175.4 GB | 3.5 | T1,T2,T3 | any | `hf download unsloth/MiniMax-M3.1-Flash-GGUF --include "*UD-IQ3_S*"` |
| `llm-minimax-m3-1-flash-mlx-3bit` | MiniMax-M3.1-Flash-Text-3bit · 3bit (text-only) (MLX) | 186.5 GB | 3.5 | T1,T2 | mac | `hf download mlx-community/MiniMax-M3.1-Flash-Text-3bit` |
| `llm-minimax-m3-1-flash-gguf-ud-q3-k-xl` | MiniMax-M3.1-Flash-GGUF · UD-Q3_K_XL (GGUF) | 193.9 GB | 3.5 | T1,T2,T3 | any | `hf download unsloth/MiniMax-M3.1-Flash-GGUF --include "*UD-Q3_K_XL*"` |
| `llm-minimax-m3-1-flash-mlx-oq3e-mtp` | MiniMax-M3.1-Flash-oQ3e-mtp · oQ3e-mtp (MLX) | 196.2 GB | 3.5 | T1,T2 | mac | `hf download mlx-community/MiniMax-M3.1-Flash-oQ3e-mtp` |
| `llm-minimax-m3-1-flash-gguf-q3-k-m` | MiniMaxAI.MiniMax-M3.1-Flash-GGUF · Q3_K_M (GGUF) | 203.5 GB | 3.5 | T1,T2,T3 | any | `hf download DevQuasar/MiniMaxAI.MiniMax-M3.1-Flash-GGUF --include "*Q3_K_M*"` |
| `llm-minimax-m3-1-flash-mlx-oq3-5e-mtp` | MiniMax-M3.1-Flash-oQ3.5e-mtp · oQ3.5e-mtp (MLX) | 213.4 GB | 4.0 | T1,T2 | mac | `hf download mlx-community/MiniMax-M3.1-Flash-oQ3.5e-mtp` |
| `llm-minimax-m3-1-flash-mxfp4-mxfp4` | MiniMax-M3.1-Flash-Quark-MXFP4 · MXFP4 (MXFP4) | 239.5 GB | 4.5 | T1,T2 | server | `hf download amd/MiniMax-M3.1-Flash-Quark-MXFP4` |
| `llm-minimax-m3-1-flash-mlx-4bit` | MiniMax-M3.1-Flash-Text-4bit · 4bit (text-only) (MLX) | 248.4 GB | 4.5 | T1,T2 | mac | `hf download mlx-community/MiniMax-M3.1-Flash-Text-4bit` |
| `llm-minimax-m3-1-flash-mlx-oq4e-mtp` | MiniMax-M3.1-Flash-oQ4e-mtp · oQ4e-mtp (MLX) | 248.8 GB | 4.5 | T1,T2 | mac | `hf download mlx-community/MiniMax-M3.1-Flash-oQ4e-mtp` |
| `llm-minimax-m3-1-flash-safetensors-native-native` | MiniMax-M3.1-Flash · native ~4bit (safetensors(native)) | 252.4 GB | 4.5 | T1,T2 | server | `hf download MiniMaxAI/MiniMax-M3.1-Flash` |
| `llm-minimax-m3-1-flash-gguf-q5-k-m` | MiniMaxAI.MiniMax-M3.1-Flash-GGUF · Q5_K_M (GGUF) | 302.9 GB | 5.5 | T1,T2,T3 | any | `hf download DevQuasar/MiniMaxAI.MiniMax-M3.1-Flash-GGUF --include "*Q5_K_M*"` |
</details>

<details><summary><b>Qwen3.8-Flash-Next</b> – 57 változat</summary>

| id | Fájl / repó | Méret | Bit | HW | Platform | Letöltés |
|---|---|---|---|---|---|---|
| `llm-qwen3-8-flash-next-gguf-ud-iq1-s` | Qwen3.8-Flash-Next-GGUF · UD-IQ1_S (GGUF) | 66.4 GB | 1.7 | T1,T2,T3,T4 | any | `hf download unsloth/Qwen3.8-Flash-Next-GGUF --include "*UD-IQ1_S*"` |
| `llm-qwen3-8-flash-next-gguf-q2-0` | Qwen3.8-Flash-Next-GSQ-RCO-GGUF · Q2_0 (GGUF) | 66.4 GB | 2.6 | T1,T2,T3 | any | `hf download ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF --include "*Q2_0*"` |
| `llm-qwen3-8-flash-next-gguf-ud-iq1-m` | Qwen3.8-Flash-Next-GGUF · UD-IQ1_M (GGUF) | 68.0 GB | 1.7 | T1,T2,T3,T4 | any | `hf download unsloth/Qwen3.8-Flash-Next-GGUF --include "*UD-IQ1_M*"` |
| `llm-qwen3-8-flash-next-gguf-iq2-xs` | Qwen3.8-Flash-Next-GSQ-RCO-GGUF · IQ2_XS (GGUF) | 68.0 GB | 2.6 | T1,T2,T3 | any | `hf download ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF --include "*IQ2_XS*"` |
| `llm-qwen3-8-flash-next-gguf-iq1-s` | Qwen3.8-Flash-Next-GGUF · IQ1_S (GGUF) | 70.1 GB | 1.7 | T1,T2,T3 | any | `hf download bartowski/Qwen3.8-Flash-Next-GGUF --include "*IQ1_S*"` |
| `llm-qwen3-8-flash-next-gguf-ud-q2-0` | Qwen3.8-Flash-Next-GGUF · UD-Q2_0 (GGUF) | 70.5 GB | 2.6 | T1,T2,T3,T4 | any | `hf download unsloth/Qwen3.8-Flash-Next-GGUF --include "*UD-Q2_0*"` |
| `llm-qwen3-8-flash-next-gguf-ud-iq2-xs` | Qwen3.8-Flash-Next-GGUF · UD-IQ2_XS (GGUF) | 75.8 GB | 2.6 | T1,T2,T3,T4 | any | `hf download unsloth/Qwen3.8-Flash-Next-GGUF --include "*UD-IQ2_XS*"` |
| `llm-qwen3-8-flash-next-gguf-iq3-xxs` | Qwen3.8-Flash-Next-GSQ-RCO-GGUF · IQ3_XXS (GGUF) | 75.8 GB | 3.5 | T1,T2,T3 | any | `hf download ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF --include "*IQ3_XXS*"` |
| `llm-qwen3-8-flash-next-gguf-ud-q2-k-xl` | Qwen3.8-Flash-Next-GGUF · UD-Q2_K_XL (GGUF) | 79.6 GB | 2.6 | T1,T2,T3,T4 | any | `hf download unsloth/Qwen3.8-Flash-Next-GGUF --include "*UD-Q2_K_XL*"` |
| `llm-qwen3-8-flash-next-gguf-iq2-m` | Qwen3.8-Flash-Next-GGUF · IQ2_M (GGUF) | 80.4 GB | 2.6 | T1,T2,T3 | any | `hf download bartowski/Qwen3.8-Flash-Next-GGUF --include "*IQ2_M*"` |
| `llm-qwen3-8-flash-next-gguf-i1-q2-k` | Qwen3.8-Flash-Next-i1-GGUF · i1-Q2_K (GGUF) | 80.5 GB | 2.6 | T1,T2,T3 | any | `hf download mradermacher/Qwen3.8-Flash-Next-i1-GGUF --include "*i1-Q2_K*"` |
| `llm-qwen3-8-flash-next-gguf-q2-k` | Qwen3.8-Flash-Next-GGUF · Q2_K (GGUF) | 80.5 GB | 2.6 | T1,T2,T3 | any | `hf download mradermacher/Qwen3.8-Flash-Next-GGUF --include "*Q2_K*"` |
| `llm-qwen3-8-flash-next-mlx-optiq-2bit` | Qwen3.8-Flash-Next-OptiQ-2bit · OptiQ-2bit (MLX) | 80.8 GB | 2.5 | T1,T2,T3,T4 | mac | `hf download mlx-community/Qwen3.8-Flash-Next-OptiQ-2bit` |
| `llm-qwen3-8-flash-next-gguf-q2-k-2` | Qwen3.8-Flash-Next-GGUF · Q2_K (GGUF) | 80.9 GB | 2.6 | T1,T2,T3 | any | `hf download bartowski/Qwen3.8-Flash-Next-GGUF --include "*Q2_K*"` |
| `llm-qwen3-8-flash-next-gguf-q2-k-3` | Qwen3.8-Flash-Next-GGUF · Q2_K (GGUF) | 83.1 GB | 2.6 | T1,T2,T3 | any | `hf download ggml-org/Qwen3.8-Flash-Next-GGUF --include "*Q2_K*"` |
| `llm-qwen3-8-flash-next-gguf-iq3-s` | Qwen3.8-Flash-Next-GSQ-RCO-GGUF · IQ3_S (GGUF) | 83.6 GB | 3.5 | T1,T2,T3 | any | `hf download ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF --include "*IQ3_S*"` |
| `llm-qwen3-8-flash-next-gguf-ud-iq3-xxs` | Qwen3.8-Flash-Next-GGUF · UD-IQ3_XXS (GGUF) | 83.6 GB | 3.5 | T1,T2,T3 | any | `hf download unsloth/Qwen3.8-Flash-Next-GGUF --include "*UD-IQ3_XXS*"` |
| `llm-qwen3-8-flash-next-gguf-q4-0` | Qwen3.8-Flash-Next-GGUF · Q4_0 (GGUF) | 85.7 GB | 4.5 | T1,T2,T3 | any | `hf download AesSedai/Qwen3.8-Flash-Next-GGUF --include "*Q4_0*"` |
| `llm-qwen3-8-flash-next-gguf-ud-q3-k-xl` | Qwen3.8-Flash-Next-GGUF · UD-Q3_K_XL (GGUF) | 89.5 GB | 3.5 | T1,T2,T3 | any | `hf download unsloth/Qwen3.8-Flash-Next-GGUF --include "*UD-Q3_K_XL*"` |
| `llm-qwen3-8-flash-next-gguf-i1-iq3-m` | Qwen3.8-Flash-Next-i1-GGUF · i1-IQ3_M (GGUF) | 89.5 GB | 3.5 | T1,T2,T3 | any | `hf download mradermacher/Qwen3.8-Flash-Next-i1-GGUF --include "*i1-IQ3_M*"` |
| `llm-qwen3-8-flash-next-gguf-iq3-m` | Qwen3.8-Flash-Next-GGUF · IQ3_M (GGUF) | 93.2 GB | 3.5 | T1,T2,T3 | any | `hf download bartowski/Qwen3.8-Flash-Next-GGUF --include "*IQ3_M*"` |
| `llm-qwen3-8-flash-next-gguf-ud-iq4-xs` | Qwen3.8-Flash-Next-GGUF · UD-IQ4_XS (GGUF) | 93.7 GB | 4.5 | T1,T2,T3 | any | `hf download unsloth/Qwen3.8-Flash-Next-GGUF --include "*UD-IQ4_XS*"` |
| `llm-qwen3-8-flash-next-gguf-i1-iq4-xs` | Qwen3.8-Flash-Next-i1-GGUF · i1-IQ4_XS (GGUF) | 97.5 GB | 4.5 | T1,T2,T3 | any | `hf download mradermacher/Qwen3.8-Flash-Next-i1-GGUF --include "*i1-IQ4_XS*"` |
| `llm-qwen3-8-flash-next-gguf-iq4-xs` | Qwen3.8-Flash-Next-GGUF · IQ4_XS (GGUF) | 97.7 GB | 4.5 | T1,T2,T3 | any | `hf download bartowski/Qwen3.8-Flash-Next-GGUF --include "*IQ4_XS*"` |
| `llm-qwen3-8-flash-next-gguf-iq4-nl` | Qwen3.8-Flash-Next-GGUF · IQ4_NL (GGUF) | 102.0 GB | 4.5 | T1,T2,T3 | any | `hf download ggml-org/Qwen3.8-Flash-Next-GGUF --include "*IQ4_NL*"` |
| `llm-qwen3-8-flash-next-ollama-ollama` |  · ollama qwen3.8-flash-next:125b-a6b-nvfp4 (ollama) | 104.8 GB | 4.5 | T1,T2,T3 | any | `ollama pull qwen3.8-flash-next:125b-a6b-nvfp4 / 125b-mlx` |
| `llm-qwen3-8-flash-next-gguf-ud-q4-k-xl` | Qwen3.8-Flash-Next-GGUF · UD-Q4_K_XL (GGUF) | 111.3 GB | 4.5 | T1,T2,T3 | any | `hf download unsloth/Qwen3.8-Flash-Next-GGUF --include "*UD-Q4_K_XL*"` |
| `llm-qwen3-8-flash-next-mlx-4bit` | Qwen3.8-Flash-Next-4bit · 4bit (MLX) | 111.5 GB | 4.5 | T1,T2,T3,T4 | mac | `hf download mlx-community/Qwen3.8-Flash-Next-4bit` |
| `llm-qwen3-8-flash-next-gguf-q4-k-m` | Qwen3.8-Flash-Next-GGUF · Q4_K_M (GGUF) | 119.2 GB | 4.5 | T1,T2,T3 | any | `hf download lmstudio-community/Qwen3.8-Flash-Next-GGUF --include "*Q4_K_M*"` |
| `llm-qwen3-8-flash-next-gguf-i1-q4-k-m` | Qwen3.8-Flash-Next-i1-GGUF · i1-Q4_K_M (GGUF) | 119.2 GB | 4.5 | T1,T2,T3 | any | `hf download mradermacher/Qwen3.8-Flash-Next-i1-GGUF --include "*i1-Q4_K_M*"` |
| `llm-qwen3-8-flash-next-gguf-q4-k-m-2` | Qwen3.8-Flash-Next-GGUF · Q4_K_M (GGUF) | 119.2 GB | 4.5 | T1,T2,T3 | any | `hf download mradermacher/Qwen3.8-Flash-Next-GGUF --include "*Q4_K_M*"` |
| `llm-qwen3-8-flash-next-gguf-q4-k-m-3` | Qwen3.8-Flash-Next-GGUF · Q4_K_M (GGUF) | 119.6 GB | 4.5 | T1,T2,T3 | any | `hf download bartowski/Qwen3.8-Flash-Next-GGUF --include "*Q4_K_M*"` |
| `llm-qwen3-8-flash-next-ollama-ollama-2` |  · ollama qwen3.8-flash-next:125b-a6b-q4_K_ (ollama) | 120.1 GB | 4.5 | T1,T2,T3 | any | `ollama pull qwen3.8-flash-next:125b-a6b-q4_K_M` |
| `llm-qwen3-8-flash-next-nvfp4-nvfp4` | Qwen3.8-Flash-Next-NVFP4 · NVFP4 (NVFP4) | 132.7 GB | 4.5 | T1,T2,T3 | server | `hf download nvidia/Qwen3.8-Flash-Next-NVFP4` |
| `llm-qwen3-8-flash-next-gguf-i1-q5-k-m` | Qwen3.8-Flash-Next-i1-GGUF · i1-Q5_K_M (GGUF) | 134.1 GB | 5.5 | T1,T2,T3 | any | `hf download mradermacher/Qwen3.8-Flash-Next-i1-GGUF --include "*i1-Q5_K_M*"` |
| `llm-qwen3-8-flash-next-gguf-q5-k-m` | Qwen3.8-Flash-Next-GGUF · Q5_K_M (GGUF) | 134.7 GB | 5.5 | T1,T2,T3 | any | `hf download bartowski/Qwen3.8-Flash-Next-GGUF --include "*Q5_K_M*"` |
| `llm-qwen3-8-flash-next-mlx-oq6e-mtp` | Qwen3.8-Flash-Next-oQ6e-mtp · oQ6e-mtp (MLX) | 150.5 GB | 6.5 | T1,T2 | mac | `hf download mlx-community/Qwen3.8-Flash-Next-oQ6e-mtp` |
| `llm-qwen3-8-flash-next-gguf-ud-q5-k-xl` | Qwen3.8-Flash-Next-GGUF · UD-Q5_K_XL (GGUF) | 158.3 GB | 5.5 | T1,T2,T3 | any | `hf download unsloth/Qwen3.8-Flash-Next-GGUF --include "*UD-Q5_K_XL*"` |
| `llm-qwen3-8-flash-next-gguf-q8-0` | Qwen3.8-Flash-Next-GGUF · Q8_0 (GGUF) | 162.6 GB | 8.5 | T1,T2,T3 | any | `hf download ggml-org/Qwen3.8-Flash-Next-GGUF --include "*Q8_0*"` |
| `llm-qwen3-8-flash-next-gguf-q5-k-m-2` | Qwen3.8-Flash-Next-GGUF · Q5_K_M (GGUF) | 164.4 GB | 5.5 | T1,T2,T3 | any | `hf download AesSedai/Qwen3.8-Flash-Next-GGUF --include "*Q5_K_M*"` |
| `llm-qwen3-8-flash-next-gguf-q6-k` | Qwen3.8-Flash-Next-GGUF · Q6_K (GGUF) | 167.6 GB | 6.5 | T1,T2,T3 | any | `hf download lmstudio-community/Qwen3.8-Flash-Next-GGUF --include "*Q6_K*"` |
| `llm-qwen3-8-flash-next-gguf-i1-q6-k` | Qwen3.8-Flash-Next-i1-GGUF · i1-Q6_K (GGUF) | 167.6 GB | 6.5 | T1,T2,T3 | any | `hf download mradermacher/Qwen3.8-Flash-Next-i1-GGUF --include "*i1-Q6_K*"` |
| `llm-qwen3-8-flash-next-gguf-q6-k-2` | Qwen3.8-Flash-Next-GGUF · Q6_K (GGUF) | 168.1 GB | 6.5 | T1,T2,T3 | any | `hf download bartowski/Qwen3.8-Flash-Next-GGUF --include "*Q6_K*"` |
| `llm-qwen3-8-flash-next-gguf-ud-q6-k-xl` | Qwen3.8-Flash-Next-GGUF · UD-Q6_K_XL (GGUF) | 169.2 GB | 6.5 | T1,T2,T3 | any | `hf download unsloth/Qwen3.8-Flash-Next-GGUF --include "*UD-Q6_K_XL*"` |
| `llm-qwen3-8-flash-next-autoround-w4a16` | Qwen3.8-Flash-Next-W4A16-AutoRound · W4A16 (AutoRound) | 181.2 GB | 4.5 | T1,T2 | server | `hf download Intel/Qwen3.8-Flash-Next-W4A16-AutoRound` |
| `llm-qwen3-8-flash-next-fp8-fp8` | Qwen3.8-Flash-Next-FP8 · FP8 (FP8) | 185.6 GB | 8.5 | T1,T2 | server | `hf download Qwen/Qwen3.8-Flash-Next-FP8` |
| `llm-qwen3-8-flash-next-nvfp4-nvfp4-2` | Qwen3.8-Flash-Next-NVFP4 · NVFP4 (NVFP4) | 186.4 GB | 4.5 | T1,T2 | server | `hf download RedHatAI/Qwen3.8-Flash-Next-NVFP4` |
| `llm-qwen3-8-flash-next-gguf-q8-0-2` | Qwen3.8-Flash-Next-GGUF · Q8_0 (GGUF) | 188.2 GB | 8.5 | T1,T2,T3 | any | `hf download lmstudio-community/Qwen3.8-Flash-Next-GGUF --include "*Q8_0*"` |
| `llm-qwen3-8-flash-next-gguf-q8-0-3` | Qwen3.8-Flash-Next-GGUF · Q8_0 (GGUF) | 188.2 GB | 8.5 | T1,T2,T3 | any | `hf download mradermacher/Qwen3.8-Flash-Next-GGUF --include "*Q8_0*"` |
| `llm-qwen3-8-flash-next-gguf-q8-0-4` | Qwen3.8-Flash-Next-GGUF · Q8_0 (GGUF) | 188.2 GB | 8.5 | T1,T2,T3 | any | `hf download unsloth/Qwen3.8-Flash-Next-GGUF --include "*Q8_0*"` |
| `llm-qwen3-8-flash-next-gguf-q8-0-5` | Qwen3.8-Flash-Next-GGUF · Q8_0 (GGUF) | 188.3 GB | 8.5 | T1,T2,T3 | any | `hf download bartowski/Qwen3.8-Flash-Next-GGUF --include "*Q8_0*"` |
| `llm-qwen3-8-flash-next-awq-awq-int4` | Qwen3.8-Flash-Next-AWQ-INT4 · AWQ-INT4 (AWQ) | 188.3 GB | 4.5 | T1,T2 | server | `hf download cyankiwi/Qwen3.8-Flash-Next-AWQ-INT4` |
| `llm-qwen3-8-flash-next-ollama-ollama-3` |  · ollama qwen3.8-flash-next:125b-a6b-q8_0 (ollama) | 189.1 GB | 8.5 | T1,T2,T3 | any | `ollama pull qwen3.8-flash-next:125b-a6b-q8_0` |
| `llm-qwen3-8-flash-next-mlx-oq8e-mtp` | Qwen3.8-Flash-Next-oQ8e-mtp · oQ8e-mtp (MLX) | 194.9 GB | 8.5 | T1,T2 | mac | `hf download mlx-community/Qwen3.8-Flash-Next-oQ8e-mtp` |
| `llm-qwen3-8-flash-next-gguf-bf16` | Qwen3.8-Flash-Next-GGUF · BF16 (GGUF) | 354.0 GB | 16 | T1,T2,T3 | any | `hf download unsloth/Qwen3.8-Flash-Next-GGUF --include "*BF16*"` |
| `llm-qwen3-8-flash-next-ollama-ollama-4` |  · ollama qwen3.8-flash-next:125b-a6b-bf16 (ollama) | 354.9 GB | 16 | T1,T2,T3 | any | `ollama pull qwen3.8-flash-next:125b-a6b-bf16` |
| `llm-qwen3-8-flash-next-ollama-ollama-5` |  · ollama qwen3.8-flash-next:125b-a6b-mlx-b (ollama) | 360.0 GB | 16 | T1,T2,T3 | any | `ollama pull qwen3.8-flash-next:125b-a6b-mlx-bf16` |
</details>

<details><summary><b>Step 5 Preview</b> – 8 változat</summary>

| id | Fájl / repó | Méret | Bit | HW | Platform | Letöltés |
|---|---|---|---|---|---|---|
| `llm-step-5-preview-gguf-q2-k` | Step-5-Preview-GGUF · Q2_K (GGUF) | 182.5 GB | 2.6 | T1,T2,T3 | any | `hf download smalinin/Step-5-Preview-GGUF --include "*Q2_K*"` |
| `llm-step-5-preview-gguf-ik-smol-iq3-ks-mix-b` | Step-5-Preview-GGUF · smol-IQ3_KS-mix-B (GGUF(ik)) | 248.8 GB | 3.5 | T1,T2 | any | `hf download L-Alchemyst/Step-5-Preview-GGUF --include "*smol-IQ3_KS-mix-B*"` |
| `llm-step-5-preview-gguf-iq3-m` | Step-5-Preview-GGUF · IQ3_M (+mmproj BF16 4.4) (GGUF) | 271.6 GB | 3.5 | T1,T2,T3 | any | `hf download smalinin/Step-5-Preview-GGUF --include "*IQ3_M*"` |
| `llm-step-5-preview-gguf-ik-iq3-ks-mix` | Step-5-Preview-GGUF · IQ3_KS-mix (GGUF(ik)) | 275.2 GB | 3.5 | T1,T2 | any | `hf download L-Alchemyst/Step-5-Preview-GGUF --include "*IQ3_KS-mix*"` |
| `llm-step-5-preview-gguf-ik-iq4-ks-mix` | Step-5-Preview-GGUF · IQ4_KS-mix (GGUF(ik)) | 333.0 GB | 4.5 | T1,T2 | any | `hf download L-Alchemyst/Step-5-Preview-GGUF --include "*IQ4_KS-mix*"` |
| `llm-step-5-preview-nvfp4-nvfp4` | Step-5-Preview-NVFP4 · NVFP4 (NVFP4) | 394.2 GB | 4.5 | T1,T2 | server | `hf download stepfun-ai/Step-5-Preview-NVFP4` |
| `llm-step-5-preview-native-native` | Step-5-Preview · native (native) | 650.3 GB | 16 | T1 | server | `hf download stepfun-ai/Step-5-Preview` |
| `llm-step-5-preview-bf16-bf16` | Step-5-Preview-BF16 · BF16 (BF16) | 1.21 TB | 16 | T1 | server | `hf download stepfun-ai/Step-5-Preview-BF16` |
</details>

<details><summary><b>GLM-5.3-Flash</b> – 44 változat</summary>

| id | Fájl / repó | Méret | Bit | HW | Platform | Letöltés |
|---|---|---|---|---|---|---|
| `llm-glm-5-3-flash-gguf-iq1-s` | GLM-5.3-Flash-BF16-GGUF · IQ1_S (GGUF) | 74.8 GB | 1.7 | T1,T2,T3 | any | `hf download bartowski/GLM-5.3-Flash-BF16-GGUF --include "*IQ1_S*"` |
| `llm-glm-5-3-flash-gguf-ud-iq1-s` | GLM-5.3-Flash-GGUF · UD-IQ1_S (GGUF) | 93.1 GB | 1.7 | T1,T2,T3 | any | `hf download unsloth/GLM-5.3-Flash-GGUF --include "*UD-IQ1_S*"` |
| `llm-glm-5-3-flash-gguf-ud-iq1-m` | GLM-5.3-Flash-GGUF · UD-IQ1_M (GGUF) | 97.6 GB | 1.7 | T1,T2,T3 | any | `hf download unsloth/GLM-5.3-Flash-GGUF --include "*UD-IQ1_M*"` |
| `llm-glm-5-3-flash-gguf-ud-iq2-xxs` | GLM-5.3-Flash-GGUF · UD-IQ2_XXS (GGUF) | 101.8 GB | 2.6 | T1,T2,T3 | any | `hf download unsloth/GLM-5.3-Flash-GGUF --include "*UD-IQ2_XXS*"` |
| `llm-glm-5-3-flash-gguf-ud-q2-k-xl` | GLM-5.3-Flash-GGUF · UD-Q2_K_XL (GGUF) | 108.7 GB | 2.6 | T1,T2,T3 | any | `hf download unsloth/GLM-5.3-Flash-GGUF --include "*UD-Q2_K_XL*"` |
| `llm-glm-5-3-flash-gguf-iq2-s` | GLM-5.3-Flash-GGUF · IQ2_S (GGUF) | 113.6 GB | 2.6 | T1,T2,T3 | any | `hf download AesSedai/GLM-5.3-Flash-GGUF --include "*IQ2_S*"` |
| `llm-glm-5-3-flash-gguf-i1-q2-k` | GLM-5.3-Flash-i1-GGUF · i1-Q2_K (GGUF) | 117.9 GB | 2.6 | T1,T2,T3 | any | `hf download mradermacher/GLM-5.3-Flash-i1-GGUF --include "*i1-Q2_K*"` |
| `llm-glm-5-3-flash-gguf-q2-k` | GLM-5.3-Flash-GGUF · Q2_K (GGUF) | 117.9 GB | 2.6 | T1,T2,T3 | any | `hf download mradermacher/GLM-5.3-Flash-GGUF --include "*Q2_K*"` |
| `llm-glm-5-3-flash-gguf-ud-iq3-xxs` | GLM-5.3-Flash-GGUF · UD-IQ3_XXS (GGUF) | 120.4 GB | 3.5 | T1,T2,T3 | any | `hf download unsloth/GLM-5.3-Flash-GGUF --include "*UD-IQ3_XXS*"` |
| `llm-glm-5-3-flash-gguf-iq2-m` | GLM-5.3-Flash-BF16-GGUF · IQ2_M (GGUF) | 120.6 GB | 2.6 | T1,T2,T3 | any | `hf download bartowski/GLM-5.3-Flash-BF16-GGUF --include "*IQ2_M*"` |
| `llm-glm-5-3-flash-gguf-iq3-s` | GLM-5.3-Flash-GGUF · IQ3_S (GGUF) | 124.7 GB | 3.5 | T1,T2,T3 | any | `hf download AesSedai/GLM-5.3-Flash-GGUF --include "*IQ3_S*"` |
| `llm-glm-5-3-flash-gguf-i1-iq3-m` | GLM-5.3-Flash-i1-GGUF · i1-IQ3_M (GGUF) | 140.4 GB | 3.5 | T1,T2,T3 | any | `hf download mradermacher/GLM-5.3-Flash-i1-GGUF --include "*i1-IQ3_M*"` |
| `llm-glm-5-3-flash-gguf-ud-q3-k-xl` | GLM-5.3-Flash-GGUF · UD-Q3_K_XL (GGUF) | 147.5 GB | 3.5 | T1,T2,T3 | any | `hf download unsloth/GLM-5.3-Flash-GGUF --include "*UD-Q3_K_XL*"` |
| `llm-glm-5-3-flash-gguf-q3-k-m` | GLM-5.3-Flash-GGUF · Q3_K_M (GGUF) | 153.7 GB | 3.5 | T1,T2,T3 | any | `hf download mradermacher/GLM-5.3-Flash-GGUF --include "*Q3_K_M*"` |
| `llm-glm-5-3-flash-gguf-q3-k-m-2` | GLM-5.3-Flash-BF16-GGUF · Q3_K_M (GGUF) | 155.0 GB | 3.5 | T1,T2,T3 | any | `hf download bartowski/GLM-5.3-Flash-BF16-GGUF --include "*Q3_K_M*"` |
| `llm-glm-5-3-flash-gguf-ud-iq4-xs` | GLM-5.3-Flash-GGUF · UD-IQ4_XS (GGUF) | 156.8 GB | 4.5 | T1,T2,T3 | any | `hf download unsloth/GLM-5.3-Flash-GGUF --include "*UD-IQ4_XS*"` |
| `llm-glm-5-3-flash-gguf-iq4-xs` | GLM-5.3-Flash-GGUF · IQ4_XS (GGUF) | 159.2 GB | 4.5 | T1,T2,T3 | any | `hf download AesSedai/GLM-5.3-Flash-GGUF --include "*IQ4_XS*"` |
| `llm-glm-5-3-flash-gguf-i1-iq4-xs` | GLM-5.3-Flash-i1-GGUF · i1-IQ4_XS (GGUF) | 171.8 GB | 4.5 | T1,T2,T3 | any | `hf download mradermacher/GLM-5.3-Flash-i1-GGUF --include "*i1-IQ4_XS*"` |
| `llm-glm-5-3-flash-autoround-w4a16` | GLM-5.3-Flash-W4A16-AutoRound · W4A16 (AutoRound) | 181.5 GB | 4.5 | T1,T2 | server | `hf download Intel/GLM-5.3-Flash-W4A16-AutoRound` |
| `llm-glm-5-3-flash-gguf-i1-q4-k-m` | GLM-5.3-Flash-i1-GGUF · i1-Q4_K_M (GGUF) | 193.8 GB | 4.5 | T1,T2,T3 | any | `hf download mradermacher/GLM-5.3-Flash-i1-GGUF --include "*i1-Q4_K_M*"` |
| `llm-glm-5-3-flash-gguf-q4-k-m` | GLM-5.3-Flash-GGUF · Q4_K_M (GGUF) | 193.8 GB | 4.5 | T1,T2,T3 | any | `hf download mradermacher/GLM-5.3-Flash-GGUF --include "*Q4_K_M*"` |
| `llm-glm-5-3-flash-awq-awq-int4` | GLM-5.3-Flash-AWQ-INT4 · AWQ-INT4 (AWQ) | 197.2 GB | 4.5 | T1,T2 | server | `hf download cyankiwi/GLM-5.3-Flash-AWQ-INT4` |
| `llm-glm-5-3-flash-nvfp4-nvfp4` | GLM-5.3-Flash-NVFP4 · NVFP4 (NVFP4) | 197.9 GB | 4.5 | T1,T2 | server | `hf download RedHatAI/GLM-5.3-Flash-NVFP4` |
| `llm-glm-5-3-flash-gguf-ud-q4-k-xl` | GLM-5.3-Flash-GGUF · UD-Q4_K_XL (GGUF) | 199.7 GB | 4.5 | T1,T2 | any | `hf download unsloth/GLM-5.3-Flash-GGUF --include "*UD-Q4_K_XL*"` |
| `llm-glm-5-3-flash-gguf-q4-k-m-2` | GLM-5.3-Flash-BF16-GGUF · Q4_K_M (GGUF) | 200.8 GB | 4.5 | T1,T2,T3 | any | `hf download bartowski/GLM-5.3-Flash-BF16-GGUF --include "*Q4_K_M*"` |
| `llm-glm-5-3-flash-gguf-q4-k-m-3` | GLM-5.3-Flash-GGUF · Q4_K_M (GGUF) | 202.0 GB | 4.5 | T1,T2,T3 | any | `hf download AesSedai/GLM-5.3-Flash-GGUF --include "*Q4_K_M*"` |
| `llm-glm-5-3-flash-mlx-4bit` | GLM-5.3-Flash-4bit · 4bit (MLX) | 204.0 GB | 4.5 | T1,T2 | mac | `hf download mlx-community/GLM-5.3-Flash-4bit` |
| `llm-glm-5-3-flash-nvfp4-nvfp4-2` | GLM-5.3-Flash-NVFP4 · NVFP4 (NVFP4) | 204.5 GB | 4.5 | T1,T2 | server | `hf download nvidia/GLM-5.3-Flash-NVFP4` |
| `llm-glm-5-3-flash-gguf-i1-q5-k-m` | GLM-5.3-Flash-i1-GGUF · i1-Q5_K_M (GGUF) | 227.9 GB | 5.5 | T1,T2,T3 | any | `hf download mradermacher/GLM-5.3-Flash-i1-GGUF --include "*i1-Q5_K_M*"` |
| `llm-glm-5-3-flash-gguf-q5-k-m` | GLM-5.3-Flash-GGUF · Q5_K_M (GGUF) | 227.9 GB | 5.5 | T1,T2,T3 | any | `hf download mradermacher/GLM-5.3-Flash-GGUF --include "*Q5_K_M*"` |
| `llm-glm-5-3-flash-gguf-ud-q5-k-xl` | GLM-5.3-Flash-GGUF · UD-Q5_K_XL (GGUF) | 240.3 GB | 5.5 | T1,T2 | any | `hf download unsloth/GLM-5.3-Flash-GGUF --include "*UD-Q5_K_XL*"` |
| `llm-glm-5-3-flash-gguf-q5-k-m-2` | GLM-5.3-Flash-GGUF · Q5_K_M (GGUF) | 240.8 GB | 5.5 | T1,T2,T3 | any | `hf download AesSedai/GLM-5.3-Flash-GGUF --include "*Q5_K_M*"` |
| `llm-glm-5-3-flash-gguf-q5-k-m-3` | GLM-5.3-Flash-BF16-GGUF · Q5_K_M (GGUF) | 243.7 GB | 5.5 | T1,T2,T3 | any | `hf download bartowski/GLM-5.3-Flash-BF16-GGUF --include "*Q5_K_M*"` |
| `llm-glm-5-3-flash-gguf-i1-q6-k` | GLM-5.3-Flash-i1-GGUF · i1-Q6_K (GGUF) | 264.0 GB | 6.5 | T1,T2,T3 | any | `hf download mradermacher/GLM-5.3-Flash-i1-GGUF --include "*i1-Q6_K*"` |
| `llm-glm-5-3-flash-gguf-q6-k` | GLM-5.3-Flash-GGUF · Q6_K (GGUF) | 264.0 GB | 6.5 | T1,T2,T3 | any | `hf download mradermacher/GLM-5.3-Flash-GGUF --include "*Q6_K*"` |
| `llm-glm-5-3-flash-gguf-q6-k-2` | GLM-5.3-Flash-BF16-GGUF · Q6_K (GGUF) | 281.0 GB | 6.5 | T1,T2,T3 | any | `hf download bartowski/GLM-5.3-Flash-BF16-GGUF --include "*Q6_K*"` |
| `llm-glm-5-3-flash-gguf-ud-q6-k-xl` | GLM-5.3-Flash-GGUF · UD-Q6_K_XL (GGUF) | 291.8 GB | 6.5 | T1,T2 | any | `hf download unsloth/GLM-5.3-Flash-GGUF --include "*UD-Q6_K_XL*"` |
| `llm-glm-5-3-flash-fp8-native-fp8` | GLM-5.3-Flash · FP8 (FP8(native)) | 328.4 GB | 8.5 | T1,T2 | server | `hf download zai-org/GLM-5.3-Flash` |
| `llm-glm-5-3-flash-fp8-fp8` | GLM-5.3-Flash-FP8 · FP8 (FP8) | 328.4 GB | 8.5 | T1 | server | `hf download unsloth/GLM-5.3-Flash-FP8` |
| `llm-glm-5-3-flash-gguf-q8-0` | GLM-5.3-Flash-GGUF · Q8_0 (GGUF) | 341.0 GB | 8.5 | T1,T2 | any | `hf download unsloth/GLM-5.3-Flash-GGUF --include "*Q8_0*"` |
| `llm-glm-5-3-flash-gguf-q8-0-2` | GLM-5.3-Flash-GGUF · Q8_0 (GGUF) | 341.5 GB | 8.5 | T1,T2,T3 | any | `hf download mradermacher/GLM-5.3-Flash-GGUF --include "*Q8_0*"` |
| `llm-glm-5-3-flash-gguf-q8-0-3` | GLM-5.3-Flash-BF16-GGUF · Q8_0 (GGUF) | 341.5 GB | 8.5 | T1,T2,T3 | any | `hf download bartowski/GLM-5.3-Flash-BF16-GGUF --include "*Q8_0*"` |
| `llm-glm-5-3-flash-gguf-bf16` | GLM-5.3-Flash-GGUF · BF16 (GGUF) | 641.6 GB | 16 | T1,T2 | any | `hf download unsloth/GLM-5.3-Flash-GGUF --include "*BF16*"` |
| `llm-glm-5-3-flash-bf16-bf16` | GLM-5.3-Flash-BF16 · BF16 (BF16) | 642.7 GB | 16 | T1 | server | `hf download zai-org/GLM-5.3-Flash-BF16` |
</details>

<details><summary><b>Mistral Large 4 (1T-A52B)</b> – 21 változat</summary>

| id | Fájl / repó | Méret | Bit | HW | Platform | Letöltés |
|---|---|---|---|---|---|---|
| `llm-mistral-large-4-gguf-ud-iq1-s` | Mistral-Large-4-1T-A52B-GGUF · UD-IQ1_S (GGUF) | 233.0 GB | 1.7 | T1,T2 | any | `hf download unsloth/Mistral-Large-4-1T-A52B-GGUF --include "*UD-IQ1_S*"` |
| `llm-mistral-large-4-gguf-ud-iq1-m` | Mistral-Large-4-1T-A52B-GGUF · UD-IQ1_M (GGUF) | 259.6 GB | 1.7 | T1,T2 | any | `hf download unsloth/Mistral-Large-4-1T-A52B-GGUF --include "*UD-IQ1_M*"` |
| `llm-mistral-large-4-gguf-iq2-xxs` | Mistral-Large-4-1T-A52B-GGUF · IQ2_XXS (GGUF) | 297.7 GB | 2.6 | T1,T2 | any | `hf download ggml-org/Mistral-Large-4-1T-A52B-GGUF --include "*IQ2_XXS*"` |
| `llm-mistral-large-4-gguf-ud-iq2-xxs` | Mistral-Large-4-1T-A52B-GGUF · UD-IQ2_XXS (GGUF) | 302.5 GB | 2.6 | T1,T2 | any | `hf download unsloth/Mistral-Large-4-1T-A52B-GGUF --include "*UD-IQ2_XXS*"` |
| `llm-mistral-large-4-mlx-2bit` | Mistral-Large-4-1T-A52B-Text-2bit · 2bit text-only (MLX) | 338.2 GB | 2.5 | T1,T2 | mac | `hf download mlx-community/Mistral-Large-4-1T-A52B-Text-2bit` |
| `llm-mistral-large-4-gguf-ud-q2-k-xl` | Mistral-Large-4-1T-A52B-GGUF · UD-Q2_K_XL (GGUF) | 378.2 GB | 2.6 | T1,T2 | any | `hf download unsloth/Mistral-Large-4-1T-A52B-GGUF --include "*UD-Q2_K_XL*"` |
| `llm-mistral-large-4-gguf-q2-k` | Mistral-Large-4-1T-A52B-GGUF · Q2_K (GGUF) | 380.7 GB | 2.6 | T1,T2 | any | `hf download ggml-org/Mistral-Large-4-1T-A52B-GGUF --include "*Q2_K*"` |
| `llm-mistral-large-4-gguf-ud-iq3-xxs` | Mistral-Large-4-1T-A52B-GGUF · UD-IQ3_XXS (GGUF) | 423.5 GB | 3.5 | T1,T2 | any | `hf download unsloth/Mistral-Large-4-1T-A52B-GGUF --include "*UD-IQ3_XXS*"` |
| `llm-mistral-large-4-mlx-3bit` | Mistral-Large-4-1T-A52B-Text-3bit · 3bit text-only (MLX) | 459.3 GB | 3.5 | T1,T2 | mac | `hf download mlx-community/Mistral-Large-4-1T-A52B-Text-3bit` |
| `llm-mistral-large-4-gguf-ud-q3-k-xl` | Mistral-Large-4-1T-A52B-GGUF · UD-Q3_K_XL (GGUF) | 492.8 GB | 3.5 | T1,T2 | any | `hf download unsloth/Mistral-Large-4-1T-A52B-GGUF --include "*UD-Q3_K_XL*"` |
| `llm-mistral-large-4-mlx-4bit` | Mistral-Large-4-1T-A52B-Text-4bit · 4bit text-only (MLX) | 590.4 GB | 4.5 | T1,T2 | mac | `hf download mlx-community/Mistral-Large-4-1T-A52B-Text-4bit` |
| `llm-mistral-large-4-gguf-ud-q4-k-xl` | Mistral-Large-4-1T-A52B-GGUF · UD-Q4_K_XL (GGUF) | 604.8 GB | 4.5 | T1,T2 | any | `hf download unsloth/Mistral-Large-4-1T-A52B-GGUF --include "*UD-Q4_K_XL*"` |
| `llm-mistral-large-4-nvfp4-nvfp4` | Mistral-Large-4-1T-A52B-NVFP4 · NVFP4 (NVFP4) | 610.1 GB | 4.5 | T1,T2 | server | `hf download mistralai/Mistral-Large-4-1T-A52B-NVFP4` |
| `llm-mistral-large-4-gguf-q4-k-m` | Mistral-Large-4-1T-A52B-GGUF · Q4_K_M (GGUF) | 634.8 GB | 4.5 | T1,T2 | any | `hf download ggml-org/Mistral-Large-4-1T-A52B-GGUF --include "*Q4_K_M*"` |
| `llm-mistral-large-4-gguf-ud-q5-k-xl` | Mistral-Large-4-1T-A52B-GGUF · UD-Q5_K_XL (GGUF) | 783.8 GB | 5.5 | T1,T2 | any | `hf download unsloth/Mistral-Large-4-1T-A52B-GGUF --include "*UD-Q5_K_XL*"` |
| `llm-mistral-large-4-gguf-ud-q6-k-xl` | Mistral-Large-4-1T-A52B-GGUF · UD-Q6_K_XL (GGUF) | 890.5 GB | 6.5 | T1,T2 | any | `hf download unsloth/Mistral-Large-4-1T-A52B-GGUF --include "*UD-Q6_K_XL*"` |
| `llm-mistral-large-4-fp8-native-fp8` | Mistral-Large-4-1T-A52B · FP8 (FP8(native)) | 1.06 TB | 8.5 | T1 | server | `hf download mistralai/Mistral-Large-4-1T-A52B` |
| `llm-mistral-large-4-gguf-q8-0` | Mistral-Large-4-1T-A52B-GGUF · Q8_0 (GGUF) | 1.12 TB | 8.5 | T1,T2 | any | `hf download unsloth/Mistral-Large-4-1T-A52B-GGUF --include "*Q8_0*"` |
| `llm-mistral-large-4-gguf-q8-0-2` | Mistral-Large-4-1T-A52B-GGUF · Q8_0 (GGUF) | 1.12 TB | 8.5 | T1,T2 | any | `hf download ggml-org/Mistral-Large-4-1T-A52B-GGUF --include "*Q8_0*"` |
| `llm-mistral-large-4-gguf-bf16` | Mistral-Large-4-1T-A52B-GGUF · BF16 (GGUF) | 2.10 TB | 16 | T1,T2 | any | `hf download unsloth/Mistral-Large-4-1T-A52B-GGUF --include "*BF16*"` |
| `llm-mistral-large-4-gguf-bf16-2` | Mistral-Large-4-1T-A52B-GGUF · BF16 (GGUF) | 2.10 TB | 16 | T1,T2 | any | `hf download ggml-org/Mistral-Large-4-1T-A52B-GGUF --include "*BF16*"` |
</details>

<details><summary><b>Muse Spark Open (816B-A42B)</b> – 17 változat</summary>

| id | Fájl / repó | Méret | Bit | HW | Platform | Letöltés |
|---|---|---|---|---|---|---|
| `llm-muse-spark-open-gguf-ud-iq1-s` | Muse-Spark-Open-816B-A42B-GGUF · UD-IQ1_S (GGUF) | 175.6 GB | 1.7 | T1,T2,T3 | any | `hf download unsloth/Muse-Spark-Open-816B-A42B-GGUF --include "*UD-IQ1_S*"` |
| `llm-muse-spark-open-gguf-ud-iq1-m` | Muse-Spark-Open-816B-A42B-GGUF · UD-IQ1_M (GGUF) | 208.9 GB | 1.7 | T1,T2,T3 | any | `hf download unsloth/Muse-Spark-Open-816B-A42B-GGUF --include "*UD-IQ1_M*"` |
| `llm-muse-spark-open-gguf-ud-iq2-xxs` | Muse-Spark-Open-816B-A42B-GGUF · UD-IQ2_XXS (GGUF) | 225.6 GB | 2.6 | T1,T2,T3 | any | `hf download unsloth/Muse-Spark-Open-816B-A42B-GGUF --include "*UD-IQ2_XXS*"` |
| `llm-muse-spark-open-gguf-ud-iq2-s` | Muse-Spark-Open-816B-A42B-GGUF · UD-IQ2_S (GGUF) | 275.5 GB | 2.6 | T1,T2,T3 | any | `hf download unsloth/Muse-Spark-Open-816B-A42B-GGUF --include "*UD-IQ2_S*"` |
| `llm-muse-spark-open-gguf-q2-k` | Muse-Spark-Open-816B-A42B-GGUF · Q2_K (GGUF) | 304.1 GB | 2.6 | T1,T2 | any | `hf download ggml-org/Muse-Spark-Open-816B-A42B-GGUF --include "*Q2_K*"` |
| `llm-muse-spark-open-gguf-ud-q2-k-xl` | Muse-Spark-Open-816B-A42B-GGUF · UD-Q2_K_XL (GGUF) | 311.2 GB | 2.6 | T1,T2,T3 | any | `hf download unsloth/Muse-Spark-Open-816B-A42B-GGUF --include "*UD-Q2_K_XL*"` |
| `llm-muse-spark-open-gguf-ud-iq3-xxs` | Muse-Spark-Open-816B-A42B-GGUF · UD-IQ3_XXS (GGUF) | 340.4 GB | 3.5 | T1,T2 | any | `hf download unsloth/Muse-Spark-Open-816B-A42B-GGUF --include "*UD-IQ3_XXS*"` |
| `llm-muse-spark-open-gguf-ud-q3-k-xl` | Muse-Spark-Open-816B-A42B-GGUF · UD-Q3_K_XL (GGUF) | 401.5 GB | 3.5 | T1,T2 | any | `hf download unsloth/Muse-Spark-Open-816B-A42B-GGUF --include "*UD-Q3_K_XL*"` |
| `llm-muse-spark-open-mlx-3bit` | Muse-Spark-Open-816B-A42B-3bit · 3bit (MLX) | 436.2 GB | 3.5 | T1,T2 | mac | `hf download mlx-community/Muse-Spark-Open-816B-A42B-3bit` |
| `llm-muse-spark-open-gguf-q4-k-s` | Muse-Spark-Open-816B-A42B-GGUF · Q4_K_S (GGUF) | 470.1 GB | 4.5 | T1,T2 | any | `hf download ggml-org/Muse-Spark-Open-816B-A42B-GGUF --include "*Q4_K_S*"` |
| `llm-muse-spark-open-gguf-ud-q4-k-xl` | Muse-Spark-Open-816B-A42B-GGUF · UD-Q4_K_XL (+mmproj BF16 4.1) (GGUF) | 505.5 GB | 4.5 | T1,T2 | any | `hf download unsloth/Muse-Spark-Open-816B-A42B-GGUF --include "*UD-Q4_K_XL*"` |
| `llm-muse-spark-open-mxfp4-mxfp4` | Muse-Spark-Open-816B-A42B-Quark-MXFP4 · MXFP4 (MXFP4) | 508.9 GB | 4.5 | T1 | server | `hf download amd/Muse-Spark-Open-816B-A42B-Quark-MXFP4` |
| `llm-muse-spark-open-mlx-4bit` | Muse-Spark-Open-816B-A42B-4bit · 4bit (MLX) | 532.8 GB | 4.5 | T1,T2 | mac | `hf download mlx-community/Muse-Spark-Open-816B-A42B-4bit` |
| `llm-muse-spark-open-nvfp4-nvfp4` | Muse-Spark-Open-816B-A42B-NVFP4 · NVFP4 (NVFP4) | 533.0 GB | 4.5 | T1 | server | `hf download meta-models/Muse-Spark-Open-816B-A42B-NVFP4` |
| `llm-muse-spark-open-gguf-q8-0` | Muse-Spark-Open-816B-A42B-GGUF · Q8_0 (GGUF) | 871.6 GB | 8.5 | T1,T2 | any | `hf download ggml-org/Muse-Spark-Open-816B-A42B-GGUF --include "*Q8_0*"` |
| `llm-muse-spark-open-gguf-bf16` | Muse-Spark-Open-816B-A42B-GGUF · BF16 (GGUF) | 1.64 TB | 16 | T1,T2 | any | `hf download ggml-org/Muse-Spark-Open-816B-A42B-GGUF --include "*BF16*"` |
| `llm-muse-spark-open-bf16-bf16` | Muse-Spark-Open-816B-A42B · BF16 (BF16) | 1.64 TB | 16 | T1 | server | `hf download meta-models/Muse-Spark-Open-816B-A42B` |
</details>

<details><summary><b>Qwen3.8-27B (dense)</b> – 58 változat</summary>

| id | Fájl / repó | Méret | Bit | HW | Platform | Letöltés |
|---|---|---|---|---|---|---|
| `llm-qwen3-8-27b-gguf-ud-iq1-s` | Qwen3.8-27B-GGUF · UD-IQ1_S (GGUF) | 6.2 GB | 1.7 | T1,T2,T3,T4 | any | `hf download unsloth/Qwen3.8-27B-GGUF --include "*UD-IQ1_S*"` |
| `llm-qwen3-8-27b-gguf-ud-iq2-xxs` | Qwen3.8-27B-GGUF · UD-IQ2_XXS (GGUF) | 7.2 GB | 2.6 | T1,T2,T3,T4 | any | `hf download unsloth/Qwen3.8-27B-GGUF --include "*UD-IQ2_XXS*"` |
| `llm-qwen3-8-27b-gguf-ud-iq2-s` | Qwen3.8-27B-GGUF · UD-IQ2_S (GGUF) | 8.4 GB | 2.6 | T1,T2,T3,T4 | any | `hf download unsloth/Qwen3.8-27B-GGUF --include "*UD-IQ2_S*"` |
| `llm-qwen3-8-27b-gguf-iq2-xs` | Qwen3.8-27B-GSQ-RCO-GGUF · IQ2_XS (GGUF) | 8.4 GB | 2.6 | T1,T2,T3,T4 | any | `hf download ISTA-DASLab/Qwen3.8-27B-GSQ-RCO-GGUF --include "*IQ2_XS*"` |
| `llm-qwen3-8-27b-gguf-iq2-xxs` | Qwen3.8-27B-GGUF · IQ2_XXS (GGUF) | 8.9 GB | 2.6 | T1,T2,T3,T4 | any | `hf download bartowski/Qwen3.8-27B-GGUF --include "*IQ2_XXS*"` |
| `llm-qwen3-8-27b-gguf-iq2-s` | Qwen3.8-27B-GSQ-RCO-GGUF · IQ2_S (GGUF) | 9.3 GB | 2.6 | T1,T2,T3,T4 | any | `hf download ISTA-DASLab/Qwen3.8-27B-GSQ-RCO-GGUF --include "*IQ2_S*"` |
| `llm-qwen3-8-27b-gguf-ud-q2-k-xl` | Qwen3.8-27B-GGUF · UD-Q2_K_XL (GGUF) | 9.9 GB | 2.6 | T1,T2,T3,T4 | any | `hf download unsloth/Qwen3.8-27B-GGUF --include "*UD-Q2_K_XL*"` |
| `llm-qwen3-8-27b-gguf-iq3-xxs` | Qwen3.8-27B-GSQ-RCO-GGUF · IQ3_XXS (GGUF) | 10.1 GB | 3.5 | T1,T2,T3,T4 | any | `hf download ISTA-DASLab/Qwen3.8-27B-GSQ-RCO-GGUF --include "*IQ3_XXS*"` |
| `llm-qwen3-8-27b-gguf-q2-k` | Qwen3.8-27B-GGUF · Q2_K (GGUF) | 10.8 GB | 2.6 | T1,T2,T3,T4 | any | `hf download bartowski/Qwen3.8-27B-GGUF --include "*Q2_K*"` |
| `llm-qwen3-8-27b-gguf-q2-k-2` | Qwen3.8-27B-i1-GGUF · Q2_K (GGUF) | 10.9 GB | 2.6 | T1,T2,T3,T4 | any | `hf download mradermacher/Qwen3.8-27B-i1-GGUF --include "*Q2_K*"` |
| `llm-qwen3-8-27b-gguf-ud-iq3-xxs` | Qwen3.8-27B-GGUF · UD-IQ3_XXS (GGUF) | 10.9 GB | 3.5 | T1,T2,T3,T4 | any | `hf download unsloth/Qwen3.8-27B-GGUF --include "*UD-IQ3_XXS*"` |
| `llm-qwen3-8-27b-gguf-iq3-s` | Qwen3.8-27B-GSQ-RCO-GGUF · IQ3_S (GGUF) | 11.8 GB | 3.5 | T1,T2,T3,T4 | any | `hf download ISTA-DASLab/Qwen3.8-27B-GSQ-RCO-GGUF --include "*IQ3_S*"` |
| `llm-qwen3-8-27b-gguf-ud-iq3-s` | Qwen3.8-27B-GGUF · UD-IQ3_S (GGUF) | 12.0 GB | 3.5 | T1,T2,T3,T4 | any | `hf download unsloth/Qwen3.8-27B-GGUF --include "*UD-IQ3_S*"` |
| `llm-qwen3-8-27b-gguf-iq3-m` | Qwen3.8-27B-i1-GGUF · IQ3_M (GGUF) | 12.8 GB | 3.5 | T1,T2,T3,T4 | any | `hf download mradermacher/Qwen3.8-27B-i1-GGUF --include "*IQ3_M*"` |
| `llm-qwen3-8-27b-gguf-ud-q3-k-xl` | Qwen3.8-27B-GGUF · UD-Q3_K_XL (GGUF) | 13.2 GB | 3.5 | T1,T2,T3,T4 | any | `hf download unsloth/Qwen3.8-27B-GGUF --include "*UD-Q3_K_XL*"` |
| `llm-qwen3-8-27b-gguf-ud-iq4-xs` | Qwen3.8-27B-GGUF · UD-IQ4_XS (GGUF) | 14.3 GB | 4.5 | T1,T2,T3,T4 | any | `hf download unsloth/Qwen3.8-27B-GGUF --include "*UD-IQ4_XS*"` |
| `llm-qwen3-8-27b-gguf-iq3-m-2` | Qwen3.8-27B-GGUF · IQ3_M (GGUF) | 14.9 GB | 3.5 | T1,T2,T3,T4 | any | `hf download bartowski/Qwen3.8-27B-GGUF --include "*IQ3_M*"` |
| `llm-qwen3-8-27b-gguf-iq4-xs` | Qwen3.8-27B-i1-GGUF · IQ4_XS (GGUF) | 15.3 GB | 4.5 | T1,T2,T3,T4 | any | `hf download mradermacher/Qwen3.8-27B-i1-GGUF --include "*IQ4_XS*"` |
| `llm-qwen3-8-27b-gguf-iq4-xs-2` | Qwen3.8-27B-GGUF · IQ4_XS (GGUF) | 15.5 GB | 4.5 | T1,T2,T3,T4 | any | `hf download bartowski/Qwen3.8-27B-GGUF --include "*IQ4_XS*"` |
| `llm-qwen3-8-27b-mlx-4bit` | Qwen3.8-27B-4bit · 4bit (MLX) | 16.1 GB | 4.5 | T1,T2,T3,T4 | mac | `hf download mlx-community/Qwen3.8-27B-4bit` |
| `llm-qwen3-8-27b-mlx-4bit-2` | Qwen3.8-27B-MLX-4bit · 4bit (MLX) | 16.1 GB | 4.5 | T1,T2,T3,T4 | mac | `hf download lmstudio-community/Qwen3.8-27B-MLX-4bit` |
| `llm-qwen3-8-27b-gguf-ud-q4-k-m` | Qwen3.8-27B-GGUF · UD-Q4_K_M (GGUF) | 16.6 GB | 4.5 | T1,T2,T3,T4 | any | `hf download unsloth/Qwen3.8-27B-GGUF --include "*UD-Q4_K_M*"` |
| `llm-qwen3-8-27b-gguf-q4-k-m` | Qwen3.8-27B-GGUF · Q4_K_M (GGUF) | 16.8 GB | 4.5 | T1,T2,T3,T4 | any | `hf download lmstudio-community/Qwen3.8-27B-GGUF --include "*Q4_K_M*"` |
| `llm-qwen3-8-27b-gguf-q4-k-m-2` | Qwen3.8-27B-i1-GGUF · Q4_K_M (GGUF) | 16.8 GB | 4.5 | T1,T2,T3,T4 | any | `hf download mradermacher/Qwen3.8-27B-i1-GGUF --include "*Q4_K_M*"` |
| `llm-qwen3-8-27b-gguf-ik-iq4-ks` | Qwen3.8-27B-GGUF · IQ4_KS (+MTP) (GGUF(ik)) | 16.9 GB | 4.5 | T1,T2,T3 | any | `hf download ubergarm/Qwen3.8-27B-GGUF --include "*IQ4_KS*"` |
| `llm-qwen3-8-27b-gguf-q4-k-m-3` | Qwen3.8-27B-GGUF · Q4_K_M (GGUF) | 17.4 GB | 4.5 | T1,T2,T3,T4 | any | `hf download bartowski/Qwen3.8-27B-GGUF --include "*Q4_K_M*"` |
| `llm-qwen3-8-27b-gguf-ud-q4-k-xl` | Qwen3.8-27B-GGUF · UD-Q4_K_XL (GGUF) | 17.7 GB | 4.5 | T1,T2,T3,T4 | any | `hf download unsloth/Qwen3.8-27B-GGUF --include "*UD-Q4_K_XL*"` |
| `llm-qwen3-8-27b-ollama-ollama` |  · ollama qwen3.8:27b / :latest / :27b-q4_K (ollama) | 17.7 GB | 4.5 | T1,T2,T3,T4 | any | `ollama pull qwen3.8:27b / :latest / :27b-q4_K_M / :27b-mtp-q4_K_M` |
| `llm-qwen3-8-27b-ollama-ollama-2` |  · ollama qwen3.8:27b-nvfp4 / :27b-mlx (ollama) | 18.2 GB | 4.5 | T1,T2,T3,T4 | any | `ollama pull qwen3.8:27b-nvfp4 / :27b-mlx` |
| `llm-qwen3-8-27b-gguf-q4-k-m-4` | Qwen3.8-27B-GGUF · Q4_K_M (GGUF) | 19.4 GB | 4.5 | T1,T2,T3 | any | `hf download ggml-org/Qwen3.8-27B-GGUF --include "*Q4_K_M*"` |
| `llm-qwen3-8-27b-mlx-5bit` | Qwen3.8-27B-MLX-5bit · 5bit (MLX) | 19.4 GB | 5.5 | T1,T2,T3,T4 | mac | `hf download lmstudio-community/Qwen3.8-27B-MLX-5bit` |
| `llm-qwen3-8-27b-gptq-int4-w4a16` | Qwen3.8-27B-INT4 · W4A16 (GPTQ/INT4) | 19.5 GB | 4.5 | T1,T2,T3 | server | `hf download RedHatAI/Qwen3.8-27B-INT4` |
| `llm-qwen3-8-27b-gguf-q5-k-m` | Qwen3.8-27B-i1-GGUF · Q5_K_M (GGUF) | 19.5 GB | 5.5 | T1,T2,T3,T4 | any | `hf download mradermacher/Qwen3.8-27B-i1-GGUF --include "*Q5_K_M*"` |
| `llm-qwen3-8-27b-gguf-q5-k-m-2` | Qwen3.8-27B-GGUF · Q5_K_M (GGUF) | 20.9 GB | 5.5 | T1,T2,T3,T4 | any | `hf download bartowski/Qwen3.8-27B-GGUF --include "*Q5_K_M*"` |
| `llm-qwen3-8-27b-gguf-ud-q5-k-xl` | Qwen3.8-27B-GGUF · UD-Q5_K_XL (GGUF) | 21.0 GB | 5.5 | T1,T2,T3,T4 | any | `hf download unsloth/Qwen3.8-27B-GGUF --include "*UD-Q5_K_XL*"` |
| `llm-qwen3-8-27b-awq-awq-int4` | Qwen3.8-27B-AWQ-INT4 · AWQ-INT4 (AWQ) | 21.0 GB | 4.5 | T1,T2,T3 | server | `hf download cyankiwi/Qwen3.8-27B-AWQ-INT4` |
| `llm-qwen3-8-27b-nvfp4-nvfp4` | Qwen3.8-27B-NVFP4 · NVFP4 (NVFP4) | 21.9 GB | 4.5 | T1,T2,T3 | server | `hf download nvidia/Qwen3.8-27B-NVFP4` |
| `llm-qwen3-8-27b-gguf-q6-k` | Qwen3.8-27B-GGUF · Q6_K (GGUF) | 22.4 GB | 6.5 | T1,T2,T3,T4 | any | `hf download lmstudio-community/Qwen3.8-27B-GGUF --include "*Q6_K*"` |
| `llm-qwen3-8-27b-gguf-q6-k-2` | Qwen3.8-27B-i1-GGUF · Q6_K (GGUF) | 22.4 GB | 6.5 | T1,T2,T3,T4 | any | `hf download mradermacher/Qwen3.8-27B-i1-GGUF --include "*Q6_K*"` |
| `llm-qwen3-8-27b-mlx-6bit` | Qwen3.8-27B-MLX-6bit · 6bit (MLX) | 22.8 GB | 6.5 | T1,T2,T3,T4 | mac | `hf download lmstudio-community/Qwen3.8-27B-MLX-6bit` |
| `llm-qwen3-8-27b-nvfp4-nvfp4-2` | Qwen3.8-27B-NVFP4 · NVFP4 (NVFP4) | 23.4 GB | 4.5 | T1,T2,T3 | server | `hf download unsloth/Qwen3.8-27B-NVFP4` |
| `llm-qwen3-8-27b-gguf-q6-k-3` | Qwen3.8-27B-GGUF · Q6_K (GGUF) | 23.9 GB | 6.5 | T1,T2,T3,T4 | any | `hf download bartowski/Qwen3.8-27B-GGUF --include "*Q6_K*"` |
| `llm-qwen3-8-27b-gguf-ud-q6-k-xl` | Qwen3.8-27B-GGUF · UD-Q6_K_XL (GGUF) | 25.3 GB | 6.5 | T1,T2,T3,T4 | any | `hf download unsloth/Qwen3.8-27B-GGUF --include "*UD-Q6_K_XL*"` |
| `llm-qwen3-8-27b-gguf-q8-0` | Qwen3.8-27B-GGUF · Q8_0 (GGUF) | 28.6 GB | 8.5 | T1,T2,T3 | any | `hf download ggml-org/Qwen3.8-27B-GGUF --include "*Q8_0*"` |
| `llm-qwen3-8-27b-gguf-q8-0-2` | Qwen3.8-27B-GGUF · Q8_0 (GGUF) | 29.1 GB | 8.5 | T1,T2,T3,T4 | any | `hf download unsloth/Qwen3.8-27B-GGUF --include "*Q8_0*"` |
| `llm-qwen3-8-27b-gguf-q8-0-3` | Qwen3.8-27B-GGUF · Q8_0 (GGUF) | 29.1 GB | 8.5 | T1,T2,T3,T4 | any | `hf download lmstudio-community/Qwen3.8-27B-GGUF --include "*Q8_0*"` |
| `llm-qwen3-8-27b-gguf-q8-0-4` | Qwen3.8-27B-GGUF · Q8_0 (GGUF) | 29.1 GB | 8.5 | T1,T2,T3,T4 | any | `hf download bartowski/Qwen3.8-27B-GGUF --include "*Q8_0*"` |
| `llm-qwen3-8-27b-mlx-8bit` | Qwen3.8-27B-8bit · 8bit (MLX) | 29.5 GB | 8.5 | T1,T2,T3,T4 | mac | `hf download mlx-community/Qwen3.8-27B-8bit` |
| `llm-qwen3-8-27b-mlx-8bit-2` | Qwen3.8-27B-MLX-8bit · 8bit (MLX) | 29.5 GB | 8.5 | T1,T2,T3,T4 | mac | `hf download lmstudio-community/Qwen3.8-27B-MLX-8bit` |
| `llm-qwen3-8-27b-ollama-ollama-3` |  · ollama qwen3.8:27b-q8_0 / :27b-mtp-q8_0 (ollama) | 30.0 GB | 8.5 | T1,T2,T3,T4 | any | `ollama pull qwen3.8:27b-q8_0 / :27b-mtp-q8_0` |
| `llm-qwen3-8-27b-ollama-ollama-4` |  · ollama qwen3.8:27b-mxfp8 (ollama) | 30.4 GB | 8.5 | T1,T2,T3,T4 | any | `ollama pull qwen3.8:27b-mxfp8` |
| `llm-qwen3-8-27b-fp8-fp8` | Qwen3.8-27B-FP8 · FP8 (FP8) | 30.9 GB | 8.5 | T1,T2,T3 | server | `hf download Qwen/Qwen3.8-27B-FP8` |
| `llm-qwen3-8-27b-fp8-fp8-2` | Qwen3.8-27B-FP8 · FP8 (FP8) | 30.9 GB | 8.5 | T1,T2,T3 | server | `hf download RedHatAI/Qwen3.8-27B-FP8` |
| `llm-qwen3-8-27b-gguf-ud-q8-k-xl` | Qwen3.8-27B-GGUF · UD-Q8_K_XL (GGUF) | 31.5 GB | 8.5 | T1,T2,T3,T4 | any | `hf download unsloth/Qwen3.8-27B-GGUF --include "*UD-Q8_K_XL*"` |
| `llm-qwen3-8-27b-gguf-bf16` | Qwen3.8-27B-GGUF · BF16 (+MTP, DFlash draft) (GGUF) | 53.8 GB | 16 | T1,T2,T3 | any | `hf download ggml-org/Qwen3.8-27B-GGUF --include "*BF16*"` |
| `llm-qwen3-8-27b-gguf-bf16-2` | Qwen3.8-27B-GGUF · BF16 (GGUF) | 54.7 GB | 16 | T1,T2,T3,T4 | any | `hf download unsloth/Qwen3.8-27B-GGUF --include "*BF16*"` |
| `llm-qwen3-8-27b-mlx-bf16` | Qwen3.8-27B-bf16 · bf16 (MLX) | 54.7 GB | 16 | T1,T2,T3,T4 | mac | `hf download mlx-community/Qwen3.8-27B-bf16` |
| `llm-qwen3-8-27b-ollama-ollama-5` |  · ollama qwen3.8:27b-bf16 (ollama) | 55.6 GB | 16 | T1,T2,T3,T4 | any | `ollama pull qwen3.8:27b-bf16` |
</details>

<details><summary><b>NVIDIA Nemotron 3.5 (Super-VL-120B-A12B, Lightning-30B-A3B, Bolt-E4B)</b> – 45 változat</summary>

| id | Fájl / repó | Méret | Bit | HW | Platform | Letöltés |
|---|---|---|---|---|---|---|
| `llm-nemotron-3-5-gguf-ud-iq2-m` | NVIDIA-Nemotron-3.5-Bolt-E4B-GGUF · UD-IQ2_M (GGUF) | 3.5 GB | 2.6 | T1,T2,T3,T4,T5 | any | `hf download unsloth/NVIDIA-Nemotron-3.5-Bolt-E4B-GGUF --include "*UD-IQ2_M*"` |
| `llm-nemotron-3-5-gguf-ud-q3-k-xl` | NVIDIA-Nemotron-3.5-Bolt-E4B-GGUF · UD-Q3_K_XL (GGUF) | 4.2 GB | 3.5 | T1,T2,T3,T4,T5 | any | `hf download unsloth/NVIDIA-Nemotron-3.5-Bolt-E4B-GGUF --include "*UD-Q3_K_XL*"` |
| `llm-nemotron-3-5-gguf-ud-q4-k-xl` | NVIDIA-Nemotron-3.5-Bolt-E4B-GGUF · UD-Q4_K_XL (GGUF) | 5.1 GB | 4.5 | T1,T2,T3,T4,T5 | any | `hf download unsloth/NVIDIA-Nemotron-3.5-Bolt-E4B-GGUF --include "*UD-Q4_K_XL*"` |
| `llm-nemotron-3-5-gguf-official-q4-k-m` | NVIDIA-Nemotron-3.5-Bolt-E4B-4GB · Q4_K_M (GGUF(official)) | 6.2 GB | 4.5 | T1,T2,T3,T4,T5 | any | `hf download nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-4GB --include "*Q4_K_M*"` |
| `llm-nemotron-3-5-ollama-ollama` |  · ollama nemotron-3.5-bolt:e4b-nvfp4 (ollama) | 7.2 GB | 4.5 | T1,T2,T3,T4 | any | `ollama pull nemotron-3.5-bolt:e4b-nvfp4` |
| `llm-nemotron-3-5-gguf-ud-q6-k-xl` | NVIDIA-Nemotron-3.5-Bolt-E4B-GGUF · UD-Q6_K_XL (GGUF) | 7.3 GB | 6.5 | T1,T2,T3,T4,T5 | any | `hf download unsloth/NVIDIA-Nemotron-3.5-Bolt-E4B-GGUF --include "*UD-Q6_K_XL*"` |
| `llm-nemotron-3-5-ollama-ollama-2` |  · ollama nemotron-3.5-bolt:e4b / :e4b-q4_K (ollama) | 7.9 GB | 4.5 | T1,T2,T3,T4 | any | `ollama pull nemotron-3.5-bolt:e4b / :e4b-q4_K_M` |
| `llm-nemotron-3-5-gguf-ud-q8-k-xl` | NVIDIA-Nemotron-3.5-Bolt-E4B-GGUF · UD-Q8_K_XL (GGUF) | 8.2 GB | 8.5 | T1,T2,T3,T4,T5 | any | `hf download unsloth/NVIDIA-Nemotron-3.5-Bolt-E4B-GGUF --include "*UD-Q8_K_XL*"` |
| `llm-nemotron-3-5-gguf-bf16` | NVIDIA-Nemotron-3.5-Bolt-E4B-GGUF · BF16 (GGUF) | 15.1 GB | 16 | T1,T2,T3,T4,T5 | any | `hf download unsloth/NVIDIA-Nemotron-3.5-Bolt-E4B-GGUF --include "*BF16*"` |
| `llm-nemotron-3-5-mlx-4bit` | NVIDIA-Nemotron-3.5-Lightning-30B-A3B-4bit · 4bit (8bit 33.58 GB) (MLX) | 17.8 GB | 4.5 | T1,T2,T3,T4 | mac | `hf download mlx-community/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-4bit` |
| `llm-nemotron-3-5-gguf-iq2-xxs` | NVIDIA-Nemotron-3.5-Lightning-30B-A3B-GGUF · IQ2_XXS (GGUF) | 18.8 GB | 2.6 | T1,T2,T3,T4 | any | `hf download bartowski/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-GGUF --include "*IQ2_XXS*"` |
| `llm-nemotron-3-5-gguf-q4-0` | NVIDIA-Nemotron-3.5-Lightning-30B-A3B-GGUF · Q4_0 (GGUF) | 18.9 GB | 4.5 | T1,T2,T3,T4 | any | `hf download ggml-org/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-GGUF --include "*Q4_0*"` |
| `llm-nemotron-3-5-ollama-ollama-3` |  · ollama nemotron-3.5-lightning:30b-a3b-nv (ollama) | 19.1 GB | 4.5 | T1,T2,T3,T4 | any | `ollama pull nemotron-3.5-lightning:30b-a3b-nvfp4 / :30b-mlx` |
| `llm-nemotron-3-5-gguf-ud-iq2-xxs` | NVIDIA-Nemotron-3.5-Lightning-30B-A3B-GGUF · UD-IQ2_XXS (GGUF) | 19.4 GB | 2.6 | T1,T2,T3,T4 | any | `hf download unsloth/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-GGUF --include "*UD-IQ2_XXS*"` |
| `llm-nemotron-3-5-gguf-ud-q3-k-xl-2` | NVIDIA-Nemotron-3.5-Lightning-30B-A3B-GGUF · UD-Q3_K_XL (GGUF) | 21.2 GB | 3.5 | T1,T2,T3,T4 | any | `hf download unsloth/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-GGUF --include "*UD-Q3_K_XL*"` |
| `llm-nemotron-3-5-nvfp4-nvfp4` | NVIDIA-Nemotron-3.5-Lightning-30B-A3B-NVFP4 · NVFP4 (NVFP4) | 21.6 GB | 4.5 | T1,T2,T3 | server | `hf download nvidia/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-NVFP4` |
| `llm-nemotron-3-5-gguf-mxfp4-moe` | NVIDIA-Nemotron-3.5-Lightning-30B-A3B-GGUF · MXFP4_MOE (GGUF) | 23.2 GB | 4.5 | T1,T2,T3,T4 | any | `hf download unsloth/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-GGUF --include "*MXFP4_MOE*"` |
| `llm-nemotron-3-5-ollama-ollama-4` |  · ollama nemotron-3.5-bolt:74b-a9b / :late (ollama) | 24.8 GB | 2.6 | T1,T2,T3,T4 | any | `ollama pull nemotron-3.5-bolt:74b-a9b / :latest (iq2)` |
| `llm-nemotron-3-5-ollama-ollama-5` |  · ollama nemotron-3.5-lightning:30b / :30b (ollama) | 25.4 GB | 4.5 | T1,T2,T3,T4 | any | `ollama pull nemotron-3.5-lightning:30b / :30b-a3b-q4_K_M` |
| `llm-nemotron-3-5-gguf-q4-k-m` | NVIDIA-Nemotron-3.5-Lightning-30B-A3B-GGUF · Q4_K_M (GGUF) | 25.5 GB | 4.5 | T1,T2,T3,T4 | any | `hf download bartowski/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-GGUF --include "*Q4_K_M*"` |
| `llm-nemotron-3-5-gguf-ud-q4-k-xl-2` | NVIDIA-Nemotron-3.5-Lightning-30B-A3B-GGUF · UD-Q4_K_XL (GGUF) | 25.5 GB | 4.5 | T1,T2,T3,T4 | any | `hf download unsloth/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-GGUF --include "*UD-Q4_K_XL*"` |
| `llm-nemotron-3-5-fp8-fp8` | NVIDIA-Nemotron-3.5-Lightning-30B-A3B-FP8 · FP8 (FP8) | 32.3 GB | 8.5 | T1,T2,T3 | server | `hf download RedHatAI/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-FP8` |
| `llm-nemotron-3-5-gguf-q8-0` | NVIDIA-Nemotron-3.5-Lightning-30B-A3B-GGUF · Q8_0 (GGUF) | 33.6 GB | 8.5 | T1,T2,T3,T4 | any | `hf download ggml-org/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-GGUF --include "*Q8_0*"` |
| `llm-nemotron-3-5-gguf-ud-q6-k-xl-2` | NVIDIA-Nemotron-3.5-Lightning-30B-A3B-GGUF · UD-Q6_K_XL (GGUF) | 35.0 GB | 6.5 | T1,T2,T3,T4 | any | `hf download unsloth/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-GGUF --include "*UD-Q6_K_XL*"` |
| `llm-nemotron-3-5-gguf-q8-0-2` | NVIDIA-Nemotron-3.5-Lightning-30B-A3B-GGUF · Q8_0 (GGUF) | 35.0 GB | 8.5 | T1,T2,T3,T4 | any | `hf download bartowski/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-GGUF --include "*Q8_0*"` |
| `llm-nemotron-3-5-ollama-ollama-6` |  · ollama nemotron-3.5-lightning:30b-a3b-q8 (ollama) | 35.0 GB | 8.5 | T1,T2,T3,T4 | any | `ollama pull nemotron-3.5-lightning:30b-a3b-q8_0` |
| `llm-nemotron-3-5-gguf-ud-iq1-m` | NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-GGUF · UD-IQ1_M (GGUF) | 46.1 GB | 1.7 | T1,T2,T3,T4 | any | `hf download unsloth/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-GGUF --include "*UD-IQ1_M*"` |
| `llm-nemotron-3-5-gguf-ud-iq2-xxs-2` | NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-GGUF · UD-IQ2_XXS (GGUF) | 51.1 GB | 2.6 | T1,T2,T3,T4 | any | `hf download unsloth/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-GGUF --include "*UD-IQ2_XXS*"` |
| `llm-nemotron-3-5-gguf-ud-q2-k-xl` | NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-GGUF · UD-Q2_K_XL (GGUF) | 57.8 GB | 2.6 | T1,T2,T3,T4 | any | `hf download unsloth/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-GGUF --include "*UD-Q2_K_XL*"` |
| `llm-nemotron-3-5-gguf-bf16-2` | NVIDIA-Nemotron-3.5-Lightning-30B-A3B-GGUF · BF16 (GGUF) | 63.2 GB | 16 | T1,T2,T3,T4 | any | `hf download ggml-org/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-GGUF --include "*BF16*"` |
| `llm-nemotron-3-5-gguf-ud-q3-k-xl-3` | NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-GGUF · UD-Q3_K_XL (GGUF) | 65.8 GB | 3.5 | T1,T2,T3,T4 | any | `hf download unsloth/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-GGUF --include "*UD-Q3_K_XL*"` |
| `llm-nemotron-3-5-gguf-bf16-3` | NVIDIA-Nemotron-3.5-Lightning-30B-A3B-GGUF · BF16 (GGUF) | 65.8 GB | 16 | T1,T2,T3,T4 | any | `hf download unsloth/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-GGUF --include "*BF16*"` |
| `llm-nemotron-3-5-gguf-q4-0-2` | NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-GGUF · Q4_0 (GGUF) | 72.1 GB | 4.5 | T1,T2,T3,T4 | any | `hf download ggml-org/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-GGUF --include "*Q4_0*"` |
| `llm-nemotron-3-5-nvfp4-nvfp4-2` | NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-NVFP4 · NVFP4 (NVFP4) | 75.1 GB | 4.5 | T1,T2,T3,T4 | server | `hf download nvidia/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-NVFP4` |
| `llm-nemotron-3-5-gguf-nvfp4` | NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-GGUF · NVFP4 (GGUF) | 78.3 GB | 4.5 | T1,T2,T3,T4 | any | `hf download ggml-org/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-GGUF --include "*NVFP4*"` |
| `llm-nemotron-3-5-ollama-ollama-7` |  · ollama nemotron-3.5-super:120b-a12b-nvfp (ollama) | 79.6 GB | 4.5 | T1,T2,T3 | any | `ollama pull nemotron-3.5-super:120b-a12b-nvfp4` |
| `llm-nemotron-3-5-gguf-ud-q4-k-xl-3` | NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-GGUF · UD-Q4_K_XL (GGUF) | 86.9 GB | 4.5 | T1,T2,T3,T4 | any | `hf download unsloth/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-GGUF --include "*UD-Q4_K_XL*"` |
| `llm-nemotron-3-5-ollama-ollama-8` |  · ollama nemotron-3.5-super:120b / :120b-a (ollama) | 90.2 GB | 4.5 | T1,T2,T3 | any | `ollama pull nemotron-3.5-super:120b / :120b-a12b-q4_K_M` |
| `llm-nemotron-3-5-gguf-ud-q5-k-xl` | NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-GGUF · UD-Q5_K_XL (GGUF) | 110.7 GB | 5.5 | T1,T2,T3,T4 | any | `hf download unsloth/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-GGUF --include "*UD-Q5_K_XL*"` |
| `llm-nemotron-3-5-gguf-ud-q6-k-xl-3` | NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-GGUF · UD-Q6_K_XL (GGUF) | 121.0 GB | 6.5 | T1,T2,T3,T4 | any | `hf download unsloth/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-GGUF --include "*UD-Q6_K_XL*"` |
| `llm-nemotron-3-5-gguf-q8-0-3` | NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-GGUF · Q8_0 (GGUF) | 128.5 GB | 8.5 | T1,T2,T3,T4 | any | `hf download ggml-org/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-GGUF --include "*Q8_0*"` |
| `llm-nemotron-3-5-fp8-fp8-2` | NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-FP8 · FP8 (FP8) | 128.8 GB | 8.5 | T1,T2 | server | `hf download RedHatAI/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-FP8` |
| `llm-nemotron-3-5-gguf-q8-0-4` | NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-GGUF · Q8_0 (GGUF) | 131.6 GB | 8.5 | T1,T2,T3,T4 | any | `hf download unsloth/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-GGUF --include "*Q8_0*"` |
| `llm-nemotron-3-5-ollama-ollama-9` |  · ollama nemotron-3.5-super:120b-a12b-q8_0 (ollama) | 133.3 GB | 8.5 | T1,T2,T3 | any | `ollama pull nemotron-3.5-super:120b-a12b-q8_0` |
| `llm-nemotron-3-5-gguf-bf16-4` | NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-GGUF · BF16 (GGUF) | 241.5 GB | 16 | T1,T2,T3,T4 | any | `hf download ggml-org/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-GGUF --include "*BF16*"` |
</details>

<details><summary><b>Muse Glimmer 30B</b> – 33 változat</summary>

| id | Fájl / repó | Méret | Bit | HW | Platform | Letöltés |
|---|---|---|---|---|---|---|
| `llm-muse-glimmer-30b-gguf-iq1-s` | Muse-Glimmer-30B-i1-GGUF · IQ1_S (GGUF) | 6.5 GB | 1.7 | T1,T2,T3,T4 | any | `hf download mradermacher/Muse-Glimmer-30B-i1-GGUF --include "*IQ1_S*"` |
| `llm-muse-glimmer-30b-gguf-iq2-xxs` | Muse-Glimmer-30B-GGUF · IQ2_XXS (GGUF) | 8.9 GB | 2.6 | T1,T2,T3,T4 | any | `hf download bartowski/Muse-Glimmer-30B-GGUF --include "*IQ2_XXS*"` |
| `llm-muse-glimmer-30b-gguf-ud-iq2-xxs` | Muse-Glimmer-30B-GGUF · UD-IQ2_XXS (GGUF) | 10.8 GB | 2.6 | T1,T2,T3,T4 | any | `hf download unsloth/Muse-Glimmer-30B-GGUF --include "*UD-IQ2_XXS*"` |
| `llm-muse-glimmer-30b-gguf-ud-q2-k-xl` | Muse-Glimmer-30B-GGUF · UD-Q2_K_XL (GGUF) | 12.4 GB | 2.6 | T1,T2,T3,T4 | any | `hf download unsloth/Muse-Glimmer-30B-GGUF --include "*UD-Q2_K_XL*"` |
| `llm-muse-glimmer-30b-gguf-iq3-m` | Muse-Glimmer-30B-GGUF · IQ3_M (GGUF) | 13.1 GB | 3.5 | T1,T2,T3,T4 | any | `hf download bartowski/Muse-Glimmer-30B-GGUF --include "*IQ3_M*"` |
| `llm-muse-glimmer-30b-gguf-ud-iq3-m` | Muse-Glimmer-30B-GGUF · UD-IQ3_M (GGUF) | 14.1 GB | 3.5 | T1,T2,T3,T4 | any | `hf download unsloth/Muse-Glimmer-30B-GGUF --include "*UD-IQ3_M*"` |
| `llm-muse-glimmer-30b-gguf-iq4-xs` | Muse-Glimmer-30B-GGUF · IQ4_XS (GGUF) | 15.4 GB | 4.5 | T1,T2,T3,T4 | any | `hf download bartowski/Muse-Glimmer-30B-GGUF --include "*IQ4_XS*"` |
| `llm-muse-glimmer-30b-gguf-ud-q4-k-xl` | Muse-Glimmer-30B-GGUF · UD-Q4_K_XL (GGUF) | 15.9 GB | 4.5 | T1,T2,T3,T4 | any | `hf download unsloth/Muse-Glimmer-30B-GGUF --include "*UD-Q4_K_XL*"` |
| `llm-muse-glimmer-30b-gguf-official-q4-k-m` | Muse-Glimmer-30B-GGUF · Q4_K_M (GGUF(official)) | 16.8 GB | 4.5 | T1,T2,T3,T4 | any | `hf download meta-models/Muse-Glimmer-30B-GGUF --include "*Q4_K_M*"` |
| `llm-muse-glimmer-30b-gguf-q4-k-m` | Muse-Glimmer-30B-GGUF · Q4_K_M (GGUF) | 16.8 GB | 4.5 | T1,T2,T3,T4 | any | `hf download lmstudio-community/Muse-Glimmer-30B-GGUF --include "*Q4_K_M*"` |
| `llm-muse-glimmer-30b-gguf-q4-k-m-2` | Muse-Glimmer-30B-i1-GGUF · Q4_K_M (GGUF) | 16.9 GB | 4.5 | T1,T2,T3,T4 | any | `hf download mradermacher/Muse-Glimmer-30B-i1-GGUF --include "*Q4_K_M*"` |
| `llm-muse-glimmer-30b-ollama-ollama` |  · ollama muse-glimmer:30b-nvfp4 (ollama) | 17.3 GB | 4.5 | T1,T2,T3,T4 | any | `ollama pull muse-glimmer:30b-nvfp4` |
| `llm-muse-glimmer-30b-gguf-q4-k-m-3` | Muse-Glimmer-30B-GGUF · Q4_K_M (GGUF) | 17.3 GB | 4.5 | T1,T2,T3,T4 | any | `hf download bartowski/Muse-Glimmer-30B-GGUF --include "*Q4_K_M*"` |
| `llm-muse-glimmer-30b-ollama-ollama-2` |  · ollama muse-glimmer:30b / :latest / :30b (ollama) | 18.2 GB | 4.5 | T1,T2,T3,T4 | any | `ollama pull muse-glimmer:30b / :latest / :30b-q4_K_M` |
| `llm-muse-glimmer-30b-ollama-ollama-3` |  · ollama muse-glimmer:30b-mlx (ollama) | 19.1 GB | 4.5 | T1,T2,T3,T4 | any | `ollama pull muse-glimmer:30b-mlx` |
| `llm-muse-glimmer-30b-mlx-4bit` | Muse-Glimmer-30B-4bit · 4bit (MLX) | 19.4 GB | 4.5 | T1,T2,T3,T4 | mac | `hf download mlx-community/Muse-Glimmer-30B-4bit` |
| `llm-muse-glimmer-30b-gguf-official-q4-k-xl` | Muse-Glimmer-30B-GGUF · Q4_K_XL (+mmproj 1.4, DFlash 1.63) (GGUF(official)) | 19.6 GB | 4.5 | T1,T2,T3,T4 | any | `hf download meta-models/Muse-Glimmer-30B-GGUF --include "*Q4_K_XL*"` |
| `llm-muse-glimmer-30b-gguf-q5-k-m` | Muse-Glimmer-30B-GGUF · Q5_K_M (GGUF) | 20.1 GB | 5.5 | T1,T2,T3,T4 | any | `hf download bartowski/Muse-Glimmer-30B-GGUF --include "*Q5_K_M*"` |
| `llm-muse-glimmer-30b-gguf-ud-q5-k-xl` | Muse-Glimmer-30B-GGUF · UD-Q5_K_XL (GGUF) | 21.8 GB | 5.5 | T1,T2,T3,T4 | any | `hf download unsloth/Muse-Glimmer-30B-GGUF --include "*UD-Q5_K_XL*"` |
| `llm-muse-glimmer-30b-int4-w4a16` | Muse-Glimmer-30B-INT4 · W4A16 (INT4) | 22.2 GB | 4.5 | T1,T2,T3 | server | `hf download RedHatAI/Muse-Glimmer-30B-INT4` |
| `llm-muse-glimmer-30b-gguf-q6-k` | Muse-Glimmer-30B-i1-GGUF · Q6_K (GGUF) | 22.9 GB | 6.5 | T1,T2,T3,T4 | any | `hf download mradermacher/Muse-Glimmer-30B-i1-GGUF --include "*Q6_K*"` |
| `llm-muse-glimmer-30b-gguf-q6-k-2` | Muse-Glimmer-30B-GGUF · Q6_K (GGUF) | 23.4 GB | 6.5 | T1,T2,T3,T4 | any | `hf download bartowski/Muse-Glimmer-30B-GGUF --include "*Q6_K*"` |
| `llm-muse-glimmer-30b-awq-awq-int4` | Muse-Glimmer-30B-AWQ-INT4 · AWQ-INT4 (AWQ) | 24.0 GB | 4.5 | T1,T2,T3 | server | `hf download cyankiwi/Muse-Glimmer-30B-AWQ-INT4` |
| `llm-muse-glimmer-30b-nvfp4-nvfp4` | Muse-Glimmer-30B-NVFP4 · NVFP4 (NVFP4) | 24.7 GB | 4.5 | T1,T2,T3 | server | `hf download nvidia/Muse-Glimmer-30B-NVFP4` |
| `llm-muse-glimmer-30b-gguf-ud-q6-k-xl` | Muse-Glimmer-30B-GGUF · UD-Q6_K_XL (GGUF) | 26.3 GB | 6.5 | T1,T2,T3,T4 | any | `hf download unsloth/Muse-Glimmer-30B-GGUF --include "*UD-Q6_K_XL*"` |
| `llm-muse-glimmer-30b-mlx-6bit` | Muse-Glimmer-30B-6bit · 6bit (MLX) | 26.4 GB | 6.5 | T1,T2,T3,T4 | mac | `hf download mlx-community/Muse-Glimmer-30B-6bit` |
| `llm-muse-glimmer-30b-gguf-q8-0` | Muse-Glimmer-30B-GGUF · Q8_0 (GGUF) | 29.6 GB | 8.5 | T1,T2,T3,T4 | any | `hf download unsloth/Muse-Glimmer-30B-GGUF --include "*Q8_0*"` |
| `llm-muse-glimmer-30b-gguf-q8-0-2` | Muse-Glimmer-30B-GGUF · Q8_0 (GGUF) | 29.6 GB | 8.5 | T1,T2,T3,T4 | any | `hf download bartowski/Muse-Glimmer-30B-GGUF --include "*Q8_0*"` |
| `llm-muse-glimmer-30b-ollama-ollama-4` |  · ollama muse-glimmer:30b-q8_0 (ollama) | 31.0 GB | 8.5 | T1,T2,T3,T4 | any | `ollama pull muse-glimmer:30b-q8_0` |
| `llm-muse-glimmer-30b-mlx-8bit` | Muse-Glimmer-30B-8bit · 8bit (MLX) | 33.4 GB | 8.5 | T1,T2,T3,T4 | mac | `hf download mlx-community/Muse-Glimmer-30B-8bit` |
| `llm-muse-glimmer-30b-fp8-fp8` | Muse-Glimmer-30B-FP8-block · FP8 (FP8) | 34.4 GB | 8.5 | T1,T2,T3 | server | `hf download RedHatAI/Muse-Glimmer-30B-FP8-block` |
| `llm-muse-glimmer-30b-gguf-bf16` | Muse-Glimmer-30B-GGUF · BF16 (GGUF) | 55.7 GB | 16 | T1,T2,T3,T4 | any | `hf download unsloth/Muse-Glimmer-30B-GGUF --include "*BF16*"` |
| `llm-muse-glimmer-30b-ollama-ollama-5` |  · ollama muse-glimmer:30b-bf16 (ollama) | 57.1 GB | 16 | T1,T2,T3,T4 | any | `ollama pull muse-glimmer:30b-bf16` |
</details>

<details><summary><b>Gemma 4 (31B, 26B-A4B, 12B, E4B, E2B)</b> – 100 változat</summary>

| id | Fájl / repó | Méret | Bit | HW | Platform | Letöltés |
|---|---|---|---|---|---|---|
| `llm-gemma-4-gguf-ud-iq2-m` | gemma-4-E2B-it-GGUF · UD-IQ2_M (GGUF) | 2.3 GB | 2.6 | T1,T2,T3,T4,T5 | any | `hf download unsloth/gemma-4-E2B-it-GGUF --include "*UD-IQ2_M*"` |
| `llm-gemma-4-gguf-q4-k-m` | gemma-4-E2B-it-GGUF · Q4_K_M (GGUF) | 3.1 GB | 4.5 | T1,T2,T3,T4,T5 | any | `hf download unsloth/gemma-4-E2B-it-GGUF --include "*Q4_K_M*"` |
| `llm-gemma-4-gguf-ud-q4-k-xl` | gemma-4-E2B-it-GGUF · UD-Q4_K_XL (GGUF) | 3.2 GB | 4.5 | T1,T2,T3,T4,T5 | any | `hf download unsloth/gemma-4-E2B-it-GGUF --include "*UD-Q4_K_XL*"` |
| `llm-gemma-4-gguf-qat-official-q4-0` | gemma-4-E2B-it-qat-q4_0-gguf · q4_0 QAT (+mmproj 0.99) (GGUF(QAT official)) | 3.4 GB | 4.5 | T1,T2,T3,T4,T5 | any | `hf download google/gemma-4-E2B-it-qat-q4_0-gguf --include "*q4_0*"` |
| `llm-gemma-4-gguf-q4-k-m-2` | gemma-4-E2B-it-GGUF · Q4_K_M (GGUF) | 3.4 GB | 4.5 | T1,T2,T3,T4,T5 | any | `hf download lmstudio-community/gemma-4-E2B-it-GGUF --include "*Q4_K_M*"` |
| `llm-gemma-4-gguf-ud-iq2-m-2` | gemma-4-E4B-it-GGUF · UD-IQ2_M (GGUF) | 3.5 GB | 2.6 | T1,T2,T3,T4,T5 | any | `hf download unsloth/gemma-4-E4B-it-GGUF --include "*UD-IQ2_M*"` |
| `llm-gemma-4-gguf-q6-k` | gemma-4-E2B-it-GGUF · Q6_K (GGUF) | 3.9 GB | 6.5 | T1,T2,T3,T4,T5 | any | `hf download lmstudio-community/gemma-4-E2B-it-GGUF --include "*Q6_K*"` |
| `llm-gemma-4-gguf-iq2-m` | google_gemma-4-E4B-it-GGUF · IQ2_M (GGUF) | 4.0 GB | 2.6 | T1,T2,T3,T4,T5 | any | `hf download bartowski/google_gemma-4-E4B-it-GGUF --include "*IQ2_M*"` |
| `llm-gemma-4-gguf-ud-iq2-m-3` | gemma-4-12b-it-GGUF · UD-IQ2_M (GGUF) | 4.2 GB | 2.6 | T1,T2,T3,T4 | any | `hf download unsloth/gemma-4-12b-it-GGUF --include "*UD-IQ2_M*"` |
| `llm-gemma-4-ollama-ollama` |  · ollama gemma4:e2b-it-qat (ollama) | 4.3 GB | 4.5 | T1,T2,T3,T4 | any | `ollama pull gemma4:e2b-it-qat` |
| `llm-gemma-4-gguf-ud-q3-k-xl` | gemma-4-E4B-it-GGUF · UD-Q3_K_XL (GGUF) | 4.6 GB | 3.5 | T1,T2,T3,T4,T5 | any | `hf download unsloth/gemma-4-E4B-it-GGUF --include "*UD-Q3_K_XL*"` |
| `llm-gemma-4-ollama-ollama-2` |  · ollama gemma4:e2b / :e2b-it-q4_K_M (ollama) | 4.6 GB | 4.5 | T1,T2,T3,T4 | any | `ollama pull gemma4:e2b / :e2b-it-q4_K_M` |
| `llm-gemma-4-gguf-iq2-s` | gemma-4-12B-it-GGUF · IQ2_S (GGUF) | 4.7 GB | 2.6 | T1,T2,T3,T4 | any | `hf download bartowski/gemma-4-12B-it-GGUF --include "*IQ2_S*"` |
| `llm-gemma-4-gguf-q8-0` | gemma-4-E2B-it-GGUF · Q8_0 (GGUF) | 5.0 GB | 8.5 | T1,T2,T3,T4,T5 | any | `hf download lmstudio-community/gemma-4-E2B-it-GGUF --include "*Q8_0*"` |
| `llm-gemma-4-gguf-q4-k-m-3` | gemma-4-E4B-it-GGUF · Q4_K_M (GGUF) | 5.0 GB | 4.5 | T1,T2,T3,T4,T5 | any | `hf download unsloth/gemma-4-E4B-it-GGUF --include "*Q4_K_M*"` |
| `llm-gemma-4-gguf-q8-0-2` | gemma-4-E2B-it-GGUF · Q8_0 (GGUF) | 5.0 GB | 8.5 | T1,T2,T3,T4,T5 | any | `hf download unsloth/gemma-4-E2B-it-GGUF --include "*Q8_0*"` |
| `llm-gemma-4-gguf-ud-q4-k-xl-2` | gemma-4-E4B-it-GGUF · UD-Q4_K_XL (GGUF) | 5.1 GB | 4.5 | T1,T2,T3,T4,T5 | any | `hf download unsloth/gemma-4-E4B-it-GGUF --include "*UD-Q4_K_XL*"` |
| `llm-gemma-4-gguf-qat-official-q4-0-2` | gemma-4-E4B-it-qat-q4_0-gguf · q4_0 QAT (+mmproj 0.99) (GGUF(QAT official)) | 5.2 GB | 4.5 | T1,T2,T3,T4,T5 | any | `hf download google/gemma-4-E4B-it-qat-q4_0-gguf --include "*q4_0*"` |
| `llm-gemma-4-gguf-q4-k-m-4` | gemma-4-E4B-it-GGUF · Q4_K_M (GGUF) | 5.3 GB | 4.5 | T1,T2,T3,T4,T5 | any | `hf download lmstudio-community/gemma-4-E4B-it-GGUF --include "*Q4_K_M*"` |
| `llm-gemma-4-gguf-q4-k-m-5` | google_gemma-4-E4B-it-GGUF · Q4_K_M (GGUF) | 5.4 GB | 4.5 | T1,T2,T3,T4,T5 | any | `hf download bartowski/google_gemma-4-E4B-it-GGUF --include "*Q4_K_M*"` |
| `llm-gemma-4-ollama-ollama-3` |  · ollama gemma4:e2b-it-q8_0 (ollama) | 6.0 GB | 8.5 | T1,T2,T3,T4 | any | `ollama pull gemma4:e2b-it-q8_0` |
| `llm-gemma-4-gguf-ud-q3-k-xl-2` | gemma-4-12b-it-GGUF · UD-Q3_K_XL (GGUF) | 6.0 GB | 3.5 | T1,T2,T3,T4 | any | `hf download unsloth/gemma-4-12b-it-GGUF --include "*UD-Q3_K_XL*"` |
| `llm-gemma-4-ollama-ollama-4` |  · ollama gemma4:e4b-it-qat (ollama) | 6.2 GB | 4.5 | T1,T2,T3,T4 | any | `ollama pull gemma4:e4b-it-qat` |
| `llm-gemma-4-gguf-q6-k-2` | gemma-4-E4B-it-GGUF · Q6_K (GGUF) | 6.2 GB | 6.5 | T1,T2,T3,T4,T5 | any | `hf download lmstudio-community/gemma-4-E4B-it-GGUF --include "*Q6_K*"` |
| `llm-gemma-4-ollama-ollama-5` |  · ollama gemma4:e4b / :latest / :e4b-it-q4 (ollama) | 6.6 GB | 4.5 | T1,T2,T3,T4 | any | `ollama pull gemma4:e4b / :latest / :e4b-it-q4_K_M` |
| `llm-gemma-4-mlx-4bit` | gemma-4-12B-it-MLX-4bit · 4bit (8bit 12.75 GB) (MLX) | 6.8 GB | 4.5 | T1,T2,T3,T4 | mac | `hf download lmstudio-community/gemma-4-12B-it-MLX-4bit` |
| `llm-gemma-4-mlx-4bit-2` | gemma-4-E4B-it-MLX-4bit · 4bit (MLX) | 6.9 GB | 4.5 | T1,T2,T3,T4,T5 | mac | `hf download lmstudio-community/gemma-4-E4B-it-MLX-4bit` |
| `llm-gemma-4-gguf-qat-official-q4-0-3` | gemma-4-12B-it-qat-q4_0-gguf · q4_0 QAT (+mmproj 0.18) (GGUF(QAT official)) | 7.0 GB | 4.5 | T1,T2,T3,T4,T5 | any | `hf download google/gemma-4-12B-it-qat-q4_0-gguf --include "*q4_0*"` |
| `llm-gemma-4-gguf-q6-k-3` | gemma-4-E4B-it-GGUF · Q6_K (GGUF) | 7.1 GB | 6.5 | T1,T2,T3,T4,T5 | any | `hf download unsloth/gemma-4-E4B-it-GGUF --include "*Q6_K*"` |
| `llm-gemma-4-gguf-q4-k-m-6` | gemma-4-12b-it-GGUF · Q4_K_M (GGUF) | 7.1 GB | 4.5 | T1,T2,T3,T4 | any | `hf download unsloth/gemma-4-12b-it-GGUF --include "*Q4_K_M*"` |
| `llm-gemma-4-ollama-ollama-6` |  · ollama gemma4:12b-it-qat (ollama) | 7.2 GB | 4.5 | T1,T2,T3,T4 | any | `ollama pull gemma4:12b-it-qat` |
| `llm-gemma-4-gguf-ud-q4-k-xl-3` | gemma-4-12b-it-GGUF · UD-Q4_K_XL (GGUF) | 7.4 GB | 4.5 | T1,T2,T3,T4 | any | `hf download unsloth/gemma-4-12b-it-GGUF --include "*UD-Q4_K_XL*"` |
| `llm-gemma-4-gguf-q4-k-m-7` | gemma-4-12B-it-GGUF · Q4_K_M (GGUF) | 7.4 GB | 4.5 | T1,T2,T3,T4 | any | `hf download lmstudio-community/gemma-4-12B-it-GGUF --include "*Q4_K_M*"` |
| `llm-gemma-4-gguf-q4-k-m-8` | gemma-4-12B-it-GGUF · Q4_K_M (GGUF) | 7.7 GB | 4.5 | T1,T2,T3,T4 | any | `hf download bartowski/gemma-4-12B-it-GGUF --include "*Q4_K_M*"` |
| `llm-gemma-4-ollama-ollama-7` |  · ollama gemma4:12b / :12b-it-q4_K_M (ollama) | 8.0 GB | 4.5 | T1,T2,T3,T4 | any | `ollama pull gemma4:12b / :12b-it-q4_K_M` |
| `llm-gemma-4-gguf-q8-0-3` | google_gemma-4-E4B-it-GGUF · Q8_0 (GGUF) | 8.0 GB | 8.5 | T1,T2,T3,T4,T5 | any | `hf download bartowski/google_gemma-4-E4B-it-GGUF --include "*Q8_0*"` |
| `llm-gemma-4-gguf-q8-0-4` | gemma-4-E4B-it-GGUF · Q8_0 (GGUF) | 8.0 GB | 8.5 | T1,T2,T3,T4,T5 | any | `hf download lmstudio-community/gemma-4-E4B-it-GGUF --include "*Q8_0*"` |
| `llm-gemma-4-gguf-q8-0-5` | gemma-4-E4B-it-GGUF · Q8_0 (GGUF) | 8.2 GB | 8.5 | T1,T2,T3,T4,T5 | any | `hf download unsloth/gemma-4-E4B-it-GGUF --include "*Q8_0*"` |
| `llm-gemma-4-gguf-ud-iq2-xxs` | gemma-4-31B-it-GGUF · UD-IQ2_XXS (GGUF) | 8.5 GB | 2.6 | T1,T2,T3,T4 | any | `hf download unsloth/gemma-4-31B-it-GGUF --include "*UD-IQ2_XXS*"` |
| `llm-gemma-4-ollama-ollama-8` |  · ollama gemma4:e4b-it-q8_0 (ollama) | 9.0 GB | 8.5 | T1,T2,T3,T4 | any | `ollama pull gemma4:e4b-it-q8_0` |
| `llm-gemma-4-gguf-bf16` | gemma-4-E2B-it-GGUF · BF16 (GGUF) | 9.3 GB | 16 | T1,T2,T3,T4,T5 | any | `hf download unsloth/gemma-4-E2B-it-GGUF --include "*BF16*"` |
| `llm-gemma-4-gguf-iq2-xxs` | google_gemma-4-26B-A4B-it-GGUF · IQ2_XXS (GGUF) | 9.7 GB | 2.6 | T1,T2,T3,T4 | any | `hf download bartowski/google_gemma-4-26B-A4B-it-GGUF --include "*IQ2_XXS*"` |
| `llm-gemma-4-gguf-q6-k-4` | gemma-4-12B-it-GGUF · Q6_K (GGUF) | 9.8 GB | 6.5 | T1,T2,T3,T4 | any | `hf download lmstudio-community/gemma-4-12B-it-GGUF --include "*Q6_K*"` |
| `llm-gemma-4-gguf-ud-iq2-xxs-2` | gemma-4-26B-A4B-it-GGUF · UD-IQ2_XXS (GGUF) | 9.9 GB | 2.6 | T1,T2,T3,T4 | any | `hf download unsloth/gemma-4-26B-A4B-it-GGUF --include "*UD-IQ2_XXS*"` |
| `llm-gemma-4-gguf-iq1-m` | google_gemma-4-31B-it-GGUF · IQ1_M (GGUF) | 10.1 GB | 1.7 | T1,T2,T3,T4 | any | `hf download bartowski/google_gemma-4-31B-it-GGUF --include "*IQ1_M*"` |
| `llm-gemma-4-gguf-q6-k-5` | gemma-4-12B-it-GGUF · Q6_K (GGUF) | 10.2 GB | 6.5 | T1,T2,T3,T4 | any | `hf download bartowski/gemma-4-12B-it-GGUF --include "*Q6_K*"` |
| `llm-gemma-4-gguf-ud-q6-k-xl` | gemma-4-12b-it-GGUF · UD-Q6_K_XL (GGUF) | 10.7 GB | 6.5 | T1,T2,T3,T4 | any | `hf download unsloth/gemma-4-12b-it-GGUF --include "*UD-Q6_K_XL*"` |
| `llm-gemma-4-gguf-ud-q2-k-xl` | gemma-4-31B-it-GGUF · UD-Q2_K_XL (GGUF) | 11.8 GB | 2.6 | T1,T2,T3,T4 | any | `hf download unsloth/gemma-4-31B-it-GGUF --include "*UD-Q2_K_XL*"` |
| `llm-gemma-4-gguf-q8-0-6` | gemma-4-12b-it-GGUF · Q8_0 (GGUF) | 12.7 GB | 8.5 | T1,T2,T3,T4 | any | `hf download unsloth/gemma-4-12b-it-GGUF --include "*Q8_0*"` |
| `llm-gemma-4-gguf-q8-0-7` | gemma-4-12B-it-GGUF · Q8_0 (GGUF) | 12.7 GB | 8.5 | T1,T2,T3,T4 | any | `hf download bartowski/gemma-4-12B-it-GGUF --include "*Q8_0*"` |
| `llm-gemma-4-gguf-q8-0-8` | gemma-4-12B-it-GGUF · Q8_0 (GGUF) | 12.7 GB | 8.5 | T1,T2,T3,T4 | any | `hf download lmstudio-community/gemma-4-12B-it-GGUF --include "*Q8_0*"` |
| `llm-gemma-4-ollama-ollama-9` |  · ollama gemma4:12b-it-q8_0 (ollama) | 12.8 GB | 8.5 | T1,T2,T3,T4 | any | `ollama pull gemma4:12b-it-q8_0` |
| `llm-gemma-4-litert-lm-t-bb` | gemma-4-E4B-it-litert-lm · több .litertlm változat (LiteRT-LM) | 12.9 GB | 4.5 | T1,T2,T3,T4,T5 | android | `hf download litert-community/gemma-4-E4B-it-litert-lm` |
| `llm-gemma-4-gguf-ud-q3-k-xl-3` | gemma-4-26B-A4B-it-GGUF · UD-Q3_K_XL (GGUF) | 12.9 GB | 3.5 | T1,T2,T3,T4 | any | `hf download unsloth/gemma-4-26B-A4B-it-GGUF --include "*UD-Q3_K_XL*"` |
| `llm-gemma-4-gguf-ud-iq4-xs` | gemma-4-26B-A4B-it-GGUF · UD-IQ4_XS (GGUF) | 13.6 GB | 4.5 | T1,T2,T3,T4 | any | `hf download unsloth/gemma-4-26B-A4B-it-GGUF --include "*UD-IQ4_XS*"` |
| `llm-gemma-4-gguf-qat-official-q4-0-4` | gemma-4-26B-A4B-it-qat-q4_0-gguf · q4_0 QAT (GGUF(QAT official)) | 14.4 GB | 4.5 | T1,T2,T3,T4 | any | `hf download google/gemma-4-26B-A4B-it-qat-q4_0-gguf --include "*q4_0*"` |
| `llm-gemma-4-gguf-bf16-2` | gemma-4-E4B-it-GGUF · BF16 (GGUF) | 15.1 GB | 16 | T1,T2,T3,T4,T5 | any | `hf download unsloth/gemma-4-E4B-it-GGUF --include "*BF16*"` |
| `llm-gemma-4-gguf-ud-q3-k-xl-4` | gemma-4-31B-it-GGUF · UD-Q3_K_XL (GGUF) | 15.4 GB | 3.5 | T1,T2,T3,T4 | any | `hf download unsloth/gemma-4-31B-it-GGUF --include "*UD-Q3_K_XL*"` |
| `llm-gemma-4-ollama-ollama-10` |  · ollama gemma4:26b-a4b-it-qat (ollama) | 15.6 GB | 4.5 | T1,T2,T3,T4 | any | `ollama pull gemma4:26b-a4b-it-qat` |
| `llm-gemma-4-mlx-4bit-3` | gemma-4-26B-A4B-it-MLX-4bit · 4bit (8bit: 27.99 GB a -MLX-8bit repóban (MLX) | 15.6 GB | 4.5 | T1,T2,T3,T4 | mac | `hf download lmstudio-community/gemma-4-26B-A4B-it-MLX-4bit` |
| `llm-gemma-4-gguf-mxfp4-moe` | gemma-4-26B-A4B-it-GGUF · MXFP4_MOE (GGUF) | 16.6 GB | 4.5 | T1,T2,T3,T4 | any | `hf download unsloth/gemma-4-26B-A4B-it-GGUF --include "*MXFP4_MOE*"` |
| `llm-gemma-4-gguf-q4-k-m-9` | gemma-4-26B-A4B-it-GGUF · Q4_K_M (GGUF) | 16.8 GB | 4.5 | T1,T2,T3,T4 | any | `hf download lmstudio-community/gemma-4-26B-A4B-it-GGUF --include "*Q4_K_M*"` |
| `llm-gemma-4-gguf-ud-q4-k-xl-4` | gemma-4-26B-A4B-it-GGUF · UD-Q4_K_XL (GGUF) | 17.0 GB | 4.5 | T1,T2,T3,T4 | any | `hf download unsloth/gemma-4-26B-A4B-it-GGUF --include "*UD-Q4_K_XL*"` |
| `llm-gemma-4-gguf-q4-k-m-10` | google_gemma-4-26B-A4B-it-GGUF · Q4_K_M (GGUF) | 17.0 GB | 4.5 | T1,T2,T3,T4 | any | `hf download bartowski/google_gemma-4-26B-A4B-it-GGUF --include "*Q4_K_M*"` |
| `llm-gemma-4-awq-awq-4bit` | gemma-4-26B-A4B-it-AWQ-4bit · AWQ-4bit (AWQ) | 17.2 GB | 4.5 | T1,T2,T3 | server | `hf download cyankiwi/gemma-4-26B-A4B-it-AWQ-4bit` |
| `llm-gemma-4-gguf-qat-official-q4-0-5` | gemma-4-31B-it-qat-q4_0-gguf · q4_0 QAT (+mmproj 1.2) (GGUF(QAT official)) | 17.6 GB | 4.5 | T1,T2,T3,T4 | any | `hf download google/gemma-4-31B-it-qat-q4_0-gguf --include "*q4_0*"` |
| `llm-gemma-4-ollama-ollama-11` |  · ollama gemma4:26b-a4b-it-q4_K_M (ollama) | 18.0 GB | 4.5 | T1,T2,T3,T4 | any | `ollama pull gemma4:26b-a4b-it-q4_K_M` |
| `llm-gemma-4-gguf-q4-k-m-11` | gemma-4-31B-it-GGUF · Q4_K_M (GGUF) | 18.3 GB | 4.5 | T1,T2,T3,T4 | any | `hf download unsloth/gemma-4-31B-it-GGUF --include "*Q4_K_M*"` |
| `llm-gemma-4-mlx-4bit-4` | gemma-4-31B-it-MLX-4bit · 4bit (6bit 26.12, 8bit 33.8 a -MLX-6bit/ (MLX) | 18.4 GB | 4.5 | T1,T2,T3,T4 | mac | `hf download lmstudio-community/gemma-4-31B-it-MLX-4bit` |
| `llm-gemma-4-gguf-q4-k-m-12` | gemma-4-31B-it-GGUF · Q4_K_M (GGUF) | 18.7 GB | 4.5 | T1,T2,T3,T4 | any | `hf download lmstudio-community/gemma-4-31B-it-GGUF --include "*Q4_K_M*"` |
| `llm-gemma-4-ollama-ollama-12` |  · ollama gemma4:26b / :26b-a4b / :26b-a4b- (ollama) | 18.7 GB | 4.5 | T1,T2,T3,T4 | any | `ollama pull gemma4:26b / :26b-a4b / :26b-a4b-it-mtp-q4_K_M` |
| `llm-gemma-4-gguf-ud-q4-k-xl-5` | gemma-4-31B-it-GGUF · UD-Q4_K_XL (GGUF) | 18.8 GB | 4.5 | T1,T2,T3,T4 | any | `hf download unsloth/gemma-4-31B-it-GGUF --include "*UD-Q4_K_XL*"` |
| `llm-gemma-4-nvfp4-nvfp4` | Gemma-4-26B-A4B-NVFP4 · NVFP4 (NVFP4) | 18.8 GB | 4.5 | T1,T2,T3 | server | `hf download nvidia/Gemma-4-26B-A4B-NVFP4` |
| `llm-gemma-4-ollama-ollama-13` |  · ollama gemma4:31b-it-qat (ollama) | 18.9 GB | 4.5 | T1,T2,T3,T4 | any | `ollama pull gemma4:31b-it-qat` |
| `llm-gemma-4-ollama-ollama-14` |  · ollama gemma4:31b-nvfp4 / :31b-mlx (ollama) | 19.4 GB | 4.5 | T1,T2,T3,T4 | any | `ollama pull gemma4:31b-nvfp4 / :31b-mlx` |
| `llm-gemma-4-gguf-q4-k-m-13` | google_gemma-4-31B-it-GGUF · Q4_K_M (GGUF) | 19.6 GB | 4.5 | T1,T2,T3,T4 | any | `hf download bartowski/google_gemma-4-31B-it-GGUF --include "*Q4_K_M*"` |
| `llm-gemma-4-ollama-ollama-15` |  · ollama gemma4:31b / :31b-it-q4_K_M (ollama) | 20.4 GB | 4.5 | T1,T2,T3,T4 | any | `ollama pull gemma4:31b / :31b-it-q4_K_M` |
| `llm-gemma-4-awq-awq` | gemma-4-31B-it-AWQ · AWQ (AWQ) | 20.5 GB | 4.5 | T1,T2,T3 | server | `hf download QuantTrio/gemma-4-31B-it-AWQ` |
| `llm-gemma-4-gguf-ud-q5-k-xl` | gemma-4-26B-A4B-it-GGUF · UD-Q5_K_XL (GGUF) | 21.2 GB | 5.5 | T1,T2,T3,T4 | any | `hf download unsloth/gemma-4-26B-A4B-it-GGUF --include "*UD-Q5_K_XL*"` |
| `llm-gemma-4-gguf-ud-q5-k-xl-2` | gemma-4-31B-it-GGUF · UD-Q5_K_XL (GGUF) | 21.9 GB | 5.5 | T1,T2,T3,T4 | any | `hf download unsloth/gemma-4-31B-it-GGUF --include "*UD-Q5_K_XL*"` |
| `llm-gemma-4-gguf-q6-k-6` | gemma-4-26B-A4B-it-GGUF · Q6_K (GGUF) | 22.6 GB | 6.5 | T1,T2,T3,T4 | any | `hf download lmstudio-community/gemma-4-26B-A4B-it-GGUF --include "*Q6_K*"` |
| `llm-gemma-4-gguf-ud-q6-k-xl-2` | gemma-4-26B-A4B-it-GGUF · UD-Q6_K_XL (GGUF) | 23.3 GB | 6.5 | T1,T2,T3,T4 | any | `hf download unsloth/gemma-4-26B-A4B-it-GGUF --include "*UD-Q6_K_XL*"` |
| `llm-gemma-4-gguf-bf16-3` | gemma-4-12b-it-GGUF · BF16 (GGUF) | 23.8 GB | 16 | T1,T2,T3,T4 | any | `hf download unsloth/gemma-4-12b-it-GGUF --include "*BF16*"` |
| `llm-gemma-4-gguf-q6-k-7` | gemma-4-31B-it-GGUF · Q6_K (GGUF) | 25.2 GB | 6.5 | T1,T2,T3,T4 | any | `hf download lmstudio-community/gemma-4-31B-it-GGUF --include "*Q6_K*"` |
| `llm-gemma-4-gguf-q6-k-8` | google_gemma-4-31B-it-GGUF · Q6_K (GGUF) | 26.7 GB | 6.5 | T1,T2,T3,T4 | any | `hf download bartowski/google_gemma-4-31B-it-GGUF --include "*Q6_K*"` |
| `llm-gemma-4-litert-lm-t-bb-2` | gemma-4-E2B-it-litert-lm · több .litertlm változat (LiteRT-LM) | 26.9 GB | 4.5 | T1,T2,T3,T4,T5 | android | `hf download litert-community/gemma-4-E2B-it-litert-lm` |
| `llm-gemma-4-gguf-q8-0-9` | gemma-4-26B-A4B-it-GGUF · Q8_0 (GGUF) | 26.9 GB | 8.5 | T1,T2,T3,T4 | any | `hf download unsloth/gemma-4-26B-A4B-it-GGUF --include "*Q8_0*"` |
| `llm-gemma-4-gguf-q8-0-10` | google_gemma-4-26B-A4B-it-GGUF · Q8_0 (GGUF) | 26.9 GB | 8.5 | T1,T2,T3,T4 | any | `hf download bartowski/google_gemma-4-26B-A4B-it-GGUF --include "*Q8_0*"` |
| `llm-gemma-4-gguf-q8-0-11` | gemma-4-26B-A4B-it-GGUF · Q8_0 (GGUF) | 26.9 GB | 8.5 | T1,T2,T3,T4 | any | `hf download lmstudio-community/gemma-4-26B-A4B-it-GGUF --include "*Q8_0*"` |
| `llm-gemma-4-gguf-ud-q6-k-xl-3` | gemma-4-31B-it-GGUF · UD-Q6_K_XL (GGUF) | 27.5 GB | 6.5 | T1,T2,T3,T4 | any | `hf download unsloth/gemma-4-31B-it-GGUF --include "*UD-Q6_K_XL*"` |
| `llm-gemma-4-ollama-ollama-16` |  · ollama gemma4:26b-a4b-it-q8_0 (ollama) | 28.1 GB | 8.5 | T1,T2,T3,T4 | any | `ollama pull gemma4:26b-a4b-it-q8_0` |
| `llm-gemma-4-fp8-fp8` | gemma-4-26B-A4B-it-FP8-dynamic · FP8 (FP8) | 28.7 GB | 8.5 | T1,T2,T3 | server | `hf download RedHatAI/gemma-4-26B-A4B-it-FP8-dynamic` |
| `llm-gemma-4-gguf-q8-0-12` | gemma-4-31B-it-GGUF · Q8_0 (GGUF) | 32.6 GB | 8.5 | T1,T2,T3,T4 | any | `hf download unsloth/gemma-4-31B-it-GGUF --include "*Q8_0*"` |
| `llm-gemma-4-gguf-q8-0-13` | google_gemma-4-31B-it-GGUF · Q8_0 (GGUF) | 32.6 GB | 8.5 | T1,T2,T3,T4 | any | `hf download bartowski/google_gemma-4-31B-it-GGUF --include "*Q8_0*"` |
| `llm-gemma-4-gguf-q8-0-14` | gemma-4-31B-it-GGUF · Q8_0 (GGUF) | 32.6 GB | 8.5 | T1,T2,T3,T4 | any | `hf download lmstudio-community/gemma-4-31B-it-GGUF --include "*Q8_0*"` |
| `llm-gemma-4-nvfp4-nvfp4-2` | Gemma-4-31B-IT-NVFP4 · NVFP4 (NVFP4) | 32.7 GB | 4.5 | T1,T2,T3 | server | `hf download nvidia/Gemma-4-31B-IT-NVFP4` |
| `llm-gemma-4-fp8-fp8-2` | gemma-4-31B-it-FP8-block · FP8 (FP8) | 33.3 GB | 8.5 | T1,T2,T3 | server | `hf download RedHatAI/gemma-4-31B-it-FP8-block` |
| `llm-gemma-4-ollama-ollama-17` |  · ollama gemma4:31b-it-q8_0 (ollama) | 33.8 GB | 8.5 | T1,T2,T3,T4 | any | `ollama pull gemma4:31b-it-q8_0` |
| `llm-gemma-4-gguf-bf16-4` | gemma-4-31B-it-GGUF · BF16 (GGUF) | 61.4 GB | 16 | T1,T2,T3,T4 | any | `hf download unsloth/gemma-4-31B-it-GGUF --include "*BF16*"` |
| `llm-gemma-4-ollama-ollama-18` |  · ollama gemma4:31b-it-bf16 (ollama) | 62.6 GB | 16 | T1,T2,T3 | any | `ollama pull gemma4:31b-it-bf16` |
</details>

<details><summary><b>Qwen3.5-4B / Qwen3.5-9B (+ MiMo-V2.6-Distill-Qwen-9B)</b> – 22 változat</summary>

| id | Fájl / repó | Méret | Bit | HW | Platform | Letöltés |
|---|---|---|---|---|---|---|
| `llm-qwen3-5-small-gguf-ud-iq2-m` | Qwen3.5-4B-GGUF · UD-IQ2_M (GGUF) | 1.8 GB | 2.6 | T1,T2,T3,T4,T5 | any | `hf download unsloth/Qwen3.5-4B-GGUF --include "*UD-IQ2_M*"` |
| `llm-qwen3-5-small-gguf-ud-q3-k-xl` | Qwen3.5-4B-GGUF · UD-Q3_K_XL (GGUF) | 2.4 GB | 3.5 | T1,T2,T3,T4,T5 | any | `hf download unsloth/Qwen3.5-4B-GGUF --include "*UD-Q3_K_XL*"` |
| `llm-qwen3-5-small-gguf-q4-k-m` | Qwen3.5-4B-GGUF · Q4_K_M (GGUF) | 2.7 GB | 4.5 | T1,T2,T3,T4,T5 | any | `hf download unsloth/Qwen3.5-4B-GGUF --include "*Q4_K_M*"` |
| `llm-qwen3-5-small-gguf-ud-q4-k-xl` | Qwen3.5-4B-GGUF · UD-Q4_K_XL (GGUF) | 2.9 GB | 4.5 | T1,T2,T3,T4,T5 | any | `hf download unsloth/Qwen3.5-4B-GGUF --include "*UD-Q4_K_XL*"` |
| `llm-qwen3-5-small-ollama-ollama` |  · ollama qwen3.5:4b (ollama) | 3.3 GB | 4.5 | T1,T2,T3,T4 | any | `ollama pull qwen3.5:4b` |
| `llm-qwen3-5-small-gguf-q6-k` | Qwen3.5-4B-GGUF · Q6_K (GGUF) | 3.5 GB | 6.5 | T1,T2,T3,T4,T5 | any | `hf download unsloth/Qwen3.5-4B-GGUF --include "*Q6_K*"` |
| `llm-qwen3-5-small-gguf-q8-0` | Qwen3.5-4B-GGUF · Q8_0 (GGUF) | 4.5 GB | 8.5 | T1,T2,T3,T4,T5 | any | `hf download unsloth/Qwen3.5-4B-GGUF --include "*Q8_0*"` |
| `llm-qwen3-5-small-gguf-iq3-m` | MiMo-V2.6-Distill-Qwen-9B-GGUF · IQ3_M (GGUF) | 4.8 GB | 3.5 | T1,T2,T3,T4,T5 | any | `hf download bartowski/MiMo-V2.6-Distill-Qwen-9B-GGUF --include "*IQ3_M*"` |
| `llm-qwen3-5-small-gguf-ud-q3-k-xl-2` | Qwen3.5-9B-GGUF · UD-Q3_K_XL (GGUF) | 5.0 GB | 3.5 | T1,T2,T3,T4,T5 | any | `hf download unsloth/Qwen3.5-9B-GGUF --include "*UD-Q3_K_XL*"` |
| `llm-qwen3-5-small-ollama-ollama-2` |  · ollama qwen3.5:4b-q8_0 (ollama) | 5.2 GB | 8.5 | T1,T2,T3,T4 | any | `ollama pull qwen3.5:4b-q8_0` |
| `llm-qwen3-5-small-gguf-q4-k-m-2` | Qwen3.5-9B-GGUF · Q4_K_M (GGUF) | 5.7 GB | 4.5 | T1,T2,T3,T4,T5 | any | `hf download unsloth/Qwen3.5-9B-GGUF --include "*Q4_K_M*"` |
| `llm-qwen3-5-small-gguf-q4-k-m-3` | MiMo-V2.6-Distill-Qwen-9B-GGUF · Q4_K_M (GGUF) | 5.8 GB | 4.5 | T1,T2,T3,T4,T5 | any | `hf download bartowski/MiMo-V2.6-Distill-Qwen-9B-GGUF --include "*Q4_K_M*"` |
| `llm-qwen3-5-small-gguf-ud-q4-k-xl-2` | Qwen3.5-9B-GGUF · UD-Q4_K_XL (GGUF) | 6.0 GB | 4.5 | T1,T2,T3,T4,T5 | any | `hf download unsloth/Qwen3.5-9B-GGUF --include "*UD-Q4_K_XL*"` |
| `llm-qwen3-5-small-ollama-ollama-3` |  · ollama qwen3.5:9b (ollama) | 6.5 GB | 4.5 | T1,T2,T3,T4 | any | `ollama pull qwen3.5:9b` |
| `llm-qwen3-5-small-ollama-ollama-4` |  · ollama mimo-v2.6:9b / :9b-q4_K_M (ollama) | 6.5 GB | 4.5 | T1,T2,T3,T4 | any | `ollama pull mimo-v2.6:9b / :9b-q4_K_M` |
| `llm-qwen3-5-small-gguf-q5-k-m` | MiMo-V2.6-Distill-Qwen-9B-GGUF · Q5_K_M (GGUF) | 6.9 GB | 5.5 | T1,T2,T3,T4,T5 | any | `hf download bartowski/MiMo-V2.6-Distill-Qwen-9B-GGUF --include "*Q5_K_M*"` |
| `llm-qwen3-5-small-gguf-q6-k-2` | Qwen3.5-9B-GGUF · Q6_K (GGUF) | 7.5 GB | 6.5 | T1,T2,T3,T4,T5 | any | `hf download unsloth/Qwen3.5-9B-GGUF --include "*Q6_K*"` |
| `llm-qwen3-5-small-gguf-q6-k-3` | MiMo-V2.6-Distill-Qwen-9B-GGUF · Q6_K (GGUF) | 7.8 GB | 6.5 | T1,T2,T3,T4,T5 | any | `hf download bartowski/MiMo-V2.6-Distill-Qwen-9B-GGUF --include "*Q6_K*"` |
| `llm-qwen3-5-small-gguf-q8-0-2` | Qwen3.5-9B-GGUF · Q8_0 (GGUF) | 9.5 GB | 8.5 | T1,T2,T3,T4,T5 | any | `hf download unsloth/Qwen3.5-9B-GGUF --include "*Q8_0*"` |
| `llm-qwen3-5-small-gguf-q8-0-3` | MiMo-V2.6-Distill-Qwen-9B-GGUF · Q8_0 (GGUF) | 9.6 GB | 8.5 | T1,T2,T3,T4,T5 | any | `hf download bartowski/MiMo-V2.6-Distill-Qwen-9B-GGUF --include "*Q8_0*"` |
| `llm-qwen3-5-small-ollama-ollama-5` |  · ollama qwen3.5:9b-q8_0 (ollama) | 10.4 GB | 8.5 | T1,T2,T3,T4 | any | `ollama pull qwen3.5:9b-q8_0` |
| `llm-qwen3-5-small-ollama-ollama-6` |  · ollama mimo-v2.6:9b-q8_0 (ollama) | 10.4 GB | 8.5 | T1,T2,T3,T4 | any | `ollama pull mimo-v2.6:9b-q8_0` |
</details>

<details><summary><b>DeepSeek-V4.1-Flash-1017 abliterated (huihui GGUF) / heretic (pqhaz) / abliterated (mrfakename)</b> – 5 változat</summary>

| id | Fájl / repó | Méret | Bit | HW | Platform | Letöltés |
|---|---|---|---|---|---|---|
| `llm-deepseek-v4-1-flash-1017-abliterated-hui-gguf-ud-iq1-s` | Huihui-DeepSeek-V4.1-Flash-1017-abliterated-GGUF · UD-IQ1_S (GGUF) | 233.0 GB | 1.7 | T1,T2 | any | `hf download huihui-ai/Huihui-DeepSeek-V4.1-Flash-1017-abliterated-GGUF --include "*UD-IQ1_S*"` |
| `llm-deepseek-v4-1-flash-1017-abliterated-hui-gguf-ud-iq1-m` | Huihui-DeepSeek-V4.1-Flash-1017-abliterated-GGUF · UD-IQ1_M (GGUF) | 250.4 GB | 1.7 | T1,T2 | any | `hf download huihui-ai/Huihui-DeepSeek-V4.1-Flash-1017-abliterated-GGUF --include "*UD-IQ1_M*"` |
| `llm-deepseek-v4-1-flash-1017-abliterated-hui-mlx-n-a` | DeepSeek-V4.1-Flash-1017-Abliterated-MLX · n/a (heretic alapú) (MLX) | 422.6 GB | 4.5 | T1,T2 | mac | `hf download apetersson/DeepSeek-V4.1-Flash-1017-Abliterated-MLX` |
| `llm-deepseek-v4-1-flash-1017-abliterated-hui-gguf-q8-0` | DeepSeek-V4.1-Flash-1017-heretic-GGUF · Q8_0 (GGUF) | 507.9 GB | 8.5 | T1 | any | `hf download pqhaz/DeepSeek-V4.1-Flash-1017-heretic-GGUF --include "*Q8_0*"` |
| `llm-deepseek-v4-1-flash-1017-abliterated-hui-safetensors-fp8-original` | DeepSeek-V4.1-Flash-1017-abliterated · original FP8 (safetensors FP8) | 510.3 GB | 8.5 | T1 | server | `hf download mrfakename/DeepSeek-V4.1-Flash-1017-abliterated` |
</details>

<details><summary><b>GLM-5.3 abliterated (huihui GGUF)</b> – 1 változat</summary>

| id | Fájl / repó | Méret | Bit | HW | Platform | Letöltés |
|---|---|---|---|---|---|---|
| `llm-glm-5-3-abliterated-huihui-gguf-gguf-ud-iq1-s` | Huihui-GLM-5.3-abliterated-GGUF · UD-IQ1_S (GGUF) | 216.7 GB | 1.7 | T1,T2 | any | `hf download huihui-ai/Huihui-GLM-5.3-abliterated-GGUF --include "*UD-IQ1_S*"` |
</details>

<details><summary><b>MiniMax-M3.1-Flash abliterated (orcarouter GGUF)</b> – 1 változat</summary>

| id | Fájl / repó | Méret | Bit | HW | Platform | Letöltés |
|---|---|---|---|---|---|---|
| `llm-minimax-m3-1-flash-abliterated-orcaroute-gguf-mix-128g` | MiniMax-M3.1-Flash-abliterated-GGUF · Mix-128G (GGUF) | 111.9 GB | 4.5 | T1,T2,T3 | any | `hf download orcarouter/MiniMax-M3.1-Flash-abliterated-GGUF --include "*Mix-128G*"` |
</details>

<details><summary><b>Qwen3.8-Flash-Next abliterated v2 (huihui GGUF)</b> – 9 változat</summary>

| id | Fájl / repó | Méret | Bit | HW | Platform | Letöltés |
|---|---|---|---|---|---|---|
| `llm-qwen3-8-flash-next-abliterated-v2-huihui-gguf-swift` | Huihui-Qwen3.8-Flash-Next-abliterated-v2-GGUF · Swift GSQ-RCO IQ2_XS (GGUF) | 68.2 GB | 2.6 | T1,T2,T3 | any | `hf download huihui-ai/Huihui-Qwen3.8-Flash-Next-abliterated-v2-GGUF --include "*Swift*"` |
| `llm-qwen3-8-flash-next-abliterated-v2-huihui-gguf-swift-2` | Huihui-Qwen3.8-Flash-Next-abliterated-v2-GGUF · Swift IQ3_XXS (GGUF) | 76.0 GB | 3.5 | T1,T2,T3 | any | `hf download huihui-ai/Huihui-Qwen3.8-Flash-Next-abliterated-v2-GGUF --include "*Swift*"` |
| `llm-qwen3-8-flash-next-abliterated-v2-huihui-gguf-swift-3` | Huihui-Qwen3.8-Flash-Next-abliterated-v2-GGUF · Swift IQ3_S (GGUF) | 83.7 GB | 3.5 | T1,T2,T3 | any | `hf download huihui-ai/Huihui-Qwen3.8-Flash-Next-abliterated-v2-GGUF --include "*Swift*"` |
| `llm-qwen3-8-flash-next-abliterated-v2-huihui-gguf-unsloth-ud-iq4-xs` | Huihui-Qwen3.8-Flash-Next-abliterated-v2-GGUF · unsloth-UD-IQ4_XS (GGUF) | 93.7 GB | 4.5 | T1,T2,T3 | any | `hf download huihui-ai/Huihui-Qwen3.8-Flash-Next-abliterated-v2-GGUF --include "*unsloth-UD-IQ4_XS*"` |
| `llm-qwen3-8-flash-next-abliterated-v2-huihui-gguf-unsloth-ud-q4-k-xl` | Huihui-Qwen3.8-Flash-Next-abliterated-v2-GGUF · unsloth-UD-Q4_K_XL (GGUF) | 111.3 GB | 4.5 | T1,T2,T3 | any | `hf download huihui-ai/Huihui-Qwen3.8-Flash-Next-abliterated-v2-GGUF --include "*unsloth-UD-Q4_K_XL*"` |
| `llm-qwen3-8-flash-next-abliterated-v2-huihui-mlx-oq5e-mtp` | Qwen3.8-Flash-Next-Uncensored-oQ5e-mtp · oQ5e-mtp (MLX) | 128.6 GB | 5.5 | T1,T2 | mac | `hf download mlx-community/Qwen3.8-Flash-Next-Uncensored-oQ5e-mtp` |
| `llm-qwen3-8-flash-next-abliterated-v2-huihui-gguf-ud-q5-k-xl` | Huihui-Qwen3.8-Flash-Next-abliterated-v2-GGUF · UD-Q5_K_XL (GGUF) | 158.3 GB | 5.5 | T1,T2 | any | `hf download huihui-ai/Huihui-Qwen3.8-Flash-Next-abliterated-v2-GGUF --include "*UD-Q5_K_XL*"` |
| `llm-qwen3-8-flash-next-abliterated-v2-huihui-gguf-ud-q6-k-xl` | Huihui-Qwen3.8-Flash-Next-abliterated-v2-GGUF · UD-Q6_K_XL (GGUF) | 169.2 GB | 6.5 | T1,T2 | any | `hf download huihui-ai/Huihui-Qwen3.8-Flash-Next-abliterated-v2-GGUF --include "*UD-Q6_K_XL*"` |
| `llm-qwen3-8-flash-next-abliterated-v2-huihui-gguf-q8-0` | Huihui-Qwen3.8-Flash-Next-abliterated-v2-GGUF · Q8_0 (GGUF) | 188.2 GB | 8.5 | T1,T2 | any | `hf download huihui-ai/Huihui-Qwen3.8-Flash-Next-abliterated-v2-GGUF --include "*Q8_0*"` |
</details>

<details><summary><b>GLM-5.3-Flash abliterated (huihui GGUF)</b> – 10 változat</summary>

| id | Fájl / repó | Méret | Bit | HW | Platform | Letöltés |
|---|---|---|---|---|---|---|
| `llm-glm-5-3-flash-abliterated-huihui-gguf-gguf-ud-iq1-s` | Huihui-GLM-5.3-Flash-abliterated-GGUF · UD-IQ1_S (GGUF) | 93.1 GB | 1.7 | T1,T2,T3 | any | `hf download huihui-ai/Huihui-GLM-5.3-Flash-abliterated-GGUF --include "*UD-IQ1_S*"` |
| `llm-glm-5-3-flash-abliterated-huihui-gguf-gguf-ud-iq2-xxs` | Huihui-GLM-5.3-Flash-abliterated-GGUF · UD-IQ2_XXS (GGUF) | 101.8 GB | 2.6 | T1,T2,T3 | any | `hf download huihui-ai/Huihui-GLM-5.3-Flash-abliterated-GGUF --include "*UD-IQ2_XXS*"` |
| `llm-glm-5-3-flash-abliterated-huihui-gguf-gguf-ud-q2-k-xl` | Huihui-GLM-5.3-Flash-abliterated-GGUF · UD-Q2_K_XL (GGUF) | 108.7 GB | 2.6 | T1,T2,T3 | any | `hf download huihui-ai/Huihui-GLM-5.3-Flash-abliterated-GGUF --include "*UD-Q2_K_XL*"` |
| `llm-glm-5-3-flash-abliterated-huihui-gguf-gguf-ud-iq3-xxs` | Huihui-GLM-5.3-Flash-abliterated-GGUF · UD-IQ3_XXS (GGUF) | 120.4 GB | 3.5 | T1,T2,T3 | any | `hf download huihui-ai/Huihui-GLM-5.3-Flash-abliterated-GGUF --include "*UD-IQ3_XXS*"` |
| `llm-glm-5-3-flash-abliterated-huihui-gguf-gguf-ud-q3-k-xl` | Huihui-GLM-5.3-Flash-abliterated-GGUF · UD-Q3_K_XL (GGUF) | 147.5 GB | 3.5 | T1,T2 | any | `hf download huihui-ai/Huihui-GLM-5.3-Flash-abliterated-GGUF --include "*UD-Q3_K_XL*"` |
| `llm-glm-5-3-flash-abliterated-huihui-gguf-gguf-ud-iq4-xs` | Huihui-GLM-5.3-Flash-abliterated-GGUF · UD-IQ4_XS (GGUF) | 156.8 GB | 4.5 | T1,T2 | any | `hf download huihui-ai/Huihui-GLM-5.3-Flash-abliterated-GGUF --include "*UD-IQ4_XS*"` |
| `llm-glm-5-3-flash-abliterated-huihui-gguf-mlx-4bit` | GLM-5.3-Flash-Abliterated-MLX-4bit · 4bit (MLX) | 185.9 GB | 4.5 | T1,T2 | mac | `hf download grant-ai/GLM-5.3-Flash-Abliterated-MLX-4bit` |
| `llm-glm-5-3-flash-abliterated-huihui-gguf-gguf-ud-q4-k-xl` | Huihui-GLM-5.3-Flash-abliterated-GGUF · UD-Q4_K_XL (GGUF) | 199.7 GB | 4.5 | T1,T2 | any | `hf download huihui-ai/Huihui-GLM-5.3-Flash-abliterated-GGUF --include "*UD-Q4_K_XL*"` |
| `llm-glm-5-3-flash-abliterated-huihui-gguf-gguf-ud-q5-k-xl` | Huihui-GLM-5.3-Flash-abliterated-GGUF · UD-Q5_K_XL (GGUF) | 240.3 GB | 5.5 | T1,T2 | any | `hf download huihui-ai/Huihui-GLM-5.3-Flash-abliterated-GGUF --include "*UD-Q5_K_XL*"` |
| `llm-glm-5-3-flash-abliterated-huihui-gguf-gguf-ud-q6-k-xl` | Huihui-GLM-5.3-Flash-abliterated-GGUF · UD-Q6_K_XL (GGUF) | 291.8 GB | 6.5 | T1,T2 | any | `hf download huihui-ai/Huihui-GLM-5.3-Flash-abliterated-GGUF --include "*UD-Q6_K_XL*"` |
</details>

<details><summary><b>Qwen3.8-27B abliterated (huihui) / heretic-ara (trohrbaugh)</b> – 6 változat</summary>

| id | Fájl / repó | Méret | Bit | HW | Platform | Letöltés |
|---|---|---|---|---|---|---|
| `llm-qwen3-8-27b-abliterated-huihui-heretic-a-gguf-q2-k` | Huihui-Qwen3.8-27B-abliterated-GGUF · Q2_K (GGUF) | 10.9 GB | 2.6 | T1,T2,T3,T4 | any | `hf download huihui-ai/Huihui-Qwen3.8-27B-abliterated-GGUF --include "*Q2_K*"` |
| `llm-qwen3-8-27b-abliterated-huihui-heretic-a-gguf-ud-iq4-xs` | Huihui-Qwen3.8-27B-abliterated-GGUF · UD-IQ4_XS (GGUF) | 14.4 GB | 4.5 | T1,T2,T3,T4 | any | `hf download huihui-ai/Huihui-Qwen3.8-27B-abliterated-GGUF --include "*UD-IQ4_XS*"` |
| `llm-qwen3-8-27b-abliterated-huihui-heretic-a-gguf-ud-dw-q4-k-m` | Huihui-Qwen3.8-27B-abliterated-GGUF · UD-DW-Q4_K_M (GGUF) | 16.6 GB | 4.5 | T1,T2,T3 | any | `hf download huihui-ai/Huihui-Qwen3.8-27B-abliterated-GGUF --include "*UD-DW-Q4_K_M*"` |
| `llm-qwen3-8-27b-abliterated-huihui-heretic-a-mlx-optiq-4bit` | Qwen3.8-27B-Uncensored-OptiQ-4bit · OptiQ-4bit (MLX) | 19.8 GB | 4.5 | T1,T2,T3,T4 | mac | `hf download mlx-community/Qwen3.8-27B-Uncensored-OptiQ-4bit` |
| `llm-qwen3-8-27b-abliterated-huihui-heretic-a-gguf-q6-k` | Huihui-Qwen3.8-27B-abliterated-GGUF · Q6_K (GGUF) | 22.4 GB | 6.5 | T1,T2,T3 | any | `hf download huihui-ai/Huihui-Qwen3.8-27B-abliterated-GGUF --include "*Q6_K*"` |
| `llm-qwen3-8-27b-abliterated-huihui-heretic-a-gguf-q8-0` | Huihui-Qwen3.8-27B-abliterated-GGUF · Q8_0 (GGUF) | 29.1 GB | 8.5 | T1,T2,T3 | any | `hf download huihui-ai/Huihui-Qwen3.8-27B-abliterated-GGUF --include "*Q8_0*"` |
</details>

<details><summary><b>NousResearch Arete-27B (a "R1-1776 utód")</b> – 2 változat</summary>

| id | Fájl / repó | Méret | Bit | HW | Platform | Letöltés |
|---|---|---|---|---|---|---|
| `llm-nousresearch-arete-27b-a-r1-1776-ut-d-gguf-iq4-xs` | NousResearch_Arete-27B-GGUF · IQ4_XS (GGUF) | 15.2 GB | 4.5 | T1,T2,T3,T4 | any | `hf download bartowski/NousResearch_Arete-27B-GGUF --include "*IQ4_XS*"` |
| `llm-nousresearch-arete-27b-a-r1-1776-ut-d-gguf-q4-k-m` | NousResearch_Arete-27B-GGUF · Q4_K_M (GGUF) | 17.2 GB | 4.5 | T1,T2,T3 | any | `hf download bartowski/NousResearch_Arete-27B-GGUF --include "*Q4_K_M*"` |
</details>

<details><summary><b>Kimi-K3 Abliterated V1 (Uniboshi)</b> – 1 változat</summary>

| id | Fájl / repó | Méret | Bit | HW | Platform | Letöltés |
|---|---|---|---|---|---|---|
| `llm-kimi-k3-abliterated-v1-uniboshi-gguf-mxfp4-moe` | Kimi-K3-Abliterated-V1-GGUF · MXFP4_MOE (GGUF) | 1.51 TB | 4.5 | T1 | any | `hf download Uniboshi/Kimi-K3-Abliterated-V1-GGUF --include "*MXFP4_MOE*"` |
</details>

<details><summary><b>Mistral-Small-4-119B-2603 heretic (darkc0de, GGUF: Rioky)</b> – 6 változat</summary>

| id | Fájl / repó | Méret | Bit | HW | Platform | Letöltés |
|---|---|---|---|---|---|---|
| `llm-mistral-small-4-119b-2603-heretic-darkc0-gguf-q2-k` | Mistral-Small-4-119B-2603-heretic-gguf · Q2_K (GGUF) | 43.4 GB | 2.6 | T1,T2,T3 | any | `hf download Rioky/Mistral-Small-4-119B-2603-heretic-gguf --include "*Q2_K*"` |
| `llm-mistral-small-4-119b-2603-heretic-darkc0-gguf-q3-k-m` | Mistral-Small-4-119B-2603-heretic-gguf · Q3_K_M (GGUF) | 56.9 GB | 3.5 | T1,T2,T3 | any | `hf download Rioky/Mistral-Small-4-119B-2603-heretic-gguf --include "*Q3_K_M*"` |
| `llm-mistral-small-4-119b-2603-heretic-darkc0-gguf-q4-k-s` | Mistral-Small-4-119B-2603-heretic-gguf · Q4_K_S (GGUF) | 67.7 GB | 4.5 | T1,T2,T3 | any | `hf download Rioky/Mistral-Small-4-119B-2603-heretic-gguf --include "*Q4_K_S*"` |
| `llm-mistral-small-4-119b-2603-heretic-darkc0-gguf-q4-k-m` | Mistral-Small-4-119B-2603-heretic-gguf · Q4_K_M (GGUF) | 72.2 GB | 4.5 | T1,T2,T3 | any | `hf download Rioky/Mistral-Small-4-119B-2603-heretic-gguf --include "*Q4_K_M*"` |
| `llm-mistral-small-4-119b-2603-heretic-darkc0-gguf-q5-k-m` | Mistral-Small-4-119B-2603-heretic-gguf · Q5_K_M (GGUF) | 84.5 GB | 5.5 | T1,T2 | any | `hf download Rioky/Mistral-Small-4-119B-2603-heretic-gguf --include "*Q5_K_M*"` |
| `llm-mistral-small-4-119b-2603-heretic-darkc0-gguf-q8-0` | Mistral-Small-4-119B-2603-heretic-gguf · Q8_0 (GGUF) | 126.5 GB | 8.5 | T1,T2 | any | `hf download Rioky/Mistral-Small-4-119B-2603-heretic-gguf --include "*Q8_0*"` |
</details>

<details><summary><b>Qwen3.6-35B-A3B uncensored-heretic (llmfan46) / abliterated-MTP (huihui)</b> – 2 változat</summary>

| id | Fájl / repó | Méret | Bit | HW | Platform | Letöltés |
|---|---|---|---|---|---|---|
| `llm-qwen3-6-35b-a3b-uncensored-heretic-llmfa-gguf-q3-k-m` | Qwen3.6-35B-A3B-uncensored-heretic-GGUF · Q3_K_M (GGUF) | 16.9 GB | 3.5 | T1,T2,T3,T4 | any | `hf download llmfan46/Qwen3.6-35B-A3B-uncensored-heretic-GGUF --include "*Q3_K_M*"` |
| `llm-qwen3-6-35b-a3b-uncensored-heretic-llmfa-gguf-q4-k-m` | Qwen3.6-35B-A3B-uncensored-heretic-GGUF · Q4_K_M (GGUF) | 21.2 GB | 4.5 | T1,T2,T3,T4 | any | `hf download llmfan46/Qwen3.6-35B-A3B-uncensored-heretic-GGUF --include "*Q4_K_M*"` |
</details>

<details><summary><b>gemma-4-31B-it heretic (coder3101) / uncensored-heretic (llmfan46)</b> – 4 változat</summary>

| id | Fájl / repó | Méret | Bit | HW | Platform | Letöltés |
|---|---|---|---|---|---|---|
| `llm-gemma-4-31b-it-heretic-coder3101-uncenso-gguf-iq4-xs` | gemma-4-31B-it-heretic-GGUF · IQ4_XS (GGUF) | 16.9 GB | 4.5 | T1,T2,T3,T4 | any | `hf download mradermacher/gemma-4-31B-it-heretic-GGUF --include "*IQ4_XS*"` |
| `llm-gemma-4-31b-it-heretic-coder3101-uncenso-mlx-4bit` | gemma-4-31B-it-uncensored-heretic-4bit · 4bit (MLX) | 17.3 GB | 4.5 | T1,T2,T3,T4 | mac | `hf download mlx-community/gemma-4-31B-it-uncensored-heretic-4bit` |
| `llm-gemma-4-31b-it-heretic-coder3101-uncenso-gguf-q4-k-m` | gemma-4-31B-it-heretic-GGUF · Q4_K_M (GGUF) | 18.7 GB | 4.5 | T1,T2,T3 | any | `hf download mradermacher/gemma-4-31B-it-heretic-GGUF --include "*Q4_K_M*"` |
| `llm-gemma-4-31b-it-heretic-coder3101-uncenso-gguf-q6-k` | gemma-4-31B-it-heretic-GGUF · Q6_K (GGUF) | 25.2 GB | 6.5 | T1,T2,T3 | any | `hf download mradermacher/gemma-4-31B-it-heretic-GGUF --include "*Q6_K*"` |
</details>

<details><summary><b>gpt-oss-120b heretic (MuXodious tainted-heresy / kldzj heretic)</b> – 3 változat</summary>

| id | Fájl / repó | Méret | Bit | HW | Platform | Letöltés |
|---|---|---|---|---|---|---|
| `llm-gpt-oss-120b-heretic-muxodious-tainted-h-mlx-mxfp4` | gpt-oss-120b-tainted-heresy-mlx-MXFP4 · MXFP4 (MLX) | 62.2 GB | 4.5 | T1,T2,T3,T4 | mac | `hf download MuXodious/gpt-oss-120b-tainted-heresy-mlx-MXFP4` |
| `llm-gpt-oss-120b-heretic-muxodious-tainted-h-gguf-mxfp4-moe` | gpt-oss-120b-tainted-heresy-GGUF · MXFP4_MoE (GGUF) | 63.4 GB | 4.5 | T1,T2,T3 | any | `hf download MuXodious/gpt-oss-120b-tainted-heresy-GGUF --include "*MXFP4_MoE*"` |
| `llm-gpt-oss-120b-heretic-muxodious-tainted-h-gguf-mxfp4-moe-2` | kldzj_gpt-oss-120b-heretic-GGUF · MXFP4_MOE (GGUF) | 63.4 GB | 4.5 | T1,T2,T3 | any | `hf download bartowski/kldzj_gpt-oss-120b-heretic-GGUF --include "*MXFP4_MOE*"` |
</details>

<details><summary><b>gemma-4-26B-A4B-it ultra-uncensored-heretic (llmfan46)</b> – 2 változat</summary>

| id | Fájl / repó | Méret | Bit | HW | Platform | Letöltés |
|---|---|---|---|---|---|---|
| `llm-gemma-4-26b-a4b-it-ultra-uncensored-here-gguf-q3-k-m` | gemma-4-26B-A4B-it-ultra-uncensored-heretic-GGUF · Q3_K_M (GGUF) | 13.3 GB | 3.5 | T1,T2,T3,T4 | any | `hf download llmfan46/gemma-4-26B-A4B-it-ultra-uncensored-heretic-GGUF --include "*Q3_K_M*"` |
| `llm-gemma-4-26b-a4b-it-ultra-uncensored-here-gguf-q4-k-m` | gemma-4-26B-A4B-it-ultra-uncensored-heretic-GGUF · Q4_K_M (GGUF) | 16.8 GB | 4.5 | T1,T2,T3,T4 | any | `hf download llmfan46/gemma-4-26B-A4B-it-ultra-uncensored-heretic-GGUF --include "*Q4_K_M*"` |
</details>

<details><summary><b>gemma-4-12B-it uncensored-heretic (llmfan46) / abliterated QAT (huihui)</b> – 1 változat</summary>

| id | Fájl / repó | Méret | Bit | HW | Platform | Letöltés |
|---|---|---|---|---|---|---|
| `llm-gemma-4-12b-it-uncensored-heretic-llmfan-gguf-q4-k-m` | gemma-4-12B-it-uncensored-heretic-GGUF · Q4_K_M (GGUF) | 8.5 GB | 4.5 | T1,T2,T3,T4 | any | `hf download llmfan46/gemma-4-12B-it-uncensored-heretic-GGUF --include "*Q4_K_M*"` |
</details>

<details><summary><b>Qwen3.5-9B heretic-v2 (trohrbaugh)</b> – 2 változat</summary>

| id | Fájl / repó | Méret | Bit | HW | Platform | Letöltés |
|---|---|---|---|---|---|---|
| `llm-qwen3-5-9b-heretic-v2-trohrbaugh-gguf-q4-k-m` | Qwen3.5-9B-heretic-v2-GGUF · Q4_K_M (GGUF) | 5.6 GB | 4.5 | T1,T2,T3,T4,T5 | any | `hf download filvyb/Qwen3.5-9B-heretic-v2-GGUF --include "*Q4_K_M*"` |
| `llm-qwen3-5-9b-heretic-v2-trohrbaugh-gguf-q8-0` | Qwen3.5-9B-heretic-v2-GGUF · Q8_0 (GGUF) | 9.5 GB | 8.5 | T1,T2,T3,T4 | any | `hf download filvyb/Qwen3.5-9B-heretic-v2-GGUF --include "*Q8_0*"` |
</details>

<details><summary><b>gpt-oss-20b heretic (MuXodious RichardErkhov-heresy / p-e-w heretic)</b> – 1 változat</summary>

| id | Fájl / repó | Méret | Bit | HW | Platform | Letöltés |
|---|---|---|---|---|---|---|
| `llm-gpt-oss-20b-heretic-muxodious-richarderk-gguf-mxfp4-moe` | gpt-oss-20b-RichardErkhov-heresy-GGUF · MXFP4_MoE (GGUF) | 12.7 GB | 4.5 | T1,T2,T3,T4 | any | `hf download MuXodious/gpt-oss-20b-RichardErkhov-heresy-GGUF --include "*MXFP4_MoE*"` |
</details>

<details><summary><b>gemma-4-E4B-it heretic (coder3101; GGUF Abiray) / ultra-uncensored (llmfan46)</b> – 1 változat</summary>

| id | Fájl / repó | Méret | Bit | HW | Platform | Letöltés |
|---|---|---|---|---|---|---|
| `llm-gemma-4-e4b-it-heretic-coder3101-gguf-ab-gguf-q4-k-m` | gemma-4-E4B-it-heretic-GGUF · Q4_K_M (GGUF) | 5.3 GB | 4.5 | T1,T2,T3,T4,T5 | any | `hf download Abiray/gemma-4-E4B-it-heretic-GGUF --include "*Q4_K_M*"` |
</details>

<details><summary><b>Qwen3.5-4B heretic-2.0 (p-e-w) / SOMPOA-heresy-v2 (MuXodious)</b> – 4 változat</summary>

| id | Fájl / repó | Méret | Bit | HW | Platform | Letöltés |
|---|---|---|---|---|---|---|
| `llm-qwen3-5-4b-heretic-2-0-p-e-w-sompoa-here-gguf-iq4-xs` | Qwen3.5-4B-heretic-2.0-GGUF · IQ4_XS (GGUF) | 2.5 GB | 4.5 | T1,T2,T3,T4,T5 | any | `hf download mradermacher/Qwen3.5-4B-heretic-2.0-GGUF --include "*IQ4_XS*"` |
| `llm-qwen3-5-4b-heretic-2-0-p-e-w-sompoa-here-gguf-q4-k-m` | Qwen3.5-4B-heretic-2.0-GGUF · Q4_K_M (GGUF) | 2.7 GB | 4.5 | T1,T2,T3,T4,T5 | any | `hf download mradermacher/Qwen3.5-4B-heretic-2.0-GGUF --include "*Q4_K_M*"` |
| `llm-qwen3-5-4b-heretic-2-0-p-e-w-sompoa-here-gguf-q6-k` | Qwen3.5-4B-heretic-2.0-GGUF · Q6_K (GGUF) | 3.5 GB | 6.5 | T1,T2,T3,T4,T5 | any | `hf download mradermacher/Qwen3.5-4B-heretic-2.0-GGUF --include "*Q6_K*"` |
| `llm-qwen3-5-4b-heretic-2-0-p-e-w-sompoa-here-gguf-q8-0` | Qwen3.5-4B-heretic-2.0-GGUF · Q8_0 (GGUF) | 4.5 GB | 8.5 | T1,T2,T3,T4,T5 | any | `hf download mradermacher/Qwen3.5-4B-heretic-2.0-GGUF --include "*Q8_0*"` |
</details>

<details><summary><b>gemma-4-E2B-it ultra-uncensored-heretic (llmfan46)</b> – 2 változat</summary>

| id | Fájl / repó | Méret | Bit | HW | Platform | Letöltés |
|---|---|---|---|---|---|---|
| `llm-gemma-4-e2b-it-ultra-uncensored-heretic--gguf-q4-k-m` | gemma-4-E2B-it-ultra-uncensored-heretic-GGUF · Q4_K_M (GGUF) | 3.4 GB | 4.5 | T1,T2,T3,T4,T5 | any | `hf download llmfan46/gemma-4-E2B-it-ultra-uncensored-heretic-GGUF --include "*Q4_K_M*"` |
| `llm-gemma-4-e2b-it-ultra-uncensored-heretic--gguf-q5-k-m` | gemma-4-E2B-it-ultra-uncensored-heretic-GGUF · Q5_K_M (GGUF) | 3.6 GB | 5.5 | T1,T2,T3,T4,T5 | any | `hf download llmfan46/gemma-4-E2B-it-ultra-uncensored-heretic-GGUF --include "*Q5_K_M*"` |
</details>


### 6.5 Cenzúrázatlan („uncensored”) változatok: mi ez és mennyit veszít

- **Abliteration:** a modell aktivációiból kiszámolt „elutasítási irányt” kivetítik a súlyokból. Gyors, nem kell hozzá tanítás. Fő gyártók: huihui-ai, mrfakename.
- **Heretic** (`p-e-w/heretic`, PyPI `heretic-llm`): automatikusan hangolt abliteration (ARA). Úgy minimalizálja az elutasítást, hogy közben az eredeti viselkedéstől való eltérés (KL) kicsi maradjon. **Offline is futtatható bármely modellen**, így egy új alapmodellből magad is készíthetsz cenzúrázatlant. Az ehhez kellő adathalmazok (`mlabonne/harmful_behaviors`, `mlabonne/harmless_alpaca`) kicsik, töltsd le őket előre.
- **Intelligenciaveszteség** (UGI NatInt mérések): nagy modellen (gemma-4-26B/31B, gpt-oss-120b, Qwen3.6-35B) ~0–2 pont, kicsin (9B–20B) akár 5–11 pont. Kis gépre ezért legyen meg az eredeti modell is.
- **Ajánlott párosítás:** egy alapmodell + egy cenzúrázatlan változat ugyanabból a családból. A szkript alapból ezt választja (`--uncensored also`). Csak cenzúrázatlan: `only`. Kihagyás: `no`.
- **A cenzúrázatlan modell nem megbízhatóbb.** Kevesebbet utasít el, de ugyanúgy hallucinál. Életveszélyes témában (gyógyszer, vegyi anyag, robbanóanyag, statika) a forrásdokumentum dönt.

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

### 6.9 Kihagyott (régi vagy gyenge) modellek

- **Felváltott generációk:** Kimi-K3 és K2.x, DeepSeek-V4-Pro-0813 és V3.x, GLM-5.2 és korábbiak, MiniMax-M3 és M2.x, Qwen3.6/3.5 nagy modellek, Step-3.7, MiMo-V2.5, Ling-3.0, Hy3, Llama 4.
- **Gyenge az AA v5-ön:** gpt-oss-120b/20b (3,8), Nemotron-3-Ultra, Command A+, Granite 4.2, Phi-4. Az ERNIE-5.5-ből csak base modell van.
- **Archívumcélra maradt bent:** a gpt-oss heretic-változata, mert kicsi, Apache-licencű és gyors.
