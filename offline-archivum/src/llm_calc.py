#!/usr/bin/env python3
"""
LLM-eszközkalkulátor (csak Python stdlib, 3.9+). Bármely eszközre megmondja a 4 változatot:
  V1  a legokosabb CENZÚRÁZATLAN modell, ami épp elfér és elfut
  V2  a legokosabb CENZÚRÁZOTT (alap) modell, ami épp elfér és elfut
  V3  CSAPAT (alap modellekből): fő modell + gyors segédmodell (router / gyors válasz / draft) + RAG-embedding, egyszerre a memóriában
  V4  VEGYES CSAPAT: alap + cenzúrázatlan modell együtt (+ gyors segéd, ha még belefér) + RAG-embedding

Bemenet: az ARCHIVUM.md (vagy JSONL) katalógus LLM-változatai (méret, bit, aktív paraméter, AA-intelligencia, formátum).
Becslési modell (NEM mérés):
  memóriaigény = fájlméret x 1,15 + 1 GB (KV cache ~16-32k kontextus, futtatói overhead)
  generálási sebesség (1 felhasználó): tok/s = 1 / ( aktív_bájt_GPU/(0,6*BW_GPU) + aktív_bájt_RAM/(0,6*BW_RAM) + fix_ms + hálózati ugrások )
  okosság = AA-index x kvantminőség-szorzó (MoE: 1,7 bit 0,55 · 2,6 bit 0,75 · 3,5 bit 0,9 · 4-5 bit 1,0 · 6 bit 1,03 · 8+ bit 1,05;
            dense: 1,7 bit 0,15 · 2,6 bit 0,6 · 3,5 bit 0,85 · 4+ bit mint MoE)
  döntés = okosság x (1 + 5% minden sebesség-duplázásért a minimum felett, max +20%)
  csapat: V3 = fő + gyors segéd (≤30% memória, ≥3,5 bit, ≥ ~2x minimum tok/s), pontszám = fő + 0,25 x segéd
          V4 = fő + másik cenzúra-típusú partner (+ gyors segéd), pontszám = fő + 0,35 x partner (azonos modellcsaládnál 0,6-os szorzó)

Használat:
  python3 llm_calc.py ARCHIVUM.md --preset all                 # a beépített eszközprofilok (lásd PRESETS)
  python3 llm_calc.py ARCHIVUM.md --preset gamer-pc-256
  python3 llm_calc.py ARCHIVUM.md --name "Saját PC" --vram 24 --vram-bw 1008 --ram 128 --ram-bw 90
  python3 llm_calc.py ARCHIVUM.md --name "2 kártya" --gpu 32:1790 --gpu 96:1800 --ram 256 --ram-bw 83 --formats any,server
  python3 llm_calc.py ARCHIVUM.md --name "Mac" --unified 512 --unified-usable 0.92 --unified-bw 819 --formats any,mac
  python3 llm_calc.py ARCHIVUM.md --name "3 db Strix" --unified 192 --unified-usable 0.83 --unified-bw 273 --nodes 3 --hop-ms 3
  --min-tps 5 (alap): ennél lassabb modellt nem tekint "elfutónak". --md: Markdown-tábla kimenet.
"""
import argparse, json, math, re, sys

EFF = 0.6
OPUS = 59.1  # Claude Opus 5.5 (max), AA Intelligence Index v5.0.1 – a "% Opus" viszonyítási pontja
EMBED_GB = 0.8  # bge-m3 Q8 + overhead


def load(path):
    t = open(path, encoding="utf-8").read()
    lines = [l for b in re.findall(r"```jsonl\n(.*?)```", t, re.S) for l in b.splitlines()] if path.endswith(".md") else t.splitlines()
    out = []
    for l in lines:
        l = l.strip()
        if l and not l.startswith("//"):
            d = json.loads(l)
            if d.get("cat", "").startswith("ai_models") and d.get("llm_aa") is not None and d.get("bytes"):
                out.append(d)
    return out


def qf(bits, moe=True):
    """Kvantminőség-szorzó. A dense (kisebb) modellek a nagyon alacsony bitszámot sokkal rosszabbul tűrik, mint a nagy MoE-k."""
    if moe:
        return 0.55 if bits < 2 else 0.75 if bits < 3 else 0.9 if bits < 4 else 1.0 if bits < 5 else 1.03 if bits < 7 else 1.05
    return 0.15 if bits < 2 else 0.6 if bits < 3 else 0.85 if bits < 4 else 1.0 if bits < 5 else 1.03 if bits < 7 else 1.05


