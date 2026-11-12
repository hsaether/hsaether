# Defense Market BBB — 31 October 2026

## Metadata

- **Analysis date:** 31 Oct 2026 (Saturday), Europe/Oslo. Information cut-off 31 Oct 2026; latest
  market prints are the 30 Oct closes. **Status: Final** (update run; scheduled weekly run).
  Three standing weaknesses, unchanged since the initial baseline:
  - The European-supplier share is a Europe-level assumption `[A]`, low confidence.
  - The segment split is built from peer-group revenue and order data, not from an official
    series `[A]`.
  - The contract award log is still incomplete (extended in this run).
- **Skill revisions:** `defense-market-bbb` **2026-10-10.1** (the 7 Oct baseline was built under
  2026-10-07.3; the current method is applied). No other skill was used.
- **Previous baseline:** 7 Oct 2026 (24 days). Window: 2026 (current year, no spread) + 2027–2029;
  long end 2030 and 2035. **Stale after 4 Jan 2027** (the 90-day rule gives 29 Jan, but the window
  rolls with the first run in January: 2026 becomes realised and 2030 joins the grid), or earlier at
  a trigger. Triggers due inside the window: the Pentagon's Europe force-posture recommendation
  (6 Nov), the German 2027 budget (Bereinigungssitzung 12 Nov, plenary 24–27 Nov), US-brokered
  Ukraine talks (expected mid-November), the Bundestag decision on Arminius (9 Dec).
- **Triggers for this run:**
  - Upstream: Oil Market BBB changed on 17 Oct (read: 24 Oct version).
  - Passed events: UK Budget (28 Oct), Kongsberg Q3 (29 Oct), France PLF 2027 (8 Oct).
  - **Fired in this run:** fiscal stress, as the OAT–Bund 10-year spread widened by more than 50 bp
    in a month (99 bp on 21 Sep → 157.5 bp on 21 Oct; 174.6 bp close on 22 Oct). Budget
    presentations: France (8 Oct), UK (28 Oct), Netherlands (15 Sep), Finland, Poland (Sejm first
    reading 8 Oct).
- **Reference FX:** ECB reference rates, 7 Oct 2026, held fixed for the whole window (unchanged).
  EUR/USD 1.1177, EUR/GBP 0.84645, EUR/NOK 10.712, EUR/SEK 11.224, EUR/DKK 7.4745, EUR/PLN 4.3825,
  EUR/CZK 24.427, EUR/RON 5.3528, EUR/HUF 366.75. Albania and North Macedonia are converted via
  NATO's USD figures.
- **Anchor series:**
  - NATO "Defence Expenditure of NATO Countries (2014–2026)", Excel, published 7 Jul 2026. Core
    defence (3.5% guideline); 2025 and 2026 are estimates. No new edition (next: June/July 2027).
  - Paths are in **nominal % of GDP** (NATO T2 current ÷ T5). NATO's headline T3 is a share of
    real GDP; the two are identical for every row except the Netherlands (2026e: 2.29% nominal vs
    2.58% T3).
- **Europe total** = 28 European allies excl. Türkiye and Iceland. Türkiye 2026e: USD 47.6bn
  (memo).
- **Other baselines read:**
  - HY BBB, 24 Oct 2026 version; its Nordic GDP view is unchanged since 5 Oct (Norway mainland
    ~1.0%, Sweden 2.4% in 2027). Used for the NO/SE nominal GDP assumptions. No change.
  - Oil Market BBB, 24 Oct 2026 (kept unchanged on 24 Oct; last value change 17 Oct): Brent Base
    **88 / 77 / 72** (2027–29; was 85 / 77 / 72 on 4 Oct), Bear 65 / 60 / 60, Bull 118 / 102 / 90.
    Read only for the Gulf export row.
- **Oldest inputs:** NATO 2026e (7 Jul 2026); company H1 reports for peers without a Q3 yet
  (Rheinmetall, Hensoldt, Leonardo, BAE, Renk, CSG: Jul–Aug 2026).
- **Connectors and gaps:**
  - Yahoo returned all 14 peer quotes (30 Oct closes).
  - The Kongsberg Q3 release could not be fetched directly (not indexed). The Q3 figures come from
    `docs/kongsberg-analysis.md` version 2 (29 Oct), which read the report and its notes.
  - Yields are daily closes from press data tables (ideal-investisseur.fr for OAT and Bund; trade
    press for gilts). FRED monthly averages for October are not yet published.
  - The Edge browser connection was not used (scheduled-run rule).

## Conclusion

- **Defense Market BBB kept unchanged.** Every Bear, Base and Bull path is unchanged: spending
  (Europe total and each country), equipment and addressable spending, segment orders and revenue,
  long end, steady state and margins. Two things moved: the status of the Bear catalyst and
  several facts behind the paths.
  - **The Bear's fiscal half is now visible.** OAT–Bund crossed the 120 bp signpost on 1 Oct and
    reached 174.6 bp on 22 Oct (French 10-year 5.13%, highest since 2002); 159 bp on 30 Oct.
    Italy cut its planned defence add-on from €22bn to €14bn over 2027–28 and postponed frigates
    and armoured vehicles. Gilts touched 5.53% in early October (now 5.31%).
  - **But every funded defence line held in this budget round.** France's PLF 2027 matches the LPM
    (mission Défense €63.4bn). The UK Budget fully funded the Defence Investment Plan. Germany's
    2027 draft stands at €139.6bn with procurement above €60bn. Poland's 2027 draft is 4.51% of
    GDP. Base already sits below the plans of France, Italy, Spain and the UK.
  - **The Bear's ceasefire half is absent.** There is no comprehensive ceasefire, only a local
    truce in Oleshky (27–31 Oct). A new US-brokered round is expected in mid-November, with the
    two sides still far apart.
  - **Orders ran ahead in Q3:** Kongsberg book-to-bill 2.06, Saab 3.2x (Gripen E for Ukraine,
    GlobalEye, German frigate systems), Airbus Defence and Space 9M orders +70%, Thales Defence
    +14%. This is inside the 2026 current-year assumptions and the orders-index ranges.
- **Base: spending.** European core defense spending rises from €575bn (2.56% of GDP) in 2026 to
  €720bn (2.88%) in 2029 and €974bn (3.16%) in 2035. That is below the 3.5% pledge, because
  France, Italy, Spain and the UK fund less than they pledged; Germany carries a third of the
  increase.
- **Base: equipment.** Equipment spending grows 8.5% a year to €252bn in 2029. The share open to
  European suppliers grows 10.7% a year to €174bn.
- **Base: industry.** Revenue grows faster than orders. The 2024–26 order surge turns into revenue
  under capacity limits, so peer book-to-bill falls from 1.0–3.2x in 2026 to about 1.0–1.5x by
  2029. After 2030, growth fades to 2–6% a year as the equipment share falls back.
- **Segment ranking (strongest → weakest), unchanged:**
  1. **Air and missile defense and missiles.** The Iran war drained US interceptor stocks (3–8
     years to replenish `[E]`); drones and NATO capability targets add demand; capacity is
     binding. SAFE round 2 names air and missile defence first.
  2. **Land.** Backlog of 5–7 years.
  3. **C4ISR and space.** Sensors and electronics are pulled along by air defense.
  4. **Naval.** Orders far ahead of yard capacity; slow conversion.
  5. **Combat air.** The F-35 takes much of the new-fighter money.
  6. **Ammunition.** Weakest after 2027: about 2m shells/yr of European 155 mm capacity by 2027
     `[E]` meets demand that peaks with the stockpile rebuild; today's 24% margins are scarcity
     margins.
- **Main Bear catalyst:** a Ukraine ceasefire combined with fiscal stress. The fiscal half is now
  present (France first, then Italy and the UK); the ceasefire half is not. The rows most exposed
  are France 2028–30 (presidential election April–May 2027), Italy and, in the segments,
  ammunition and Ukraine-related orders.
- **Main Bull catalyst:** a US drawdown from Europe together with further Russian pressure on NATO
  territory. The Pentagon's recommendation reaches Hegseth on **6 Nov** (25,000–40,000 of ~80,000
  troops); the 2026 defense bill slows any cut below 76,000.
- **Market signal (context, not an input):** peers rebounded since 7 Oct (median about +11%;
  Kongsberg +20%, TKMS +19%, Saab +14%, Rheinmetall +12%). They are still 3–59% below their
  52-week highs. The pre-mortem's main risk to Base stays conversion (cash, margins, programme
  cuts), now joined by fiscal stretch in France and Italy.

## Interface — core defense spending (EUR bn, fixed FX; Bear / Base / Bull)

All values unchanged from 7 Oct 2026.

| Row | 2026 | 2027 | 2028 | 2029 | 2030 | 2035 | Target (year) |
|---|---|---|---|---|---|---|---|
| **Europe total** | 575 | 606 / 632 / 654 | 629 / 678 / 722 | 653 / 720 / 783 | 676 / 760 / 838 | 829 / 974 / 1,136 | 3.5% core by 2035 (NATO) |
| Germany | 125 | 140 / 148 / 156 | 150 / 163 / 175 | 160 / 177 / 192 | 165 / 190 / 204 | 186 / 217 / 236 | 3.5% by 2029 |
| France | 68 | 71 / 74 / 75 | 73 / 78 / 82 | 75 / 82 / 87 | 77 / 86 / 92 | 96 / 116 / 139 | LPM to 2030; 3.5% by 2035 |
| United Kingdom | 96 | 101 / 103 / 105 | 105 / 109 / 113 | 109 / 113 / 121 | 113 / 119 / 130 | 146 / 167 / 183 | 2.7% to 2029-30; 3% by 2030 (unfunded); 3.5% by 2035 |
| Italy | 48 | 50 / 52 / 53 | 52 / 56 / 60 | 54 / 60 / 65 | 55 / 63 / 69 | 68 / 83 / 103 | 2.5% by 2028; 3.5% by 2035 |
| Poland | 44 | 43 / 45 / 47 | 42 / 48 / 51 | 43 / 50 / 54 | 44 / 51 / 57 | 56 / 64 / 80 | ≈4.5–4.8% |
| Spain | 35 | 37 / 38 / 39 | 38 / 40 / 44 | 39 / 42 / 50 | 40 / 44 / 54 | 48 / 53 / 88 | 2.1% cap |
| Netherlands | 28 | 30 / 31 / 33 | 31 / 34 / 37 | 33 / 37 / 41 | 35 / 40 / 45 | 46 / 55 / 58 | 3.5% by 2035 |
| Norway | 17.4 | 17.6 / 17.9 / 18.2 | 17.1 / 18.5 / 19.4 | 16.9 / 19.2 / 20.4 | 16.6 / 19.6 / 21.4 | 19.7 / 22.9 / 24.9 | 3.5% core by 2035 |
| Sweden | 19.4 | 20.1 / 20.7 / 21.3 | 20.9 / 22.2 / 23.1 | 21.7 / 23.4 / 25.1 | 22.6 / 24.7 / 26.8 | 27.5 / 30.9 / 34.3 | 3.5% by 2030 |
| Denmark | 14.9 | 15.4 / 16.3 / 17.6 | 15.0 / 16.4 / 17.8 | 15.0 / 16.9 / 17.9 | 15.5 / 17.0 / 18.5 | 18.3 / 20.0 / 21.7 | 3.5% by 2030 |
| Finland | 7.7 | 7.7 / 8.0 / 8.3 | 8.0 / 8.6 / 9.2 | 8.5 / 9.5 / 10.1 | 8.8 / 9.8 / 10.7 | 11.3 / 13.2 / 13.6 | ≥3% by 2029 |
| Baltics | 9.3 | 8.6 / 9.7 / 10.1 | 8.6 / 10.2 / 10.8 | 8.6 / 10.6 / 11.2 | 8.5 / 10.9 / 11.8 | 10.1 / 13.3 / 14.6 | 5%+ |
| Rest of NATO Europe | 63 | 66 / 68 / 71 | 68 / 74 / 80 | 71 / 80 / 88 | 74 / 85 / 97 | 96 / 120 / 140 | 3.5% by 2035 (pledges) |

**Same rows as % of nominal GDP (Bear / Base / Bull):**

