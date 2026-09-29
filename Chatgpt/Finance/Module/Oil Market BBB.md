# Oil Market BBB

## Dokumentinformasjon

- Dokumenttype: gjenbrukbar prosedyre for å oppdatere markedsmodulen.
- Opprettet: 29. september 2026.
- Kilde: oppgaven [Oil Market BBB](https://chatgpt.com/c/6aa52f85-efcc-83eb-97ef-25e86c459d0c), særlig prosedyrebeskrivelsen fra 27. september 2026 og standardmodulen fra 12. september 2026.
- Prosedyrefil: `C:\GitWork\hsaether\Chatgpt\Finance\Module\Oil Market BBB.md`.
- Resultatmappe: `C:\GitWork\hsaether\Chatgpt\Finance\Doc`.
- Siste analyseresultat ved opprettelsen: [Oil Market BBB – 26. september 2026](../Doc/Oil%20Market%20BBB%20-%202026-09-26.md).
- Skrivetilgang: bekreftet 29. september 2026 ved opprettelse, gjenlesing og sletting av en midlertidig kontrollfil i begge mapper.

## Formål og bruk

Oil Market BBB er et felles Bear/Base/Bull-markedsgrunnlag for råolje, raffinerte produkter, råoljetank, produkttank, raffinering, offshore/oljeservice og energirelatert high yield. Prosedyren utløses ved **«Oppdater modul»** i Oil Market BBB-sammenheng, eller ved **«Oppdater Oil Market BBB»** fra en annen oppgave.

Prosedyren nedenfor er hentet fra originaloppgaven. Avsnittene om lokal lagring og rapportformat konkretiserer denne filbaserte versjonen. Opprettelsen av dokumentene er en dokumentasjon og eksport av eksisterende arbeid; det er ikke gjennomført en ny markedsanalyse 29. september 2026.

## Faste modellpremisser fra originaloppgaven

Modellens utgangspunkt er **25 % Bear/Loose, 50 % Base og 25 % Bull/Tight**. Gjeldende baseline og senere begrunnede endringer går foran eldre scenarioforslag. Skill mellom strukturelle vekter for analyseperioden og midlertidige kortsiktige risikovekter; merk alltid tidshorisonten.

Russland/Ukraina behandles i originalmodellen som et felles premiss på tvers av scenarioene: fortsatt krig og raffineriangrep, liten eller ingen netto destillateksport, mulig behov for produktimport og samtidig mulighet for relativt høy råoljeeksport. Dette er modellforutsetninger fra oppgaven, og skal verifiseres ved hver oppdatering. De er ikke nyverifiserte fakta i dette prosedyredokumentet.

Brent og destillater vurderes separat. For frakt skilles transporterte volumer, transportavstand og effektiv flåtekapasitet. Samme bortfall må ikke telles flere ganger gjennom sammenhengende transportledd. Vær og ekstremhendelser behandles som egne sensitiviteter, slik at de ikke utilsiktet endrer definisjonen av de ordinære scenarioene.

## Fast oppdateringsprosedyre fra oppgaven

Ved instruksjonen **«Oppdater modul»** kjøres denne faste prosedyren for **Oil Market BBB**:

1. **Start med siste baseline**
   - Hent gjeldende Oil Market BBB.
   - Identifiser hva som har endret seg siden forrige baseline.
   - Behold faste premisser, særlig Russland/Ukraina, med mindre ny verifisert informasjon tilsier at de må endres.

2. **Midtøsten og chokepoints**
   - Hormuz: faktisk trafikk, angrep, restriksjoner, forsikring, reopening-signaler.
   - Rødehavet/Bab el-Mandeb: Houthi-aktivitet, skipstrafikk, rerouting.
   - Suez/SUMED: tilgjengelighet og faktisk flow.
   - Saudi East–West og UAE/Fujairah bypass: kapasitet, skader, reparasjonstid, faktisk pumping/loadings.
   - Saudi/Oman STS: kapasitet, kø, transfer-tid og bundet tonnasje.
   - Iran–USA: konfliktnivå, forhandlinger og militære hendelser.
   - Panama: transitbegrensninger, vannstand og effekt på produktfrakt.

3. **Råoljetilbud**
   - OPEC+ produksjon, kvoter, compliance og faktisk eksport.
   - Saudi, UAE, Iran og øvrig Gulf-produksjon.
   - USA, Brasil, Guyana, Canada m.fl.
   - Russisk råoljeeksport.
   - Vurdér om fysisk supply faktisk når markedet, ikke bare nominell produksjon.

4. **Lager**
   - USA crude, Cushing, SPR, gasoline og distillates.
   - Kina crude- og produktlagre.
   - OECD/Europa.
   - ARA diesel/gasoil/jet.
   - Singapore middle distillates.
   - Se på:
     - ukentlig trekk/bygg
     - sesongavvik
     - nivå mot 5-årssnitt
     - hvor mange dager lagerdekning markedet har.

5. **Etterspørsel og faktisk forbruk**
   - Global oljeetterspørsel.
   - USA, Kina, Europa, India og andre viktige regioner.
   - Diesel, jet og bensin separat.
   - Skille mellom:
     - strukturell etterspørselsendring
     - demand destruction på grunn av høy pris/fysisk knapphet
     - rebound etter tidligere demand destruction.

6. **Russland/Ukraina**
   - Verifiser at fast premiss fortsatt holder.
   - Nye angrep mot raffinerier.
   - Refinery throughput og outages.
   - Innenlandsk produktmangel/import.
   - Diesel-/produktexport.
   - Diplomatiske signaler teller ikke som modellendring før de gir **fysisk og varig effekt**.

7. **Raffinering og destillatproduksjon**
   - Utilization og outages i:
     - Gulf
     - USA
     - Europa
     - Kina
     - India
     - Afrika/Dangote
     - Korea/Japan.
   - Ny kapasitet og permanente closures.
   - Kina som swing-supplier: throughput, produktlagre og eksportkvoter.
   - USA og India som marginale eksportører.

8. **Forwardmarked**
   - Brent spot/front og minst 3-månederskurven.
   - Fast klassifisering:
     - > $5/bbl backwardation = tydelig Tight
     - $2–5 = moderat Tight
     - $0–2 = omtrent balansert
     - contango = Loose/Bear.
   - ICE gasoil/diesel 3-månedersspread i $/tonn.
   - Se forwardkurven sammen med lagrene:
     - backwardation + lagerfall = sterk fysisk Tightness
     - backwardation + lagerbygging = mulig normalisering
     - contango + lagerbygging = klart Loose-signal.

9. **Cracks**
   - Diesel/gasoil crack.
   - Jet crack.
   - Gasoline crack.
   - Vurder om endringen skyldes crude, refinery availability eller faktisk produktknapphet.

10. **Shipping / ton-mile**
   - Crude tank:
     - VLCC, Suezmax, Aframax
     - STS
     - rerouting
     - faktisk vessel availability
     - Atlantic Basin → Asia.
   - Product tank:
     - MR, LR1, LR2
     - Gulf/India/Kina/USA → Europa/LatAm/Asia
     - Panama/Rødehavet-effekter
     - ton-mile og effektiv flåtekapasitet.
   - Følg også orderbook som strukturell motvekt.

11. **Skill fakta fra tolkning**
   Hver oppdatering deles mentalt i:
   - **ny fakta**
   - **hva dette betyr fysisk**
   - **om det faktisk endrer modellen**.

   Enkeltstående nyheter skal normalt **ikke** endre BBB.

12. **Test BBB**
   Vurder separat:
   - Bear/Loose 25 %
   - Base 50 %
   - Bull/Tight 25 %

   Spør:
   - Har sannsynlighetene endret seg?
   - Har Brent-intervallene endret seg?
   - Har dieselcrack-intervallene endret seg?
   - Har crude-tank- eller product-tankbildet endret seg?

13. **Oppdater bare ved tilstrekkelig evidens**
   Scenario eller prisintervall endres når:
   - flere uavhengige datapunkter peker samme vei, eller
   - én hendelse er stor nok til å endre fysisk supply, logistikk eller lagerbane vesentlig.

14. **Avslutt alltid med en change log**
   Oppdateringen skal eksplisitt si:
   - hva som er nytt siden forrige baseline
   - hva som er uendret
   - hva som eventuelt er endret i BBB
   - ny baseline-dato.

Den viktigste regelen er:

> **«Oppdater modul» betyr ikke “oppsummer siste olje-nyheter”. Det betyr “gjør ny grundig research og test om den eksisterende Oil Market BBB fortsatt er riktig”.**

Og hvis ny informasjon ikke er sterk nok til å endre modellen, skal konklusjonen være eksplisitt: **Oil Market BBB beholdes uendret.**

## Praktisk gjennomføring og dokumentasjon

### Datagrunnlag

1. Les denne prosedyren og siste daterte analyseresultat i Doc. Noter tidligere baseline, scenariointervaller, vekter, premisser og åpne spørsmål.
2. Gjør ny research for alle de 14 punktene over. Bruk tilgjengelige primærkilder for produksjon, lagre, eksport, raffinering og markedspriser, supplert med etterprøvbare nyhetskilder for hendelser.
3. Oppgi kilde med direkte lenke, observasjonsdato, publiseringsdato der den er relevant, enhet og eventuell forsinkelse. Skill observerte tall, eksterne prognoser og egne scenarioantakelser.
4. Marker manglende eller motstridende data. Manglende observasjon betyr ikke at et forhold er uendret. Ikke oppgi konstruerte eller udokumenterte markedsdata.
5. Dokumenter kjeden **ny informasjon → fysisk konsekvens → betydning for BBB** før en endring besluttes.

### Forwardkurver og enheter

Bruk kontrakter som faktisk ligger tre måneder fra hverandre, og oppgi kontraktsmånedene og samme observasjonstidspunkt. Beregn spread som nær kontrakt minus kontrakten tre måneder senere. Positiv verdi er backwardation; negativ verdi er contango. En tomånedersspread skal merkes som to måneder og kan ikke behandles direkte som den definerte tremånedersindikatoren.

Originaloppgavens intervaller overlapper ved nøyaktig 2 USD/fat. For entydig bruk i denne filversjonen benyttes: negativ spread = Loose/Bear; 0 til under 2 = omtrent balansert; 2 til og med 5 = moderat Tight; over 5 = tydelig Tight. Dette er en praktisk presisering, ikke en ny markedsanalyse.

ICE gasoil rapporteres i USD/tonn. Originalprosedyren fastsetter ikke numeriske gasoil-grenser; beskriv styrken med dokumentert sammenligningsgrunnlag. Ikke overfør Brent-grensene til gasoil. For crack-spreader oppgis produkt, råoljereferanse og enhet, og eventuell omregning dokumenteres.

### Fast resultatformat

Hver full oppdatering skal inneholde:

1. **Tittel og metadata:** analyzedato, tidspunkt/tidssone, forrige baseline, datadekning og lenke til prosedyren.
2. **Konklusjon:** om modellen beholdes eller endres, og de viktigste begrunnelsene.
3. **Research:** funn fra alle kontrollområdene, med kilder, datoer og tydelig skille mellom fakta og vurdering.
4. **BBB-tabell:** gjeldende sannsynligheter og Brent-/dieselcrack-intervaller per år i analyseperioden, samt separate vurderinger av råoljetank og produkttank. Vektene innen hver horisont skal summere til 100 %.
5. **Modellbeslutning:** hvilke premisser, vekter eller intervaller som endres, gammel og ny verdi, samt evidensen som utløser endringen.
6. **Videre bruk:** hvilke selskapsanalyser som berøres, og koblingen til relevante markedsdrivere, operasjonelle nøkkeltall, kontantstrøm og verdsettelse.
7. **Usikkerhet og neste kontrollpunkter:** datamangler, motstridende signaler og hva som kan endre konklusjonen.
8. **Endringslogg:** nytt siden forrige baseline, uendret, endret i BBB og ny baseline-dato.

### Lagringsregel

- Selve prosedyren lagres i `C:\GitWork\hsaether\Chatgpt\Finance\Module\Oil Market BBB.md`.
- Hvert analyseresultat lagres som et eget Markdown-dokument i `C:\GitWork\hsaether\Chatgpt\Finance\Doc`.
- Standard filnavn: `Oil Market BBB - ÅÅÅÅ-MM-DD.md`, med analyzedato i filnavnet.
- Ved flere analyser samme dag brukes `Oil Market BBB - ÅÅÅÅ-MM-DD - TTMM.md` med lokal tid i Europe/Oslo. Bevar tidligere resultater.
- Bruk nyeste analysedato, ikke filens endringstid, for å finne siste baseline.
- Etter lagring: les filen tilbake og kontroller dato, tabeller, norske tegn og lenken til prosedyren.
- En eksport av en gammel analyse skal beholde opprinnelig analyzedato og oppgi eksportdato separat.
- Denne dokumentasjonen oppretter ingen automatisk kjøring. Den ukentlige **Oil Market BBB Watch** som er beskrevet i originaloppgaven, bruker samme kontrollområder og beslutningsregler, men med en kortere rapport som starter med røde flagg og avslutter med hva som må følges neste uke.

## Endringslogg for prosedyredokumentet

| Dato | Endring |
|---|---|
| 2026-09-29 | Opprettet fra Oil Market BBB-oppgaven. Bevarte 14-punktsprosedyren og dokumenterte modellpremisser, lokal lagring, rapportformat og praktiske presiseringer for datakvalitet og forward-spreader. Begge mapper besto skrivekontrollen. |

