#!/usr/bin/env python3
"""LLM-kutatás (research/llm_*.md.txt) -> items_llm.jsonl. Modellenként egy group, kvantonként egy változat."""
import json, re, sys
sys.path.insert(0, ".")
from llm_parse import load_blocks

UNIT = {"KB": 1e3, "MB": 1e6, "GB": 1e9, "TB": 1e12}
SKIP_FMT = re.compile(r"patch|mmproj|extra|base for patch|NEM abliterated", re.I)


def first_size(*txts):
    for t in txts:
        m = re.search(r"([\d.]+)\s*(KB|MB|GB|TB)\b", str(t or ""), re.I)
        if m:
            return int(float(m.group(1)) * UNIT[m.group(2).upper()])
    for t in txts:  # "Q4_K_M 2.74 / ..." – mértékegység nélkül GB
        m = re.search(r"\b(?:Q\d\w*|IQ\d\w*|UD-\w+|MXFP4\w*|q4_0)\s+([\d.]+)\b", str(t or ""))
        if m:
            return int(float(m.group(1)) * 1e9)
    return None


QTOK = r"((?:UD-|KLX-)?(?:I?Q\d[\w]*|MXFP4[\w]*|BF16|F16|q4_0)|[\w.-]+\.gguf)"


def expand(q):
    """Egy kutatási sorból (quant + size) -> [(quant_név, bájt)]."""
    quant, size = str(q.get("quant") or q.get("format")), str(q.get("size") or "")
    pairs = re.findall(QTOK + r"\s+([\d.]+)\s*(?:GB)?(?=[\s,/;)…+]|$)", quant)
    if len(pairs) >= 1 and not re.search(r"\d\s*GB", size) or len(pairs) >= 2:
        return [(n, int(float(v) * 1e9)) for n, v in pairs]
    names = [x.strip() for x in re.split(r"\s*/\s*", quant)]
    sizes = re.findall(r"([\d.]+)", size.split("(")[0]) if "/" in size else []
    if len(names) > 1 and len(names) == len(sizes):
        return [(n, int(float(v) * 1e9)) for n, v in zip(names, sizes)]
    return [(quant, first_size(size, quant))]


def hw_list(tier):
    ns = [int(n) for n in re.findall(r"T([1-5])", str(tier or ""))]
    return [f"T{i}" for i in range(1, max(ns) + 1)] if ns else []


def platform(fmt, runtime):
    f, r = str(fmt), str(runtime or "")
    if "LiteRT" in f:
        return "android"
    if "MLX" in f:
        return "mac"
    if "GGUF" in f or "llama.cpp" in r or "ollama" in r.lower():
        return "any"
    return "server"  # safetensors / FP8 / NVFP4 / AWQ / GPTQ / EXL3 – vLLM, SGLang, KTransformers (NVIDIA)


def hf_repo(u):
    m = re.search(r"(?:huggingface\.co/)?([\w.-]+/[\w.-]+)", str(u or ""))
    return m.group(1) if m and "/" in m.group(1) else None


def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", str(s).lower()).strip("-")[:40]


AA = {  # Artificial Analysis Intelligence Index v5.0.1 (2026-11-12); "~" = becslés (nincs v5 pont)
 "kimi-k3-1-pro": 46.5, "deepseek-v4-1-flash-1017": 32.6, "glm-5-3": 31.7, "mimo-v2-6-pro": 29.9, "ling-3-1-flash-1019": 29.6,
 "minimax-m3-1-flash": 29.1, "qwen3-8-flash-next": 28.6, "step-5-preview": 28.5, "glm-5-3-flash": 27.8, "muse-spark-open": 24.9,
 "qwen3-8-27b": 20.1, "muse-glimmer-30b": 6.3, "inkling-2-small": 30.6, "hy4-preview": 34.6, "qwen3-8-2-4t-a95b": 33.7,
 "mistral-large-4": 25.3, "longcat-2-5": 30.0}
