#!/usr/bin/env python3
"""Offline, önálló HTML: LLM-kalkulátor + eszközmátrix + modelltábla. Kimenet:
  ../ARCHIVUM-LLM.html          teljes dokumentum (offline megnyitható)
  ../ARCHIVUM-LLM.fragment.html  ugyanaz doctype/html/head nélkül (Artifact-publikáláshoz)
A kalkulátor JS-logikája a llm_calc.py 1:1 átirata; az adatok és a profilok ugyanabból a katalógusból jönnek."""
import json, os, re, sys, datetime
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import llm_calc
from llm_parse import load_blocks
from llm_to_items import slug, unc_estimate

HERE = os.path.dirname(os.path.abspath(__file__))
from build import cut
OPUS, FABLE = 59.1, 64.6


def variants():
    vs = llm_calc.load(os.path.join(HERE, "..", "ARCHIVUM.md"))
    out = []
    for v in vs:
        d = v["download"]
        name, rest = (v["name"].split(" · ", 1) + [""])[:2]
        out.append({"id": v["id"], "m": name, "q": rest, "u": v["cat"] == "ai_models_uncensored", "g": v["group"],
                    "f": llm_calc.family(v), "b": v["bytes"], "bits": v["llm_bits"], "aa": v["llm_aa"], "est": bool(v.get("llm_aa_est")),
                    "act": v.get("active_b"), "moe": v.get("moe", True), "plat": v.get("platform", "any"), "hw": v.get("hw_tiers", []),
                    "dl": (f"hf download {d['repo']}" + "".join(f' --include "{p}"' for p in d.get("include") or []))
                          if d["method"] == "hf" else f"ollama pull {d.get('tag')}",
                    "repo": d.get("repo"), "rel": (re.search(r"\d{4}-\d{2}-\d{2}", str(v.get("released") or "")) or [""])[0],
                    "lic": cut(str(v.get("license") or ""), 28)})
    return out


def models(vs):
    """Modellszintű összesítés + kutatási metaadatok."""
    fr = {slug(m.get("id")): m for m in load_blocks(os.path.join(HERE, "research/llm_frontier.md.txt"))[0]}
    un = load_blocks(os.path.join(HERE, "research/llm_uncensored_runtimes.md.txt"))[0]
    unm = {m["name"]: m for m in un}
    groups = {}
    for v in vs:
        groups.setdefault(v["g"], []).append(v)
    out = []
    for g, L in groups.items():
        L.sort(key=lambda x: x["b"])
        h = L[0]
        aa = max(x["aa"] for x in L)
        meta = unm.get(h["m"]) if h["u"] else fr.get(g.replace("llm-", ""))
        extra = {}
        if h["u"] and meta:
            a, base, r, why, e = unc_estimate(slug(meta["name"]))
            extra = {"base": meta.get("base"), "base_aa": base, "ratio": r, "why": why, "repo": (meta.get("hf_repo") or "").split("huggingface.co/")[-1]}
        elif meta:
            extra = {"org": meta.get("org"), "params": str(meta.get("params_total") or "")[:60], "active": str(meta.get("params_active") or "")[:40],
                     "ctx": meta.get("context"), "repo": (meta.get("hf_repo") or "").split("huggingface.co/")[-1],
                     "strength": str(meta.get("strengths_hu") or "")[:300]}
        out.append({"g": g, "m": h["m"], "u": h["u"], "aa": aa, "est": any(x["est"] for x in L), "n": len(L),
                    "minb": L[0]["b"], "maxb": L[-1]["b"], "plats": sorted({x["plat"] for x in L}),
                    "hw": sorted({t for x in L for t in x["hw"]}, key=lambda t: t), "rel": h["rel"], "lic": h["lic"],
                    "moe": h["moe"], "act": h["act"], **extra})
    out.sort(key=lambda x: -x["aa"])
    return out