# --- eszközprofilok. Minden GB decimális. "usable" = ami ténylegesen a modellnek jut (OS, appok, GPU-limit levonva). ---
PRESETS = {
 # telefonok
 "s24-ultra": dict(name="Samsung Galaxy S24 Ultra (12 GB, Snapdragon 8 Gen 3)", kind="telefon", unified=12, unified_usable=0.62,
                   unified_bw=68, formats="any,android", fix_ms=25, min_tps=4,
                   note="Android: PocketPal / ChatterUI (GGUF). Kb. 7,5 GB jut a modellnek. Sávszélesség ~68 GB/s (LPDDR5X, becslés)."),
 "iphone-15-pro": dict(name="iPhone 15 Pro (8 GB, A17 Pro)", kind="telefon", unified=8, unified_usable=0.62, unified_bw=51,
                       formats="any,mac", fix_ms=25, min_tps=4,
                       note="iOS: PocketPal / LLM Farm (GGUF), Locally AI (MLX). Kb. 5 GB jut a modellnek (iOS app-memórialimit)."),
 # laptopok
 "pavilion-8": dict(name="HP Pavilion 15-bc504ur (8 GB DDR4, GTX 1050 4 GB) – mostani", kind="laptop", vram=4, vram_bw=112,
                    ram=8, ram_usable=0.6, ram_bw=21, formats="any", fix_ms=15, min_tps=4,
                    note="i5-9300H + GTX 1050 4 GB (a bc504TX testvérmodell adatai alapján). Egycsatornás DDR4-2666 ~21 GB/s."),
 "pavilion-16": dict(name="HP Pavilion 15-bc504ur (16 GB DDR4 dual channel, GTX 1050 4 GB)", kind="laptop", vram=4, vram_bw=112,
                     ram=16, ram_usable=0.75, ram_bw=42, formats="any", fix_ms=15, min_tps=4,
                     note="+8 GB → kétcsatornás DDR4-2666 ~42 GB/s. A gyors SSD a modell betöltését gyorsítja, a futást nem."),
 "zbook-g3a-192": dict(name="HP ZBook Ultra G3a (192 GB unified, Ryzen AI Max+ PRO 495)", kind="laptop", unified=192,
                       unified_usable=0.83, unified_bw=256, formats="any", fix_ms=10, min_tps=5,
                       note="A GPU-nak max. 160 GB adható (HP). LPDDR5X-8000 × 256 bit ≈ 256 GB/s (számolt). Linux + llama.cpp Vulkan/ROCm ajánlott."),
 # AI workstation (Strix/Gorgon Halo mini PC-k, USB4 v2 80 Gbps-sel összekötve)
 "ms-s1-x1": dict(name="1× MINISFORUM MS-S1 MAX-P495 (192 GB)", kind="workstation", unified=192, unified_usable=0.83,
                  unified_bw=273, formats="any", fix_ms=10, min_tps=5, note="LPDDR5X-8533 × 256 bit ≈ 273 GB/s (számolt); GPU-ra max. 160 GB."),
 "ms-s1-x2": dict(name="2× MS-S1 MAX-P495 (2×192 GB, USB4 v2 80 Gbps)", kind="workstation", unified=192, unified_usable=0.83,
                  unified_bw=273, nodes=2, hop_ms=3, formats="any", fix_ms=10, min_tps=5,
                  note="llama.cpp RPC / exo pipeline-párhuzamosítás: a kapacitás összeadódik, a sebesség ~1 gépé + hálózati késleltetés."),
 "ms-s1-x4": dict(name="4× MS-S1 MAX-P495 (4×192 GB, USB4 v2 gyűrű)", kind="workstation", unified=192, unified_usable=0.83,
                  unified_bw=273, nodes=4, hop_ms=3, formats="any", fix_ms=10, min_tps=5,
                  note="Gépenként 2 db USB4 v2 port → gyűrű topológia; alternatíva 2×10GbE. 640 GB GPU-memória összesen."),
 # gamer PC (Ryzen 9 9950X3D, X870E, RTX 6090 – pletyka: 32 GB GDDR7, ~1,79 TB/s)
 "gamer-pc-96": dict(name="Gamer PC – RTX 6090 32 GB + 96 GB DDR5-6000", kind="gamer PC", vram=32, vram_bw=1790, ram=96,
                     ram_usable=0.85, ram_bw=96, formats="any,server", fix_ms=6, min_tps=5,
                     note="RTX 6090 adatai nem hivatalosak (pletyka). 2 DIMM DDR5-6000 kétcsatornás ≈ 96 GB/s."),
 "gamer-pc-128": dict(name="Gamer PC – RTX 6090 32 GB + 128 GB DDR5", kind="gamer PC", vram=32, vram_bw=1790, ram=128,
                      ram_usable=0.87, ram_bw=96, formats="any,server", fix_ms=6, min_tps=5, note="2×64 GB, DDR5-6000 feltételezve."),
 "gamer-pc-192": dict(name="Gamer PC – RTX 6090 32 GB + 192 GB DDR5", kind="gamer PC", vram=32, vram_bw=1790, ram=192,
                      ram_usable=0.9, ram_bw=86, formats="any,server", fix_ms=6, min_tps=5, note="4×48 GB → kb. DDR5-5400 (4 DIMM-mel lassabb) ≈ 86 GB/s."),
 "gamer-pc-256": dict(name="Gamer PC – RTX 6090 32 GB + 256 GB DDR5", kind="gamer PC", vram=32, vram_bw=1790, ram=256,
                      ram_usable=0.9, ram_bw=83, formats="any,server", fix_ms=6, min_tps=5,
                      note="4×64 GB (AM5 maximum) → kb. DDR5-5200 ≈ 83 GB/s."),
 # gamer PC + második kártya: a következő generációs RTX Pro csúcs (Rubin-utód) – NINCS hivatalos adat, 3 forgatókönyv
 "gamer-2gpu-pro96": dict(name="Gamer PC – RTX 6090 32 GB + köv. gen. RTX Pro 96 GB (A: konzervatív) + 256 GB DDR5", kind="gamer PC",
                          gpus=[(32, 1790), (96, 1800)], ram=256, ram_usable=0.9, ram_bw=83, formats="any,server", fix_ms=7, min_tps=5,
                          note="A: az utód a mostani RTX PRO 6000 Blackwell szintjén (96 GB, ~1,8 TB/s). Összesen 128 GB VRAM."),
 "gamer-2gpu-pro128": dict(name="Gamer PC – RTX 6090 32 GB + köv. gen. RTX Pro 128 GB (B: valószínű) + 256 GB DDR5", kind="gamer PC",
                           gpus=[(32, 1790), (128, 2300)], ram=256, ram_usable=0.9, ram_bw=83, formats="any,server", fix_ms=7, min_tps=5,
                           note="B: 128 GB, ~2,3 TB/s (becslés). Összesen 160 GB VRAM."),
 "gamer-2gpu-pro192": dict(name="Gamer PC – RTX 6090 32 GB + köv. gen. RTX Pro 192 GB (C: optimista) + 256 GB DDR5", kind="gamer PC",
                           gpus=[(32, 1790), (192, 2800)], ram=256, ram_usable=0.9, ram_bw=83, formats="any,server", fix_ms=7, min_tps=5,
                           note="C: 192 GB, ~2,8 TB/s (optimista becslés). Összesen 224 GB VRAM."),
 # FELOLDVA: memória-túlhajtás ×1,06 (+5–10% decode [becslés]); két kártyánál tensor parallel + P2P (aikitoria patch), hatásfok 0,82
 "gamer-pc-128-unl": dict(name="Gamer PC – RTX 6090 FELOLDVA (mem-OC) + 128 GB DDR5", kind="gamer PC", vram=32, vram_bw=1790, vram_bw_mult=1.06,
                          ram=128, ram_usable=0.87, ram_bw=96, formats="any,server", fix_ms=6, min_tps=5,
                          note="Egy kártya: a P2P irreleváns; a tensor-felezés feloldása Blackwell/Rubinon nem várható → csak memória-OC ×1,06."),
 "gamer-pc-256-unl": dict(name="Gamer PC – RTX 6090 FELOLDVA (mem-OC) + 256 GB DDR5", kind="gamer PC", vram=32, vram_bw=1790, vram_bw_mult=1.06,
                          ram=256, ram_usable=0.9, ram_bw=83, formats="any,server", fix_ms=6, min_tps=5, note="Memória-OC ×1,06."),
 "gamer-2gpu-pro96-unl": dict(name="RTX 6090 + köv. RTX Pro 96 GB – FELOLDVA (P2P + TP + mem-OC) + 256 GB", kind="gamer PC",
                              gpus=[(32, 1790), (96, 1800)], vram_bw_mult=1.06, tensor_parallel=True, tp_eff=0.82, ram=256, ram_usable=0.9,
                              ram_bw=83, formats="any,server", fix_ms=7, min_tps=5,
                              note="A két kártya párhuzamosan (tensor parallel, P2P patch: aikitoria open-gpu-kernel-modules); vegyes generációnál libcuda-patch is kell."),
 "gamer-2gpu-pro128-unl": dict(name="RTX 6090 + köv. RTX Pro 128 GB – FELOLDVA (P2P + TP + mem-OC) + 256 GB", kind="gamer PC",
                               gpus=[(32, 1790), (128, 2300)], vram_bw_mult=1.06, tensor_parallel=True, tp_eff=0.82, ram=256, ram_usable=0.9,
                               ram_bw=83, formats="any,server", fix_ms=7, min_tps=5, note="B forgatókönyv, feloldva."),
 "gamer-2gpu-pro192-unl": dict(name="RTX 6090 + köv. RTX Pro 192 GB – FELOLDVA (P2P + TP + mem-OC) + 256 GB", kind="gamer PC",
                               gpus=[(32, 1790), (192, 2800)], vram_bw_mult=1.06, tensor_parallel=True, tp_eff=0.82, ram=256, ram_usable=0.9,
                               ram_bw=83, formats="any,server", fix_ms=7, min_tps=5, note="C forgatókönyv, feloldva."),
 # Linux szerverek
 "srv-epyc": dict(name="Linux szerver – EPYC 12 csatornás DDR5 768 GB + 1× RTX 6090 32 GB", kind="szerver", vram=32, vram_bw=1790,
                  ram=768, ram_usable=0.92, ram_bw=460, formats="any,server", fix_ms=8, min_tps=5,
                  note="ik_llama.cpp / KTransformers: MoE-szakértők RAM-ban, figyelem a GPU-n."),
 "srv-8xh200": dict(name="Linux szerver – 8× H200 141 GB (tensor parallel)", kind="szerver", vram=1128, vram_bw=8 * 4800 * 0.6,
                    ram=1024, ram_usable=0.9, ram_bw=460, formats="any,server", fix_ms=8, min_tps=5,
                    note="vLLM/SGLang TP=8; az összesített sávszélesség ~60%-át számolom (kommunikációs veszteség)."),
}