AA_EST = {"hy4-preview", "qwen3-8-2-4t-a95b", "longcat-2-5"}  # Hy4: a végleges Hy4 pontja (34,6), mi a preview-t archiváljuk; 2.4T: a Qwen3.8-Max (API) 33,7-es pontja alapján
UNC_BASE = [("deepseek-v4-1", 32.6), ("glm-5-3-flash", 27.8), ("glm-5-3", 31.7), ("qwen3-8-flash-next", 28.6), ("kimi-k3", 17.4),
 ("minimax-m3-1", 29.1), ("gpt-oss-120b", 3.8), ("mistral-small-4", 8.0), ("qwen3-8-27b", 20.1), ("arete-27b", 19.0),
 ("gemma-4-31b", 4.4), ("gemma-4-26b", 3.5), ("qwen3-6-35b", 8.0), ("gpt-oss-20b", 2.5), ("gemma-4-12b", 3.0),
 ("qwen3-5-9b", 3.0), ("qwen3-5-4b", 2.0), ("gemma-4-e4b", 2.5), ("gemma-4-e2b", 1.5)]


def aa_for(mid, name, quant, b, kind):
    if kind == "uncensored":
        for k, v in UNC_BASE:
            if k in mid:
                return round(v * 0.95, 2), True
        return 5.0, True
    if mid == "gemma-4":
        for tok, v in (("E2B", 1.5), ("E4B", 2.5), ("12B", 3.0), ("26B", 3.5), ("31B", 4.4)):
            if tok.lower() in quant.lower():
                return v, tok != "31B"
        return 4.4 if b > 18e9 else 2.5, True
    if mid == "nemotron-3-5":
        if b > 40e9: return 13.6, False
        return (2.5, True) if "bolt" in quant.lower() else (5.5, False)   # Bolt-E4B: nincs AA-pont, E4B-szintű becslés
    if mid == "qwen3-5-small":
        return (2.0, True) if b < 4e9 else (3.0, True)
    return AA.get(mid, 5.0), mid in AA_EST or mid not in AA


def bits_of(q, fmt):
    t = (q + " " + fmt).upper()
    m = re.search(r"\bOQ(\d(?:\.\d)?)E?\b|\bBPW(\d(?:\.\d)?)|(\d(?:\.\d)?)\s*BIT", t)
    if m:
        return float(next(g for g in m.groups() if g)) + 0.5
    for pat, b in ((r"IQ1|Q1_|UD-Q1|1BIT|1-BIT", 1.7), (r"IQ2|Q2_|2BIT|2-BIT|OPTIQ-2", 2.6), (r"IQ3|Q3_|3BIT|3-BIT|BPW3", 3.5),
                   (r"Q4|IQ4|4BIT|4-BIT|MXFP4|NVFP4|AWQ|INT4|GPTQ|W4A4|OQ4|AUTOROUND|EXL3", 4.5), (r"Q5|5BIT", 5.5),
                   (r"Q6|6BIT", 6.5), (r"Q8|8BIT|FP8|INT8|MXFP8", 8.5), (r"BF16|F16|NATIVE", 16)):
        if re.search(pat, t):
            return b
    return 4.5


REJ = []
# aktív paraméter (milliárd) és MoE-jelző modellenként; a vegyes csoportoknál változatonként dől el (active_for)
ACT = {"kimi-k3-1-pro": (104, True), "deepseek-v4-1-flash-1017": (16, True), "glm-5-3": (40, True), "glm-5-3-flash": (18, True),
 "mimo-v2-6-pro": (42, True), "ling-3-1-flash-1019": (25, True), "minimax-m3-1-flash": (23, True), "qwen3-8-flash-next": (6, True),
 "qwen3-8-2-4t-a95b": (95, True), "step-5-preview": (27, True), "inkling-2-small": (17, True), "hy4-preview": (49, True),
 "mistral-large-4": (52, True), "muse-spark-open": (42, True), "qwen3-8-27b": (27.8, False), "muse-glimmer-30b": (29.6, False),
 "longcat-2-5": (48, True)}
