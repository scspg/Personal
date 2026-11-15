#!/usr/bin/env python3
"""4c fejezet: tárolók (SSD, HDD, robusztus, archív, NAS, Faraday) – termékek, árak, szétosztás, adatmegőrzés.
Forrás: research/storage.json (a storage_hdd.yaml + storage_ssd.yaml kutatásból, 2026-11-14). Csak standard könyvtár."""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
KAT = {"ssd_nvme_gen5": "NVMe SSD (PCIe 5.0) – a gépbe", "ssd_nvme_gen4": "NVMe SSD (PCIe 4.0) – a gépbe",
       "ssd_enterprise": "Vállalati SSD (15–122 TB)", "ssd_rugged": "Strapabíró hordozható SSD", "ssd_sata": "2,5\" SATA SSD (laptopba)",
       "enclosure": "Külső házak, adapterek", "hdd_internal": "Nagy kapacitású HDD (3,5\", CMR)", "hdd_rugged": "Strapabíró / tűzálló hordozható HDD",
       "optical": "Archív optikai lemez (M-DISC)", "tape": "LTO-szalag", "nas": "NAS (hálózati tároló)", "das": "Többlemezes USB-ház (DAS)",
       "faraday": "Faraday- és fizikai védelem", "other": "Egyéb, megjegyzés"}
ORDER = ["hdd_internal", "ssd_nvme_gen5", "ssd_nvme_gen4", "ssd_rugged", "hdd_rugged", "ssd_sata", "ssd_enterprise", "enclosure",
         "nas", "das", "optical", "tape", "faraday", "other"]
SZINT = {"olcso": "olcsó", "kozep": "közép", "profi": "profi", "extrem": "extrém"}


def load():
    d = json.load(open(os.path.join(HERE, "research", "storage.json"), encoding="utf-8"))
    prods = d["hdd"]["termekek"] + d["ssd_products"]
    return d, prods


LABEL = {"28_TB": "28–32 TB – a teljes archívumhoz (ajánlott)", "24_TB": "24 TB – két gyártó, a 16 TB-os tervhez", "32_TB": "32 TB – a legkisebb térfogat a teljes archívumhoz", "5_TB_mag": "5 TB-os mag – zsebméret",
         "gaming_pc_munkameghajto_llm": "Gamer PC munkameghajtó (LLM-ek)", "gyors_hordozhato_masolat": "Gyors hordozható másolat",
         "enterprise_30_120tb_all_flash": "Vállalati all-flash, 30–120 TB", "profi": "profi", "kozep": "közép", "kozep_olcso": "közép / olcsó",
         "olcsobb_qlc": "olcsóbb (QLC)", "profi_tlc": "profi (TLC)", "oszinte_ertekeles": "őszinte értékelés", "megjegyzes": "megjegyzés",
         "8_TB": "8 TB", "16_TB": "16 TB", "32_TB_e": "32 TB", "64_TB": "64 TB", "128_TB": "128 TB"}
BUNDLE_CAP = {"~150": "5 TB HDD + 0,5 TB M-DISC", "~400": "2 × 8 TB", "~1 m": "2 × 24 TB + 0,5 TB M-DISC (a 16 TB-os tervhez)", "~3": "66 TB NAS + 84 TB offline", "Extr": "132 TB + 132 TB (HDD vagy LTO)"}
BUNDLE_SURV = {"~150": "lemezhiba (2 példány); a mag víz, EMP és zsarolóvírus ellen is (M-DISC)", "~400": "1 lemezhiba; ha a B példány máshol van: tűz, víz, lopás; Faraday: EMP",
               "~1 m": "1 lemezhiba, tűz/víz/lopás (külön helyszín), EMP (Faraday), zsarolóvírus (offline); a mag 3. médiumon is",
               "~3": "1 lemezhiba a NAS-ban + teljes offline másolat másik helyen", "Extr": "2 lemezhiba a NAS-ban + teljes offline másolat; LTO-val 30 év bekapcsolás nélkül"}