def tp_fractions(gpus, need):
    """A modell hányadai kártyánként: sávszélesség-arányos, de legfeljebb a kártya kapacitásáig (iteratív kitöltés)."""
    n = len(gpus); frac = [0.0] * n; free = set(range(n)); rest = need
    while free and rest > 1e-9:
        tot = sum(gpus[i][1] for i in free)
        capped = [i for i in free if rest * gpus[i][1] / tot > gpus[i][0]]
        if not capped:
            for i in free:
                frac[i] = rest * gpus[i][1] / tot / need
            break
        for i in capped:
            frac[i] = gpus[i][0] / need; rest -= gpus[i][0]; free.discard(i)
    return frac


class Device:
    def __init__(self, **k):
        self.name = k.get("name", "eszköz"); self.kind = k.get("kind", "")
        gpus = k.get("gpus") or ([(k["vram"], k["vram_bw"])] if k.get("vram") else [])
        m = k.get("vram_bw_mult", 1.0)                     # memória-túlhajtás (feloldott változat), pl. 1,08
        gpus = [(g, b * m) for g, b in gpus]
        self.gpus = gpus
        self.tp = bool(k.get("tensor_parallel"))           # P2P-vel: kártyák párhuzamosan (sávszélesség összeadódik)
        self.tp_eff = k.get("tp_eff") or 0.85
        self.vram = sum(g for g, _ in gpus)
        # több (eltérő) GPU rétegenkénti felosztással: a token sorban halad át a kártyákon → kapacitással súlyozott harmonikus sávszélesség
        self.vram_bw = self.vram / sum(g / b for g, b in gpus) if gpus else 0
        self.ram = (k.get("ram") or 0) * k.get("ram_usable", 0.85); self.ram_bw = k.get("ram_bw") or 0
        self.nodes = k.get("nodes") or 1; self.hop_ms = k.get("hop_ms") or 0
        self.uni = (k.get("unified") or 0) * k.get("unified_usable", 0.8) * self.nodes; self.uni_bw = k.get("unified_bw") or 0
        self.formats = set((k.get("formats") or "any").split(","))
        self.fix_ms = k.get("fix_ms", 10); self.min_tps = k.get("min_tps", 5); self.note = k.get("note", "")

    def capacity(self):
        return max(self.uni, self.vram + self.ram, self.vram, self.ram)

    def run(self, v, mem_left=None, vram_used=0.0):
        """(tok/s, elhelyezés, igény GB) vagy None, ha nem fér el / nem futtatható. vram_used: csapatnál a már foglalt VRAM."""
        fmt = v.get("platform", "any")
        if fmt not in self.formats:
            return None
        need = v["bytes"] / 1e9 * 1.15 + 1
        cap_left = mem_left if mem_left is not None else self.capacity()
        if need > cap_left + 1e-9:
            return None
        act = (v.get("active_b") or 30) * 1e9 * v["llm_bits"] / 8
        opts = []
        fix = self.fix_ms / 1000
        if self.uni and need <= min(self.uni, cap_left) and fmt != "server":
            hops = max(0, math.ceil(need / (self.uni / self.nodes)) - 1) if self.nodes > 1 else 0
            t = act / (EFF * self.uni_bw * 1e9) + fix + hops * self.hop_ms / 1000
            opts.append((1 / t, f"unified{' ×' + str(self.nodes) if self.nodes > 1 else ''}"))
        vram = max(0.0, self.vram - vram_used)
        gpus = [(g * vram / self.vram, b) for g, b in self.gpus] if self.vram else []
        if vram and need <= vram:
            bw, how = self.vram_bw, "csak GPU"
            if self.tp and len(gpus) > 1:
                # tensor parallel eltérő kártyákkal: "vízszint-kitöltés" – a kártyák egyszerre dolgoznak, a lassabbik dönt;
                # a kis kártya megtelik (capacity cap), a maradék a többire kerül sávszélesség-arányosan
                fr = tp_fractions(gpus, need)
                t_rel = max(f / b for f, (g, b) in zip(fr, gpus))            # idő / (aktív bájt), 1/(GB/s)
                bw_tp = self.tp_eff / t_rel
                if bw_tp > bw:
                    bw, how = bw_tp, f"csak GPU, tensor parallel ×{len(self.gpus)} (P2P)"
            opts.append((1 / (act / (EFF * bw * 1e9) + fix), how))
        if fmt != "server" and self.ram and need <= vram + self.ram and need > vram:
            share = max(0.0, (vram - 2) / need)
            f = min(1.0, (0.3 + 0.7 * share) if v.get("moe", True) else share) if vram > 2 else 0.0
            t = (act * f / (EFF * self.vram_bw * 1e9) if f else 0) + act * (1 - f) / (EFF * self.ram_bw * 1e9) + fix
            opts.append((1 / t, ("hibrid GPU+RAM" if f else "csak CPU") + ("" if v.get("moe", True) else " (dense)")))
        if fmt != "server" and self.ram and need <= self.ram and not self.uni:
            opts.append((1 / (act / (EFF * self.ram_bw * 1e9) + fix), "csak CPU"))
        if not opts:
            return None
        tps, where = max(opts)
        return tps, where, need


