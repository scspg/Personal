# Kockázat/jog – 2. kör: 89,0 (1. kör 81,8); javítás után ~93,7
a 93 · b 92 · c 85 · d 89 · e 86 · f 89. Újraszámolt számok mind egyeznek (reflexió rövid oldal 1,21%/14,74%; farokkapu MC; sokknapok; visszajátszás; §5.3 stressztábla; margin-példák; méretezési golden teszt 733 USD minimum; HTML átlag).
1 (a) grid-MC nem független (az appendix az átnéző grid_mc.py-ja) → független eseményvezérelt motor a valódi stratégiakóddal (spec §6.6) mint kapu, ±2 százalékpont egyezés a referencia-griden.
2 (a) spec §6.2 stressz-forgatókönyv kitöltési szabálya kétértelmű („hiányzó mozgás a legközelebbi devizalábbal” → EURUSD kaphatja a CHF −14,4%-át, 1,7E vs 5,4E) → minden forgatókönyv-dátumra teljes ECB keresztmetszet (párok tényleges mozgása); csak a pálya kedvezőtlen oldalán lévő szintek, nem |x| mindkét oldalra.
3 (a) HTML: „Nulla alá ment stop-outok X%” minden pályára oszt (54/400 = 13,5%), az a7 a stop-outok 23,4%-át írja → osztás ruin-nal vagy átcímkézés; mcalc lábjegyzetből hiányzik az FX-tényező.
4 (b) 12. fejezet 968. sor „1:500 legálisan, EU-s felügyelet mellett is elérhető” → ugyanabba a pontba: ≤10× belefér a 30:1 lakossági keretbe, pro-státusz nem kell józan méretezéshez.
5 (c) Revolut: felfüggesztés 2025-07-04/05 (hvg 2025-07-05), teljes kivonulás/számlazárás 2025-12-18 – két külön esemény; a 2025-07-17 hibás (a8 §5.3, 5. fejezet, JSONL).
6 (c) ETÜ veszteség-ablak: 67/A (6)–(8) szerint a t. évi veszteség t−2…t+2 ETÜ-adóját csökkentheti → „visszafelé és előre két-két év (összesen öt adóév), az adott évi bevallásban a tárgyév és az előző két év ETÜ-adójáig” (a8, 12. és 10. fejezet egységesen).
7 (c) 10. fejezet 3652. sor kriptoveszteség „időkorlát nélkül” → „legfeljebb a tárgyév és az előző két év kriptoadójáig”.
8 (d) pro-kritériumok: Bszt. 49. § (1) magyar cégekre; CySEC-jogalanyok (Pepperstone EU, FP Markets EU) ciprusi átültetést és saját „jelentős méret” definíciót alkalmaznak.
9 (d) 5. fejezet 1361., 1363. sor (MiCA, DAC8, a2 JSONL) „Nem ellenőrzött részletek” → mért, a 17. fejezettel egyezően.
10 (e) 4. fejezet (A1) 653., 668. sor „jellemzően Vantage Global Limited (VFSC 700271) [mért]” → történeti, utalás VIG Group / ügyfélszerződés.
11 (e) AFM tétel (655., 681., 889. sor) „mért” → másodlagos (Finance Magnates 2024-11-13), az AFM elsődleges oldal nem volt elérhető.
12 (f) OPA fail-open hiányzó bemenetre (spec §7.2): ctx.post_trade_eff_leverage vagy ctx.stress_loss_pct hiánya → to_number undefined → nincs deny; data.risk.* hiánya ugyanígy → deny contains "MISSING_INPUT" minden kötelező mezőre (vagy bemeneti séma); opa test hiányzó és nem numerikus értékre.
13 (f) exit_order csak méretet néz, irányt nem: MT5 hedging számlán az ellentétes megbízás hedge-et nyit → ellentétes oldal + hedging számlán close-by-ticket vagy position_id; teszt: azonos oldali reduce_only elutasítva.
14 (f) TOTP a /kill-en (spec §6.5 K6) a biztonságos irányban súrlódás → engedélyezett listáról /kill TOTP nélkül; TOTP csak visszakapcsoláshoz, szintemeléshez, limitlazításhoz.
Forráskorlát: (e) ~90 (Vantage/VIG ügyfélszerződés PDF 403, AFM elsődleges, Mauritius FSC GB20026165 nyilvántartás); (c) ~93 (nincs NAV-szöveg/állásfoglalás a nem-ETÜ CFD egyéb jövedelemként kezeléséről és a Polymarket-besorolásról); (d) FCA COBS 22.5 elsődleges forrásból valószínűleg pótolható.
