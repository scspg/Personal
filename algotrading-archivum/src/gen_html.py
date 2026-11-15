#!/usr/bin/env python3
"""ALGOTRADING.html: szűrhető katalógus, stratégiák, ötletek, kalkulátorok (1:500 margin/stop-out, grid-csőd Monte Carlo, Kelly), táblák.
Bemenet: ../katalogus.jsonl + research/a7_*.jsonl + research/a8_tables.md. Futtatás a build.py után: python3 -I gen_html.py"""
import json, os, re, html

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
RES = os.path.join(HERE, "research")


def jl(p):
    out = []
    if os.path.exists(p):
        for line in open(p, encoding="utf-8"):
            try:
                o = json.loads(line)
                if isinstance(o, dict):
                    out.append(o)
            except ValueError:
                pass
    return out


def md_tables(md):
    """egyszerű MD → HTML: címsorok, bekezdések, csőtáblák, felsorolás, linkek"""
    E = html.escape
    def inline(s):
        s = E(s)
        s = re.sub(r"\[([^\]]+)\]\((https?://[^)\s]+)\)", r'<a href="\2" target="_blank" rel="noopener">\1</a>', s)
        s = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", s)
        return re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    out, rows, ul, code, buf = [], [], False, False, []
    def flush():
        nonlocal rows
        if rows:
            hdr, *rest = rows
            out.append('<div class="tw"><table><thead><tr>' + "".join(f"<th>{inline(c)}</th>" for c in hdr) + "</tr></thead><tbody>"
                       + "".join("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>" for r in rest) + "</tbody></table></div>")
            rows = []
    for line in md.splitlines():
        s = line.strip()
        if s.startswith("```"):
            if code:
                out.append("<pre><code>" + E("\n".join(buf)) + "</code></pre>"); buf = []
            else:
                flush()
            code = not code
            continue
        if code:
            buf.append(line)
            continue
        if s == "---":
            flush(); out.append("<hr>"); continue
        if s.startswith("|"):
            cells = [c.strip() for c in s.strip("|").split("|")]
            if not all(re.fullmatch(r":?-{2,}:?", c) for c in cells if c):
                rows.append(cells)
            continue
        flush()
        if ul and not s.startswith(("- ", "* ")):
            out.append("</ul>"); ul = False
        m = re.match(r"(#{1,4}) (.*)", s)
        if m:
            lv = min(len(m.group(1)) + 1, 4)
            out.append(f"<h{lv}>{inline(m.group(2))}</h{lv}>")
        elif s.startswith(("- ", "* ")):
            if not ul:
                out.append("<ul>"); ul = True
            out.append(f"<li>{inline(s[2:])}</li>")
        elif s:
            out.append(f"<p>{inline(s)}</p>")
    flush()
    if ul:
        out.append("</ul>")
    return "\n".join(out)