UNC_ACT = [("deepseek-v4-1", 16, True), ("glm-5-3-flash", 18, True), ("glm-5-3", 40, True), ("qwen3-8-flash-next", 6, True),
 ("kimi-k3", 104, True), ("minimax-m3-1", 23, True), ("gpt-oss-120b", 5.1, True), ("mistral-small-4", 6.5, True),
 ("qwen3-8-27b", 27.8, False), ("arete-27b", 27.4, False), ("gemma-4-31b", 31.3, False), ("gemma-4-26b", 4, True),
 ("qwen3-6-35b", 3, True), ("gpt-oss-20b", 3.6, True), ("gemma-4-12b", 12, False), ("qwen3-5-9b", 9.5, False),
 ("qwen3-5-4b", 4.6, False), ("gemma-4-e4b", 4.5, False), ("gemma-4-e2b", 2, False)]


def active_for(mid, kind, quant_repo, b):
    q = quant_repo.lower()
    if kind == "uncensored":
        for k, a, moe in UNC_ACT:
            if k in mid:
                return a, moe
        return None, True
    if mid == "gemma-4":
        for tok, a, moe in (("e2b", 2, False), ("e4b", 4.5, False), ("12b", 12, False), ("26b", 4, True), ("31b", 31.3, False)):
            if tok in q:
                return a, moe
        return (31.3, False) if b > 18e9 else (4.5, False)
    if mid == "nemotron-3-5":
        if b > 40e9: return 12, True
        return (3, True) if "lightning" in q else (4, False)
    if mid == "qwen3-5-small":
        for tok, a in (("0.8b", 0.9), ("2b-", 2.3), ("4b", 4.6), ("9b", 9.5)):
            if tok in q: return a, False
        return (4.6, False) if b < 4e9 else (9.5, False)
    if mid == "mimo-v2-6-pro" and "flash" in q:
        return 15, True
    return ACT.get(mid, (None, True))


