# ALGOTRADING – végső pontozás és minőségkapu (2026-11-15)

**Kapu (megrendelői feltétel):** minden terület ≥ 90, a hat átnéző átlaga ≥ 95.
**Eredmény:** az átlag **93,6**. A 36 területből 34 ≥ 90, kettő **89** (forráskorlátos). **A kapu teljes egészében nem teljesült.** A hiány forrása nem szöveg, hanem olyan mérés, belépés vagy ügyféladat, amely a dokumentumok szerkesztésével nem pótolható (részletek lent). Kitalált forrással, mért helyett becsült adattal vagy a pontozás lazításával nem zártuk le.

## Átnézők és pontszámok (négy kör)

| Átnéző | 1. kör | 2. kör | 3. kör | **4. kör (végső)** | Területek a 4. körben |
|---|---|---|---|---|---|
| AI-ágens (prompt, katalógus, letöltő, újraépítés, F0-bootstrap, kalkulátorok) | 78,7 | 91,3 | 95,0 | **96,0** | 95 · 95 · 95 · 99 · 96 · 96 |
| Fejlesztői tech lead (spec, átvételi feltételek, architektúra, döntési réteg, átadás, konzisztencia) | 70,3 | 90,7 | 95,0 | **95,8** | 96 · 95 · 96 · 96 · 96 · 96 |
| Kockázatkezelő és jogász (matek, figyelmeztetések, HU adó/jog, szabályozás, partnerkockázat, AI-irányítás) | 81,8 | 89,0 | 92,7 | **93,3** | 96 · 96 · 92 · 92 · 90 · 94 |
| Kvant-kutató (stratégiák, validálás, esettanulmányok, hipotézisgyár, adatforrások, irodalom) | 81,7 | 90,3 | 92,3 | **92,8** | 93 · 95 · 94 · 91 · 91 · 93 |
| Adatbeszerző (piaci adat, makró/PIT, árak, linkek, letöltő, magyar források) | 75,7 | 86,7 | 89,0 | **92,2** | **89** · 93 · 92 · 95 · 91 · 93 |
| Végrehajtási mérnök (MT5-híd/OMS, bróker-összehasonlítás, végrehajtás-minőség, infra, platformfüggetlenség, kripto/predikciós API) | 65,7 | 87,7 | 90,7 | **91,3** | 92 · **89** · 91 · 90 · 94 · 92 |
| **Átlag** | **75,6** | **89,3** | **92,5** | **93,6** | |

A 4. kör után a szövegesen javítható maradék hibákat is javítottuk (HF-méret a main ágból; A3-licenc az ÁSZF-ből; A4-továbbadhatóság a licencből; AFM-mondat; Polymarket-díjkerekítés; VIF; PEP 668-biztos uv-telepítés; `pit_applicable`; `related_ids`; PIT-jegyzetek; stratégiafájl-normalizálás; MNB napi gate). Ezeket újrapontozás nem követte; az átnézők becslése szerint kb. +0,5–1,5 pont átnézőnként.

## Ellenőrzések (a 4. körben mérve)

- Katalógus: 1633 tétel, 0 JSON-hiba, 0 típushiba, 0 duplikált id/URL/név (az elemzési sorokon kívül), profilpontok 5 × 1633 pontosan reprodukálhatók.
- Linkek: több mintán **0 halott link**; a nem 200-as válaszok botvédelem (DOI-kiadók, SSRN, SEC, Bloomberg, brókerek) vagy a sandbox hálózati korlátja. Mind a 345 GitHub-repó él (`git ls-remote`), a tesztelt DOI-k mind regisztráltak.
- Kockázati számok: a kockázati átnéző saját kóddal újraszámolta, mind egyezik.
- Specifikáció: 38 kódblokk parse-ol; a `contracts.py` importálható; a JSON Schema és a Pydantic modell 2926 mutációból 12 várt eltéréssel egyezik; az F0-bootstrap 412 teszttel átment.
- Letöltő: próbafuttatás 434 OK / 0 FAIL; célmappa-védelem fail-closed; méretőr működik.
- HTML: 0 JS-hiba, 400 és 1300 px, világos és sötét mód; a kalkulátorok 17/17 esetben egyeznek egy független Python-implementációval.
- Újraépítés a `forras/` mappából bájtazonos; a ZIP determinisztikus.

## Ami a 95-öt meggátolja – és honnan pótolható

| Hiány | Érintett terület | Ki / mivel pótolható |
|---|---|---|
| Vantage/VIG ügyfélszerződés (jogalany, stop-out 20% vagy 50%, NBP, visszaélési, carry trade és profit-visszavonási záradékok) | partnerkockázat, bróker-összehasonlítás | az ügyfél: a saját szerződés PDF-je (a weboldal innen 403-at ad) |
| MT5-viselkedés: FileFlush tartóssága, CryptEncode HMAC, MetaEditor CLI Wine alatt, megjegyzésmező-csonkítás, w32time < 1 ms | MT5-híd, infra | fejlesztőcsapat: F1-tesztek demószámlán |
| Testnet-válaszok: Binance `countdownCancelAll` és a reduce-only stopok, a ccxt sandbox, a Kalshi előjel és tick, a Polymarket order-hash (F6.4) | kripto/predikciós API | fejlesztőcsapat: F4/F6 testnet-futtatás (a Polymarket élő hívása Magyarországról jogilag tilos) |
| Vantage szerver adatközpontja (LD4?) | infra | traceroute és RTT egy VPS-ről |
| OPA/Rego-szabályok futtatása | AI-irányítás | CI: `opa check --strict`, `opa test -v` (itt a letöltést a biztonsági ellenőrzés nem engedte) |
| A 165 ötlet egyike sincs tesztelve; az ügyfél gridje nincs a farokkapun átvezetve | hipotézisgyár, stratégiák | ~10 ötlet előregisztrált pilotja Vantage tick/swap/fill naplóval; az EA forráskódja és a szimbólum-specifikáció |
| Független TCA lakossági brókerre nem létezik | végrehajtás-minőség | a saját §3.7 audit (617 vagy 153 fill vödrönként) |
| Tőzsdei licencfeltételek és díjak, ~290 intézményi ár; WRDS mögötti adatok; Ken French/FRED a sandboxból | piaci adat, árak, PIT | ajánlatkérés, belépés, másik hálózat |
| NAV-állásfoglalás: nem-ETÜ offshore CFD és Polymarket-nyeremény besorolása | HU adó | NAV vagy adótanácsadó írásos véleménye |
| A Medallion hozamai auditálatlanok; a Bloomberg-funkciókódok Terminal-belépés mögött vannak | irodalom | természeténél fogva, illetve Terminal-hozzáféréssel |

**Becsült plafon:** dokumentációból kb. 94–95; a fenti tételek lezárásával 95–97.