CSS = r"""
:root{
  /* Elrendezés: műszerfal – felül a kalkulátor (a lap fő feladata), alatta eszközmátrix, legalul a teljes modelltábla. */
  --bg:#f3f4f2; --surface:#ffffff; --sunk:#e9ebe7; --ink:#1d2321; --muted:#5d6762; --line:#d4d8d3;
  --accent:#b4581a; --accent-ink:#ffffff; --accent-soft:#f6e3d4;
  --good:#2f7d4f; --warn:#a86b00; --bad:#b03a2e; --unc:#6b3fa0; --unc-soft:#ece3f6; --base:#22607a; --base-soft:#dcebf1;
  --bar:#22607a; --bar-bg:#e2e6e2;
  --c1:#b03a2e; --c2:#2f7d4f; --c3:#22607a; --c4:#b4581a; --c5:#7a7d22; --c6:#4a5fa8; --c7:#2a8a8a; --c8:#7a6a55; --c9:#c2185b; --c10:#6b3fa0; --c11:#8a8a8a; --c12:#00796b; --c13:#9e6b00;
  --f-display:"Bahnschrift","DIN Alternate","DIN 2014","Barlow Semi Condensed","Arial Narrow",ui-sans-serif,system-ui,sans-serif;
  --f-body:ui-sans-serif,system-ui,-apple-system,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif;
  --f-mono:ui-monospace,"SF Mono","Cascadia Mono","JetBrains Mono",Menlo,Consolas,monospace;
}
@media (prefers-color-scheme: dark){ :root:not([data-theme="light"]){
  --bg:#141816; --surface:#1c211f; --sunk:#232926; --ink:#e6ebe7; --muted:#9aa5a0; --line:#323a36;
  --accent:#e08a4c; --accent-ink:#1a1206; --accent-soft:#3a2617;
  --good:#5fbf86; --warn:#e0a83e; --bad:#ec7b6e; --unc:#b48cf0; --unc-soft:#2c2340; --base:#6cb6d4; --base-soft:#173039;
  --bar:#6cb6d4; --bar-bg:#2a322e;
  --c1:#ef7f72; --c2:#6fd096; --c3:#7cc4e2; --c4:#f0a066; --c5:#cfd36a; --c6:#9fb0f5; --c7:#5fd6d6; --c8:#c9b58f; --c9:#f48fb1; --c10:#c9a3f5; --c11:#bdbdbd; --c12:#4fd1b8; --c13:#e8c15a;
  color-scheme:dark }}
:root[data-theme="dark"]{
  --bg:#141816; --surface:#1c211f; --sunk:#232926; --ink:#e6ebe7; --muted:#9aa5a0; --line:#323a36;
  --accent:#e08a4c; --accent-ink:#1a1206; --accent-soft:#3a2617;
  --good:#5fbf86; --warn:#e0a83e; --bad:#ec7b6e; --unc:#b48cf0; --unc-soft:#2c2340; --base:#6cb6d4; --base-soft:#173039;
  --bar:#6cb6d4; --bar-bg:#2a322e;
  --c1:#ef7f72; --c2:#6fd096; --c3:#7cc4e2; --c4:#f0a066; --c5:#cfd36a; --c6:#9fb0f5; --c7:#5fd6d6; --c8:#c9b58f; --c9:#f48fb1; --c10:#c9a3f5; --c11:#bdbdbd; --c12:#4fd1b8; --c13:#e8c15a;
  color-scheme:dark }
*{box-sizing:border-box}
body{background:var(--bg);color:var(--ink);font:15px/1.5 var(--f-body);margin:0}
.wrap{max-width:1320px;margin:0 auto;padding-block:20px 60px;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px));display:grid;gap:28px}
h1,h2,h3{font-family:var(--f-display);text-wrap:balance;margin:0;letter-spacing:.01em}
h1{font-size:clamp(26px,3.4vw,38px);font-weight:700}
h2{font-size:22px;font-weight:700}
h3{font-size:16px;font-weight:700}
p{margin:0;max-width:75ch}
.muted{color:var(--muted)}
.eyebrow{font:600 11px/1 var(--f-body);letter-spacing:.12em;text-transform:uppercase;color:var(--muted)}
header.top{display:grid;gap:10px}
.refs{display:flex;flex-wrap:wrap;gap:8px}
.chip{display:inline-flex;align-items:center;flex-wrap:wrap;gap:4px 6px;padding:3px 9px;border-radius:999px;border:1px solid var(--line);background:var(--surface);font-size:12.5px;max-width:100%}
.mcell .chip,.vcard .chip,td .chip{white-space:nowrap}
.chip b{font-variant-numeric:tabular-nums}
.chip.u{background:var(--unc-soft);border-color:transparent;color:var(--unc)}
.chip.a{background:var(--base-soft);border-color:transparent;color:var(--base)}
.chip.est{border-style:dashed}
nav.tabs{display:flex;gap:6px;flex-wrap:nowrap;overflow-x:auto;position:sticky;top:env(safe-area-inset-top,0px);z-index:5;background:var(--bg);padding-block:8px;border-bottom:1px solid var(--line)}
nav.tabs{scrollbar-width:none}
nav.tabs::-webkit-scrollbar{display:none}
nav.tabs a{white-space:nowrap;flex:none;font:600 13px var(--f-body);color:var(--ink);text-decoration:none;padding:6px 12px;border-radius:6px}
nav.tabs a:hover,nav.tabs a:focus-visible{background:var(--sunk);outline:none}
body::before{content:"";position:fixed;inset:0 0 auto;height:env(safe-area-inset-top,0px);z-index:10;background:var(--bg)}
section{display:grid;gap:14px;scroll-margin-top:60px}
.calc{display:grid;grid-template-columns:minmax(0,360px) minmax(0,1fr);gap:20px;align-items:start}
.calc>*{min-width:0}
@media (max-width:900px){.calc{grid-template-columns:minmax(0,1fr)}}
form.dev{background:var(--surface);border:1px solid var(--line);border-radius:10px;padding:16px;display:grid;gap:12px}
fieldset{border:0;margin:0;padding:0;display:grid;gap:8px}
legend{font:600 11px var(--f-body);letter-spacing:.1em;text-transform:uppercase;color:var(--muted);margin-bottom:4px}
.row{display:grid;grid-template-columns:1fr 1fr;gap:8px}
.row3{display:grid;grid-template-columns:1fr 1fr 1fr;gap:8px}
label{display:grid;gap:3px;font-size:12.5px;color:var(--muted)}
.row>label,.row3>label{align-content:end}
details.adv{background:none;border:0;padding:0}
details.adv>summary{font:600 11px var(--f-body);letter-spacing:.1em;text-transform:uppercase;color:var(--muted);margin-bottom:6px}
details.adv>fieldset{margin-top:6px}
input,select{font:14px var(--f-body);padding:7px 8px;border:1px solid var(--line);border-radius:6px;background:var(--bg);color:var(--ink);width:100%;min-width:0}
input:focus-visible,select:focus-visible,button:focus-visible{outline:2px solid var(--accent);outline-offset:1px}
.checks{display:flex;flex-wrap:wrap;gap:10px 14px}
.checks label{display:flex;align-items:center;gap:6px;color:var(--ink);font-size:13px}
.checks input{width:auto}
button{font:600 13px var(--f-body);border-radius:6px;border:1px solid var(--line);background:var(--surface);color:var(--ink);padding:7px 12px;cursor:pointer}
button.primary{background:var(--accent);color:var(--accent-ink);border-color:var(--accent)}
.hint{font-size:12px;color:var(--muted)}
.results{display:grid;gap:12px;min-width:0}
.sum{display:flex;flex-wrap:wrap;gap:8px 18px;font-size:13px;color:var(--muted)}
.sum b{color:var(--ink);font-variant-numeric:tabular-nums}
.vcards{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px}
@media (max-width:700px){.vcards{grid-template-columns:minmax(0,1fr)}}
.vcard{background:var(--surface);border:1px solid var(--line);border-radius:10px;padding:14px;display:grid;grid-template-columns:minmax(0,1fr);gap:10px;align-content:start;min-width:0}
.vcard>*{min-width:0}
.vcard header{display:flex;justify-content:space-between;gap:8px;align-items:baseline}
.vtag{font:700 12px var(--f-display);letter-spacing:.06em;padding:2px 7px;border-radius:4px;background:var(--sunk)}
.vtag.u{background:var(--unc-soft);color:var(--unc)}
.member{display:grid;grid-template-columns:minmax(0,1fr);gap:5px;padding-top:8px;border-top:1px dashed var(--line);min-width:0}
.member:first-of-type{border-top:0;padding-top:0}
.mname{font-weight:700;overflow-wrap:anywhere}
.role{font-size:12px;color:var(--muted)}
.kv{display:flex;flex-wrap:wrap;gap:4px 12px;font-size:12.5px;font-variant-numeric:tabular-nums;min-width:0}
.kv span{white-space:nowrap}
.kv span.q{white-space:normal;overflow-wrap:anywhere;flex-basis:100%;color:var(--muted)}
.meter{display:grid;grid-template-columns:minmax(0,1fr) auto;gap:8px;align-items:center}
.meter .track{height:8px;border-radius:4px;background:var(--bar-bg);overflow:hidden;position:relative}
.meter .fill{height:100%;background:var(--bar);border-radius:4px}
.meter .fill.u{background:var(--unc)}
.meter .val{font:700 13px var(--f-mono);font-variant-numeric:tabular-nums}
code.cmd{display:block;font:12px/1.45 var(--f-mono);background:var(--sunk);padding:7px 9px;border-radius:6px;white-space:pre-wrap;word-break:break-all;max-width:100%}
.cmdrow{display:grid;grid-template-columns:minmax(0,1fr) auto;gap:6px;align-items:start}
.cmdrow button{padding:5px 8px;font-size:12px}
.empty{color:var(--muted);font-size:13px}
.tablebox{overflow-x:auto;border:1px solid var(--line);border-radius:10px;background:var(--surface)}
table{border-collapse:collapse;width:100%;font-size:13px}
th,td{padding:7px 10px;border-bottom:1px solid var(--line);text-align:left;vertical-align:top}
th{position:sticky;top:0;background:var(--sunk);font:600 12px var(--f-body);white-space:nowrap;z-index:1}
#models th button{all:unset;cursor:pointer;display:inline-block}
#models th button:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
#models td.date{white-space:nowrap}
.soft td{vertical-align:top}.soft .sd{font-size:.86em;color:var(--muted);max-width:420px}.soft td:first-child{min-width:160px}
#models td.det{max-width:380px}
#models td.det div{display:-webkit-box;-webkit-line-clamp:4;-webkit-box-orient:vertical;overflow:hidden}
th[aria-sort="ascending"]::after{content:" ▲"} th[aria-sort="descending"]::after{content:" ▼"}
td.num,th.num{text-align:right;font-variant-numeric:tabular-nums;white-space:nowrap}
tr:hover td{background:color-mix(in srgb,var(--sunk) 60%,transparent)}
.pctcell{display:grid;grid-template-columns:52px 70px;gap:6px;align-items:center;justify-content:end}
.pctcell .track{height:6px;border-radius:3px;background:var(--bar-bg);overflow:hidden}
.pctcell .fill{height:100%;background:var(--bar)}
.pctcell .fill.u{background:var(--unc)}
.filters{display:flex;flex-wrap:wrap;gap:10px;align-items:end}
.filters label{min-width:140px}
.matrix td{min-width:200px}
@media (max-width:700px){
  .matrix thead{display:none}
  .matrix tr{display:grid;gap:6px;padding:10px 0;border-bottom:1px solid var(--line)}
  .matrix td{display:block;min-width:0;border:0;padding:2px 10px}
  .matrix td[data-l]::before{content:attr(data-l);display:block;font:600 11px var(--f-body);letter-spacing:.08em;text-transform:uppercase;color:var(--muted);margin-bottom:2px}
  #ssd td.num:nth-child(n+4),#ssd th.num:nth-child(n+4){display:none}
  #ssd td:nth-child(4){min-width:160px!important}
}
.matrix td.dev{min-width:180px;font-weight:600}
.mcell{display:grid;gap:3px}
.mcell small{color:var(--muted)}
details{background:var(--surface);border:1px solid var(--line);border-radius:10px;padding:12px 14px}
details summary{cursor:pointer;font-weight:600}
details .body{display:grid;gap:8px;margin-top:10px;font-size:14px}
ul{margin:0;padding-left:20px;display:grid;gap:4px}
a{color:var(--base)}
footer{font-size:12px;color:var(--muted)}
.stack{display:flex;height:14px;border-radius:4px;overflow:hidden;background:var(--bar-bg)}
.stack span{display:block;height:100%;box-shadow:inset -1px 0 var(--surface)}
.legend{display:flex;flex-wrap:wrap;gap:6px 14px;font-size:12px;color:var(--muted)}
.legend .lg{display:inline-flex;align-items:center;gap:5px}
.legend i{display:inline-block;width:10px;height:10px;border-radius:2px}
@media (prefers-reduced-motion: reduce){*{transition:none!important;animation:none!important}}
"""

