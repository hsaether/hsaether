---
name: rig-market-bbb
description: Bear/Base/Bull (25/50/25) rammeverk for det offshore riggmarkedet (jackups, drillships, semisubs), med 3-års utfallsrom (2027-2029) for marketed committed utilization og leading-edge dagrater per riggklasse og region. Oversetter Oil Market BBB ([[oil-market-bbb]]) via E&P-kontantstrøm, capex/FID og operatørplaner til riggetterspørsel, og bygger regional tilbuds- og etterspørselsbalanse (flåte, stacked, nybygg, reaktivering, retirement, kontraktsdekning). ALLTID bruk denne skillen når brukeren nevner "Rig Market BBB"/"Riggmarked BBB", ber om å lage/kjøre/oppdatere modul for riggmarkedet, eller spør om dagrater, utilization, tilgjengelighet, nybygg eller reaktivering for jackups, drillships eller semisubs (inkl. NCS harsh-environment) - selv uten å nevne skillnavnet. Input til IAF ([[iaf-valuation]]) for riggselskaper; bygger på Oil Market BBB og lager ALDRI en ny oljeanalyse selv. Dekker IKKE selskapsspesifikk backlog, realisert rate, kostnader, capex og gjeld - det håndteres i selskapsanalysen.
---

# Rig Market BBB

Et strukturert Bear/Base/Bull-scenariosett (25 % / 50 % / 25 %, i tråd med
[[iaf-valuation]]) for det offshore riggmarkedet — jackups, drillships og
semisubs — med et utfallsrom for de neste tre hele kalenderårene
(2027–2029). Formålet er en testbar hypotese om **marketed committed
utilization** og **leading-edge dagrater** per riggklasse og region, med
eksplisitt tilbuds-/etterspørselsbalanse og risikovurdering — komprimert til
hovedpunktene, uten å drukne i detaljer.

Output av enhver kjøring er ett dokument: **`docs\rig-market-bbb.md`**.

Markedsrater er *input* til selskapsanalysene. Faktisk kontraktsdekning,
realisert rate, inntjeningsdager, kostnader, investeringer og gjeld
håndteres separat i selskapsanalysen (se "Kobling til IAF").

## Grunnprinsipp: input, ikke duplikat

Rig Market BBB lager **aldri** en egen oljeprognose. Den henter
oljescenarioer, etterspørsel, Midtøsten/geopolitikk og forwardkurve fra
gjeldende [[oil-market-bbb]] (`docs\oil-market-bbb.md`) og oversetter dem
til riggmarkedet via denne kjeden:

**Oljepris → E&P-kontantstrøm → offshore capex/FID → riggetterspørsel
(riggår) → utilization → leading-edge dagrate**

…modifisert av *effektivt riggtilbud* (flåte, stacked, nybygg, reaktivering,
retirement) og *kontraktsdekning* (hvor mye av hvert år som allerede er
låst).

Tre forhold gjør at kjeden ikke kan brukes mekanisk:

1. **Forsinkelse.** Riggetterspørsel følger forventet/mid-cycle oljepris og
   E&P-kontantstrøm med 6–18 mnd (leteboring) til 1–3 år (dypvannsutbygging).
   2027 er i stor grad allerede bestemt av backlog; 2029 avhenger av FID-er
   som tas i 2026–2027. Dagens spotpris er aldri en treårsforutsetning.
2. **Tilbudsrespons.** Høye rater kan utløse reaktivering og nybygg som kapper
   oppsiden — og gjør at høy olje ikke automatisk gir Bull-rigg.
3. **Operasjonell geopolitikk.** Høy oljepris kan opptre samtidig med
   evakuering, force majeure, offhire og suspenderte rigger i enkeltregioner
   (særlig Midtøsten). Oljepriseffekt og operasjonell risiko vurderes
   separat.

Hvis gjeldende Oil Market BBB er utdatert eller mangler: si det eksplisitt,
merk analysen **Foreløpig**, og be om (eller kjør) en oppdatering av
oljeanalysen først — ikke lag en skygge-oljeanalyse her, og presenter aldri
eldre oljeforutsetninger som nyverifiserte. Konkrete kriterier står i
`references/update-procedure.md` (steg 1).

## Filer og lagring