| Row | 2026 | 2027 | 2028 | 2029 | 2030 | 2035 |
|---|---|---|---|---|---|---|
| **Europe total** | 2.56 | 2.60 / 2.71 / 2.81 | 2.61 / 2.81 / 2.99 | 2.61 / 2.88 / 3.13 | 2.61 / 2.93 / 3.24 | 2.69 / 3.16 / 3.68 |
| Germany | 2.69 | 2.92 / 3.10 / 3.26 | 3.03 / 3.30 / 3.54 | 3.13 / 3.47 / 3.76 | 3.13 / 3.60 / 3.88 | 3.00 / 3.50 / 3.80 |
| France | 2.22 | 2.26 / 2.36 / 2.39 | 2.26 / 2.41 / 2.54 | 2.25 / 2.46 / 2.61 | 2.25 / 2.49 / 2.68 | 2.40 / 2.90 / 3.50 |
| United Kingdom | 2.56 | 2.60 / 2.65 / 2.70 | 2.60 / 2.70 / 2.80 | 2.60 / 2.70 / 2.90 | 2.60 / 2.75 / 3.00 | 2.80 / 3.20 / 3.50 |
| Italy | 2.10 | 2.10 / 2.20 / 2.25 | 2.12 / 2.30 / 2.45 | 2.15 / 2.40 / 2.60 | 2.15 / 2.45 / 2.70 | 2.30 / 2.80 / 3.50 |
| Poland | 4.68 | 4.30 / 4.50 / 4.70 | 4.00 / 4.50 / 4.80 | 3.80 / 4.40 / 4.80 | 3.70 / 4.30 / 4.80 | 3.50 / 4.00 / 5.00 |
| Spain | 2.00 | 2.00 / 2.05 / 2.10 | 2.00 / 2.10 / 2.30 | 1.95 / 2.10 / 2.50 | 1.95 / 2.10 / 2.60 | 1.90 / 2.10 / 3.50 |
| Netherlands | 2.29 | 2.35 / 2.45 / 2.60 | 2.40 / 2.60 / 2.85 | 2.45 / 2.75 / 3.05 | 2.50 / 2.85 / 3.20 | 2.80 / 3.30 / 3.50 |
| Norway | 3.17 | 3.15 / 3.20 / 3.25 | 3.00 / 3.25 / 3.40 | 2.90 / 3.30 / 3.50 | 2.80 / 3.30 / 3.60 | 3.00 / 3.50 / 3.80 |
| Sweden | 3.22 | 3.20 / 3.30 / 3.40 | 3.20 / 3.40 / 3.55 | 3.20 / 3.45 / 3.70 | 3.20 / 3.50 / 3.80 | 3.20 / 3.60 / 4.00 |
| Denmark | 3.49 | 3.50 / 3.70 / 4.00 | 3.30 / 3.60 / 3.90 | 3.20 / 3.60 / 3.80 | 3.20 / 3.50 / 3.80 | 3.20 / 3.50 / 3.80 |
| Finland | 2.65 | 2.60 / 2.70 / 2.80 | 2.60 / 2.80 / 3.00 | 2.70 / 3.00 / 3.20 | 2.70 / 3.00 / 3.30 | 3.00 / 3.50 / 3.60 |
| Baltics | 5.17 | 4.60 / 5.20 / 5.40 | 4.40 / 5.20 / 5.50 | 4.20 / 5.20 / 5.50 | 4.00 / 5.10 / 5.50 | 3.80 / 5.00 / 5.50 |
| Rest of NATO Europe | 2.24 | 2.25 / 2.35 / 2.45 | 2.25 / 2.45 / 2.65 | 2.25 / 2.55 / 2.80 | 2.25 / 2.60 / 2.95 | 2.40 / 3.00 / 3.50 |

- **Status of the figures:**
  - 2026 = NATO 2026e `[F]` (an estimate by the allies; it will be revised in the 2027 edition).
  - 2027–2035 = own paths `[A]` built from the budgets and plans in the Spending tracker. Nominal
    GDP growth `[A]`:
    - DE 3.3%, FR 3.0%, UK 3.8%, IT 2.8%, PL 6.0%, ES 4.0%, NL 3.5%
    - NO 2.0% (petroleum output falls in 2028–29), SE 4.0%, DK 3.3%, FI 3.0%
    - Baltics 4.5%, Rest 4.0%
- **Ranges inside each scenario (country rows):** ±3% (2027), ±5% (2028), ±7% (2029), ±10%
  (2030), ±15% (2035). For the Europe total, use about two-thirds of those widths. **France
  2028–30 and Italy:** the risk inside the Base range is now skewed to the lower half (fiscal
  stress, French presidential election 2027, Italy's cut add-on); the point is kept because the
  2027 budgets held (see Spending tracker).
- **Bear still grows in nominal terms** (+4.3% a year 2026–29), because Germany's exemption and
  most frontline plans are legally or politically locked. The Bear tail sits in equipment and in
  the European share (next table), not in total spending.

## Interface — equipment and addressable spending, Europe total (EUR bn; Bear / Base / Bull)

All values unchanged from 7 Oct 2026.

| Line | 2026 | 2027 | 2028 | 2029 | 2030 | 2035 |
|---|---|---|---|---|---|---|
| Equipment share % | 34.3 | 33.0 / 34.5 / 35.5 | 31.5 / 35.0 / 36.5 | 30.5 / 35.0 / 37.0 | 30.0 / 34.5 / 37.0 | 26.0 / 30.0 / 33.0 |
| Equipment spending | 197 | 200 / 218 / 232 | 198 / 237 / 264 | 199 / 252 / 290 | 203 / 262 / 310 | 215 / 292 / 375 |
| European-supplier share % | 65 | 64 / 66 / 67 | 62 / 68 / 70 | 61 / 69 / 72 | 60 / 70 / 74 | 60 / 72 / 78 |
| **Addressable spending** | **128** | 128 / 144 / 156 | 123 / 161 / 185 | 122 / 174 / 209 | 122 / 183 / 229 | 129 / 210 / 292 |

| Growth, % a year | Bear | Base | Bull |
|---|---|---|---|
| Equipment CAGR 2026–29 | 0.3 | 8.5 | 13.7 |
| Addressable CAGR 2026–29 | −1.8 | 10.7 | 17.6 |
| Equipment CAGR 2030–35 | 1.2 | 2.2 | 3.9 |
| Addressable CAGR 2030–35 | 1.2 | 2.8 | 5.0 |

- **Equipment share:** 2026e 34.3% `[F]` (2014: 17.8%; 3-year average 2024–26: 31.4%). Paths `[A]`;
  range ±1.5 pp.
  - Base holds about 35% through 2029, carried by funded procurement plans. They include Germany's
    25-Mio-Vorlagen flow and **military procurement of more than €60bn in the 2027 draft (2026:
    €45bn)** `[F]`, Poland at 56%, UK munitions and drones, and **the UK's capital budget +18% in
    2027-28 against −2% day-to-day** `[F]`. France's programmes à effet majeur rise 24% to €17.2bn
    in 2027 `[F]`. The share falls back to 30% by 2035 as personnel growth (conscription,
    Bundeswehr expansion) and sustainment take over.
  - Bear cuts procurement first, since it is the flexible line under fiscal stress. Italy did this
    in October: frigates, armoured vehicles, drone plants and satellite communications were
    postponed, while GCAP (€8.8bn) was protected `[E]`.
  - These moves are below the 2 pp minimum at Europe level, so the paths are kept.
- **European-supplier share:** 65% in 2026 is a Europe-level assumption `[A]`, low confidence, range
  55–75%.
  - Germany's plan sends about 8% to US suppliers `[E]` and France very little. Poland, Finland,
    Norway, the Netherlands, Romania, Greece and Czechia carry large F-35, Patriot, HIMARS and
    Korean programmes.
  - Non-European buys found in this run are all small: Sweden HIMARS SEK 7bn (FMS, 7 Sep), Spain
    128 K9 howitzers (Hanwha, early Sep; single source `[?]`), Croatia 18 Chunmoo launchers
    (Hanwha, 8 Sep). Nothing above €5bn.
  - SIPRI 2021–25: the US supplied 58% of European NATO imports `[F]`, but imports are only part of
    equipment spending. An IRIS study of the Feb 2022–Jun 2023 emergency buys found 78% outside the
    EU `[E]`, which was a crisis period and excluded UK/NO suppliers.
  - What pushes the share up in Base: SAFE's 65% EU/EEA/Ukraine component rule `[F]` (round 2 adds
    joint procurement with Ukraine), EDIP, and US supply limits after the Iran war. Bear is US
    trade pressure to "buy American".
- **Addressable vs industry:** industry also sells into operations and maintenance (ammunition,
  spares, MRO) and exports outside Europe. Peer revenue (≈€150bn in 2026 `[A]`) can therefore
  exceed addressable spending (€128bn).
- **EU-level line (not in national figures):** EDIP €1.47bn for 2026–27 `[F]`; EDF; the MFF
  2028–34 proposal of €131bn for defence and space `[E]`, still under negotiation. This is below
  0.5% of the Europe total, so it is a memo only. SAFE loans finance national spending already
  counted (Data discipline), so SAFE round 2 adds no demand of its own.

## Interface — segments (Bear / Base / Bull)

All values unchanged from 7 Oct 2026.

Revenue = revenue of European suppliers in the segment (peer group) from all customers.
Orders = firm order intake, index 2026 = 100. 2026 is the same in all scenarios (current-year
growth from H1 and Q3 actuals and guidance).

| Segment | Scenario | Orders 2027 / 28 / 29 (2026 = 100) | Revenue growth 2027 / 28 / 29 % | Revenue CAGR 26–29 % | CAGR 30–35 % | Steady-state EBIT % |
|---|---|---|---|---|---|---|
| **Land systems** (2026: +20%) | Bear | 70 / 60 / 55 | 12 / 5 / −2 | 4.8 | 1 | 8 |
| | Base | 90 / 85 / 85 | 18 / 14 / 10 | 14.0 | 3 | 10 |
| | Bull | 105 / 105 / 100 | 22 / 18 / 14 | 18.0 | 4 | 12 |
| **Ammunition and energetics** (2026: +25%) | Bear | 55 / 45 / 45 | 5 / −10 / −15 | −7.0 | −3 | 10 |
| | Base | 85 / 75 / 70 | 15 / 5 / 0 | 6.5 | −2 | 14 |
| | Bull | 105 / 100 / 95 | 22 / 15 / 8 | 14.9 | 0 | 18 |
| **Air and missile defense and missiles** (2026: +35%) | Bear | 85 / 75 / 75 | 15 / 8 / 4 | 8.9 | 3 | 12 |
| | Base | 110 / 110 / 105 | 25 / 18 / 14 | 18.9 | 6 | 15 |
| | Bull | 125 / 130 / 125 | 30 / 25 / 20 | 24.9 | 8 | 17 |
| **Combat air and aerostructures** (2026: +10%) | Bear | 80 / 75 / 70 | 6 / 3 / 2 | 3.7 | 3 | 7 |
| | Base | 100 / 100 / 100 | 10 / 9 / 8 | 9.0 | 5 | 9 |
| | Bull | 115 / 115 / 110 | 12 / 12 / 10 | 11.3 | 6 | 10 |
| **Naval** (2026: +8%) | Bear | 60 / 55 / 55 | 6 / 5 / 4 | 5.0 | 4 | 5 |
| | Base | 85 / 90 / 90 | 9 / 10 / 10 | 9.7 | 7 | 7 |
| | Bull | 100 / 110 / 110 | 10 / 12 / 13 | 11.7 | 8 | 8 |
| **C4ISR, electronics and space** (2026: +15%) | Bear | 75 / 70 / 70 | 8 / 4 / 2 | 4.6 | 3 | 10 |
| | Base | 100 / 100 / 100 | 14 / 12 / 10 | 12.0 | 5 | 12 |
| | Bull | 115 / 120 / 120 | 18 / 16 / 13 | 15.6 | 6 | 13 |
| Uncrewed and counter-drone (secondary) | Base | — (lumpy, small base) | 40 / 35 / 30 | 35 | 12 | `[?]` |
| Services, MRO and training (secondary) | Base | — | 6 / 6 / 6 | 6 | 4 | 8 |

- **Weighted peer revenue growth**, using 2026 European-supplier revenue weights `[A]` (land 18,
  ammunition 14, air and missile defense 15, combat air 31, naval 20, C4ISR 26; €bn):

| | 2027 | 2028 | 2029 | CAGR 2026–29 |
|---|---|---|---|---|
| Bear | 8.3% | 3.0% | 0.1% | 3.7% |
| Base | 14.2% | 11.2% | 8.9% | 11.4% |
| Bull | 17.7% | 15.6% | 12.7% | 15.3% |

  Base revenue (11.4%) runs slightly ahead of addressable spending (10.7%) because 2024–26
  backlogs are converted.
  - In Bear, revenue holds up through 2027 on backlog while orders fall 25–45%.
  - In Bull, capacity caps revenue below addressable growth (17.6%). The gain shows in longer
    backlogs and in margins.
- **Ranges:** ±4 pp per year on revenue growth (±6 pp for air and missile defense and for
  ammunition); ±15 points on the orders index; ±2 pp on steady-state EBIT.
- **Steady-state EBIT** is set below today's scarcity margins (ammunition 24%, CSG Defence
  Systems 29%). It sits close to the pre-2022 levels for each segment plus a modest premium for
  larger volumes `[A]`.
- **Current-year check (2026, Q3 data):** air and missile defense +35% vs Kongsberg 9M revenue +36%
  `[F]`; C4ISR +15% vs Thales Defence 9M sales +13% `[F]`; group-level Saab Q3 organic +30.6% `[F]`.
  No 2026 row needs a change. Q3 orders were strong in air defense, combat air and naval, which
  lifts the 2026 order base: if anything, the 2027 orders index (2026 = 100) is at risk of being
  too high, not too low. It stays inside the ±15 point range, so it is kept.

