# Weekly update

The running report of the update chain (`update-chain` skill): the weekly run on Saturdays (Mode E)
and the daily company news search on weekdays (Mode F). Newest entry first. The bookkeeping is in
`docs/update-register.md`; the numbers are in the documents themselves.

## Daily news — Wednesday 25 Nov 2026

- **Updated:** `dof` 13.1% → 12.6%, **marginal (flipped from clears)** at NOK 126.00: mostly the price (+1.6%); the Skandi Forza sale and charterback is about NAV-neutral (−0.09 pp) `[F]`.
- SK hynix (skh) −10.8% to KRW 1,030,000 and Samsung (smsn) −9.9% to 170,700 in Seoul after the US chip sell-off; price only, both still clear by wide margins `[F]`.
- Minor: Hafnia dividend form, Trustly Q3 and Norse Q3 not out by 08:00; NVIDIA 10-Q not filed yet; Borr insurance receipt unconfirmed; Scatec flagging notice; no fund-house forum posts.

**Needs you:** DOF (held) flipped clears → marginal; it clears again at NOK 125.3 or less and fails above NOK 130.4.

**Left for next run:** `dnb`, `stb` (stale date only, no news; Saturday). On hold (user): `defense`, `kog`, `rhm`, no news.

**Register:** Forza sale event done; Forza delivery (Q4, watch) added.

## Daily news — Tuesday 24 Nov 2026

- **Updated:** none (no report in the window; no item moves a value the documents read).
- Price only, verdict bands at the 24 Nov close vs each P_k: NVIDIA (nvda) $155.38, fails → marginal (+0.5%); Micron (mu) $629.79, clears → marginal (+0.8%); Microsoft (msft) $496.13, clears → marginal (+0.2%); Alphabet (googl) $279.05, marginal → fails (−5.5%) `[F]`.
- DOF (dof, held) NOK 126.00: clears → marginal (+1.1%), price only `[F]`.
- NVIDIA (nvda): Commerce put Megaspeed and Alibaba's Apex on the Entity List; Huang testifies to Senate Banking next week `[E]`. Goes into the 10-Q run.
- Anthropic (anthropic) $81.91, below its $83 IPO price; still fails `[F]`.
- Minor: BNP cuts Micron to Neutral `[E]`; Kuo says Google TPU-8i 2027 orders −20% `[E]`; KOSPI +7%; Borr insurance not yet confirmed; no fund-house forum posts.

**Left for next run:** `dnb`, `stb` (stale date only, no news; Saturday). On hold (user): `defense`, `kog`, `rhm`, no news.

**Register:** Korea support and Amazon–Decart closed; Huang testimony/GTC (~1 Dec) added; Entity List note added to the NVIDIA 10-Q event.

## Daily news — Monday 23 Nov 2026

- **Updated:** none (no report in the window; no item moves a value the documents read).
- NVIDIA (nvda): Bessent says the administration "needs answers" on China chip sales and compliance; Trump urges the board to rehire Huang; board has ruled it out `[E]`. Already in v2.0's probe and leadership lines.
- Market (equity, ai): worst week since 2020 (S&P −8.6%, SOX −17%); KOSPI −5% today; Korea eases buyback limits from 24 Nov `[F]`.
- Trump threatens a "tremendous tax" on US firms building data centres abroad (msft, googl, amzn; AI BBB owns it) `[E]`.
- TSMC and Samsung (tsm, smsn) paused advanced-chip shipments to China-designed customers under the 16 Nov BIS rule (FT `[E]`); TSMC China ~5% of revenue.
- Minor: Heimdal forum yields HH N 10.33%, HH+ 10.91% `[E]`; Amazon–Decart ~$7.5bn; YouTube ~$3bn settlement; Borr insurance due 24 Nov.

**Left for next run:** `dnb` (stale since 21 Nov, no news; Saturday). SK hynix and Samsung re-mark: in progress elsewhere (10:00 task). On hold (user): `defense`, `kog`, `rhm`, no news.

**Register:** added Borr insurance (24 Nov), Korea support (24 Nov), Amazon–Decart (~27 Nov), BIS foundry pause (21 Dec); Heimdal 4 Dec event extended.

## Week 47 — Saturday 21 Nov 2026 (scheduled run)