def smart(v):
    return v["llm_aa"] * qf(v["llm_bits"], v.get("moe", True))


def unusable_quant(v):
    """Dense (kisebb) modell 2,5 bit alatt gyakorlatilag használhatatlan – kizárjuk."""
    return v.get("moe") is False and v["llm_bits"] < 2.5


def usable(v, tps, min_tps):
    """Döntési pontszám: okosság, enyhe sebesség-bónusszal (+5% a minimum feletti minden sebesség-duplázásért, max +20%)."""
    import math
    return smart(v) * (1 + min(0.2, 0.05 * max(0.0, math.log2(tps / min_tps))))


def family(v):
    g = v["group"].replace("llm-", "")
    for base in ("deepseek-v4-1", "glm-5-3-flash", "glm-5-3", "qwen3-8-flash-next", "qwen3-8-27b", "qwen3-8-2-4t", "kimi-k3", "minimax-m3-1",
                 "gemma-4", "qwen3-5", "qwen3-6", "gpt-oss", "mistral", "nemotron", "mimo", "ling", "step-5", "inkling", "hy4", "muse", "longcat"):
        if base in g:
            return base
    return g


def best_single(dev, vs, unc, mem_left=None, min_tps=None, exclude_groups=(), alts=None):
    best = None
    allc = []
    for v in vs:
        if (v["cat"] == "ai_models_uncensored") != unc or v["group"] in exclude_groups or unusable_quant(v):
            continue
        r = dev.run(v, mem_left)
        if not r or r[0] < (min_tps or dev.min_tps):
            continue
        key = (usable(v, r[0], min_tps or dev.min_tps), r[0])
        allc.append((key, v, r))
        if best is None or key > best[0]:
            best = (key, v, r)
    if best and alts is not None:   # közel azonos (≥95%) alternatívák más modellcsaládból
        seen = {family(best[1])}
        for key, v, r in sorted(allc, key=lambda x: x[0], reverse=True):
            if family(v) not in seen and key[0] >= 0.95 * best[0][0]:
                alts.append((v, r)); seen.add(family(v))
            if len(alts) >= 2:
                break
    return best


