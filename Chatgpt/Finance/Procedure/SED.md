# SED – analyse- og oppdateringsprosedyre

**Versjon:** 1.0  
**Opprettet og vurdert:** 29. september 2026  
**Selskap:** SED Energy Holdings / Energy Holdings, omtalt som ENH i originaltråden. Verifiser gjeldende navn, ticker og selskapsstruktur ved kjøring.  
**Prosedyrefil:** `C:\GitWork\hsaether\Chatgpt\Finance\Procedure\SED.md`  
**Resultatmappe:** `C:\GitWork\hsaether\Chatgpt\Finance\Doc`  
**Historisk startgrunnlag:** [SED – 22. september 2026](../Doc/SED%20-%202026-09-22.md). Dette er historisk eksport, ikke en fullført analyse etter denne reviderte prosedyren.  
**Kilde:** [SED Analyse](https://chatgpt.com/c/6a998b8f-a028-83eb-8186-5e2805a5f515).

## 1. Formål og opphav

Oppdater SED fra kontrakter og marked til økonomi per aksje, finansiering, utbetalinger og forventet investoravkastning. Analysen skal vise hva som er endret siden sist, hvilken risiko aksjekursen forutsetter, og hva som kan avkrefte investeringshypotesen.

Prosedyren er sammenstilt fra rigg-for-rigg-modellen, korreksjonen til felles FCF-yield, Ventura-vurderingen 11. september, analysehierarkiet 19. september og kontraktsoppdateringen 22. september 2026. Originaltråden inneholder en arbeidsmåte og senere presiseringer, ikke én samlet ferdig prosedyre. Dokumentet nedenfor systematiserer disse og legger til kontrollene beskrevet i punkt 3.

Opprettelsen er en metodegjennomgang og historisk eksport. Det er ikke gjennomført ny selskaps- eller markedsresearch 29. september. Historiske rater, selskapsnavn, transaksjonsvilkår og verdianslag er ikke permanente prosedyrepremisser.

## 2. Obligatorisk input og rangordning

| Input | Rolle og bruk |
|---|---|
| [Investment Analysis Framework – IAF](../Investment_Analysis_Framework_IAF.md) | Overordnet metode. Les ved hver kjøring og oppgi versjon. Ved opprettelsen: v1.1, 28. september 2026. |
| Siste daterte, fullførte `Doc/Rig Market BBB - ÅÅÅÅ-MM-DD.md` | Primær markedsanalyse: riggklasse, region, dagrate, tilbud, aktivitet og kontraktsrisiko. |
| Siste daterte, fullførte `Doc/Oil Market BBB - ÅÅÅÅ-MM-DD.md` | Makrobakgrunn: flerårig offshore-capex, prosjektøkonomi og geopolitikk. |
| Siste daterte SED-analyse i Doc | Modell, antakelser, endringslogg og åpne kontrollpunkter. |
| Rapporter, flåtestatus og børsmeldinger | Kilde til faktiske selskapsdata. Nyere, verifiserte opplysninger går foran historiske chatanslag. |

[Prosedyren for Rig Market BBB](../Module/Rig%20Market%20BBB.md) og [prosedyren for Oil Market BBB](../Module/Oil%20Market%20BBB.md) beskriver hvordan markedsgrunnlaget oppdateres. Selve markedsinputen hentes fra analyseresultatene i Doc.

Ved opprettelsen er de nyeste lokale markedsfilene [Rig Market BBB – 26. september](../Doc/Rig%20Market%20BBB%20-%202026-09-26.md) og [Oil Market BBB – 26. september](../Doc/Oil%20Market%20BBB%20-%202026-09-26.md). Disse er historiske eksporter og er nyere enn SED-startgrunnlaget. De skal vurderes ved neste oppdatering, ikke føres inn som om de var brukt 22. september.

IAF styrer metodekonflikter. Bruk normalt k = 12 %, 3–5 års horisont og Bear/Base/Bull 25/50/25. Forklar avvik; summer vekter til 100 %. Hold IAF stabil og lagre nye selskapsdata i analysen.

## 3. Vurdering og forbedringer av originalprosedyren

| Tema | Vurdering og vedtatt forbedring |
|---|---|
| Rigg-for-rigg og kontraktsvegg | Beholdes. Beregn dager etter konkrete datoer; ikke bruk flåteutnyttelse som skjuler enkeltstående kontraktsgap. |
| Marked kontra selskap | Beholdes. Et tapt anbud kan svekke SED uten å svekke samlet riggetterspørsel. Høy aktivitet betyr ikke automatisk høye rater. |
| Felles verdsettelsesyield | Behold originaltrådens korreksjon: samme sentrale yield i hovedscenarioene; alternative yields vises separat. Historiske 13 % er et utgangspunkt som må begrunnes på nytt, ikke IAFs k. |
| FCF-definisjon | Krev full bro fra EBITDA til kontanter etter renter, skatt, investeringer, leasing og finansiering. EBITDA-tap og FCF-tap er ulike størrelser. |
| Ventura | Modeller gjennomføring, forsinkelse og bortfall separat. En LOI er ikke fullført eierskap. Kontroller utvanning, overtakelsesdato og netto gjeld samtidig. |
| D+G | Originalen viste nødvendig g, men dokumenterte ikke at veksten ville oppstå. Beregn normalisert økonomisk vekst per aksje; vis «ikke dokumentert» hvis det mangler grunnlag. |
| Verdi og tid | Normalisert FCF/yield er en betinget verdsettelse på angitt tidspunkt. Beregn nåverdi og investor-IRR med faktiske mellomliggende utbetalinger. |
| Idle versus lav kontraktsrate | Sammenlign nåverdien av kontantstrømmer, ikke bare brutto omsetning. Ta med standbykostnader, oppstart, risiko og likviditetsbehov. |
| Kildekontroll | Originalen overså først vesentlig ny informasjon. Kontroller børsmeldinger og nyhetskilder samme dag før «ingen nye meldinger» brukes. Skill meglerreferat fra selskapsmelding. |
| Etterprøvbarhet | Dokumenter kilder, input, formler, kontrollsummer og åpne hull; bevar daterte analyser. |

## 4. Hva «Oppdater» betyr

**«Oppdater» i SED-sammenheng**, eller **«Oppdater SED»**, utløser følgende:

1. Les denne prosedyren, gjeldende IAF, siste SED-analyse og de nyeste relevante markedsanalysene.
2. Registrer analyzedato, Europe/Oslo, datagrense, inputversjoner og prognoseår.
3. Hent nye selskapsopplysninger og kontroller alle vesentlige antakelser som videreføres.
4. Oppdater segmentmodellen, kontrakter, investeringer, finansiering og aksjeantall.
5. Beregn Bear/Base/Bull, normalisert g, verdsettelse og investor-IRR.
6. Sammenlign med forrige analyse og dokumenter endret eller uendret konklusjon.
7. Lagre et nytt datert Markdown-dokument i Doc, les det tilbake og kontroller innhold og lenker.

Dette er en instruksjonsstyrt arbeidsflyt. Dokumentet oppretter eller endrer ingen automatisk vakt.

En SED-oppdatering endrer ikke automatisk markedsmodulene. Dersom input er foreldet eller motsagt av nyere hendelser, oppgi begrensningen og vis eventuell selskapsspesifikk sensitivitet. Ved bestilling av hele kjeden kjøres **Oil Market BBB → Rig Market BBB → SED** etter de respektive prosedyrene. Ikke lag en konkurrerende global markedsbaseline inne i SED.

## 5. Kilder og kontroll av nye hendelser

Kontroller selskapets offisielle meldingsfeed, NewsWeb/Euronext og eventuell MFN-publisering, deretter siste kvartalsrapport, presentasjon, flåtestatus, årsrapport og finansieringsdokumenter. For transaksjoner brukes også motpartens dokumenter; for kontrakter brukes operatørens tildelinger når tilgjengelige. Megleranslag og bransjenyheter er supplerende kilder.

Registrer direkte lenke, publiseringsdato, observasjonsperiode, lest dato, valuta/enhet og klassifisering: **rapportert fakta / guiding / eksternt estimat / eget anslag**. Ikke presenter selskapets illustrative normaldriftsscenario som guiding eller uavhengig Bear.

Oppgi hvilke kanaler som faktisk er kontrollert. Manglende tilgang eller manglende offentlig dagrate merkes eksplisitt; fravær av et søketreff beviser ikke fravær av nyheter. Verifiser aksjekurs, tidspunkt, ex-utbytte og valuta før beregning.

## 6. Fastsett selskapsomfang før modellering

Vis separat:

- **Standalone:** Energy Drilling, SeaBird og konsern, med faktisk aksjebase og gjeld.
- **Pro forma:** tillegg fra Ventura dersom transaksjonen gjennomføres på oppgitte vilkår.
- **Rapportert overgangsår:** bare økonomien etter faktisk eller scenarioantatt overtakelse konsolideres.

Kontroller juridisk status, bytteforhold, nye aksjer, opsjoner, egne aksjer, eierandeler, transaksjonskostnader, oppgjørsjusteringer og betingelser. Lag aksjebro fra gammel til ny aksjebase. Bruk tidsvektet aksjetall for EPS der relevant og aksjene som er berettiget på utbetalingsdato for distribusjoner. Terminalverdi deles på fullt utvannet relevant aksjetall.

Inkluder gjennomføring, forsinkelse og bortfall som transaksjonsgrener i hvert markedsscenario når risikoen er vesentlig. Dokumenter betingede sannsynligheter; samlet sannsynlighet er markedsvekt ganger grenvekt. Hvis sannsynligheter ikke kan underbygges, vis betingede verdier uten å konstruere én presis risikovektet verdi. Ikke legg på en ekstra vilkårlig transaksjonsrabatt for samme risiko.

## 7. Flåte- og kontraktsmodell

Opprett én rad per rigg/fartøy og én tidslinje per prognoseår, med minst månedlig oppløsning rundt kontraktskifter.

| Påkrevd felt | Behandling |
|---|---|
| Navn, riggtype, region og eierandel | Skill eid, innleid og bare administrert enhet. |
| Kunde, rate og valuta | Skill kontraktsrate, cash-rate, engangsvederlag og refusjoner. |
| Start, fast utløp og opsjoner | Opsjoner føres separat fra fast backlog. |
| Teknisk tilgjengelighet og betalingsdager | Skill mobilisering, verftsopphold, idle, off-hire og arbeid. |
| Kostnader | Aktiv opex, idle/stacking, charter/leasing og segmentoverhead. |
| Investeringer | SPS/vedlikehold, oppgraderinger, mobilisering, reaktivering og vekst. |
| Neste kontrakt | Tenderstatus, forventet tildeling, start, rate, sikkerhet og kilde. |

Historiske kontrollnavn fra originaltråden er EDrill-1, EDrill-2, T-15, T-16, ED Vencedor og GHTH. For Ventura: Victoria, Carolina og Catarina samt eventuell management-inntekt fra Zonda. Dette er en sjekkliste som må verifiseres mot faktisk flåte, ikke en låst eiendelsover­sikt.

Særskilte kontroller:

- EDrill-1/T-15: PTTEP-utfall, alternativt arbeid, kontraktsgap og konkurranse fra jackups.
- T-16: CPOC, videre kontrakt, timing og samlet konsentrasjon av ledige rigger.
- Victoria/Carolina: teknisk ferdigstillelse, aksept, mobilisering og kontraktsstart.
- Catarina: kontraktsdekning og økonomien i videre drift.
- GHTH: charterkostnad, varighet og tilbakelevering. Ikke bruk økonomien til en eid rigg.
- Zonda eller andre administrerte enheter: inntektsfør bare tilhørende honorar/økonomisk eierandel.
- SeaBird: modeller separat med fartøysdager, kontrakter og kostnader; riggmarkedets rater skal ikke brukes på seismikk.

Langsiktige fastpriskontrakter repriser ikke automatisk når spotmarkedet stiger. Backlog er framtidig omsetning, ikke kontanter eller FCF.

## 8. Fra marked til selskapsøkonomi

Importer relevante regioner og riggklasser fra Rig Market BBB. Tender-assist skal ha egne rate- og kontraktsforutsetninger; ikke overfør globale premium-jackup- eller Tier-1-drillship-rater direkte.

Vis kjeden:

**Olje/prosjektøkonomi → operatørens investeringsplan → relevant etterspørsel og konkurranse → SED-kontrakt → betalingsdager og margin.**

Skill markedsaktivitet, teknisk tilgjengelighet, faktisk kontraktsdekning og evne til å oppnå høyere rate. Et tenderprospekt er ikke en tildeling. Kostnadsfordeler garanterer ikke kontraktsseier.

Andre selskapers presentasjoner kan brukes som kilde til relevante markedsdata, men ingen egen selskaps­sammenligning skal lages uten bestilling. Dette bevarer originaltrådens avgrensning ved bruk av Dolphin-materiale.

## 9. Regnskaps-, kontantstrøm- og finansieringsbro

Kalibrer modellen mot siste rapporterte kvartal og halvår. Vis avvik; ikke annualiser et toppkvartal som normalisert drift.

For hver kontraktsperiode beregnes inntekt som rate × betalingsdager, korrigert for eierandel, refusjoner og regnskapsføring. Kontroller at dagene summerer til kalenderen uten dobbelttelling. Beregn aktiv opex og idle-kostnader med ulike satser.

Vis minst følgende årlige bro:

1. Segmentinntekter minus segmentkostnader og konsernkostnader = EBITDA.
2. EBITDA minus avskrivninger, netto finans og regnskapsskatt = resultat til aksjonærene; avstem EPS.
3. EBITDA minus kontantskatt, kontant­renter, arbeidskapitaløkning og nødvendige vedlikeholds-/erstatningsinvesteringer = kontantinntjening etter vedlikehold.
4. Trekk fra vekstinvesteringer, øvrige investeringer og engangskostnader for å vise kontantstrøm etter alle investeringer.
5. Vis leasingbetalinger konsistent med EBITDA-/kontantstrømdefinisjonen, samt låneopptak og avdrag separat.
6. Avstem kontanter, gjeld, bundne midler, utbetalinger, tilbakekjøp og emisjoner.

Definer eksplisitt hvilken størrelse som kalles FCF og brukes per aksje. Renter og leasing skal verken utelates eller trekkes to ganger. Skill FCF før netto lånebevegelser fra FCFE etter netto lånebevegelser og fra faktisk tilgjengelig utbetalingskapasitet.

Utbytte begrenses av likviditet, obligatoriske avdrag, covenants, nødvendig reserve og investeringsplan. Payout er en modellantakelse med mindre selskapet har gitt dokumentert guiding. Avdragsfri finansiering endrer timing og restgjeld; det skaper ikke bedre drift.

Vis gjeldsforfall, rente, refinansieringsbehov, covenant-margin og minimumskontanter per scenario. Eventuelt finansieringsgap utløser en eksplisitt løsning: mindre utbytte, utsatt investering, ny gjeld, eiendelssalg eller emisjon med utvanning.

## 10. Normalisering og økonomisk vekst

Bruk normalisert kontantinntjening per aksje etter nødvendig vedlikehold og erstatningsbehov som hovedmål, støttet av NAV og normalisert EPS. Oppgi valgt mål X, startverdi, sluttverdi og normaliserte rater, utnyttelse, kostnader og finansiering.

Beregn **g = (X_N / X_0)^(1/N) − 1** med sammenlignbare endepunkter. Ved null/negative verdier brukes årlig bane og absolutt endring, ikke vanlig CAGR.

Skill:

- midlertidig innhenting fra idle til arbeid;
- sykliske rateendringer;
- varig kapasitets- eller effektivitetsendring;
- transaksjon, finansiering og aksjeantall.

Historiske 2027 som overgangsår og 2028–2029 som normaliseringsår er hypoteser som skal testes. Rull prognoseårene framover ved senere kjøringer.

Test Ventura per aksje med samme kontantstrømdefinisjon på begge sider:

**(SED-FCF + netto bidrag fra Ventura og synergier) / (gamle aksjer + nye aksjer) > SED-FCF / gamle aksjer.**

Netto bidrag inkluderer ekstra konsernkostnader, renter, skatt og nødvendige investeringer. En engangsøkning ved oppkjøp skal ikke videreføres som evig vekst. Kontroller kapitalbehov og avkastning på investert kapital etter IAF.

## 11. BBB, verdsettelse og investoravkastning

Bygg normalt tre årlige baner over 3–5 år. Vis per scenario inntekter, EBITDA, EPS, capex, definert FCF, FCF/aksje, utbetaling/aksje, kontanter, gjeld, aksjetall og normalisert g. Bear må omfatte reelle drifts- og finansieringsproblemer; «lav rate med nesten full drift» er utilstrekkelig.

Vis:

- P/E på meningsfull, normalisert EPS og egen merking av rapportert P/E.
- FCF-yield med definert egenkapitalrelevant kontantstrøm.
- Utbytteyield d_t = D_t / P_0 og begrunnet normalisert d.
- D+G mot k. Beregn g; ikke sett g lik det som kreves for å bestå.
- Relevant NAV og/eller EV-kryssjekk.

For kontinuitet kan **13 % felles normalisert FCF-yield** vises som historisk referanse, med separat 11/13/15 %-sensitivitet. Begrunn valgt sentral yield og forutsetningene om investeringer, levetid og finansiering. Den er ikke det samme som k = 12 %, og FCF/yield alene er ikke en komplett nåverdimodell.

Angi om FCF/yield-verdien gjelder i dag eller ved slutten av prognosen. Ved terminalverdi diskonteres både denne og mellomliggende investorutbetalinger. Velg en konsistent metode: egenkapitalverdi fra egenkapitalstrøm eller EV minus terminal netto gjeld og andre krav. Ikke trekk gjeld to ganger eller legg til kontanter som allerede ligger i verdien.

Beregn investor-IRR fra kjøpspris, daterte utbetalinger og exitverdi, inklusive eventuelle nye kapitalinnskudd. Sammenlign hvert scenario med k. Vis gjerne sannsynlighetsvektet nåverdi ved k; et veid gjennomsnitt av IRR skal merkes som en beskrivende statistikk.

Forklar forskjellen mellom D+G og IRR med timing, syklus, utbetalingsprofil, finansiering og endret verdsettelse. Ikke erklær «IAF bestått» uten dokumentert g og sluttkontroll med IRR/nåverdi.

## 12. Sensitiviteter og beslutningspunkter

Test minst kontraktsgap, nye rater, idle-kostnader, vedlikeholds-/oppstartscapex, renter/refinansiering, valuta, payout og aksjeutvanning. For Ventura vis forsinkelse og bortfall i tillegg til normal gjennomføring.

Prioriter triggerregisteret med **hendelse → kilde/status → berørt modellvariabel → konsekvens per aksje → neste kontroll**. Originaltrådens viktigste triggere var T-16, nytt arbeid for EDrill-1/T-15, vinnerrater i Thailand, Ventura-avtalen, riggoppstart og refinansiering. Oppdater listen etter faktisk utvikling.

Ved vurdering av å vente på en bedre kontrakt sammenlignes diskonterte netto kontantstrømmer og sannsynlighet for kontrakt, inklusive standby, mobilisering og finansieringsbuffer. En brutto omsetningsforskjell beviser ikke at venting er lønnsom.

## 13. Fast format for analysedokumentet

1. Metadata: status, analyzedato/datagrense, kurs/valuta, horisont, IAF-versjon og lenker til faktisk brukte input.
2. Kort konklusjon og hva som er priset inn, med viktigste betingelser.
3. Ny informasjon siden forrige analyse og kildeoversikt.
4. Selskapsstruktur, transaksjonsstatus og aksjebro.
5. Flåte-/kontraktstabell, fast dekning, opsjoner og gap.
6. Markedsforutsetninger og selskapsspesifikke avvik.
7. Regnskap, kontantstrømbro, finansiering og kapitalallokering.
8. Normalisering, vekstbro og kapitalavkastning.
9. Årlige Bear/Base/Bull-tabeller, standalone/pro forma og transaksjonsgrener.
10. P/E, FCF-yield, utbytte, D+G, terminalverdi, investor-IRR og nåverdi ved k.
11. Sensitiviteter, risiko, triggerregister og datamangler.
12. Endringslogg med gammel verdi, ny verdi, årsak og kilde; kvalitetskontroll.

Sentrale beregninger skal kunne gjenskapes fra tabeller og formler i dokumentet eller et eksplisitt lenket modellvedlegg. Manglende essensielle data medfører status **foreløpig**, ikke oppdiktede tall eller en ubetinget investeringskonklusjon.

## 14. Lagring og kvalitetskontroll

- Lagre resultat som `C:\GitWork\hsaether\Chatgpt\Finance\Doc\SED - ÅÅÅÅ-MM-DD.md`.
- Bruk faktisk analyzedato. Ved flere kjøringer samme dag: `SED - ÅÅÅÅ-MM-DD - TTMM.md`, lokal tid Europe/Oslo, eventuelt sekunder.
- Bevar tidligere analyser. Historisk eksport beholder original analyzedato og oppgir eksportdato separat.
- Velg siste fullførte analyse etter metadata og analyzedato, ikke filens endringstid. Les også nyere foreløpige notater for vesentlige hendelser. Historisk eksport er startgrunnlag inntil en ny fullført analyse foreligger.
- Oppdater lenken til siste fullførte analyse i prosedyren etter vellykket lagring. Et utkast skal ikke erstatte denne.
- «Oppdater» oppdaterer analysen; metodeendringer i prosedyren versjoneres med begrunnelse.

Før ferdigstilling kontrolleres:

- [ ] Kurs, dato, valuta, enheter, inputversjoner og datadekning er eksplisitte.
- [ ] Rigg-/fartøysdager summerer; fast kontrakt, opsjon og egne anslag er skilt.
- [ ] Segmenter og eierandeler summerer til konsernet uten dobbelttelling.
- [ ] Standalone/pro forma, aksjetall og overtakelsestidspunkt er avstemt.
- [ ] EBITDA, EPS, kontantstrøm, investeringer, gjeld og likviditet henger sammen.
- [ ] Utbytte og tilbakekjøp er finansiert og redusert fra balansen.
- [ ] Normalisert g er beregnet separat fra syklisk innhenting og reprising.
- [ ] Scenario-/grenvekter summerer til 100 % og risiko er ikke straffet flere ganger.
- [ ] Terminalverdi, mellomliggende utbetalinger, IRR og nåverdi er konsistente.
- [ ] Forskjellen mellom historiske tall, verifiserte fakta og anslag er tydelig.
- [ ] Filen finnes, er lest tilbake og har fungerende lokale lenker og korrekte norske tegn.

## 15. Endringslogg

| Versjon | Dato | Endring |
|---|---|---|
| 1.0 | 2026-09-29 | Sammenstilt SED Analyse og senere korreksjoner. Lagt til full kontantstrøm-/finansieringsbro, transaksjonsgrener, normalisert g, investor-IRR, tidfestet verdi, kildekontroll og datert dokumentflyt. IAF v1.1 er beholdt uendret. |