Skill revisions: `update-chain` 2026-11-12.2; `supply-market-bbb` 2026-11-18.1; `iaf-valuation` 2026-11-18.1.
*Run complete. After the three runs the check shows list 1 empty; there were no loop checks.*

### Check (21 Nov)

- List 1 (3 items, in order): `supply` (Subsea7 Q3 19 Nov; Equinor AHTS tender checkpoint 20 Nov), `dof` (same two events; DOF ex-dividend 20 Nov), `global-index` (stale since 17 Nov; equity, ai, nvda, hy changed).
- Deferred: `kospi` (own update 30 Nov). On hold (user): `defense`, `borr`, `capt`, `kog`, `rhm`, `shb`. `portfolio`: never run unattended.
- Run list: `supply` and `global-index` in parallel (no link between them), then `dof` on the new supply baseline.
- Housekeeping: entries before 7 Nov moved to `docs/log/weekly-update-2026-11.md` and `docs/log/weekly-update-2026-10.md`.

### News sweep (14–21 Nov; company news from the daily entries of 17, 18 and 20 Nov and this week's runs)

- **Oil (oil):** IEA OMR 13 Nov: 2027 demand growth +2.0 mb/d, unchanged; 2026 −2.7 mb/d; larger 2027 surplus `[F]`. Below the 0.5 mb/d trigger: read at the oil run before OPEC+ (29 Nov).
- **US–China (nvda, ai, shipping):** Trump–Xi at APEC Shenzhen 18–19 Nov: no chip or port-fee agreement found; US says it does not negotiate export controls `[E]`.
- **Ukraine (defense, on hold):** Abu Dhabi talks 10–11 Nov: a prisoner-swap deal, no ceasefire, no date for the next round `[F]`.
- **NVIDIA (nvda):** Huang agreed to testify behind closed doors, no date set (Moolenaar via BGov `[E]`). The SEC-probe report is already in v2.0.
- **Tankers (shipping):** VLCC rates fell more than 60% from their record by 13 Nov; FFAs point to a peak `[F]`. Already in the 13 and 18 Nov shipping runs.
- **Norges Bank (hy):** 4.5% held on 4 Nov; next decision 17 Dec. No Nordic HY default or bondholder notice found for held issuers beyond `hy-issuers` of 19 Nov.
- **Register:** eight passed `watch` events closed with outcomes; none surprised (commit a5c425d).

### Progress

- **`supply`, done, kept** (recorded, stale after 12 Dec; commit a14127f). Equinor AHTS term tender: no award by 21 Nov, so the AHTS turn call (Base 2027 £52k) holds; reversal deadline 31 Jan. Subsea7 Q3: utilisation 84% (Q2 85%), book-to-bill 0.5, backlog $12.5bn, 2027 guide ~$8bn; NS CSV watch call kept flat. Events added: AHTS reversal deadline (31 Jan), Subsea7 Q4 (~26 Feb).
- **`dof`, done, changed yes, flipped marginal → clears** (recorded, stale after 18 Dec; commit abc1edd). Ex-dividend re-mark at NOK 124.00 (20 Nov) / USD/NOK 9.750: Base 12.8% → 13.1%, P_k NOK 127.4, margin +1.8% → +2.7% (bottom of the clears band; fails above NOK 130.0). No sector row moved; the krone +0.20 pp, the close below the dividend-adjusted price +0.15 pp. A.P. Møller Maritime bought 1.85m more shares 19–20 Nov (2.8m over 18–20 Nov, ~1.1%).
- **`global-index`, done, changed yes, still fails** (recorded, stale after 6 Dec; commit 68489c1). v7, DNB Global Indeks A only (Nordnet Global Indeks dropped, user 1 Nov), NAV 835.76 (19 Nov): Base after cost 4.58% → 6.66%, P_k NAV 703 → 723, margin −19.0% → −13.5%, E / R 0.008 → 0.081. Compacted 808 → 405 lines. Register: inputs amzn and mu added.

### Summary

- **`dof` flipped to clears:** Base 13.1%, margin +2.7%. The cause is the ex-dividend price and the krone; no sector row moved.
- **`global-index` still fails** but is nearer: 6.66%, −13.5%. On the indicative 20 Nov NAV of ≈ 812.5 the margin is −10.6% and the pre-alert at NAV 830 is crossed.
- **Supply BBB kept unchanged:** no Equinor AHTS award, and Subsea7's Q3 is steady. No Base path moved.