def team(dev, vs, mixed):
    """V3 (mixed=False): alap fő + alap gyors segéd. V4 (mixed=True): fő + másik cenzúra-típusú partner (+ gyors segéd, ha fér)."""
    cap = dev.capacity() - EMBED_GB
    cands = [(v, dev.run(v)) for v in vs if not unusable_quant(v)]
    cands = [(v, r) for v, r in cands if r and r[0] >= dev.min_tps]
    if not mixed:
        cands = [c for c in cands if c[0]["cat"] == "ai_models"]
    cands.sort(key=lambda c: -usable(c[0], c[1][0], dev.min_tps))
    helper_tps = min(20, 2 * dev.min_tps + 2)            # telefonon ~10, PC-n 12-20 tok/s
    helper_max = max(4.0, min(40.0, 0.3 * cap))          # a segéd kicsi legyen
    def vram_of(r):
        return min(r[2], dev.vram) if r[1].startswith("csak GPU") else dev.vram if r[1].startswith("hibrid") else 0.0
    best = None
    for v1, r1 in cands[:80]:
        left = cap - r1[2]
        for v2, _r2 in cands:
            if v2["group"] == v1["group"] or _r2[2] > left:
                continue
            r2 = dev.run(v2, left, vram_of(r1))            # a maradék VRAM-ba/RAM-ba kell beférnie
            if not r2 or r2[0] < dev.min_tps:
                continue
            if mixed and (v1["cat"] == "ai_models_uncensored") == (v2["cat"] == "ai_models_uncensored"):
                continue
            if not mixed and (r2[0] < max(helper_tps, 1.2 * r1[0]) or r2[2] > helper_max or v2["llm_bits"] < 3.5):
                continue  # gyors segéd: kicsi, gyors, legalább ~3,5 bites
            if mixed and v2["llm_bits"] < 3.5 and v2.get("moe") is False:
                continue
            same = family(v1) == family(v2)
            w = (0.35 if mixed else 0.25) * (0.6 if same else 1.0)
            score = usable(v1, r1[0], dev.min_tps) + w * usable(v2, r2[0], dev.min_tps)
            if best is None or score > best[0]:
                best = (score, [(v1, r1, "fő modell"), (v2, r2, "partner (" + ("cenzúrázatlan" if v2["cat"] == "ai_models_uncensored" else "alap") + ")" if mixed else "gyors segéd / router")])
    if best and mixed:
        used = sum(r[2] for _, r, _ in best[1])
        groups = {v["group"] for v, _, _ in best[1]}
        h = None
        vu = sum(vram_of(r) for _, r, _ in best[1])
        for v, _r in cands:
            r = dev.run(v, cap - used, vu)
            if not r or v["group"] in groups or r[2] > cap - used or r[0] < max(helper_tps, 1.5 * best[1][0][1][0]) or v["llm_bits"] < 3.5 or r[2] > helper_max:
                continue
            if h is None or smart(v) > smart(h[0]):
                h = (v, r)
        if h:
            best[1].append((h[0], h[1], "gyors segéd / router"))
    if best:
        return best[1]
    # nem fér el egyszerre két modell (pl. telefon): VÁLTOTT csapat – a tárhelyen több modell, egyszerre egy fut
    singles = [c for c in cands if mixed or c[0]["cat"] == "ai_models"]
    if not singles:
        return None
    v1, r1 = singles[0]
    pool = [c for c in singles if c[0]["group"] != v1["group"] and c[0]["llm_bits"] >= 3.5]
    if mixed:
        pool = [c for c in pool if (c[0]["cat"] == "ai_models_uncensored") != (v1["cat"] == "ai_models_uncensored")]
        pool.sort(key=lambda c: -usable(c[0], c[1][0], dev.min_tps))
    else:
        pool = [c for c in pool if c[1][0] >= 1.5 * r1[0]] or pool
        pool.sort(key=lambda c: (-c[1][0], -smart(c[0])))
    if not pool:
        return None
    v2, r2 = pool[0]
    return [(v1, r1, "fő modell (váltva)"), (v2, r2, ("partner, váltva" if mixed else "gyors segéd, váltva") +
            " – egyszerre csak egy fér a memóriába, a tárhelyen mindkettő ott van")]


