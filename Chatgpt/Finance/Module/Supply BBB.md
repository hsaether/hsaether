# Supply BBB

## Dokumentinformasjon

- Dokumenttype: gjenbrukbar prosedyre for markedsanalyse av offshore støttefartøy (OSV).
- Opprettet: 29. september 2026.
- Kilde: [Supply BBB](https://chatgpt.com/c/6aae6c65-2d58-83ed-8c34-0922e9bcc399), opprinnelig mandat og prosedyre fra 19. september, med presiseringer 22., 23. og 26. september 2026.
- Prosedyrefil: `C:\GitWork\hsaether\Chatgpt\Finance\Module\Supply BBB.md`.
- Resultatmappe: `C:\GitWork\hsaether\Chatgpt\Finance\Doc`.
- Første lokale resultat: [Supply BBB – 26. september 2026](../Doc/Supply%20BBB%20-%202026-09-26.md).
- Bakgrunnsinformasjon: siste daterte analyser av **Oil Market BBB** og **Rig Market BBB** i Doc. Oppdateringsmetodene finnes i [Oil Market BBB](Oil%20Market%20BBB.md) og [Rig Market BBB](Rig%20Market%20BBB.md).

Dette dokumentet systematiserer prosedyren fra originaltråden. Rapportformat, lokale lagringsregler og kontrollpunkter er praktiske presiseringer for filversjonen. Opprettelsen er dokumentasjon av eksisterende arbeid, ikke en ny markedsanalyse.

## Formål og omfang

Lag en grundig Bear/Base/Bull-analyse for de tre neste hele kalenderårene, ved opprettelsen **2027–2029**. Analyser **område × fartøytype × teknisk kvalitet**, med utilization, rater, etterspørsel, eksisterende kapasitet og nybygg. Resultatet skal være markedsgrunnlag for relevante selskapsanalyser.

Utgangspunktet i originalmodellen er **Bear 25 % / Base 50 % / Bull 25 %**. Bruk siste dokumenterte baseline og test vektene ved hver oppdatering. Kortvarig Bull-vekt i oljemarkedet skal ikke automatisk overføres til et treårig supplyscenario.

### Geografisk dekning

Norge/NCS og UK/Nordsjøen vurderes separat. Øvrige kjerneområder er Brasil, Guyana/CARICOM og øvrig Latin-Amerika, Vest-Afrika, Midtøsten, Sørøst-Asia, Australia, India, US Gulf og Middelhavet. Øst-Afrika og andre områder tas inn når materielle. Definer regionene uten dobbelttelling.

### Fartøyklasser

| Segment | Påkrevd underdeling |
|---|---|
| PSV | Liten, medium og large/high-spec; oppgi DWT, dekksareal, lastekapasitet og relevant teknisk kvalitet |
| AHTS low/mid-spec | Egen vurdering; siste baseline omtaler under 12k BHP som low/mid-spec |
| AHTS mellomklasser | Oppgi eksplisitt plassering av 12–16k BHP og andre grensefartøy; de skal ikke falle ut av flåteregnskapet |
| Large AHTS | Omtrent 16–20k BHP og rundt 180–210 tonn bollard pull, med kildeavhengig definisjon |
| Very Large / true high-end AHTS | Over 20–22k BHP, normalt over 220 tonn bollard pull; teknisk og regional egnethet avgjør |
| CSV/MPSV | Eget specialist-segment |
| ROVSV/RSV | Eget specialist-segment; definer betegnelsene og unngå overlapp |
| DSV og pipelay | Separate segmenter når relevante |
| OSRV og øvrige specialist-fartøy | Tas med når de påvirker etterspørsel eller tilbud vesentlig |

**Over 200 tonn bollard pull er ikke synonymt med true high-end AHTS.** Bruk BHP, bollard pull, winch, deck, DP, design og regional kvalifikasjon sammen. Kildenes terskler ved 20k og 22k BHP er ikke identiske; behold definisjonen ved sammenligning. Specialist-fartøy blandes ikke inn i PSV/AHTS-totaler uten en eksplisitt avstemming av universet.

## Instruksjonen «Oppdater modul»

**«Oppdater modul» i Supply BBB-sammenheng**, eller **«Oppdater Supply BBB»** fra en annen oppgave, betyr:

1. Hent og les denne prosedyren.
2. Les siste daterte Supply BBB-analyse og noter forutsetninger, scenarioer, datamangler og kontrollpunkter.
3. Hent siste Oil Market BBB- og Rig Market BBB-analyser fra Doc, og noter dato/status for begge.
4. Gjennomfør hele oppdateringsprosedyren nedenfor med ny research.
5. Oppdater analysen, dokumenter hva som er endret og lagre et nytt datert Markdown-dokument i Doc.
6. Les resultatet tilbake og kontroller innhold og lenker.

Kommandoen oppdaterer **analysedokumentet**. Prosedyrefilen endres ved uttrykkelig metodeendring eller dokumentert nødvendig presisering. Kjøringen er manuell.

Originalprosedyren sier «Oppdater Oil Market BBB og hent siste Rig Market BBB som input». I denne filbaserte arbeidsflyten hentes begge bakgrunnsanalysene først. Ved behov for å oppdatere oljegrunnlaget brukes Oil Market BBBs egen prosedyre og separat output. Et manglende eller vesentlig utdatert olje-/rigggrunnlag skal synliggjøres; et avhengig Supply-resultat merkes foreløpig inntil grunnlaget er tilstrekkelig.

## Fast oppdateringsprosedyre

### 1. Etabler sammenlignbar baseline og bakgrunn

Hent forrige Supply-baseline og siste Oil/Rig BBB. Registrer oljeprisbaner, offshore capex-retning, regional riggaktivitet, riggtyper og endringer siden sist. Bruk bakgrunnsmodulene som felles forutsetninger; unngå en konkurrerende olje- eller riggprognose uten eksplisitt begrunnelse.

Skill langsiktig prosjektøkonomi fra kortvarig oljeprissjokk. Oljepris, operasjonelle avbrudd og faktisk offshoreaktivitet kan trekke i ulik retning.

### 2. Oppdater dagens marked per område og fartøyklasse

Hent aktiv og marketed flåte, tilgjengelige fartøy, utilization, spotrater, termrater, leading-edge fixtures, kontraktsdekning og backlog. Oppgi periode, definisjon, teknisk klasse og valuta.

Skill spotmarked fra termmarked og markedstall fra ett selskaps realiserte rater. Tidewaters regionale gjennomsnitt er for eksempel indikatorer for selskapets flåtemiks, ikke rene markedsindekser. Samme utilization i Midtøsten og Nordsjøen innebærer ikke samme økonomi.

Bruk siste komplette månedsrapport som normalisert referanse. Suppler med ferske fixtures og tilgjengelighetsdata. En ufullstendig live-visning erstatter ikke en sammenlignbar månedsserie.

### 3. Oversett Rig BBB og prosjektaktivitet til vessel-demand

Kartlegg rig campaigns, rig moves, FPSO-er, feltutbygginger, EPCI/subsea, produksjonsstøtte, decommissioning og eventuell offshore-wind cross-trading.

- PSV: aktive riggdager × PSV per rigg, pluss produksjonsstøtte, prosjektarbeid og øvrig aktivitet.
- AHTS: rig moves, mooring/anchor work, drilling support og prosjektarbeid, med antall fartøy og varighet per oppdrag.
- Specialist: prosjektplaner og fartøydager for den aktuelle typen og tekniske kvalifikasjonen.

Angi forutsetningene for omregning til vessel-days og unngå overlapp mellom etterspørselskategorier. Skill kontrahert arbeid, tendere og usikre prosjekter. Bekreft om kilden oppgir riggdager, riggår, antall rigger eller annen enhet før omregning.

### 4. Oppdater eksisterende og effektiv kapasitet

Kartlegg alder, laid-up/stacked, realistisk reaktivering, kostnad/ledetid, skraping, konverteringer, vedlikehold og tekniske kvalifikasjoner. Vurder hvilke fartøy som faktisk kan konkurrere om oppdragene.

Registrer flytting mellom regioner. Innflytting øker regional kapasitet, men ikke global kapasitet. Eierskifter og konsolidering endrer heller ikke fysisk flåte. Vurder eventuell kommersiell disiplin separat fra antall tilgjengelige skip.

### 5. Bygg en egen nybyggmodell

| Felt | Krav |
|---|---|
| Identitet og antall | Fartøy/prosjekt, eier og verft der kjent |
| Type/spec | PSV, AHTS eller specialist; BHP, BP, DWT, deck og andre relevante egenskaper |
| Status | Firm ordre, opsjon, procurement/pipeline eller intensjon |
| Finansiering/arbeid | Speculative eller contract-backed; kontrakt og finansiering hvis dokumentert |
| Levering | År, forventet operativ dato, forsinkelsesrisiko og oppstartsperiode |
| Region | Planlagt marked og eventuell lokal binding |
| Økonomi | Nybyggpris, valuta, byggetid og relevant rate-/kontraktskrav |
| Kilde | Direkte lenke, publiseringsdato, observasjonsdato og flåtedefinisjon |

Ikke tell pipeline og opsjoner som sikre leveranser. En levert enhet flyttes fra orderbook til operativ flåte og telles ikke to ganger. Fordel Brasil-programmer på faktiske skipstyper; PSV/RSV/OSRV er ikke AHTS-kapasitet. Bekreft spesifikasjoner for nye ordre fremfor å utlede dem bare fra eiers eksisterende flåte eller lav kontraktspris.

Orderbook/fleet skal ha samme dato og univers. Ikke bland historiske Westwood-, Veson- eller andre tall med ulik dekning til én presis nåverdi.

### 6. Følg kapitalsyklusen før nybyggene bestilles

Fast indikator fra 26. september:

**Secondhand-verdier → newbuild parity → tilgjengelig egenkapital/gjeld → nybygg-IRR → faktiske ordre.**

Oppdater transaksjonsverdier, nybyggpriser, finansiering, forventet avkastning og kontraktsdekning som kan utløse bestillinger. Skill kapital brukt til M&A/refinansiering fra kapital brukt til nybygg. Selskapenes egne vurderinger av rabatt til replacement cost kontrolleres separat.

Test særlig om tilbudsresponsen flytter seg fra low/mid-spec til 16–20k BHP og videre til over 20/22k BHP. Dette er en løpende indikator, ikke en fast påstand om at high-end alltid mangler nybygg.

### 7. Bygg tilbuds- og etterspørselsbalansen for hvert år

Beregn regional og global utvikling per klasse:

**Sluttflåte = startflåte + leveranser + reaktiveringer − skraping/uttak ± konverteringer + innflytting − utflytting.**

Avstem globalt slik at regionale flyttinger summerer til null. Behandle konverteringer konsistent mellom segmentene. Vis både antall fartøy og effektiv tilgjengelig kapasitet når forskjellen er viktig. Beregn netto flåtevekst med samme definisjon ved start og slutt.

Sammenhold etterspurte fartøydager med tilgjengelige fartøydager. Ikke presenter kontrahert utilization, spotutnyttelse, marketed utilization og totalflåteutnyttelse som samme mål.

### 8. Test Bear/Base/Bull per område × fartøytype

For hvert av de tre analyseårene: angi utilization-intervall, rateintervall, netto flåtevekst og viktigste forutsetninger. Oppgi datadekning og usikkerhet. Samle til global Supply BBB med dokumentert vekting; unngå enkelt gjennomsnitt av ulike regioner og fartøyklasser.

Bruk siste baseline som startpunkt. Test om svakere aktivitet, prosjektutsettelser, reaktivering eller nybygg endrer Bear; om Rig BBB og leveranseplaner støtter Base; og om samtidige rig moves/prosjekter og knapp kvalifisert kapasitet gir større rateutslag i Bull.

High-end AHTS kan ha høy spotrate selv ved moderat gjennomsnittlig utilization fordi oppdrag krever flere kvalifiserte fartøy samtidig. Modeller **rate per arbeidsdag og antall inntektsdager separat**. Ikke annualiser en ekstrem spotrate med 365 dager, og ikke multipliser utilization inn en gang til dersom raten allerede er målt per tilgjengelig dag.

### 9. Kontroller triggere og beslutt endringer

Vurder særlig:

- Endringer i regional riggaktivitet, FPSO-/EPCI-planer og prosjektutsettelser.
- NCS versus UK, Brasil PSV-leveranser og high-end AHTS, samt APAC high-spec versus low/mid-spec.
- Varige endringer i fixtures, termrater, arbeidende fartøydager og ledig kvalifisert kapasitet.
- Firm nybyggordre i large og very large AHTS, samt vesentlig reaktivering av laid-up large AHTS.
- Tidligere PSV/RSV-leveranser, India/Kina-programmer og tonnasjeflytting mellom regioner.
- Økende tilgang på kapital og nybyggøkonomi som kan varsle senere tilbudsvekst.

Dokumenter **ny informasjon → etterspørsel/effektiv kapasitet → utilization/rater → BBB-beslutning**. Oppgi gammel og ny verdi eller vurdering, årsak og kilde. Scenarioene kan beholdes selv om enkelte regioner endres. Manglende data betyr ikke at markedet er uendret. Scenario­vektene skal summere til 100 %.

### 10. Klargjør input til selskapsanalysene

Bruk følgende mapping:

**Fartøy → størrelse/spec → region → kontraktstype → relevant utilization → relevant rate → lokal kapasitet/nybygg → Rig BBB-demand.**

Vis hvilke eksponeringer som påvirkes. Faktisk kontraktsdekning, realisert rate, kostnader, offhire, investeringer og finansiering håndteres i selskapsanalysen. En generell formulering om at «OSV-markedet er sterkt» er ikke tilstrekkelig modellinput.

## Kilder og datakvalitet

Bruk tilgjengelige offentlige Westwood-publikasjoner, Seabrokers, Fearnley/FOSLive, Braemar, operatør-/verftsmeldinger, Petrobras-tendere, børsmeldinger og flåte-/kvartalsrapporter fra relevante selskaper. Betalte databaser brukes bare når faktisk tilgjengelige. Ingen bestemt datadekning forutsettes uten kontroll.

Oppgi direkte lenker, datoer, enheter og definisjoner. Skill rapporterte observasjoner, eksterne prognoser og egne modellestimater. Trianguler kilder og forklar avvik. Ved utilstrekkelige data brukes begrunnede intervaller eller «ikke tilgjengelig» fremfor falsk presisjon. Historiske påstander om null orderbook må testes på nytt.

## Fast resultatformat

1. Metadata: analyzedato/tidssone, analyseår, status, prosedyrelenke, forrige Supply-baseline og brukte Oil/Rig BBB-versjoner med lenker.
2. Hovedkonklusjon og endringer i BBB, med segmentrangering og begrunnelse.
3. Nye funn siden sist med kilder og datoer.
4. Dagens marked: region × fartøyklasse, utilization, spot/term/leading-edge rater, flåte og tilgjengelighet.
5. Etterspørsel fra Rig BBB og prosjektaktivitet, med antakelser for fartøydager.
6. Nybyggtabell, reaktivering, skraping, konverteringer, flåteflytting og årlig netto kapasitet.
7. Kapitalsyklus og nybyggøkonomi per relevant segment.
8. Bear/Base/Bull-tabeller per region/klasse/år og global sammenstilling: vekter, utilization, rater og netto flåtevekst.
9. Modellbeslutning, triggere, berørte selskapseksponeringer og begrensninger.
10. Endringslogg: nytt, uendret, endret i BBB, neste kontrollpunkter og ny baseline-dato.

## Lagringsregel

- Prosedyren lagres i `Module\Supply BBB.md`.
- Hvert output lagres separat som `C:\GitWork\hsaether\Chatgpt\Finance\Doc\Supply BBB - ÅÅÅÅ-MM-DD.md`.
- Ved flere oppdateringer samme dag tilføyes ` - TTMM` i lokal tid Europe/Oslo; bruk sekunder ved behov. Bevar tidligere analyser.
- Siste fullførte, daterte analyse er gjeldende baseline. Bruk analyzedato og status, ikke filens endringstid. Foreløpige utkast erstatter ikke automatisk en fullført baseline.
- Historiske eksporter beholder opprinnelig analyzedato og oppgir eksportdato separat. En historisk baseline kan brukes som sammenligningsgrunnlag, men er ikke nyverifiserte markedsdata.
- Etter lagring kontrolleres eksistens, lesbarhet, norske tegn, tabeller, datoer, enheter, scenarioår og lokale lenker.

## Endringslogg for prosedyren

| Dato | Endring |
|---|---|
| 2026-09-29 | Opprettet fra Supply BBB-tråden. Bevarer område-/fartøymodellen og senere presiseringer om AHTS-klasser, orderbook, Brasil, APAC og kapitalsyklus. Definerer Oil/Rig BBB som bakgrunn, manuell oppdatering og datert output i Doc. |
