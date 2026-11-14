OVERRIDES = {
 "_drop": ["ollama-runtime-placeholder", "kiwix-tools-serve", "nomic-embed-text-placeholder"],
 "debian-13-amd64-dvd1-iso": {"group": "debian", "variant_rank": 1},
 "debian-13-amd64-bd-jigdo-set": {"group": "debian", "variant_rank": 2, "variant_role": "pref"},
 "debian-full-archive-ftpsync": {"group": "debian", "variant_rank": 3, "variant_role": "luxury"},
 "geofabrik-hungary-pbf": {"group": "osm", "variant_rank": 1},
 "osm-europe-pbf": {"group": "osm", "variant_rank": 2, "variant_role": "pref"},
 "kolibri-khan-academy": {"group": "khan", "variant_rank": 2},
 "enwiki-pages-articles-xml": {"subsumed_by": ["kx-wp-en-maxi", "kx-wp-en-nopic"]},
 "huwiki-pages-articles-xml": {"subsumed_by": ["kx-wp-hu-maxi", "kx-wp-hu-nopic"]},
}
OVERRIDES.update({
 "rachel-world-possible": {"tier": 4, "notes": "Nagyrészt átfedés a Kiwix-anyagokkal (Wikipedia, Khan, Gutenberg) – csak nagy tárhelyen érdemes."},
 "protomaps-planet-pmtiles": {"tier": 3},
 "fdroid-repo-mirror": {"tier": 5, "notes": "Az összes app minden verziója; a fontos APK-k a tool-fdroid-repo-apks tételben vannak."},
})
