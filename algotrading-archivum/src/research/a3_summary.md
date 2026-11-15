# A3 – M5 Predikciós piacok és sportfogadás: összefoglaló

Ellenőrzés napja: 2026-11-15. Tételek száma: 112 (`a3_predict_sports.jsonl`). Ebből 66 mért, 42 becsült, 4 nem ellenőrzött.
Árfolyam (ECB, 2026-11-13): 1 EUR = 1.1052 USD = 0.83559 GBP. Ezzel számoltuk az EUR/hó értékeket, ezek becsültek.

## Fő megállapítások (címke zárójelben)
1. **A Polymarket API-ja átalakult (mért).** A Data API v1-et kivezették, a végpontok ma a `/v2` alatt vannak. A `py-clob-client` 2026-05-25-én archiválva lett, az utódja a `Polymarket/py-sdk`. A CLOB V2 exchange-re álltak át, új szerződéscímekkel (a NautilusTrader-docs szerint pUSD collateral). Így a 2025 előtt írt nyílt forrású botok nagy része nem működik.
2. **A Polymarket díjmentes korszaka véget ért (mért, docs).** A taker díj képlete `C × r × p(1−p)`, ahol r = 0.04–0.07 kategóriától függően (a geopolitika 0). A makerek nem fizetnek, és 15–25% rebate-et kapnak. A Kalshi díja ugyanilyen alakú: `roundup(0.07·C·P(1−P))`. A 2024–2025-ös arbitrázs- és FLB-tanulmányok számait ezért lefelé kell korrigálni.
3. **A Pinnacle referencia-ár kiesett (mért).** A Pinnacle API 2025-07-23 óta zárva van a nyilvánosság előtt. A football-data.co.uk PL-fájljában a Pinnacle-oszlopok 2026-01-08 után üresek (210/380 meccsnél van adat), a 2026/27-es fájlból pedig hiányoznak. A CLV-referencia ezentúl a Betfair Exchange záró ára (358/380 meccsnél van adat) vagy több sharp iroda konszenzusa.
4. **Az FBref elvesztette az Opta haladó adatait, és ez hatással van a fogadási feature-ökre (becsült).** 2026 januárjától nincs xG, progresszív passz és SCA. Ingyenes xG-pótlásnak az Understat és a StatsBomb Open Data marad.
5. **A Kalshi makró-piacai valódi FX- és index-jelek (becsült).** A Fed FEDS 2026-010 tanulmány szerint a fed funds előrejelzésük a dealer survey szintjén van, CPI-n pedig kisebb a hibájuk, mint a Bloomberg-konszenzusé. Csak olvasási hozzáférés kell hozzájuk, ami HU-ból jogilag kezelhető.
6. **A takerek veszítenek, a longshotok túlárazottak (becsült).** Bürgi–Deng–Whelan: a Kalshin a takerek átlagosan kb. 32%-ot, a makerek kb. 10%-ot veszítenek. A lehetséges edge iránya: maker-végrehajtás és a longshot-oldal eladása.
7. **A Polymarket volumenének egy része wash trading (becsült).** A Columbia 2025-ös preprintje szerint átlagosan kb. 25%, sportpiacokon kb. 45%. Szűrés nélkül a volumen- és smart-money-jelek félrevezetők.
8. **Az arbitrázs létezett, de lecseng (mért, arXiv).** Saguillo et al. 2024-04 és 2025-04 között kb. 40 M USD realizált Polymarket-arbitrázst talált, a díjak bevezetése előtt. Ma a díjak és a botok versenye viszi el a hasznot.
9. **Legjobb ingyenes adatalapok (mért).** `Jon-Becker/prediction-market-analysis`: 36 GiB, kb. 3.9k csillag. HF `TimeSeventeen/Polymarket-v1`: CC-BY-4.0, 1.2 Mrd trade. football-data.co.uk. nflverse (CC-BY-4.0). Retrosheet (kereskedelmi célra is szabad).
10. **Eszközök a végrehajtáshoz (mért).** A pmxt egységes API 15 venue-hoz (kb. 2.2k csillag). A NautilusTrader Polymarket- és Betfair-adaptere ugyanabban az eseményvezérelt magban futhat, mint az FX.

