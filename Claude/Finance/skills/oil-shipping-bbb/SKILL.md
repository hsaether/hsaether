---
name: oil-shipping-bbb
description: Bear/Base/Bull (25/50/25) rammeverk for tank shipping (crude og product tank), 3-års utfallsrom (2027-2029) for VLCC/Suezmax/Aframax og LR2/LR1/MR TCE. Oversetter Oil Market BBB ([[oil-market-bbb]]) til shippingeffekter — spot/TCE, seilingsmønstre/ton-mile, chokepoints (Hormuz, Rødehavet, Suez, Panama, Cape of Good Hope, Saudi East-West/Yanbu), effektiv tonnasje (shadow fleet, alder, drydock, feilposisjonering, clean/dirty switching), fleet supply/orderbook, forwardmarked (TC/FFA/secondhand). ALLTID bruk når brukeren nevner "Oil Shipping BBB"/"Shipping BBB", ber om å lage/kjøre/oppdatere shipping-modulen, eller spør om tankmarkedet, tank-rater, TCE, ton-mile, effektiv flåte/tonnasje — selv uten å nevne skillnavnet. Input til IAF ([[iaf-valuation]]) for shipping/tank-selskaper; bygger på Oil Market BBB, lager ALDRI en ny oljeanalyse selv.
---

# Oil Shipping BBB

**Revision:** 2026-10-04.1 — bump on every change (date.counter). The installed skill is only a
pointer to this file; this folder copy is the master.

Et strukturert Bear/Base/Bull-scenariosett (25 % / 50 % / 25 %, i tråd med
[[iaf-valuation]]) for tank shipping-markedet, med et utfallsrom for de neste
ca. 3 årene (2027-2029). Formålet er å **oversette** [[oil-market-bbb]] til
konkrete shippingeffekter — rater, seilingsmønstre, tonnasje — ikke å lage en
ny oljeanalyse. Komprimert til hovedpunktene, med en testbar hypotese og en
eksplisitt risikovurdering, uten å drukne i detaljer.

Output av enhver kjøring er ett dokument: **`Oil Shipping BBB.md`**.
Strukturen står under "Output-format".

## Grunnprinsipp: input, ikke duplikat

Oil Shipping BBB skal **aldri** re-analysere oljemarkedet selv. Den henter
oljepris-/etterspørselsbane, crude/product-balanser, refinery-effekter,
Russland og Midtøsten/geopolitikk fra gjeldende [[oil-market-bbb]]-baseline,
og oversetter dette til:

- shipping-etterspørsel (ton-mile) via handelsstrømmer og distanse
- effektiv tonnasje-tilbud
- rater (spot, periode, normalisert TCE)

Hvis gjeldende Oil Market BBB er utdatert eller mangler, si dette eksplisitt
og be om (eller kjør) en oppdatering av den **først** — ikke lag en egen
skygge-oljeanalyse inne i shipping-modulen.

## To segmenter, samme metodikk

1. **Crude tank** — VLCC, Suezmax, Aframax.
2. **Product tank** — LR2, LR1, MR.

Begge segmenter kjøres gjennom samme rammeverk (rater, ton-mile, chokepoints,
effektiv tonnasje, fleet supply, forwardmarked), men holdes som **separate**
scenariotabeller siden de har ulike lasteprofiler, handelsruter og
clean/dirty-krysseffekter (særlig LR2/Aframax).

## To kjøremodus

### A. Initiér (lag ny baseline fra bunnen)

Trigges av f.eks. "lag Oil Shipping BBB", "start en ny shipping-baseline".
Gjør full research på alle punktene under "Analyseområder", og skriv et
komplett `Oil Shipping BBB.md` med dagens dato som baseline-dato.

### B. Oppdater modul

Trigges av "oppdater modul", "oppdater Shipping BBB" eller når en av de
faste rekalibreringstriggerne (se lenger ned) er utløst. Følg
`references/update-procedure.md` **trinn for trinn** — dette er en presis,
brukerdefinert prosedyre og skal ikke forkortes eller erstattes med en
friere research-runde.

Den viktigste regelen, gjentatt fra prosedyren fordi den lett glemmes:

> «Oppdater modul» betyr ikke «oppsummer siste shipping-nyheter». Det betyr
> «gjør ny grundig research og test om den eksisterende Oil Shipping BBB
> fortsatt er riktig». Dagens ekstremspot skal aldri automatisk
> annualiseres. Hvis ny informasjon ikke er sterk nok til å endre modellen,
> skal konklusjonen være eksplisitt: **Oil Shipping BBB beholdes uendret.**

