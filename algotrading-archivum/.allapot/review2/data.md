# Adatbeszerző – 2. kör: 86,7 (1. kör 75,7); javítás után ~93,2; forráskorlát: a ~93, b ~95, c ~93, d ~96
a 84 · b 89 · c 86 · d 94 · e 80 · f 87. Dry-run 409/409 OK; guard python-fallback OK; 12 hf repo él; link-minta 100: 0 halott; célzott 16: 14 OK, nbs-china reset, ec-business-consumer-surveys 404.
1 (a) A1 data 67 sor: license null 40, redistribution 9/67, exchange_fees 7/67, history_from null 31; cme-datamine minden mező null; kripto adat redistribution 0/49; A3 adat license 11/55 → kitölteni, ahol nem publikus: "ajánlatkérés szükséges" (+6).
2 (a) A3 predikciós/sport adatsorokon nincs pit / revision_policy / timestamp_semantics (+1).
3 (b) PIT-mezők nagyrészt helyőrzők (401 sorból revision_policy null 352, timestamp_semantics 356, pit 359, pit_source „nem ellenőrzött…” 342) → legalább a 0–1. szintű A4 sorok; ahol nincs vintage: pit:false + „saját pillanatkép” (+4).
4 (b) history_from null: ecb-rtd-euro-area, oecd-revisions-db, wrds-ibes, wrds-compustat-snapshot (+1).
5 (c) lseg-news-mrn „egyedi ajánlat (nem publikus) (~1 357 €/hó) (mért)” ellentmondás (+2).
6 (c) Ingyenes szinten módszer-sorok („Módszer: Vantage…” ×2), cikk (Cont–Kukanov–Stoikov 2014), infra-tények (binance-aws-tokyo-region, Hyperliquid AWS-Tokió) → budget_section zárja ki: M13 Tudás, execution-quality módszer, *-infrastruktura tény (+2).
7 (c) 324 fizetős/freemium/intézményi tételnek nincs price_eur_month; 130 árazott tételen price_verified null („nincs jelölve”: Xetra, Euronext, LSE, Compustat, I/B/E/S, PrimeXM); lmax-global „nem ellenőrzött (becsült)” → nem publikus árnál price_verified „nem ellenőrzött” vagy „egyedi ajánlat”; Profi szint csak 18 sor (+3).
8 (d) 133 pitfalls_hu és 31 api_detail "" → null (+0,5).
9 (d) ec-business-consumer-surveys 404 (nem 429) → új oldal; nbs-china és reloc-monaco csak főoldal → mélylink (+1,5).
10 (e) download.files[] 0 tételen; csak 13 fájl, ebből 7 adat; 342 ingyenes adatszerű tételből 258 nincs szkriptelve, nincs TODO-lista (117 regisztrációs sem) → files[]: Ken French CSV zip, ECB eurofxref-hist.zip, KSH HVD, ÁKK referenciahozamok, Philly RTDSM xlsx, FRED-MD csv, Bybit/Binance havi zip; minden szkripteletlen ingyenes/regisztrációs tételre echo "TODO <id> <ok>" (+8).
11 (e) alap-UA kapcsolat nélkül → SEC 403 (igazolva); „név email@domain” formával 200 → SEC-sorok leállnak, ha $UA-ban nincs @ (+2).
12 (e) FILE_RE-ből hiányzik .xml (ecb-eurofxref kimarad); guard engedi $HOME, /usr/*, /var/* → ALLOW_DEST=1 nélkül tiltani; méret-figyelmeztetés (bytes_est) a több GB-os hf-sufe-aiflm-lab-fin-r1 előtt (+2).
13 (f) GKI konjunktúraindex hiányzik; nincs szkriptelve: MNB SOAP (POST http://www.mnb.hu/arfolyamok.asmx; HTTPS-en a POST 404), KSH HVD (data.ksh.hu/datasets.json, 13 adatkészlet), ÁKK referenciahozamok export (+6).
