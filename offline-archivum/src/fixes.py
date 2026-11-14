#!/usr/bin/env python3
"""Adatjavítások a minőségellenőrzés (QA) alapján – a build minden futáskor alkalmazza (apply(items) -> items).
Egy helyen, újrafuttathatóan: nyelvi enumok, letöltési blokkok, duplikátumok, tierek/pontok, magyar szövegek."""
import re

DELETE = {"village-earth-at-library"}          # azonos a village-earth-appropriate-technology-library tétellel

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
    "kx-gardenology": {"download": {"method": "kiwix", "book": "gardenology.org_en_all", "flavour": None}},
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
                           "bytes": 2595406221, "size_status": "measured:2026-11-14:hf-api", "subsumed_by": ["hub-whisper-cpp-large-v3-turbo"]},
    "piper-tts-hu": {"download": {"method": "hf", "repo": "rhasspy/piper-voices", "include": ["hu/*"]}, "bytes": 189988337,
                     "size_status": "measured:2026-11-14:hf-api (hu/ mappa, 12 fájl)", "size_human": "190 MB", "subsumed_by": ["hub-piper-hu-voices"]},
    "argos-translate-hu": {"subsumed_by": ["hub-argos-translate-hu"]},
    **{i: {"bytes_est": 50_000_000, "size_status": "estimated:git mirror (Markdown lista)"} for i in
       ["hub-awesome-selfhosted", "hub-awesome-sysadmin", "hub-awesome-open-hardware", "hub-awesome-public-datasets", "hub-awesome-meta"]},
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


def apply(items):
    out = []
    for it in items:
        if it["id"] in DELETE:
            continue
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
        p = PATCH.get(it["id"])
        if p:
            for k, v in p.items():
                it[k] = v
        dm = (it.get("download") or {}).get("method")
        if dm in ("s3", "jigdo") or it["id"] == "debian-full-archive-ftpsync":
            src = it["download"].get("url") or ""
            how = {"s3": "AWS CLI-vel (aws s3 sync … --no-sign-request; fizetős vödörnél --request-payer requester, előtte költségbecslés)",
                   "jigdo": "jigdo-lite-tal (apt install jigdo-file; jigdo-lite <…>.jigdo) – a .jigdo fájlok a megadott könyvtárban vannak",
                   "rsync": "Debian ftpsync-kel (https://salsa.debian.org/mirror-team/archvsync) – helyi tükör beállítása, nem egyszerű rsync"}[
                   "rsync" if it["id"] == "debian-full-archive-ftpsync" else dm]
            it["download"] = {"method": "agent", "note": f"Letöltés {how}. Forrás/parancs: {src}", "seed_urls": [u for u in re.findall(r"(?:https?|s3)://\S+", str(src))]}
        if it["id"] in MULTI_FILE and it.get("download", {}).get("method") == "http":
            urls = it["download"].get("urls") or []
            it["download"] = {"method": "agent", "note": "Több fájlból álló készlet: a kiinduló URL mellett a megjegyzésben (notes) és a forrásoldalon felsorolt további fájlok is kellenek.",
                              "seed_urls": urls + ([it["info_url"]] if it.get("info_url") else [])}
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