def label(v):
    d = v["download"]
    src = f"{d.get('repo')} {' '.join(d.get('include') or [])}".strip() if d["method"] == "hf" else f"ollama {d.get('tag')}"
    return v["name"].split(" · ")[0], src


def evaluate(dev, vs):
    res = {}
    for key, unc in (("V1", True), ("V2", False)):
        alts = []
        b = best_single(dev, vs, unc, alts=alts)
        res[key] = [(b[1], b[2], "egyedül")] + [(v, r, "közel azonos alternatíva") for v, r in alts] if b else None
    res["V3"] = team(dev, vs, False)
    res["V4"] = team(dev, vs, True)
    return res


def hu(x, d=1):
    """Szám magyar tizedesvesszővel."""
    return f"{x:.{d}f}".replace(".", ",")


def fmt_member(v, r, role):
    name, src = label(v)
    aa = v["llm_aa"]
    e = '~' if v.get('llm_aa_est') else ''
    return (f"{name} [AA v5 {e}{hu(aa)} = {e}{100 * aa / OPUS:.0f}% Opus 5.5 · "
            f"{hu(v['llm_bits'])} bit, {hu(v['bytes'] / 1e9)} GB, ~{r[0]:.0f} tok/s, {r[1]}] – {role} – `{src}`")


