OVERRIDES = {
 "usda-complete-guide-home-canning-2015": {"download": {"method": "http", "urls":
   ["https://nchfp.uga.edu/papers/guide/INTRO_HomeCanrev0715.pdf"] +
   [f"https://nchfp.uga.edu/papers/guide/GUIDE0{i}_HomeCan_rev0715.pdf" for i in range(1, 8)]}},
 "msf-cholera-and-public-health-engineering": {"download": {"method": "http", "urls": [
   "https://medicalguidelines.msf.org/sites/default/files/pdf/guideline-800-en.pdf",
   "https://medicalguidelines.msf.org/sites/default/files/2022-06/Public_health_engineering_2010.pdf"]}},
 "cd3wd-2012-dvd-isos": {"download": {"method": "http", "urls": [
   f"https://ftpmirror.your.org/pub/misc/cd3wd/cd3wd%202012%206%20dvds/100{i}_cd3wd.iso" for i in range(1, 7)] +
   ["https://ftpmirror.your.org/pub/misc/cd3wd/cd3wd%202012%206%20dvds/cd3wd_checksums.sha1"]},
   "subsumed_by": [], "notes": "A CD3WD 6 DVD ISO-ja (2012). A Kiwix kx-cd3wd ZIM (0,57 GB) a webes változat – ha kevés a hely, az elég; az ISO-k a teljes, eredeti PDF-gyűjtemény."},
}
EST = {"wikem-emergency-medicine-wiki": (1_500_000_000, "estimated:~5k MediaWiki oldal képekkel, wget-tükör"),
       "kitinoja-kader-small-scale-postharvest": (20_000_000, "estimated:HTML könyv"),
       "fao-human-nutrition-developing-world": (20_000_000, "estimated:HTML könyv"),
       "fao-better-farming-series": (120_000_000, "estimated:~50 kötet x ~2 MB EPUB/PDF"),
       "pfaf-plants-for-a-future": (1_000_000_000, "estimated:~8000 HTML növényoldal képekkel"),
       "icraf-agroforestree-database": (1_000_000_000, "estimated:HTML fajoldalak képekkel")}
for k, (b, st) in EST.items():
    OVERRIDES.setdefault(k, {}).update({"bytes_est": b, "size_status": st})
OVERRIDES["cd3wd-2012-dvd-isos"].update({"group": "cd3wd", "variant_rank": 2, "variant_role": "pref"})
OVERRIDES["msf-clinical-guidelines"] = {"download": {"method": "http", "urls": [
    "https://medicalguidelines.msf.org/sites/default/files/pdf/guideline-170-en.pdf"]},
    "notes": "Stabil útvonal: /sites/default/files/pdf/guideline-170-<nyelv>.pdf (en, fr, es, ar). A dátumos mappa (pl. 2026-05) frissítéskor változik."}