## Scenario definitions

| Scenario | Weight (convention) | Policy regime | Catalyst(s) | Mechanism | Earliest | Signposts |
|---|---|---|---|---|---|---|
| Bear | 25% | Ceasefire in Ukraine; markets punish deficits; US pushes "buy American" | **Ukraine ceasefire + fiscal stress** (FR, IT, UK, BE); US trade pressure; execution failures (F126-type cancellations); ammunition overcapacity | Later plan years stretched; procurement cut first (equipment share 34% → 30% by 2029); European share falls to ~61%; ammunition and Ukraine-related orders collapse; backlog cushions revenue to 2027 | 2027 budgets (decided H2 2026–H1 2027); France 2028 budget after the 2027 presidential election | Ceasefire signed (not met); **OAT–Bund > 120 bp (crossed 1 Oct; 159 bp on 30 Oct)**; gilt 10y > 5.5% (touched 5.53% early Oct; 5.31% on 28 Oct); PLF 2027 Défense < €60bn (not met: €63.4bn); next level: OAT–Bund > 200 bp or a Moody's downgrade of France (Aa3 negative, held 23 Oct); mission Défense cut in parliament or an LFR; Italy cuts again; big US buy > €5bn; peer book-to-bill < 1.0 for two quarters; shell price cuts |
| Base | 50% | War continues or freezes without settlement; Russian threat assessment unchanged; US partially draws down; EU instruments as agreed | Funded national plans executed with haircuts (DE 95%; FR LPM slips one year; IT, ES, UK below pledges) | Europe 2.9% of GDP by 2029, 3.2% by 2035; equipment share ~35% to 2029; European share rises to ~69% | — | German 2027 budget adopted ≥ draft (12 Nov / 24–27 Nov); PLF 2027 Défense ≈ €63bn (met: €63.4bn); UK DIP funded (met, 28 Oct); NATO 2027e Europe ≥ 2.7% |
| Bull | 25% | US drawdown of 25,000+ troops; Russian challenge to NATO territory; more common EU money | **US drawdown + Russian escalation**; SAFE 2 or defence Eurobonds; MFF €131bn window adopted; Spain changes government | Faster ramp-up (Europe 3.1% of GDP by 2029, 3.7% by 2035); Europe replaces US enablers; European share 72% by 2029; capacity caps revenue, so margins and backlogs rise | 6 Nov 2026 (Pentagon recommendation to Hegseth) | Pentagon decision ≥ 25k troops; incident with casualties on NATO territory; new EU borrowing for defence (SAFE round 2 is the existing envelope, not new money); Spanish election (by Aug 2027) |

- **Ceasefire ≠ peace dividend:** European plans rest on the assessed Russian threat, not on the
  war itself. The Bear therefore needs fiscal stress or US pressure on top of a ceasefire.
- **Status of the Bear (31 Oct):** half of it is in place. Fiscal stress is visible in France
  (OAT–Bund 159 bp) and Italy (defence add-on cut), and gilts are near their signpost. No
  ceasefire is in sight. So far the stress has hit Italian procurement timing, not any funded
  national total. **The Bear paths and weights are unchanged.**
- **Ukraine after a ceasefire can be Bull:** an EU-financed rebuild of Ukraine's army (land,
  ammunition, air defense) is treated as a Bull element, not as offsetting the Bear. The Gripen E
  order for Ukraine (SEK 24.6bn, reportedly financed through the EU Ukraine Support Loan) is an
  early example of EU money buying European equipment for Ukraine.
- **Long-end tail (all scenarios):** a procurement holiday after the build-up.
  - SIPRI: Central and Western European real spending fell 22% from 1989 to 1996–98 and stayed
    flat until 2014 `[F]`.
  - US real spending fell 31% from 1989 to 1998 `[F]`. Procurement fell more than total spending.
  - The Bear 2035 equipment share (26%) reflects that pattern, although the 1990s followed the
    disappearance of the threat, which is not the case today.

## Spending tracker

| Country | Target (% GDP, year) | NATO 2025e / 2026e % GDP | Equipment share 3-yr (2026e) | Budget 2026 | Draft 2027 | Plan to [year] | Credibility | Base 2029 (% GDP / €bn) | Change vs previous |
|---|---|---|---|---|---|---|---|---|---|
| Germany | 3.5% by 2029; 3.5% core 2035 | 2.22 / 2.69 | 26.2 (32.1) | EP14 €82.7bn + Sondervermögen €25.5bn = €108.2bn `[F]` | **EP14 €109.7bn + SV €29.9bn = €139.6bn** (Bundestag, first reading 9 Sep) `[F]`; procurement > €60bn (2026: €45bn); Bereinigungssitzung 12 Nov, plenary 24–27 Nov | Finanzplan EP14 €153.9bn (2028), €169.9bn (2029), €180–184bn (2030) `[E]` | **A** — debt-brake exemption for defence above 1% of GDP (€85.4bn exempt in 2027) | 3.47 / 177 | Unchanged (2027 total reconciled) |
| France | LPM to 2030; 3.5% by 2035 | 2.04 / 2.22 | 30.9 (34.1) | Mission Défense €56.9–57.1bn `[F]` | **PLF 8 Oct: €63.4bn excl. pensions (+€6.5bn, +11.4%) = LPM** `[F]`; programmes à effet majeur €17.2bn (+24%); SAFE €15.1bn (36 projects, signed June) | LPM update (law 16 Aug 2026): €69.5bn / €72.6bn / €75.7bn (2028–30); +€36bn 2026–30; €435.7bn 2024–30 `[F]` | **B** — law in place and 2027 funded; OAT–Bund 159 bp; Moody's Aa3 negative; presidential election Apr–May 2027 | 2.46 / 82 | Unchanged (risk to 2028–30 skewed down) |
| United Kingdom | 2.6% 2026-27 → 2.7% to 2029-30; **3% by 2030** (unfunded); 3.5% 2035 | 2.32 / 2.56 | 35.6 (37.2) | MoD £68.3bn (2026-27) `[F]` | £73.8bn (2027-28) `[F]`; **Budget 28 Oct: DIP fully funded** (last £4.7bn from Whitehall capital, already inside the £298bn); MoD capital +18%, day-to-day −2% (2027-28) `[F]` | DIP (30 Jun 2026): £76.5bn / £79.1bn (2028-29, 2029-30); £298bn over four years `[F]`; path to 3% and 3.5% set at the 2027 Spending Review | **B** to 2.7% (now fully funded); **C** for 3% by 2030 and beyond | 2.70 / 113 | Unchanged |
| Italy | 2.5% by 2028; 3.5% 2035 | 2.09 / 2.10 | 23.8 (24.4) | MoD ordinary ≈ €31.3bn (2025) `[E]` | Budget law (Oct): **+€7bn a year in 2027 and 2028** (0.3% of GDP; €11bn a year planned) `[E]`; frigates, armoured vehicles, drone plants postponed; GCAP protected | +0.15 / +0.15 / +0.2 pp GDP (2026–28) `[E]`; SAFE **€8.9bn** requested (of €14.9bn) `[F]`; NATO-basis 2027 level not derivable `[?]` | **C** — 2026 step missed; add-on cut by €8bn | 2.40 / 60 | Unchanged (evidence conflicts: direction down vs plan, level not clear) |
| Poland | ≈4.5–4.8% | 4.25 / 4.68 | 49.8 (55.9) | PLN 200bn (4.8%; MON + FWSZ) `[F]` | **PLN 198.1bn (4.51%)** `[F]`; Sejm second/third reading 2/4 Dec, Senate 8 Dec | SAFE €43.7bn signed 8 May (€6.56bn pre-financing) `[F]`; deficit 7.1% of GDP (2027 draft) | **A** for ≈4.5%; fiscal risk | 4.40 / 50 | Unchanged |
| Spain | 2.1% cap (opt-out from 3.5%) | 2.00 / 2.00 | 36.2 (34.0) | €35.4bn (2.0%) `[F]` | `[?]` (budget extensions) | — | **D** beyond 2.1% | 2.10 / 42 | Unchanged |
| Netherlands | 3.5% by 2035 | 2.24 / 2.29 (T3: 2.53 / 2.58) | 25.5 (33.7) | €26.8bn (Dutch definition) `[E]` | **€28.9bn** (Prinsjesdag 15 Sep; materiel fund €14.1bn, 49%) + Ukraine aid > €3bn `[F]` | New coalition agreement centred on defence `[E]` | **B** | 2.75 / 37 | Unchanged |
| Norway | 3.5% core by 2035 | 3.16 / 3.17 | 24.3 (17.9) | ≈ NOK 112bn excl. Ukraine `[F]` | 7 Oct: NOK 191.7bn incl. Ukraine; NOK 123bn excl. (+NOK 6.5bn real) `[F]`; Storting vote in December | Long-term plan 2025–36 + NOK 115bn to 2036 (31bn by 2030) `[F]`; Nansen ≥ NOK 344bn 2023–30 | **A** | 3.30 / 19.2 | Unchanged |
| Sweden | 3.5% by 2030 | 2.85 / 3.22 | 26.8 (25.4) | `[?]` | Military defence SEK 148bn (≈2.8%, Swedish measure) `[E]` | SEK 175bn military defence in 2030 `[E]` | **A–B** — the left bloc won the 13 Sep election by one seat; Kristersson resigned; new government's 2027 figures not found `[?]` | 3.45 / 23.4 | Unchanged |
| Denmark | 3.5% by 2030 | 3.27 / 3.49 | 31.2 (34.7) | Incl. Ukraine Fund `[F]` | +DKK 21bn `[E]` | Acceleration fund DKK 120bn + DKK 42.7bn (Oct 2025) `[F]`; +DKK 260bn 2026–33 `[E]` | **A** | 3.60 / 16.9 | Unchanged |
| Finland | ≥3% by 2029; 3.5% core 2035 | 2.75 / 2.65 | 40.8 (36.7) | `[?]` | **MoD €7.0bn (+€0.6bn; 2.6% of GDP, national measure)** `[E]`; materiel €1.3–1.8bn (sources differ), F-35 €1.4bn | +€0.6bn (2028), +€3.0bn (2029) vs earlier level; F-35 ≈ €1.5bn/yr → €0.4bn 2029–30 `[E]` | **B** (back-loaded to the next parliament) | 3.00 / 9.5 | Unchanged |
| Baltics | 5%+ | 3.91 / 5.17 | 38.3 (44.0) | — | — | SAFE: LT €6.4bn, LV €3.5bn, EE €2.3bn `[F]` | **A** | 5.20 / 10.6 | Unchanged |
| Rest of NATO Europe | 3.5% by 2035 (pledges) | 2.08 / 2.24 | 29.6 (32.5) | — | — | SAFE: RO €16.7bn, BE €8.3bn, PT €5.8bn, HU €5.4bn, BG €3.3bn, CZ €2.1bn, HR €1.7bn, GR €0.8bn `[F]` | **C** (CZ may fall below 2% `[E]`; GR already 3.65%) | 2.55 / 80 | Unchanged |

- **Why no country path moved** (minimum change: 3% of a country's annual spending or 0.1 pp of
  GDP):
  - Germany: the reconciled 2027 total (€139.6bn vs the earlier €133.3–137.2bn) adds ≈€2bn after
    the 95% haircut, about +1.5% on the NATO-basis Base (€148bn). Below the threshold.
  - France: PLF 2027 ×1.18 (pensions and other NATO items) ≈ €74.8bn vs Base €74bn (+1%).
  - Poland 4.51% vs Base 4.50%.
  - Netherlands: the national budget rises 8% (€26.8bn → €28.9bn), with Ukraine aid > €3bn on
    top. Applied to NATO's 2026e (€28bn), that points to about €30–32bn, the Base 2027 range
    (€31bn ±3%). The Dutch and NATO definitions differ, so the point is not moved.
  - Finland: +€0.6bn on the NATO 2026e €7.7bn gives ≈ €8.3bn vs Base €8.0bn (+3.5%), but the
    €7.0bn is the national MoD measure, not NATO's. Not applied until the definitions are
    reconciled (checkpoint 4).
  - UK: the 3% by 2030 date is a target without funding (grade C). Base 2030 at 2.75% already
    leans towards it; Bull carries 3.0%.
  - Italy: the 22 → 14bn cut points down against the plan, but +€7bn a year on the 2026 level
    would sit above Base. Meloni's 2.8% for "defence and security" includes 0.71 pp of security
    `[E]`. The two readings conflict, so Base stays and the row is flagged.
- **Source cross-check, 2025, current USD bn (NATO 2025e vs SIPRI 2025):** unchanged (no new
  editions).

