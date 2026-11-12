# Review: the KOSPI analysis as a basis for buying IQQK — quality and risk — 1 Nov 2026

**Reviewed:** `docs/kospi-analysis.md` version 1.6 (29 Oct 2026, IQQK followed) and its model
`.claude/skills/equity-market-bbb/references/fund/korea.py`.

**Skill revisions:**
- `iaf-valuation` **2026-10-29.1** (method reference; the document ran under 2026-10-18.2);
- `update-chain` **2026-10-29.1** (register check);
- `hy-market-bbb` 2026-10-24.1 (HY fund E / R read from `docs/hy-funds-analysis.md`, 31 Oct).

**New data:** Yahoo closes of **Fri 30 Oct** (Seoul 15:30 KST, Xetra 17:35 CET) for Samsung, the
preference share, SK hynix, SK Square, SK Inc, the 42-name rest sample, KOSPI, IQQK.DE, EUR/KRW and
EUR/NOK `[F]`. Every other number comes from the documents named. `[A]` marks my own runs: scratch
scripts that call `korea.py`'s own functions (paths, weights, fee and capping unchanged).

## Answer in brief

- **The quality is good.** `py korea.py SENS FUND IQQK TRIG` reproduces every v1.6 figure, the
  arithmetic in the tables checks out, inputs and tags are traceable, and the caveats are honest
  (the rest of Korea fails k; the margin rests on the 2027–28 memory payouts).
- **Four weak spots matter for a buy decision:**
  1. **The price is stale.** On 30 Oct IQQK's NAV-equivalent fell 3.35% in KRW (SK hynix −7.1%,
     Samsung −3.0%), and Xetra closed at EUR 98.45 (−5.6%). Re-marked on the model's own rules:
     Base 15.9%, margin +10.4%, **E / R 0.188** (was 0.167) `[A]`.
  2. **Korean withholding inside the fund is left out of Base.** Your rule keeps in-fund
     withholding in the return. Counting it costs about 0.5 pp of Base and 0.007 of E / R `[A]`.
  3. **The E / R trigger (EUR 97.4) uses a different convention from a re-run.** Re-priced the way
     the model re-prices, E / R reaches 0.196 at EUR ~99.8, not 97.4 `[A]`.
  4. **It compares only with the HY market reference (0.196).** Your HY funds stand at
     0.239–0.424 (31 Oct). A switch from one of them has to beat that fund. *User, 1 Nov: E / R
     against HY is the wrong test for this position; the question is the memory cycle (section 5).*
- **The risk is high and concentrated:**
  - half the fund is two memory makers;
  - the capped Bear loses 38.7% in 2027 in NOK (about 43% without the NOK cushion);
  - "adverse together" (memory values ×0.8, rest EPS ×0.9, rest exit −2) gives Base 6.0% and
    2027 −53.6%;
  - the Xetra price moved 5.6% in one day while Seoul was shut.
- **What it means at the 30 Oct close:**
  - IQQK clears k and is about on the HY market line: EUR ~98–99 on the Xetra-open basis.
  - It is **well short of the HY funds it would replace.** Matching Heimdal Høyrente N
    (0.239) needs EUR ~92; Sissener or Fondsfinans HY needs EUR ~71–78.
  - On the agreed rule it is at most a conditional move at a trigger. Model results, not personal
    advice.

## 1. Quality of the analysis

### What holds

| Check | Result |
|---|---|
| Model reproduces the document | Yes: every IQQK figure (Base 14.4%, margin +6.4%, Bear 0.2%, Bull 23.7%, capped −8.9% / −38.7%, E / R 0.167, triggers +6.4% / −6.9%) and all sensitivities |
| Company blocks reproduce their analyses | Samsung 23.3 / 5.2 / 34.3 / −10.5 and SK hynix 21.0 / 2.4 / 33.6 / −14.7 against the analyses within 0.1 pp (timing of D_t) |
| Table arithmetic `[A]` | Year returns (+21.5 / +8.9 / +14.1; capped −38.7 / +11.1 / +15.5), capital preserved, E = 14.4 − 4.37, R = 21.5 + 38.7, EUR hurdles (× 1.046) all agree |
| Inputs at 29 Oct | Current: Samsung v2 (29 Oct), SK hynix v2 re-priced, AI BBB Update 5, HY reference 0.196 (unchanged on 31 Oct) |
| Vehicle choice | Sound: a KID check at Nordnet; IQQK and LKOR level, and the swap counterparty breaks the tie |
| Honesty of the verdict | It says the rest of Korea fails k (7.4%), that about 4 pp of the 14.4% is the memory cycle, and that the NOK cushion in the Bear is doubtful |

