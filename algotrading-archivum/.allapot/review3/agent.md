# AI-ágens – 3. kör: 95,0 (78,7 → 91,3 → 95,0); minden ≥93
a 93 · b 94 · c 93 · d 99 · e 95 · f 96. Validátor 0 típushiba; újraépítés bájtazonos, ZIP determinisztikus, 54 tag; dry-run 434 OK; F0.1 408 teszt (uv 0.13.6), F0.3 pip-audit tiszta, F0.6 OK; séma-szinkron 402/402 és 379/379; kalkulátorok 17/17.
1 (a,b) adattétel-definíció vs adat: 546-ból 144 adattételen nincs PIT-kulcs (42 a3, kripto-cex-api ×12, kripto-mev-mempool ×12, infra, research) → [JAVÍTVA buildben: kizárási lista + null-kitöltés]
2 (b) 3 elemzési sor link nélkül (a11-broker-xm-global→xm-trading-point, a11-pro-lmax→lmax-global, a11-plat-execution-latency-profiles→lmax-global); 2 related_ids nem létező id-re (vantage-account-types, hu-szja-tv-29-egyeb-jovedelem); beágyazott "" (github.license ×36, strategiak notes_hu ×26) → [JAVÍTVA: rekurzív null, related_ids feloldás]
3 (c) MAX_GB csak hf-en, mind 0 → [JAVÍTVA: HF API méret, ismeretlen tiltva, curl Content-Length]
4 (c) FinGPT/fingpt-sentiment-train kétszer → [JAVÍTVA]
5 (c) SEC-tipp idézőjel nélkül → [JAVÍTVA]
6 (e) syrupy==2026.4.6.124150327040 visszavont (yanked); PYTHON_VERSION=3.12.16 nem kényszerített (nincs .python-version, uv rendszer 3.12.3-at vett); [tool.uv] required-version "==0.13.6" más uv-n elbukik, nincs telepítési lépés → visszavonatlan syrupy, .python-version 3.12.16, F0-ban pip install uv==0.13.6 vagy uv self update 0.13.6.
7 (f) teljes chat 128k kontextust igényel – elfogadható a mini mellett.
