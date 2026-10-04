---
name: oil-market-bbb
description: Bear/Base/Bull-rammeverk for råolje- og destillatmarkedet med årlig bane 2027–2029 (rulleres hvert år) for Brent og produktcracks (diesel/gasoil, jet, bensin). Base er hovedscenarioet; Bear og Bull er stresstester knyttet til navngitte katalysatorer, og 25/50/25 er en merket konvensjonsvekt, ikke en kalibrert sannsynlighet. Dekker chokepoints (Hormuz, Rødehavet/Bab el-Mandeb, Suez/SUMED, Panama, Saudi/UAE bypass), råoljetilbud, lager, etterspørsel, Russland/Ukraina, raffinering og forwardkurve. Dekker IKKE tankshipping ([[oil-shipping-bbb]]) eller riggmarkedet ([[rig-market-bbb]]) — begge bruker denne som input. ALLTID bruk når brukeren nevner "Oil Market BBB"/olje-BBB, ber om å lage, kjøre eller "oppdatere modul" for oljemarkedet, eller spør om Brent-utfallsrom, destillatmarkedet, crack-spreader, forwardkurve eller oljelager — selv uten skillnavnet. Input til IAF ([[iaf-valuation]]) for olje- og raffineriselskaper.
---

# Oil Market BBB

**Revision:** 2026-10-04.1 — bump on every change (date.counter). The installed skill is only a
pointer to this file; this folder copy is the master.

Et Bear/Base/Bull-scenariosett for råolje- og destillatmarkedet med en årlig
bane for de tre neste hele kalenderårene. Formålet er en testbar hypotese om
utfallsrommet og en eksplisitt risikovurdering — ikke en nyhetsoppsummering.
Hold dokumentet til hovedpunktene.

Skillen er **toppen av kjeden**: [[oil-shipping-bbb]] og [[rig-market-bbb]]
henter oljebildet herfra og lager aldri egne oljeprognoser. Det betyr at
denne skillen må levere et stabilt, definert grensesnitt (se «Grensesnitt
mot nedstrømsskills og IAF»).

## Filer og lagring