### Weak spots, by effect on the decision

| # | Issue | Effect | Fix at the next run |
|---|---|---|---|
| 1 | **Price stale.** 30 Oct: Samsung −3.02%, preference −5.33%, SK hynix −7.08%, SK Square −5.88%, rest −1.66% (42-name sample); KOSPI 5,730.74 (−3.5%). NAV-equivalent −3.35% in KRW. Xetra: open EUR 100.64, close 98.45 | Re-mark `[A]`: Base **15.9%**, margin **+10.4%**, Bear 1.5%, capped −8.1% / 2027 −37.5%, **E / R 0.188** | Re-run at the latest Seoul close |
| 2 | **Withholding not in Base.** Korea withholds on dividends paid to the fund. The document has this only as a sensitivity (15% on all D_t, "upper bound", 13.4%) | 15% on all D_t is an upper bound because D_t also holds buybacks. At half of it (7.5%, a stand-in for the dividend share) `[A]`: Base −0.4 to −0.5 pp, E / R −0.007. On 30 Oct: 15.4% / +9.3% / 0.181 | Withholding on the cash-dividend part in Base; the full 15% as the sensitivity |
| 3 | **E / R trigger convention.** `TRIG` keeps every path fixed and leaves out the stub distribution (0.42). A re-run moves Base interim marks and the capped multiple with the price (the document's assumptions 3 and 5) | From 29 Oct, E / R = 0.196 at `[A]`: −6.9% (EUR 97.4) as the document has it; −6.3% (EUR 98.1) with the stub D added; **−4.6% (EUR 99.8)** with the model's own re-pricing. The published trigger is ~2 points stricter than its own re-run would give. The bid-ask and withholding lines also drop the stub D (13.4% is 13.6% with it) | Add the stub D in `TRIG` and the cost lines; compute the trigger with the re-pricing rules, or state both |
| 4 | **Benchmark.** E / R is set against the HY market reference only | The money would come from cash or from HY funds at 0.239 (Heimdal Høyrente N) to 0.424 (Fondsfinans Kreditt). Under the rule that a switch must beat what it replaces, the bar is higher (section 3) | Add a switch row against the fund that would be sold |
| 5 | **E / R depends on the path shape.** R uses the Base 2027 return (+21.5%). Most of it is the multiple glide that the company analyses put in 2027 | The same exit value with an even glide: R 60.2 → 56.1, E / R 0.167 → **0.179** `[A]`. About 0.01 of E / R is a timing convention, which is large next to the 0.029 gap to 0.196 | State this next to the verdict; no change to the rule |
| 6 | **Data age.** IQQK holdings from 31 Aug (iShares publishes daily). Rest weights from EWY (MSCI 25/50, not 20/35). Consensus from 26 Oct (SK hynix consensus +8% on 29 Oct not used). SK hynix is re-priced, not re-run | Small. The stub is price-flat and the December re-cap resets the weights | Take IQQK's daily holdings file at the next run |
| 7 | **Bookkeeping.** The header (line 200) corrects "Version 1.6" from inside version 1.6, with no change-log line. The DNB Teknologi row is 22 Oct (now Base 8.6%, E / R 0.110, 31 Oct). `iaf-valuation` is now 2026-10-29.1. The register showed rev 2026-10-29.1 for kospi while the header says 2026-10-18.2 (register fixed to the header) | No effect on IQQK's figures | Clean up at the next run |

- **The rest of Korea is a real cost of the vehicle, not a defect of the analysis.** It is 46% of
  IQQK and returns 7.4% in Base against 22.2% for the Samsung + SK hynix part. Buyability costs
  about 8 pp of Base. It also holds thesis-correlated names at consensus (Samsung C&T, Life, Fire,
  Samsung Electro-Mechanics, Hanmi), so its diversification is smaller than its weight suggests.

## 2. Risk of an IQQK position

| Risk | Size (NOK, after cost) | In the model? |
|---|---|---|
| **Memory cycle concentration** | 50.1% Samsung + SK hynix at the caps, 72% of CY27 earnings (80% with SK Square). Without the cycle, Base ~10.5% (below k). Memory values ×0.878 every year → Base = k | Yes |
| **Exit multiple** | Samsung + SK hynix exit P/E 10 → 8: Base 11.4% (fails k). Rest exit P/E −2: 11.6% | Yes (sensitivity) |
| **Stress** | Capped Bear: 2027 −38.7%, −8.9% a year, capital −23.5% at exit. Without the I-44 cushion: 2027 −43.0%. Adverse together: Base 6.0%, capped −16.7% a year, 2027 −53.6% `[A]` (the document prints only the 6.0%) | Yes |
| **Realised volatility** | IQQK 52-week range EUR 52.41–137.98, now −29% from the high. KOSPI −39% from the June record. Circuit breaker on 15 Oct; foreign selling above USD 10bn in October | No: a path the 3-year model does not price |
| **NOK / KRW** | Base flat. The Bear assumes NOK weakens 7.6% (a cushion) that the document itself doubts. NOK is near its 52-week high against EUR (EUR/NOK 10.27; 52-week low 10.24) | Partly |
| **Trading** | Xetra trades while Seoul is shut: the price is a market maker's estimate (30 Oct: open 100.64, close 98.45, Seoul closed all day). Nordnet spread unverified; Nordnet FX fee not in the model | No |
| **Index mechanics** | The MSCI review (~1 Dec) re-caps Samsung and SK hynix: it sells the winners in a rally. No re-capping gives 14.6% against 14.4% | Yes |
| **Vehicle** | Physical, securities lending (small counterparty risk); KID present, so the order should go through | Yes |
| **Tails** | Korean peninsula; US export controls on Korean memory sold to China; a reversal of Korea Value-up (the rest's exit P/E) | No (named) |
| **Overlap with the portfolio** | DNB Teknologi (2.6% of the total) already holds the same Samsung and SK hynix blocks. IQQK adds to the same memory factor | No (the analysis neither reads nor writes the portfolio) |

## 3. Where IQQK stands at the 30 Oct close `[A]`

These are re-marks on the model's own rules: unchanged paths and v1.6 weights, the 30 Oct Seoul
closes, stub 62 days. The EUR levels are on the Xetra-open basis (EUR 100.64 = NAV-equivalent on
30 Oct) at today's EUR/KRW.

| | No withholding | Withholding 7.5% of D_t | Withholding 15% (upper bound) |
|---|---|---|---|
| Base IRR / margin of safety | 15.9% / +10.4% | 15.4% / +9.3% | 15.0% / +8.1% |
| E / R (capped Bear) | 0.188 | 0.181 | 0.174 |
| Base = k (12%) | EUR ~111.1 (+10.4%) | | |

Further fall needed from 30 Oct before IQQK's E / R matches each comparison (kept for reference
only: the user does not use E / R against HY as the decision for this position, section 5):

| Comparison (E / R) | No withholding | Withholding 7.5% |
|---|---|---|
| HY market reference (0.196) | −1.3% → **EUR 99.3** | −2.4% → **EUR 98.2** |
| Heimdal Høyrente N (0.239) | −8.0% → EUR 92.6 | −9.1% → EUR 91.5 |
| Sissener Corporate Bond (0.347) | −23.0% → EUR 77.5 | −24.0% → EUR 76.5 |
| Fondsfinans High Yield (0.395) | −28.9% → EUR 71.5 | −30.0% → EUR 70.5 |

- **The 30 Oct Xetra close (EUR 98.45) is at the HY market line.** It includes moves after Seoul
  closed, so Monday's Seoul close decides where the NAV-equivalent actually is.
- **Against the HY funds you hold, IQQK does not pass at this price.** Heimdal Høyrente N, the
  weakest, would need a further ~8–9% fall.
- **The k hurdle barely moved** (EUR 111.3 → ~111.1): the paths are unchanged, so the price fall
  went into the margin of safety.
- These levels hold only at unchanged paths. The AI BBB is due an update after Amazon's Q3, and
  NVIDIA reports on 17 Nov. Either can move every row above.

## 4. Recommended changes for kospi-analysis v1.7

1. Re-run at the latest Seoul close, after the AI BBB update: the update chain runs ai before
   kospi.
2. Put the withholding on the cash-dividend part of D_t into Base. Keep 15% on all D_t as the
   upper-bound sensitivity.
3. `korea.py`: include the stub distribution in `TRIG` and in the cost sensitivities (a bug). The
   E / R trigger can go with the HY gate (section 5); the k hurdle is computed correctly.
4. ~~Add switch rows against the HY funds~~ (dropped, user 1 Nov). Lead with the memory cycle
   instead (section 5).
5. Refresh the DNB Teknologi row (31 Oct) and take IQQK's holdings from iShares' daily file.
6. Remove the self-referencing "Version 1.6 called…" note in the header and log the correction.

## 5. Follow-up (user, 1 Nov): the cycle, not the HY comparison

**User:** E / R against HY will almost always favour the less risky HY. Numbers are easy to
produce while the memory cycle is changing; that is irrelevant and bad analysis. The analysis
should ask whether the cycle continues, what can turn it, and whether that is likely.

**Assessment:**
- **Points 2 and 3.**
  - The withholding (2) should go into Base. It is a certain cost inside the fund and the user's
    rule keeps such costs. It is small (~0.5 pp) and decides nothing.
  - In 3, the missing stub payout is a bug and should be fixed. The trigger convention matters only
    for the E / R trigger, which goes if E / R against HY is no longer the gate.
- **Agreed: E / R against HY is not a useful gate for this position.**
  - HY's R is ~9 pp and an equity's 40–60 pp, so an equity needs about five times HY's excess
    return to tie. In this workspace no equity has cleared 0.196 except at deep discounts (World
    0.024, DNB Teknologi 0.110, the AI baskets).
  - The test says that equities are riskier than HY, which is known. It does not say whether this
    is a good equity opportunity.
- **Agreed: the IRR is mostly an echo of one assumption.** IQQK's k verdict flips with memory
  values ×0.88, or with an exit P/E of 8 instead of 10. Decimals on that are false precision.
- **One nuance: the market already expects the turn.**
  - Samsung and SK hynix trade at ~3× CY27 earnings, and the KOSPI is −39% from June. Memory
    shares usually turn a few quarters before memory earnings.
  - So the decisive question is whether the turn comes **later or shallower than the price
    assumes**. The model's one useful output is that implied path, in place of a precise IRR.

**What the cycle analysis should cover** (material already in `docs/ai-market-bbb.md`, H2, not yet
brought together):

| Question | Evidence now (AI BBB, company analyses) |
|---|---|
| Where are we? | DRAM contract prices Q4-26 +15–20%, Q1-27 +3–8% (slowing). 2027 HBM sold out. LTAs cover > 50% of 2027–28 capacity (SK hynix); Samsung targets 60–70%; Micron has > 75% of 2027 committed `[E]` |
| What can turn it: supply | Capex step-up (Samsung 2026 +60% and higher in 2027; SK hynix 2027 "significantly" higher, Yongin 2027); Micron fabs from mid-2027 and the 1δ / G11 node ramp in 2H-27 (bits for 2028); CXMT |
| What can turn it: demand | AI capex digestion after the contracted 2027 build; AI lab financing (the AI BBB's platform-funding signpost is already crossed); customer inventory built during the shortage |
| What can turn it: contracts | LTA price ranges renegotiated down; LTA floors still undisclosed (Q3 business reports ~mid-Nov) |
| How likely, and when | AI BBB Base already puts the turn in 2028 (EPS 0.60 → 0.40 of CY27 consensus), on the 2017–19 analogue `[A]`. Against an early or deep turn: LTA ranges, "tight through 2028" (Micron, Samsung). For it: the capex wave, node bits, Broadcom saying shortages are easing |
| What the price assumes | Not yet computed: the memory path at which IQQK returns k |
| Signposts | DRAM contract prices for 2H-27; LTA ranges and floors; foreign flows in Kospi; NVIDIA (17 Nov) and Micron (16 Dec) |

- **Where it belongs:** CLAUDE.md sets the memory view only in the AI BBB. So the cycle section is
  written there (the H2 layer). The kospi, Samsung and SK hynix analyses then lead with it, and the
  IRR shrinks to "what the price implies".
