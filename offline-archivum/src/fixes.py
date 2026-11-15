#!/usr/bin/env python3
"""Adatjavítások a minőségellenőrzés (QA) alapján – a build minden futáskor alkalmazza (apply(items) -> items).
Egy helyen, újrafuttathatóan: nyelvi enumok, letöltési blokkok, duplikátumok, tierek/pontok, magyar szövegek."""
import json, os, re

DELETE = {"village-earth-at-library", "llm-qwen3-8-27b-gguf-bf16-2"}          # azonos a village-earth-appropriate-technology-library tétellel

# nyelvi enum (hu/en/multi) – enélkül a kiválasztó soha nem választotta ki; külön lépés, hogy más javítás ne írja felül
LANG = {**{i: "en" for i in ["openstax", "kolibri-khan-academy", "practical-action-knowledge-centre", "reprap-wiki-dump", "ck12",
                             "sci-hub", "natural-earth", "where-there-is-no-doctor", "dartnell-the-knowledge"]},
        **{i: "multi" for i in ["tesseract-ocr-tessdata", "whisper-cpp-models", "nllb-200", "piper-tts-hu", "argos-translate-hu",
                                "firefox-translations-bergamot"]}}

PATCH = {
    # --- git-blokkok: weboldal helyett repó (git ls-remote-tal ellenőrizve a QA során) ---
    "openflexure-microscope": {"download": {"method": "git", "repos": ["https://gitlab.com/openflexure/openflexure-microscope.git"]}},
    "wikihouse-skylark": {"download": {"method": "git", "repos": ["https://github.com/wikihouseproject/Skylark"]}},
    "libre-solar-hardware": {"download": {"method": "git", "repos": ["https://github.com/LibreSolar/mppt-2420-hc", "https://github.com/LibreSolar/bms-c1",
                                                                     "https://github.com/LibreSolar/charge-controller-firmware"]}},
    "precious-plastic-download-kit-v4": {"download": {"method": "git", "repos": ["https://github.com/ONEARMY/precious-plastic-kit"]}},
    "openinverter-stm32-sine": {"download": {"method": "git", "repos": ["https://github.com/jsphuebner/stm32-sine", "https://github.com/jsphuebner/libopeninv"]}},
    "respiraworks-ventilator": {"download": {"method": "git", "repos": ["https://github.com/RespiraWorks/Ventilator"]}},
    # --- hf-blokkok repo nélkül → pontos repo + include, mért méret ---
    "nllb-200": {"download": {"method": "agent", "note": "Két HF-repó: hf download facebook/nllb-200-distilled-600M ; hf download facebook/nllb-200-3.3B",
                              "seed_urls": ["https://huggingface.co/facebook/nllb-200-distilled-600M", "https://huggingface.co/facebook/nllb-200-3.3B"]}},
    # --- egyéb használhatatlan blokkok ---
    "babcock-wilcox-steam-1913": {"download": {"method": "archive.org", "ids": ["steamitsgenerati22657gut"]}, "bytes": 13296398,
                                  "size_status": "measured:2026-11-14:archive.org metadata"},
    "nebih-kiadvanyok": {"download": {"method": "agent", "note": "A NÉBIH tájékoztatók/kiadványok oldaláról a PDF-linkek összegyűjtése, majd letöltés.",
                                      "seed_urls": ["https://portal.nebih.gov.hu/-/tajekoztatok-kiadvanyok"]}},
    "msf-clinical-guidelines": {"download": {"method": "http", "urls": ["https://medicalguidelines.msf.org/sites/default/files/2026-05/guideline-170-en.pdf"]},
                                "bytes": 6751876, "notes": "A /pdf/guideline-170-en.pdf útvonal csak 16 KB-os csonk – a dátumos mappa a valódi kézikönyv (2026-05). Frissítéskor a dátum változhat: a https://medicalguidelines.msf.org/en oldalról keresd."},
    "india-mark-ii-handpump-manual-2008": {"download": {"method": "http", "urls": ["https://susana.org/_resources/documents/default/3-4194-7-1617282174.pdf"]},
                                           "bytes": 3177902, "size_status": "measured:2026-11-14:content-length (SuSanA tükör)"},
    "kx-gardenology": {"download": {"method": "kiwix", "book": "gardenology_en_all", "flavour": None,
                                    "url": "https://lb.download.kiwix.org/zim/other/gardenology.org_en_all_2026-09.zim"}},
    "kuphaldt-lessons-in-electric-circuits": {"bytes": 75805218},
    "ubuntu-26041-desktop-iso": {"bytes": 6482409472, "size_status": "measured:2026-11-14:content-length"},
    "raspberry-pi-os-full-arm64": {"bytes": 2064882780, "size_status": "measured:2026-11-14:content-length"},
    "alpine-3244-extended-iso": {"bytes": 1458192384, "size_status": "measured:2026-11-14:content-length"},
    "osa-seed-saving-guide": {"bytes_est": 5_000_000}, "voroskereszt-kiadvanyok": {"bytes_est": 50_000_000},
    "internet-in-a-box": {"bytes_est": 5_000_000_000}, "engineering-toolbox": {"bytes_est": 5_000_000_000},
    # --- duplikátumok, csoportok, átfedések ---
    "pmc-open-access": {"subsumed_by": ["pmc-open-access-s3"]},
    "survivor-library-flash-drive": {"group": "survivor", "variant_rank": 3},
    "kx-gutenberg-hu": {"subsumed_by": ["kx-gutenberg-mul", "project-gutenberg-rsync"]},
    "where-there-is-no-doctor": {"group": "wtnd", "variant_rank": 2},
    "hesperian-where-there-is-no-doctor-2025": {"group": "wtnd", "variant_rank": 1, "variant_role": "pref"},
    "debian-13-source-bd-jigdo-set": {"subsumed_by": ["debian-full-archive-ftpsync"]},
    **{i: {"subsumed_by": ["mek-oszk"]} for i in ["pallas-nagy-lexikona", "revai-nagy-lexikona", "magyar-neprajzi-lexikon", "magyar-eletrajzi-lexikon"]},
    "cd3wd-2012-dvd-isos": {"cat": "appropriate_tech"}, "survivor-library": {"cat": "library"},
    "kx-khan": {"tier": 2},
    # --- Hugging Face / platform tételek: átfedések és apró hibák ---
    "hub-whisper-cpp-large-v3-turbo": {"bytes": 1624555275 + 574041195, "size_status": "measured:2026-11-14:hf-api (2 fájl)"},
    "hub-paddleocr-vl-1-6": {"download": {"method": "hf", "repo": "PaddlePaddle/PaddleOCR-VL-1.6", "include": []}},
    "hub-indra-ocr": {"download": {"method": "hf", "repo": "datalab-to/indra-ocr", "include": []}},
    "whisper-cpp-models": {"download": {"method": "hf", "repo": "ggerganov/whisper.cpp", "include": ["ggml-large-v3-turbo-q5_0.bin", "ggml-medium.bin", "ggml-small.bin"]},
                           "bytes": 2595406221, "size_status": "measured:2026-11-14:hf-api"},
    "piper-tts-hu": {"download": {"method": "hf", "repo": "rhasspy/piper-voices", "include": ["hu/*"]}, "bytes": 189988337,
                     "size_status": "measured:2026-11-14:hf-api (hu/ mappa, 12 fájl)", "size_human": "190 MB", "subsumed_by": ["hub-piper-hu-voices"]},
    "argos-translate-hu": {"group": "argos-translate", "variant_rank": 2, "variant_role": "luxury"},
    **{i: {"bytes_est": 50_000_000, "size_status": "estimated:git mirror (Markdown lista)"} for i in
       ["hub-awesome-selfhosted", "hub-awesome-sysadmin", "hub-awesome-open-hardware", "hub-awesome-public-datasets", "hub-awesome-meta"]},
    # --- régi tételek, amelyeket az ellenőrzött nyílt forráskódú szoftvertételek lefednek ---
    # (a régi tételek a bináris telepítőt/firmware-t töltik, az oss-* a forráskódot – mindkettő kell, nincs lefedés)
    "internet-in-a-box": {"subsumed_by": ["oss-internet-in-a-box"], "download": {"method": "git", "repos": ["https://github.com/iiab/iiab"]}},
    # --- tier/pont-javítások ---
    "tool-vlc": {"tier": 2}, "internet-archive-ia-cli": {"tier": 3}, "organic-syntheses": {"tier": 2},
}