def report(dev, res, md=False):
    title = {"V1": "V1 legokosabb cenzúrázatlan", "V2": "V2 legokosabb alap (cenzúrázott)",
             "V3": "V3 csapat (alap modellek)", "V4": "V4 vegyes csapat (alap + cenzúrázatlan)"}
    out = []
    if md:
        cap = dev.capacity()
        out.append(f"#### {dev.name}\n\n*Modellnek jutó memória: ~{hu(cap, 1 if cap < 20 else 0)} GB · {dev.note}*\n")
        out.append("| Változat | Modell(ek) – kvant, méret, becsült sebesség, elhelyezés, letöltés |\n|---|---|")
        for k in ("V1", "V2", "V3", "V4"):
            r = res[k]
            cell = "<br>".join(fmt_member(*m) for m in r) if r else "nincs elég memória / túl lassú"
            if r and len(r) > 1 and k in ("V3", "V4") and "váltva" not in r[0][2]:
                cell += f"<br>+ RAG-embedding: `gpustack/bge-m3-GGUF *Q8_0*` (0,6 GB). Összesen ~{hu(sum(m[1][2] for m in r) + EMBED_GB, 0)} GB"
            out.append(f"| **{title[k]}** | {cell} |")
        out.append("")
    else:
        cap = dev.capacity()
        out.append(f"\n=== {dev.name}  (modellnek jutó memória ~{hu(cap, 1 if cap < 20 else 0)} GB)\n    {dev.note}")
        for k in ("V1", "V2", "V3", "V4"):
            r = res[k]
            out.append(f"  {title[k]}:")
            for m in (r or []):
                out.append("     - " + fmt_member(*m))
            if not r:
                out.append("     - nincs elég memória / túl lassú")
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("catalog")
    ap.add_argument("--preset", help="profil neve vagy 'all' (" + ", ".join(PRESETS) + ")")
    ap.add_argument("--name", default="Saját eszköz")
    ap.add_argument("--vram", type=float, help="dedikált GPU-memória GB"); ap.add_argument("--vram-bw", type=float, help="GPU sávszélesség GB/s")
    ap.add_argument("--gpu", action="append", default=[], help="több GPU: GB:GB/s, ismételhető (pl. --gpu 32:1790 --gpu 96:1800)")
    ap.add_argument("--ram", type=float, help="rendszer-RAM GB"); ap.add_argument("--ram-usable", type=float, default=0.85)
    ap.add_argument("--ram-bw", type=float, help="RAM sávszélesség GB/s (DDR5 2 csatorna ≈ 80-96, DDR4 2 csatorna ≈ 40-50)")
    ap.add_argument("--unified", type=float, help="unified memória GB (Mac, Strix Halo, telefon)")
    ap.add_argument("--unified-usable", type=float, default=0.8); ap.add_argument("--unified-bw", type=float)
    ap.add_argument("--nodes", type=int, default=1); ap.add_argument("--hop-ms", type=float, default=3)
    ap.add_argument("--formats", default="any", help="any (GGUF/Ollama), mac (MLX), server (vLLM/SGLang safetensors), android (LiteRT)")
    ap.add_argument("--min-tps", type=float, default=5); ap.add_argument("--fix-ms", type=float, default=10)
    ap.add_argument("--tensor-parallel", action="store_true", help="több GPU párhuzamosan (P2P), mint a HTML 'FELOLDVA' profiljai")
    ap.add_argument("--tp-eff", type=float, default=0.85, help="tensor parallel hatásfok (0,3–1,0; P2P-vel ~0,82)")
    ap.add_argument("--vram-bw-mult", type=float, default=1.0, help="memória-túlhajtás szorzója (pl. 1.06)")
    ap.add_argument("--md", action="store_true")
    a = ap.parse_args()
    vs = load(a.catalog)
    devs = []
    if a.preset:
        keys = list(PRESETS) if a.preset == "all" else a.preset.split(",")
        unknown = [k for k in keys if k not in PRESETS]
        if unknown:
            ap.error(f"ismeretlen profil: {', '.join(unknown)} – választható: {', '.join(PRESETS)}")
        devs = [Device(**PRESETS[k]) for k in keys]
    else:
        try:
            gpus = [tuple(float(x) for x in g.split(":")) for g in a.gpu] or None
        except ValueError:
            ap.error("--gpu formátuma GB:GB/s, pl. --gpu 32:1790")
        if gpus and any(len(g) != 2 or g[0] <= 0 or g[1] <= 0 for g in gpus):
            ap.error("--gpu formátuma GB:GB/s, mindkettő pozitív, pl. --gpu 32:1790")
        if a.vram and not (a.vram_bw and a.vram_bw > 0):
            ap.error("--vram mellé --vram-bw (GB/s) is kell")
        if a.ram and not (a.ram_bw and a.ram_bw > 0):
            ap.error("--ram mellé --ram-bw (GB/s) is kell (DDR4 2 csatorna ≈ 40–50, DDR5 2 csatorna ≈ 80–96)")
        if a.unified and not (a.unified_bw and a.unified_bw > 0):
            ap.error("--unified mellé --unified-bw (GB/s) is kell")
        if not (gpus or a.vram or a.ram or a.unified):
            ap.error("adj meg legalább egy memóriát: --gpu / --vram, --ram vagy --unified (vagy használj --preset-et)")
        if a.min_tps <= 0 or not (0.3 <= a.tp_eff <= 1.0) or a.nodes < 1:
            ap.error("--min-tps > 0, --tp-eff 0,3–1,0, --nodes >= 1 kell")
        devs = [Device(name=a.name, gpus=gpus, vram=a.vram, vram_bw=a.vram_bw, ram=a.ram, ram_usable=a.ram_usable, ram_bw=a.ram_bw,
                       unified=a.unified, unified_usable=a.unified_usable, unified_bw=a.unified_bw, nodes=a.nodes, hop_ms=a.hop_ms,
                       formats=a.formats, fix_ms=a.fix_ms, min_tps=a.min_tps, tensor_parallel=a.tensor_parallel, tp_eff=a.tp_eff,
                       vram_bw_mult=a.vram_bw_mult)]
    for d in devs:
        print(report(d, evaluate(d, vs), a.md))


if __name__ == "__main__":
    main()
