# Oil Shipping BBB

## Dokumentinformasjon

- Dokumenttype: gjenbrukbar prosedyre for oppdatering av tankmarkedsanalysen.
- Opprettet: 29. september 2026.
- Kilde: [Shipping BBB](https://chatgpt.com/c/6aae49a0-f320-83eb-b9a6-1df52e178751), mandat fra 19. september og siste prosedyrebeskrivelse fra 27. september 2026.
- Navn i originaloppgaven: **Shipping Market BBB / Shipping BBB**. Det lokale modulnavnet er **Oil Shipping BBB**.
- Prosedyrefil: `C:\GitWork\hsaether\Chatgpt\Finance\Module\Oil Shipping BBB.md`.
- Resultatmappe: `C:\GitWork\hsaether\Chatgpt\Finance\Doc`.
- Første lokale analyseresultat: [Oil Shipping BBB – 26. september 2026](../Doc/Oil%20Shipping%20BBB%20-%202026-09-26.md).
- Skrivetilgang: bekreftet 29. september 2026 ved opprettelse, gjenlesing og sletting av en midlertidig kontrollfil i begge mapper.

## Formål og avgrensning

Modulen gir et felles Bear/Base/Bull-markedsgrunnlag for selskapsanalyser innen råoljetank og produkttank. Den dekker VLCC, Suezmax, Aframax, LR2, LR1 og MR. Panamax tas med der relevant, og Handy når det påvirker MR-markedet vesentlig. Container, tørrbulk, LNG og LPG inngår ikke i denne modulen.

Kjeden som skal analyseres er:

**Oil Market BBB → handelsstrømmer → seilingsdistanse → ton-mile → skipsdøgn → effektiv tonnasje → normaliserte TCE/rater.**

Analysen dekker de neste tre analyseårene; ved opprettelsen er dette **2027–2029**. Flåtetilbudet vurderes dessuten for kommende 36 måneder. Ved årsskifte rulleres analyseårene eksplisitt og endringen dokumenteres.

Dette dokumentet bevarer prosedyren fra originaloppgaven. Avsnittene om lokal arbeidsflyt, lagring, resultatformat og beregningspresiseringer konkretiserer filversjonen. Opprettelsen 29. september er dokumentasjon og eksport av tidligere arbeid, ikke en ny markedsanalyse.

## Instruksjonen «Oppdater modul»

**«Oppdater modul» i Oil Shipping BBB-sammenheng**, eller **«Oppdater Oil Shipping BBB»** fra en annen oppgave, betyr at denne prosedyren hentes og kjøres komplett, og at et oppdatert analysedokument lagres i Doc.

1. Les denne filen og siste daterte Oil Shipping BBB-analyse i Doc.
2. Hent siste daterte Oil Market BBB-analyse i Doc som oljegrunnlag. [Oil Market BBB-prosedyren](Oil%20Market%20BBB.md) beskriver hvordan dette grunnlaget oppdateres. Originalmandatet forutsetter at Oil Market BBB allerede er oppdatert; noter hvilken baseline som brukes. Ved manglende eller åpenbart utdatert grunnlag skal begrensningen gjøres tydelig, og en foreløpig shippinganalyse skal merkes som foreløpig.
3. Gjennomfør alle ti kontrollpunktene og vurder triggerne nedenfor med ny research.
4. Sammenlign med forrige shippingbaseline, dokumenter beslutningen og lagre et nytt datert analyseresultat.
5. Les resultatet tilbake og bekreft at dokumentet er komplett og korrekt lagret.

Kommandoen oppdaterer **analysedokumentet**. De faste prosedyrene endres bare når bruker ber om en metodeendring, eller en nødvendig metodisk presisering blir uttrykkelig dokumentert. Det opprettes ingen automatisk kjøring eller markedswatch.

## Fast prosedyre fra Shipping BBB

Prosedyren for **«Oppdater modul» i Shipping Market BBB** er fast og skal kjøres komplett hver gang, uten at du trenger å spesifisere noe mer.

1. **Importer siste Oil Market BBB**
   - Oil BBB skal være oppdatert på forhånd.
   - Importer oljepris-/etterspørselsbane, crude/product balances, refinery-effekter, Russland, Midtøsten og geopolitikk.
   - Shipping BBB skal ikke lage en ny oljeanalyse, men oversette Oil BBB til shippingeffekter.

2. **Oppdater spot/TCE for alle relevante segmenter**
   - Crude: VLCC, Suezmax, Aframax.
   - Product: LR2, LR1, MR.
   - Bruk Baltic/andre markedsdata, faktiske fixtures og rapporterte selskaps-TCE-er.
   - Skille eksplisitt mellom ekstrem spot og bærekraftige/normaliserte rater.
   - Sammenlikn med forrige Shipping BBB.

3. **Oppdater seilingsmønstre og ton-mile**
   - MEG → Asia.
   - Atlantic Basin → Asia.
   - US Gulf → Europa/Latin-Amerika/Asia.
   - Russland.
   - India/Asia/Midtøsten → Europa.
   - Inventory restocking/floating storage.
   - Se etter endringer i både volum **og distanse**.

4. **Oppdater alle viktige chokepoints**
   - Hormuz.
   - Red Sea/Bab el-Mandeb.
   - Suez.
   - Saudi East-West pipeline/Yanbu.
   - Panama.
   - Cape of Good Hope.
   
   Effekten skal uttrykkes i **ekstra seilingsdøgn, ventetid, repositioning og redusert effektiv tonnasje**, ikke bare «åpen/lukket».

5. **Beregn effektiv tilgjengelig tonnasje**
   Ikke bare nominell flåte:
   - sanctioned/shadow fleet
   - skip >15 og >20 år
   - drydock/offhire
   - skip bundet på lange voyages
   - feilposisjonering
   - STS/shuttle/venting
   - clean↔dirty switching, spesielt LR2/Aframax.

6. **Oppdater fleet supply for kommende 36 måneder**
   Per segment:
   
   **dagens flåte + leveranser − skraping ± crossover = effektiv fleet growth**
   
   Følg:
   - orderbook/fleet
   - nye ordre
   - leveringsår
   - slippage
   - kanselleringer
   - skraping
   - alder
   - verftskapasitet.

7. **Oppdater refinery- og handelsgeografien**
   - nye raffinerier
   - closures
   - outages
   - russiske refinery-skader
   - Middle East export availability
   - Kina/India/USA eksportpolitikk
   - regional diesel/jet/gasoline-ubalanse.
   
   Dette er særlig viktig for LR/MR.

8. **Kontroller forward-markedet**
   - 1-års time charter.
   - 2–3 års perioderater.
   - relevante FFAs.
   - secondhand values.
   - resale/newbuild-priser.
   
   Periodemarkedet brukes som viktig kontroll på de normaliserte BBB-ratene.

9. **Rekalibrer Bear/Base/Bull 2027–2029**
   For hvert scenario skal vi oppdatere:
   - ton-mile
   - effektiv fleet growth
   - utilization/tightness
   - normalisert TCE for VLCC/Suezmax/Aframax/LR2/LR1/MR
   - scenario-sannsynlighet.
   
   **Dagens ekstremspot skal aldri automatisk annualiseres.**

10. **Change log mot forrige Shipping BBB**
   
   Oppdateringen skal eksplisitt svare:
   
   **Hva er nytt → hva betyr det → endrer det BBB?**
   
   Det skal fremgå dersom ny informasjon er interessant, men **ikke sterk nok til å endre ratebane eller sannsynligheter**.

### Faste rekalibreringstriggere

Full vurdering skal spesielt utløses når:
- spot/perioderater flytter seg >15 % på én måned eller >25 % på én uke
- orderbook/fleet endres >2 prosentpoeng
- ton-mile-estimat endres >1 prosentpoeng
- Hormuz/Suez/Red Sea/Panama-flow endres omtrent >20 %
- refinery/exportkapasitet endres >0,5 mb/d
- sanctioned/shadow fleet endres >2 % av relevant effektiv flåte
- 1-års TC/FFA endres >10 %
- faktisk amerikansk dieselrestriksjon eller annen større handelsregulering endrer product-flow vesentlig.

**Sluttproduktet ved «Oppdater modul» skal dermed være:** ny markedsstatus, endringer siden sist, oppdatert crude/product-balanse, supply/ton-mile, BBB-sannsynligheter og normaliserte TCE-baner for 2027–2029. Deretter blir dette den nye faste Shipping BBB-baselinen som selskapsanalysene bruker.

## Praktiske presiseringer for filversjonen

### Baseline og scenarioer

Bruk siste dokumenterte shippingbaseline, ikke den eldste versjonen i samtalen. Per 26. september 2026 var de strukturelle vektene **Bear 25 % / Base 50 % / Bull 25 %**. Den opprinnelige fordelingen 20/45/35 fra 19. september ble erstattet 22. september. Vektene er analyseforutsetninger som skal testes ved oppdatering, ikke permanente prosedyrekrav.

Importer oljescenarioenes premisser, men vurder shippingens egne sannsynligheter mot flåtevekst og transportbehov. Dokumenter sammenhengen dersom olje- og shippingvektene avviker. Skill alltid mellom dagens markedsregime og de strukturelle treårsscenarioene.

### Datakvalitet og kilder

- Oppgi direkte kildelenke, observasjonsdato, relevant publiseringsdato, enhet og eventuell forsinkelse.
- Skill observerte markedsdata, rapporterte selskapsrater, eksterne prognoser og egne modellforutsetninger.
- Bruk tilgjengelige primærkilder, eksempelvis Baltic Exchange, kanalmyndigheter, rederirapporter og offentlige handelsdata; suppler med etterprøvbare bransje- og nyhetskilder.
- Marker manglende eller motstridende data. Betalingsbegrensede spot-, FFA- eller flåtedata skal ikke erstattes med konstruerte observasjoner.
- Sammenlign like ruter, fartøytyper, måleenheter og måleperioder. Spot i Worldscale eller USD/tonn er ikke direkte sammenlignbart med TCE i USD/dag uten dokumentert omregning.
- Triggergrensene krever vurdering, ikke automatisk endring av BBB. Angi sammenligningsdato og datagrunnlag. For triggere uten fast angitt målevindu brukes forrige baseline, med tillegg av uke-/månedsendringer der relevante data finnes.
- Enkeltstående ekstremrater og diplomatiske signaler må knyttes til faktisk og varig transporteffekt før de endrer normaliserte ratebaner.

### Flåte, ton-mile og dobbelttelling

Originalens flåteformel er en forenklet huskeregel. For konsistent beregning skilles flåtenivå fra vekstrate:

- **Nominell flåte ved periodeslutt = startflåte + leveranser − skraping ± netto segmentoverføringer.**
- Beregn deretter effektiv kapasitet med dokumenterte justeringer for kommersiell tilgjengelighet, offhire, sanksjoner, geografisk plassering og faktisk clean/dirty-bruk.
- **Effektiv flåtevekst = effektiv kapasitet ved periodeslutt / effektiv kapasitet ved periodestart − 1.** Bruk sammenlignbare enheter og metode i begge perioder.
- Alder over 15/20 år er en indikator på tilgjengelighet, skrapingsrisiko og kundekrav; gamle skip trekkes ikke automatisk fra flåten.
- Unngå overlappende fradrag for samme fartøy, for eksempel både alder og sanksjoner.
- Dokumenter ekstra transportarbeid og bundne skipsdøgn. Samme omseiling eller ventetid skal ikke fullt ut telles både som økt etterspørsel og redusert kapasitet.
- Vis clean/dirty-overføringer konsistent på begge sider; en LR2 som skifter marked, skaper ikke et nytt skip.

### Fast resultatformat

Hvert oppdatert analysedokument skal inneholde:

1. **Metadata:** analyzedato, tidspunkt/tidssone, analyseår, forrige shippingbaseline, benyttet Oil Market BBB-baseline og lenke til denne prosedyren.
2. **Konklusjon:** om BBB beholdes eller endres, og de viktigste årsakene.
3. **Markedsstatus:** spot/TCE, faktiske slutninger og rapporterte selskapsrater for alle seks segmenter, sammenlignet med forrige baseline.
4. **Olje- og produktbalanse:** importerte forutsetninger fra Oil Market BBB og oversettelsen til lastevolumer og shippingetterspørsel.
5. **Handelsstrømmer og flaskehalser:** ton-mile, seilingsdøgn, venting, STS, regional tonnasje og alle definerte chokepoints.
6. **Flåtetilbud:** orderbook, leveringsprofil kommende 36 måneder, skraping, alder, sanksjoner og crossover per segment, med datamangler synliggjort.
7. **Raffinering og handelspolitikk:** endringer i kapasitet og eksportgeografi, med særskilt vurdering av produkttank.
8. **Forwardkontroll:** 1-års TC, 2–3 års perioderater, relevante FFA-er og skipsverdier.
9. **BBB-tabeller:** sannsynligheter og normalisert TCE for hvert segment og hvert analyseår i Bear, Base og Bull; ton-mile, effektiv flåtevekst og kapasitetsutnyttelse per scenario. Oppgi om vurderingene er kvantitative eller kvalitative. Vektene skal summere til 100 %.
10. **Triggerkontroll og modellbeslutning:** hvilke terskler som er passert, gammel og ny forutsetning og begrunnelsen for endring eller videreføring.
11. **Bruk i selskapsanalyser:** hvilke segmentforutsetninger som berører hvilke selskaper, med markedsrater som input til faktisk flåtemiks, kontraktsdekning og inntjeningsdager.
12. **Usikkerhet og endringslogg:** nytt, uendret, endret i BBB, manglende data, neste kontrollpunkter og ny baseline-dato.

Shipping BBB leverer markedsforutsetninger. Selskapsverdsettelsen gjennomføres separat under IAF med selskapets kostnader, investeringer, gjeld og antall aksjer.

### Lagringsregel

- Prosedyren lagres i `C:\GitWork\hsaether\Chatgpt\Finance\Module\Oil Shipping BBB.md`.
- Hvert analyseresultat lagres som eget Markdown-dokument i `C:\GitWork\hsaether\Chatgpt\Finance\Doc`.
- Standard filnavn: `Oil Shipping BBB - ÅÅÅÅ-MM-DD.md`, med analyzedato.
- Ved flere oppdateringer samme dag brukes `Oil Shipping BBB - ÅÅÅÅ-MM-DD - TTMM.md` med lokal tid Europe/Oslo; bruk sekunder ved behov for å unngå kollisjon. Bevar tidligere analyser.
- Nyeste fullførte, daterte analyse er gjeldende baseline. Bruk analyzedato og status i dokumentet, ikke filens endringstid. Et foreløpig utkast erstatter ikke en fullført baseline uten tydelig beslutning.
- Eksporterte historiske analyser beholder opprinnelig analyzedato og får eksportdato oppgitt separat.
- Kontroller etter lagring: fil finnes, innhold kan leses, norske tegn er korrekte, tabeller har alle segmenter/år/scenarioer, og lokale dokumentlenker virker.
- Bekreft filplasseringen og om BBB er endret eller beholdt etter hver kjøring.

## Endringslogg for prosedyren

| Dato | Endring |
|---|---|
| 2026-09-29 | Opprettet fra Shipping BBB. Bevarte siste tipunktsprosedyre og alle åtte rekalibreringstriggere. Dokumenterte lokal oppdateringskommando, lagring, resultatformat og presiseringer om datakvalitet og flåteberegning. Skrivetilgang kontrollert i Module og Doc. |