JS = r"""
const EFF=0.6, EMBED_GB=0.8, OPUS=__OPUS__;
const V=__VARIANTS__, M=__MODELS__, PRESETS=__PRESETS__;
const FAMS=["deepseek-v4-1","glm-5-3-flash","glm-5-3","qwen3-8-flash-next","qwen3-8-27b","qwen3-8-2-4t","kimi-k3","minimax-m3-1","gemma-4","qwen3-5","qwen3-6","gpt-oss","mistral","nemotron","mimo","ling","step-5","inkling","hy4","muse","longcat"];
const $=s=>document.querySelector(s), fmt=(x,d=1)=>Number(x).toLocaleString('hu-HU',{maximumFractionDigits:d,minimumFractionDigits:d});
const gb=b=>b>=1e12?fmt(b/1e12,2)+' TB':fmt(b/1e9,1)+' GB';
const pct=a=>Math.round(100*a/OPUS);
function qf(bits,moe){ if(moe!==false) return bits<2?0.55:bits<3?0.75:bits<4?0.9:bits<5?1.0:bits<7?1.03:1.05;
  return bits<2?0.15:bits<3?0.6:bits<4?0.85:bits<5?1.0:bits<7?1.03:1.05;}
const smart=v=>v.aa*qf(v.bits,v.moe);
const unusableQ=v=>v.moe===false&&v.bits<2.5;
const usable=(v,t,mn)=>smart(v)*(1+Math.min(0.2,0.05*Math.max(0,Math.log2(t/mn))));
function tpFractions(gpus,need){const n=gpus.length,frac=new Array(n).fill(0),free=new Set([...Array(n).keys()]);let rest=need;
  while(free.size&&rest>1e-9){const tot=[...free].reduce((s,i)=>s+gpus[i][1],0);const capped=[...free].filter(i=>rest*gpus[i][1]/tot>gpus[i][0]);
    if(!capped.length){for(const i of free) frac[i]=rest*gpus[i][1]/tot/need;break;}
    for(const i of capped){frac[i]=gpus[i][0]/need;rest-=gpus[i][0];free.delete(i);}}
  return frac;}
class Device{constructor(k){
  this.name=k.name||'Saját eszköz'; this.note=k.note||'';
  let gpus=k.gpus||(k.vram?[[k.vram,k.vram_bw]]:[]); const m=k.vram_bw_mult||1; gpus=gpus.map(([g,b])=>[g,b*m]);
  this.gpus=gpus; this.tp=!!k.tensor_parallel; this.tp_eff=k.tp_eff||0.85;
  this.vram=gpus.reduce((s,[g])=>s+g,0); this.vram_bw=gpus.length?this.vram/gpus.reduce((s,[g,b])=>s+g/b,0):0;
  this.ram=(k.ram||0)*(k.ram_usable??0.85); this.ram_bw=k.ram_bw||0; this.nodes=k.nodes||1; this.hop_ms=k.hop_ms||0;
  this.uni=(k.unified||0)*(k.unified_usable??0.8)*this.nodes; this.uni_bw=k.unified_bw||0;
  this.formats=new Set((k.formats||'any').split(',')); this.fix_ms=k.fix_ms??10; this.min_tps=k.min_tps??5;}
  capacity(){return Math.max(this.uni,this.vram+this.ram,this.vram,this.ram);}
  run(v,left,vramUsed=0){const fmtp=v.plat; if(!this.formats.has(fmtp)) return null;
    const need=v.b/1e9*1.15+1, cap=left??this.capacity(); if(need>cap+1e-9) return null;
    const act=(v.act||30)*1e9*v.bits/8, fix=this.fix_ms/1000, o=[];
    if(this.uni&&need<=Math.min(this.uni,cap)&&fmtp!=='server'){const hops=this.nodes>1?Math.max(0,Math.ceil(need/(this.uni/this.nodes))-1):0;
      const t=act/(EFF*this.uni_bw*1e9)+fix+hops*this.hop_ms/1000; o.push([1/t,'unified'+(this.nodes>1?' ×'+this.nodes:'')]);}
    const vram=Math.max(0,this.vram-vramUsed), gpus=this.vram?this.gpus.map(([g,b])=>[g*vram/this.vram,b]):[];
    if(vram&&need<=vram){let bw=this.vram_bw,how='csak GPU';
      if(this.tp&&gpus.length>1){const fr=tpFractions(gpus,need); const tRel=Math.max(...fr.map((f,i)=>f/gpus[i][1])); const bwTp=this.tp_eff/tRel;
        if(bwTp>bw){bw=bwTp;how='csak GPU, tensor parallel ×'+this.gpus.length+' (P2P)';}}
      o.push([1/(act/(EFF*bw*1e9)+fix),how]);}
    if(fmtp!=='server'&&this.ram&&need<=vram+this.ram&&need>vram){const share=Math.max(0,(vram-2)/need);
      const f=vram>2?Math.min(1,v.moe!==false?0.3+0.7*share:share):0; const t=(f?act*f/(EFF*this.vram_bw*1e9):0)+act*(1-f)/(EFF*this.ram_bw*1e9)+fix;
      o.push([1/t,(f?'hibrid GPU+RAM':'csak CPU')+(v.moe!==false?'':' (dense)')]);}
    if(fmtp!=='server'&&this.ram&&need<=this.ram&&!this.uni) o.push([1/(act/(EFF*this.ram_bw*1e9)+fix),'csak CPU']);
    if(!o.length) return null; o.sort((a,b)=>b[0]-a[0]); return [o[0][0],o[0][1],need];}}
function bestSingle(dev,unc){let best=null; const all=[];
  for(const v of V){ if(v.u!==unc||unusableQ(v)) continue; const r=dev.run(v); if(!r||r[0]<dev.min_tps) continue;
    const key=usable(v,r[0],dev.min_tps); all.push([key,v,r]); if(!best||key>best[0]||(key===best[0]&&r[0]>best[2][0])) best=[key,v,r];}
  if(!best) return null; const out=[[best[1],best[2],'egyedül']], seen=new Set([best[1].f]);
  all.sort((a,b)=>b[0]-a[0]); for(const [k,v,r] of all){ if(out.length>=3) break; if(!seen.has(v.f)&&k>=0.95*best[0]){out.push([v,r,'közel azonos alternatíva']);seen.add(v.f);} }
  return out;}
function team(dev,mixed){const cap=dev.capacity()-EMBED_GB;
  let c=V.filter(v=>!unusableQ(v)).map(v=>[v,dev.run(v)]).filter(([v,r])=>r&&r[0]>=dev.min_tps);
  if(!mixed) c=c.filter(([v])=>!v.u);
  c.sort((a,b)=>usable(b[0],b[1][0],dev.min_tps)-usable(a[0],a[1][0],dev.min_tps));
  const hTps=Math.min(20,2*dev.min_tps+2), hMax=Math.max(4,Math.min(40,0.3*cap)); let best=null;
  const vramOf=r=>r[1].startsWith('csak GPU')?Math.min(r[2],dev.vram):r[1].startsWith('hibrid')?dev.vram:0;
  for(const [v1,r1] of c.slice(0,80)){const left=cap-r1[2];
    for(const [v2,_r2] of c){ if(v2.g===v1.g||_r2[2]>left) continue;
      const r2=dev.run(v2,left,vramOf(r1)); if(!r2||r2[0]<dev.min_tps) continue;
      if(mixed&&v1.u===v2.u) continue;
      if(!mixed&&(r2[0]<Math.max(hTps,1.2*r1[0])||r2[2]>hMax||v2.bits<3.5)) continue;
      if(mixed&&v2.bits<3.5&&v2.moe===false) continue;
      const w=(mixed?0.35:0.25)*(v1.f===v2.f?0.6:1); const s=usable(v1,r1[0],dev.min_tps)+w*usable(v2,r2[0],dev.min_tps);
      if(!best||s>best[0]) best=[s,[[v1,r1,'fő modell'],[v2,r2,mixed?('partner ('+(v2.u?'cenzúrázatlan':'alap')+')'):'gyors segéd / router']]];}}
  if(best&&mixed){const used=best[1].reduce((s,m)=>s+m[1][2],0), groups=new Set(best[1].map(m=>m[0].g)); let h=null;
    const vu=best[1].reduce((s,m)=>s+vramOf(m[1]),0);
    for(const [v,_r] of c){ const r=dev.run(v,cap-used,vu); if(!r||groups.has(v.g)||r[2]>cap-used||r[0]<Math.max(hTps,1.5*best[1][0][1][0])||v.bits<3.5||r[2]>hMax) continue; if(!h||smart(v)>smart(h[0])) h=[v,r];}
    if(h) best[1].push([h[0],h[1],'gyors segéd / router']);}
  if(best) return best[1];
  const singles=c.filter(([v])=>mixed||!v.u); if(!singles.length) return null; const [v1,r1]=singles[0];
  let pool=singles.filter(([v])=>v.g!==v1.g&&v.bits>=3.5);
  if(mixed){pool=pool.filter(([v])=>v.u!==v1.u); pool.sort((a,b)=>usable(b[0],b[1][0],dev.min_tps)-usable(a[0],a[1][0],dev.min_tps));}
  else{const fast=pool.filter(([,r])=>r[0]>=1.5*r1[0]); pool=fast.length?fast:pool; pool.sort((a,b)=>b[1][0]-a[1][0]||smart(b[0])-smart(a[0]));}
  if(!pool.length) return null; const [v2,r2]=pool[0];
  return [[v1,r1,'fő modell (váltva)'],[v2,r2,(mixed?'partner':'gyors segéd')+', váltva – egyszerre csak egy fér a memóriába']];}
function evaluate(dev){return {V1:bestSingle(dev,true),V2:bestSingle(dev,false),V3:team(dev,false),V4:team(dev,true)};}
const TITLES={V1:['V1','Legokosabb cenzúrázatlan',1],V2:['V2','Legokosabb alap (cenzúrázott)',0],V3:['V3','Csapat – alap modellek',0],V4:['V4','Vegyes csapat – alap + cenzúrázatlan',1]};
function esc(s){return String(s??'').replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));}
function meter(aa,u,est){const p=Math.min(110,100*aa/OPUS);return `<div class="meter" title="AA v5 ${fmt(aa)} / Opus 5.5 ${OPUS}"><div class="track"><div class="fill${u?' u':''}" style="width:${Math.min(100,p)}%"></div></div><span class="val">${est?'~':''}${pct(aa)}%</span></div>`;}
function memberHTML([v,r,role]){return `<div class="member"><div class="mname">${esc(v.m)}</div><div class="role">${esc(role)} · <span class="chip ${v.u?'u':'a'}">${v.u?'cenzúrázatlan':'alap'}</span></div>
  ${meter(v.aa,v.u,v.est)}
  <div class="kv"><span>AA v5 <b>${v.est?'~':''}${fmt(v.aa)}</b></span><span class="q">${esc(v.q)}</span><span><b>${fmt(v.bits,1)}</b> bit</span><span>fájl <b>${gb(v.b)}</b></span><span>memória <b>${fmt(r[2],0)} GB</b></span><span>~<b>${fmt(r[0],0)}</b> tok/s</span><span>${esc(r[1])}</span><span>${v.act?(v.moe!==false?'MoE, ':'dense, ')+fmt(v.act,1)+'B aktív':''}</span></div>
  <div class="cmdrow"><code class="cmd">${esc(v.dl)}</code><button type="button" data-copy="${esc(v.dl)}">Másolás</button></div></div>`;}
function render(dev,res,el){const cap=dev.capacity();
  if(cap<=0){el.innerHTML='<p class="empty">Adj meg VRAM-ot, RAM-ot vagy unified memóriát (és a hozzá tartozó sávszélességet), vagy válassz egy eszközprofilt.</p>';return;}
  el.innerHTML=`<div class="sum"><span>Eszköz: <b>${esc(dev.name)}</b></span><span>Modellnek jutó memória: <b>~${fmt(cap,cap<20?1:0)} GB</b></span>${dev.vram?`<span>VRAM: <b>${fmt(dev.vram,0)} GB</b> @ <b>${fmt(dev.vram_bw,0)} GB/s</b>${dev.tp?' (P2P tensor parallel)':''}</span>`:''}${dev.uni?`<span>Unified: <b>${fmt(dev.uni,dev.uni<20?1:0)} GB</b> @ <b>${fmt(dev.uni_bw,0)} GB/s</b></span>`:''}${dev.ram&&!dev.uni?`<span>RAM: <b>${fmt(dev.ram,0)} GB</b> @ <b>${fmt(dev.ram_bw,0)} GB/s</b></span>`:''}<span>Min. sebesség: <b>${dev.min_tps} tok/s</b></span></div>
  ${dev.note?`<p class="hint">${esc(dev.note)}</p>`:''}
  <div class="vcards">${['V1','V2','V3','V4'].map(k=>{const [t,label,u]=TITLES[k],r=res[k];
    const total=r&&r.length>1&&!String(r[0][2]).includes('váltva')?`<p class="hint">Együtt a memóriában: ~${fmt(r.reduce((s,m)=>s+m[1][2],0)+EMBED_GB,0)} GB (+ bge-m3 RAG-embedding 0,6 GB)</p>`:'';
    return `<article class="vcard"><header><h3>${label}</h3><span class="vtag${u?' u':''}">${t}</span></header>${r?r.map(memberHTML).join(''):'<p class="empty">Nincs olyan modell, ami elfér és eléri a minimális sebességet.</p>'}${total}</article>`;}).join('')}</div>`;}
/* ---------- űrlap ---------- */
const F=id=>document.getElementById(id);
function fillPresetSelect(){const s=F('preset'); s.innerHTML='<option value="">— saját adatok —</option>'+Object.entries(PRESETS).map(([k,p])=>`<option value="${k}">${esc(p.name)}</option>`).join('');}
function presetToForm(k){const p=PRESETS[k]; if(!p) return; const g=p.gpus||(p.vram?[[p.vram,p.vram_bw]]:[]);
  F('g1gb').value=g[0]?.[0]??''; F('g1bw').value=g[0]?.[1]??''; F('g2gb').value=g[1]?.[0]??''; F('g2bw').value=g[1]?.[1]??'';
  F('ram').value=p.ram??''; F('ramu').value=Math.round((p.ram_usable??0.85)*100); F('rambw').value=p.ram_bw??'';
  F('uni').value=p.unified??''; F('uniu').value=Math.round((p.unified_usable??0.8)*100); F('unibw').value=p.unified_bw??'';
  F('nodes').value=p.nodes??1; F('hop').value=p.hop_ms??3; F('mintps').value=p.min_tps??5; F('fixms').value=p.fix_ms??10;
  F('oc').value=Math.round(((p.vram_bw_mult??1)-1)*100); F('tp').checked=!!p.tensor_parallel; F('tpeff').value=Math.round((p.tp_eff??0.85)*100);
  for(const f of ['any','mac','server','android']) F('fmt_'+f).checked=(p.formats||'any').split(',').includes(f);
  F('dname').value=p.name;}
function formToDevice(){const n=(id,def=0,min=0,max=1e7)=>{const x=parseFloat(F(id).value);return Number.isFinite(x)?Math.min(max,Math.max(min,x)):def;}; const gpus=[]; if(n('g1gb')&&n('g1bw')) gpus.push([n('g1gb'),n('g1bw')]); if(n('g2gb')&&n('g2bw')) gpus.push([n('g2gb'),n('g2bw')]);
  const k=F('preset').value?PRESETS[F('preset').value]:{};
  return new Device({name:F('dname').value||'Saját eszköz',note:k.note&&F('preset').dataset.dirty!=='1'?k.note:'',gpus,ram:n('ram'),ram_usable:n('ramu',85,10,100)/100,ram_bw:n('rambw'),
    unified:n('uni'),unified_usable:n('uniu',80,10,100)/100,unified_bw:n('unibw'),nodes:n('nodes',1,1,16),hop_ms:n('hop',3,0,1000),
    formats:['any','mac','server','android'].filter(f=>F('fmt_'+f).checked).join(',')||'any',min_tps:n('mintps',5,0.5,1000),fix_ms:n('fixms',10,0,1000),
    vram_bw_mult:1+n('oc',0,0,30)/100,tensor_parallel:F('tp').checked,tp_eff:n('tpeff',85,30,100)/100});}
function calc(){const d=formToDevice(); render(d,evaluate(d),F('out'));}
/* ---------- eszközmátrix ---------- */
function matrix(){const rows=Object.entries(PRESETS).map(([k,p])=>{const d=new Device(p),r=evaluate(d);
  const cell=x=>x?x.filter(m=>!String(m[2]).includes('alternatíva')).map(([v,rr,role])=>`<div class="mcell"><span><span class="chip ${v.u?'u':'a'}">${v.est?'~':''}${pct(v.aa)}%</span> ${esc(v.m.replace(/\s*\(.*?\)/g,''))}</span><small>${esc((v.q.split(' · ')[0]||'').slice(0,40))} · ${fmt(v.bits,1)} bit · ${gb(v.b)} · ~${fmt(rr[0],0)} tok/s · ${esc(role)}</small></div>`).join(''):'<span class="empty">—</span>';
  return `<tr><td class="dev">${esc(p.name)}<br><small class="muted">~${fmt(d.capacity(),d.capacity()<20?1:0)} GB</small></td><td data-l="V1 cenzúrázatlan">${cell(r.V1)}</td><td data-l="V2 alap">${cell(r.V2)}</td><td data-l="V3 csapat">${cell(r.V3)}</td><td data-l="V4 vegyes csapat">${cell(r.V4)}</td></tr>`;}).join('');
  F('matrix').innerHTML=`<table class="matrix"><thead><tr><th>Eszköz</th><th>V1 – cenzúrázatlan</th><th>V2 – alap</th><th>V3 – csapat (alap)</th><th>V4 – vegyes csapat</th></tr></thead><tbody>${rows}</tbody></table>`;}
/* ---------- modelltábla ---------- */
let sortKey='aa',sortDir=-1;
const COLS=[['m','Modell',0],['u','Típus',0],['aa','AA v5',1],['pct','% Opus 5.5',1],['rel','Kiadva',0],['act','Aktív param.',1],['minb','Legkisebb',1],['maxb','Legnagyobb',1],['n','Kvant',1],['plats','Formátum',0],['hw','Gépszint',0],['lic','Licenc',0],['info','Részletek',0]];
function modelTable(){const q=F('mq').value.toLowerCase(), typ=F('mtyp').value, minp=parseFloat(F('mpct').value)||0, maxs=parseFloat(F('msize').value)||1e9;
  let L=M.filter(m=>(!q||m.m.toLowerCase().includes(q)||(m.repo||'').toLowerCase().includes(q))&&(typ===''||(typ==='u')===m.u)&&pct(m.aa)>=minp&&m.minb/1e9<=maxs);
  L.sort((a,b)=>{const k=sortKey,x=k==='pct'?a.aa:a[k],y=k==='pct'?b.aa:b[k];return (x>y?1:x<y?-1:0)*sortDir;});
  const th=COLS.map(([k,l,n])=>k==='info'?`<th>${l}</th>`:`<th class="${n?'num':''}" data-k="${k}" aria-sort="${sortKey===k?(sortDir>0?'ascending':'descending'):'none'}"><button type="button">${l}</button></th>`).join('');
  const tr=L.map(m=>`<tr><td><b>${esc(m.m)}</b>${m.repo?`<br><a href="https://huggingface.co/${esc(m.repo)}" target="_blank" rel="noopener">${esc(m.repo)}</a>`:''}</td>
    <td><span class="chip ${m.u?'u':'a'}">${m.u?'cenzúrázatlan':'alap'}</span></td><td class="num">${m.est?'~':''}${fmt(m.aa)}</td>
    <td class="num"><div class="pctcell"><div class="track"><div class="fill${m.u?' u':''}" style="width:${Math.min(100,100*m.aa/OPUS)}%"></div></div><span>${m.est?'~':''}${pct(m.aa)}%</span></div></td>
    <td class="date">${esc(m.rel)}</td><td class="num">${m.act?fmt(m.act,1)+'B '+(m.moe!==false?'MoE':'dense'):'?'}</td><td class="num">${gb(m.minb)}</td><td class="num">${gb(m.maxb)}</td><td class="num">${m.n}</td>
    <td>${m.plats.map(p=>({any:'GGUF',mac:'MLX',server:'vLLM',android:'LiteRT'}[p]||p)).join(', ')}</td><td>${esc(m.hw.join(' '))}</td><td>${esc(m.lic)}</td>
    <td class="det" style="min-width:260px"><div title="${esc(m.u?(m.why||''):(m.strength||''))}">${m.u?`alap: ${esc(m.base||'')} (AA ${fmt(m.base_aa)}) × ${fmt(m.ratio,3)} – ${esc(m.why||'')}`:esc(m.strength||'')}</div></td></tr>`).join('')||'<tr><td colspan="13" class="empty">Nincs a szűrésnek megfelelő modell.</td></tr>';
  F('models').innerHTML=`<table><thead><tr>${th}</tr></thead><tbody>${tr}</tbody></table>`; F('mcount').textContent=L.length+' modell';
  F('models').querySelectorAll('th[data-k]').forEach(t=>t.addEventListener('click',()=>{const k=t.dataset.k; if(sortKey===k) sortDir*=-1; else {sortKey=k; sortDir=['m','rel','lic','u'].includes(k)?1:-1;} modelTable();}));}
/* ---------- szoftverek és modellek ---------- */
const S=__SOFT__;
function softTable(){const q=F('sq').value.toLowerCase(), c=F('scat').value;
  const L=S.filter(x=>(!c||x.c===c)&&(!q||(x.n+' '+x.need+' '+x.d+' '+x.alt).toLowerCase().includes(q)));
  const link=(u,l)=>u?`<a href="${esc(u)}" target="_blank" rel="noopener">${l}</a>`:'';
  const tr=L.map(x=>`<tr><td>${esc(x.need)}<br><small class="muted">${esc(x.c)}</small></td><td><b>${esc(x.n)}</b><div class="sd">${esc(x.d)}</div><small>${[link(x.w,'web'),link(x.r,'repó'),link(x.rel,'letöltés')].filter(Boolean).join(' · ')}</small></td>
    <td class="num">${x.t}</td><td>${esc(x.v)||'–'}</td><td>${esc(x.lic)}</td><td class="num">${x.b?gb(x.b):'–'}</td><td class="sd">${esc(x.alt)||'–'}</td></tr>`).join('')||'<tr><td colspan="7" class="empty">Nincs találat.</td></tr>';
  F('soft').innerHTML=`<table class="soft"><thead><tr><th>Igény</th><th>Legjobb választás</th><th class="num">Tier</th><th>Verzió</th><th>Licenc</th><th class="num">Méret</th><th>Alternatívák</th></tr></thead><tbody>${tr}</tbody></table>`;
  F('scount').textContent=L.length+' tétel';}
(()=>{const sel=F('scat'); [...new Set(S.map(x=>x.c))].sort((a,b)=>a.localeCompare(b,'hu')).forEach(c=>sel.add(new Option(c,c))); F('sq').addEventListener('input',softTable); sel.addEventListener('change',softTable); softTable();})();
/* ---------- indítás ---------- */
document.addEventListener('click',e=>{const b=e.target.closest('button[data-copy]'); if(!b) return; const t=b.dataset.copy;
  const done=()=>{b.textContent='Másolva';setTimeout(()=>b.textContent='Másolás',1500)};
  const sel=()=>{const c=b.previousElementSibling;const r=document.createRange();r.selectNodeContents(c);const s=getSelection();s.removeAllRanges();s.addRange(r);b.textContent='Kijelölve – Ctrl+C';setTimeout(()=>b.textContent='Másolás',2500);};
  if(navigator.clipboard?.writeText) navigator.clipboard.writeText(t).then(done).catch(sel); else sel();});
fillPresetSelect();
F('preset').addEventListener('change',()=>{F('preset').dataset.dirty='0'; if(!F('preset').value){F('dname').value='Saját eszköz';} else presetToForm(F('preset').value); calc();});
F('devform').addEventListener('input',e=>{if(e.target.id!=='preset'&&e.target.id!=='dname'&&F('preset').dataset.dirty!=='1'){F('preset').dataset.dirty='1'; if(F('preset').value&&!/módosítva\)$/.test(F('dname').value)) F('dname').value=F('dname').value+' (módosítva)';} calc();});
if(window.matchMedia&&matchMedia('(max-width:900px)').matches) document.querySelectorAll('details.adv').forEach(d=>d.open=false);
F('devform').addEventListener('submit',e=>{e.preventDefault();calc();});
['mq','mtyp','mpct','msize'].forEach(id=>F(id).addEventListener('input',modelTable));
let start='__START__'; try{const s=localStorage.getItem('archivum-preset'); if(s&&PRESETS[s]) start=s;}catch(e){}
F('preset').value=start; presetToForm(start); calc(); matrix(); modelTable();
F('preset').addEventListener('change',()=>{try{localStorage.setItem('archivum-preset',F('preset').value)}catch(e){}});
"""

