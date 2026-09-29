# Paratus – analyse- og oppdateringsprosedyre

**Versjon:** 1.0  
**Opprettet og vurdert:** 29. september 2026  
**Prosedyrefil:** `C:\GitWork\hsaether\Chatgpt\Finance\Procedure\Paratus.md`  
**Resultatmappe:** `C:\GitWork\hsaether\Chatgpt\Finance\Doc`  
**Siste lagrede analyse:** [Paratus – 2026-09-26](../Doc/Paratus%20-%202026-09-26.md), historisk eksport med kontrollmerknader.  
**Opprinnelse:** [Paratus Analyse](https://chatgpt.com/c/6a9877b0-b77c-83ed-89d4-470baf888f5b), særlig avtalt analysehierarki, fartøymodell, kapitalstruktur og siste oppdateringer 19. og 26. september 2026.

Dette dokumentet systematiserer og forbedrer arbeidsmåten fra originaltråden. Opprettelsen omfatter metodevurdering og eksport av siste analyseresultat; den er ikke en ny selskapsanalyse med ferske markedsdata. Historiske selskaps- og modellverdier skal verifiseres ved neste kjøring.

## 1. Formål, avgrensning og input

Analyser Paratus fra fartøy og kontrakter til kontantstrøm som faktisk er tilgjengelig for Paratus-aksjonærene. Vurder normalisert økonomi per aksje, kapitalbehov, risiko, verdsettelse og investoravkastning.

| Input | Rolle |
|---|---|
| [IAF](../Investment_Analysis_Framework_IAF.md) | Overordnet beslutnings- og verdsettelsesramme. Ved opprettelsen v1.1, normalt k = 12 %, 3–5 år og Bear/Base/Bull 25/50/25. |
| Siste daterte Supply BBB-analyse i Doc | Direkte markedsinput for Brasil/PLSV/subsea. Beholdes fra brukerens uttrykkelige føring i originaltråden. |
| Siste daterte Rig Market BBB-analyse i Doc | Bakgrunn for brasiliansk offshoreaktivitet, brønner og fremtidig subseabehov; også relevant for pant/tilbakebetalingsevne knyttet til selgerkreditt når dokumentert. |
| Siste daterte Oil Market BBB-analyse i Doc | Bakgrunn for Petrobras' investeringskapasitet, prosjektøkonomi og utsettelsesrisiko. |
| Siste daterte Paratus-analyse i Doc | Utgangspunkt for antakelser, endringer og åpne kontrollpunkter. |
| Siste rapporter, børsmeldinger og kontraktsinformasjon | Primærkilder for selskapsfakta og faktisk utvikling. |

Tilgjengelige markedsbaseliner ved opprettelsen: [Supply BBB](../Doc/Supply%20BBB%20-%202026-09-26.md), [Rig Market BBB](../Doc/Rig%20Market%20BBB%20-%202026-09-26.md) og [Oil Market BBB](../Doc/Oil%20Market%20BBB%20-%202026-09-26.md), alle datert 26. september. Disse er historiske eksporter med egne kildebegrensninger.

Markedsresultatene hentes fra **Doc**. Filene i **Module** er oppdateringsprosedyrer, ikke nye markedsdata. Les gjeldende IAF ved hver kjøring og oppgi versjonen. Hold rammeverket stabilt.

Bare Paratus er analyseobjekt. Bruk informasjon fra DOF, Dolphin og andre når den belyser Paratus; ikke lag en selvstendig selskapssammenligning uten bestilling. Riggrater, PSV-rater og AHTS-rater skal ikke brukes som PLSV-rater.

## 2. Hva «Oppdater» betyr

**«Oppdater» i Paratus-sammenheng**, eller **«Oppdater Paratus»** fra en annen oppgave, betyr:

1. Les denne prosedyren, gjeldende IAF og siste daterte Paratus-analyse.
2. Les siste daterte Oil, Rig og Supply BBB-resultater. Registrer dato, status og relevante endringer.
3. Hent nye selskapsmeldinger, rapporter, kontrakter og markedsbevis siden forrige datagrense.
4. Oppdater fartøy-for-fartøy-modellen, Seagems, holding, selgerkreditt, finansiering og aksjeantall.
5. Beregn årlige Bear/Base/Bull-kontantstrømmer, normalisert vekst, verdsettelse og investor-IRR.
6. Forklar hva som har endret seg, hva som er priset inn og hva som kan svekke eller bekrefte tesen.
7. Lagre et nytt datert analysedokument i Doc, kontroller det og oppdater lenken til siste analyse her.

En vanlig selskapsoppdatering bruker de tilgjengelige markedsbaselinene. Hvis de er vesentlig utdaterte eller motsies av nye hendelser, synliggjør dette og bruk dokumenterte selskapsspesifikke sensitiviteter. Ikke kall gammel markedsinput nyverifisert. Ved bestilling av hele kjeden oppdateres **Oil → Rig → Supply → Paratus**, etter de respektive modulprosedyrene.

Manglende vesentlige data gir status **foreløpig**, med konkret forklaring av hvilke resultater som ikke kan underbygges. Fullfør dokumenterbare deler. Kommandoen oppdaterer analysen; metodeendringer loggføres særskilt. Dette er en arbeidsflyt på bestilling.

## 3. Kilder og datagrunnlag

Start med selskapets meldinger via børsens offisielle meldingskanal og selskapets IR-side; les siste kvartalsrapport, presentasjon og flåte-/kontraktsoversikt. Kontroller også Petrobras' offisielle planer og relevante anbud/tildelinger. En IR-side eller søketreff alene er ikke tilstrekkelig grunnlag for «ingen nye meldinger».

Registrer hver vesentlig input med kilde/URL, publiseringsdato, hvilken periode den gjelder, lesedato, valuta/enhet og status: rapportert faktum, selskapsguiding, markedsanslag eller eget modellanslag.

Kontroller spesielt:

- Selskap, ticker, børs, aksjekurs og tidspunkt; dagens aksjer, egne aksjer og mulig utvanning.
- Eierandel i Seagems, rapporteringsmetode og hvilke virksomheter som faktisk inngår etter eventuelle salg.
- Kontraktsrater, start/slutt, opsjoner, indeksregulering, USD/BRL-komponenter og betalbare driftsdager.
- JV- og holdinggjeld hver for seg, renter, avdrag, forfall, innløsningspremier, covenants og bundet cash.
- Selgerkredittens hovedstol, rentetrinn, betalingsform, forfall, sikkerheter, prioritet og kredittrisiko.
- Vedtatte utbytter, ex-datoer og betalingsdatoer; forventede utbytter må merkes som modellanslag.

Avstem videreført virksomhet mot historiske konserntall. Ikke sammenlign justert EBITDA, JV-EBITDA og holdingresultat uten en bro. Avstem gjeld og cash fra rapportdato til analyzedato; proforma-tall og gjennomførte transaksjoner må ikke blandes.

## 4. Marked: Petrobras og faktisk konkurrerende PLSV-kapasitet

Bruk Supply BBBs relevante delmarked, supplert med konkrete PLSV-kontrakter og anbud. Globale OSV-utnyttelsesgrader er ikke Seagems' tekniske utnyttelse.

Undersøk Petrobras' sanksjonerte feltutbygginger, FPSO-planer, subseainstallasjon, tie-ins og vedlikehold. Skill vedtatt aktivitet fra ambisjoner og betingede investeringer. Lav prosjekt-breakeven alene garanterer ikke kontraktstildeling eller uendret CAPEX.

Kartlegg konkurrerende fartøy etter kapasitet, teknisk egnethet, lokal kvalifikasjon, geografisk tilgjengelighet og kontraktsutløp. Skille mellom ny fysisk kapasitet, eierskifte og flytting av eksisterende kapasitet. Et anbud, akseptert bud, endelig tildeling og signert kontrakt er forskjellige stadier.

Bruk Oil og Rig BBB til å teste aktivitetsgrunnlaget og tidsforsinkelser. Ikke legg en ekstra olje- eller riggpremie på PLSV-rater som allerede gjenspeiler det samme markedssynet. Behold 25/50/25 som utgangspunkt; begrunn eventuelle endringer.

## 5. Fartøy-for-fartøy-modell

Historiske fartøynavn fra tråden er Diamante, Topázio, Esmeralda, Ônix, Jade og Rubi. Verifiser flåte og eierskap ved hver oppdatering.

Lag én rad per fartøy og kontraktsperiode med:

| Felt | Krav |
|---|---|
| Identitet og kapasitet | Navn, alder, pipelay-kapasitet, operatør/eier og eventuelt innleieforhold. |
| Kontrakt | Kunde, fast periode, opsjoner, rate, eskalering og kilde. |
| Kalender | Dager på gammel kontrakt, kontraktsgap, mobilisering, dokking og ny kontrakt. |
| Drift | Teknisk tilgjengelighet, kommersiell dekning, betalbare dager og eventuelle reduserte rater. |
| Kostnader | OPEX også under relevante ledige dager, charter, skatt/avgifter, vedlikehold og vekstinvesteringer. |
| Resultat | Inntekter, EBITDA og kontantstrøm med tydelig 100 %- eller Paratus-andel. |

Bruk kvartalsvis modell rundt kontraktsutløp og finansieringshendelser, deretter årlig sammenstilling. Nye rater får bare effekt etter faktisk/forutsatt kontraktsstart. Kalenderdager må avstemmes, inklusive skuddår.

```text
Fartøysinntekt = sum(rate per kontraktsperiode × betalbare dager)
              + øvrige dokumenterte inntekter
Betalbare dager bygger på kontraktsdekning og teknisk tilgjengelighet.
```

Ikke trekk det samme kontraktsgapet eller dokkeoppholdet både eksplisitt og gjennom en samlet utilization-faktor. Driftskostnader faller ikke automatisk bort når inntekten stopper. Definer skattenes beregningsgrunnlag; inntektsavgifter og overskuddsskatt er forskjellige poster.

EDD (Extended Dry-Docking) må dokumenteres per fartøy. Modellér tidsbestemt spart dokking og flere inntektsdager, men behold påkrevd vedlikehold og langsiktig erstatningsbehov. Én unngått dokking er ikke en evig årlig besparelse.

### Fartøy nummer 7

Vis seksfartøysmodellen separat fra tilleggsfartøyet. Skill mellom ingen avtale/forsinkelse, charter og kjøp. Ta med kontraktsstart, mobilisering/oppgradering, charterbetalinger, OPEX, skatt, kjøpesum, finansiering og Paratus' andel av kapitalbehovet.

Et akseptert bud eller en MOU gjør ikke hele prosjektet sikkert. Tillegg i Base må være eksplisitt betinget, og modellen skal også vise Base uten fartøyet. Unngå både sannsynlighetsvekting inne i kontantstrømmen og en ekstra identisk sannsynlighetsreduksjon uten forklaring.

Test prosjektets kontantstrøm og prosjekt-IRR, restverdi og risiko. Enkel `incremental FCF / kjøpesum` er en screening, ikke tilstrekkelig investeringsbeslutning. Skill ubelånt prosjektavkastning fra egenkapitalavkastning, og anvend IAFs kapitaldisiplin med sammenlignbare mål.

## 6. Fra Seagems til Paratus-aksjonæren

Bruk to separate nivåer; eierandel skal anvendes nøyaktig én gang.

```text
Seagems, 100 %:
Inntekter − driftskostnader − charter − administrasjon = EBITDA
EBITDA − kontante renter − skatt − Δarbeidskapital
       − vedlikehold/erstatning − vekstcapex = kontantstrøm før finansiering
+ nye lån − avdrag − påkrevd cashbuffer = mulig JV-distribusjon

Paratus holding:
Mottatt JV-distribusjon til Paratus
+ mottatte renter på selgerkreditt + andre kontantinntekter
− holdingkostnader − holdingrenter − holdingskatt
= løpende holdingkontantstrøm
```

Vis også økonomisk FCFE som tilhører Paratus og forskjellen fra faktisk mottatt JV-distribusjon. JV-lånevilkår, kapitalbehov, beslutningsrett og cashbuffer kan begrense overføringen.

Bygg separat holding-cashbro:

```text
Sluttcash = startcash + løpende holdingkontantstrøm
          + innbetalt hovedstol på selgerkreditt
          + lån/emisjoner/andre kapitalprovenyer
          − avdrag/innløsningspremier − egenkapitalinnskudd/investeringer
          − utbytte − tilbakekjøp
Sluttgjeld = startgjeld + nye lån − nedbetalt hovedstol
```

Hovedstol fra selgerkreditten er kapitalfrigjøring, ikke tilbakevendende FCF. Definer FCF/share før bruk og vis finansierings-/investeringsposter separat. Utbytter må ha dekning på holdingnivå etter nødvendige investeringer, avdrag og likviditetsbuffer. Ikke oppretthold samme utbytte i Bear dersom det krever udokumentert finansiering.

Skill rapportert netto gjeld fra gjennomskuet økonomisk gjeld. Ikke trekk både JV-gjeld i JV-egenkapitalverdien og på nytt i holdingverdien.

## 7. Selgerkreditt og kapitalstruktur

Modellér faktisk løpetid, renteperioder og mottatte betalinger. Kapitalisert rente er ikke mottatt cash. Etter tilbakebetaling opphører renteinntekten; etter gjeldsinnløsning opphører rentekostnaden på den innløste hovedstolen.

```text
Netto endring i årlig finansieringskontantstrøm ved innfrielse
= spart gjeldsrente − bortfalt selgerkredittrente
  + rente på eventuell gjenværende cash
  − relevante skatter/gebyrer
```

Rentebesparelse alene er ikke netto FCF-vekst. Innløsning med eksisterende cash reduserer gjeld og cash samtidig; gebyrer og premier reduserer verdi. Ikke tell samme selgerkreditt som både fortsatt fordring, utbetalt kapital og nedbetalt gjeld.

Bruk scenarioer for rettidig betaling, forsinkelse og tap/recovery med dokumentert sikkerhet og realisasjonstid. Ikke behandle nominell fordring som risikofri cash. Bruk enten scenariobaserte betalinger eller en konsistent separat nåverdi; unngå å legge samme kredittap inn flere ganger.

Vis likviditet frem til låneforfall og vurder refinansiering. Test tilbakekjøp, gjeldsreduksjon, investering og ekstrautbytte på samme kapitalgrunnlag.

## 8. Normalisering og IAF

Velg primært normalisert kontantinntjening per aksje, med NAV/share som kontroll. Angi start-/sluttverdi, aksjeantall, horisont og sammenlignbar normalisering:

```text
g = (X_slutt / X_start)^(1/N) − 1
d_t = D_t / P_0
```

Bruk samme normaliserte markedsøkonomi ved begge endepunkter. Skill rateøkning og midlertidig utnyttelsesbedring fra varig kapasitet/effektivitet. Finansiering og tilbakeholdt cash må være konsistente med den normaliserte banen.

Lag en bro mellom drift, syklus, EDD, finansiering, fartøy nummer 7 og aksjeantall. Ikke viderefør originalens g = 5–7 % uten beregning. Vanlig CAGR brukes ikke ved null/negativ startverdi. Hold multippeløkning utenfor g.

Vis årlig utbytte og definert normalisert d. Annualisert siste kvartalsutbytte er kun en referanse. D+G og P/E-heuristikken er kontroller; investor-IRR er sluttkontrollen. IAFs 12 % investoravkastningskrav og en terminal FCF-yield er forskjellige størrelser.

## 9. Verdsettelse og avkastning

Bygg tre sammenhengende scenarioer for 3–5 år, med årlige tall for rater, gap, kostnader, capex, JV-distribusjon, selgerkreditt, gjeld/cash, aksjer, FCFE og utbytte. Oppgi valuta og FX-bane.

Bruk konsistent verdsettelse:

- **Sum av delene:** Paratus-andel av Seagems' egenkapitalverdi + nåverdi av selgerkreditt + holdingcash − holdinggjeld − øvrige seniorposter og relevante holdingkostnader.
- **FCFE/terminal yield:** Bare bærekraftig egenkapitalkontantstrøm etter nødvendig vedlikehold/erstatning og riktig finansieringsbelastning. Midlertidige selgerkredittrenter kan ikke kapitaliseres evig.
- **Gjennomskuet EV:** Avstem kontantstrømmer og gjeld på samme nivå. Kapitalisert egenkapitalverdi skal ikke reduseres med samme gjeld på nytt.

Forklar restlevetid, kontraktsvarighet og behovet for reinvestering etter prognoseperioden. Dersom overskuddscash prises separat, fjern tilhørende renteinntekt fra kapitalisert resultat. Sjekk at utbetalt utbytte ikke fortsatt ligger i terminalcash.

Beregn investor-IRR/XIRR med kjøpsdato, fremtidige utbyttedatoer og exitdato. Allerede utbetalte utbytter inngår ikke. Oppgi før/etter skatt og kostnader. Vis per scenario IRR mot k og sannsynlighetsvektet nåverdi ved k. Skill vektet gjennomsnitt av IRR-er fra IRR på vektede kontantstrømmer.

Vis terminalverdiens andel av nåverdien. Sensitiviteter skal minst dekke nye PLSV-rater, kontraktsgap, teknisk nedetid, OPEX, USD/NOK, selgerkreditt, refinansiering og fartøy nummer 7. Sensitivitetsverdier er stresstester, ikke observerte prognoser.

## 10. Konklusjon og kontroll før lagring

Konklusjonen skal svare på hva inngangsprisen forutsetter, om modellert avkastning overstiger k, og hvilke hendelser som kan bekrefte eller svekke tesen. Følg særlig Jade/fornyelser, definitive avtaler for nytt fartøy, faktisk JV-cash, selgerkredittbetalinger og finansieringsbehov.

Kontroller:

- [ ] Alle økonomiske tall er merket som 100 % JV, Paratus-andel eller holding.
- [ ] Kontraktsdager og teknisk nedetid avstemmes uten dobbelt fradrag.
- [ ] Faktiske kontrakter og betingede avtaler er atskilt.
- [ ] Skatt, renter, capex og aksjeantall avstemmes; drift uten inntekt har realistiske kostnader.
- [ ] Selgerkredittrenter opphører ved innfrielse, og hovedstol teller bare én gang.
- [ ] Utbytte, gjeldsreduksjon og vekstinvesteringer har samlet finansiering.
- [ ] g er normalisert og beregnet, ikke en ubegrunnet videreføring.
- [ ] Scenarioer har samme dato-/valutagrunnlag og vektene summerer til 100 %.
- [ ] Nåverdi ved beregnet IRR stemmer med inngangsbeløpet; terminalverdi og gjeld teller én gang.
- [ ] Endringstabellen skiller nye fakta, endrede anslag og retting av feil.
- [ ] Kilder og lokale lenker fungerer; manglende data og modellbegrensninger er synlige.

## 11. Resultatformat og lagring

Lagre hver fullført analyse som:

```text
C:\GitWork\hsaether\Chatgpt\Finance\Doc\Paratus - YYYY-MM-DD.md
```

Datoen er analyzedatoen, ikke eksportdatoen for et eldre resultat. Behold historikk. En ny analyse samme dag får ` - 02`, deretter ` - 03` før filendelsen. En uttrykkelig retting kan gjøres i eksisterende fil med endringslogg. Ingen konkurrerende udatert analyse er nødvendig.

Resultatet skal inneholde:

1. Status, analyzedato/datagrense, kursdato, horisont, IAF-versjon og k.
2. Konklusjon, hva som er priset inn og endringer fra forrige analyse.
3. Inputregister med datoer på Oil/Rig/Supply BBB.
4. Selskapsfakta, fartøy-/kontraktsregister og Petrobras/PLSV-marked.
5. Årlig BBB-modell og bro fra JV til holding og per aksje.
6. Selgerkreditt, kapitalallokering, finansiering og fartøy nummer 7.
7. Normalisert g, utbytte, verdsettelse, IRR og sensitiviteter.
8. Risiko, revurderingstriggere, kildeoversikt, datamangler og endringslogg.

Lenk til denne prosedyren. Les filen tilbake og kontroller eksistens, tekst, datoer og lenker før leveranse. Oppdater «siste lagrede analyse» øverst først etter vellykket lagring.

## 12. Egen vurdering av originalprosedyren

Originalen har et godt utgangspunkt: fartøybasert økonomi, Petrobras' faktiske behov og vekt på kapitalstruktur. Følgende presiseringer innføres:

| Tema | Vurdering og endring |
|---|---|
| Input | Beholder originalens Supply BBB som direkte markedsinput; Oil og Rig brukes som bakgrunn. |
| JV og holding | Skiller økonomisk andel fra faktisk utdelingskapasitet og avstemmer gjeld på hvert nivå. |
| Selgerkreditt | Krever netto rentebro, tidsbestemte betalinger og kontroll mot dobbelttelling av hovedstol. |
| Vekst | Erstatter skjønnsmessig g med IAF v1.1-normalisering og dokumentert vekstbro. |
| Fartøy nummer 7 | Krever seksfartøysreferanse, betinget tillegg og sammenligning av charter/kjøp med finansiering. |
| Utbytte | Kontrollerer samlet dekning etter investeringer og avdrag, også i Bear. |
| Avkastning | Innfører eksplisitt årlig investor-IRR og vektet nåverdi; fremtidig kursverdi er ikke dagens verdi. |
| Sporbarhet | Innfører daterte filer, kilde-/inputregister, kontrollpunkter og endringslogg. |

## 13. Endringslogg

| Versjon | Dato | Endring |
|---|---|---|
| 1.0 | 2026-09-29 | Systematisert originaltrådens prosedyre og vurdert den mot IAF v1.1. Innført kontrollene ovenfor og datert historisk resultat i Doc. |

