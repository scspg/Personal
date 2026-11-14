### 6.11 GeForce AI-korlátozások és feloldásuk (RTX 30 → 60)

> **Kutatás:** 2026-11-14.
> - **Források:** a repókat `git ls-remote` paranccsal ellenőriztem, a whitepaper-számokat az NVIDIA PDF-ekből vettem.
> - **Jelölések:** **[B]** = becslés, **[NE]** = nem ellenőrzött vagy pletyka.
> - **Kalkulátor:** a feloldott profilok neve „… FELOLDVA”.

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

#### Korlátozások generációnként

| Korlát | RTX 30 | RTX 40 | RTX 50 | RTX 60 (várható) | Feloldható? | Eszköz | Hatás LLM-re |
|---|---|---|---|---|---|---|---|
| FP16/BF16 tensor FP32-akkumulálással **felezve** | igen | igen | igen (az FP4 nem felezett) | valószínű [B] | 30: igen (stabil) · 40: kísérleti · 50: **nem** | Zagitta/gpu-unlock, JustAResearcher/gpu-unlock-ada | prefill, finomhangolás; decode: 0 |
| FP8 FP32-akkumulálással felezve | – | igen | igen | valószínű [B] | 40: kísérleti | gpu-unlock-ada | FP8 prefill |
| FP64 = 1/64 | igen | igen | igen | valószínű | **nem** (a profi lapkán is 1/64) | – | nincs |
| PCIe **P2P tiltva** | igen (3090-en NVLink van) | igen | igen | valószínű | **igen** (Linux, open kernel modul) | tinygrad / aikitoria open-gpu-kernel-modules | multi-GPU TP: 2 kártyánál ~+3%, 8 kártyánál több |
| NVLink | csak 3090/3090 Ti | nincs | nincs | ? | hardveres hiány | – | – |
| vGPU / SR-IOV / MIG | nincs | nincs | nincs („hardware-blocked”) | valószínű | 30/40/50: nem | DualCoder/vgpu_unlock (csak Maxwell–Turing) | otthon nem számít |
| NVENC session-limit | igen | igen | igen | valószínű | igen | keylase/nvidia-patch | LLM-re nincs hatás |
| LHR (kriptobányászati limit) | igen | – | – | – | igen (2022-05) | NBMiner, NiceHash QuickMiner | LLM-re nincs hatás |
| ECC | nincs | 4090: kapcsolható | GDDR7 on-die ECC, mindig be van kapcsolva | hasonló [B] | – | – | ECC ki (4090): ~+1,6% |
| Power limit / VBIOS-zár | aláírt VBIOS | aláírt VBIOS | aláírt VBIOS, de XOC BIOS-ok kiszivárogtak | valószínű | részben (kockázatos) | nvflash + XOC BIOS | prefill +0–5%, decode ≈0 [B] |
| Illesztőprogram-licenc (EULA): adatközponti használat tiltva | igen | igen | igen | valószínű | jogi korlát | – | otthoni használatot nem érint |
| **VRAM-kapacitás** | 24 GB | 24 GB | 32 GB | 32 GB [NE] | szoftveresen nem | – | **ez a valódi korlát** |

**Whitepaper-számok** (dense/sparse TFLOPS; a GeForce felezett értékek **félkövérrel**):
- RTX 3090: FP16-acc 142/285, **FP32-acc 71/142**.
- RTX A6000 (profi kártya): FP32-acc 155/310, teljes sebesség.
- RTX 4090: FP16-acc 330/661, **FP32-acc 165/330**.
- RTX 5090: FP16-acc 419/838, **FP32-acc 210/419**, FP4 1676/3352 (nem felezett).