BODY = """<title>ARCHIVUM LLM-kalkulátor</title>
<meta name="claude:viewport-fit-sides" content="cover">
<style>__CSS__</style>
<div class="wrap">
<header class="top">
  <span class="eyebrow">ARCHIVUM · offline LLM-tervező · állapot: __DATE__</span>
  <h1>Melyik nyílt modell fut a gépeden – és milyen okos?</h1>
  <p class="muted">Add meg az eszközöd memóriáját és sávszélességét: a kalkulátor kiszámolja a legokosabb cenzúrázatlan és alap modellt, ami elfér és elfut, valamint a két csapat-változatot. Minden szám becslés (AA Intelligence Index v5 + memória-sávszélesség modell), lásd a módszertant alul. Internet nélkül is működik.</p>
  <div class="refs">
    <span class="chip">Claude Opus 5.5 (max) = <b>59,1</b> AA v5 = <b>100%</b></span>
    <span class="chip">Claude Fable 5.2 = <b>64,6</b> = <b>109%</b></span>
    <span class="chip a">Legjobb nyílt: Kimi K3.1 Pro <b>46,5 = 79%</b></span>
    <span class="chip u">Legjobb cenzúrázatlan: DeepSeek-V4.1-Flash abliterated <b>~31,6 = ~53%</b></span>
    <span class="chip est">~ = becsült érték</span>
  </div>
</header>
<nav class="tabs"><a href="#kalkulator">Kalkulátor</a><a href="#eszkozok">Eszközmátrix</a><a href="#modellek">Modelltábla</a><a href="#szoftverek">Szoftverek és modellek</a><a href="#ssd">SSD-tervező</a><a href="#modszertan">Módszertan</a><a href="#fogalmak">Fogalmak</a></nav>

<section id="kalkulator">
  <h2>Kalkulátor</h2>
  <div class="calc">
    <form class="dev" id="devform">
      <label>Eszközprofil<select id="preset"></select></label>
      <label>Név<input id="dname" type="text"></label>
      <fieldset><legend>Videokártya(k)</legend>
        <div class="row"><label>GPU 1 VRAM (GB)<input id="g1gb" type="number" min="0" step="1"></label><label>GPU 1 sávszél. (GB/s)<input id="g1bw" type="number" min="0" step="10"></label></div>
        <div class="row"><label>GPU 2 VRAM (GB)<input id="g2gb" type="number" min="0" step="1"></label><label>GPU 2 sávszél. (GB/s)<input id="g2bw" type="number" min="0" step="10"></label></div>
      </fieldset>
      <fieldset><legend>Rendszer-RAM (hibrid / CPU)</legend>
        <div class="row3"><label>RAM (GB)<input id="ram" type="number" min="0" step="1"></label><label>Használható %<input id="ramu" type="number" min="10" max="100"></label><label>Sávszél. (GB/s)<input id="rambw" type="number" min="0" step="1"></label></div>
      </fieldset>
      <details class="adv" open><summary>Unified memória (Mac, Strix Halo, telefon)</summary><fieldset>
        <div class="row3"><label>Memória (GB)<input id="uni" type="number" min="0" step="1"></label><label>GPU-nak jut %<input id="uniu" type="number" min="10" max="100"></label><label>Sávszél. (GB/s)<input id="unibw" type="number" min="0" step="1"></label></div>
        <div class="row"><label>Gépek száma (klaszter)<input id="nodes" type="number" min="1" max="16"></label><label>Hálózati késleltetés gépenként (ms)<input id="hop" type="number" min="0" step="0.5"></label></div>
      </fieldset></details>
      <details class="adv" open><summary>Feloldás / túlhajtás (GeForce)</summary><fieldset>
        <div class="row"><label>Memória-túlhajtás (+%)<input id="oc" type="number" min="0" max="30"></label><label>TP hatásfok (%)<input id="tpeff" type="number" min="30" max="100"></label></div>
        <div class="checks"><label><input id="tp" type="checkbox"> P2P + tensor parallel (két kártya párhuzamosan)</label></div>
      </fieldset></details>
      <details class="adv" open><summary>Formátumok és küszöb</summary><fieldset>
        <div class="checks"><label><input id="fmt_any" type="checkbox"> GGUF / Ollama</label><label><input id="fmt_mac" type="checkbox"> MLX (Mac/iPhone)</label><label><input id="fmt_server" type="checkbox"> vLLM / SGLang</label><label><input id="fmt_android" type="checkbox"> LiteRT</label></div>
        <div class="row"><label>Min. sebesség (tok/s)<input id="mintps" type="number" min="1" step="0.5"></label><label>Fix többletidő (ms/token)<input id="fixms" type="number" min="0" step="1"></label></div>
      </fieldset></details>
      <p class="hint">Sávszélesség-segítség: DDR4 2 csatorna ≈ 40–50, DDR5 2 csatorna ≈ 80–96, Apple M3 Ultra 819, Strix Halo ≈ 256–273, RTX 4090 1008, RTX 5090 1792 GB/s.</p>
    </form>
    <div class="results" id="out" aria-live="polite"></div>
  </div>
</section>

<section id="eszkozok">
  <h2>Eszközmátrix – a te gépeid, 4 változatban</h2>
  <p class="muted">Minden profil a kalkulátorral számolva. A százalék a modell AA v5 pontja az Opus 5.5-höz (59,1) képest; lila = cenzúrázatlan, kék = alap.</p>
  <div class="tablebox" id="matrix"></div>
</section>

<section id="modellek">
  <h2>Modelltábla – minden nyílt modell, alap és cenzúrázatlan</h2>
  <div class="filters">
    <label>Keresés<input id="mq" type="search" placeholder="pl. qwen, deepseek, heretic"></label>
    <label>Típus<select id="mtyp"><option value="">mind</option><option value="a">alap</option><option value="u">cenzúrázatlan</option></select></label>
    <label>Min. % Opus<input id="mpct" type="number" min="0" max="100" value="0"></label>
    <label>Legkisebb kvant ≤ (GB)<input id="msize" type="number" min="1" placeholder="pl. 24"></label>
    <span class="hint" id="mcount"></span>
  </div>
  <div class="tablebox" id="models"></div>
</section>

<section id="szoftverek">
  <h2>Mindenre a legjobb nyílt forráskódú szoftver, modell és adathalmaz</h2>
  <p class="muted">Igényenként a legjobb választás: GitHub/GitLab/Codeberg-repók (git ls-remote-tal ellenőrizve, 2026-11-14), Hugging Face-modellek és -adathalmazok (HF API-val ellenőrzött méret). A „Tier” 0 = életmentő … 5 = luxus.</p>
  <div class="filters">
    <label>Keresés<input id="sq" type="search" placeholder="pl. térkép, orvosi, rádió, whisper"></label>
    <label>Kategória<select id="scat"><option value="">mind</option></select></label>
    <span class="hint" id="scount"></span>
  </div>
  <div class="tablebox" id="soft"></div>
</section>

<section id="ssd">
  <h2>Hány TB-os SSD kell? – 1, 2, 4, 8, 16, 32 TB</h2>
  <p class="muted">Kiszámolt tartalom tárhelyenként (a teljes ARCHIVUM-katalógusból, balanced profil, T2-es LLM-gép ~300 GB memóriával, alap + cenzúrázatlan modellekkel). A sáv a meghajtó teljes kapacitásához viszonyít; 8% tartalék marad. Nyisd le a méretet a teljes listához.</p>
  __SSD__
  <details><summary>Melyik meghajtót vedd</summary><div class="body"><ul>
    <li><b>A gépben:</b> NVMe SSD (TLC, DRAM-cache, magas TBW). A modellek <b>betöltését</b> gyorsítja, a futásukat nem.</li>
    <li><b>Archív példány:</b> az SSD áram nélkül 1–3 évig tartja megbízhatóan az adatot (becslés). Hosszú távra HDD (CMR) vagy M-DISC kell; a HDD-t évente kapcsold be és ellenőrizd.</li>
    <li><b>3-2-1:</b> 3 példány, 2 különböző adathordozón, 1 máshol tárolva. Az életmentő anyag legyen kinyomtatva is.</li>
    <li><b>Fájlrendszer:</b> exFAT vagy ext4, <b>nem FAT32</b> (4 GB-os fájlméret-korlát).</li>
  </ul></div></details>
</section>

<section id="modszertan">
  <h2>Módszertan és feltételezések</h2>
  <details open id="fogalmak"><summary>Fogalmak</summary><div class="body"><ul>
    <li><b>V1</b> = legokosabb cenzúrázatlan modell · <b>V2</b> = legokosabb alap (cenzúrázott) modell · <b>V3</b> = alap fő modell + gyors segédmodell egyszerre · <b>V4</b> = alap + cenzúrázatlan modell együtt (+ segéd).</li>
    <li><b>AA v5</b> = Artificial Analysis Intelligence Index v5.0.1 (nehéz, részben titkos feladatsor). <b>% Opus</b> = a modell pontja a Claude Opus 5.5 (legmagasabb gondolkodási beállítás) 59,1 pontjához képest. 50% nem azt jelenti, hogy „fele olyan okos”: nehéz feladatoknál kb. a felét hozza, hétköznapiaknál jóval közelebb van.</li>
    <li><b>Gépszint:</b> T1 szerver (≥1 TB) · T2 workstation 256–1000 GB · T3 gamer PC 24–32 GB VRAM + RAM · T4 laptop · T5 telefon.</li>
    <li><b>tok/s</b> = token másodpercenként (magyar szövegnél kb. 0,5–0,7 szó/token). 5 tok/s még olvasható, 20+ tok/s kényelmes.</li>
    <li><b>Kvant</b> = tömörített modellváltozat; kevesebb bit → kisebb és gyorsabb, de butább (4–5 bit a jó kompromisszum). <b>GGUF</b> = mindenhol futó formátum (llama.cpp, Ollama), <b>MLX</b> = Apple, <b>vLLM</b> = NVIDIA-szerver formátum.</li>
    <li><b>MoE</b> = sok „szakértőből” álló modell, tokenenként csak egy részük dolgozik (aktív paraméter) → gyors; <b>dense</b> = minden paraméter dolgozik.</li>
  </ul></div></details>
  <details open><summary>Hogyan számol a kalkulátor</summary><div class="body"><ul>
    <li><b>Okosság:</b> Artificial Analysis Intelligence Index v5.0.1 (2026-11-12). Viszonyítás: Claude Opus 5.5 (max) 59,1 = 100%. Az AA a v5-ben megszüntette a külön Coding Indexet; a kódolás (FrontierCode 2.0 + Terminal-Bench 4.0) az összpont 25%-a.</li>
    <li><b>Cenzúrázatlan modellek:</b> alapmodell AA × (cenzúrázatlan / alap) arány. Az arány a UGI ranglista NatInt-méréséből jön, ahol van („M”), máshol becslés: nagy MoE 0,95–0,97, közösségi/nem ellenőrzött 0,93, kis dense 0,93.</li>
    <li><b>Kvantminőség:</b> MoE 1,7 bit ×0,55 · 2,6 bit ×0,75 · 3,5 bit ×0,9 · 4–5 bit ×1,0 · 6 bit ×1,03 · 8+ bit ×1,05. Dense modellek 2,5 bit alatt kizárva.</li>
    <li><b>Memória:</b> fájlméret × 1,15 + 1 GB (KV cache ~16–32k kontextus).</li>
    <li><b>Sebesség (1 felhasználó, generálás):</b> tok/s = 1 / (aktív bájt / (0,6 × sávszélesség) + fix ms). Hibridnél MoE-ra a figyelem ~30%-a a GPU-n. Több eltérő GPU rétegenként: harmonikus sávszélesség; P2P + tensor parallel: a sávszélességek összege × hatásfok. Klaszter: + késleltetés gépenként.</li>
    <li><b>Döntés:</b> a legokosabb nyer, kis sebesség-bónusszal (+5% duplázásonként, max +20%). V3: fő + gyors segéd (≤30% memória, ≥3,5 bit). V4: fő + másik cenzúra-típusú partner (+ segéd). Ha nem fér el egyszerre: váltott csapat.</li>
    <li><b>Ez becslés, nem mérés.</b> A valós sebesség a futtatótól (llama.cpp, ik_llama.cpp, vLLM, MLX), a kontextushossztól és a prompt-feldolgozástól függ.</li>
  </ul></div></details>
  <details><summary>Hardver-feltételezések</summary><div class="body"><ul>
    <li><b>RTX 6090:</b> nem bejelentett; pletyka: 32 GB GDDR7, ~1,79 TB/s. A „FELOLDVA” profilok: memória-túlhajtás ×1,06; két kártyánál P2P + tensor parallel (hatásfok 0,82). A 8× H200 profil a 8 GPU-t összevontan modellezi.</li>
    <li><b>Következő generációs RTX Pro:</b> nincs adat; három forgatókönyv: 96 / 128 / 192 GB.</li>
    <li><b>MS-S1 MAX-P495, ZBook Ultra G3a:</b> 192 GB LPDDR5X, a GPU-nak max. 160 GB; sávszélesség ~256–273 GB/s (számolt).</li>
    <li><b>HP Pavilion 15-bc504ur:</b> i5-9300H + GTX 1050 4 GB (a bc504TX testvérmodell adatlapja alapján).</li>
    <li><b>Telefonok:</b> S24 Ultra ~7,5 GB, iPhone 15 Pro ~5 GB jut a modellnek (becslés).</li>
  </ul></div></details>
</section>
<footer>ARCHIVUM · a teljes katalógus, letöltési receptek és a Python-kalkulátor: ARCHIVUM.md (6. és 12. fejezet). Generálva: __DATE__.</footer>
</div>
<script>__JS__</script>
"""