### Updated

| Document | Changed or kept | What moved | Stale after |
|---|---|---|---|
| `supply` | kept | Nothing; turn-call families and signposts re-read (Equinor tender, Subsea7 Q3) | 12 Dec |
| `dof` | changed | Base 12.8% → 13.1%; P_k NOK 130.6 → 127.4 at NOK 124.00; margin +1.8% → +2.7%; **marginal → clears** | 18 Dec |
| `global-index` | changed | Base 4.58% → 6.66%; P_k 703 → 723; margin −19.0% → −13.5%; fails; E / R 0.008 → 0.081 | 6 Dec |

### Needs you

- `dof` (a holding) **flipped from marginal to clears**, at the bottom of the band. It fails again above NOK 130.0.
- `global-index`: the pre-alert (NAV 830) is likely crossed on the 20 Nov NAV, which is due about 23 Nov (watch event added).
- A register row from another session, "User request (21 Nov): re-mark SK hynix and Samsung at the 23 Nov Seoul close", was in the working copy. It was committed with the supply record (a14127f); Monday's daily run picks it up.
- Not obtained: the Petrobras PSV 4500 / 3000 bid ranking (not public), the November North Sea spot print, and Nordnet's "Total pris" for the fund cost (0.25% carried).
- Flags only, no action asked: the Equity BBB `world3.py` lacks the GOOGL v2.3 and NVIDIA v2.0 interim values (Base −0.03 pp). The AI BBB E-rest row's Bear exit P/E of 17 sits above where Meta and Oracle trade.

### Left for next run

- `kospi`: deferred to its own update on 30 Nov (smsn, skh and ai changes waiting).
- `oil`: stale after 30 Nov; OPEC+ on 29 Nov with 2027 quotas, then its downstream as the change gate flags.
- `sed`: Q3 on 27 Nov, in the daily run.
- On hold (user): `defense` (5 causes waiting), `rhm` (3), `borr` (1), `capt`, `kog`, `shb`.

### Events in the next 14 days

- 23 Nov: DNB Global Indeks A NAV of 20 Nov (pre-alert test); skh and smsn re-mark at the Seoul close (user request).
- 25 Nov: Trustly Q3; Norse Atlantic Q3 (approx.); NVIDIA 10-Q; Anthropic closing 8-K; Hafnia dividend form; Petrobras PSV 3000 bareboat bids.
- 26 Nov: SSB Q3 national accounts. 27 Nov: SED Q3; German 2027 budget (on hold); Petrobras plan 2027–31 (approx.); Westwood rig dashboard; Frontline Q3.
- 29 Nov: OPEC+ (2027 quotas). 30 Nov: CAPT Q3 (on hold); MSCI review effective; SK hynix dividend record; DRAM/NAND contract prints; Dooba and Point deadlines; DOF dividend paid.
- 1 Dec: Transocean–Valaris closing; Booster standstill ends; GPU rental indices. ~4 Dec: November *Seabreeze* (AHTS and PSV Q4 test); Heimdal November reports; Polish budget vote.

## Daily news — Friday 20 Nov 2026

- **Updated:** `anthropic` Base 3.8% → −4.6%, fails (re-mark at the $97.17 first close; P_k $58.9).
- **Updated:** `amzn` Base 5.2% → 7.7%, fails (Anthropic stake at market, $338.6bn).
- **Updated:** `googl` Base 9.1% → 10.9%, fails narrowly (margin −3.0%).
- **Updated:** `msft` Base 9.6% → 11.9%, **marginal (flipped)**, from the price alone.
- Anthropic (anthropic, amzn, googl, msft): IPO priced at $83, above the $70–78 range; upsized to 980m shares (~$81bn); first close $97.17 (+17%) `[F]`.
- Minor: no new fund-house forum posts; DOF $0.40 goes ex today; Alphabet C$ notes; Microsoft Ignite (products only).

**Needs you:** `msft` flipped to marginal. Subsea7's Q3 (19 Nov) is not read yet. Left for Saturday's weekly run: `supply`, `dof`, `tsm`, `global-index`.