- Skill: `C:\GitWork\hsaether\Claude\Finance\skills\rig-market-bbb\`
  (`SKILL.md` + `references/`).
- Output: `C:\GitWork\hsaether\Claude\Finance\docs\rig-market-bbb.md` — én
  løpende baseline-fil (som `oil-market-bbb.md` og `oil-shipping-bbb.md`).
  Baseline-dato står i H1. Før overskriving: les forrige fil og ta forrige
  BBB-verdier med i endringsloggen som «forrige verdi», slik at diff kan
  gjøres uten eldre filer. Git gir full historikk.
- Input: `docs\oil-market-bbb.md`.
- Skriv alltid via Filesystem-verktøyene og **les filen tilbake** for å
  kontrollere innhold, tabeller og lenker. Levering kun i chat er ikke nok.

## To kjøremodus

### A. Initiér (ny baseline fra bunnen)

Trigges av "lag Rig Market BBB", "start ny riggbaseline" — og **automatisk
når `docs\rig-market-bbb.md` ikke finnes**. Gjør full research på alle
analyseblokker (se under). Det finnes da ingen forrige baseline å teste mot:
sett status «Initiell baseline», bruk indikatortabellen i
`references/update-procedure.md` som *startkalibrering* (ikke som
validerte terskler), og ta med seed-kontrollpunktene derfra i «Åpne
kontrollpunkter».

### B. Oppdater modul

Trigges av «Oppdater modul» i Rig Market BBB-sammenheng, av «Oppdater Rig
Market BBB» fra en annen oppgave, eller av en rekalibreringstrigger (se
under). Følg `references/update-procedure.md` **trinn for trinn** — ikke
forkort eller erstatt med en friere research-runde. Definisjoner, regionkart
og kildehierarki står i `references/definitions-and-sources.md`.

Kommandoen oppdaterer **analysedokumentet**. Selve prosedyren endres bare
ved en uttrykkelig metodeendring eller en dokumentert nødvendig
presisering. Arbeidsflyten er manuell.

Den viktigste regelen, gjentatt fordi den lett glemmes:

> «Oppdater modul» betyr ikke «oppsummer siste rigg-nyheter». Det betyr «gjør
> ny grundig research og test om den eksisterende Rig Market BBB fortsatt er
> riktig». Bruk siste baseline som utgangspunkt — ikke nullstill — men la
> den ikke bli et anker: hver kjøring skal aktivt forsøke å falsifisere
> Base. Hvis ny informasjon ikke er sterk nok til å endre modellen, skal
> konklusjonen være eksplisitt: **Rig Market BBB beholdes uendret.**

## Analysevindu

De tre neste hele kalenderårene ved kjøringstidspunktet — per opprettelse
**2027–2029**, likt for [[oil-market-bbb]] og [[oil-shipping-bbb]].
Vinduet rulleres ved årsskiftet: første kjøring i et nytt kalenderår legger
til nytt sluttår og flytter det første året til «realisert» (grunnlag for
forecast-vs-faktisk i endringsloggen). Rulling er ikke nullstilling —
overlappende år arves fra forrige baseline og testes.

## Segmenter og regioner

BBB-tabeller (utilization + rate per år) lages for:

| Segment | Merknad |
|---|---|
| Tier-1 drillships | Primært 6./7. generasjon |
| NCS harsh-environment semisubs | Egen rate/utilization — ikke overfør fra global HE |
| Benign/deepwater semisubs | Skilles fra NCS HE |
| Premium/high-spec jackups | Global premium-rate overføres ikke til eldre standardrigger, tender-assist eller norske HE-jackups |

Andre segmenter (eldre standard jackups, norske HE-jackups, tender-assist,
platform rigs, Tier-2 drillships) vurderes separat, med datamangler
synliggjort. Offentlige data skiller ikke Tier-1, NCS HE og benign/deepwater; bruk
proxy (se `references/definitions-and-sources.md` §3) og merk den tydelig.
Hver rigg tilordnes **én** region — regionkartet og
klassifiseringen står i `references/definitions-and-sources.md`.

## Scenarioer: definisjon og kobling til Oil Market BBB

Rig-scenarioer er **tilstander i riggmarkedet**, ikke omdøpte oljescenarioer:

- **Bear:** svak utnyttelse og press på rater — kan skyldes lav olje/FID-
  utsettelser, *eller* tilbudsflom (reaktivering/nybygg) og aggressive
  anbud selv med høy olje.
- **Base:** gradvis, regionalt differensiert utvikling.
- **Bull:** stram tilgjengelighet og stigende leading-edge rater over tid,
  med begrenset tilbudsrespons.

For å gjøre koblingen til oljen eksplisitt og etterprøvbar skal hver
baseline vise en **betinget matrise** P(rig-scenario | olje-scenario), og
sjekke at den implisitte marginalen er nær 25/50/25 (avvik >3 pp
begrunnes). Startkalibrering for første kjøring (mitt forslag, ikke evidens; senere
kjøringer starter fra matrisen i siste baseline — begrunn og
juster hver kjøring):

| Oljescenario (Oil Market BBB) | Rig Bear | Rig Base | Rig Bull |
|---|---|---|---|
| Bear (25 %) | 50 % | 40 % | 10 % |
| Base (50 %) | 20 % | 60 % | 20 % |
| Bull (25 %) | 10 % | 45 % | 45 % |
| **Implisitt marginal** | 25 % | 51 % | 24 % |

Bull-olje drevet av forsyningssjokk (f.eks. stengt Hormuz) gir bare 45 %
Bull-rigg: kontantstrømmen løfter Brasil/NCS/Vest-Afrika med forsinkelse,
men Gulf-jackups, demand destruction og makrorisiko trekker motsatt vei.

**Kontraktsdekning styrer spredningen.** Bear–Bull-spredningen i utilization
og rate skal være smal i 2027 (høy backlog-dekning) og utvides mot 2029.
Avvik fra dette må forklares.

Én felles vekting (25/50/25) brukes for alle segmenter med mindre en
segmentspesifikk skjevhet dokumenteres — vektene skal alltid summere til
100 %.

## Analyseblokker (bruk som overskrifter i dokumentet)

Detaljer per steg i `references/update-procedure.md`.

1. **Oljegrunnlag** — importert fra Oil Market BBB, med kjeden over.
2. **Rig count, utilization, availability** — global og regional.
3. **Fixtures og rate-slutninger** — leading-edge, med konfidensgrad.
4. **Selskapenes flåtestatus** — rigg-for-rigg availability og kontraktsdekning.
5. **Operatøretterspørsel** — prospects → anbud → tildelinger, i riggår.
6. **Riggtilbud og ekspansjon** — nybygg, stranded, reaktivering, retirement.
7. **Regional balanse** — region × riggklasse.
8. **BBB 2027–2029** — utilization + leading-edge rate per segment og år.
9. **Indikatorer og modelltest** — score, avgrenset oppdatering.
10. **Beslutning og change log.**

## Datadisiplin (faste regler)

- Merk hvert tall: `[F]` rapportert fakta, `[E]` ekstern prognose, `[A]` egen
  antakelse, `[?]` ukjent. Ukjent rate eller manglende flåtedata merkes
  ukjent — manglende nye observasjoner er ikke dokumentasjon på uendret marked.
- Oppgi alltid kildens definisjon, nevner og dato (observasjon + publisering).
  Bland aldri kilder i samme tidsserie uten å dokumentere overgangen.
- Rate-konfidens A–D per fixture (se definisjonsfilen). Tynt utvalg
  (n < 3 sammenlignbare fixtures på 6 mnd) → intervall, ikke punktestimat.
- Skill: rene dagrater ≠ kontraktsverdi per dag ≠ realisert langsiktig rate.
- Én regional kontrakt endrer ikke den globale modellen uten begrunnelse.
- Regional flytting, eierskifter og konsolidering skaper ikke nye rigger.
  Unngå dobbelttelling mellom nybygg, reaktivering og markedsført flåte.
- Skill stigende aktivitet fra økt evne til å oppnå høyere rater
  (utilization kan stige mens aggressive tilbud holder ratene nede).
- Direkte kildelenke for alle nye funn; ingen lenker som ikke faktisk er hentet.
- **Brukerens input er input, ikke referanse.** Lenker, tall, utkast og
  kilder brukeren gir vurderes kritisk for verdi (hva måler den, definisjon,
  ferskhet, tilgang, avgrensning) — hent ut det som er fornuftig, avvis eller
  nedvekt resten, og dokumenter vurderingen i kildeoversikten.
- **Én serie = én kilde.** Westwood-MCU, Petrodata «marketed contracted» og
  Baker Hughes «active» måler ulike ting og kan ikke blandes eller brukes
  til å korrigere hverandre; bruk dem til kryssjekk av retning.
- **Kilderegioner er grovere enn vårt regionkart** (f.eks. «NW Europe»,
  «South America»). Der en region ikke kan splittes: si det, og ikke
  konstruer NCS-/UK- eller Brasil-/Guyana-tall.
- **Dynamisk innhold** (tabeller/grafer som lastes som bilder) kan ikke
  leses automatisk: merk kilden «ikke lest», og be brukeren om skjermbilde
  eller kopierte tall i stedet for å gjette.

## Rekalibreringstriggere (forslag — bekreft)

Ikke en del av originalprosedyren; foreslått for konsistens med
[[oil-shipping-bbb]]. Full vurdering utløses når:

- Oil Market BBB endrer scenario, sannsynlighet eller intervall vesentlig
- marketed committed utilization for et BBB-segment flytter seg >3 pp
- leading-edge rate for et BBB-segment avviker >10 % fra Base for samme år
- ≥2 nye Tier-1 floaters bestilles, eller en kjent stranded/cold-stacked
  enhet reaktiveres med kontrakt
- en operatør utsetter/kansellerer et flerårig tildelingsprogram
  (Petrobras, Aramco, Equinor, m.fl.)
- større fusjon/oppkjøp endrer riggeierskap eller flåtedata
- krigshendelse som setter en hel region offhire/force majeure

## Output-format: `rig-market-bbb.md`

Bruk alltid denne strukturen. Hold hoveddelen komprimert (Region × riggtype-
matrisen kun for materielle celler; fixtures, rigg-for-rigg og kilder i
vedlegg).

```markdown
# Rig Market BBB — [baseline-dato]