| Country | NATO | SIPRI | Gap | Note |
|---|---|---|---|---|
| Germany | 112.1 | 113.6 | +1% | |
| United Kingdom | 92.9 | 89.0 | −4% | |
| France | 68.9 | 68.0 | −1% | |
| Italy | 53.3 | 48.1 | **−10%** | Italy's 2025 NATO jump from 1.52% to 2.09% includes reclassified items `[E]` |
| Poland | 44.2 | 46.8 | +6% | |
| Spain | 38.1 | 40.2 | +6% | |
| Netherlands | 29.8 | 28.9 | −3% | |
| Norway | 16.8 | 17.0 | +1% | |
| Sweden | 19.1 | 16.5 | **−14%** | Likely Ukraine aid and civil items in the NATO figure `[?]` |
| Denmark | 15.1 | 14.9 | −1% | |
| Finland | 8.7 | 8.1 | −7% | |

- **EDA vs NATO:** EDA's EU27 2025 total of €418bn `[F]` vs the NATO EU members ≈ €405bn plus
  non-NATO EU members ≈ €6–7bn (at today's FX), so −2%. Consistent.
- **COFOG vs NATO, 2024** (delivery basis vs payment basis): EU27 1.5% vs ≈ 2.0% of GDP;
  DE 1.4% vs 2.00%; FR 1.9% vs 2.04%; PL 2.9% vs 3.75%. The largest gaps (DE, PL) fit large
  prepayments and pending deliveries, plus pensions outside COFOG GF02. Use as a direction only.
- **National vs NATO, Italy:** the official accounts show €35.5bn for 2025 (of which €7.7bn
  disbursed for materiel) against ≈ €47bn in NATO's count `[E]` (L'Espresso, 13 Oct). The gap is
  the reclassification noted above.
- **Forecast vs actual:** none yet (2026 is not realised). NATO's 2025e and 2026e estimates are
  revised in the 2027 edition.

## Market check

Peer group: listed European defense companies plus KNDS and MBDA. Latest reported period: Q3 2026
where reported (Kongsberg 29 Oct, Saab 23 Oct, Thales 22 Oct, Airbus 28 Oct), otherwise H1 or Q2
2026 (`[F]` from company releases unless tagged). Rheinmetall, Hensoldt and Renk report on 5 Nov.

| Segment | Peer order intake LTM (B2B) | Firm backlog / revenue | Revenue growth (latest) | EBIT % (latest) | Capacity balance |
|---|---|---|---|---|---|
| Land systems | Rheinmetall Vehicle Systems nomination €6.7bn H1 (2.8x, incl. frames); Renk 1.9x (H1) | RHM VS €28.8bn ≈ 6 yr; KNDS €33.1bn ≈ 7.5 yr (end-2025) | RHM VS +28% (H1); KNDS +16% (2025); Renk +3% (H1) | RHM VS 11.3%; Renk 15.4% (adj.) | **Shortage**: KNDS in capacity talks with Mercedes/VW plants `[E]` |
| Ammunition and energetics | RHM W&A €3.1bn H1 (1.8x); CSG backlog +15% YTD; RHM artillery order €444m (~21 Oct; grade C) | RHM W&A €25.3bn ≈ 7 yr (incl. frames); CSG €17bn; Chemring £1.4bn | RHM W&A +33%; CSG +17%; Chemring +6.5% | RHM W&A 23.7%; CSG 24.1% (DS 28.8%) | **Tight now → surplus risk from ~2028**: ≈2m shells/yr Europe by 2027 `[E]`; delivered rounds lag announced ceilings (Unterlüß: low five-figure first batch in Jul 2026) `[E]`; no price cuts found |
| Air and missile defense and missiles | **Kongsberg Q3 2.06x (9M 2.16x)**: NASAMS Belgium NOK 9.8bn, Netherlands NOK 1.5bn; RHM Air Defence €1.5bn H1 (3.2x) | **Kongsberg NOK 174.2bn ≈ 3.9 yr** (NOK 52bn for 2027 delivery) | **Kongsberg Q3 +50%** (Defence Systems +58%, Missiles & Aerostructures +87%); RHM AD +62% (H1); MBDA output +40% (2026) `[E]` | Kongsberg 16.4% (DS 20.6% incl. one-offs; M&A 11.6%, Zone 5 dilution); RHM AD 16.0% | **Binding**: MBDA doubles Aster output in 2026; Diehl near 2,000 IRIS-T missiles/yr `[E]`; Kongsberg Virginia and Australia plants 2027–28, Norwegian missile facilities completed; US stocks drained by the Iran war `[E]` |
| Combat air and aerostructures | **Airbus D&S 9M €11.5bn (vs €6.8bn, +70%)**; **Saab Q3: Gripen E Ukraine SEK 24.6bn, GlobalEye SEK 10.1bn**; Dassault €2.9bn (H1); Leonardo €16bn group (1.6x, H1) | Dassault €45.4bn (208 Rafale: 165 export, 43 France) | Dassault 12 Rafale delivered H1; Leonardo +12% (H1) | **Airbus D&S adj. EBIT €672m 9M (vs €420m)**; Leonardo EBITA 7.8% | Rate-limited (Rafale ramp); F-35 dominates European new-fighter choices |
| Naval | **Saab Q3: German frigate systems SEK 8.7bn**; Naval Group Sweden 4 FDI €4.3bn (31 Aug; grade C); F128/MEKO A-200 option approved 8 Oct (€5.6bn; grade B); TKMS €3.6bn 9M + €6.3bn MEKO A-200 | TKMS >€25bn ≈ 10 yr (revenue ≈ €2.3bn `[A]`); Fincantieri €74.2bn total (incl. cruise); RHM Naval €6.3bn | TKMS 2026 guidance +2–5%; Fincantieri defence held back (Constellation reset) | RHM Naval 9.8% | **Yard-limited**; F126 frigate cancelled (Jun 2026), replaced by TKMS MEKO A-200; Italy postpones frigates `[E]` |
| C4ISR, electronics and space | **Thales Defence 9M orders €11.3bn (+14% organic), B2B ≈ 1.21**; Hensoldt 2.4x (H1); Indra Defence orders €1.5bn H1 | Hensoldt €10.4bn ≈ 3.8 yr; Indra Defence €11.7bn | **Thales Defence 9M +13%**; Hensoldt +24% (H1); Indra Defence ≈ +100% (H1); RHM Digital +23% | Thales 12.5% (H1); Hensoldt adj. EBITDA 11.8% (H1; FY guidance 18.5–19%); RHM Digital 7.7% | Tight (microelectronics, skilled labour) |
| Group level (multi-segment) | **Saab Q3 orders SEK 65.8bn, B2B 3.2x**; BAE £16.4bn H1 (1.04x); Kitron 1.4x (Q2) | Saab SEK 274bn (Q2; Q3 not read); BAE £84bn; Leonardo €59bn; Kitron €794m | **Saab Q3 +30.6% organic**; BAE +9%; Kitron +72% (Q2) | **Saab Q3 EBIT 9.5%** (EBITDA 13.8%); BAE 10.8% | — |

- **Peer book-to-bill** is above 1.0 in every core segment (latest 1.04–3.2x). There is no Bear
  signpost on orders. The Bull signpost (> 2.0 sector-wide) is met by Kongsberg and Saab, not by
  the sector (Thales 1.2, BAE 1.0).
- **Cash improved at the Nordic peers:** Saab's operating cash flow was SEK 6.8bn in Q3 (SEK 0.1bn
  a year earlier) and Kongsberg's NOK 4.1bn, with net cash of NOK 5.3bn. Rheinmetall's operating
  FCF was −€1.6bn in H1; its Q3 (5 Nov) is the next test of the conversion risk.
- **Valuation context (Yahoo, 30 Oct 2026 closes; context only, never an IAF input):**

| Ticker | Price 30 Oct | vs 7 Oct | vs 52-week high | Forward PE |
|---|---|---|---|---|
| RHM.DE | €1,037.6 | +12% | −47% (low €909 after 7 Oct) | 19.6 |
| KOG.OL | NOK 355.8 | +20% | −17% | 31.1 |
| SAAB-B.ST | SEK 675.2 | +14% | −10% | 67.9 (Yahoo value wrong: forward EPS 9.95 below current-year 14.91) |
| HO.PA | €235.7 | +9% | −14% | 19.0 |
| LDO.MI | €51.76 | +13% | −22% | 17.9 |
| BA.L | 2,070p | +13% | −12% | 21.6 |
| HAG.DE | €85.62 | +14% | −11% | 34.3 |
| R3NK.DE | €36.92 | +7% | −46% | 17.6 |
| TKMS.DE | €88.80 | +19% | −18% | 31.6 |
| CSG.AS | €14.47 | +5% | −59% | 10.6 |
| AM.PA | €307.0 | +10% | −15% | 16.3 |
| FCT.MI | €12.65 | +5% | −44% | 15.5 |
| IDR.MC | €63.88 | +9% | −3% | 19.3 |
| KIT.OL | NOK 90.50 | −13% | −22% | 18.4 |

  - Other signals: KNDS postponed its IPO in July 2026 (investors would not pay above €12bn).
    The WisdomTree Europe Defence trailing PE fell from 39.5x to 30.9x by June 2026 `[E]`.

## Drivers

### Threat and policy regime

- **Ukraine:**
  - No comprehensive ceasefire. Trump's "energy ceasefire" (around 11 Oct) drew violation claims.
    The Kremlin rejected Zelenskyy's 60-day truce to allow elections. A local truce in Oleshky
    (Kherson), brokered by Melania Trump, was set for 27–31 Oct for humanitarian aid `[F]`.
  - Putin agreed "in principle" to restart talks; a new US-brokered round is expected in
    mid-November `[E]`. Russia keeps maximalist demands; Kyiv rejects giving up land. Metaculus'
    most likely ceasefire date was 24 Nov 2027 `[E]` (7 Oct reading).
  - SIPRI 2025: Russia USD 190bn (7.5% of GDP), Ukraine USD 84bn (39.6% of GDP) `[F]`.
- **Russia vs NATO:** drone and airspace incidents keep recurring (largest: Poland, Sep 2025;
  later shoot-downs over Lithuania `[E]`). No incident with casualties was found for October 2026
  `[?]`. The threat assessment underpinning the plans is unchanged.
- **US posture:**
  - 5,000 troops ordered out of Germany (May 2026) `[F]`. The Pentagon review weighs withdrawing
    25,000–40,000 of the ~80,000 in Europe; the final recommendation goes to Hegseth on **6 Nov**,
    before any proposal to Trump `[E]`.
  - The 2026 defense policy bill bars using certain funds to keep US troops in Europe below 76,000
    for more than 45 days unless assessments and certifications go to Congress, followed by a
    60-day wait `[E]`. It slows a cut; it does not prevent one.
  - The 2026 Iran war drained US munitions and interceptors (3–8 years to replenish `[E]`). That
    delays US deliveries to Europe (Patriot PAC-3) and supports European suppliers. US efforts on
    Ukraine were paused while the Iran war ran.
- **NATO:**
  - Hague targets: 3.5% core + 1.5% related by 2035, with a review of the trajectory in 2029.
  - Ankara summit (7–8 Jul 2026): Europe and Canada raised core spending by ≈USD 139bn in 2025;
    €70bn pledged to Ukraine for 2026; >USD 50bn of new procurements announced, incl. >USD 40bn
    of counter-drone capability over five years `[E]`.
  - Five allies are above 3.5% in 2026 (LT 5.33, EE 5.11, LV 4.92, PL 4.68, GR 3.65); 17 meet the
    1.5% part `[F]`.
- **EU:**
  - SAFE €150bn: 19 states applied for > €130bn; all national plans approved; 16 loan agreements
    signed; ≈ €13.5bn pre-financing paid to 11 states `[F]` (Eunews, 29 Oct). France €15.1bn
    (36 projects, first tranche > €2.2bn) `[E]`. Italy requests €8.9bn of €14.9bn. Hungary cut to
    €5.4bn. Germany did not apply.
  - **SAFE round 2 opened 29 Oct: €21.3bn** left in the original envelope, open to all 27; priority
    to joint procurement with Ukraine in air and missile defence, drones and counter-drone, and
    ammunition and missiles; allocations within two weeks of the deadline, projects to be
    finalised by year-end `[F]`. It is financing inside the existing envelope, not new money.
  - EDIP: €1.47bn work programme (30 Mar 2026). MFF 2028–34: €131bn defence and space proposed;
    the October European Council conclusions were not found `[?]`.
- **UK (outside the EU):** treaty talks with Finland, Poland and the Netherlands on a multilateral
  defence financing mechanism; a defence finance task force works towards the 2027 Spending Review
  `[F]` (Budget, 28 Oct). PM Andy Burnham, Chancellor John Healey (first Budget). An early general
  election (Dec 2026 or spring 2027) is press speculation `[E]`.

### Fiscal capacity

- **10-year yields (daily closes; Aug = FRED monthly average, the 7 Oct baseline value):**