**Register:** added Anthropic closing 8-K (~25 Nov), quiet-period end (~14 Dec) and one-year lock-up (18 Nov 2027); Alphabet ex-dividend (7 Dec); Microsoft AGM (8 Dec) and dividend declaration (~15 Dec).

## Daily news — Wednesday 18 Nov 2026

- **Updated:** `nvda` Base 17.7% → 20.7%, clears (Q3 $115.8bn, Q4 guide $130bn; cascade −15.2%).
- **Updated:** `hafnia` Base −0.5% → 7.4%, fails (Q3; P_k NOK 81.6 vs 90.00).
- Hafnia (hafnia): TORM stake to be paid out as special dividend (~$1.28/share), else 90% cash; form set 25 Nov `[F]`.
- NVIDIA (nvda, ai): GM guide 71–72%, supply commitments $390bn, $1.8bn stake impaired; BIS remote-access rule issued 16 Nov `[F]`.
- DOF (dof, supply): Skandi Africa re-contracted by TechnipFMC, "Very Large" ($100–200m), in direct continuation; term not given (17 Nov, added from user input) `[F]`.
- DOF (dof): A.P. Møller Maritime buys 950k shares at NOK 128.01 (NOK 121.6m) after Fredriksen's ~NOK 900m (Finansavisen, user input) `[E]`.
- Minor: Hofseth corrected Q3; Anthropic prices tonight; Trump–Xi in Shenzhen; fund-house forum posts unchanged.

**Needs you:** `ai` is due its rebuild: NVIDIA's guide sits at its Bull row. SED Q3 not out yet; Petrobras PSV ranking not public. `supply`, `mu`, `tsm`, `global-index` left.

**Register:** added NVIDIA Q4 (~24 Feb), Hugging Face closing, Hafnia dividend form (25 Nov), Hafnia Q4 (~26 Feb).

## Daily news — Tuesday 17 Nov 2026

- **Updated:** none. No tracked company reported or had material news since the 16 Nov runs.
- NVIDIA (nvda): Q3 FY27 out tonight ~22:20 CET, call 23:00; consensus revenue ~$108.8bn against the $108bn guide; runs tomorrow `[F]`.
- Anthropic (anthropic, amzn, googl): book ~6× covered, bankers weigh pricing above $70–78; pricing 18 Nov, so a re-mark is likely `[E]`.
- Borr (borr, on hold; hy-issuers): Q3 confirmed for 18 Nov after the NYSE close, call 19 Nov `[F]`.
- Minor: fund-house forum posts unchanged since 10 Nov; Hafnia and SED report tomorrow morning.

**Needs you:** `hafnia` is in list 1 only for TORM's ex-dividend; left for tomorrow's Q3 run. Petrobras PSV tender opens today (`supply`, weekly run).

**Register:** Borr Q3 date set firm (18 Nov). No events added.

## Daily news — Thursday 12 Nov 2026

- **Updated:** `nvda` Base 20.9% → 19.8%, clears (re-mark at $173.73; Base kept, no board decision yet).
- NVIDIA (nvda): board met on Huang after a second affair report; search firm hired, interim CEO weighed; −8.6% after hours `[E]`.
- NVIDIA (nvda, ai): BIS rule on Chinese remote chip access via Malaysia, Singapore, Thailand reportedly near `[E]`.
- DOF (dof, on hold): Q3 EBITDA ex gains $219m (+13%), backlog $7.0bn, dividend $0.40 ex 20 Nov `[F]`.
- Minor: TSMC ADR +5% on 11 Nov; MSFT −2.3%; Alphabet HKD/SGD bonds; Amazon Italy VAT probe; Micron $1bn into Anthropic; Anthropic book oversubscribed.

**Needs you:** DOF's Q3 is out; its hold waits for the Supply check. `rig`, `shipping`, `supply` and `shb` (Riksbank) are left for the weekly run.

**Register:** nvda recorded. Added: NVIDIA board decision (12 Nov), BIS rule (~30 Nov), DOF ex-dividend (20 Nov).

## Daily news — Wednesday 11 Nov 2026

