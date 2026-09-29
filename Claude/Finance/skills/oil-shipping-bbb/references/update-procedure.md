# Oppdateringsprosedyre — "oppdater modul" (Oil Shipping BBB)

Denne prosedyren kjøres **hver gang** brukeren ber om å oppdatere Oil
Shipping BBB, eller når en av de faste rekalibreringstriggerne (se
SKILL.md) utløses. Den skal følges i sin helhet og i rekkefølge — den er
ikke en sjekkliste å plukke fra.

Den viktigste regelen, som gjelder gjennom hele prosedyren:

> «Oppdater modul» betyr ikke "oppsummer siste shipping-nyheter". Det
> betyr "gjør ny grundig research og test om den eksisterende Oil Shipping
> BBB fortsatt er riktig".
>
> Og hvis ny informasjon ikke er sterk nok til å endre modellen, skal
> konklusjonen være eksplisitt: **Oil Shipping BBB beholdes uendret.**
>
> Dagens ekstremspot skal aldri automatisk annualiseres eller settes inn
> direkte som ny normalisert BBB-rate.

## 1. Importer siste Oil Market BBB

- Hent gjeldende [[oil-market-bbb]]-baseline. Hvis den er utdatert eller
  mangler helt: si dette eksplisitt til brukeren og få den oppdatert
  (eller kjør oil-market-bbb-skillen) **før** shipping-modulen oppdateres
  videre — ikke gjett på oljebildet.
- Hent ut: oljepris-/etterspørselsbane, crude/product-balanser,
  refinery-effekter, Russland- og Midtøsten-status, geopolitikk.
- Oversett dette til implikasjoner for shipping-etterspørsel og
  handelsstrømmer. Ikke re-analyser oljemarkedet selv — det er
  oil-market-bbb sin jobb.
- Sammenlign mot forrige Shipping BBB: har Oil Market BBB-baselinen som
  ligger til grunn endret seg siden sist, og i så fall hvordan slår det
  inn i shippingbildet?

## 2. Oppdater spot/TCE for alle relevante segmenter

- Crude: VLCC, Suezmax, Aframax.
- Product: LR2, LR1, MR.
- Bruk Baltic/andre markedsdata, faktiske fixtures og rapporterte
  selskaps-TCE-er.
- Skill eksplisitt mellom:
  - ekstrem spot (kortvarige topper/bunner drevet av enkelthendelser)
  - bærekraftig/normalisert rate (det som faktisk skal inn i
    scenariotabellene).
- Sammenlign hvert segment mot forrige Shipping BBB — hvilken retning, og
  er bevegelsen stor nok til å telle (se rekalibreringstriggere)?

## 3. Oppdater seilingsmønstre og ton-mile

- MEG → Asia.
- Atlantic Basin → Asia.
- US Gulf → Europa/Latin-Amerika/Asia.
- Russland.
- India/Asia/Midtøsten → Europa.
- Inventory restocking/floating storage.
- Se etter endringer i **både** volum og distanse — en volumøkning på en
  kortere rute kan gi lavere ton-mile enn samme volum på en lengre rute.

## 4. Oppdater alle viktige chokepoints

- Hormuz.
- Rødehavet/Bab el-Mandeb.
- Suez.
- Saudi East-West-pipeline/Yanbu.
- Panama.
- Cape of Good Hope.
- For hver: uttrykk effekten i ekstra seilingsdøgn, ventetid,
  repositioning og redusert effektiv tonnasje — **ikke** bare
  "åpen/lukket" eller et generelt trusselnivå.

## 5. Beregn effektiv tilgjengelig tonnasje

Ikke bare nominell flåte. Vurder for hvert segment:

- sanctioned/shadow fleet
- skip >15 år og >20 år
- drydock/offhire
- skip bundet på lange voyages
- feilposisjonering
- STS/shuttle/venting
- clean↔dirty switching, særlig LR2/Aframax.

## 6. Oppdater fleet supply for kommende 36 måneder

Per segment:

```
dagens flåte + leveranser − skraping ± crossover = effektiv fleet growth
```

Følg:

- orderbook/fleet
- nye ordre
- leveringsår
- slippage
- kanselleringer
- skraping
- alder
- verftskapasitet.

## 7. Oppdater refinery- og handelsgeografien

- Nye raffinerier.
- Closures.
- Outages.
- Russiske refinery-skader.
- Middle East export availability.
- Kina/India/USA eksportpolitikk.
- Regional diesel/jet/gasoline-ubalanse.

Dette er særlig viktig for LR/MR.

## 8. Kontroller forward-markedet

- 1-års time charter.
- 2-3 års perioderater.
- Relevante FFAs.
- Secondhand values.
- Resale/newbuild-priser.

Periodemarkedet brukes som viktig kontroll på de normaliserte
BBB-ratene — hvis 1-års TC avviker vesentlig fra Base-scenarioets
normaliserte rate, undersøk hvorfor før du beholder eller endrer BBB.

## 9. Rekalibrer Bear/Base/Bull 2027-2029

For hvert scenario (Bear/Base/Bull) og hvert segment
(VLCC/Suezmax/Aframax/LR2/LR1/MR), oppdater:

- ton-mile
- effektiv fleet growth
- utilization/tightness
- normalisert TCE
- scenario-sannsynlighet.

Test eksplisitt:

- Har sannsynlighetene endret seg?
- Har TCE-intervallene endret seg per segment?
- Har crude tank- eller product tank-bildet endret seg mer enn det andre?

Scenario eller rateintervall endres når:

- flere uavhengige datapunkter peker samme vei, eller
- én hendelse er stor nok til å endre ton-mile, effektiv tonnasje eller
  fleet growth vesentlig.

## 10. Skill fakta fra tolkning

Del hver oppdatering mentalt i:

- ny fakta
- hva dette betyr fysisk for ton-mile/tonnasje/rate
- om det faktisk endrer modellen.

Enkeltstående nyheter (én fixture, én ukes rateoppgang, én diplomatisk
uttalelse) skal normalt **ikke** endre BBB før de gir en verifisert,
varig fysisk effekt.

## 11. Avslutt alltid med en change log

Oppdateringen skal eksplisitt svare:

- Hva er nytt → hva betyr det → endrer det BBB?
- Hva er uendret siden forrige baseline.
- Marker eksplisitt når ny informasjon er interessant, men ikke sterk nok
  til å endre ratebane eller sannsynligheter.
- Ny baseline-dato.

## Faste rekalibreringstriggere (repetert fra SKILL.md)

Full vurdering (denne prosedyren i sin helhet) skal spesielt utløses når:

- spot/perioderater flytter seg >15 % på én måned eller >25 % på én uke
- orderbook/fleet endres >2 prosentpoeng
- ton-mile-estimat endres >1 prosentpoeng
- Hormuz/Suez/Red Sea/Panama-flow endres omtrent >20 %
- refinery/eksportkapasitet endres >0,5 mb/d
- sanctioned/shadow fleet endres >2 % av relevant effektiv flåte
- 1-års TC/FFA endres >10 %
- faktisk amerikansk dieselrestriksjon eller annen større handelsregulering
  endrer product-flow vesentlig
- gjeldende Oil Market BBB oppdateres med en endring stor nok til å
  påvirke crude/product-balansen eller refinery-bildet.