| | DE | FR | IT | UK |
|---|---|---|---|---|
| 30 Oct 2026 | 3.34% | 4.93% | `[?]` (below FR) | 5.31% (28 Oct, 14:00) |
| October peak | 3.60% (1 Oct) | 5.13% (22 Oct; highest since July 2002) | — | 5.53% (early Oct; highest since 2007) |
| Aug 2026 (monthly avg) | 3.18% | 4.00% | 3.99% | 4.99% |

- **OAT–Bund:** 82 bp (Aug average) → ≈ 96 bp (mid-Sep) → 117 bp (30 Sep) → 130 bp (1 Oct) →
  **174.6 bp (22 Oct close; ≈ 178 bp intraday), the widest since late 2011** → 159.0 bp (30 Oct)
  `[F]`. France now borrows above Italy `[E]`. BTP–Bund 116 bp on 6 Oct `[E]`.
  - Drivers `[E]`: French public debt 115.7% of GDP (2025) heading for 121.7% in 2027, deficit 5.1%,
    a fragmented parliament for the 2027 budget, and the presidential election in April–May 2027.
    Moody's held Aa3 (negative) on 23 Oct.
  - **The Bear signpost (> 120 bp) is crossed and the fiscal-stress trigger fired** (+58 bp from
    21 Sep to 21 Oct).
  - The defence line has not been touched: PLF 2027 keeps the LPM step (+€6.5bn).
- **Italy:** in the EU's excessive deficit procedure. The budget law cuts the defence add-on from
  €22bn to €14bn over 2027–28 (€7bn a year) and postpones frigates, armoured vehicles, drone plants
  and satellite communications `[E]`. Italy's SAFE request is €8.9bn of €14.9bn.
- **UK:** the gilt 10-year touched 5.53% in early October. The Budget was received calmly (5.31%
  on the day). Debt interest is £14bn higher this year `[E]`. The DIP is funded; 3% by 2030 is not.
- **Poland** runs a 7.1% deficit in the 2027 draft `[F]` (the commitment was 3.7%).
- **Germany** is the counterweight: debt-brake exemption, 2027 draft €139.6bn, Finanzplan to
  €180bn+ in 2030. The Bund also rose (3.18% → 3.34–3.60%).
- Base credibility haircuts carry these differences (see Spending tracker). France 2028–30 and
  Italy are the rows to watch.

### Equipment share and European share

- Europe's equipment spending at fixed FX: €35bn (2014) → €119bn (2024) → €197bn (2026e)
  `[F]`, ×5.6 in twelve years. The equipment share rose from 17.8% to 34.3%.
- High-share countries: Poland 56%, Baltics 44%, UK 37%. Norway 17.9% in 2026e, because Ukraine
  aid (NOK 70bn military in 2027) is about a third of its NATO figure.
- New in this run: German procurement > €60bn in the 2027 draft (+33% on 2026), UK MoD capital
  +18% in 2027-28, French programmes à effet majeur +24%. Against: Italy's postponements. Net
  effect is within the Base equipment-share path (±1.5 pp range).
- **Ukraine aid inside donor figures (memo):**
  - Norway NOK 70bn (2027 budget) `[F]`; Netherlands > €3bn in 2027 `[F]`; UK at least £3bn a year
    plus the Budget's £10bn package (mostly loans and export-credit guarantees) and £500m of urgent
    military aid this winter, paid from the Treasury Reserve but counted for NATO `[F]`.
  - Germany, Denmark (Ukraine Fund) and Sweden also count large aid lines.
  - Kiel: European military aid in H1 2026 was close to the 2025 level `[F]`. Order of magnitude
    €30–40bn a year inside the Europe total `[A]`.
  - Part of it buys from European industry (Nansen, the Danish model, NASAMS); part buys US
    weapons (PURL).
- European share drivers in Base:
  - Germany's procurement list (8% US `[E]`).
  - SAFE content rule (65% EU/EEA/Ukraine), now with round 2's Ukraine joint-procurement priority.
  - EDIP and joint procurement (collaborative 24% of EU equipment spending, EDA `[F]`).
  - US supply constraints.
  - Against: F-35 programmes (Finland, Czechia, Greece, Romania, Belgium, Poland, Norway, Denmark),
    Korean land systems in Poland, and the September buys (Sweden HIMARS, Spain K9 `[?]`, Croatia
    Chunmoo). None above €5bn.

### Segment allocation and leading indicators

- **Germany:** 153 25-Mio-Vorlagen planned for Sep 2025–Dec 2026 (≈€83bn); 104 approved in 2025
  (>€45bn) `[E]`; about 60 more announced for 2026 `[E]`. The F128/MEKO A-200 four-ship option was
  approved on 8 Oct (€5.6bn budgeted, completion 2035; grade B). The year-end batch of Vorlagen comes
  with the December committee sessions; Arminius (Boxer, ≈ €12.4bn Rheinmetall share) is due on
  9 Dec `[E]`.
- **Norway 2027 investment lines:** submarines NOK 7.7bn, battle tanks 4.6bn, combat aircraft
  3.3bn, frigate life extension 2.3bn, air surveillance 1.9bn; NOK 516m for industry capacity
  `[F]`.
- **UK DIP (4 years):** munitions £11bn, drones and autonomy £5bn, GCAP £8.6bn, space £3.2bn
  `[F]`. Budget: National Wealth Fund and British Business Bank up to £5bn of investment and
  lending for defence and dual-use firms over four years (outside the MoD budget) `[F]`.
- **France PLF 2027:** programmes à effet majeur €17.2bn (+24%), MCO €7.3bn (+14%), deterrence
  €7.9bn (+7%); SAFE projects include A400M, GlobalEye, CAESAR, naval drones and munitions;
  radars, electronic attack and studies for a Leclerc successor `[F]`.
- **Italy:** frigates, armoured vehicles, drone factories and satellite communications postponed;
  GCAP €8.8bn protected `[E]`. Naval and land orders from Italy slip.
- **SAFE round 2 priorities:** air and missile defence, drones and counter-drone, ammunition and
  missiles, with Ukraine.
- Allocation conclusion `[A]`, unchanged: air defense, munitions, drones and sensors take a rising
  share; land is large but already booked; naval is booked into the 2030s; combat air is held back
  by F-35 choices and by long development cycles (GCAP, FCAS), with Gripen and GlobalEye orders as
  the European exceptions.

### Industry supply and capacity

| Segment | Status | Base consequence |
|---|---|---|
| Ammunition | European 155 mm capacity heads for ≈2m/yr by 2027; "supply likely to outstrip demand in the early 2030s" `[E]`. Rheinmetall Unterlüß 350k/yr from 2027 (first batch in Jul 2026 a low five-figure quantity `[E]`); Lithuania 100k/yr from Q2 2027; Aschau powder 4,500 t/yr from Q3 2027; Albacete medium calibre > 1m rounds/yr mid-2027 `[E]`; Poland ×6 to 180k by 2027 `[E]`. Shell forging is running ahead of explosives and propellant filling `[E]` | Revenue flat from 2028–29; margins fall from 24% toward 14%. Delivered output lags announcements, which may push the surplus later: watched, not applied |
| Air and missile defense | Binding constraints: MBDA invests €5bn 2026–30 and hires 2,800 in 2026 `[E]`; Diehl plans 10 IRIS-T systems in 2026 `[E]`; Kongsberg: new missile facilities in Norway completed, US and Australia plants under way, new Polish counter-drone factory, "capacity to execute on the current order backlog" `[F]`; Rheinmetall rocket motors at Unterlüß from Q1 2027 `[E]` | Shortage through the window; pricing power holds |
| Land | Vehicle plants full; KNDS seeking automotive sites `[E]` | Backlog conversion is the limit |
| Naval | Yard slots set the pace (TKMS backlog ≈ 10 years) | Slow conversion |
| Bottlenecks | Energetics, rocket motors, microelectronics, skilled labour `[E]`; China's dual-use export stop on Rheinmetall and 13 other European defense companies (end-July 2026; rare earths, chemicals) `[E]` | Cap the Bull volume upside |

### Orders to revenue

- 2026 peer book-to-bill is 1.04–3.2x and backlogs are 4–10 years of revenue. Revenue growth in
  2027–28 is therefore largely booked in Base. Kongsberg's backlog for 2027 delivery (NOK 52bn)
  equals 117% of its 2026E revenue `[F]`/`[A]` (kog v2).
- The Base orders index falls in land, ammunition and naval after the 2025–26 mega-frames and
  submarine/frigate awards. It holds in air defense and C4ISR.
- The Bear is an orders shock (index 55–75 by 2029) with a lagged revenue effect (+8% in 2027,
  0% by 2029).

### Pricing and margins

| Segment | Latest margin | Base steady state | Why |
|---|---|---|---|
| Ammunition | 24–29% (scarcity) | 14% | Surplus risk from 2028 |
| Air and missile defense | ~16% (Kongsberg Q3 16.4%) | 15% | Shortage persists |
| Land | 11–15% | 10% | |
| C4ISR | ~12% EBIT | 12% | |
| Combat air | 8–10% | 9% | |
| Naval | ~5–10% | 7% | |

- Fixed-price contracts with escalation dominate. Customer advances fund part of the ramp-up
  (Kongsberg prepayments NOK 36.8bn at 30 Sep), but working capital is still absorbing cash at
  Rheinmetall (H1).
- Kongsberg's Defence Systems margin of 20.6% in Q3 includes risk releases on projects; the
  underlying level is closer to 16–17% `[A]`. No steady-state margin changes.
- Bear margins are 2–4 pp lower (price pressure in ammunition and land). Bull margins are 1–4 pp
  higher.

### Ukraine and export markets

- **Ukraine:**
  - 2027 draft budget: security and defence UAH 4.885tn (≈USD 110bn, ≈44% of GDP), +12% `[F]`.
  - EU Ukraine Support Loan: €90bn for 2026–27, of which €60bn is military `[F]`. It is
    non-NATO financing and therefore additional to the Europe total.
  - **Gripen E:** 16 aircraft, SEK 24.6bn, signed with FMV on 30 Jun and booked by Saab in Q3;
    deliveries 2029–30; reportedly paid through the EU loan with UK support `[E]`. Ukraine row,
    combat air segment. The 2025 letter of intent for 100–150 Gripen E remains an ambition.
  - Kyiv's defence need is €83bn for 2026–27 (EU estimate) `[E]`.
  - Base: Ukraine demand for European industry stays high to 2027 and then depends on the
    ceasefire path (Bull: an EU-financed rebuild; Bear: fall-off).
- **Gulf** (reads Oil BBB 24 Oct: Brent Base 88 / 77 / 72, Bear 65 / 60 / 60, Bull 118 / 102 /
  90): restocking of air defense after the Iran war. Since 22 Oct, Houthi strikes inside Saudi
  Arabia and Aramco's Dhahran evacuation add to the need. Examples: NASAMS for Kuwait (Kongsberg,
  ≈ USD 400m, not yet booked), radars and surveillance for Qatar and the UAE (Thales), MBDA's Gulf
  demand. Base: strong (unchanged; the higher 2027 oil Base only firms it). Bear tied to oil Bear
  (60–65 $/bbl).
- **US:** Kongsberg (NSM/JSM incl. JSM for the USAF USD 100m; Zone 5 Rusty Dagger USD 65m for the
  US Navy; AUVs for DIU USD 54m; Virginia plant), BAE Inc., Leonardo DRS, Rheinmetall (155 mm order
  via the US for Eastern Europe, Sep 2026). US budgets are not modelled here.
- **Asia-Pacific and other:** Rafale exports (165 in backlog), Gripen, GlobalEye (SEK 10.1bn to an
  undisclosed customer in Q3), Hanwha competition. Base only.

### Base test (pre-mortem)