- **Updated:** `tsm` Base 13.7% → 9.5%, **fails (flipped)**: price +12.6% to $396.48; October revenue +59.7% y/y, above the +45% signpost; stub kept.
- **Updated:** `amzn` Base 6.6% → 5.2%, fails (price re-mark at $270.87).
- **Updated:** `googl` kept, Base 9.1%, fails.
- Anthropic (googl, amzn, ai): S-1/A of 10 Nov, range $70–78, Q3 revenue $17.0bn; both stakes sit near carrying value; pricing ~18 Nov `[F]`/`[E]`.
- NVIDIA (nvda): CEO probe goes on, board hired Wachtell; read at the 17 Nov Q3 run `[E]`.
- CoreWeave (ai): Q3 revenue $3.66bn, FY26 guide raised to $13.0–13.3bn, backlog $132.5bn `[F]`.
- Minor: HH+ yield 10.65% NOK (Heimdal Erik `[E]`); Claude for Word vs MSFT; Taptravel outcome not out.

**Needs you:** `tsm` flipped to fails. The 11 Nov holds (rig, shipping, supply, Oslo names, shb) end today, and DOF reports tomorrow. `oil`, `hy` and `ai` are left in list 1.

**Register:** googl, amzn, tsm recorded. Anthropic pricing moved to 18 Nov. Added: TSMC board (done), November revenue ~10 Dec, dividends ex 10 Dec and 11 Mar.

## Daily news — Tuesday 10 Nov 2026

- **Updated:** none. No tracked company reported or had material news since 9 Nov.
- Taptravel (hy-issuers): written-procedure vote closed 9 Nov; no outcome notice found yet `[F]`.
- Anthropic (googl, amzn, ai): still no price range or share count in the S-1/A of 2 Nov; roadshow timing is press-reported only `[E]`.
- Minor: Sissener October report (+0.2%, yield 7.7%) already in hy-funds; Heimdal and Fondsfinans forum posts unchanged since 5 Nov; TSMC October revenue not yet out.

**Needs you:** `oil` (stale since 7 Nov) and `hy`/`hy-issuers` (Taptravel event) are in list 1; they are market baselines, left for the weekly run or you.

**Register:** no events added; Taptravel vote event stays open until the outcome is out.

## Daily news — Monday 9 Nov 2026

- **Updated:** none. No tracked company reported or had material news over the weekend.
- Taptravel (hy-issuers): bondholder written-procedure vote closes today 15:00 CET (new SEK 50m share issue, senior bonds 8% PIK, overdue interest paid in cash after); outcome not yet out `[F]`.
- Anthropic (googl, amzn, ai): S-1/A of 2 Nov still has no price range or share count; roadshow expected from ~10 Nov `[E]`.
- Minor: fund-house forum posts (Heimdal, Sissener, Fondsfinans) are unchanged since 4 Nov; Fondsfinans Oct reports already read.

**Register:** no events added; Taptravel vote and Anthropic roadshow events stay open. `oil` and `hy-issuers`/`hy-funds` remain in list 1 (stale and Hofseth covenant event); left for the weekly run or the user.

## Week 45 — Saturday 7 Nov 2026 (scheduled run)

Skill revisions: `update-chain` 2026-11-05.2; `ai-market-bbb` 2026-11-06.1; `iaf-valuation` 2026-11-01.1.
*In progress — this entry is written as the run goes.*

### Check (7 Nov)

- List 1 has 28 items. `hy`'s anchor-spread event (6 Nov) was already used in the 5 Nov update: marked done, no re-run.
- `defense` and `rhm` stay on hold (user, per the daily entries 4-6 Nov): not run.
- `portfolio`: never run unattended.
- Run list (max 6): `ai` (equity changed 6 Nov) first, then `googl`, `borr`, `amzn`, `msft`, `hy-issuers` as capacity allows.

### Progress

- **`ai`, done, changed yes (prices only)** (recorded, stale after 17 Nov). Update 7: no path moved. Equity 6 Nov and HY reference 0.254 read; all six baskets return 10.0% Base NOK at the 6 Nov close; memory basket 21.6%, margin +28.1%. TSMC ADS is 1.7% above its hurdle price (marginal band). Event added: CoreWeave Q3 (10 Nov).
- **`googl`, `borr`: running** (two in parallel). Then `amzn`, `msft`, `hy-issuers` if capacity allows.