def software():
    from gen_sections import all_items
    from build import CAT_HU, hu
    out = []
    for i in all_items():
        if not i["id"].startswith(("oss-", "hub-")):
            continue
        d = i.get("download") or {}
        repo = (d.get("repos") or [None])[0] or (f"https://huggingface.co/{d['repo']}" if d.get("repo") else None) or d.get("url")
        out.append({"n": i["name"], "c": CAT_HU.get(i["cat"], i["cat"]), "need": hu(i.get("need_hu") or ""), "d": cut(i.get("desc_hu") or "", 260),
                    "v": i.get("latest_version") or "", "lic": cut(i.get("license") or "", 40), "b": i.get("bytes") or i.get("bytes_est") or 0,
                    "t": i["tier"], "w": i.get("info_url") or "", "r": repo or "", "rel": d.get("release_url") or "",
                    "alt": cut(hu(i.get("alternatives") or ""), 220)})
    out.sort(key=lambda x: (x["c"], x["t"], x["n"].lower()))
    return out


def ssd_html():
    import html as H
    P = json.load(open(os.path.join(HERE, "ssd_plans.json"), encoding="utf-8"))
    sys.path.insert(0, HERE)
    from build import CAT_GROUP
    sz = lambda i: (i.get("bytes") or i.get("bytes_est") or 0)
    def hb(b):
        t = f"{b/1e12:.2f} TB" if b >= 1e12 else (f"{b/1e9:.1f} GB" if b >= 1e9 else f"{b/1e6:.0f} MB")
        return t.replace(".", ",")
    groups = ["Életmentő: orvoslás, víz, élelem, túlélés", "Mezőgazdaság, megfelelő technológia, energia", "Lexikonok, szótárak", "Magyar források",
              "Mérnöki tudás, gyártás, kémia, elektronika", "Tudomány, oktatás, könyvtárak", "Térképek, geoadatok", "Szoftver, OS, forráskód",
              "Nyílt forráskódú szoftverek", "AI-modellek, adathalmazok, platformok",
              "LLM-ek (alap)", "LLM-ek (cenzúrázatlan)", "Olvasók, futtatók"]
    colors = [f"var(--c{i})" for i in range(1, 14)]
    rows, cards = [], []
    prev, prevg = set(), set()
    for b, items, used in P:
        tot = {g: 0 for g in groups}
        for i in items:
            tot[CAT_GROUP.get(i["cat"], "Olvasók, futtatók")] = tot.get(CAT_GROUP.get(i["cat"], "Olvasók, futtatók"), 0) + sz(i)
        cap = float(b.replace("TB", "")) * 1e12
        bar = "".join(f'<span title="{H.escape(g)}: {hb(tot[g])}" style="width:{100*tot[g]/cap:.2f}%;background:{c}"></span>' for g, c in zip(groups, colors) if tot[g])
        rows.append(f'<tr><td><b>{b.replace("TB", " TB")}</b></td><td class="num">{hb(used)}</td><td class="num">{len(items)}</td><td style="min-width:260px"><div class="stack">{bar}</div></td>'
                    + "".join(f'<td class="num">{hb(tot[g]) if tot[g] else "–"}</td>' for g in groups) + "</tr>")
        new = sorted([i for i in items if i["id"] not in prev and (i.get("group") or i["id"]) not in prevg], key=lambda i: -sz(i))
        by = {}
        for i in items:
            by.setdefault(CAT_GROUP.get(i["cat"], "Olvasók, futtatók"), []).append(i)
        det = "".join(f'<p><b>{H.escape(g)}</b> – {hb(sum(sz(i) for i in by[g]))}: ' + "; ".join(
            f'{H.escape(cut(i.get("name") or i["id"], 70))} <span class="muted">({hb(sz(i))})</span>' for i in sorted(by[g], key=lambda i: (i["tier"], -sz(i)))) + "</p>"
            for g in groups if g in by)
        cards.append(f'<details><summary><b>{b.replace("TB", " TB")} SSD</b> – {len(items)} tétel, {hb(used)}'
                     + (f' · új az előzőhöz képest: {H.escape("; ".join(cut(i.get("name") or i["id"], 45) for i in new[:4]))}' if new else '')
                     + f'</summary><div class="body">{det}</div></details>')
        prev = {i["id"] for i in items}; prevg = {i.get("group") or i["id"] for i in items}
    legend = "".join(f'<span class="lg"><i style="background:{c}"></i>{H.escape(g)}</span>' for g, c in zip(groups, colors))
    head = "".join(f'<th class="num">{H.escape(g.split(":")[0].split(",")[0])}</th>' for g in groups)
    return (f'<div class="legend">{legend}</div><div class="tablebox"><table><thead><tr><th>SSD</th><th class="num">Felhasználva</th><th class="num">Elem</th><th>Tartalom aránya</th>{head}</tr></thead>'
            f'<tbody>{"".join(rows)}</tbody></table></div>' + "".join(cards))


