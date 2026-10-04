---
name: oil-market-bbb
description: Bear/Base/Bull (25/50/25) rammeverk for råolje- og destillatmarkedet, med 3-års utfallsrom for Brent, dieselcrack og andre produktcracks. Dekker chokepoints (Hormuz, Rødehavet/Bab el-Mandeb, Suez, Panama, Saudi/UAE bypass), råoljetilbud, lagerstatus, etterspørsel, Russland/Ukraina, raffinering og forwardkurve. Dekker IKKE shipping/tankrater — det er en egen skill, [[oil-shipping-bbb]]. ALLTID bruk denne skillen når brukeren nevner "Oil Market BBB", ber om å "lage", "kjøre" eller "oppdatere modul" for oljemarkedet, spør om olje-BBB, destillatmarked, crack-spreader, Brent-utfallsrom, eller ber om en oppdatert baseline for råolje/diesel/jet/bensin-markedet — selv om de ikke nevner skillnavnet eksplisitt. Dette er en input til Investment Analysis Framework (IAF, se [[iaf-valuation]]) for olje- og raffineriselskaper — for shipping/tank-selskaper, gå via [[oil-shipping-bbb]] i stedet. Kan også kjøres frittstående som et rent markedssyn.
---

# Oil Market BBB

Et strukturert Bear/Base/Bull-scenariosett (25 % / 50 % / 25 %, i tråd med
[[iaf-valuation]]) for råolje- og destillatmarkedet, med et utfallsrom for de
neste ca. 3 årene. Formålet er **ikke** en utømmende nyhetsoppsummering, men
en testbar hypotese om hvor markedet er på vei, pluss en eksplisitt
risikovurdering — komprimert til hovedpunktene, uten å drukne i detaljer.

Output av enhver kjøring er ett dokument: **`Oil Market BBB.md`**. Strukturen
står under "Output-format". Shipping/tankrater dekkes **ikke** her — det er
en egen skill, [[oil-shipping-bbb]], som bruker denne baselinen som input og
oversetter den til rater/TCE.

## To atskilte, men koblede markeder

1. **Råoljemarkedet** — retningen på Brent/WTI.
2. **Destillatmarkedet** (diesel/gasoil, jet, bensin) — behandles som
   **marginmessig delvis frikoblet** fra råoljeprisen. Crack-spreadene har sin
   egen tilbuds-/etterspørselsdynamikk (raffinerikapasitet, outages,
   sesong, regionale ubalanser) og kan bevege seg motsatt av råolje. Hver
   BBB-runde skal derfor gi **separate** scenariointervaller for Brent og for
   de viktigste crackene — ikke utlede crack fra en fast beta mot råolje.

## To kjøremodus

### A. Initiér (lag ny baseline fra bunnen)

Trigges av f.eks. "lag Oil Market BBB", "start en ny baseline". Gjør full
research på alle punktene under "Analyseområder", og skriv et komplett
`Oil Market BBB.md` med dagens dato som baseline-dato.

### B. Oppdater modul

Trigges av "oppdater modul" eller "oppdater Oil Market BBB". Følg
`references/update-procedure.md` **trinn for trinn** — dette er en presis,
brukerdefinert prosedyre og skal ikke forkortes eller erstattes med en
friere research-runde.

Den viktigste regelen, gjentatt fra prosedyren fordi den lett glemmes:

> «Oppdater modul» betyr ikke «oppsummer siste olje-nyheter». Det betyr «gjør
> ny grundig research og test om den eksisterende Oil Market BBB fortsatt er
> riktig». Hvis ny informasjon ikke er sterk nok til å endre modellen, skal
> konklusjonen være eksplisitt: **Oil Market BBB beholdes uendret.**

## Analyseområder (initiér-modus dekker alle; oppdater-modus se referansefilen)

Grupper research i disse blokkene — bruk dem som overskrifter i det
ferdige dokumentet:

1. **Chokepoints og omdirigering** — Hormuz (trafikk, angrep, forsikring,
   reopening-signaler), Rødehavet/Bab el-Mandeb (Houthi-aktivitet,
   rerouting), Suez/SUMED (faktisk flow), Saudi East–West-pipeline +
   UAE/Fujairah bypass (kapasitet, skader, faktisk pumping), Saudi/Oman STS
   (kø, transfertid, bundet tonnasje), Iran–USA-spenning, Panama
   (transitbegrensninger, vannstand, effekt på produktfrakt).
2. **Råoljetilbud** — OPEC+ (kvoter, compliance, faktisk eksport), Saudi/UAE/
   Iran/øvrig Gulf, USA/Brasil/Guyana/Canada, russisk råoljeeksport. Skill
   alltid mellom nominell produksjon og fysisk supply som faktisk når
   markedet.
3. **Lager** — USA (crude, Cushing, SPR, bensin, distillates), Kina
   (crude + produkt), OECD/Europa, ARA (diesel/gasoil/jet), Singapore
   (middle distillates). Se på ukentlig trekk/bygg, sesongavvik, nivå mot
   5-årssnitt, og dagers lagerdekning.
4. **Etterspørsel** — global + USA/Kina/Europa/India, brutt ned på
   diesel/jet/bensin. Skill mellom strukturell etterspørselsendring, demand
   destruction (pris/knapphet), og rebound etter tidligere destruction.
5. **Russland/Ukraina** — fast premiss (se "Standing parameters"), men
   verifiser hver gang: raffineriangrep, throughput/outages, innenlands
   produktmangel, diesel-/produkteksport.
6. **Raffinering og destillatproduksjon** — utilization/outages i Gulf, USA,
   Europa, Kina, India, Afrika/Dangote, Korea/Japan; ny kapasitet og
   permanente closures; Kina som swing-supplier (throughput, lager,
   eksportkvoter); USA/India som marginale eksportører. Dette er også der
   destillat-spesifikke drivere hører hjemme: kapasitetsøkninger i
   USA/Europa/Kina/Afrika, og regionale over-/underskuddsbilder per marked.
   Selve seilings-/ton-mile-effekten av disse ubalansene dekkes av
   [[oil-shipping-bbb]], ikke her.
7. **Forwardmarked** — Brent spot/front + minst 3-måneders kurve, klassifisert
   etter tabellen under. ICE gasoil/diesel 3-måneders spread i $/tonn. Les
   alltid kurven sammen med lagerbevegelsen (se tabell).
8. **Cracks** — diesel/gasoil, jet, bensin. Vurder for hver om endringen
   skyldes råoljeprisen, raffineritilgjengelighet, eller faktisk
   produktknapphet — dette er kjernen i frikoblingsvurderingen mellom
   råolje og destillat.

## Forwardkurve-klassifisering (fast regel)

| Brent 3M-spread | Signal |
|---|---|
| Backwardation > $5/bbl | Tydelig Tight |
| Backwardation $2–5/bbl | Moderat Tight |
| −$2 til +$2/bbl (om lag flatt) | Omtrent balansert |
| Contango | Loose / Bear |

Kombinér alltid med lagerretningen:

| Kurve | Lager | Tolkning |
|---|---|---|
| Backwardation | Fallende | Sterk fysisk Tightness |
| Backwardation | Byggende | Mulig normalisering på vei |
| Contango | Byggende | Klart Loose-signal |

## Fakta vs. tolkning (gjelder begge moduser)

Del hver oppdatering mentalt i tre: (1) ny fakta, (2) hva den betyr fysisk,
(3) om den faktisk endrer modellen. Enkeltstående nyhetssaker skal normalt
**ikke** flytte BBB-scenarioene eller -sannsynlighetene. Diplomatiske
signaler (forhandlinger, våpenhviler, uttalelser) teller ikke som
modellendring før de gir en verifisert fysisk og varig effekt på flow,
produksjon eller lager.

## Output-format: `Oil Market BBB.md`

Bruk alltid denne strukturen:

```markdown
# Oil Market BBB — [baseline-dato]

## Sammendrag
- Base case i én-to setninger (Brent-intervall + diesel crack-intervall)
- De 2-3 største risikoene til hver side (bear-risiko / bull-risiko)

## Scenariotabell
| Scenario | Sannsynlighet | Brent (3 år) | Diesel crack | Nøkkeldrivere |
|---|---|---|---|---|
| Bear  | 25 % | ... | ... | ... |
| Base  | 50 % | ... | ... | ... |
| Bull  | 25 % | ... | ... | ... |

## Råoljemarkedet
### Chokepoints og omdirigering
### Tilbud (OPEC+, non-OPEC, Russland)
### Lager
### Etterspørsel
### Russland/Ukraina (fast premiss — status)
### Forwardkurve

## Destillatmarkedet
### Raffinering og kapasitet
### Regionale balanser
### Sesongeffekter
### Cracks (diesel / jet / bensin)
### Frikobling fra råolje — vurdering av prissensitivitet
   (se metodikk under "Destillat-prissensitivitet")

## Risikovurdering
- Hva må skje for at Bear/Bull faktisk inntreffer
- Hva overvåkes videre til neste oppdatering

## Change log
- Nytt siden forrige baseline
- Uendret siden forrige baseline
- Endringer i BBB (scenario, sannsynlighet, intervaller) — eller eksplisitt:
  "Oil Market BBB beholdes uendret"
- Ny baseline-dato
```

Hold hoveddelen komprimert til hovedpunkter per underoverskrift (noen
setninger til et par avsnitt) — detaljerte tallrekker/kilder kan legges i et
vedlegg nederst i dokumentet hvis nødvendig, men skal ikke drukne
sammendraget og scenariotabellen.

## Destillat-prissensitivitet — hvordan anslå den

Fordi destillat er delvis frikoblet fra råolje, skal crack-spreaden
behandles som en **egen tilstandsvariabel**, ikke som råoljepris × en fast
beta:

1. Se på nivå og trend i crack-spreadene isolert (diesel/gasoil, jet,
   bensin) mot deres egne historiske normalbånd, ikke bare mot råoljeprisen.
2. Bygg Bear/Base/Bull for cracks **separat** fra Bear/Base/Bull for Brent —
   de kan gå ulik vei (f.eks. løst råoljemarked + stram destillatbalanse pga.
   raffineri-outages).
3. Bruk raffineringsblokken (utilization, outages, ny kapasitet, Kina som
   swing-supplier) som hoveddriver for crack-scenarioene, og
   lager/sesong som bekreftende signaler.
4. Angi eksplisitt hvor sensitiv sluttproduktprisen (diesel/jet/bensin til
   forbruker/marginalkjøper) er for en gitt endring i crack vs. en gitt
   endring i råolje — dette er selve svaret på "hvordan blir frikoblingen
   fremover".

## Standing parameters

- BBB-vekting: 25 % Bear / 50 % Base / 25 % Bull — konsistent med
  [[iaf-valuation]], med mindre brukeren ber om noe annet for denne kjøringen.
- Tidshorisont: 3 år (samme vindu som IAF sitt standard forecast-vindu).
- Russland/Ukraina er et **fast premiss** inntil ny verifisert informasjon
  tvinger en endring — se punkt 5 og "Fakta vs. tolkning" over.
- Forwardkurve-terskler: se tabellen over — ikke sett egne terskler ad hoc.
- Shipping/tankrater, ton-mile og fartøystilbud hører hjemme i
  [[oil-shipping-bbb]], ikke her — ikke legg dette til i denne skillen igjen.
- Ved oppdatering: følg alltid `references/update-procedure.md` i sin
  helhet fremfor å improvisere en kortere runde.

## Kobling til IAF

Når Oil Market BBB brukes som input til en selskapsanalyse i
[[iaf-valuation]] (oljeselskap, raffineri), er det scenariotabellen
(Brent-intervaller og crack-intervaller per scenario) som mates inn i det
år-for-år-bygde g-estimatet for det selskapet — ikke et enkelt
punktestimat. Behold Bear/Base/Bull-spennet helt til IAF-testen, i tråd med
IAF-skillens egne prinsipper. For shipping/tank-selskaper: gå via
[[oil-shipping-bbb]], som oversetter denne baselinen til rater/TCE — ikke
mat Oil Market BBB direkte inn i et shippingselskaps IAF.