# több fájlból álló készletek, ahol csak egy URL szerepelt: AI-feladattá alakítjuk (a teljes méret megmarad)
MULTI_FILE = ["who-imci-distance-learning-2014", "who-monographs-medicinal-plants-vol1-4", "who-imai-district-clinician-manual",
              "who-essential-medicines-list-2025", "unicef-practica-manual-drilling-toolkit", "peace-corps-ice-manuals",
              "meshtastic-firmware-and-docs", "worldclim-21", "hydrosheds", "natural-earth", "freecad-and-parts-library", "arduino-ide-offline",
              "calibre", "freedos-14", "linux-kernel-source", "gebco-2026-grid", "wikidata-json-dump", "enwiki-pages-articles-xml",
              "kicad-eda-and-libraries"]

GPU_UNLOCK_R = {"tinygrad-p2p-kmod": 3, "aikitoria-p2p-kmod": 3, "zagitta-gpu-unlock": 3, "gpu-unlock-ada": 3}

HU_DESC = {
    "kearny-nuclear-war-survival-skills": [("csapadék elleni óvóhely", "radioaktív kihullás elleni óvóhely")],
    "village-earth-appropriate-technology-library": [("megfelelő-technológiai", "„megfelelő technológiai” (appropriate technology)"), ("Kurált", "Gondosan válogatott")],
    "who-decontamination-medical-devices-2016": [("Eldobható eszközök nélkül nélkülözhetetlen.", "Ha nincs eldobható eszköz, nélkülözhetetlen.")],
    "annas-archive": [("Szerzői jogi szempontból jogsértő tartalom túlnyomó része.", "Tartalmának túlnyomó része szerzői jogot sért.")],
    "gingery-metal-shop-from-scrap": [("Ehhez a lépéssorhoz nincs igazi ingyenes megfelelő.", "Egyenértékű ingyenes alternatívája nincs.")],
    "open-rn-nursing-skills-pharmacology": [("Az orvosi kézikönyvek mellől az ápolási gyakorlat hiányzott.", "Az orvosi kézikönyveket az ápolási gyakorlattal egészíti ki.")],
    "icrc-war-surgery-vol1": [("debridement", "sebkimetszés (debridement)"), ("triage", "osztályozás (triázs)"), ("Trauma-sebészet alapműve", "A traumasebészet alapműve")],
    "special-forces-medical-handbook-st-31-91b": [("Klasszikus különleges erők orvosi kézikönyve", "A különleges erők klasszikus orvosi kézikönyve")],
    "hesperian-where-women-have-no-doctor-2023": [("Női egészség kézikönyv", "Női egészségügyi kézikönyv"), ("STI", "nemi úton terjedő fertőzések")],
}
GENERIC_HU = [("rebuild szempontból", "az újjáépítés szempontjából"), ("bulk-ban", "tömegesen"), ("offline flasheléshez", "internet nélküli feltöltéshez"),
              ("HVAC", "fűtés-, szellőzés- és klímatechnika"), ("unverified", "nem ellenőrzött"), ("Szöveg-only", "Csak szöveges"),
              ("Wikipedia", "Wikipédia"), ("teljes WP", "teljes Wikipédia"), ("bevezető + infobox", "csak a bevezető és az infodoboz"),
              ("infobox", "infodoboz")]


def _clean_null(d):
    """'null' szöveg → valódi hiány; rekurzívan a download blokkban is."""
    for k in list(d):
        v = d[k]
        if v == "null" or v == "None":
            if k in ("price",):
                d.pop(k)
            elif k == "url" and isinstance(d, dict) and "method" in d:
                d.pop(k)
            else:
                d[k] = None
        elif isinstance(v, dict):
            _clean_null(v)
    return d