BUNDLE_PRICE = {"Extr": "~5,9 M Ft (HDD-másolattal) / ~8,3 M Ft (LTO-val)"}


def lab(k):
    return LABEL.get(k, str(k).replace("_", " "))


def hunum(t):
    import re as _r
    t = _r.sub(r"(?<=\d)\s?x\s?(?=\d|AFR|0,)", " × ", str(t))
    """angol tizedespont → vessző, csak mértékegység / százalék előtt (típusszámokat nem bánt)."""
    import re
    t = re.sub(r"(?<![\w.])(\d+)\.(\d+)(\s?(?:%|TB|GB|MB|PB|M Ft|W\b|GB/s|GbE|EUR|€|USD|DWPD|PBW|-szer|x\b|°C|év))", r"\1,\2\3", t)
    return re.sub(r"(?<![\w.])(\d+)\.(\d+)(?=\s?(?:[-–/]\s?\d+(?:[.,]\d+)?\s?(?:TB|GB|GbE)))", r"\1,\2", t)   # „30.72 / 61,44TB”, „1-2.5 GbE” bal oldala


def sent(x):
    """mondatzáró pont, ha hiányzik."""
    x = str(x).rstrip()
    return x if x[-1:] in ".!?…" else x + "."


def _e(s):
    return hunum(str(s if s is not None else "")).replace("|", "\\|").replace("\n", " ")


def ft(x):
    return f"{int(x):,}".replace(",", " ") + " Ft" if isinstance(x, (int, float)) and x else "–"


def dur(t):
    if not isinstance(t, dict):
        return _e(t)
    keys = [("ip", "IP"), ("viz", "víz"), ("tuz", "tűz"), ("eses", "esés"), ("drop", "esés"), ("utes", "ütés"), ("tbw", "TBW"),
            ("garancia_ev", "garancia, év"), ("garancia", "garancia"), ("mtbf_ora", "MTBF, óra"), ("elettartam", "élettartam"),
            ("backblaze", "Backblaze"), ("plp", "PLP")]
    out = []
    for k, l in keys:
        v = t.get(k)
        if v in (None, "", False) or (k == "plp" and v is False):
            continue
        out.append(f"{l}: {v}")
    return _e("; ".join(str(x) for x in out)[:220])


def speed(s):
    if isinstance(s, dict):
        r, w = s.get("olvasas"), s.get("iras")
        v = "/".join(str(x) for x in (r, w) if x not in (None, ""))
        return _e(v) if v else "–"
    return _e(s) if s not in (None, "") else "–"


def links(p):
    L = p.get("linkek") or []
    return " · ".join(f"[{_e(l.get('bolt'))}]({l.get('url')})" for l in L[:3] if l.get("url"))


def src_tag(p):
    f = p.get("ar_forras")
    f = " ".join(f) if isinstance(f, list) else str(f or "")
    if f.strip().lower().startswith("becsült") or "nincs ellenőrzött" in f:
        return "becsült"
    return "mért" if "mért" in f else ("becsült" if f else "–")