- Skill: `C:\GitWork\hsaether\Claude\Finance\skills\oil-market-bbb\`
  (`SKILL.md` + `references/update-procedure.md` +
  `references/definitions-and-sources.md`).
- Output: `C:\GitWork\hsaether\Claude\Finance\docs\oil-market-bbb.md` — én
  løpende baseline-fil. Baseline-dato står i H1. Git gir historikk.
- Før overskriving: les forrige fil og ta med forrige BBB-verdier i change
  log som «forrige verdi», slik at endringer kan spores uten eldre filer.
- Skriv alltid via Filesystem-verktøyene og **les filen tilbake** for å
  kontrollere tabeller og innhold. Levering kun i chat er ikke nok.

## To kjøremodus

### A. Initiér

Trigges av «lag Oil Market BBB», «start ny baseline» — og automatisk når
`docs\oil-market-bbb.md` ikke finnes. Full research på alle analyseblokkene.
Status: «Initiell baseline».

### B. Oppdater modul

Trigges av «oppdater modul» i oljesammenheng, «oppdater Oil Market BBB», eller
av en rekalibreringstrigger. Følg `references/update-procedure.md` **trinn for
trinn** — ikke forkort eller erstatt med en friere research-runde.

> «Oppdater modul» betyr ikke «oppsummer siste olje-nyheter». Det betyr «gjør
> ny grundig research og test om den eksisterende Oil Market BBB fortsatt er
> riktig». Bruk siste baseline som utgangspunkt, men la den ikke bli et anker:
> hver kjøring skal aktivt forsøke å falsifisere Base. Hvis ny informasjon ikke
> er sterk nok til å endre modellen, skal konklusjonen være eksplisitt: **Oil
> Market BBB beholdes uendret.**

## Analysevindu og prisbasis

- Tre hele kalenderår fra kjøringstidspunktet — per nå **2027–2029**, samme
  vindu som [[oil-shipping-bbb]] og [[rig-market-bbb]].
- Rulleres ved årsskiftet: første kjøring i et nytt år legger til nytt sluttår
  og flytter første år til «realisert» (grunnlag for forecast vs. faktisk).
  Rulling er ikke nullstilling — overlappende år arves og testes.
- Alle priser er **årsgjennomsnitt i nominelle USD**, ikke sluttkurs eller
  spot. Dagens spot (eller en krigstopp) brukes aldri automatisk som
  treårsforutsetning.
- Benchmarks og crack-definisjoner står i `references/definitions-and-sources.md`
  og skal brukes uendret fra kjøring til kjøring. Bytte av serie dokumenteres
  i change log.

## Scenarioer: Base og katalysatorbaserte stresstester

Det finnes ingen statistisk fordeling bak geopolitiske og strukturelle
oljehendelser. I tråd med [[iaf-valuation]] gjelder derfor:

- **Base** er den mest sannsynlige banen og beslutningscaset som
  selskapsanalyser bygger på.
- **Bear** og **Bull** er stresstester, hver knyttet til **navngitte
  katalysatorer** — hva som må skje, mekanismen, når det tidligst kan slå inn,
  og hvilke **signposts** (observerbare indikatorer) som viser at markedet
  beveger seg dit. Bear er det verste rimelig forutsigbare utfallet, Bull det
  beste. De trenger ikke være symmetriske.
- Vurder både en **tilbuds-** og en **etterspørselskatalysator** for hver hale
  (f.eks. Bear: Hormuz-gjenåpning *og* global resesjon/OPEC+-markedsandelskamp;
  Bull: varig chokepoint-stenging *og* sterk rebound med tomme lagre). Velg den
  eller kombinasjonen som gir det mest relevante stresset, og si hvorfor.
- **25/50/25** er en merket konvensjonsvekt, ikke en kalibrert sannsynlighet.
  Kolonnen heter «Vekt (konvensjon)». Den brukes som felles vekting i
  nedstrømsskills, og endres bare ved en dokumentert skjevhet. Sannsynlighets-
  språk om halene unngås.

## To atskilte, men koblede markeder

1. **Råolje** — Brent (og WTI-spread ved behov).
2. **Destillat** (diesel/gasoil, jet, bensin) — behandles som **marginmessig
   delvis frikoblet** fra råolje. Crackene har egen dynamikk (raffinerikapasitet,
   outages, sesong, regionale balanser) og kan gå motsatt vei av Brent.

Derfor lages Brent-bane og crack-bane **separat**, og produktprisen fremkommer
som sum:

```
Produktpris ($/fat) = Brent + crack
Δ produktpris        = Δ Brent + Δ crack
```

### Destillat-prissensitivitet

1. Vurder hver crack mot sitt eget historiske normalbånd, ikke bare mot Brent.
2. Bruk raffineringsblokken som hoveddriver for crack-banen; lager, sesong og
   forwardspread som bekreftende signaler.
3. Vis en **sensitivitetsmatrise** for diesel/gasoil (Brent-scenario ×
   crack-scenario, Base-året 2027 og snitt 2027–2029), med produktpris i $/fat
   og $/tonn. Marker hvilke kombinasjoner som er konsistente og hvilke som er
   lite sannsynlige (f.eks. Bear-Brent + Bull-crack krever raffineribortfall
   uten råoljeknapphet).
4. Dekomponér siste periodes faktiske diesel-prisendring i Brent-bidrag og
   crack-bidrag. Det er det konkrete svaret på «hvor frikoblet er destillat nå».

## Analyseblokker (bruk som overskrifter)

Detaljer per steg i `references/update-procedure.md`.

1. **Chokepoints og omdirigering** — Hormuz, Rødehavet/Bab el-Mandeb,
   Suez/SUMED, Saudi East–West og UAE/Fujairah bypass, Saudi/Oman STS,
   Iran–USA, Panama. Uttrykk effekten i fat/dag som faktisk når markedet, ikke
   bare «åpen/stengt». Tonnasje- og rate-effekter hører hjemme i
   [[oil-shipping-bbb]].
2. **Råoljetilbud** — OPEC+ (kvoter, compliance, faktisk eksport, ledig
   kapasitet og om den fysisk kan nå markedet), Gulf, USA/Brasil/Guyana/Canada,
   Russland. Skill nominell produksjon fra fysisk supply.
3. **Lager** — USA (crude, Cushing, SPR, bensin, destillat), Kina, OECD/Europa,
   ARA, Singapore. Trekk/bygg, sesongavvik, nivå mot 5-årssnitt, dager dekning.
4. **Etterspørsel** — global og USA/Kina/Europa/India, per produkt. Skill
   strukturell endring, demand destruction og rebound.
5. **Russland/Ukraina** — fast premiss, verifiseres hver gang.
6. **Raffinering og destillatproduksjon** — utilization/outages per region, ny
   kapasitet og closures, Kina som swing-supplier, USA/India som marginale
   eksportører, regionale over-/underskudd.
7. **Forwardmarked** — Brent M1–M4-spread (klassifisering under), ICE gasoil
   M1–M4 i $/tonn, og **lang ende** (desemberkontrakter for 2027–2029). Lang
   ende er markedets pris på mid-cycle og er nøkkelinput for E&P-capex i
   [[rig-market-bbb]].
8. **Cracks** — diesel/gasoil, jet, bensin. Vurder om endringen skyldes
   råolje, raffineritilgjengelighet eller faktisk produktknapphet.
9. **Balansesjekk** — enkel tilbud − etterspørsel = implisitt lagerendring
   (mb/d) per scenario og år. Formålet er konsistens: en Brent-bane som krever
   en lagerbane markedet ikke kan levere, må justeres.

## Forwardkurve-klassifisering (fast regel)

| Brent M1–M4 | Signal |
|---|---|
| Backwardation > $5/fat | Tydelig Tight |
| Backwardation $2–5/fat | Moderat Tight |
| Backwardation $0–2/fat | Omtrent balansert |
| Contango $0–2/fat | Svakt Loose |
| Contango > $2/fat | Tydelig Loose / Bear |

Les alltid sammen med lagerretningen:

| Kurve | Lager | Tolkning |
|---|---|---|
| Backwardation | Fallende | Sterk fysisk Tightness |
| Backwardation | Byggende | Mulig normalisering på vei |
| Contango | Fallende | Kurven henger etter, eller risikopremie er priset ut — sjekk |
| Contango | Byggende | Klart Loose-signal |

Hvis spreaden ikke kan hentes med kilde og dato: merk `[?]` og ikke klassifiser.

## Datadisiplin

- Merk hvert tall: `[F]` rapportert fakta, `[E]` ekstern prognose, `[A]` egen
  antakelse, `[?]` ukjent. Manglende nye data er ikke bevis for uendret marked.
- Oppgi kilde, definisjon, enhet og dato (observasjon og publisering).
  Bland aldri serier (f.eks. NYMEX ULSD–WTI og ICE gasoil–Brent) uten å si det.
- Fakta vs. tolkning: (1) ny fakta, (2) hva den betyr fysisk, (3) om den
  endrer modellen. Enkeltnyheter flytter normalt ikke BBB. Diplomatiske
  signaler teller ikke før de gir verifisert, varig fysisk effekt.
- **Brukerens input er input, ikke referanse.** Lenker, tall og utkast vurderes
  kritisk (hva måler det, ferskhet, definisjon) — bruk det som holder, avvis
  resten, og dokumenter vurderingen i kildeoversikten.
- Kildekatalog, konverteringsfaktorer og kjente datasvakheter står i
  `references/definitions-and-sources.md`.

## Rekalibreringstriggere (forslag)

Full oppdatering utløses når:

- Brent front eller lang ende (des.-kontrakt) flytter seg > 15 % på en måned
- Brent M1–M4 skifter regime i klassifiseringstabellen og holder seg der i to uker
- faktisk flow gjennom Hormuz, Bab el-Mandeb/Suez eller East–West/Yanbu endres > 20 %
- OPEC+-vedtak eller faktisk produksjonsendring > 0,5 mb/d
- raffineri- eller eksportkapasitet endres > 0,5 mb/d (outage, oppstart, closure)
- dieselcrack beveger seg > 25 % på en måned
- IEA/OPEC/EIA reviderer global etterspørsel > 0,5 mb/d for et år i vinduet
- Russland/Ukraina-premisset brytes (f.eks. eksportforbud opphevet eller varig utvidet)
- en Bear- eller Bull-katalysator utløses eller en signpost krysses

## Output-format: `docs\oil-market-bbb.md`

```markdown
# Oil Market BBB — [baseline-dato]