# --- 3. adatminőségi átnézés (2026-11-14) javításai: mért értékek (Content-Length / HF tree) ---
M = "measured:2026-11-14"
PATCH2 = {
    "oss-internet-in-a-box": {"tier": 2},
    "oss-osmium-tool": {"bytes_est": 5_000_000, "size_human": "~5 MB (csak az eszköz; a bolygófájl külön tétel: osm-planet-pbf)"},
    "oss-whisper-cpp": {"bytes": None, "bytes_est": 30_000_000, "size_human": "~30 MB forráskód (a modellek: whisper-cpp-models, hub-whisper-cpp-large-v3-turbo)"},
    "oss-piper": {"bytes": None, "bytes_est": 15_000_000, "size_human": "~15 MB forráskód (a magyar hangok: hub-piper-hu-voices)"},
    "oss-debian": {"bytes": None, "bytes_est": 60_000_000, "size_human": "~60 MB (debian-installer forrás; a DVD-képfájl külön tétel)"},
    "oss-gcc": {"bytes": 107_200_820}, "oss-git": {"bytes": 8_494_608}, "oss-go": {"bytes": 70_680_823},
    "hub-codeberg-gitlab": {"download": {"method": "manual", "url": "https://codeberg.org/explore/repos"}},
    "hub-modelscope": {"download": {"method": "manual", "url": "https://modelscope.cn/models"}},
    "hub-myminifactory": {"download": {"method": "manual", "url": "https://www.myminifactory.com/"}},
    "tesseract-ocr-tessdata": {"download": {"method": "git", "repos": ["https://github.com/tesseract-ocr/tessdata_best"]}},
    "hub-tesseract-hun-best": {"bytes": 12_350_405, "size_status": M + ":content-length", "size_human": "12,4 MB"},
    "hub-ds-plantnet-300k": {"download": {"method": "http", "urls": ["https://zenodo.org/api/records/5645731/files/plantnet_300K.zip/content"]},
                             "bytes": 31_670_505_069, "size_status": M + ":content-length"},
    "hub-argos-translate-hu": {"download": {"method": "http", "urls": ["https://argos-net.com/v1/translate-en_hu-1_9.argosmodel",
                               "https://argos-net.com/v1/translate-hu_en-1_9.argosmodel"]}, "bytes": 67_859_271 + 71_809_926,
                               "size_status": M + ":content-length", "group": "argos-translate", "variant_rank": 1, "variant_role": "pref"},
    "hub-parakeet-tdt-v3-onnx": {"bytes": 670_619_803, "size_status": M + ":hf-tree"},
    "hub-ds-osm-wikidata-linked": {"bytes": 37_894_983_893, "size_status": M + ":hf-tree"},
    "hub-ds-medqa": {"bytes": None, "bytes_est": 18_300_000, "size_status": M + ":hf-tree (csak MedQA; MedMCQA, PubMedQA külön repó)"},
    "hub-torchxrayvision": {"bytes": 28_382_008, "bytes_est": None, "size_status": M + ":content-length"},
    "hub-real-esrgan-ncnn": {"download": {"method": "http", "urls": [
        "https://github.com/xinntao/Real-ESRGAN/releases/download/v0.2.5.0/realesrgan-ncnn-vulkan-20220424-ubuntu.zip",
        "https://github.com/xinntao/Real-ESRGAN/releases/download/v0.2.5.0/realesrgan-ncnn-vulkan-20220424-windows.zip"]},
        "bytes": 46_931_474 + 45_474_481, "size_status": M + ":content-length"},
    "hub-ds-hulu-benchmarks": {"bytes": 1_300_000, "size_status": M + ":hf-tree (csak HuCOLA; a többi NYTK-adathalmaz a HF-en: NYTK/*)"},
    "hub-medsiglip-448": {"access": "free-registration"}, "hub-ds-the-stack-v2": {"access": "free-registration"},
    "oss-osmand": {"cat": "oss_maps"}, "oss-qgis": {"cat": "oss_maps"}, "oss-freecad": {"cat": "oss_engineering"},
    "oss-kicad": {"cat": "oss_embedded"}, "oss-prusaslicer": {"cat": "oss_3dprint"}, "oss-openemr": {"cat": "oss_health"},
    "oss-linuxcnc": {"cat": "oss_engineering"}, "oss-home-assistant": {"cat": "oss_automation"}, "oss-arduino-ide": {"cat": "oss_embedded"},
    "hub-plantnet-plantclef2024-vitb": {"tier": 2, "scores": {"S": 5, "R": 6, "A": 8, "U": 9, "Q": 7, "O": 8},
        "notes": "Növényfelismerés segédeszköz: ehetőségi döntéshez SOHA ne egyedül – határozókönyvvel és több bélyeggel ellenőrizd."},
    "oss-mpp-solar": {"tier": 3},
    "alpine-3244-extended-iso": {"bytes": 1_458_192_384, "size_status": M + ":content-length"},
    "tool-sumatra": {"download": {"method": "http", "urls": ["https://www.sumatrapdfreader.org/dl/rel/3.6.1/SumatraPDF-3.6.1-64-install.exe"]},
                     "bytes": 11_075_960, "bytes_est": None, "size_status": M + ":content-length"},
    "survivor-library-flash-drive": {"download": {"method": "manual", "url": "https://www.survivorlibrary.com/index.php/store/",
        "note": "pendrive a boltban; kategóriánkénti ZIP-ek: https://www.survivorlibrary.com/index.php/main-category-index/"}},
    "where-there-is-no-doctor": {"download": {"method": "manual", "url": "https://hesperian.org/",
        "note": "a 2025-ös fejezetenkénti PDF-ek külön tételként szerepelnek (hesperian-where-there-is-no-doctor-2025)"}},
}
for _k, _v in PATCH2.items():
    _d = PATCH.setdefault(_k, {})
    for _kk, _vv in _v.items():
        if _kk == "download" and isinstance(_d.get("download"), dict):
            _d["download"] = {**_d["download"], **_vv}
        else:
            _d[_kk] = _vv

# magyar stílus: oss/hub szövegek
_STYLE = [(r'"([^"\n]{1,80})"', r"„\1”"), (r"<->", "↔"), (r"(?<![<-])->", "→"), (r"Nem-lineáris", "Nemlineáris"),
          (r"\b(\d+)\.(\d+) ?(GB|MB|TB|kB)\b", r"\1,\2 \3"), (r"\b(\d+)\.(\d+)M\b", r"\1,\2 millió"),
          (r"\bdashboard(ok|ot|on|ja)?\b", lambda m: "irányítópult" + {"ok": "ok", "ot": "ot", "on": "on", "ja": "ja"}.get(m.group(1) or "", "")),
          (r"offline-first", "elsősorban offline"), (r"streamelés", "közvetítés"), (r"önhosztolt", "saját szerveren futó")]


def _style(t):
    import re as _r
    for a, b in _STYLE:
        t = _r.sub(a, b, t)
    return t

# --- 4. adat-átnézés (2026-11-14): mért értékek ---
OSMAND = [("budapest", 50700592), ("eszak-magyarorszag", 71024960), ("del-alfold", 61816441), ("kozep-dunantul", 71895326),
          ("eszak-alfold", 57575935), ("nyugat-dunantul", 63927851), ("del-dunantul", 57166149), ("pest", 112792975)]
PATCH3 = {
    "msf-essential-drugs": {"download": {"method": "http", "urls": [f"https://medicalguidelines.msf.org/sites/default/files/pdf/guideline-339-{l}.pdf" for l in ("en", "fr", "es", "ar")]},
                            "notes": "Angol, francia, spanyol és arab kiadás.", "bytes": 2_798_456 + 2_946_935 + 2_922_550 + 4_114_820, "size_status": M + ":content-length (4 nyelv)"},
    "open-library": {"download": {"method": "http", "urls": ["https://openlibrary.org/data/ol_dump_latest.txt.gz"]}, "bytes": 18_205_492_645,
                     "size_status": M + ":content-length"},
    "neets-navy-electricity-electronics": {"bytes": 132_000_000, "bytes_est": None, "size_status": M + ":archive.org metadata (*.pdf)"},
    **{i: {"subsumed_by": ["mek-oszk", "mek-oszk-szakmai"]} for i in ["pallas-nagy-lexikona", "revai-nagy-lexikona", "magyar-neprajzi-lexikon", "magyar-eletrajzi-lexikon"]},
    "whisper-cpp-models": {"download": {"method": "hf", "repo": "ggerganov/whisper.cpp", "include": ["ggml-medium.bin", "ggml-small.bin"]},
                           "bytes": 1_533_763_059 + 487_601_967, "size_status": M + ":hf-tree (medium + small; a turbo a hub-whisper tételben)"},
    "python-source-and-docs": {"download": {"method": "http", "urls": ["https://www.python.org/ftp/python/3.15.2/Python-3.15.2.tar.xz",
                               "https://docs.python.org/3.15/archives/python-3.15-docs-html.zip"]}, "bytes": 27_960_396 + 16_094_031, "size_status": M + ":content-length"},
    "linux-kernel-source": {"download": {"method": "http", "urls": ["https://cdn.kernel.org/pub/linux/kernel/v7.x/linux-7.3.4.tar.xz"]}, "bytes": 162_439_264, "size_status": M + ":content-length"},
    "calibre": {"download": {"method": "http", "urls": ["https://download.calibre-ebook.com/9.18.0/calibre-9.18.0-x86_64.txz"],
                "note": "Windows/macOS telepítő: https://calibre-ebook.com/download"}, "bytes": 240_948_148, "size_status": M + ":content-length (Linux)", "tier": 2},
    "osmand-hungary-maps": {"download": {"method": "http", "urls": [f"https://download.osmand.net/download?standard=yes&file=Hungary_{r}_europe_2.obf.zip" for r, _ in OSMAND]},
                            "bytes": sum(b for _, b in OSMAND), "size_status": M + ":osmand get_indexes (8 régió)"},
    "freecad-and-parts-library": {"tier": 2}, "kicad-eda-and-libraries": {"tier": 2}, "arduino-ide-offline": {"tier": 2},
    "devdocs-offline": {"tier": 2}, "zim-tools": {"tier": 2},
    "hub-tesseract-hun-best": {"bytes_est": None},
    "us-army-atp-4-02-11-first-aid": {"bytes": 14_300_000, "size_status": M + ":content-length (2 fájl összege)"},
    "oss-7zip": {"download": {"method": "http", "urls": ["https://www.7-zip.org/a/7z2606-x64.exe",
                 "https://github.com/ip7z/7zip/releases/download/26.06/7z2606-linux-x64.tar.xz", "https://github.com/ip7z/7zip/releases/download/26.06/7z2606-src.tar.xz"]},
                 "bytes": 1_659_704 + 1_575_552 + 1_567_328},
    "oss-memtest-smart": {"download": {"method": "http", "urls": ["https://memtest.org/download/v9.00/mt86plus_9.00.binaries.zip",
                          "https://github.com/smartmontools/smartmontools/releases/download/RELEASE_7_5/smartmontools-7.5.tar.gz"]}, "bytes": 383_461 + 1_122_317},
    "internet-in-a-box": {"bytes_est": 50_000_000},
}
for _k, _v in PATCH3.items():
    _d = PATCH.setdefault(_k, {})
    for _kk, _vv in _v.items():
        if _kk == "download":
            _d["download"] = _vv
        else:
            _d[_kk] = _vv