def section(plans):
    d, prods = load()
    hd, sx = d["hdd"], d["ssd_extra"]
    P = {b: p["items"] for b, p in plans}
    full = P.get("32TB") or plans[-1][1]["items"]
    sz = lambda L: sum((i.get("bytes") or i.get("bytes_est") or 0) for i in L) / 1e12
    llm = [i for i in full if i["cat"].startswith("ai_models")]
    nl = [i for i in full if not i["cat"].startswith("ai_models")]
    t01, t2, t3 = sz([i for i in nl if i["tier"] <= 1]), sz([i for i in nl if i["tier"] == 2]), sz([i for i in nl if i["tier"] >= 3])
    tot = sz(full)
    c = lambda x: f"{x:.1f}".replace(".", ",")
    md = ["---", "", "## 4c. Tárolók: mit vegyél, és hogyan oszd szét, hogy soha ne vesszen el", "",
          "> **Kutatás dátuma:** 2026-11-14. **Árak:** ipon.hu, pcx.hu, aqua.hu, senetic.hu, alternate.de, amazon.de – „mért” = a bolt oldalán látott ár, „becsült” = keresőtalálat vagy számítás. "
          "Az arukereso.hu, az alza.hu, az emag.hu, az edigital.hu és a mediamarkt.hu az ellenőrzéskor blokkolta az automatikus lekérést – vásárlás előtt ott is nézd meg az árat. Árfolyam: 1 EUR = 365,60 Ft (EKB, 2026-11-13).",
          "> **Piaci helyzet:** 2025 vége óta az AI-adatközpontok miatt hiány van; az SSD-k a 2025-ös ár 2–4-szeresébe, a HDD-k kb. +50%-ba kerülnek. Az árak gyorsan változnak.", "",
          "### A lényeg – egy mondatban", "",
          f"**A teljes archívum ({c(tot)} TB) egyetlen 28–32 TB-os HDD-re ráfér (24 TB-on 94%-os telítettséggel már nem marad tartalék) – ez a „minden egyben” fizikai minimum. "
          "De egyetlen példány 10 év alatt kb. 13–22% eséllyel elvész; egy második, offline, más gyártótól származó példánnyal ez kb. 0,1–0,3%-ra csökken (~70×). "
          "Ezért a logikus, legkompaktabb megoldás: 2 db 28–32 TB-os HDD (egy használatban, egy Faraday-tasakban, lőszerládában, másik helyen) + egy kicsi, strapabíró SSD a létfontosságú maggal.**", "",
          "### Mi hova kerüljön – rétegek", "",
          "| Réteg | Mi kerül rá | Méret (32 TB-os terv) | Ajánlott eszköz | Miért |", "|---|---|---|---|---|",
          f"| **1. Mag** (mindig nálad, bármikor olvasható) | 0–1. szintű tudás: orvoslás, víz, élelem, túlélés, alapkönyvtár + 1 kis LLM | ~{c(t01 + 0.05)} TB | strapabíró SSD 2–4 TB, alapajánlat: **Samsung T7 Shield 4TB** (IP65, 3 m esés, ~317 ezer Ft, becsült; a 2 TB-os ipon 198 391 Ft, mért) **és** a legfontosabb ~0,5 TB M-DISC BDXL lemezeken; olcsóbb HDD-s változat: LaCie Rugged 5TB (nem vízálló) vagy ADATA HD710 Pro (IP68) | telefonról, laptopról is olvasható, víz- és ütésálló; az M-DISC áram, mágnes és zsarolóvírus ellen véd |",
          f"| **2. Munka** (gyors, a gépben) | az LLM-modellek + amit naponta használsz | ~{c(sz(llm))} TB + tartalék | NVMe PCIe 5.0 SSD 4–8 TB a gamer PC-ben | a modell betöltése 8 TB-os Gen5-ről ~50 s; ez NEM archívum, mindenről van másolat |",
          f"| **3. Teljes archívum** (A példány, használatban) | minden: 2–5. szint, nagy tükrök, térképek, lexikonok | ~{c(tot)} TB | 1 db 28–32 TB HDD (CMR) dokkolóban, ZFS-sel | a legolcsóbb TB-ár, havi ellenőrzéssel önjavító |",
          f"| **4. Offline másolat** (B példány) | ugyanaz, mint a 3. | ~{c(tot)} TB | 1 db 28–32 TB HDD, **más gyártótól vagy termékcsaládtól**, antisztatikus tasak + Faraday-tasak + tömített acél lőszerláda + szilikagél, **másik épületben** | tűz, víz, lopás, villám, EMP, zsarolóvírus, rossz parancs ellen; félévente be kell kapcsolni és végigolvasni |",
          "| **5. (opcionális) 30 éves réteg** | a teljes archívum harmadik példánya | 22–128 TB | LTO-9 szalag (kazetta ~2 000 Ft/TB) | csak ~260 TB felett vagy 3+ másolatnál éri meg a ~4 M Ft-os meghajtó miatt; a meghajtót is meg kell őrizni |", "",
          "### Ajánlott összeállítások árszintenként", "",
          "| Keret | Összeállítás | Kapacitás | Ár | Mit bír ki | Megjegyzés / alternatíva |", "|---|---|---|---|---|---|"]
    J = hd.get("javaslat") or {}
    for k, v in J.items():
        el = v.get("elemek") or []
        key = next((b for b in BUNDLE_CAP if k.startswith(b)), "")
        md.append(f"| **{_e(k)}** | " + "<br>".join(_e(x) for x in el) + f" | {BUNDLE_CAP.get(key, '–')} | {_e(BUNDLE_PRICE.get(key) or v.get('osszesen'))} | "
                  f"{BUNDLE_SURV.get(key, '–')} | {_e(v.get('megjegyzes') or v.get('alternativa') or '–')} |")
    K2 = hd.get("kompakt_2_eszkoz") or {}
    md += ["", "### A legkompaktabb kételemes megoldás (a „minden egyben” kérésre; a B példány vizet, ütést, EMP-t is túlél)", "",
           "| Változat | 1. eszköz | 2. eszköz (offline) | Védelem | Összesen |", "|---|---|---|---|---|"]
    for k, v in K2.items():
        if not isinstance(v, dict):
            continue
        md.append(f"| **{lab(k)}** | {_e(v.get('eszkoz_1_elsodleges') or v.get('eszkoz_1'))} | {_e(v.get('eszkoz_2_offline') or v.get('eszkoz_2'))} | "
                  f"{_e(v.get('vedelem') or v.get('plusz_opcionalis_mag') or '')}{(' ' + _e(v['megjegyzes'])) if v.get('megjegyzes') else ''} | {_e(v.get('osszesen'))} |")
    if K2.get("miert_nem_raid1_egy_dobozban"):
        md += ["", f"*Miért nem egy RAID1-es doboz?* {_e(K2['miert_nem_raid1_egy_dobozban'])}"]
    GY = sx.get("javaslat") or {}
    md += ["", "### A leggyorsabb, legprofibb (SSD) ág", ""]
    for k, v in GY.items():
        if isinstance(v, dict):
            md.append(f"- **{lab(k)}:**")
            md += [f"  - *{lab(kk)}:* {_e(vv)}" for kk, vv in v.items()]
    E1 = hd.get("egyeszkozos_opciok") or {}
    md += ["", "### Egyetlen eszköz méretenként (ha mégis egy kell)", "", "| Méret | Lehetőségek |", "|---|---|"]
    for k, v in E1.items():
        if isinstance(v, list):
            md.append(f"| **{lab(k + '_e' if k == '32_TB' else k)}** | " + "<br>".join(_e(x) for x in v) + " |")
    if E1.get("kovetkeztetes"):
        md += ["", f"> **Figyelem:** {_e(E1['kovetkeztetes'])}"]
    KA = hd.get("kockazat_elemzes") or {}
    s10 = KA.get("szamitas_10_ev") or {}
    md += ["", "### Egy vagy két példány – számokkal (becslés, a Backblaze Q2 2026 meghibásodási adataiból)", "",
           f"- **Módszer:** {_e(s10.get('modszer'))}",
           "- **Egy példány, 10 év:** " + "; ".join(f"{_e(k)} → **{_e(v)}**" for k, v in (s10.get("egy_masolat") or {}).items()),
           "- **Két példány, félévente ellenőrizve:** " + "; ".join(f"{_e(k)} → **{_e(v)}**" for k, v in (s10.get("ket_masolat_felevente_ellenorizve") or {}).items()),
           f"- **Két példány karbantartás nélkül:** {_e(s10.get('ket_masolat_karbantartas_nelkul_10_evig'))}",
           f"- **Rejtett bithiba (URE):** {_e(s10.get('bit_rot_ure'))}",
           f"- **SSD:** {_e((sx.get('egy_vs_ket_peldany') or {}).get('egy_ssd'))} {_e((sx.get('egy_vs_ket_peldany') or {}).get('ssd_plusz_offline_masolat'))}",
           f"- **Következtetés:** {_e(KA.get('konkluzio'))}", "",
           "**Modellenkénti meghibásodási arány (Backblaze, élettartam-AFR):** " +
           "; ".join(f"{_e(k).replace('_', ' ')}: {_e(v)}" for k, v in ((KA.get('backblaze_q2_2026') or {}).get('modellek_elettartam_afr') or {}).items()) +
           " – a Toshiba MG és a WD HC5xx család a legmegbízhatóbb; az Exos X24 24TB kerülendő.", ""]
    AM = sx.get("adatmegorzes_tenyek") or {}
    AI = hd.get("adatintegritas") or {}
    md += ["### Adatmegőrzés és -épség – a gyakorlat", "",
           "**SSD áram nélkül (JEDEC JESD218):**"] + [f"- {_e(x)}" for x in AM.get("jedec_jesd218") or []] + [f"- {_e(AM.get('homerseklet'))}", f"- {_e(AM.get('tlc_vs_qlc'))}", ""]
    for k, l in [("zfs_btrfs", "ZFS / Btrfs (önjavító ellenőrzőösszeg)"), ("snapraid_par2", "SnapRAID / par2 (paritás)"), ("offline_bekapcsolas", "Offline példány karbantartása"),
                 ("tarolasi_klima", "Tárolási klíma"), ("smart", "SMART-figyelés")]:
        v = AI.get(k)
        if v:
            md.append(f"- **{l}:**")
            md += [f"  - {_e(x)}" for x in (v if isinstance(v, list) else [v])]
    if AI.get("diverzifikacio"):
        md.append(f"- **Diverzifikáció:** {_e(AI['diverzifikacio'])}")
    note = next((p for p in prods if p.get("kategoria") == "other" and not p.get("ar_huf")), None)
    real = [p for p in prods if p.get("kategoria") != "other" or p.get("ar_huf")]
    md += ["- **SSD-gyakorlat:**"] + [f"  - {_e(x)}" for x in AM.get("gyakorlat") or []] + ["",
           f"### Terméktábla – {len(real)} termék, kategóriánként", ""]
    if note:
        md += [f"> **{_e(note.get('nev'))}** – " + " ".join(_e(sent(x)) for x in (note.get("hatranyok") or []) + (note.get("elonyok") or [])), ""]
    md += [
           "Szint: olcsó / közép / profi / extrém. Sebesség MB/s (SSD-nél olvasás/írás). A „Forrás” oszlop jelzi, hogy az ár mért vagy becsült.", ""]
    by = {}
    for p in real:
        by.setdefault(p.get("kategoria"), []).append(p)
    for k in ORDER:
        if k not in by:
            continue
        md += [f"#### {KAT.get(k, k)}", "", "| Termék | TB | Tartósság | Sebesség | Ár | Ft/TB | Forrás | Szint | Hol kapható | Előny / hátrány |",
               "|---|---|---|---|---|---|---|---|---|---|"]
        for p in sorted(by[k], key=lambda p: (p.get("ar_huf") is None, (p.get("ar_huf") or 0) / max(float(p.get("kapacitas_tb") or 1), 0.001))):
            pro = "; ".join((p.get("elonyok") or [])[:2])
            con = "; ".join((p.get("hatranyok") or [])[:2])
            md.append(f"| **{_e(p.get('nev'))}** | {(str(p['kapacitas_tb']).replace('.', ',') if p.get('kapacitas_tb') is not None else '–')} | {dur(p.get('tartossag'))} | {speed(p.get('sebesseg_mb_s'))} | "
                      f"{ft(p.get('ar_huf'))} | {_e(p.get('ar_per_tb') or '–')} | {src_tag(p)} | {SZINT.get(p.get('ajanlas_szint'), '–')} | {links(p)} | "
                      f"+ {_e(pro)}<br>− {_e(con)} |")
        md.append("")
    md += ["**Források:** " + " · ".join(f"<{u}>" for u in (hd.get("forrasok") or []) + (AM.get("forrasok") or [])), ""]
    return "\n".join(md)


if __name__ == "__main__":
    print(section([("32TB", {"items": []})])[:3000])