| What would make Base wrong | Evidence now | Verdict |
|---|---|---|
| **Too high: fiscal retreat** | OAT–Bund 82 → 159 bp (peak 174.6 bp, 22 Oct), French 10y 5.13% peak, Moody's Aa3 negative, French presidential election Apr–May 2027; Italy cut its defence add-on (22 → 14bn) and postponed frigates and armoured vehicles; gilts 5.31% (peak 5.53%); UK 3% unfunded | **Signpost crossed, trigger fired.** But every funded 2027 line held: PLF = LPM, DIP fully funded, German draft €139.6bn, Poland 4.51%. Base already sits below the plans or pledges of FR (2.46% vs LPM ≈2.5% in 2029), IT (2.40% vs 2.5%), ES (2.1%) and UK (2.75% in 2030 vs 3%). **Base kept**; France 2028–30 and Italy carry a downward skew |
| **Too high: conversion fails** (cash, capacity, cost overruns) | Rheinmetall operating FCF −€1.6bn in H1 (Q3 on 5 Nov); Saab Q3 operating cash flow SEK 6.8bn; Kongsberg NOK 4.1bn; peers +5–20% since 7 Oct | Risk eased at the Nordic peers; unchanged elsewhere. It hits the *timing* of revenue (2027–28) more than budgets. Base unchanged |
| **Too high: ceasefire → peace dividend** | No ceasefire; local Oleshky truce only; talks expected mid-November; plans rest on the threat assessment | Unchanged. A ceasefire alone does not cut Base, but it does hit ammunition and Ukraine orders (in the segment paths) |
| **Too high: European share** | No > €5bn US buy logged; Sweden HIMARS SEK 7bn, Spain K9 `[?]`, Croatia Chunmoo (September); SAFE round 2 with the 65% rule | Low confidence either way. Kept at 65% → 69% with a ±10 pp range |
| **Too low: Germany executes 100%** | 2027 draft procurement > €60bn (+33%); 25-Mio flow continues; F128 option approved | Possible. Base applies a 95% haircut; Bull carries full execution. Test: Bereinigungssitzung 12 Nov |
| **Too low: US drawdown in November** | Recommendation to Hegseth on 6 Nov (25–40k troops); the 76,000 floor in the defense bill slows a cut | A Bull catalyst with a date. Next update right after the decision |
| **Too low: orders running ahead** | Kongsberg B2B 2.06, Saab 3.2x, Airbus D&S 9M orders +70%, Thales Defence +14% | Lifts the 2026 order base; the 2027 orders index is, if anything, too high. Revenue paths unaffected. Kept inside the ±15 point range |

- **Against external projections:** EDA's "€547bn by 2029 on current trends" (EU27) compares with
  ≈€594bn in this Base (EU members + non-NATO EU, at today's FX). That is +9% in 2029 and a CAGR
  of 8.3% vs 6.4%. The difference is mainly Germany's July 2026 Finanzplan, which is newer than
  the EDA data collection.
- **Against company guidance:**
  - Rheinmetall's 2026 guidance (€13.7–14.2bn, ≈ +40%; confirmed 6 Oct) and Saab's 22% organic
    CAGR target (2023–27; Q3 +30.6%) are consistent with the current year and with Base.
  - Kongsberg's NOK 100bn ambition for 2029 (reiterated in Q3) is above Base (see For IAF).
- **Conclusion of the test:** Base is kept as the most likely path. The fiscal stress is real and
  concentrated in France and Italy, but it has not yet cut a funded national total; Italy shows
  how it would first appear (postponed procurement). The market's rebound since 7 Oct does not
  change that reading.

## Signposts and monitoring

| Signpost | Threshold (Bear / Bull) | Now (31 Oct) | Previous (7 Oct) | Direction |
|---|---|---|---|---|
| Ukraine ceasefire | Signed and holding with fiscal stress (Bear) / EU-financed army rebuild (Bull) | No ceasefire; local Oleshky truce 27–31 Oct; talks expected mid-Nov | Talks paused since Sep 2026 | Neutral |
| US troops in Europe | Decision ≥ 25,000 withdrawn (Bull) | Recommendation to Hegseth 6 Nov; 76,000 floor in the defense bill | Review; recommendation early Nov | Toward Bull |
| OAT–Bund 10y spread | > 120 bp (Bear); next level > 200 bp | **159 bp (30 Oct); 174.6 bp peak (22 Oct) — crossed** | 82 bp (Aug avg) | **Bear (crossed)** |
| French rating | Moody's downgrade below Aa3 (Bear) | Aa3 negative, held 23 Oct | — | Watch |
| UK 10y gilt | > 5.5% (Bear) | 5.31% (28 Oct); touched 5.53% early Oct | 4.99% (Aug avg) | Toward Bear |
| German 2027 budget | EP14 < €100bn (Bear) / > €115bn (Bull) | Draft €109.7bn (+ SV €29.9bn); Bereinigungssitzung 12 Nov | Draft €109.7bn | Base |
| France PLF 2027, mission Défense | < €60bn (Bear) / > €65bn (Bull) | **€63.4bn (PLF 8 Oct) — Base met**; parliament to pass it | LPM €63.3bn; PLF due | Base |
| UK funding | DIP cut (Bear) / 3% by 2030 funded (Bull) | DIP fully funded; 3% by 2030 unfunded until the 2027 Spending Review | DIP £298bn, £4.7bn unidentified | Base |
| Italy defence add-on | Further cut or more postponements (Bear) | €14bn over 2027–28 (planned €22bn); frigates, vehicles postponed | — | Toward Bear |
| Peer book-to-bill | < 1.0 for 2 quarters (Bear) / > 2.0 sector-wide (Bull) | 1.04–3.2x (Kongsberg 2.06, Saab 3.2, Thales Defence 1.2) | 1.04–3.2x | Base/Bull |
| Ammunition pricing | Price cuts or idle lines (Bear) | No evidence; surplus forecast for the early 2030s `[E]` | No evidence | Watch |
| European buy of a US system | > €5bn (Bear for the European share) | None (largest: Sweden HIMARS SEK 7bn) | None logged | — |
| EU common financing | SAFE 2 (new money) / Eurobonds / MFF €131bn adopted (Bull) | SAFE round 2 = €21.3bn left in the existing envelope (opened 29 Oct); MFF in negotiation | SAFE round 1 disbursing | Neutral |
| Russian action on NATO territory | Incident with casualties (Bull) | Recurrent incursions; none with casualties found for Oct `[?]` | Recurrent drone incursions | Watch |
| NATO 2027e data (Jun/Jul 2027) | Europe < 2.6% (Bear) / > 2.8% (Bull) | 2026e 2.56% | 2026e 2.56% | — |

**Open checkpoints:**
1. ~~Read France's PLF 2027 (mission Défense).~~ **Closed:** €63.4bn excl. pensions (8 Oct). New:
   follow its passage through parliament and any 2026–27 annulation decree (a September decree was
   reported but not found `[?]`).
2. ~~Netherlands' 2027 budget.~~ **Closed:** €28.9bn + Ukraine > €3bn. Carried: the coalition's
   figures beyond 2027.
3. Sweden: **election outcome read** (left bloc by one seat; Kristersson resigned). Carried: the new
   government and its 2027 defence figures.
4. ~~Finland: 2027 budget.~~ **Closed:** MoD €7.0bn (+€0.6bn). New: reconcile the national measure
   (2.6%) with NATO's 2.65% for 2026e.
5. Build country-level European-supplier shares, starting with the big US/Korean programmes.
   Verify Spain's 128 K9 (single source).
6. Denmark: is the "+DKK 21bn in 2027" measured against 2026 (that would put Denmark on the Bull path) or against the earlier plan?
7. Make the award log complete (OCCAR, NSPA, national agencies). Extended in this run.
8. Nammo and MBDA annual figures (Kongsberg Q3 gives none; look-through Nammo share ≈ 25% via
   Patria `[E]`).
9. Services row data.
10. **New:** Italy's NATO-basis path for 2027–28 (budget law text; the two readings conflict).
11. **New:** Germany: rebuild the NATO-basis 2027 figure from EP14 + SV + other ministries
    (Ukraine aid) after the Bereinigungssitzung.

**Calendar to the next update:**

| When | Event |
|---|---|
| 3 Nov | US midterms |
| 5 Nov | Rheinmetall, Hensoldt and Renk Q3 |
| 6 Nov | Pentagon posture recommendation to Hegseth; Leonardo 9M (date estimated) |
| 12 Nov | Bundestag budget committee, Bereinigungssitzung (2027 budget) |
| Mid-Nov | US-brokered Russia–Ukraine talks (expected) |
| 24–27 Nov | Bundestag plenary on the 2027 budget (adoption) |
| 1 Dec | SIPRI Top 100 |
| 2–4 Dec | Polish Sejm second and third reading of the 2027 budget (Senate 8 Dec) |
| 7 Dec | TKMS annual report |
| 9 Dec | Bundestag decision on Arminius (Boxer; Rheinmetall ≈ €12.4bn) `[E]` |
| Dec | Storting adopts Norway's budget; EU Council (MFF); SAFE round 2 allocations; French PLF vote |
| Jan 2027 | Window roll (first run in January) |
| Feb 2027 | Eurostat COFOG; Kongsberg Q4 (11 Feb) |
| Apr–May 2027 | French presidential election |
| 2027 | UK Spending Review (path to 3% and 3.5%; date not set) |

## For IAF

- **No material change.** All segment order and revenue paths, long-end CAGRs, steady-state margins
  and the capacity balance are unchanged. Defense company analyses need no update from this run.
  What they should note:
  - The Bear's fiscal half is now present (OAT–Bund 159 bp; Italy's cut add-on). Bear mappings
    stay as they are; France- and Italy-exposed revenue is the first to test.
  - The Bull's date is 6 Nov (Pentagon recommendation).
- **Rheinmetall:**
  - Rows: Land (Vehicle Systems), Ammunition (Weapon and Ammunition), Air and missile defense,
    C4ISR (Digital Systems), Naval (from Feb 2026).
  - Backlog €80.5bn includes frames; FY26 sales guidance €13.7–14.2bn (confirmed 6 Oct). Separate
    firm backlog from frames before testing coverage.
  - Ammunition is the largest profit pool (23.7% margin) and the weakest segment in Base after
    2027. Test the Base steady state at 14%.
  - New since 7 Oct: Italy postpones armoured vehicles (a Land-row risk for the Leonardo JV
    business) and frigates; the 2027 German draft keeps procurement above €60bn; Arminius goes to
    the Bundestag on 9 Dec; Q3 on 5 Nov.
- **Kongsberg:**
  - Rows: Air and missile defense and missiles (NASAMS, NSM/JSM), Combat air (F-35 parts), C4ISR
    (Discovery); export rows US and Gulf.
  - Q3 (kog v2): firm backlog NOK 174.2bn ≈ 3.9 years; NOK 52bn for 2027 delivery covers 87% of
    the kog Base 2027. Orders ahead of the row; revenue in line at group (+36% 9M vs the row's
    +35%).
  - The NOK 100bn revenue ambition for 2029 `[E]` (reiterated in Q3) stays above the Base row
    (+19% a year). The gap must be explained by named share gains and the US plant, or treated as
    a Bull element (kog v2 treats it as an overlay).
- **Saab:** Combat air (Gripen), Air and missile defense, C4ISR (Surveillance, GlobalEye), Naval
  (Kockums; Polish submarines; German frigate systems). Q3 orders SEK 65.8bn; backlog SEK 274bn at
  Q2.
- **Others** (Thales, Leonardo, BAE, Hensoldt, Renk, TKMS, CSG, Dassault, Airbus D&S): use the
  appendix mapping. US subsidiaries (BAE Inc., Leonardo DRS) are outside the European rows.
- **Growth capex:** test ammunition capacity against the surplus risk from about 2028 (Base) and
  air defense capacity against the shortage (Base).

## For downstream skills

- [[hy-market-bbb]]: no defense issuer in the Nordic HY watchlist (Kongsberg is rated A by NCR,
  one NOK 1bn bond; not high yield). Answer: "none known".

## Change log

- **Update, 31 Oct 2026 (skill 2026-10-10.1). Defense Market BBB kept unchanged.**
  - **Triggers:** upstream oil changed (17 Oct); passed events (UK Budget 28 Oct, Kongsberg Q3
    29 Oct, France PLF 8 Oct); fiscal-stress trigger fired (OAT–Bund +58 bp, 21 Sep → 21 Oct);
    budget presentations (FR, UK, NL, FI, PL first reading).
  - **New:**
    - UK Budget: DIP fully funded; 3% by 2030 on record, unfunded; MoD capital +18%, day-to-day
      −2% (2027-28); £10bn Ukraine package; NWF/BBB up to £5bn; multilateral financing talks.
    - France PLF 2027: mission Défense €63.4bn (+€6.5bn) = LPM; SAFE €15.1bn.
    - Germany 2027 draft reconciled: €139.6bn (EP14 109.7 + SV 29.9); procurement > €60bn.
    - Italy: defence add-on €14bn over 2027–28 (planned €22bn); postponements; SAFE €8.9bn.
    - Poland 2027 draft PLN 198.1bn (4.51%), parliament schedule. Netherlands €28.9bn plus
      Ukraine aid above €3bn. Finland €7.0bn. Sweden: left bloc won.
    - OAT–Bund 159 bp (peak 174.6 bp); French 10y peak 5.13%; gilt 10y 5.31% (peak 5.53%).
    - SAFE round 2 (€21.3bn, 29 Oct); round 1 status (16 signed, ≈ €13.5bn paid).
    - Ukraine: energy ceasefire violations; Oleshky truce; talks expected mid-November.
    - US posture: recommendation to Hegseth on 6 Nov; 76,000 floor in the defense bill.
    - Q3: Kongsberg (B2B 2.06, backlog NOK 174.2bn, +50%), Saab (orders SEK 65.8bn, +30.6%
      organic), Thales Defence 9M (+14% orders, +13% sales), Airbus D&S 9M (orders +70%).
    - Award log: 23 rows added, 3 filled or updated (appendix).
    - Oil read for the Gulf row: Base 88 / 77 / 72 (from 85 / 77 / 72).
  - **Unchanged:** all spending paths (Europe total and every country, in EUR and % of GDP, all
    scenarios); equipment share, European share, equipment and addressable spending; every segment
    path (orders, revenue, CAGRs, long end, steady-state margins); capacity balance; segment
    ranking; catalysts; the Gulf export row (Base strong).
  - **Changed (no path value moved):**