MULTI_FILE_DONE = {"linux-kernel-source", "calibre"}
_STYLE += [(r"cross-platform", "többplatformos"), (r"drag-and-drop", "fogd és vidd"), (r"all-in-one", "mindent egyben"), (r"\bdiskless\b", "lemez nélküli"),
           (r"\bsnapshot", "pillanatkép"), (r"\branswomware\b", "zsarolóvírus"), (r"\bransomware\b", "zsarolóvírus"), (r"(\d)\.(\d)B-s\b", r"\1,\2B-s")]
# --- 5. adat-átnézés (2026-11-14): mért értékek ---
GH = "https://github.com"
PATCH5 = {
    "ose-wiki-dump-gvcs": {"download": {"method": "archive.org", "ids": ["wiki-wiki.opensourceecology.org-20250809"], "glob": "*.7z"},
                           "bytes": 10_254_612_473, "size_status": M + ":archive.org metadata (images.7z)"},
    "devdocs-offline": {"download": {"method": "agent", "note": "Az alkalmazás: git clone https://github.com/freeCodeCamp/devdocs (Docker-képpel futtatható). A dokumentációk listája: https://documents.devdocs.io/docs.json → minden kért dokumentációhoz a <slug>/db.json és index.json letöltése; vagy a futó app „Offline” menüjéből.",
                        "seed_urls": ["https://github.com/freeCodeCamp/devdocs", "https://documents.devdocs.io/docs.json"]}},
    "primary-surgery-king-vol1-2": {"download_ids_add": ["primary-surgery-vol-2-trauma-2nd-edition"], "bytes": 188_418_039, "size_status": M + ":archive.org metadata (2 kötet)"},
    "pd-craft-classics-tanning-pottery-weaving-glass": {"download_ids_add": ["potterscraftprac00binnuoft", "handloomweavingp00hooprich", "glassblowing00shenrich"],
                                                        "bytes": 109_451_725, "size_status": M + ":archive.org metadata (4 könyv)"},
    "usbr-design-of-small-dams": {"glob": "designofsmalldam00unit.pdf", "bytes": 49_663_550},
    "practical-blacksmithing-richardson": {"glob": "practicalblacksm00richrich.pdf", "bytes": 15_585_506},
    "foundry-work-wendt-1923": {"glob": "foundryworktexto00wend.pdf", "bytes": 13_598_969},
    "rogers-industrial-chemistry-1912": {"glob": "2015.141919.Rogers-Industrial-Chemistry.pdf", "bytes": 50_576_173},
    "thomssen-soap-making-manual-1922": {"glob": "soapmakingmanua00thomgoog_text.pdf", "bytes": 9_961_906},
    "gebco-2026-grid": {"download": {"method": "http", "urls": ["https://dap.ceda.ac.uk/bodc/gebco/global/gebco_2026/ice_surface_elevation/netcdf/GEBCO_2026.zip?download=1"]},
                        "bytes": 4_252_016_343, "size_status": M + ":content-length (jégfelszíni rács, NetCDF)"},
    "freedos-14": {"download": {"method": "http", "urls": [f"https://www.ibiblio.org/pub/micro/pc-stuff/freedos/files/distributions/1.4/FD14-{x}.zip" for x in ("FullUSB", "LiveCD")]},
                   "bytes": 668_803_454 + 293_950_337, "size_status": M + ":content-length"},
    "arduino-ide-offline": {"download": {"method": "http", "urls": ["https://downloads.arduino.cc/arduino-1.8.19-linux64.tar.xz", "https://downloads.arduino.cc/arduino-1.8.19-windows.zip"]},
                            "bytes": 128_583_740 + 210_670_368, "size_status": M + ":content-length (Linux + Windows)"},
    "kicad-eda-and-libraries": {"download": {"method": "http", "urls": [f"{GH}/KiCad/kicad-source-mirror/releases/download/10.0.8/kicad-10.0.8-x86_64.exe"],
                                "note": "Linuxon a disztribúció csomagja; a könyvtárak a Windows-telepítőben vannak."}, "bytes": 969_079_176, "size_status": M + ":content-length (Windows, könyvtárakkal)"},
    "freecad-and-parts-library": {"download": {"method": "http", "urls": [f"{GH}/FreeCAD/FreeCAD/releases/download/1.1.4/FreeCAD_1.1.4-Linux-x86_64-py311.AppImage",
                                  f"{GH}/FreeCAD/FreeCAD/releases/download/1.1.4/FreeCAD_1.1.4-Windows-x86_64-py311-installer.exe"]},
                                  "bytes": 820_812_280 + 519_314_976, "size_status": M + ":content-length",
                                  "notes": "Az alkatrészkönyvtár külön, nagy git-repó: https://github.com/FreeCAD/FreeCAD-library (git clone --depth 1 elég)."},
    "ventoy": {"download": {"method": "http", "urls": [f"{GH}/ventoy/Ventoy/releases/download/v1.1.18/ventoy-1.1.18-linux.tar.gz",
               f"{GH}/ventoy/Ventoy/releases/download/v1.1.18/ventoy-1.1.18-windows.zip"]}, "bytes": 20_320_548 + 16_680_699, "size_status": M + ":content-length"},
    "hu-radioamator-vizsga-anyagok": {"bytes": 5_394_642, "size_status": M + ":content-length"},
    "npm-go-registries-note": {"info_url": "https://replicate.npmjs.com/"},
    "oss-yt-dlp": {"bytes_est": 3_500_000}, "oss-imagemagick": {"bytes_est": 14_000_000}, "oss-openscad": {"bytes_est": 23_100_000}, "oss-wireshark": {"bytes_est": 92_400_000},
    "oss-podman": {"bytes": None, "bytes_est": 21_400_000, "size_status": M + ":sekély klón (du)"},
}
MULTI_FILE_DONE |= {"worldclim-21", "natural-earth", "hydrosheds", "gebco-2026-grid", "freedos-14", "arduino-ide-offline", "kicad-eda-and-libraries", "freecad-and-parts-library"}
for _k, _v in PATCH5.items():
    _d = PATCH.setdefault(_k, {})
    for _kk, _vv in _v.items():
        _d[_kk] = _vv