def main():
    items = jl(os.path.join(ROOT, "katalogus.jsonl"))
    strat = jl(os.path.join(RES, "a7_strategies.jsonl"))
    ideas = jl(os.path.join(RES, "a7_ideas.jsonl"))
    tables = open(os.path.join(RES, "a8_tables.md"), encoding="utf-8").read() if os.path.exists(os.path.join(RES, "a8_tables.md")) else ""
    specp = os.path.join(ROOT, "FEJLESZTOI-SPEC.md")
    spec = open(specp, encoding="utf-8").read() if os.path.exists(specp) else ""
    cat_items = [{"i": o["id"], "n": o.get("name"), "c": o.get("cat"), "s": o.get("src") or "", "u": o.get("url"),
                  "a": o.get("access"), "p": o.get("price") or "", "e": o.get("price_eur_month"), "t": o.get("tier"),
                  "g": (o.get("prof") or {}).get("gyors_mt5"), "k": (o.get("prof") or {}).get("kockazat"),
                  "r": (o.get("prof") or {}).get("kutatas"), "d": (o.get("prof") or {}).get("predikcio"),
                  "h": (o.get("notes_hu") or " · ".join(x for x in (o.get("method_hu"), o.get("result_hu"), o.get("improve_hu")) if x) or "")[:500], "b": (o.get("pitfalls_hu") or "")[:250], "v": o.get("verified")} for o in items]
    st = [{"n": s.get("name"), "u": s.get("url"), "f": (s.get("formula_hu") or "")[:400], "w": (s.get("works_when_hu") or "")[:250],
           "x": (s.get("dies_when_hu") or "")[:250], "m": s.get("mt5_fit")} for s in strat]
    def pr(s):
        p = s.get("prereg")
        if not isinstance(p, dict):
            return (s.get("test_hu") or "")[:300]
        mn = p.get("min_n"); mn = f"{mn.get('n')} {mn.get('unit', '')}" if isinstance(mn, dict) else mn
        return f"{p.get('metric')} · horizont {p.get('horizon')} · min. n {mn} · α {p.get('alpha')} ({p.get('multiplicity')}) · OOS {p.get('oos_start')} · leállítás: {p.get('kill_rule')}"[:600]
    idz = [{"n": s.get("title_hu"), "m": (s.get("mechanism_hu") or "")[:400], "t": pr(s),
            "y": s.get("novelty"), "f": s.get("mt5_fit"), "r": (s.get("risk_hu") or "")[:200]} for s in ideas]
    data = json.dumps({"items": cat_items, "strat": st, "ideas": idz}, ensure_ascii=False).replace("</", "<\\/")
    page = TEMPLATE.replace("__DATA__", data).replace("__TABLES__", md_tables(tables) if tables else "<p>A táblák a kutatás végén kerülnek ide.</p>") \
        .replace("__SPEC__", md_tables(spec) if spec else "<p>A fejlesztői specifikáció külön fájlban: FEJLESZTOI-SPEC.md.</p>") \
        .replace("__N__", str(len(items))).replace("__NS__", str(len(strat))).replace("__NI__", str(len(ideas)))
    open(os.path.join(ROOT, "ALGOTRADING.html"), "w", encoding="utf-8").write(page)
    print(f"OK: ALGOTRADING.html ({len(page)//1024} KB), {len(items)} tétel")