## Metadata
- Analysedato, status (Initiell / Endelig / Foreløpig og hvorfor)
- Forrige baseline (dato), analysevindu (2027–2029)
- Benchmarks brukt (se definitions-and-sources)

## Hovedkonklusjon
- BBB endret / beholdes uendret — eksplisitt
- Base i to setninger (Brent-bane + dieselcrack-bane)
- Viktigste Bear- og Bull-katalysator

## Scenariodefinisjoner
| Scenario | Vekt (konvensjon) | Katalysator(er) | Mekanisme | Tidligst | Signposts |
|---|---|---|---|---|---|
| Bear | 25 % | ... | ... | ... | ... |
| Base | 50 % | ... | ... | ... | ... |
| Bull | 25 % | ... | ... | ... | ... |

## Brent ($/fat, årsgjennomsnitt)
| Scenario | 2027 | 2028 | 2029 | Snitt |
|---|---|---|---|---|

## Cracks ($/fat, årsgjennomsnitt)
| Scenario | Diesel/gasoil 27 / 28 / 29 | Jet 27 / 28 / 29 | Bensin 27 / 28 / 29 |
|---|---|---|---|

## Destillat-sensitivitet
- Matrise Brent × dieselcrack (produktpris $/fat og $/tonn)
- Dekomponering av siste periodes dieselprisendring (Brent vs. crack)