_STYLE += [(r"(\d)\.(\d+)B\b", r"\1,\2B"), (r"(\d+)\.(\d+) pont", r"\1,\2 pont"), (r"offline-first", "elsősorban offline"), (r"\bworkflow", "munkafolyamat")]


# kézi fordítás a fordítás után módosult / kimaradt szövegekre
NOTES_FIX = {
    "osm-europe-pbf": {"notes": "A Geofabrik (download.geofabrik.de) a kutatáskor nem volt elérhető innen (kapcsolat bontva), ezért az OSM France tükör szerepel. A nyers adathoz megjelenítő/útvonaltervező szoftver kell (OsmAnd, Organic Maps, tilemaker, OSRM)."},
    "us-army-tm-9-237-welding": {"notes": "Újabb kiadás (1993/2004, TC 9-237) is létezhet, ezt nem ellenőriztük. Kiegészítő tétel: TM9-237-1MaterialsUsedforBrazingWeldingSoldering (1960)."},
    "survivor-library": {"size_human": "~200 GB+ (2021-es tükör: ~200 GB / 13 763 PDF; azóta bővült)"},
    "foxfire-book-series": {"notes": "Az archive.org-on kölcsönözhető példányok vannak (pl. foxfire-5-by-eliot-wigginton; a szerzői jogi helyzet tisztázatlan, szürke zónaként kezeld). Nyomtatott példányt érdemes venni."},
    "cheesbrough-district-laboratory-practice": {"notes": "ISBN: 1. rész 9780521676304, 2. rész 9780521676311. Az archive.org-on vannak feltöltések (district-laboratory-practice-in-tropical-countries-part-1: 6 768 991 B; -part-2: 7 357 296 B; „PD Mark” jelöléssel, ami szinte biztosan téves) – szürke zóna. Ajánlott: a nyomtatott kötetek megvásárlása. A cambridge.org termékoldala innen 403-at adott."},
    "unicef-practica-manual-drilling-toolkit": {"notes": "Fájlok (bájt): manual-drilling-series-augering 4 018 970; -jetting 3 080 303; -percussion 2 845 872; understanding-groundwater-wells-in-manual-drilling 2 701 878; Manual-Drilling-Techniques 384 671; Selection-of-Well-Construction-Methods 359 531 (mind a /content/uploads/2019/08/ alatt). Francia változatok is elérhetők."},
    "rachel-plus": {"size_human": "az alap tárhely nincs megadva; bővítés 880 GB / 1760 GB"},
}
for _k, _v in NOTES_FIX.items():
    PATCH.setdefault(_k, {}).update(_v)

NOTES_FIX2 = {
    "debian-full-archive-ftpsync": "Az összes kiadást tartalmazza (oldstable…unstable), ha nincs kizárva; az ftpsync ARCH_EXCLUDE beállításával vagy a debmirror-ral egy kiadásra szűkíthető. Tartsd be a tükrözési etikettet, és közeli rsync-tükröt válassz.",
    "rust-standalone-installer": "Az offline dokumentáció (rust-docs) benne van. A crate-ekhez helyi crates-tükör kell (lásd crates-io-mirror).",
    "internet-in-a-box": "A telepítőnek internet kell: még az összeomlás előtt futtasd, majd készíts képfájlt az SD-kártyáról. 2,4 GHz-es hotspot a régi eszközöknek. Legutóbbi git-tag: v7.0.9, az oldalon 8.3-as előzetes kiadás is van.",
    "babcock-wilcox-steam-1913": "Archive.org-tükör: https://archive.org/details/steamitsgenerati22657gut . Más kiadások szkennelései: steamitsgenerati00babc_0 (1894).",
    "kx-maps-hungary": "kiwix book=maps_en_hungary flavour=null. 605 227 506 bájt. Az európai változat (maps_en_europe) 26,7 GB. Átfed az OsmAnd/Geofabrik tételekkel, de csak Kiwix-olvasó kell hozzá.",
}
for _k, _v in NOTES_FIX2.items():
    PATCH.setdefault(_k, {})["notes"] = _v
PATCH.setdefault("usda-fooddata-central-sr-legacy", {}).update({"bytes": 6_074_592, "size_status": "measured:2026-11-14:content-length"})
PATCH.setdefault("ose-wiki-dump-gvcs", {}).update({"glob": "*.7z|*.zst", "bytes": 10_298_646_303})
try:
    _SSHU = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "research", "size_status_hu.json"), encoding="utf-8"))
except OSError:
    _SSHU = {}

NOTES_FIX3 = {
    "hu-radioamator-vizsga-anyagok": "jegyzet.pdf 5 394 642 B; az NMHH-rendelet HTML-ben 293 099 B. Hivatalos NMHH-kérdésbankot nem találtunk az interneten; további oktatási anyag: mrasz.hu.",
    "reticulum-nomadnet-sideband": "git ls-remote rendben: Reticulum 1.6.0, NomadNet 1.5.0, Sideband 2.3.0, RNode_Firmware v1.17. A Sideband APK kitalált fájlneve 404-et adott, ezért a valódi nevet a kiadási oldalon nézd meg. A pip-csomagokat így mentsd: pip download rns lxmf nomadnet sbapp.",
    "meshtastic-firmware-and-docs": "Kiadási ZIP-ek (bájt): esp32 40 071 234; esp32s3 227 052 406; nrf52840 58 645 536; rp2040 3 107 185; esp32c3 5 468 481; esp32c6 9 413 978 (minta: firmware-<plat>-2.8.2.d5f1619.zip). git ls-remote rendben: legutóbbi firmware-tag v2.8.2.d5f1619 (van v2.8.2.4c89b69 is), a dokumentáció repója github.com/meshtastic/meshtastic (HEAD 4097527c). Tükrözd a Meshtastic Android APK-t (F-Droid) és a webes flashelőt is.",
}
for _k, _v in NOTES_FIX3.items():
    PATCH.setdefault(_k, {})["notes"] = _v

