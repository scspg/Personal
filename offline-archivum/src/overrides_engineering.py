E = "https://www.energy.gov/sites/default/files/2026-04/"
DOE = ["DOE-HDBK-1010-92.pdf"] + [f"DOE-HDBK-1011-92_VOL{i}.pdf" for i in range(1,5)] + [f"DOE-HDBK-1012-92_VOL{i}.pdf" for i in range(1,4)] \
    + [f"DOE-HDBK-1014-92_VOL{i}.pdf" for i in (1,2)] + [f"DOE-HDBK-{n}-93_VOL{i}.pdf" for n in (1015,1016,1017,1018,1019) for i in (1,2)]
NA = "https://thenauticalalmanac.com/"
OVERRIDES = {
 "_drop": ["cd3wd-2012-dvd-set"],
 "doe-fundamentals-handbooks": {"download": {"method": "http", "urls": [E + f for f in DOE]},
    "notes": "A DOE-HDBK-1010-92 fájlnév ellenőrizetlen (lehet VOL nélküli vagy _VOL1); 404 esetén próbáld a másikat. 1013 (műszerezés): archive.org doe-hdbk-1013-1-92, doe-hdbk-1013v-2. A mappa dátuma (2026-04) változhat."},
 "us-army-construction-fms": {"download": {"method": "archive.org", "ids": ["FM_5_428_C_M_1998", "FM_5_426_C_1995", "fm-5-125-rigging-techniques-procedures-and-applications-1995"], "glob": "*.pdf"}},
 "neets-navy-electricity-electronics": {"download": {"method": "archive.org", "ids": ["neetsmodules_202003"], "glob": "*.pdf"}, "bytes_est": 1_500_000_000, "size_status": "estimated:csak PDF-ek (a 5 GB nagy része jp2.zip)"},
 "survivor-library": {"download": {"method": "wget-mirror", "url": "https://www.survivorlibrary.com/index.php/main-category-index/", "wget_args": "-l 3 -A pdf,zip -nc"},
    "bytes_est": 200_000_000_000, "size_status": "estimated:173-200 GB (közösségi adatok 2019/2021)"},
 "voron-2-4-and-trident": {"download": {"method": "git", "repos": ["https://github.com/VoronDesign/Voron-2", "https://github.com/VoronDesign/Voron-Trident"]}},
 "engineering-toolbox": {"download": {"method": "manual", "note": "Csak kiválasztott táblák PDF-be nyomtatása (ÁSZF)."}, "access": "free"},
 "bowditch-american-practical-navigator-2024": {"download": {"method": "http", "urls": [
    NA + "2024_Bowditch-_American_Practical_Navigator/Volume_1/Bowditch_Vol_1_2024.pdf",
    NA + "2024_Bowditch-_American_Practical_Navigator/Volume_2/Bowditch_Vol_2_2024.pdf"]}},
 "nautical-almanac-and-sight-reduction-tables": {"download": {"method": "http", "urls":
    [NA + "TNARegular/2026_Nautical_Almanac.pdf"] + [NA + f"Pub_No_229/Pub229Vol{i}.pdf" for i in range(1, 7)] +
    [NA + "Tables/TABLE_4-_GHA_and_Declination_of_the_Sun_for_the_Years_2001_to_2036.pdf", NA + "GHA_Aries_Long_Term/GHA_Aries_2022_to_2030.pdf"]}},
 "navedtra-trade-manuals-everyspec": {"download": {"method": "wget-mirror", "url": "https://everyspec.com/USN/NAVEDTRA/", "wget_args": "-l 2 -A pdf -nc"}},
 "farm-hack-tools": {"bytes_est": 500_000_000, "size_status": "estimated:HTML + mellékletek"},
}
OVERRIDES["survivor-library"].update({"group": "survivor", "variant_rank": 2})