| Item | Previous (7 Oct) | New (31 Oct) | Reason |
|---|---|---|---|
| Status | Initial baseline | Final | Update run |
| Stale after | 5 Jan 2027 | 4 Jan 2027 | Window roll with the first run in January (90-day date would be 29 Jan) |
| Oil read (Gulf row) | Brent Base 85 / 77 / 72 (4 Oct) | 88 / 77 / 72 (24 Oct) | Oil BBB change of 17 Oct; Gulf row stays "strong" |
| OAT–Bund signpost | 82 bp (Aug avg), toward Bear | 159 bp (30 Oct), **crossed** (> 120 bp since 1 Oct) | French fiscal and political stress; trigger fired |
| Gilt signpost | 4.99% (Aug avg) | 5.31% (28 Oct); touched 5.53% | Toward Bear, not held above 5.5% |
| Bear signposts | — | Added: OAT–Bund > 200 bp, Moody's downgrade below Aa3, mission Défense cut in parliament or an LFR, further Italian cuts | Next level after the crossing |
| France PLF signpost | Open | Base met (€63.4bn) | PLF 8 Oct |
| UK target | 3% next parliament | 3% by 2030 (unfunded; grade C) | Budget 28 Oct |
| Germany 2027 total | EP14 €109.7bn + SV €27.5–30bn; €133.3bn quoted, unreconciled | €139.6bn (SV €29.9bn) | Bundestag |
| Italy SAFE request | €8bn | €8.9bn | Eunews 29 Oct |
| Base range note | Symmetric | France 2028–30 and Italy skewed to the lower half (points kept) | Fiscal stress; Italy's cut |
| Market check, valuation | H1 data; 7 Oct prices | Q3 data where reported; 30 Oct prices | New reports |
| Open checkpoints | 9 open | 1, 2, 4 closed; 3 partly; 10 and 11 added | This run |

  - **Forecast vs actual:** not applicable until the window rolls (2026 not realised). Q3 actuals
    are in line with the 2026 current-year row assumptions.
  - **Weights:** 25/50/25 convention, kept.
  - **IAF:** no update needed from this run (kog and rhm read unchanged paths).
  - **Input assessed:** the run brief cited DNB Carnegie (23 Oct): French 10-year above 5% and
    OAT–Bund above 170 bp. Confirmed for 22–23 Oct (5.13%, 174.6 bp close); the spread has since
    narrowed to 153–159 bp. Used as a signpost reading, not as a forecast.
  - New baseline date: 31 Oct 2026.
- **Initial baseline (7 Oct 2026, skill 2026-10-07.3).** No previous values.
  - Method notes, recorded in the skill (revision 2026-10-07.3):
    - Paths in nominal % of GDP, with NATO's T3 shown where it differs (NL).
    - The European-supplier share is set at Europe level for now.
    - Segment weights are 2026 peer-group revenue estimates `[A]`.
    - The SIPRI Excel is readable; SIPRI fact-sheet PDFs are not.
  - Weights: 25/50/25 convention.

## Appendix

### Contract award log (incomplete; extended 31 Oct)

| Date | Buyer | Segment | Supplier | Value | Firm / frame | Funding | Delivery | Grade | Source |
|---|---|---|---|---|---|---|---|---|---|
| 7 Apr 2026 | Netherlands | Air and missile defense (non-European) | Raytheon — Patriot fire unit | USD 627m | Firm | National | — | C | Trade press |
| 21 Apr 2026 | Denmark | Air and missile defense | Eurosam (Thales/MBDA) — SAMP/T NG, 4 systems | ≈ €1.47bn | Firm | National | — | C | Thales via trade press |
| 29 May 2026 | Romania | Land / air defense / ammunition / naval | Rheinmetall — SAFE package (Lynx, air defense, ammunition, 4 vessels €0.92bn) | €5.7bn | Nomination | SAFE | — | A | Rheinmetall (rhm analysis) |
| Q2 2026 | Poland | Naval | Saab (Kockums) — Orka submarines | SEK 47bn | Firm | National | 2030s | A | Saab Q2 2026 |
| Q2 2026 | Canada / Germany / US Air Force | Air and missile defense and missiles | Kongsberg — JSM | NOK 4.7bn / 3.5bn / 2.7bn | Firm | National | — | C | Kongsberg Q2 (kog analysis) |
| Q2 2026 | Kuwait (via Raytheon/FMS) | Air and missile defense (export) | Kongsberg — NASAMS | ≈ USD 400m | Agreed, **not booked** at Q3 | National | — | B | Kongsberg Q2/Q3 |
| 2026 | Germany | Land | Rheinmetall/KNDS — Puma +200 | €3.5bn (Rheinmetall €2bn) | Firm | National | — | A | Rheinmetall (rhm) |
| 2026 | Germany | Uncrewed | Rheinmetall — FV-014 loitering munition | Low single-digit €bn | Frame | National | — | A | Rheinmetall (rhm) |
| 2026 | UK | Services | Rheinmetall — ACTS training | ≈ €1bn Rheinmetall share | Firm (15 yr) | National | 15 yr | A | Rheinmetall (rhm) |
| Jun 2026 | Germany | Naval | F126 frigate (Damen/Rheinmetall NVL) **cancelled**; Rheinmetall wrote off €2.15bn of Naval backlog (Jul) | −€2.15bn backlog; −€0.3bn 2026 sales | Cancellation | — | — | A | Rheinmetall H1 |
| 30 Jun 2026 (booked Q3) | Sweden FMV for Ukraine | Combat air | Saab — 16 Gripen E + spares | SEK 24.6bn | Firm | EU Ukraine Support Loan + UK (reported `[E]`) | 2029–30 | A | Saab Q3 |
| Jul 2026 | US Air Force | Air and missile defense and missiles (export) | Kongsberg — JSM | USD 100m | Firm | US | — | A | Kongsberg (kog) |
| H1 2026 | Germany and others | Land | Rheinmetall Vehicle Systems — nominations | €6.7bn | Mostly frames | National | 2026–30+ | A | Rheinmetall H1 |
| H1 2026 | Various | Air and missile defense | Rheinmetall Air Defence — nominations | €1.5bn | Mixed | — | — | A | Rheinmetall H1 |
| H1 2026 | Various | C4ISR | Hensoldt — orders | €2.8bn | Firm | — | — | A | Hensoldt H1 |
| H1 2026 | Various | Combat air / C4ISR / air defense | Leonardo — orders (AW149, M-346, air defense) | €16bn | Firm | — | — | A | Leonardo H1 |
| H1 2026 | Various | Combat air / space | Airbus Defence and Space — orders | €9.3bn | Firm | — | — | A | Airbus H1 |
| H1 2026 | Spain mainly | C4ISR | Indra Defence — orders | €1.5bn | Firm | National + programmes | — | A | Indra H1 |
| 31 Aug 2026 | Sweden | Naval | Naval Group — 4 FDI frigates | €4.3bn | Firm | National | First ship 2030 | C | Trade press (defence-industry.eu) |
| Early Sep 2026 | Spain | Land (non-European) | Hanwha — 128 K9 howitzers | `[?]` | Firm `[?]` | — | — | C (single source) | Grosswald |
| 7 Sep 2026 | Sweden | Air and missile defense / long-range fires (non-European) | Lockheed Martin — HIMARS (FMS), ~10 launchers + ammunition | SEK 7bn | Firm | National | 2027 | C | Grosswald / trade press |
| 8 Sep 2026 | Croatia | Long-range fires (non-European) | Hanwha — 18 Chunmoo | `[?]` | Firm | — | — | C | Grosswald |
| 14–16 Sep 2026 | US for Eastern Europe | Ammunition | Rheinmetall — 155 mm | Three-digit € millions | Firm | US | — | C | Rheinmetall release |
| 29 Sep 2026 (booked Q3) | Belgium (via the Dutch procurement agency) | Air and missile defense | Kongsberg — NASAMS (18th nation) | NOK 9.8bn | Firm | National | — | A | Kongsberg Q3 (kog) |
| Q3 2026 | Netherlands | Air and missile defense | Kongsberg — NASAMS | NOK 1.5bn | Firm | National | — | A | Kongsberg Q3 (kog) |
| Q3 2026 | Canada | Land | Kongsberg — Protector remote weapon stations (ACSV) | NOK 1.1bn | Firm | National | — | A | Kongsberg Q3 (kog) |
| Q3 2026 | US Navy | Missiles (export) | Kongsberg (Zone 5) — Rusty Dagger | USD 65m | Firm | US | — | A | Kongsberg Q3 (kog) |
| Q3 2026 | Undisclosed | C4ISR / combat air | Saab — GlobalEye | SEK 10.1bn | Firm | — | — | A | Saab Q3 |
| Q3 2026 | Germany | Naval | Saab — systems for the new frigates (MEKO A-200) | SEK 8.7bn | Firm | National | — | A | Saab Q3 |
| Q3 2026 | Germany | Naval | TKMS — 4 MEKO A-200 DEU frigates | €6.3bn | Firm | National | — | A | TKMS 9M report |
| 8 Oct 2026 | Germany | Naval | F128/MEKO A-200 four-ship option approved by the budget committee | €5.6bn budgeted | Option approved | National | To 2035 | B | Grosswald frigate tracker |
| ~21 Oct 2026 | `[?]` | Ammunition | Rheinmetall — artillery ammunition | €444m | Firm | — | — | C | Financial press |
| 22 Oct 2026 | Denmark | Missiles | Kongsberg — JSM for F-35 (intention; value to be negotiated) | `[?]` | Intention, not booked | National | — | D | Kongsberg (kog) |
| 29 Oct 2026 (Q3 order) | US DIU | C4ISR (export) | Kongsberg — autonomous underwater vehicles | USD 54m | Firm | US | — | A | Kongsberg (kog) |
| 9 Dec 2026 (pending) | Germany | Land | Rheinmetall — Arminius (Boxer) | ≈ €12.4bn Rheinmetall share; 30% advance | Pending Bundestag | National | — | C | rhm analysis `[E]` |
| 2027 budget | Norway | Naval / land / air | Budget lines: submarines NOK 7.7bn, MBT NOK 4.6bn, combat aircraft NOK 3.3bn | — | Budget | National | 2027 | B | Regjeringen 7 Oct 2026 |

### Country plans (additional detail)

- **Germany:**
  - 2026 total €108.2bn (EP14 + SV). The NATO figure of €124.7bn adds Ukraine aid and other
    ministries (≈€16.5bn).
  - 2027 draft: EP14 €109.7bn + SV €29.9bn = €139.6bn (Bundestag, 9 Sep first reading); the April
    Eckwerte had EP14 €105.8bn. Military procurement > €60bn (€30.3bn EP14 + €29.9bn SV; 2026:
    €45bn). Bereinigungssitzung 12 Nov; plenary 24–27 Nov.
  - Base applies a 5% execution haircut to the plan in 2027–29.
- **France:** NATO/mission ratio 1.18 in 2026 (pensions and other items, ≈ €10.5bn). PLF 2027
  €63.4bn = LPM, so Base keeps 2027 at the LPM and lets 2028–30 slip by about one year. The 2028
  budget will be prepared after the April–May 2027 presidential election, the main risk to
  2028–30.
- **UK:** NATO 2.6% in 2026-27 and 2.7% in 2027-28 to 2029-30 per the DIP, now fully funded. The
  MoD departmental budget is ≈ 2.3% of GDP in 2027-28 against the 2.7% NATO headline; the gap
  (pensions, intelligence, the Integrated Security Fund, Ukraine aid) is ≈ 15% of the total `[E]`.
  Reaching 3% by 2030-31 needs ≈ £11bn a year more; 3.5% by 2035 ≈ £25bn a year `[E]`. Base reaches
  3.0% only in the early 2030s and 3.2% in 2035.
- **Italy:** budget law adds €7bn a year in 2027 and 2028 (0.3% of GDP), against €11bn a year
  planned under the escape clause (€22bn of €36bn requested for energy and defence) `[E]`. GCAP
  €8.8bn protected. The NATO-basis level for 2027 cannot be derived from the press (checkpoint 10).
- **Poland:** the 2027 draft is PLN 198.1bn (4.51% of GDP), lower as a share of GDP than 2026
  (4.8%). Base holds about 4.4–4.5%. SAFE money (€43.7bn) finances spending already counted.
  Parliament: second and third reading 2 and 4 Dec, Senate 8 Dec; the president cannot veto a
  budget law.
- **Netherlands:** 2027 budget €28.9bn (materiel fund €14.1bn, 49%), Ukraine aid > €3bn on top.
- **Norway:** the NATO figure includes Ukraine aid (NOK 70bn military in 2027). Base assumes the
  aid line stays in through 2030 and that the core ramps per the long-term plan.