## Jogi hozzáférés HU/EU (2026-11-15)
| Venue | Saját geo/ÁSZF HU-ra | Magyar hatóság | EU-s helyzet | Címke |
|---|---|---|---|---|
| Polymarket (globális) | nincs a geoblokk-listán; VPN-tilalom az ÁSZF-ben | SZTFH ideiglenes ISP-blokk 2026-01-16-tól, végleges döntést nem találtunk | close-only: FR, DE, IT, BE, PL, SK; csak frontend: IE, NL, MT (sport); hatósági blokk: PT, CZ, FR (ANJ), IT | mért / becsült |
| Polymarket US (QCX) | csak US-lakos, KYC | – | nem elérhető | becsült |
| Kalshi | HU a 55 korlátozott joghatóság között | – | EU-ból korlátozott: BE, BG, FR, HU, IE, IT, PL, PT; ES ISP-blokk (1 forrás) | becsült |
| PredictIt | csak US | – | nem elérhető | mért |
| Betfair Exchange | – | SZTFH-blokk 2023-09-től, tiltólistán | EU-ban országonként eltér | becsült |
| Smarkets / Matchbook / Betdaq | nem ellenőrzött | nincs engedélyük, tiltólista-kockázat | – | nem ellenőrzött |
| Pinnacle | egy blog szerint HU-t nem fogad | nincs engedélye | – | nem ellenőrzött |
| TippmixPro (Szerencsejáték Zrt.) | legális | engedélyes, a nyeremény adómentes | – | mért (NAV) |
| Manifold, Metaculus, GJOpen | nincs tét / játékpénz | nem szerencsejáték | szabad | becsült |
| Csak olvasás (Gamma, Data API, Kalshi publikus, on-chain) | adatolvasás | fogadás nélkül nem szerencsejáték | szabad | következtetett |

**Adó HU-ban (mért, NAV-oldal, de az oldal 2026-05-02 óta archivált jelölésű).**
- Az engedélyes távszerencsejáték nyereménye adómentes (Szja tv. 76. § (4)).
- Az engedély nélküli, például külföldi oldalon szerzett nyeremény egyéb jövedelem, és fogadásonként kell elszámolni: a vesztes fogadások nem csökkentik az adóalapot.
- Fizetendő: 15% szja-előleg és 13% szocho, mindkettő a jövedelem 89%-ára, a negyedévet követő hó 12-éig. Éves bevallás május 20-ig.
- Emiatt egy sok fogadásos, kis edge-ű stratégia HU-ban adózás után negatív lehet. A 2026-os szabályt adószakértővel újra kell ellenőrizni.

**Politikai kontextus (becsült, sajtó).** A 2026. május 9-én hivatalba lépett kormány felülvizsgálja a Szerencsejáték Zrt. kiváltságait. Szóba került az SZTFH megszüntetése is (jelentési határidő 2026-09-30). A szabályozás 2027-re változhat.

## Következtetés a platformra
- **Mag (Z ≥ 8).** Predikciós piaci árak csak olvasásra, mint makró-, esemény- és FX-jel. A Kalshi makró-piacai és a Polymarket geopolitikai és Fed-piacai az ensemble szavazóiba kerülnek, kalibrációval és lejárati korrekcióval. Sport: TippmixPro, CLV-méréssel Betfair-záróárhoz.
- **Kutatás.** FLB, maker/taker és arbitrázs-backtest a 36 GiB-os és a HF-adathalmazokon, a 2026-os díjakkal újraszámolva.
- **Kerülendő HU-lakosként.** Polymarket-, Kalshi- és Betfair-kereskedés, VPN-nel sem: ÁSZF-sértés, a fiók befagyasztásának kockázata, hatósági blokk és kedvezőtlen adózás.

## Hiányok (nyitottak)
1. **Kalshi Member Agreement PDF.** A szerver 429-et adott, ezért a HU-korlátozás csak két aggregátorból „becsült”.
2. **SZTFH végleges Polymarket-határozat és hivatalos tiltólista-URL.** Nem találtuk. A Betfair-blokk mai érvényessége magyar IP-ről sem ellenőrzött (a mi IP-nk US).
3. **Árak.** A Betfair Historical Data ADVANCED/PRO ára nem látható (az oldal 403-at adott). Az OpticOdds és a Sportradar ára csak versenytárs-becslés. A Smarkets, Matchbook és Betdaq HU-hozzáférése és jutaléka nem ellenőrzött.
4. **2026-os HU-adószabály.** A NAV-tájékoztató archivált, az aktuális kulcsot és alapot nem erősítettük meg. A predikciós piaci (kripto-alapú) nyereség adóminősítése nyitott.
5. **Nem fedtük le.**
   - Azuro, SX Bet, Overtime, Opinion, Myriad és Augur (on-chain sport/predikció): elfogyott a keresési keret.
   - Néhány GitHub-repó utolsó commitja nem mért: `py-sdk`, `polymarket-subgraph`.
   - A gh API ebben a környezetben tiltott. A csillagszámokat és dátumokat a GitHub-oldalakról és az Atom-feedből mértük.

Megjegyzés: a munka során elértük a turnusonkénti 200 WebSearch-hívásos keretet. A fenti hiányok egy része egy következő körben pótolható.