NOTES_FIX4 = {
    "ham-digital-modes-fldigi-js8call-direwolf": "Mért (bájt): fldigi setup.exe 7 504 745; fldigi-4.2.13.tar.gz 5 244 946; fldigi_help.pdf 14 638 082; JS8Call win64 https://github.com/js8call/js8call/releases/download/v2.3.1/js8call-2.3.1-win64.exe 21 165 527 (összesen 48,6 MB). Dire Wolf: git https://github.com/wb2osz/direwolf, tag 1.8.1 (az archív tarball 403-at adott, git clone kell; ~10 MB, becsült). fldigi git: git.code.sf.net/p/fldigi/fldigi v4.2.13. Érdemes a Pat Winlinket is (github.com/la5nta/pat v1.0.1; a kiadási fájl neve nem volt megtalálható).",
    "omme-meheszet-egeszsegugy-hu": "OMME 2026-os szám 6 214 815 B + https://www.biokontroll.hu/wp-content/uploads/2013/04/mehbetegsegek_kezelese_megelozese.pdf 4 416 139 B. Régebbi OMME-szám: mehegeszsegugyi-ismeretek-20.pdf 6 454 498 B. Alapokhoz lásd még: Agrodok 32 és Peace Corps ICE.",
    "arxiv-bulk-s3": "Requester-pays: az AWS-adatforgalmat te fizeted. Ingyenes alternatíva: a Kaggle arXiv-metaadat (csak metaadat). Főleg kutatási szintű, közvetlen túlélési értéke kicsi.",
    "prusa-original-i3": "git clone --depth 1 https://github.com/prusa3d/Original-Prusa-i3 . Firmware hozzá: https://github.com/MarlinFirmware/Marlin (42 MB .git / 153 MB) vagy https://github.com/Klipper3d/klipper (12 MB / 230 MB, GPL-3.0). Az összeszerelési útmutatók online vannak (help.prusa3d.com), ezeket külön mentsd PDF-be.",
    "voron-2-4-and-trident": "git clone --depth 1 https://github.com/VoronDesign/Voron-2 ; git clone --depth 1 https://github.com/VoronDesign/Voron-Trident . Kereskedelmi alkatrészek kellenek (lineáris sínek, léptetőmotorok, vezérlőlapok), ezért csak a korai időszakban reális, amíg van készlet.",
    "npm-go-registries-note": "Az összeomlás előtt állíts be gyorsítótárazó proxyt: Verdaccio (npm) vagy Athens (Go), illetve projektenként „go mod vendor”.",
}
for _k, _v in NOTES_FIX4.items():
    PATCH.setdefault(_k, {})["notes"] = _v
PATCH.setdefault("bowditch-american-practical-navigator-2024", {}).update({"bytes": 206_875_030, "size_status": "measured:2026-11-14:content-length (2 kötet)"})
# GitHub-kiadás helyett meglévő bináris tétel (ne töltődjön le kétszer)
BINARY_ITEM = {"oss-freecad": "freecad-and-parts-library", "oss-calibre": "calibre", "oss-ventoy": "ventoy", "oss-kicad": "kicad-eda-and-libraries",
               "oss-arduino-ide": "arduino-ide-offline", "oss-meshtastic": "meshtastic-firmware-and-docs", "oss-cpython": "python-source-and-docs",
               "oss-alpine": "alpine-3244-extended-iso", "oss-7zip": "oss-7zip"}
for _k, _v in BINARY_ITEM.items():
    if _k != _v:
        PATCH.setdefault(_k, {})["binaries_item"] = _v

PATCH.setdefault("soilgrids-1km", {})["download"] = {"method": "wget-mirror", "url": "https://files.isric.org/soilgrids/latest/data_aggregated/1000m/",
                                                     "wget_args": "-l 2 -A tif -R index.html*"}

# --- végső szakértői átnézés (2026-11-15) ---
PATCH6 = {
    "usda-complete-guide-home-canning-2015": {"tier": 0},
    "special-forces-medical-handbook-st-31-91b": {"tier": 2},
    "who-model-formulary-2008": {"tier": 1},
    "katasztrofavedelem-lakossagi-kiadvanyok": {"tier": 1, "download": {"method": "http", "urls": [
        "https://jasz.katasztrofavedelem.hu/application/uploads/documents/2019-08/63348.pdf",
        "https://veszprem.katasztrofavedelem.hu/application/uploads/documents/2025-04/85885.pdf"]},
        "bytes": 857_985 + 927_997, "size_status": "measured:2026-11-15:content-length (2 PDF; a megyei oldalakon továbbiak)"},
    "voroskereszt-kiadvanyok": {"tier": 1},
    "kx-wp-en-med": {"subsumed_by": ["kx-wp-en-maxi"]},
    "fema-wood-gas-generator-1989": {"notes": "FIGYELEM: a fagáz szén-monoxidot tartalmaz – csak a szabadban üzemeltesd, CO-érzékelővel. 1 992 702 bájt. Másik szkennelés: archive.org DTIC_ADA208249 (3,4 MB). Bővített változat a Biomass Energy Foundation 2001-es jegyzeteivel: femasimplifiedwoodgasgeneratormar1989withbiomassenergyfoundation2001."},
    "hu-gomba-klasszikusok": {"notes": "FIGYELEM: a korabeli könyvek ehetőnek tartják a begöngyöltszélű cölöpgombát (Paxillus involutus), amely ma ismerten halálos vérbontó mérgezést okoz – gombát csak mai határozóval és szakellenőrrel. Istvánffy 102 793 181 B; Cserey https://www.mek.oszk.hu/10900/10910/10910.pdf 43 767 892 B. Egyik sem helyettesít egy mai határozót: vegyél egy friss magyar gombahatározót (pl. „Gombák – Képes határozó”, Kossuth, 2024; ár nem ellenőrzött)."},
    "ifrc-first-aid-guidelines-2020": {"notes": "4 432 256 bájt. Az ILCOR/ERC 2025 előtti kiadás – az újraélesztéshez az erc-guidelines-2025-layperson az irányadó."},
}
for _k, _v in PATCH6.items():
    PATCH.setdefault(_k, {}).update(_v)