- **Finland:** 2027 MoD €7.0bn (+€0.6bn), 2.6% of GDP on the national measure; Ukraine €0.2bn;
  the last budget of the government term.

### Company segment mapping

| Company | Reported segment → row |
|---|---|
| Rheinmetall | Vehicle Systems → Land; Weapon and Ammunition → Ammunition; Air Defence → Air and missile defense; Digital Systems → C4ISR; Naval Systems (NVL, since Feb 2026) → Naval. Civil Power Systems sold (closing Q4 2026) |
| Kongsberg | Defence Systems → Air and missile defense (NASAMS) + Land (remote weapon stations) + C4ISR; Missiles & Aerostructures (incl. Zone 5 from 9 Jun 2026) → Air and missile defense and missiles + Combat air (F-35); Discovery (incl. Sonatech from 1 Sep 2026) → C4ISR (part civil). Kongsberg Maritime demerged 23 Apr 2026 |
| Saab | Aeronautics → Combat air; Dynamics → Air and missile defense + Ammunition (Carl-Gustaf, AT4); Surveillance → C4ISR (incl. GlobalEye); Kockums → Naval; Combitech → Services |
| Thales | Defence → C4ISR + Air and missile defense; Aerospace, Cyber & Digital → mostly outside scope |
| Leonardo | Helicopters (military) and Aeronautics → Combat air; Electronics Europe and Space → C4ISR & space; DRS → US export row; IDV → Land; MBDA stake → Air and missile defense |
| BAE Systems | Air → Combat air; Maritime → Naval; Cyber & Intelligence → C4ISR; UK munitions → Ammunition; Hägglunds → Land; US businesses → US export row |
| Hensoldt | Sensors → C4ISR / Air and missile defense (radars); Optronics → Land / C4ISR |
| Renk | Vehicle Mobility Solutions → Land; Marine & Industry → Naval (part civil) |
| TKMS | Submarines, surface ships, Atlas Elektronik → Naval |
| CSG | Defence Systems → Ammunition; Land Systems → Land |
| Dassault Aviation | Rafale → Combat air (mostly export); Falcon → outside scope |
| Airbus Defence and Space | Military aircraft → Combat air; Space and connected intelligence → C4ISR & space |
| Fincantieri | Defence → Naval (cruise outside scope) |
| Indra | Defence → C4ISR |
| Chemring | Countermeasures & Energetics → Ammunition; Sensors & Information → C4ISR |
| Kitron, Theon, Exail | Tier-2: Kitron (EMS, Kongsberg main customer) → Air and missile defense / C4ISR; Theon → Land / C4ISR; Exail → Naval / C4ISR |
| Private: KNDS, Nammo, MBDA, Diehl, Naval Group, Patria | KNDS → Land + Ammunition; Nammo → Ammunition + rocket motors; MBDA and Diehl → Air and missile defense; Naval Group → Naval; Patria → Land |

### Sources

| Source | Content | Definition | Observed / published |
|---|---|---|---|
| NATO, Defence Expenditure of NATO Countries (2014–2026), Excel (`def-exp-2026-en.xlsx`) | Core spending, % GDP, real change, equipment share | NATO core definition, payment basis | 2014–2026e / 7 Jul 2026 |
| NATO, Defence Investment Update | Five allies > 3.5%; 17 meet 1.5% | — | 7 Jul 2026 |
| SIPRI Military Expenditure Database (`SIPRI-Milex-data-1949-2025.xlsx`) | 2025 by country; 1949–2025 history; regional totals | SIPRI definition, constant 2024 USD | 2025 / Apr 2026 |
| SIPRI Arms Transfers (fact sheet) | US 58% of European NATO imports 2021–25 | TIV | 2021–25 / 9 Mar 2026 |
| SIPRI Top 100 | 26 European firms USD 151bn arms revenue (2024) | Arms revenue | 2024 / 1 Dec 2025 |
| EDA, Defence Data 2025–2026 | EU27 €418bn (2025), €454bn (2026e), procurement €115bn, R&D €17bn, collaborative 24% | EDA definition | 2025–26 / 16 Jul 2026 |
| Eurostat COFOG `gov_10a_exp` (API) | GF02 % of GDP | ESA 2010, delivery basis | 2024 / 16 Sep 2026 |
| esut.de (German draft budget 2027; Finanzplan) | EP14, SV, Finanzplan | Federal budget | 7 Jul 2026 |
| esut.de / Bartels | €110bn + €30bn (2027) → €180bn (2030) | — | 29 Aug 2026 |
| **Bundestag textarchiv (kw37)** | **2027: EP14 €109.7bn + SV €29.9bn = €139.6bn; procurement > €60bn** | Federal budget draft | 9 Sep 2026 (printed 31 Oct) |
| **Bundestag hib 839/2026; kw34 timetable** | **Bereinigungssitzung 12 Nov; plenary 24–27 Nov** | — | 16 Oct 2026 |
| Assemblée nationale / LPM update | Mission Défense CP path 2026–30 | Payment credits | 1 Jul 2026 (law 16 Aug) |
| **Ministère des Armées, PLF 2027 (LPM année 4)** | **Mission Défense €63.4bn excl. pensions, +€6.5bn; programmes €17.2bn** | Payment credits | 8 Oct 2026 |
| **Forces Operations Blog** | **PLF 2027 detail; SAFE €15.1bn, 36 projects** | — | 1 Oct 2026 `[E]` |
| GOV.UK, DIP funding explainer | MoD budget and NATO % path; £298bn | NATO core | 30 Jun 2026 |
| **Navy Lookout; ADS Advance (UK Budget)** | **DIP fully funded (£4.7bn); 3% by 2030 unfunded; CDEL +18%, RDEL −2%; £10bn Ukraine; NWF/BBB £5bn** | — | 28 Oct 2026 `[E]` |
| Regjeringen (forsvarsbudsjettet 2027) | NOK 191.7bn; 123bn excl. Ukraine; investment lines | Prop. 1 S basis | 7 Oct 2026 |
| Regeringen.se (press slides 15 Sep) / search summary | SEK 148bn (2027), SEK 175bn (2030) | Swedish measure | Sep 2026 `[E]` |
| **Al Jazeera / CP24 (Sweden election)** | **Left bloc narrow win; Kristersson to resign** | — | 17 Sep 2026 |
| Notes from Poland / defence24 / Sejm | 2027 draft PLN 198.1bn, 4.51%; deficit 7.1%; reading schedule | MON + FWSZ | 28 Aug–8 Oct 2026 |
| Camera dei deputati / DPP | Italy +0.15/+0.15/+0.2 pp | — | Jul 2026 `[E]` |
| **L'Espresso (Italy budget law)** | **+€14bn over 2027–28 vs €22bn planned; postponements; GCAP €8.8bn** | — | 13 Oct 2026 `[E]` |
| **Defensie.nl (Prinsjesdag)** | **2027 €28.9bn; materiel fund €14.1bn; Ukraine > €3bn** | Dutch budget | 15 Sep 2026 |
| **Yle / Verkkouutiset (Finland 2027)** | **MoD €7.0bn, +€0.6bn, 2.6% of GDP** | National measure | Sep 2026 `[E]` |
| BBVA Research / La Moncloa | Spain €35.4bn, 2.0% | — | Jul 2026 |
| Danish MoD / defence24 | Acceleration fund; 3.5% by 2030 | — | 2025–26 `[E]` |
| Finnish Government | ≥3% by 2029 | — | 2025 `[E]` |
| Grosswald SAFE, frigate and award trackers | SAFE allocations; F128 option 8 Oct; Gripen Ukraine; HIMARS Sweden; K9 Spain; Chunmoo Croatia | — | Sep–Oct 2026 `[E]` |
| Council of the EU, SAFE page | SAFE terms | — | 2026 |
| **Eunews / Table.Briefings (SAFE round 2)** | **€21.3bn; 16 signed; ≈ €13.5bn paid; Italy €8.9bn** | — | 29 Oct 2026 |
| Commission, EDIP work programme | €1.47bn 2026–27 | — | 30 Mar 2026 |
| Kiel Ukraine Support Tracker | European aid through Jun 2026 | Allocations | 13 Aug 2026 |
| EU / Kyiv Independent (Ukraine Support Loan) | €90bn, €60bn military | — | 2026 |
| Ukraine draft budget 2027 (Reuters / UkraNews) | UAH 4.885tn security and defence | — | 16 Sep 2026 |
| **CNBC / NPR / MPR / Al Jazeera (Ukraine)** | **Energy ceasefire, Oleshky truce, talks expected mid-November** | — | 5–27 Oct 2026 |
| **AA / Yeni Şafak (NBC report, US posture)** | **Recommendation to Hegseth 6 Nov; 25–40k; 76,000 floor** | — | Sep–Oct 2026 `[E]` |
| **ideal-investisseur.fr; FXStreet; Cbonds** | **OAT and Bund daily closes, OAT–Bund 21 Sep–30 Oct; peak 174.6/178 bp; Moody's 23 Oct** | Daily close | 27–30 Oct 2026 |
| **Portfolio Adviser / trade press (gilts)** | **Gilt 10y 5.31% on 28 Oct; peak 5.53%** | Intraday | 23–28 Oct 2026 `[E]` |
| Quifinanza (BTP–Bund) | 116 bp on 6 Oct | Morning | 6 Oct 2026 `[E]` |
| `docs/kongsberg-analysis.md` v2 (reads the Kongsberg Q3 report) | Q3 orders, backlog, divisions, awards, capacity | Company APM | 29 Oct 2026 |
| `docs/rheinmetall-analysis.md` (For other modules) | Award log, capacity table, China export stop | — | 7 Oct 2026 |
| **Saab Q3 2026 release (via Inderes)** | **Orders SEK 65.8bn; sales SEK 20.6bn, +30.6% organic; EBIT 9.5%; op. cash flow SEK 6.8bn; major orders** | Company | 23 Oct 2026 |
| **Thales 9M 2026 release (via webdisclosure)** | **Defence orders €11.3bn (+14%), sales €9.36bn (+13%)** | Company | 22 Oct 2026 |
| **Airbus 9M 2026 release** | **D&S orders €11.5bn (vs €6.8bn); adj. EBIT €672m** | Company | 28 Oct 2026 |
| Company releases (H1) | Rheinmetall H1 (6 Aug), Kongsberg Q2 (13 Jul), Saab Q2 (17 Jul), Thales H1 (23 Jul), Leonardo H1 (30 Jul), BAE H1 (30 Jul), Hensoldt H1 (31 Jul), Renk H1, CSG H1, TKMS 9M, Dassault H1, Airbus H1, Indra H1, Chemring interim, Kitron Q2, KNDS IPO documents | Company definitions (Rheinmetall backlog incl. frames) | Jul–Aug 2026 |
| Polskie Radio / Defense Post; Grosswald ammunition tracker; Business Insider | 2m shells by 2027; surplus early 2030s; filling lags forging; delivered output lags | — | 2025–26 `[E]` |
| Defense News / Militarnyi / Kongsberg | MBDA, Diehl, Kongsberg capacity | — | 2026 `[E]` |
| Morningstar / Breaking Defense (KNDS IPO) | IPO postponed; RHM −30% YTD; CSG −57% | — | Jul 2026 `[E]` |
| WisdomTree | Europe Defence index P/E | — | Jun 2026 `[E]` |
| FRED (OECD MEI) | 10-year yields DE, FR, IT, UK | Monthly average | Aug 2026 / 15 Sep 2026 |
| ECB via AllRatesToday | Reference FX | ECB reference | 7 Oct 2026 |
| Yahoo Finance | Peer prices, 52-week range, PE, earnings dates | — | 30 Oct 2026 closes |
| `docs/oil-market-bbb.md` | Brent paths for the Gulf row | ICE Brent | 24 Oct 2026 |
| `docs/hy-market-bbb.md` | Nordic GDP | — | 24 Oct 2026 (values of 5 Oct) |
| ICDS tracker | Plan context; CZ, ES, FR/IT/UK obstacles | — | 9 Jul 2026 `[E]` |

**Input assessment:**
- The run brief's DNB Carnegie reading (23 Oct: French 10y > 5%, OAT–Bund > 170 bp) is confirmed
  for 22–23 Oct by daily closes; it is a market print, used for the signpost only.
- Several search summaries mixed the 2025 and 2026 UK Budgets; only items dated 28 Oct 2026 with
  Chancellor Healey were used. Spain's 128 K9 order rests on one source and is held as `[?]`.
- Not obtained: the Kongsberg Q3 release directly (taken via kog v2); the French annulation decree
  (reported, not found); Italy's NATO-basis 2027 level; Sweden's new government and 2027 figures;
  Spain's 2027 budget; the October European Council conclusions (MFF); BTP–Bund after 6 Oct;
  Saab's Q3 backlog; Indra Q3 (29 Oct, not read).