Források: [GA102](https://www.nvidia.com/content/PDF/nvidia-ampere-ga-102-gpu-architecture-whitepaper-v2.pdf), [Ada](https://images.nvidia.com/aem-dam/Solutions/geforce/ada/nvidia-ada-gpu-architecture.pdf), [Blackwell](https://images.nvidia.com/aem-dam/Solutions/geforce/blackwell/nvidia-rtx-blackwell-gpu-architecture.pdf) whitepaper.

#### Feloldási idővonal: mikor törték fel a korábbi generációkat

| Mit | Generáció | Dátum | Ki | Késés a korlát után | Link |
|---|---|---|---|---|---|
| NVENC session-limit patch | Maxwell+ | 2016-07-15 | keylase | – | [repó](https://github.com/keylase/nvidia-patch) |
| vGPU unlock | Maxwell–Turing | 2021-01-28 (git), 2021-04 (bejelentés) | DualCoder | Turing után ~2,3 év | [repó](https://github.com/DualCoder/vgpu_unlock) |
| A 470.05 dev driver véletlenül kikapcsolja az RTX 3060 limiterét | RTX 3060 | 2021-03-15 | NVIDIA (visszavonta) | ~3 hét | [TechPowerUp](https://www.techpowerup.com/279759/) |
| LHR bejelentés (3080/3070/3060 Ti) | RTX 30 | 2021-05-18 | NVIDIA | – | [PC Gamer](https://www.pcgamer.com/nvidia-rtx-3080-lhr-cryptocurrency-limit-announcement) |
| LHR **~70%** feloldás (NBMiner v39.0, `-lhr 68`) | RTX 30 LHR | **2021-08-16** | NBMiner | ~3 hónap | [DVHardware](https://www.dvhardware.net/article75535.html) |
| LHR **100%** feloldás (LHRv3 kivételével; QuickMiner v0.5.4.0 RC) | RTX 30 LHR | **2022-05-07** | NiceHash | ~12 hónap | [Notebookcheck](https://www.notebookcheck.net/NVIDIA-GeForce-RTX-3000-series-LHR-mining-limit-gets-fully-bypassed-100-percent-hashrate-now-possible-on-NiceHash-QuickMiner-with-LHR-cards.618266.0.html) |
| P2P patch | RTX 4090 | 2024-04-12 | tinygrad (George Hotz) | ~18 hónap | [repó](https://github.com/tinygrad/open-gpu-kernel-modules) |
| P2P patch | RTX 5090 | 2025-05/06 | tinygrad (`570.148.08-p2p` branch) | ~3–4 hónap | ugyanott |
| P2P vegyes kártyákkal (5090 ↔ PRO 6000; generációk közti libcuda-patch) | 30/40/50 | 2026 (legújabb: `615.78.08-p2p`, 2026-09-04) | aikitoria | – | [repó](https://github.com/aikitoria/open-gpu-kernel-modules) |
| vGPU-kísérlet Blackwellen (sikertelen, hardveresen blokkolt) | RTX 5090 | 2026-03-31 | bird | – | [repó](https://github.com/bird/vgpu-unlock-blackwell) |
| **FP32-akkumulálás feloldása (tensor)** | RTX 30 | **2026-09-28** | Zagitta | ~6 év | [repó](https://github.com/Zagitta/gpu-unlock) |
| **FP32-akkumulálás feloldása (tensor)** | RTX 40 | **2026-10-23** (v1.1.0) | JustAResearcher | ~4 év | [repó](https://github.com/JustAResearcher/gpu-unlock-ada) |

**Mintázat:**
- A **driver-szintű** korlátok hónapok alatt dőlnek el (P2P az 5090-en: 3–4 hónap).
- A **firmware- vagy fuse-közeli** korlátok évek alatt, vagy soha (tensor-felezés: 4–6 év; Blackwellen nincs).
- Az RTX 6090-re reális várakozás:
  - **P2P:** néhány hónapon belül [B];
  - **tensor-felezés:** bizonytalan, valószínűleg nem.

#### Mennyit ér ez a helyi LLM-futtatásban

| Feloldás | Decode (1 felhasználó) | Prefill / első token | Batch / szerver | Finomhangolás | Forrás |
|---|---|---|---|---|---|
| Tensor FP32-akkumulálás feloldása (csak RTX 30/40) | 0% | +16% (3090, llama.cpp, hosszú kontextus) … +25–55% (FP16/BF16/AWQ, vLLM) | GEMM +12–34% | +25–50% | Zagitta README, [Notebookcheck](https://www.notebookcheck.net/Nvidia-RTX-3090-performance-nearly-doubles-with-free-GPU-unlock-but-theres-a-catch.1432805.0.html), gpu-unlock-ada |
| ugyanez kvantált GGUF / FP8 / INT4 modellen | 0% | 0–15% | ≈0 | – | ugyanott (kvantált MoE: 0,98×) |
| P2P, 2 GPU (2×5090, vLLM TP=2) | **+2,7%** átlag (−1,9…+4,7%) | hasonló | – | – | [vLLM fórum](https://discuss.vllm.ai/t/dual-rtx-5090-tp-2-shm-vs-patched-bar1-p2p-cumem-single-pass-2-7-mean-point-estimate/2870) |
| P2P, 8×4090 all-reduce | – | – | busbw +42%; késleltetés 11,7 → 1,2 µs | DDP-nél számít | [charlie0129](https://charlie0129.github.io/blog/p/rtx4090-p2p-unlocked/) |
| P2P + MoE-hangolás, 2×3090 vLLM | 35–65 → 90–197 tok/s (a két hatás összemosódik) | – | „10–30% összesen” | – | [smcleod](https://smcleod.net/2026/02/patching-nvidias-driver-and-vllm-to-enable-p2p-on-consumer-gpus/) |
| Memória-túlhajtás | **+5–10%** [B] | ≈0 | kicsi | ≈0 | közvetlen A/B mérés nincs |
| Power limit emelése / XOC BIOS | ≈0 | +0–5% [B] | – | kicsi | – |
| ECC kikapcsolása (4090) | ~+1,6% | – | – | – | [dev.to](https://dev.to/maximsaplin/4090-ecc-on-vs-ecc-off-36m4) |

**A kalkulátorban használt értékek:**
- memória-túlhajtás: **×1,06**;
- tensor parallel hatásfok: P2P nélkül 0,80, **P2P-vel 0,82** (0,80 × 1,027);
- prefill-szorzó az RTX 6090-re: 1,00, mert a tensor-feloldás Blackwell/Rubin generáción nem várható.

#### Kockázatok

- **Garancia:** VBIOS- és XOC-flash esetén elveszhet. A kernel-modul alapú feloldás nyom nélkül eltávolítható, kikapcsolás után a kártya gyári állapotban indul.
- **Stabilitás:**
  - A tensor-feloldást kevés kártyán tesztelték. Első alkalommal hideg indítás (teljes kikapcsolás), utána újraindítás kell.
  - A P2P patch az IOMMU-t `pt` módba állítja, ezzel megszűnik a DMA-izoláció. Megbízhatatlan eszközzel vagy VM-mel kockázatos.
- **Adatintegritás:** a memória-túlhajtást a GDDR7 hibajavító újrapróbálkozása (EDR) elfedheti. Ilyenkor gyorsulás helyett lassulást, ritkán numerikus hibát okoz. Hosszú finomhangolás előtt memória-teszt és determinisztikus összehasonlítás ajánlott.
- **Illesztőprogram-licenc (EULA)** (NVIDIA, [licenc](https://www.nvidia.com/en-us/drivers/geforce-license/)):
  - 2.8: adatközponti használat tiltva;
  - 2.3: bináris módosítás tiltva;
  - 2.6: technikai korlát megkerülése tiltva.

  Az open kernel modul forrása MIT/GPL licencű, a módosítása licencszerű. A libcuda bináris patch és a firmware-útvonalú feloldás viszont a licenccel ütközhet. Ez szerződéses kockázat, nem büntetőjogi.
- **Jog:** a saját hardver és driver magáncélú módosítása az EU-ban általában nem jogellenes. Kereskedelmi terjesztés vagy bérbeadás más megítélés alá esik. Ez nem jogi tanács.

#### Lépésről lépésre (Linux)

**A) P2P patchelt kernel modul** (aikitoria README alapján):
```bash
# 0. UEFI: Above 4G Decoding + Resizable BAR BE; ACS KI, ha a BIOS engedi
nvidia-smi -q | grep -i bar -A 3          # a BAR1 Total legyen >= VRAM
# 1. IOMMU passthrough: /etc/default/grub → GRUB_CMDLINE_LINUX_DEFAULT="... amd_iommu=on iommu=pt" ; sudo update-grub
# 2. a driververziódhoz illő branch
git ls-remote --heads https://github.com/aikitoria/open-gpu-kernel-modules | grep p2p
# 3. ugyanazt a userspace drivert telepítsd: ./NVIDIA-Linux-x86_64-<ver>.run --no-kernel-modules
git clone --depth 1 -b 615.78.08-p2p https://github.com/aikitoria/open-gpu-kernel-modules
cd open-gpu-kernel-modules && ./install.sh
# vegyes generációnál (pl. 6090 + más generációs RTX Pro) a libcuda patch is kell: sudo ./patch-libcuda-p2p.py /usr/lib/x86_64-linux-gnu/libcuda.so.1  (előtte mentés!)
sudo reboot
nvidia-smi topo -p2p r                    # "OK" kell a GPU-k között
git clone --depth 1 -b v13.3 https://github.com/NVIDIA/cuda-samples   # a p2pBandwidthLatencyTest a 13.4-ből kikerült
```

**B) Tensor-feloldás:** csak RTX 30/40-re, az RTX 6090-re nem.
```bash
git clone https://github.com/Zagitta/gpu-unlock && cd gpu-unlock && make install
# kernel cmdline: gpu_unlock.targets=all ; első alkalommal hideg indítás (teljes kikapcsolás) kell
journalctl -k -b | grep gpu_unlock        # "gpu_unlock: unlocked"
```

**C) Fogyasztás, órajel, memória-túlhajtás:**
```bash
sudo nvidia-smi -pm 1 && nvidia-smi -q -d POWER
sudo nvidia-smi -i 0 -pl 500                            # power limit (W) a VBIOS-tartományon belül
# memória-offset Linuxon: nvidia_oc (NVML, headless/Wayland) vagy LACT (GUI + daemon)
./nvidia_oc set --index 0 --power-limit 500000 --mem-offset 1500     # a power limit itt mW-ban; lépésenként teszteld
llama-bench -m model.gguf -p 512 -n 128                 # A/B mérés gyári ↔ túlhajtott állapot
```
