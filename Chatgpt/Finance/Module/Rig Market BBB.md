# Rig Market BBB

## Dokumentinformasjon

- Dokumenttype: gjenbrukbar prosedyre for riggmarkedsanalyse.
- Opprettet: 29. september 2026.
- Kilde: [Rig Market BBB](https://chatgpt.com/c/6aae64d8-ee00-83eb-9443-e51fb5c4e431), mandat og prosedyre fra 19. september, med presiseringer fra 22. og 26. september 2026.
- Prosedyrefil: `C:\GitWork\hsaether\Chatgpt\Finance\Module\Rig Market BBB.md`.
- Resultatmappe: `C:\GitWork\hsaether\Chatgpt\Finance\Doc`.
- Første lokale resultat: [Rig Market BBB – 26. september 2026](../Doc/Rig%20Market%20BBB%20-%202026-09-26.md).
- Obligatorisk input: siste daterte **Oil Market BBB-analyse** i Doc. [Oil Market BBB-prosedyren](Oil%20Market%20BBB.md) beskriver oppdatering av oljegrunnlaget.

Dette dokumentet systematiserer prosedyren fra originaltråden. Lokal lagring, rapportformat og kontrollregler er praktiske presiseringer for filversjonen. Opprettelsen er dokumentasjon og eksport av eksisterende arbeid, ikke en ny markedsanalyse.

## Formål og analyseomfang

Lag en grundig Bear/Base/Bull-analyse av riggmarkedet for de tre neste hele kalenderårene, ved opprettelsen **2027–2029**. Vurder riggtype, kvalitet, region, oljeprisfølsomhet, kapasitetsutnyttelse, rater og ekspansjon i konkurransedyktig riggtilbud.

Utgangspunktet i originalmodellen er **Bear 25 % / Base 50 % / Bull 25 %**. Vekter og scenariointervaller er analyseforutsetninger som testes ved hver oppdatering. Bruk siste dokumenterte baseline; ikke nullstill modellen til første versjon.

| Riggtype | Segmentering |
|---|---|
| Jackups | Premium/high-spec og eldre standardenheter; norske HE-jackups vurderes separat |
| Drillships | Tier-1/high-spec, primært 6./7. generasjon |
| Semisubs | Harsh-environment og benign/deepwater |
| Andre | Tender-assist og platform rigs når relevante |

Geografisk dekning: Middle East, Norge/North Sea, UK/NW Europe, Brasil/South America, US Gulf, West Africa, Southeast Asia, India og Mexico. Australia, Canada og Mediterranean inkluderes når relevante. Bruk entydige geografiske avgrensninger slik at overlappende regionnavn ikke dobbelttelles.

## Instruksjonen «Oppdater modul»

**«Oppdater modul» i Rig Market BBB-sammenheng**, eller **«Oppdater Rig Market BBB»** fra en annen oppgave, betyr:

1. Hent og les denne prosedyren.
2. Les siste daterte, fullførte Rig Market BBB-analyse i Doc.
3. Hent siste daterte Oil Market BBB-analyse i Doc og noter baseline, scenarioer og endringer siden oljegrunnlaget brukt sist.
4. Gjennomfør hele prosedyren nedenfor med ny research.
5. Test og oppdater analysen, dokumenter endringer og lagre et nytt datert Markdown-dokument i Doc.
6. Les resultatet tilbake og kontroller innhold og lenker.

Kommandoen oppdaterer **analysedokumentet**. Selve prosedyren endres ved en uttrykkelig metodeendring eller en dokumentert nødvendig presisering. Arbeidsflyten er manuell.

## Fast oppdateringsprosedyre fra originaltråden

Originalens sammenhengende prosedyre er her delt i ti arbeidssteg:

### 1. Importer Oil Market BBB

Bruk siste oljeanalyse som felles makrogrunnlag. Importer oljeprisbaner per scenario og år, etterspørsel, Midtøsten og geopolitikk. Lag ikke en konkurrerende oljeprognose i riggmodulen.

Analyser kjeden:

**Oljepris → E&P-kontantstrøm → offshore capex/FID → riggetterspørsel → utilization → dagrate.**

Vurder tidsforsinkelsene og oljeprisfølsomheten per segment. Skill sanksjonerte prosjekter og strategiske NOC-programmer fra fremtidig FID og leteboring. Vurder oljepriseffekt og operasjonell geopolitisk risiko separat; høy oljepris kan opptre samtidig med evakuering, offhire og lavere faktisk aktivitet.

Hvis oljegrunnlaget mangler eller er vesentlig utdatert, marker dette konkret. En analyse som avhenger av et utilstrekkelig grunnlag merkes foreløpig. Ikke presenter eldre oljeforutsetninger som nyverifiserte.

### 2. Oppdater rig count, utilization og availability

Hent siste globale og regionale riggtall, månedlig utilization, tilgjengelig kapasitet, cold/warm stacked og backlog. Bruk ferske ukentlige tellinger som supplement til siste komplette månedsdatasett.

Skill marketed committed utilization, working utilization og total utilization. Oppgi kildens definisjon og nevner; kontraherte rigger kan være midlertidig ute av drift. Ukentlig working count erstatter ikke månedlig utilization eller backlog.

### 3. Samle faktiske fixtures og rate-slutninger

Registrer nye kontrakter med rigg, type/spec, region, operatør, annonseringsdato, oppstart, fast varighet, opsjoner, dagrate og kilde. Sammenlign med tidligere slutninger og 6–12 måneders trend.

Bruk **leading-edge rater og siste faktiske fixtures per region og riggklasse**. Skill rene dagrater, kontraktsverdi per dag og realiserte langsiktige kontraktsrater. Mobilisering, tjenester, bonus og eskalering kan gjøre kontraktsverdi/dager misvisende som ren dagrate.

### 4. Gjennomgå riggselskapenes flåtestatus

Les fleet-statusrapporter, resultater og børsmeldinger fra blant annet Transocean, Valaris, Noble, Seadrill, Borr, Odfjell, ADES, Shelf og relevante regionale aktører. Kontroller dagens selskaps- og riggeierskap ved hver kjøring.

Oppdater rigg-for-rigg availability for hvert analyseår: kontraktsutløp, opsjoner, ledige perioder, verftsopphold, mobilisering og geografisk tilgjengelighet. Skill fast backlog fra usikre opsjoner.

### 5. Undersøk operatørenes etterspørsel

Kontroller drilling plans, tenders, FID og capex hos Petrobras, Equinor, Aker BP, Vår Energi, Aramco, ADNOC, QatarEnergy, Exxon, Chevron, Shell, BP, TotalEnergies, Eni, Petronas, PTTEP og ONGC, samt andre relevante operatører.

Skill prospects, utlyste anbud, tildelte kontrakter og pågående arbeid. Oversett dokumentert aktivitet til riggdager/riggår når mulig. Nye brønner eller funn er ikke automatisk nye riggkontrakter.

### 6. Oppdater reelt riggtilbud og ekspansjon

Undersøk nybygg, stranded units, levering, reaktivering, skraping og retirement. Bruk:

**Nominell ordrebok → sannsynlig levering → konkurransedyktig kapasitet.**

Vurder finansiering, teknisk standard, ferdigstillelseskostnad, kontraktsdekning og tid til oppstart for den enkelte enheten. Gamle uferdige eller cold-stacked rigger telles ikke automatisk som tilgjengelig tilbud. Sannsynligheter skal begrunnes; illustrasjonene i originaltråden er ikke faste standardvekter.

Oppdater nybyggkostnad, byggetid, nødvendig dagrate og kontraktslengde, samt reaktiveringskostnad og ledetid. Test om dagens rater faktisk kan utløse en tilbudsrespons innen analyseperioden.

Regional flytting gir økt kapasitet i mottakerregionen og redusert kapasitet i avsenderregionen, uten å øke globalt antall rigger. Eierskifter og konsolidering skaper heller ikke nye rigger. Unngå dobbelttelling mellom nybygg, reaktivering og allerede markedsført flåte.

### 7. Bygg regional tilbuds- og etterspørselsbalanse

For hver relevant region × riggklasse, oppdater:

| Nøkkeltall | Enhet / presisering |
|---|---|
| Marketed committed utilization | Prosent, med definisjon |
| Working utilization og total utilization | Separate mål når tilgjengelige |
| Marketed available | Antall |
| Cold/warm stacked | Antall, hver for seg |
| Leading-edge rate | USD/dag |
| Ratetrend siste 6–12 måneder | Retning og dokumenterte observasjoner |
| Ledig kapasitet per analyseår | Riggår |
| Tender/prospect demand | Riggår, skill sikkerhet/stadium |
| Nybygg og reaktivering | Antall og forventet tilgjengelighetsdato |
| Retirement potential | Antall, begrunnet |
| Netto flåtevekst | Prosent, med eksplisitt flåtedefinisjon |
| Oljeprisfølsomhet | Lav/middels/høy, med begrunnelse |

Vis både nominell og effektiv kapasitet når forskjellen er vesentlig. Beregn vekst med sammenlignbare flåtedefinisjoner ved start og slutt. Marker datamangler fremfor å konstruere presise regionale estimater.

### 8. Sett og test Bear/Base/Bull

Oppdater marketed committed utilization og leading-edge dagrater for hvert segment og hvert analyseår. Vurder regionale avvik eksplisitt. Scenarioene skal følge oljegrunnlaget, men også reflektere riggspesifikt tilbud, kvalitet, kontraktslengde og konkurranse.

Skill stigende aktivitet fra økt evne til å oppnå høyere rater. Thailand/APAC-eksemplet i siste baseline viser at utilization kan stige samtidig som aggressive tilbud holder ratene nede, og at jackups kan erstatte tender-assist.

Ikke bruk dagens ekstreme oljepris som permanent treårsforutsetning. Ikke overfør global premium-jackup-rate direkte til eldre standardrigger, tender-assist eller norske HE-jackups.

### 9. Vurder indikatorer som flytter scenarioene

Følgende indikatorer kommer fra baseline 19. september; de er kontrollpunkter, ikke automatiske beslutningsregler:

| Indikator | Mot Bear | Mot Bull |
|---|---|---|
| Tier-1 drillship utilization | Under 90 % | Over 96–97 % |
| Tier-1 fixtures | Under USD 400 000/dag | Over USD 500 000/dag med lang varighet |
| NCS HE availability | Ledige rigger i de nærmeste analyseårene | Fullbooket langt frem i analyseperioden |
| Petrobras tenders | Utsettelser/kanselleringer | Nye flerårige tildelinger |
| West Africa tenders | FID-utsettelser | Namibia/Nigeria/Mozambique konverterer til arbeid |
| Saudi/UAE jackups | Tidlige termineringer | Suspenderte rigger tilbake og nye kontrakter |
| APAC | Vedvarende lav semi-utilization | Langvarige Malaysia/Indonesia-kontrakter |
| Reaktivering | Mange rigger returnerer | Få returer grunnet svak økonomi |
| Nybygg | Store nye ordre | Fortsatt liten kommersiell respons |
| Offshore FID/EPC | Kraftig fall | Fortsatt vekst |

Tillegg fra 26. september: Undersøk faktiske PTTEP/Foresight-rater. Rater vesentlig under omtrent USD 100 000/dag, kombinert med tilsvarende konkurranse i Vietnam/Malaysia/Indonesia, kan begrunne formell nedjustering av APAC-ratecaset. Dette er et betinget kontrollpunkt; originaltråden hadde ikke offentlig bekreftede vinnerrater.

### 10. Beslutt endringer og dokumenter ny baseline

Sammenlign med forrige analyse: **ny informasjon → effekt på tilbud/etterspørsel → effekt på utilization/rater → eventuell endring i BBB**.

Oppgi eksplisitt om vekter og intervaller beholdes eller endres. Én regional kontrakt skal ikke uten begrunnelse endre hele den globale modellen. Vis gammel og ny verdi, årsak, kilde og berørte regioner/selskaper. Vektene skal summere til 100 %.

## Datakvalitet og kildebruk

Bruk tilgjengelige primærkilder: offentlige Westwood/RigLogix-publikasjoner, operatørmeldinger, innkjøpsplaner, fleet-statusrapporter, børsmeldinger, presentasjoner og relevante myndigheter. Suppler med etterprøvbare bransjekilder. Betalt RigLogix/Petrodata kan brukes dersom faktisk tilgjengelig; prosedyren forutsetter ikke slik tilgang.

Oppgi direkte kildelenke, observasjonsdato, publiseringsdato, enhet og definisjon. Skill rapporterte data, eksterne prognoser og egne scenarioantakelser. Ukjent rate eller manglende flåtedata skal merkes ukjent. Manglende nye observasjoner er ikke dokumentasjon på uendret marked.

## Fast resultatformat

Hvert analyseresultat inneholder:

1. Metadata: analyzedato og tidssone, analyseår, status, forrige riggbaseline, brukt Oil Market BBB-baseline og lenker til input/prosedyre.
2. Hovedkonklusjon: endret eller uendret BBB, segmentrangering og viktigste begrunnelser.
3. Nye funn siden sist, med datoer og kilder.
4. Region × riggtype-matrise med utilization, rater, tilgjengelighet, etterspørsel og tilbud.
5. Fixture-oversikt og rigg-for-rigg tilgjengelighet der data finnes.
6. Nybygg, reaktivering, skraping, nybyggøkonomi og netto effektiv kapasitetsendring.
7. Kobling fra oljescenarioene til regional capex, FID og riggetterspørsel.
8. BBB-tabeller: Bear/Base/Bull utilization og dagrater per år for Tier-1 drillships, NCS HE semis, benign/deepwater semis og premium jackups. Andre segmenter vurderes separat, med datamangler synliggjort.
9. Triggerkontroll, modellbeslutning og konsekvenser for relevante selskapsanalyser.
10. Usikkerhet, neste kontrollpunkter og endringslogg: nytt, uendret, endret og ny baseline-dato.

Markedsrater er input til selskapsanalysene. Faktisk kontraktsdekning, realisert rate, inntjeningsdager, kostnader, investeringer og gjeld må håndteres separat.

## Lagringsregel

- Prosedyren ligger i `Module\Rig Market BBB.md`.
- Output lagres i `C:\GitWork\hsaether\Chatgpt\Finance\Doc\Rig Market BBB - ÅÅÅÅ-MM-DD.md`.
- Ved flere oppdateringer samme dag tilføyes ` - TTMM` med lokal tid Europe/Oslo; bruk sekunder ved behov. Bevar tidligere analyser.
- Siste fullførte, daterte analyse er gjeldende baseline. Bruk analyzedato og status, ikke filens endringstid. Et foreløpig utkast erstatter ikke en fullført baseline uten uttrykkelig beslutning.
- Historisk eksport beholder original analyzedato; eksportdato oppgis separat.
- Etter lagring kontrolleres filens eksistens, lesbarhet, norske tegn, tabeller, scenarioår, enheter og lokale lenker.

## Endringslogg for prosedyren

| Dato | Endring |
|---|---|
| 2026-09-29 | Opprettet fra Rig Market BBB-tråden. Systematisert opprinnelig prosedyre, region-/riggmatrise, triggere og senere presiseringer. Definert Oil Market BBB som obligatorisk input og datert output i Doc. |