## Råoljemarkedet
### Chokepoints og omdirigering
### Tilbud
### Lager
### Etterspørsel
### Russland/Ukraina (fast premiss — status)
### Forwardkurve (M1–M4, gasoil-spread, lang ende, klassifisering)
### Balansesjekk

## Destillatmarkedet
### Raffinering og kapasitet
### Regionale balanser
### Sesongeffekter
### Cracks

## Signpost-status og risikovurdering
- Signposts: status nå vs. forrige baseline
- Hva overvåkes til neste oppdatering

## Grensesnitt for nedstrømsskills
- Kort liste: hva endret seg som [[oil-shipping-bbb]] / [[rig-market-bbb]]
  må ta inn (eller «ingen endring av betydning»)

## Change log
- Nytt / uendret / endret (forrige verdi → ny verdi, årsak, kilde)
- Forecast vs. faktisk (for realisert eller delvis observert år)
- Vekter: beholdt eller endret — eksplisitt
- Ny baseline-dato

## Vedlegg: kilder
(kilde, definisjon, observasjons- og publiseringsdato)
```

Hoveddelen skal være kort per underoverskrift. Tallrekker og kildedetaljer
legges i vedlegg.

## Grensesnitt mot nedstrømsskills og IAF

Hver baseline skal levere, i fast form:

- Brent-bane per scenario og år, og lang ende av forwardkurven
- crack-bane per scenario og år (diesel/gasoil, jet, bensin)
- chokepoint-status uttrykt i fat/dag som faktisk når markedet
- raffineri- og handelsgeografi (hvem eksporterer, hvem underskudd)
- lagerbane (bygging/tapping, inkl. SPR-gjenoppbygging)
- scenariokatalysatorer og signposts

**IAF ([[iaf-valuation]])**: For olje- og raffineriselskaper mates Base-banen
inn som beslutningscase; Bear og Bull brukes som katalysatorbaserte
stresstester. For shipping- og riggselskaper går veien via
[[oil-shipping-bbb]] eller [[rig-market-bbb]] — Oil Market BBB mates ikke
direkte inn i deres IAF.

## Standing parameters

- Analysevindu: tre hele kalenderår (2027–2029 nå), rulleres årlig.
- Base = beslutningscase; Bear/Bull = stresstester med navngitte katalysatorer.
- Vekt 25/50/25 = konvensjon, ikke sannsynlighet.
- Årsgjennomsnitt, nominelle USD, faste benchmarks.
- Russland/Ukraina er fast premiss til ny verifisert informasjon tvinger en endring.
- Forwardkurve-terskler som i tabellen — ikke sett egne terskler ad hoc.
- Shipping, tonnasje og rigger hører ikke hjemme her.
- Ved oppdatering: følg `references/update-procedure.md` i sin helhet.