## Metadata
- Analysedato og tidssone (Europe/Oslo), analyseår
- Status: Endelig / Foreløpig (og hvorfor)
- Forrige riggbaseline (dato)
- Oil Market BBB brukt (dato, alder i dager, scenarioer)
- Lenker: SKILL.md, update-procedure.md, docs\oil-market-bbb.md

## Hovedkonklusjon
- BBB endret / uendret — eksplisitt
- Segmentrangering (sterkest → svakest) med viktigste begrunnelser
- Største risiko mot Bear / mot Bull

## BBB-tabeller 2027–2029
### Tier-1 drillships
| Scenario | Sannsynlighet | 2027 | 2028 | 2029 | Nøkkeldrivere |
|---|---|---|---|---|---|
| Bear | 25 % | util % / USD k/dag | ... | ... | ... |
| Base | 50 % | ... | ... | ... | ... |
| Bull | 25 % | ... | ... | ... | ... |
(samme tabell for NCS HE semis, benign/deepwater semis, premium jackups;
 celleformat "marketed committed util % / leading-edge USD tusen per dag")
### Andre segmenter (separat vurdert, datamangler markert)

## Modellkoherens mot Oil Market BBB
- Betinget matrise P(rig | olje), implisitt marginal, avvik og begrunnelse
- Kontraktsdekning per segment og år (forklarer spredningen)

