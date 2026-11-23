# Review: NVIDIA against rival AI chips (custom silicon, AMD) for LLMs — 23 Nov 2026

Static note (user question, 23 Nov 2026). No skill run; reads `docs/nvda-analysis.md` v2.1 (23 Nov,
P = $167.01) and the AI BBB 20 Nov note (`docs/ai-market-bbb.md`). Nothing applied to any document: the
user declined a competition sensitivity in the NVIDIA analysis for now (23 Nov); custom silicon stays a
signpost there. Tags: `[F]` filing, `[E]` press or tracker, `[K]` model knowledge to mid-2026, `[A]` own
arithmetic.

## 1. Question

Rival chips (Google TPU, Amazon Trainium, AMD, Microsoft Maia, Meta MTIA, OpenAI–Broadcom) are thought
to trail NVIDIA on memory and power, while the most advanced LLMs need Rubin. An agent task is a chain
of steps from CPU work to simple and advanced model calls, so the cheaper chips may suffice for much of
it. How big is the competition, how hard is it to build and industrialise such a chip, and is Rubin a
deal-breaker or do the slightly weaker chips threaten NVIDIA's margins?

## 2. Answer in brief

Rubin keeps NVIDIA at the top but does not end the competition. The rivals threaten NVIDIA not by
beating it but by being good enough for most tokens at a much lower cost to own. That caps NVIDIA's
pricing: a margin and share risk from 2028, not a leadership risk.

## 3. The premise, corrected

- **Frontier models already run off NVIDIA.** Gemini trains and serves on TPU. Anthropic uses TPU,
  Trainium and NVIDIA: S-1 commitments Google ≥ ~$121bn plus an estimated $125–150bn of further TPU
  compute, Amazon ≥ $110bn, Microsoft (NVIDIA hardware) ~$31bn `[F]` (per the AI BBB): most of its
  compute is not NVIDIA.
- **"Less memory" is not general.**

| Chip | HBM per chip | Scale-up domain | Source |
|---|---|---|---|
| NVIDIA Rubin | 288 GB HBM4, ~19–22 TB/s | 72 GPUs (Vera Rubin NVL72) | NVIDIA `[E]` |
| AMD MI450 | 432 GB HBM4 | 72 (Helios rack) | `[K]` |
| Google TPU Ironwood | 192 GB HBM3e | ~9,216 chips per pod | `[K]` |
| AWS Trainium 3 | 144 GB HBM3e | UltraServer | `[K]` |

  What decides is the cost per token of the whole system, not the spec of one chip.

## 4. The step model favours the rivals

- An agent task is CPU orchestration, retrieval, many cheap model calls and a few hard reasoning steps.
  Most tokens are cheap inference at volume on fixed models: the work custom chips are built for
  (predictable, high volume, priced on cost per token).
- NVIDIA's real edge: frontier training, new model architectures (flexibility), and the long tail of
  buyers that cannot build a chip (enterprise, sovereign, neoclouds). Frontier training is the slowest-
  growing part as inference takes over.

## 5. How hard is it to build and industrialise?

| Barrier | How hard | Who is past it |
|---|---|---|
| Chip design | ~$0.5–1bn+ and 3–4 years a generation `[K]`; Broadcom and Marvell supply SerDes, HBM interface and packaging | Hyperscalers with partners; Broadcom ~60% of custom chips by 2027 (Counterpoint `[E]`) |
| Factory and memory supply | TSMC N3/N2, CoWoS packaging and HBM sold out; NVIDIA has $390bn of supply commitments `[F]` | The largest buyers only: NVIDIA's strongest short-term moat |
| Software | CUDA is the default; JAX/XLA, PyTorch, Triton and vLLM erode it for firms running their own models | Google fully; Amazon and Anthropic mostly; AMD partly |
| Rack and networking | NVLink, rack design, annual cadence; AMD's first full rack (Helios) only now | NVIDIA leads, Google closest |
| Scale to justify the cost | Pays only with one's own huge workload | Google, Amazon, Meta, OpenAI (Broadcom 10 GW, AMD 6 GW `[K]`); Microsoft Maia has lagged |

Market shares (trackers, method-dependent `[E]`): NVIDIA ~70–85% of 2026 accelerator revenue (peak ~87%
in 2024); custom chips ~12–18% by revenue and ~28% of AI server shipments (TrendForce, +45% a year);
AMD ~5–7%.

## 6. Is Rubin a deal-breaker?

- **Performance: no contest.** NVIDIA claims ~10× lower cost per token than GB200 NVL72 (5× inference,
  3.5× training vs Blackwell) `[E]`; no independent benchmarks yet. It raises the bar the rivals chase
  each year.
- **Pricing: the rivals matter.** At a 71–75% gross margin a buyer pays ~4× NVIDIA's production cost. An
  in-house chip 30–40% weaker per chip can still win on total cost for its owner's own inference. A
  credible alternative alone caps what NVIDIA can charge the five largest buyers.
- **Signs already visible:**
  - Gross margin 71–72%, FY28 guided 72–73% `[F]`: NVIDIA cites supply costs, but price pressure
    can hide in the same number.
  - Customer funding, $75bn a year in the NVIDIA Base, works partly as a hidden discount: it keeps
    buyers on NVIDIA without cutting the list price.
  - Google sells TPU systems externally to ~100 customers `[E]`.

## 7. What it means for the valuation

- **Sensitivity `[A]`:** 1 pp of gross margin ≈ $0.21 of EPS on ~$600bn revenue (≈ 1.6% of Base 2028 EPS
  $12.93). A 5 pp give-back from 2028 ≈ −8% EPS; 10 pp of share lost in a flat market ≈ −12% revenue.
- **Verdict unchanged:** NVIDIA fails k = 12% at $167.01 on the funding issue alone (Base 9.4%, P_k
  $156.1). The Base carries only the FY28 margin guide; competition is further downside, held as the
  "Custom silicon; Taiwan" signpost, not a scenario.
- **Signposts:** NVIDIA data center below the AI BBB H1 path two quarters; gross margin < 71%; the
  OpenAI–Broadcom chip and AMD MI450 at volume in 2027; Google external TPU revenue.

## 8. Sources

- TechPowerUp, Rubin architecture: https://www.techpowerup.com/350947/nvidia-details-the-rubin-architecture-die-annotation-vera-cpu-hbm4-and-disaggregated-inference
- TechTimes, Vera Rubin ships: https://www.techtimes.com/articles/319203/20260627/nvidia-vera-rubin-ships-this-fall-8-cloud-partners-10x-lower-token-cost-hbm4-triples-bandwidth.htm
- The Register, Rubin at CES: https://www.theregister.com/2026/01/05/ces_rubin_nvidia/
- Silicon Analysts, value chain: https://siliconanalysts.com/research/ai-data-center-value-chain
- Presenc, custom silicon tracker: https://presenc.ai/research/hyperscaler-custom-silicon-tracker-2026
- Finviz / Counterpoint, Broadcom 60%: https://finviz.com/news/288744/broadcom-set-to-dominate-custom-ai-chip-market-with-60-share-by-2027-counterpoint-says
- AI World Today, custom chips: https://www.aiworldtoday.net/p/how-custom-ai-chips-are-challenging