## Analyseområder (initiér-modus dekker alle; oppdater-modus se referansefilen)

Grupper research i disse blokkene — bruk dem som overskrifter i det
ferdige dokumentet:

1. **Input fra Oil Market BBB** — baseline-dato, scenario lagt til grunn,
   oljepris-/etterspørselsbane, crude/product-balanser, refinery-effekter,
   Russland, Midtøsten/geopolitikk. Oversettes til shippingeffekter, gjengis
   ikke som ny oljeanalyse.
2. **Spot og periodemarked (TCE)** — crude tank (VLCC/Suezmax/Aframax) og
   product tank (LR2/LR1/MR). Bruk Baltic/andre markedsdata, faktiske
   fixtures og rapporterte selskaps-TCE-er. Skill eksplisitt mellom ekstrem
   spot og bærekraftig/normalisert rate. Sammenlign alltid mot forrige
   Shipping BBB.
3. **Seilingsmønstre og ton-mile** — MEG → Asia, Atlantic Basin → Asia, US
   Gulf → Europa/LatAm/Asia, Russland, India/Asia/Midtøsten → Europa,
   inventory restocking/floating storage. Se etter endringer i både volum
   og distanse.
4. **Chokepoints** — Hormuz, Rødehavet/Bab el-Mandeb, Suez, Saudi
   East-West-pipeline/Yanbu, Panama, Cape of Good Hope. Uttrykk effekten i
   ekstra seilingsdøgn, ventetid, repositioning og redusert effektiv
   tonnasje — ikke bare «åpen/lukket».
5. **Effektiv tilgjengelig tonnasje** — ikke bare nominell flåte: sanctioned/
   shadow fleet, skip >15 og >20 år, drydock/offhire, skip bundet på lange
   voyages, feilposisjonering, STS/shuttle/venting, clean↔dirty switching
   (særlig LR2/Aframax).
6. **Fleet supply (36 måneder)** — per segment: dagens flåte + leveranser
   − skraping ± crossover = effektiv fleet growth. Følg orderbook/fleet,
   nye ordre, leveringsår, slippage, kanselleringer, skraping, alder,
   verftskapasitet.
7. **Refinery- og handelsgeografi** — nye raffinerier, closures, outages,
   russiske refinery-skader, Middle East export availability, Kina/India/
   USA eksportpolitikk, regional diesel/jet/gasoline-ubalanse. Særlig
   viktig for LR/MR.
8. **Forwardmarked** — 1-års time charter, 2-3 års perioderater, relevante
   FFAs, secondhand values, resale/newbuild-priser. Periodemarkedet brukes
   som viktig kontroll på de normaliserte BBB-ratene.
9. **Bear/Base/Bull 2027-2029** — for hvert scenario: ton-mile, effektiv
   fleet growth, utilization/tightness, normalisert TCE for VLCC/Suezmax/
   Aframax/LR2/LR1/MR, scenario-sannsynlighet.
10. **Change log** — hva er nytt → hva betyr det → endrer det BBB? Marker
    eksplisitt når ny informasjon er interessant, men ikke sterk nok til å
    endre ratebane eller sannsynligheter.

## Fakta vs. tolkning (gjelder begge moduser)

Del hver oppdatering mentalt i tre: (1) ny fakta, (2) hva den betyr fysisk
for ton-mile/tonnasje/rate, (3) om den faktisk endrer modellen.
Enkeltstående nyhetssaker (én fixture, én dags rateoppgang) skal normalt
**ikke** flytte BBB-scenarioene eller -sannsynlighetene.

## Faste rekalibreringstriggere

Full vurdering skal spesielt utløses når:

- spot/perioderater flytter seg >15 % på én måned eller >25 % på én uke
- orderbook/fleet endres >2 prosentpoeng
- ton-mile-estimat endres >1 prosentpoeng
- Hormuz/Suez/Red Sea/Panama-flow endres omtrent >20 %
- refinery/eksportkapasitet endres >0,5 mb/d
- sanctioned/shadow fleet endres >2 % av relevant effektiv flåte
- 1-års TC/FFA endres >10 %
- faktisk amerikansk dieselrestriksjon eller annen større handelsregulering
  endrer product-flow vesentlig
- gjeldende Oil Market BBB oppdateres med en endring som er stor nok til å
  påvirke crude/product-balansen eller refinery-bildet.

## Output-format: `Oil Shipping BBB.md`

Bruk alltid denne strukturen:

```markdown
# Oil Shipping BBB — [baseline-dato]

## Sammendrag
- Base case i én-to setninger per segment (crude tank TCE-intervall,
  product tank TCE-intervall)
- De 2-3 største risikoene til hver side (bear-risiko / bull-risiko)
- Hvilken Oil Market BBB-baseline (dato + scenario) som ligger til grunn

## Scenariotabell — Crude tank (normalisert TCE, 2027-2029)
| Scenario | Sannsynlighet | VLCC | Suezmax | Aframax | Nøkkeldrivere |
|---|---|---|---|---|---|
| Bear  | 25 % | ... | ... | ... | ... |
| Base  | 50 % | ... | ... | ... | ... |
| Bull  | 25 % | ... | ... | ... | ... |

## Scenariotabell — Product tank (normalisert TCE, 2027-2029)
| Scenario | Sannsynlighet | LR2 | LR1 | MR | Nøkkeldrivere |
|---|---|---|---|---|---|
| Bear  | 25 % | ... | ... | ... | ... |
| Base  | 50 % | ... | ... | ... | ... |
| Bull  | 25 % | ... | ... | ... | ... |

## Input fra Oil Market BBB
### Baseline brukt og relevante scenarioer
### Overføring til shippingeffekter

## Spot og periodemarked i dag
### Crude tank (VLCC/Suezmax/Aframax)
### Product tank (LR2/LR1/MR)
   (ekstremspot vs. normalisert rate; sammenligning mot forrige Shipping BBB)

## Seilingsmønstre og ton-mile
### Crude
### Product
### Inventory restocking / floating storage

## Chokepoints
### Hormuz
### Rødehavet / Bab el-Mandeb
### Suez
### Saudi East-West / Yanbu
### Panama
### Cape of Good Hope
   (uttrykt i ekstra seilingsdøgn, ventetid, repositioning, redusert
   effektiv tonnasje)

## Effektiv tilgjengelig tonnasje
### Crude tank
### Product tank

## Fleet supply (36 måneder)
### Crude tank
### Product tank
   (dagens flåte + leveranser − skraping ± crossover = effektiv fleet growth)

## Refinery- og handelsgeografi
   (særlig relevant for LR/MR)

## Forwardmarked og verdivurdering
### Time charter og FFA
### Secondhand / newbuild

## Bear/Base/Bull 2027-2029 (rekalibrert)
### Crude tank
### Product tank

## Risikovurdering
- Hva må skje for at Bear/Bull faktisk inntreffer
- Hva overvåkes videre til neste oppdatering

## Change log
- Nytt siden forrige baseline → hva det betyr → endrer det BBB?
- Uendret siden forrige baseline
- Endringer i BBB (scenario, sannsynlighet, intervaller) — eller eksplisitt:
  "Oil Shipping BBB beholdes uendret"
- Ny baseline-dato
```

Hold hoveddelen komprimert til hovedpunkter per underoverskrift (noen
setninger til et par avsnitt) — detaljerte tallrekker/kilder kan legges i et
vedlegg nederst i dokumentet hvis nødvendig, men skal ikke drukne
sammendraget og scenariotabellene.

## Standing parameters

- BBB-vekting: 25 % Bear / 50 % Base / 25 % Bull — konsistent med
  [[iaf-valuation]] og [[oil-market-bbb]], med mindre brukeren ber om noe
  annet for denne kjøringen.
- Tidshorisont: 3 år, 2027-2029 (samme vindu som IAF sitt standard
  forecast-vindu og som [[oil-market-bbb]]).
- Segmenter holdes alltid separat: crude tank (VLCC/Suezmax/Aframax) og
  product tank (LR2/LR1/MR) — aldri én blandet rate.
- Dagens ekstremspot skal aldri automatisk annualiseres eller brukes direkte
  som normalisert BBB-rate.
- Ved oppdatering: følg alltid `references/update-procedure.md` i sin
  helhet fremfor å improvisere en kortere runde.
- Se "Faste rekalibreringstriggere" over for når full vurdering skal
  utløses automatisk.

## Kobling til IAF

Når Oil Shipping BBB brukes som input til en selskapsanalyse i
[[iaf-valuation]] (tank shipping-selskap), er det scenariotabellene
(normalisert TCE per segment og scenario) som mates inn i det
år-for-år-bygde g-estimatet (og evt. FCF-forecasten) for det selskapet —
ikke et enkelt punktestimat. Behold Bear/Base/Bull-spennet helt til
IAF-testen, i tråd med IAF-skillens egne prinsipper. Match selskapets
faktiske flåtesammensetning (segment, alder, andel spot vs. periode) mot
riktig rad i scenariotabellene før ratene brukes i modellen.