## Nye funn siden sist (dato + kilde)

## Region × riggtype-matrise (materielle celler)
Utilization (definisjon) · marketed available · warm/cold stacked ·
leading-edge rate + 6–12 mnd trend · ledig kapasitet og etterspørsel per år
(riggår) · nybygg/reaktivering · retirement · netto flåtevekst ·
oljeprisfølsomhet · datakonfidens

## Tilbud: nybygg, reaktivering, skraping og netto effektiv kapasitet
(nominell ordrebok → sannsynlig levering → konkurransedyktig kapasitet;
 nybygg-/reaktiveringsøkonomi vs. dagens rater)

## Olje → capex/FID → riggetterspørsel (per oljescenario og region)

## Triggerkontroll og modellbeslutning
(indikatortabell med score, vekt-/intervallbeslutning)

## Konsekvenser for selskapsanalyser

## Usikkerhet, datakvalitet og åpne kontrollpunkter
(inkl. kildestatus: hva som ble lest, as-of-dato, hva som var
 utilgjengelig/dynamisk)

## Change log
- Nytt / uendret / endret (gammel → ny verdi, årsak, kilde, berørte
  regioner/selskaper)
- Forecast vs. faktisk (forrige baselines verdi for året som nå er realisert/
  delvis observert)
- Vekter og intervaller: beholdt eller endret — eksplisitt
- Ny baseline-dato

## Vedlegg
Fixture-logg · rigg-for-rigg availability · kilder (lenke, observasjonsdato,
publiseringsdato, definisjon)
```

## Standing parameters

- BBB-vekting: 25 % Bear / 50 % Base / 25 % Bull — konsistent med
  [[iaf-valuation]] og [[oil-market-bbb]], med mindre brukeren ber om noe
  annet eller en segmentskjevhet er dokumentert. Vektene testes ved hver
  oppdatering og summerer til 100 %.
- Tidshorisont: tre hele kalenderår (2027–2029 ved opprettelsen), se
  "Analysevindu".
- Segmenter og regioner holdes separate — aldri én blandet global rate.
- Dagens ekstreme oljepris (og dagens spot-rater) brukes aldri automatisk som
  treårsforutsetning.
- Ved oppdatering: følg alltid `references/update-procedure.md` i sin helhet.

## Kobling til IAF

Når Rig Market BBB brukes som input til en selskapsanalyse i
[[iaf-valuation]] (Transocean, Valaris, Noble, Seadrill, Borr, Odfjell,
ADES, Shelf m.fl. — sjekk gjeldende eierskap/flåte), er det BBB-tabellene
(utilization og leading-edge rate per segment, år og scenario) som mates
inn i det år-for-år-bygde g-estimatet/FCF-forecasten — ikke et
punktestimat. Behold Bear/Base/Bull-spennet helt til IAF-testen.

Match selskapets faktiske flåtesammensetning (klasse, spec, region, alder)
mot riktig rad før ratene brukes. Selskapets resultat styres av *backlog og
realisert rate*, ikke leading-edge: bruk gapet mellom leading-edge og
selskapets gjennomsnittlige backlog-rate (mark-to-market) som overgang, og
håndter dekning, revenue efficiency, kostnader, capex og gjeld i
selskapsanalysen.