# --- AI-ágens végső átnézés (2026-11-15) ---
AGENT_NOTE = "Gyűjteményoldal: a megjegyzésben (notes) leírt módon gyűjtsd ki a fájlokat, majd töltsd le őket; maradj a tétel tervezett méretén belül."
PATCH7 = {
    "where-there-is-no-psychiatrist-2018": {"download": {"method": "agent", "note": "A könyvoldalról gyűjtsd ki a 29 fejezet-PDF linkjét (/core/services/aop-cambridge-core/content/view/…/9781108683302c*_CBO.pdf), majd töltsd le őket.",
        "seed_urls": ["https://www.cambridge.org/core/books/where-there-is-no-psychiatrist/47578A845CAFC7E23A181749A4190B54"]}},
    "fao-better-farming-series": {"download": {"method": "agent", "note": "A teljes sorozat HTML-tükre (a CD3WD-ből): https://piku.codeberg.page/better_farming/INDEX.HTML – wget -m -np -k; az FAO EPUB-gyűjteményei: /fileadmin/user_upload/faoweb/e-books/BetterFarming/ (indexoldal nincs).",
        "seed_urls": ["https://piku.codeberg.page/better_farming/INDEX.HTML", "https://www.fao.org/fileadmin/user_upload/faoweb/e-books/BetterFarming/Food_Crops16.epub"]}},
    "attra-ncat-publications": {"download": {"method": "agent", "note": "WP REST API: https://www.ncat.org/wp-json/wp/v2/publication?per_page=100&page=N (X-WP-Total 375) → minden kiadvány oldaláról a .pdf linkek.",
        "seed_urls": ["https://www.ncat.org/wp-json/wp/v2/publication?per_page=100&page=1", "https://www.ncat.org/tools-and-media/?media-type=publication"]}},
    "pfaf-plants-for-a-future": {"download": {"method": "agent", "note": "A PFAF adatbázis tükrözése előtt KÉRDEZD MEG AZ EMBERT (engedélyt kell kérni a PFAF-tól); robots.txt-et tartsd tiszteletben, lassan (--wait=2).",
        "seed_urls": ["https://pfaf.org/user/Default.aspx"]}},
    "esa-worldcover": {"notes": "Csak a magyar csempék (N45/N48 × E015/E018/E021) – lásd a Leírás parancsát; a teljes globális térkép sok TB."},
    "worldclim-21": {"download": {"method": "http", "urls": [f"https://geodata.ucdavis.edu/climate/worldclim/2_1/base/wc2.1_2.5m_{v}.zip" for v in
        ("prec", "tmin", "tmax", "tavg", "srad", "wind", "vapr", "bio", "elev")]}, "bytes": 2_791_449_150,
        "size_status": "measured:2026-11-15:content-length (9 fájl, 2,5 ívperc)", "notes": "A teljes 2,5'-es éghajlati készlet (csapadék, hőmérséklet, sugárzás, szél, páratartalom, 19 bioklimatikus változó, domborzat) – termesztési zónákhoz bőven elég. Nagyobb felbontás (30\") és CMIP6-előrejelzések a forrásoldalon."},
    "natural-earth": {"notes": "A natural_earth_vector.gpkg.zip az összes vektorréteget tartalmazza (1:10m, 1:50m, 1:110m) egy fájlban. Utolsó kiadás 2022 (v5.1.x), stabil."},
    "hydrosheds": {"notes": "Európa folyói (HydroRIVERS v1.0, vízhozam-becsléssel és rendűséggel) – törpe vízerőmű helyének kiválasztásához. A tavak (HydroLAKES) és vízgyűjtők (HydroBASINS) a forrásoldalon."},
    "omsz-mentok-elsosegely": {"notes": "Az oldalon nincs PDF: mentsd el a HTML-t, és nyomtasd ki papírra. Az omsz.hu nem válaszolt, a mentok.hu működik. Egészítsd ki az ERC 2025 laikus irányelvvel (erc-guidelines-2025-layperson) és a Hesperian-könyvekkel.",
        "download": {"method": "agent", "note": "Az oldal(ak) mentése: wget -p -k <url>, vagy nyomtatás PDF-be", "seed_urls": ["https://www.mentok.hu/ha-baj-van/mit-tegyen-mig-megerkezik-a-mento/"]}},
    "wikem-emergency-medicine-wiki": {"download": {"method": "wget-mirror", "url": "https://www.wikem.org/wiki/Main_Page",
                                                   "wget_args": "-l 4 --reject-regex '(Special:|action=|oldid=|diff=|printable=)'"}},
    "esa-worldcover": {"download": {"method": "agent", "note": "Csak Magyarország csempéi (a teljes globális térkép sokkal nagyobb): aws s3 sync s3://esa-worldcover/v200/2021/map/ <cél> --no-sign-request --exclude '*' --include '*N4[5-8]E01[5-9]*' --include '*N4[5-8]E02[0-2]*'"}},
    "cd3wd-2012-dvd-isos": {"access": "free", "variant_role": "luxury", "license": "vegyes (harmadik felek dokumentumai, a CD3WD-projekt nyilvános tükrén terjesztve – mint a kx-cd3wd ZIM)"},
    "agromisa-agrodok-series": {"download": {"method": "agent", "note": "CGSpace DSpace API: https://cgspace.cgiar.org/server/api/discover/search/objects?query=agrodok&dsoType=ITEM (313 találat) → az angol Agrodok-füzetek bitstreamjei (/server/api/core/bitstreams/<uuid>/content); minta: AD32.pdf 1 053 178 B. Maradj ~55 MB-on belül."}},
    "kx-cd3wd": {"variant_role": "pref"},
    "kx-khan": {"tier": 3}, "kolibri-khan-academy": {"tier": 3},   # 1 TB-on a gyakorlati tier 0–1 anyag elsőbbséget kap
}
for _k, _v in PATCH7.items():
    _d = PATCH.setdefault(_k, {})
    for _kk, _vv in _v.items():
        if _kk == "download" and isinstance(_d.get("download"), dict) and "method" not in _vv:
            _d["download"] = {**_d["download"], **_vv}
        else:
            _d[_kk] = _vv


# hiányzó leírás / méret (validátor: 2026-11-14)
EXTRA_DESC = {
    "llm-gemma-4-e2b-it-ultra-uncensored-heretic-": "Gemma 4 E2B (kb. 2 milliárd effektív paraméter) Heretic-eljárással cenzúrázatlanított változata. Telefonon és 8 GB-os laptopon is gyorsan fut; tudása szerény, egyszerű kérdés-válaszra, fordításra és vázlatírásra jó.",
}
EXTRA_SIZE = {"oss-openfda": 3_000_000_000}
# a kutatás a teljes tartalmas telepítést (2 TB) írta – a tartalom (ZIM, Kolibri, OSM) külön tételként szerepel, itt csak a telepítő kell
SIZE_OVERRIDE = {"oss-internet-in-a-box": 50_000_000}   # becsült: drug/label + event részhalmaz zip JSON


_NHU = None


def _notes_hu():
    global _NHU
    if _NHU is None:
        try:
            _NHU = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "research", "notes_hu.json"), encoding="utf-8"))
        except OSError:
            _NHU = {"notes": {}, "size_human": {}}
    return _NHU

# kézi tételek: az URL-mezőben csak URL, a magyarázat a note-ba (magyarul)
MANUAL_URL = {
    "apt-mirror-debmirror": ("https://github.com/apt-mirror/apt-mirror", "git: https://github.com/apt-mirror/apt-mirror ; Debianon: apt install debmirror"),
    "kiwix-hotspot": ("https://get.kiwix.org/en/shop/", "csak az OS-képek, fizetős letöltés"),
    "rachel-plus": ("https://rachel.worldpossible.org/", "az ingyenes tartalommodulok itt érhetők el"),
    "hathitrust": ("https://babel.hathitrust.org/", "kötetenként; a teljes PDF többnyire csak tagintézményi belépéssel"),
    "google-books-pd": ("https://books.google.com/", "könyvenként „PDF letöltése” a teljes nézetű (közkincs) tételeknél"),
    "hungaricana": ("https://library.hungaricana.hu/", "oldalankénti / dokumentumonkénti PDF-export (a korlátok nem ellenőrzöttek)"),
    "tankonyvkatalogus-oh": ("https://www.tankonyvkatalogus.hu/", "címenkénti PDF-letöltés a katalógusban (az OH tulajdonában lévő tankönyvek)"),
    "digitalis-tankonyvtar": ("https://www.tankonyvtar.hu/", "könyvenkénti PDF-letöltés (bejelentkezés kellhet, nem ellenőrzött)"),
    "voroskereszt-kiadvanyok": ("https://voroskereszt.hu/kiadvanyaink/", "valamint: https://voroskereszt.hu/katasztrofak/felkeszules-a-katasztrofakra/"),
    "lechner-terkepek": ("https://map.lechnerkozpont.hu/", "nézegető; az adatok a Lechner Tudásközponttól rendelhetők (fizetős)"),
}
_SS_KIND = {"measured": "measured", "estimated": "estimated", "official": "official", "mért": "measured", "becsült": "estimated"}