TEMPLATE = r"""<!doctype html><html lang="hu"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>Algotrading-archívum</title>
<style>
:root{--bg:#f6f7f9;--card:#fff;--fg:#14181f;--mut:#5b6472;--line:#dde1e7;--acc:#0b6bcb;--pos:#127a3e;--neg:#b3261e;--chip:#eef2f7;color-scheme:light}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#0e1116;--card:#161b22;--fg:#e6e9ee;--mut:#9aa4b2;--line:#2a313b;--acc:#5aa9ff;--pos:#4cc27a;--neg:#ff7a70;--chip:#1f2630;color-scheme:dark}}
:root[data-theme="dark"]{--bg:#0e1116;--card:#161b22;--fg:#e6e9ee;--mut:#9aa4b2;--line:#2a313b;--acc:#5aa9ff;--pos:#4cc27a;--neg:#ff7a70;--chip:#1f2630;color-scheme:dark}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--fg);font:15px/1.5 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif}
header{position:sticky;top:0;z-index:5;background:var(--card);border-bottom:1px solid var(--line);padding:10px max(16px,env(safe-area-inset-left)) 0 max(16px,env(safe-area-inset-right))}
h1{font-size:18px;margin:0 0 6px}nav{display:flex;flex-wrap:wrap;gap:2px 4px}pre{overflow-x:auto;background:var(--chip);padding:8px;border-radius:6px;font-size:12px}hr{border:0;border-top:1px solid var(--line);margin:16px 0}nav button{border:0;background:none;color:var(--mut);padding:8px 10px;font:inherit;cursor:pointer;border-bottom:2px solid transparent;white-space:nowrap}
nav button[aria-current="page"]{color:var(--fg);border-color:var(--acc);font-weight:600}
main{padding:16px max(16px,env(safe-area-inset-left)) 40px max(16px,env(safe-area-inset-right));max-width:1400px;margin:0 auto}
section[hidden]{display:none}.card{background:var(--card);border:1px solid var(--line);border-radius:8px;padding:14px;margin:0 0 14px}
.row{display:flex;flex-wrap:wrap;gap:8px;align-items:end}.row label{display:flex;flex-direction:column;font-size:12px;color:var(--mut);gap:2px}
input,select{font:inherit;padding:6px 8px;border:1px solid var(--line);border-radius:6px;background:var(--bg);color:var(--fg);min-width:0}
input[type=number]{width:8.5em}.tw{overflow-x:auto;max-width:100%}table{border-collapse:collapse;width:100%;font-size:13px}
th,td{border-bottom:1px solid var(--line);padding:6px 8px;text-align:left;vertical-align:top}th{position:sticky;top:0;background:var(--card);cursor:pointer;font-weight:600}
a{color:var(--acc)}.chip{display:inline-block;background:var(--chip);border-radius:10px;padding:0 7px;font-size:12px;margin:1px}
.out{font-variant-numeric:tabular-nums}.out b{font-size:17px}.neg{color:var(--neg)}.pos{color:var(--pos)}.mut{color:var(--mut);font-size:13px}
button.go{background:var(--acc);color:#fff;border:0;border-radius:6px;padding:7px 14px;font:inherit;cursor:pointer}
.grid2{display:grid;grid-template-columns:repeat(auto-fit,minmax(320px,1fr));gap:14px}.grid2>*{min-width:0}
@media (max-width:640px){td,th{font-size:12px;padding:5px}}
</style></head><body>
<header><h1>Algotrading-archívum <span class="mut">· __N__ tétel · __NS__ stratégia · __NI__ ötlet</span></h1>
<nav id="nav"><button data-t="kat" aria-current="page">Katalógus</button><button data-t="kalk">Kalkulátorok</button><button data-t="str">Stratégiák</button><button data-t="otl">Ötletek</button><button data-t="inf">Infrastruktúra, adó</button><button data-t="spec">Fejlesztői spec</button><button data-t="mod">Módszertan</button></nav></header>
<main>
<section id="kat"><div class="card"><div class="row">
<label>Keresés<input id="q" placeholder="pl. tick, Polymarket, MT5"></label>
<label>Hozzáférés<select id="fa"><option value="">mind</option><option value="free">ingyenes</option><option value="registration">regisztrációs</option><option value="freemium">freemium</option><option value="paid">fizetős</option><option value="institutional">intézményi</option></select></label>
<label>Max €/hó<input id="fe" type="number" min="0" placeholder="nincs"></label>
<label>Max szint<select id="ft"><option value="3">3</option><option value="2">2</option><option value="1">1</option><option value="0">0</option></select></label>
<label>Rendezés profil szerint<select id="fp"><option value="g">Gyors pénz – aktív automatizált</option><option value="k">Aladdin-szerű kockázat</option><option value="r">Kutatás</option><option value="d">Predikció és sport</option></select></label>
<label>Terület<select id="fs"><option value="">mind</option></select></label>
</div><p class="mut" id="cnt"></p></div>
<div class="card tw"><table id="tk"><thead><tr><th>Sz.</th><th>Név</th><th>Terület</th><th>Hozzáférés</th><th>Ár</th><th>Pont</th><th>Mire jó</th><th>Buktató</th></tr></thead><tbody></tbody></table>
<p><button class="go" id="more" hidden>Több sor</button></p></div></section>

<section id="kalk" hidden><div class="grid2">
<div class="card"><h2>Margin és stop-out (1:500)</h2><div class="row">
<label>Egyenleg (USD)<input id="mb" type="number" value="1000"></label><label>Tőkeáttétel<input id="ml" type="number" value="500"></label>
<label>Lot<input id="mlot" type="number" value="1" step="0.01"></label><label>Kontraktusméret<input id="mc" type="number" value="100000"></label>
<label>Ár<input id="mp" type="number" value="1.08" step="0.0001"></label><label>Pipméret<input id="mpip" type="number" value="0.0001" step="0.0001"></label>
<label>Stop-out % (brókerfüggő)<input id="mso" type="number" value="50"></label>
<label>Jegyzett deviza → számladeviza árfolyam<input id="mfx" type="number" value="1" step="0.0001"></label></div><p class="out" id="mo"></p>
<p class="mut">Képlet: margin = lot × kontraktus × ár × (jegyzett deviza → számladeviza) / áttétel; USD-számlán XXX/USD párnál az átváltás 1, USD/JPY-nál 1/árfolyam, EUR/GBP-nél a GBP/USD árfolyam; stop-out, ha tőke / margin × 100 &lt; stop-out%. A számlát elvivő ellenirányú mozgás = (tőke − SO% × margin) / (lot × kontraktus). A stop-out szint brókerenként és jogalanyonként eltér (pl. EU/UK lakossági 50%, egyes offshore ECN-számlák 20%); a saját értéket a számlaszerződésből és a szimbólum-specifikációból kell venni.</p></div>
<div class="card"><h2>Grid-csőd Monte Carlo</h2><div class="row">
<label>Egyenleg<input id="gb" type="number" value="1000"></label><label>Áttétel<input id="gl" type="number" value="500"></label>
<label>Lot/szint<input id="glot" type="number" value="0.01" step="0.01"></label><label>Rács (pip)<input id="gs" type="number" value="20"></label>
<label>Célprofit (pip)<input id="gt" type="number" value="20"></label><label>Max szint<input id="gn" type="number" value="30"></label>
<label>Éves vol %<input id="gv" type="number" value="8"></label><label>Spread (pip)<input id="gsp" type="number" value="1"></label>
<label>Nap<input id="gd" type="number" value="250"></label><label>Szimuláció<input id="gm" type="number" value="400"></label>
<label>Stop-out %<input id="gso" type="number" value="50"></label>
<label>Negatívegyenleg-védelem<select id="gnbp"><option value="0">nincs (a veszteség túlléphet)</option><option value="1">van (nulla alá nem megy)</option></select></label><button class="go" id="grun">Futtatás</button></div><p class="out" id="go"></p>
<p class="mut">Modell: csak long rács EURUSD-szerű párra (ár 1,08, 100 000-es kontraktus), óránkénti geometriai bolyongás, drift nélkül, swap nélkül. Minden szint külön zár +célprofitnál. Determinisztikus mag: ugyanaz a bemenet ugyanazt adja. Becslés, nem előrejelzés: a valódi piac vastagabb farkú, és rezsimeket vált.</p></div>
<div class="card"><h2>Kelly-méretezés</h2><div class="row">
<label>Nyerési valószínűség p<input id="kp" type="number" value="0.55" step="0.01"></label><label>Nettó szorzó b (nyereség/kockázat)<input id="kb" type="number" value="1" step="0.05"></label></div>
<p class="out" id="ko"></p><p class="mut">f* = p − (1 − p) / b. Várható log-növekedés tétenként: g(f) = p·ln(1 + b·f) + (1 − p)·ln(1 − f). A 2×Kelly várható növekedése ≈ 0, efölött negatív: a túlméretezés hosszú távon biztos veszteség.</p></div>
</div></section>

<section id="str" hidden><div class="card"><input id="sq" placeholder="Keresés a stratégiák között"></div><div class="card tw"><table id="ts"><thead><tr><th>Stratégia</th><th>FX/CFD</th><th>Lényeg / képlet</th><th>Mikor működik</th><th>Mikor hal meg</th></tr></thead><tbody></tbody></table></div></section>
<section id="otl" hidden><div class="card"><input id="iq" placeholder="Keresés az ötletek között"></div><div class="card tw"><table id="ti"><thead><tr><th>Ötlet</th><th>Új</th><th>FX/CFD</th><th>Mechanizmus</th><th>Előregisztráció</th><th>Kockázat</th></tr></thead><tbody></tbody></table></div></section>
<section id="inf" hidden><div class="card">__TABLES__</div></section>
<section id="spec" hidden><div class="card"><p class="mut">A teljes szöveg: <code>FEJLESZTOI-SPEC.md</code>. A 12. fejezet (platform- és brókerfüggetlenség) minden más fejezetet felülír. A mermaid-ábrák itt forráskódként látszanak.</p>__SPEC__</div></section>
<section id="mod" hidden><div class="card"><h2>Pontozás</h2><p>Tételpontok 0–10: R relevancia, E edge-potenciál, Q minőség, C költséghatékonyság, L késleltetés/frissesség, F karbantartottság, Z jogi/ÁSZF-biztonság. Profilpont 0–100 = súlyozott átlag × 10. Súlyok (R/E/Q/C/L/F/Z): gyors pénz .15/.30/.10/.10/.20/.05/.10 · kockázat .25/.05/.30/.10/.05/.15/.10 · kutatás .25/.20/.25/.10/0/.15/.05 · predikció .15/.30/.15/.10/.10/0/.20.</p>
<p>Ellenőrzés: „mért” = a forrás oldalán látott adat a kutatás napján; „becsült” = számított vagy közvetett; „nem ellenőrzött” = a link vagy szám nem volt megerősíthető. Nem befektetési tanácsadás.</p></div></section>
</main>
<script>
const D=__DATA__;const $=s=>document.querySelector(s);const E=s=>String(s??"").replace(/[&<>"']/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]));
const fmt=(x,d=2)=>{let v=Number(x);if(Math.abs(v)<0.5*Math.pow(10,-d))v=0;return v.toLocaleString("hu-HU",{maximumFractionDigits:d,minimumFractionDigits:0})};
const AH={free:"ingyenes",registration:"regisztrációs",freemium:"freemium",paid:"fizetős",institutional:"intézményi"};
const norm=s=>String(s||"").normalize("NFD").replace(/[̀-ͯ]/g,"").toLowerCase();
const SRC={a1_market_exec:"Piac, végrehajtás",a2_crypto:"Kripto",a3_predict_sports:"Predikció, sport",a4_macro_news_alt:"Makró, hírek, alt. adat",a5_oss:"Nyílt szoftver",a6_ai_research:"AI-kutatás, irodalom",a8_infra_legal:"Infra, adó, jog",a9_platform:"Platform",a10_methods:"Bevált módszerek, esettanulmányok",a11_platforms:"Platform- és bróker-összehasonlítás"};
for(const [k,v] of Object.entries(SRC)){if(D.items.some(o=>o.s===k)){const o=document.createElement("option");o.value=k;o.textContent=v;$("#fs").append(o)}}
document.querySelectorAll("#nav button").forEach(b=>b.onclick=()=>{document.querySelectorAll("#nav button").forEach(x=>x.removeAttribute("aria-current"));b.setAttribute("aria-current","page");document.querySelectorAll("main>section").forEach(s=>s.hidden=s.id!==b.dataset.t);try{history.replaceState(null,"","#"+b.dataset.t)}catch(e){}});
function goHash(){const b=document.querySelector(`#nav button[data-t="${location.hash.slice(1)}"]`);if(b)b.click()}if(location.hash)goHash();window.addEventListener("hashchange",goHash);
let lim=150,sk=null,sd=-1;const SKEY=[t=>t.t??9,t=>norm(t.n),t=>norm(t.s),t=>norm(t.a),t=>t.e??1e12,null,t=>norm(t.h),t=>norm(t.b)];
document.querySelectorAll("#tk th").forEach((th,i)=>{th.title="Kattints a rendezéshez";th.onclick=()=>{if(i===5){sk=null}else{sd=sk===i?-sd:1;sk=i}rk()}});
function rk(){const q=norm($("#q").value),a=$("#fa").value,e=parseFloat($("#fe").value),t=+$("#ft").value,p=$("#fp").value,s=$("#fs").value;
const L=D.items.filter(o=>(!q||norm(o.n+" "+o.h+" "+o.c+" "+o.i).includes(q))&&(!a||o.a===a)&&(isNaN(e)||(o.a==="free"||o.a==="registration"?true:(o.e!=null&&o.e<=e)))&&(o.t??2)<=t&&(!s||o.s===s)).sort((x,y)=>{if(sk!=null){const f=SKEY[sk],a=f(x),b=f(y);return (a>b?1:a<b?-1:0)*sd}return (y[p]??0)-(x[p]??0)});
$("#cnt").textContent=`${L.length} tétel a(z) ${D.items.length}-ból`;$("#tk tbody").innerHTML=L.slice(0,lim).map(o=>`<tr><td>${E(o.t)}</td><td>${o.u?`<a href="${E(o.u)}" target="_blank" rel="noopener">${E(o.n)}</a>`:E(o.n)}<br><span class="mut">${E(o.v)}</span></td><td><span class="chip">${E(SRC[o.s]||o.s)}</span><br><span class="mut">${E(o.c)}</span></td><td>${E(AH[o.a]||o.a)}</td><td>${E(o.p)}${o.e?`<br><span class="mut">~${fmt(o.e,0)} €/hó</span>`:""}</td><td><b>${o[p]==null?"–":fmt(o[p],0)}</b></td><td>${E(o.h)}</td><td>${E(o.b)}</td></tr>`).join("");$("#more").hidden=L.length<=lim}
["#q","#fa","#fe","#ft","#fp","#fs"].forEach(s=>$(s).addEventListener("input",()=>{lim=150;rk()}));$("#more").onclick=()=>{lim+=300;rk()};rk();
function rs(){const q=norm($("#sq").value);$("#ts tbody").innerHTML=D.strat.filter(o=>!q||norm(o.n+o.f+o.w).includes(q)).sort((a,b)=>(b.m??0)-(a.m??0)).map(o=>`<tr><td>${o.u?`<a href="${E(o.u)}" target="_blank" rel="noopener">${E(o.n)}</a>`:E(o.n)}</td><td>${E(o.m??"?")}/10</td><td>${E(o.f)}</td><td>${E(o.w)}</td><td>${E(o.x)}</td></tr>`).join("")}
function ri(){const q=norm($("#iq").value);$("#ti tbody").innerHTML=D.ideas.filter(o=>!q||norm(o.n+o.m+o.t).includes(q)).sort((a,b)=>((b.y??0)+(b.f??0))-((a.y??0)+(a.f??0))).map(o=>`<tr><td><b>${E(o.n)}</b></td><td>${E(o.y??"?")}</td><td>${E(o.f??"?")}</td><td>${E(o.m)}</td><td>${E(o.t)}</td><td>${E(o.r)}</td></tr>`).join("")}
$("#sq").oninput=rs;$("#iq").oninput=ri;rs();ri();
function mcalc(){const B=+$("#mb").value,Lv=+$("#ml").value,lot=+$("#mlot").value,C=+$("#mc").value,P=+$("#mp").value,pip=+$("#mpip").value,SO=+$("#mso").value/100,FX=+$("#mfx").value;
if(!(B>0&&Lv>0&&lot>0&&C>0&&P>0&&pip>0&&SO>=0&&SO<5&&FX>0)){$("#mo").innerHTML='<span class="neg">Minden mező pozitív szám legyen (stop-out 0–500%).</span>';return}
const notional=lot*C*P*FX,m=notional/Lv,ml=m>0?B/m*100:Infinity,mv=(B-SO*m)/(lot*C*FX);
if(m>B){$("#mo").innerHTML=`<span class="neg">A szükséges margin (${fmt(m,2)}) nagyobb az egyenlegnél (${fmt(B,2)}): ez a pozíció nem nyitható meg.</span>`;return}
$("#mo").innerHTML=`Névérték: <b>${fmt(notional,0)} USD</b> · lekötött margin: <b>${fmt(m,2)} USD</b> · margin-szint: <b>${fmt(ml,0)}%</b><br>`+(mv<=0?`<span class="neg">Már nyitáskor stop-out alatt.</span>`:`Stop-out ennyi ellenirányú mozgásnál: <b class="neg">${fmt(mv,5)}</b> (${fmt(mv/P*100,3)}%, ${fmt(mv/pip,1)} pip). Tényleges áttétel: <b>${fmt(notional/B,1)}×</b>.`)}
["#mb","#ml","#mlot","#mc","#mp","#mpip","#mso","#mfx"].forEach(s=>$(s).addEventListener("input",mcalc));mcalc();
function rng(a){return function(){a|=0;a=a+0x6D2B79F5|0;let t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296}}
function grid(){const B=+$("#gb").value,Lv=+$("#gl").value,lot=+$("#glot").value,S=+$("#gs").value*1e-4,T=+$("#gt").value*1e-4,N=+$("#gn").value,vol=+$("#gv").value/100,sp=+$("#gsp").value*1e-4,days=+$("#gd").value,M=Math.max(1,Math.min(3000,Math.round(+$("#gm").value)||1)),SO=+$("#gso").value/100,C=100000;
if(!(B>0&&Lv>0&&lot>0&&S>0&&T>0&&N>=1&&vol>0&&days>0&&sp>=0)){$("#go").innerHTML='<span class="neg">Minden mező pozitív szám legyen.</span>';return}
const r=rng(12345),steps=Math.round(days*24),sig=vol/Math.sqrt(252*24);let ruin=0,fin=[],trades=0,k=0,neg=0,surv=[];const NBP=$("#gnbp").value==="1";$("#grun").disabled=true;
function chunk(){const end=Math.min(M,k+50);for(;k<end;k++){let P=1.08,bal=B,pos=[],dead=false;for(let i=0;i<steps&&!dead;i++){let u=r()||1e-12,v=r();P*=Math.exp(sig*Math.sqrt(-2*Math.log(u))*Math.cos(2*Math.PI*v));
pos=pos.filter(e=>{if(P>=e+T){bal+=T*lot*C;trades++;return false}return true});
if(pos.length===0||(pos.length<N&&P<=Math.min(...pos)-S)){pos.push(P+sp)}
let fl=0;for(const e of pos)fl+=(P-e)*lot*C;const eq=bal+fl,mg=pos.length*lot*C*P/Lv;if(mg>0&&eq/mg<SO){dead=true;bal=NBP?Math.max(0,eq):eq;ruin++;if(eq<0)neg++}}
if(!dead){let fl=0;for(const e of pos)fl+=(P-e)*lot*C;bal+=fl;surv.push(bal)}fin.push(bal)}
if(k<M){$("#go").textContent=`Számolás… ${k}/${M}`;setTimeout(chunk,0);return}$("#grun").disabled=false;
fin.sort((a,b)=>a-b);const q=p=>fin[Math.min(fin.length-1,Math.floor(p*fin.length))];
const mean=a=>a.length?a.reduce((x,y)=>x+y,0)/a.length:NaN;
$("#go").innerHTML=`<b>Átlagos végső tőke MINDEN pályán: <span class="${mean(fin)<B?"neg":"pos"}">${fmt(mean(fin),0)}</span></b> (kezdő ${fmt(B,0)}; ${fmt((mean(fin)/B-1)*100,1)}%) · csak a túlélők átlaga: ${fmt(mean(surv),0)} – a túlélők önmagukban túlélési torzítás<br>`+(NBP?"":`Nulla alá ment stop-outok: <b class="neg">${neg}</b> (${fmt(neg/M*100,1)}%) – negatívegyenleg-védelem nélkül tartozás keletkezik<br>`)+`Stop-out valószínűsége ${days} nap alatt: <b class="${ruin/M>0.05?"neg":"pos"}">${fmt(ruin/M*100,1)}%</b> (${ruin}/${M})<br>Végső tőke mediánja: <b>${fmt(q(.5),0)}</b> · 5%: ${fmt(q(.05),0)} · 95%: ${fmt(q(.95),0)} · átlagos lezárt ügylet/szimuláció: ${fmt(trades/M,0)}`}chunk()}
$("#grun").onclick=grid;
function kelly(){const p=+$("#kp").value,b=+$("#kb").value;if(!(p>0&&p<1&&b>0)){$("#ko").innerHTML='<span class="neg">0 &lt; p &lt; 1 és b &gt; 0 kell.</span>';return}const f=p-(1-p)/b,g=x=>x<=0?0:x>=1?-Infinity:p*Math.log(1+b*x)+(1-p)*Math.log(1-x);
$("#ko").innerHTML=f<=0?`<span class="neg">Negatív várható érték: f* = ${fmt(f,3)} – ne kössön.</span>`:`f* = <b>${fmt(f*100,1)}%</b> tétenként · növekedés/tét: ½ Kelly ${fmt(g(f/2)*100,3)}% · Kelly ${fmt(g(f)*100,3)}% · 2× Kelly <span class="neg">${2*f>=1?"csőd (a teljes tőke kockán, egy vesztes tét nulláz)":fmt(g(2*f)*100,3)+"%"}</span>`}
["#kp","#kb"].forEach(s=>$(s).addEventListener("input",kelly));kelly();
</script></body></html>"""

if __name__ == "__main__":
    main()