def main():
    vs = variants()
    ms = models(vs)
    presets = {k: dict(v) for k, v in llm_calc.PRESETS.items()}
    js = (JS.replace("__OPUS__", str(OPUS)).replace("__VARIANTS__", json.dumps(vs, ensure_ascii=False, separators=(",", ":")))
          .replace("__MODELS__", json.dumps(ms, ensure_ascii=False, separators=(",", ":"), default=str))
          .replace("__PRESETS__", json.dumps(presets, ensure_ascii=False, separators=(",", ":")))
          .replace("__SOFT__", json.dumps(software(), ensure_ascii=False, separators=(",", ":")))
          .replace("__START__", "gamer-pc-128" if "gamer-pc-128" in presets else next(iter(presets))))
    date = datetime.date.today().isoformat()
    frag = BODY.replace("__SSD__", ssd_html()).replace("__CSS__", CSS).replace("__JS__", js).replace("__DATE__", date)
    open(os.path.join(HERE, "..", "ARCHIVUM-LLM.fragment.html"), "w", encoding="utf-8").write(frag)
    full = ('<!doctype html>\n<html lang="hu">\n<head>\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n' +
            frag.replace("<style>", "<style>[hidden]{display:none!important}", 1).split('<div class="wrap">', 1)[0] +
            '</head>\n<body>\n<div class="wrap">' + frag.split('<div class="wrap">', 1)[1] + "\n</body>\n</html>\n")
    open(os.path.join(HERE, "..", "ARCHIVUM-LLM.html"), "w", encoding="utf-8").write(full)
    print(f"OK: ARCHIVUM-LLM.html ({len(full) / 1e3:.0f} KB), {len(vs)} változat, {len(ms)} modell, {len(presets)} profil")


if __name__ == "__main__":
    main()