def _norm_size_status(v):
    """size_status egységesítése: <measured|estimated|official>:<dátum>:<forrás>."""
    v = str(v or "")
    if v in ("measured", "estimated", "official"):
        return f"{v}:2026-11-14:forrás nincs megadva"
    m = re.match(r"^(measured|estimated|official)\((.*)$", v, re.S)        # kind(forrás) [+ folytatás]
    if m:
        src = m.group(2)
        depth, cut_at = 1, None
        for i, ch in enumerate(src):                   # a nyitó zárójel párja
            depth += ch == "("
            depth -= ch == ")"
            if depth == 0:
                cut_at = i
                break
        body = (src[:cut_at] + src[cut_at + 1:]) if cut_at is not None else src
        kind = "estimated" if re.search(r"estimated|becsült", body) and m.group(1) == "measured" else m.group(1)
        return f"{kind}:2026-11-14:{body.strip()}"
    m = re.match(r"^(measured|estimated|official):(\d{4}-\d{2}-\d{2}):?(.*)$", v, re.S)
    if m:
        return f"{m.group(1)}:{m.group(2)}:{m.group(3).strip() or 'forrás nincs megadva'}"
    return v


def apply(items):
    out, seen = [], set()
    for it in items:
        if it["id"] in DELETE or it["id"] in seen:     # azonos id két kutatásból: az első (részletesebb) marad
            continue
        seen.add(it["id"])
        it = _clean_null(it)
        dl = it.get("download") or {}
        if isinstance(dl.get("include"), list):
            dl["include"] = [x for x in dl["include"] if x not in ("null", "None", None, "")]
        if it.get("bytes", 0) is None:
            it.pop("bytes")
        if it["id"] in LANG:
            it["lang"] = LANG[it["id"]]
        elif it.get("lang") not in ("hu", "en", "multi"):
            it["lang"] = "multi" if "," in str(it.get("lang")) else "en"
        if not (it.get("desc_hu") or "").strip() and it.get("group") in EXTRA_DESC:
            it["desc_hu"] = EXTRA_DESC[it["group"]]
        if it["id"] in SIZE_OVERRIDE:
            it.pop("bytes", None); it["bytes_est"] = SIZE_OVERRIDE[it["id"]]
            it["size_human"] = "~20–50 MB (csak a telepítő; a tartalom a katalógus ZIM-, Kolibri- és térképtételeiből jön)"
        if it["id"] in EXTRA_SIZE and not it.get("bytes"):
            it["bytes_est"] = EXTRA_SIZE[it["id"]]
        p = PATCH.get(it["id"])
        if p:
            for k, v in p.items():
                if v is None:
                    it.pop(k, None)
                else:
                    it[k] = v
        if it["id"] in MANUAL_URL and (it.get("download") or {}).get("method") == "manual":
            u, note = MANUAL_URL[it["id"]]
            it["download"] = {**it["download"], "url": u, "note": note}
        if it.get("size_status"):
            it["size_status"] = _norm_size_status(it["size_status"])
            if it["id"] in _SSHU:
                kind_date = ":".join(it["size_status"].split(":")[:2]) if re.match(r"^\w+:\d{4}-", it["size_status"]) else "estimated:2026-11-14"
                it["size_status"] = f"{kind_date}:{_SSHU[it['id']]}"
        if p and "glob" in p:
            it["download"]["glob"] = it.pop("glob")
        if p and "download_ids_add" in p:
            ids = it["download"].setdefault("ids", [])
            ids += [x for x in it.pop("download_ids_add") if x not in ids]
        if (it.get("download") or {}).get("method") == "archive.org" and not it["download"].get("glob") and "PDF" in str(it.get("format", "")).upper():
            it["download"]["glob"] = "*.pdf"
        if not it["cat"].startswith("ai_models"):
            for k in ("notes", "size_human"):          # angol megjegyzések magyarul (csak ha a forrásszöveg azóta nem változott)
                tr = _notes_hu()[k].get(it["id"])
                if tr and it.get(k) == tr[0]:
                    it[k] = tr[1]
            for k in ("desc_hu", "need_hu", "alternatives"):
                if isinstance(it.get(k), str):
                    it[k] = _style(it[k])
            if isinstance(it.get("need_hu"), str):
                it["need_hu"] = it["need_hu"].rstrip(". ")
        dm = (it.get("download") or {}).get("method")
        if dm == "jigdo":      # automatikus: a select_items jigdo-lite --noask ciklust ír (a könyvtár .jigdo fájljaira)
            it["download"] = {"method": "jigdo", "url": it["download"].get("url")}
        elif dm == "s3" or it["id"] == "debian-full-archive-ftpsync":
            src = it["download"].get("url") or ""
            how = {"s3": "AWS CLI-vel (aws s3 sync … --no-sign-request; fizetős vödörnél --request-payer requester, előtte költségbecslés)",
                   "jigdo": "jigdo-lite-tal (apt install jigdo-file; jigdo-lite <…>.jigdo) – a .jigdo fájlok a megadott könyvtárban vannak",
                   "rsync": "Debian ftpsync-kel (https://salsa.debian.org/mirror-team/archvsync) – helyi tükör beállítása, nem egyszerű rsync"}[
                   "rsync" if it["id"] == "debian-full-archive-ftpsync" else dm]
            it["download"] = {"method": "agent", "note": f"Letöltés {how}. Forrás/parancs: {src}", "seed_urls": [u for u in re.findall(r"(?:https?|s3)://\S+", str(src))]}
        if it["id"] in MULTI_FILE and it["id"] not in MULTI_FILE_DONE and it.get("download", {}).get("method") == "http":
            urls = it["download"].get("urls") or []
            # az ismert fájlok automatikusan jönnek; a további fájlok AI-feladatként (todo_note) – így nem vész el az életmentő alap
            it["download"] = {**it["download"], "todo_note": "a készlet további fájljai a megjegyzésben (notes) és a forrásoldalon: " + (it.get("info_url") or "")}
        if it.get("cat") == "gpu_unlock":
            sc = it.setdefault("scores", {})
            sc["S"] = 0
            sc["R"] = min(sc.get("R", 0), GPU_UNLOCK_R.get(it["id"], 2))
        if it.get("cat", "").startswith("ai_models"):
            # FP8-natív checkpointok bitszáma; Kiwix/kx-se szöveg; requires
            if re.search(r"native", it["id"]) and re.search(r"mimo-v2-6-pro|step-5-preview", it["id"]):
                it["llm_bits"] = 8.5
            if it["download"].get("method") == "ollama":
                it.setdefault("requires", ["tool-ollama-installers"])
            elif it.get("platform") == "any":
                it.setdefault("requires", ["ai-llamacpp-binaries"])
        if it["id"] == "llm-nemotron-3-5-ollama-ollama-4" or (it.get("download", {}).get("tag") == "nemotron-3.5-bolt:74b-a9b"):
            it["active_b"], it["moe"] = 9, True
        d = it.get("desc_hu") or ""
        for a, b in HU_DESC.get(it["id"], []):
            d = d.replace(a, b)
        if it["id"].startswith("kx-se-") and "Q&A" in d:
            d = d.replace(" Q&A", " – kérdés-válasz gyűjtemény (Stack Exchange)").replace("Q&A", "kérdés-válasz gyűjtemény (Stack Exchange)")
        for a, b in GENERIC_HU:
            d = d.replace(a, b)
        d = re.sub(r"'([^']{3,60})'", r"„\1”", d)
        if d:
            it["desc_hu"] = d
        out.append(it)
    return out
