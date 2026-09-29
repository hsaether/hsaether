# CAPT – oppdateringsprosedyre

**Dokumenttype:** gjenbrukbar prosedyre for selskapsanalysen av Capital Tankers Corp.  
**Versjon:** 1.0.  
**Opprettet:** 29. september 2026.  
**Prosedyrefil:** `C:\GitWork\hsaether\Chatgpt\Finance\Procedure\Capt.md`.  
**Resultatmappe:** `C:\GitWork\hsaether\Chatgpt\Finance\Doc`.  
**Siste lagrede analyse ved opprettelsen:** [CAPT – 2026-09-29](../Doc/CAPT%20-%202026-09-29.md).

## 1. Formål og styrende dokumenter

Oppdater CAPT som en finansiert selskapsmodell: fra marked og flåte til kontantstrøm per aksje, kapitalallokering, verdsettelse og investoravkastning. Vis både endringen fra forrige analyse og hvilke forhold som fortsatt er usikre.

| Dokument | Rolle |
| --- | --- |
| [Investment Analysis Framework – IAF](../Investment_Analysis_Framework_IAF.md) | Overordnet prosedyre og metodiske krav. |
| Siste daterte `Doc/Oil Market BBB - YYYY-MM-DD.md` | Bakgrunn for oljevolumer, handelsstrømmer, lager og geopolitikk. |
| Siste daterte `Doc/Oil Shipping BBB - YYYY-MM-DD.md` | Direkte markedsinput: segmentrater og Bear/Base/Bull-scenarioer. |
| Siste daterte `Doc/CAPT - YYYY-MM-DD.md` | Forrige selskapsmodell, antakelser, konklusjon og åpne kontrollpunkter. |
| [CAPT Analyse](https://chatgpt.com/c/6a9878fd-d2b0-83ed-8178-18e14b95c7f9) | Historiske selskapsopplysninger, brukerføringer og tidligere modellarbeid. Nyere regnskap og børsmeldinger styrer faktiske selskapsdata. |

Filene i `Module` beskriver hvordan markedsanalysene oppdateres. CAPT importerer selve **analyseresultatene i Doc**, ikke modulprosedyrene som om de var markedsdata.

Ved opprettelsen er IAF v1.1 styrende, med normalt `k = 12 %` og scenarioer 25/50/25. Les gjeldende IAF ved hver oppdatering. Hold IAF stabil; nye selskaps- eller markedstall skal inn i analysen. Endring av grunnprinsippene krever en uttrykkelig beslutning.

## 2. Instruksjonen «Oppdater CAPT»

«Oppdater CAPT» betyr å lese denne prosedyren, gjennomføre kontrollene nedenfor, beregne modellen på nytt og lagre et nytt datert analyseresultat.

1. Les gjeldende IAF, siste CAPT-analyse og siste daterte olje- og shippinganalyser.
2. Registrer analyzedato, datagrense, kildeversjoner, aksjekurs med tidspunkt, valuta og prognoseår.
3. Hent nye børsmeldinger og rapporterte selskapsdata siden forrige CAPT-analyse.
4. Oppdater flåte, inntektsdager, kapitalbehov, finansiering og aksjeantall.
5. Importer shippingratene og beregn alle tre scenarioer, normalisert vekst og investoravkastning.
6. Sammenlign resultatene med forrige analyse og forklar endret vurdering.
7. Lagre, les tilbake og kontroller den nye analysefilen. Oppdater lenken til siste lagrede analyse øverst i denne prosedyren.

En CAPT-oppdatering endrer ikke automatisk markedsanalysene. Hvis en markedsbaseline er foreldet eller nye hendelser motsier den, forklar begrensningen og behovet for ny markedsanalyse. Ved eksplisitt bestilling av hele kjeden oppdateres **Oil Market BBB → Oil Shipping BBB → CAPT** i denne rekkefølgen, etter de respektive prosedyrene.

Manglende data skal merkes. Fullfør det som kan dokumenteres, og klassifiser resultatet som foreløpig dersom manglene hindrer en underbygget verdsettelse. Ikke fyll datamangler med umerkede anslag.

## 3. Kontroller selskapet før modelloppdateringen

### Børsmeldinger og rapporter

Kontroller først [NewsWeb](https://newsweb.oslobors.no/) / [Euronext](https://live.euronext.com/) og selskapets meldinger publisert gjennom [MFN](https://mfn.se/). Bruk deretter [selskapets nettsted](https://www.capitaltankers.com/), kvartalsrapport, presentasjon og eventuell resultatgjennomgang.

Selskapets IR-side eller et søketreff kan være forsinket. Ikke konkluder med «ingen nye meldinger» uten å ha kontrollert tilgjengelig børsmeldingsfeed. Hvis feeden ikke kan leses, oppgi det.

Registrer for hver vesentlig opplysning: kilde, publiseringsdato, perioden opplysningen gjelder og lesedato. Skill mellom rapporterte fakta, selskapsplaner, markedsforutsetninger og egne modellanslag.

### Obligatoriske selskapskontroller

- **Instrument og kurs:** selskap, ticker, børs, valuta, aksjekurs og tidspunkt. En historisk referansekurs må ikke presenteres som dagens kurs.
- **Flåte:** levert, under bygging, solgt og opsjoner, per segment og skip når tilgjengelig.
- **Kommersiell dekning:** kontrakter, bookede rater, dekningsgrad, kontraktsutløp og off-hire.
- **Resultat og kontantstrøm:** TCE, drift, administrasjon, renter, avskrivninger, skatt og arbeidskapital. Avstem justerte tall mot rapporterte tall.
- **Balanse og finansiering:** brutto gjeld, fri/bundet cash, leasing/SLB, avdrag, balloon-forfall, sikkerheter og likviditetskrav.
- **CAPEX:** betalt og gjenstående nybygg-/oppgraderingsbetalinger, med kvartalsvis forfall.
- **Aksjer:** utstedt kapital, egne aksjer, incentivaksjer, RSU-er og annen mulig utvanning. Hold veid EPS-nevner adskilt fra dagens kapital.
- **Kapitalallokering:** vedtatte utbytter, tilbakekjøp, emisjoner, nye skipskjøp og opsjonsbeslutninger.

## 4. Oversett shippinganalysen til CAPT

Importer segmentvise Bear/Base/Bull-rater, år og sannsynligheter fra den valgte shippingbaselinen. Dokumenter eventuelle avvik i CAPT-modellen og begrunnelsen for dem.

Bruk VLCC, Suezmax, Aframax og LR2 separat. Ikke gi LR2 crude-rate uten dokumentert handelsmiks. Ikke legg en ekstra oljepris- eller geopolitisk premie oppå shippingrater som allerede inkluderer effekten.

Skill dagens observerte spotrater fra bookede CAPT-rater og normaliserte fremtidsrater. Store forstyrrelser kan både binde tonnasje og fjerne laster; høy oljepris er ikke automatisk positivt for tanktransport.

Beregn inntektsdager fra leveringsdatoer og kommersiell tilgjengelighet. Ikke gi et nybygg helårsinntjening før det er levert. OPEX påløper også på relevante off-hire-dager. Hvis kildens tilgjengelige dager allerede inkluderer off-hire, skal et ekstra fradrag forklares slik at samme bortfall ikke trekkes to ganger.

## 5. Bygg en sammenhengende finansieringsmodell

Start fra siste rapporterte balanse og modeller perioden frem til analyse-/prognosestart eksplisitt. Erstatt tidligere anslag med faktiske tall når disse blir tilgjengelige.

Vis minst denne årlige broen, og kvartalsvis likviditet når store leveringsbetalinger eller låneforfall gjør det nødvendig:

```text
TCE = rate × inntektsdager
EBITDA = TCE − skipsdrift − administrasjon
Kontantinntjening = EBITDA − kontante nettorenter − skatt
                   − vedlikehold/erstatningsinvesteringer − Δarbeidskapital
FCFE etter planlagt finansiering =
    kontantinntjening − vekstcapex + nye lån − ordinære avdrag
Sluttcash = startcash + FCFE − utbytte − tilbakekjøp
            − ekstra avdrag + eventuelle emisjonsprovenyer
Sluttgjeld = startgjeld + lånetrekk − ordinære avdrag − ekstra avdrag
Netto gjeld = brutto gjeld − relevante kontantmidler
```

Definer hvilke kontantmidler som inngår i netto gjeld. Bundet cash må ikke behandles som fri likviditet. Reiseutgifter ligger allerede i TCE og trekkes ikke en gang til.

Skill **kontantinntjening før vekstcapex** fra faktisk fri kontantstrøm etter investeringer. Skill løpende vedlikehold/dokking fra langsiktig flåteerstatning. Identifiser om avskrivninger er regnskapsførte eller egne økonomiske anslag.

Skill signerte fasiliteter, lån under arbeid og nye finansieringsantakelser. Lånetrekk er ikke inntekter. Utbytte eller ekstra avdrag må ikke skape negativ tilgjengelig likviditet. Hvis finansieringen ikke dekker behovet, vis gapet og nødvendige scenarioendringer; ikke skjul gapet med automatisk låneopptak.

Kontroller eventuell førtidig nedbetaling mot lånevilkår, gebyrer og kommende likviditetsbehov. Modeller renter med en konsistent gjelds- og cashbane. Unngå å trekke aktiverte renter både i kontante rentekostnader og i samme CAPEX-post.

Opsjoner skal være separat fra den faste flåten til utøvelse er bekreftet eller et uttrykkelig finansiert opsjonsscenario er laget. Ta med kjøpesum, tidspunkt, lån, egenkapitalbehov, utvanning og avkastning på investert kapital. En takstrabatt alene beviser ikke verdiskaping.

## 6. Beregn normalisert vekst etter IAF

Velg og definer én primær økonomisk metrikk per aksje, normalt kontantinntjening eller økonomisk verdi/NAV. Vis `X₀`, `Xₙ`, horisont og:

```text
g = (Xₙ / X₀)^(1/N) − 1
```

Hold rate-/verdsettelsesforutsetninger sammenlignbare ved begge endepunkter. For en separat normalisert finansieringsbane må også mellomårene bruke konsistente normaliserte forutsetninger, slik at midlertidige rategevinster ikke skjules i gjeldsreduksjon og strukturell vekst.

Forklar bidragene fra kapasitet, flåtemiks, effektivitet, syklus, kapitalallokering, gjeld og aksjeantall. Skipsprisvekst og multippeløkning er ikke strukturell `g`. En null eller negativ startverdi skal ikke brukes til vanlig CAGR.

Vurder kapitalen som kreves for veksten og den inkrementelle avkastningen. Kontantavkastning før finansiering er ikke identisk med ROIC. Høyere kapasitet finansiert med gjeld eller emisjon er ikke automatisk høyere verdi per aksje.

Skill byggefasen fra moden drift. Ikke viderefør høy byggevekst evig eller legg inn fast langsiktig vekst uten finansierings- og reinvesteringsgrunnlag. Bruk `d + g` og P/E-heuristikken som kontroller; scenarioenes investoravkastning er sluttkontrollen.

## 7. Verdsettelse og investoravkastning

Vis for hvert scenario årlige driftsresultater, kontantinntjening per aksje, faktisk FCFE, utbytte, gjeld og relevant sluttverdi. Bruk en terminalmetode som passer dokumentasjonen.

- **EPS-metode:** oppgi resultatgrunnlag og multipler. En beregnet egenkapitalverdi skal ikke reduseres med netto gjeld en gang til.
- **NAV:** oppgi daterte takster eller merk skipsverdier som antakelser. Trekk fra gjeld og andre seniorposter én gang. NAV er ikke en garantert kursbunn.
- **Kontantstrøm:** kapitalisering krever tilstrekkelig vedlikehold og erstatningsinvesteringer. Før-vekst-CAPEX-inntjening kan ikke uten videre kapitaliseres som evig FCFE.
- **Ulike kapitalstrukturer:** bruk en konsistent EV/egenkapital-bro. Ved separat verdsettelse av overskuddscash tas tilhørende renteinntekt ut av kapitalisert resultat. Ren P/E-sammenligning kan ellers undervurdere cash og feilprise gjeldsnedbetaling.

Beregn investor-IRR med oppgitte betalingsdatoer, kjøpsdato og exitdato; bruk XIRR når periodene er ujevne. Allerede utbetalte utbytter inngår ikke som fremtidige investorinnbetalinger. Angi valuta og behandling av skatt/kostnader.

Rapporter scenario-IRR og sannsynlighetsvektet nåverdi ved `k`. Hvis IRR på vektede kontantstrømmer eller gjennomsnittet av scenario-IRR-er oppgis, navngi metodene og skill dem tydelig. Eventuell 15 %-inngangspris er en supplerende kontroll, ikke en automatisk endring av IAFs krav.

Vis terminalverdiens andel av nåverdien, hovedsensitiviteter og et finansieringsstress når finansieringsrisikoen er vesentlig. Forklar avvik mellom `d + g` og investor-IRR.

## 8. Konklusjon, endringer og kvalitetskontroll

Konklusjonen skal svare på hva som er priset inn, om modellert avkastning overstiger `k`, hva som kan bevise eller svekke tesen, og hvilke datamangler som hindrer en sterkere vurdering.

Sammenlign med forrige analyse i en endringstabell: nye selskapsfakta, marked, prognoser, finansiering, verdi og investoravkastning. Skill et endret markedssyn fra retting av en tidligere beregnings- eller kildefeil.

Kontroller før lagring:

- Flåteantall, leveringsdager, segmentrater og prognoseår henger sammen.
- Kontantstrøm, gjeld, aksjer, utbytter og terminalverdi avstemmes uten dobbelttelling.
- Sannsynlighetene summerer til 100 %, og alle scenarioer er beregnet på samme tids- og valutagrunnlag.
- Nåverdi ved beregnet IRR samsvarer med inngangsprisen.
- Historiske fakta, datofestede planer, egne anslag og manglende opplysninger er tydelig atskilt.
- Finansiering og vedlikehold/erstatning er tilstrekkelig dokumentert, eller begrensningen er synlig i konklusjonen.
- Kildelenker og lokale dokumentlenker virker; interne chatmarkører og uferdige plassholdere er fjernet.

## 9. Resultatformat og datomerking

Lagre hver fullførte oppdatering som:

```text
C:\GitWork\hsaether\Chatgpt\Finance\Doc\CAPT - YYYY-MM-DD.md
```

Datoen er **analysens baseline-/oppdateringsdato**, ikke bare datoen et eldre resultat ble eksportert. Vis i dokumentet både analysedato, selskapsdataenes datagrense og datoene på olje-/shippinggrunnlaget.

Behold eldre daterte analyser. Ved en ny selvstendig oppdatering samme dato brukes `CAPT - YYYY-MM-DD - 02.md`, deretter `- 03.md` osv. En uttrykkelig bestilt retting av eksisterende versjon kan gjøres i samme fil med endringslogg. Ikke opprett en ekstra udatert analyse som kan bli en konkurrerende versjon.

Analysen skal minst inneholde:

1. Datert konklusjon, pris, horisont, IAF-versjon og avkastningskrav.
2. Dokumenthierarki og importerte BBB-forutsetninger.
3. Rapporterte selskapsdata og flåte-/leveringsplan.
4. Modellforutsetninger og full kontantstrøm-/finansieringsbro.
5. Årlige BBB-resultater og normalisert per-aksje-vekst.
6. Kapitalallokering, verdsettelse, investor-IRR og følsomheter.
7. Risiko, observerbare revurderingstriggere og neste relevante rapport.
8. Kilderegister, usikkerheter og endringslogg.

Lenk fra analysen til denne prosedyren. Oppdater «siste lagrede analyse» øverst her etter en fullført kjøring. Les begge filer tilbake og kontroller filnavn, datoer og lenker før leveransen bekreftes.

Denne prosedyren kjøres på bestilling. Lagring av dokumentet oppretter ingen periodisk oppgave eller varsling.

## 10. Endringslogg

| Versjon | Dato | Endring |
| --- | --- | --- |
| 1.0 | 29.09.2026 | Opprettet egen CAPT-oppdateringsprosedyre fra IAF og arbeidsflyten bak analysen 29.09.2026. Innført daterte analyser i Doc og lenker mellom prosedyre og siste resultat. |