def main():
    out, seen = [], set()

    def uid(base):
        i, b = 1, base
        while b in seen:
            i += 1; b = f"{base}-{i}"
        seen.add(b); return b

    def emit(model, qlist, cat, tier, kind):
        mid = slug(model.get("id") if not str(model.get("id", "")).startswith(("A", "B")) or len(str(model.get("id"))) > 3 else model.get("name"))
        group = f"llm-{mid}"
        sc = model.get("scores") or {}
        num = lambda x, d: float(re.match(r"[\d.]+", str(x)).group(0)) if x is not None and re.match(r"[\d.]+", str(x)) else d
        intel = num(sc.get("intelligence"), 6)
        O = round(num(sc.get("offline_ease"), 5))
        prev_repo = hf_repo(model.get("hf_repo"))
        vars_ = []
        for q in qlist or []:
            fmt = str(q.get("format") or "")
            if SKIP_FMT.search(fmt) or str(q.get("tier")) in ("-", "None"):
                continue
            repo = hf_repo(q.get("repo_url")) if q.get("repo_url") not in (None, "same") else prev_repo
            prev_repo = repo or prev_repo
            hw = hw_list(q.get("tier"))
            if not (repo and hw):
                continue
            plat = platform(fmt, q.get("runtime"))
            for quant, b in expand(q):
                if not b:
                    continue
                m = re.search(r"[\w.-]+\.gguf", quant)
                if plat == "any" and m:
                    inc = [m.group(0)]
                elif plat == "any":
                    inc = [f"*{quant.split()[0]}*"]
                else:
                    inc = []
                vars_.append(dict(repo=repo, b=b, hw=hw, plat=plat, quant=quant, fmt=fmt, runtime=q.get("runtime"), inc=inc,
                                  st=q.get("size_status"), tier_txt=q.get("tier")))
        for o in model.get("ollama") or []:
            b = first_size(o.get("size"))
            if b and b > 0 and "cloud" not in str(o.get("tag")):
                tag = str(o.get("tag")).split(",")[0].strip()
                vars_.append(dict(repo=None, b=b, hw=["T1", "T2", "T3", "T4"] if b < 60e9 else ["T1", "T2", "T3"], plat="any",
                                  quant=f"ollama {tag}", fmt="ollama", runtime="Ollama", inc=[], st="verified (ollama registry)", tag=tag, tier_txt="Ollama, CPU/GPU vegyes"))
        # fizikai józansági ellenőrzés: bájt >= 0.5 * paraméter * bit/8 (egy-méretű modellnél)
        ptxt = str(model.get("params_total") or model.get("params") or "")
        nums = [float(n) * (1000 if u == "T" else 1) * 1e9 for n, u in re.findall(r"([\d.]+)\s*([BT])\b", ptxt)]
        if nums:
            P = min(nums)  # alsó korlát: a legkisebb említett (aktív/legkisebb tag) paraméterszám
            keep = []
            for v in vars_:
                exp = P * bits_of(v["quant"], v["fmt"]) / 8
                if v["b"] >= 0.5 * exp or v["fmt"] == "ollama":
                    keep.append(v)
                else:
                    REJ.append(f"{mid}: {v['quant']} {v['b']/1e9:.2f} GB < 0.5 x {exp/1e9:.0f} GB")
            vars_ = keep
        vars_.sort(key=lambda v: v["b"])
        for rank, v in enumerate(vars_, 1):
            iid = uid(f"llm-{mid}-{slug(v['fmt'])}-{slug(v['quant'].split()[0])}")
            aa, est = aa_for(mid, str(model.get("name")), f"{v['quant']} {v['repo'] or ''}", v["b"], kind)
            if mid == "mimo-v2-6-pro" and "flash" in f"{v['quant']} {v['repo'] or ''}".lower():
                aa = 26.7  # MiMo-V2.6-Flash (AA v5)
            act, moe = active_for(mid, kind, f"{v['quant']} {v['repo'] or ''}", v["b"])
            bits = bits_of(v["quant"], v["fmt"])
            S = {"S": 4, "R": round(4 + 6 * (aa / 46.5) ** 0.5), "A": 6, "U": 7 if kind == "uncensored" else 6, "Q": 5, "O": O}
            dl = {"method": "ollama", "tag": v["tag"]} if v["fmt"] == "ollama" else {"method": "hf", "repo": v["repo"], "include": v["inc"]}
            gated = "gated" in json.dumps(model, ensure_ascii=False, default=str).lower() and "nem gated" not in json.dumps(model, ensure_ascii=False, default=str).lower()
            out.append({
                "id": iid, "name": f"{model.get('name')} · {(v['repo'] or '').split('/')[-1]} · {v['quant'][:40]} ({v['fmt']})", "cat": cat, "tier": tier,
                "group": group, "variant_rank": rank,
                "desc_hu": (model.get("strengths_hu") or model.get("notes") or "")[:400],
                "lang": "multi", "access": "free-registration" if gated else "free", "license": str(model.get("license")),
                "bytes": v["b"], "size_human": f"{v['b'] / 1e9:.2f} GB", "size_status": f"measured:2026-11-14:{v['st'] or 'hf-api'}",
                "format": v["fmt"], "info_url": f"https://huggingface.co/{v['repo']}" if v["repo"] else "https://ollama.com/library",
                "download": dl, "url_status": "200 verified 2026-11-14 (HF API)", "scores": S,
                "hw_tiers": v["hw"], "platform": v["plat"], "runtime": v["runtime"],
                "notes": f"Hardver: {v['tier_txt']}. Runtime: {v['runtime']}. " + str(model.get("notes") or "")[:300],
                "released": str(model.get("released") or model.get("base_created") or ""),
                "llm_aa": aa, "llm_aa_est": est, "llm_bits": bits, "active_b": act, "moe": moe,
            })

    fr = load_blocks("research/llm_frontier.md.txt")[0]
    for m in fr:
        emit(m, m.get("quants"), "ai_models", 2, "frontier")
    un = load_blocks("research/llm_uncensored_runtimes.md.txt")
    for m in un[0]:
        emit(m, m.get("quants"), "ai_models_uncensored", 3, "uncensored")
    open("items_llm.jsonl", "w", encoding="utf-8").write("\n".join(json.dumps(o, ensure_ascii=False, separators=(",", ":")) for o in out) + "\n")
    groups = {}
    for o in out:
        groups.setdefault(o["group"], []).append(o)
    print(f"{len(out)} változat, {len(groups)} modell; elvetett (méret-ellentmondás): {len(REJ)}")
    for r in REJ: print("   REJ", r)
    for g, v in groups.items():
        print(f"  {g:<45} {len(v):>3} var  {v[0]['size_human']:>10} … {v[-1]['size_human']:>10}  plat={sorted({x['platform'] for x in v})}")


if __name__ == "__main__":
    main()
