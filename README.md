# broth-evidence-review

Evidence review behind a nourishing bone-broth protocol for someone living with
**stage 4 cancer** and **liver cirrhosis** — and an audit of the health claims that
were attached to it.

> **Headline answer: NO.**
> No broth, spice, or cooking method destroys cancer cells or reverses cirrhosis.
> The recipe here is *supportive nutrition* — calories, protein and comfort for
> someone who struggles to eat. It is not a treatment and must not delay one.

## Why this repo exists

A proposed recipe — turmeric potentiated with black pepper, cinnamon, a 13-hour
boil, salty Mediterranean sides — was going to be sent to a person with liver
cirrhosis. Checked against the literature, **that specific combination is close to
the worst formulation you could hand a failing liver.** Three independent problems
stack up, and all three are cheap to fix.

## The three findings that changed the recipe

| # | Finding | Fix |
|---|---------|-----|
| 1 | Turmeric + **piperine** is the pattern implicated in turmeric-associated liver injury; piperine raises curcumin bioavailability ~20x | Culinary turmeric only. No piperine supplements, no "golden paste" megadoses |
| 2 | **Cassia** cinnamon is ~1% coumarin vs Ceylon's ~0.004% — a ~250x difference. One tsp of cassia can exceed the EFSA daily limit on its own | Use **Ceylon** cinnamon. Verify the species, not just the label word "cinnamon" |
| 3 | A 13-hour reduction salted in the pot destroys a **<2 g/day sodium** ceiling in one mug | Zero salt in the pot. Salt at the bowl, to taste |

## The finding that matters most

Bone broth protein is collagen: **zero tryptophan**, incomplete by PDCAAS, low in
the branched-chain amino acids that matter most in cirrhosis. A mug of broth is
soothing and hydrating and nutritionally close to hot water with personality.

Meanwhile the guidelines say protein should go **up**, not down — the old
protein-restriction dogma in liver disease has been overturned (EASL: 1.2–1.5 g/kg/day).
And a **late-evening snack** is specifically recommended, because cirrhotic livers
burn through glycogen overnight and go catabolic.

**So: broth is the vehicle, not the payload.** Put real protein in it.

## Contents

| Path | What's in it |
|------|--------------|
| [`RECIPE.md`](RECIPE.md) | The recipe card, liver-safe, plain ASCII for copy-paste |
| [`docs/01-hepatotoxicity.md`](docs/01-hepatotoxicity.md) | Turmeric DILI, cassia coumarin, dose thresholds |
| [`docs/02-cirrhosis-nutrition.md`](docs/02-cirrhosis-nutrition.md) | EASL protein targets, late-evening snack, collagen quality, sodium |
| [`docs/03-food-safety.md`](docs/03-food-safety.md) | *Vibrio vulnificus*, lead in bone broth, immunocompromised handling |
| [`docs/04-cancer-claims.md`](docs/04-cancer-claims.md) | What curcumin trials actually show; fibrosis regression, honestly |
| [`data/claims.json`](data/claims.json) | Every claim → verdict → evidence, machine-readable |
| [`data/sources.json`](data/sources.json) | Source list with type and what each supports |

## Method

Claims were checked against clinical practice guidelines (EASL, AASLD), the
Drug-Induced Liver Injury Network case series, EFSA toxicological limits, and
peer-reviewed primary literature. Where the evidence is weak or contested, that is
stated rather than smoothed over. Nothing here is sourced to a supplement vendor.

## Not medical advice

Research notes, not clinical guidance. Anyone on chemotherapy should disclose every
supplement to their oncologist — high-dose antioxidants and CYP-inhibiting compounds
can interact with the drugs doing the actual work. Anyone with cirrhosis should take
dietary changes to their hepatologist, because sodium, protein and fluid targets are
individual and change with decompensation.

---

# Part two — the full diet, and the root cause

The original review answered a narrow question about a bone-broth recipe. It has since
been extended into a complete dietary review, driven by one fact that reorders
everything: **the underlying cause here is alcohol.**

That makes abstinence the treatment, not a lifestyle note sitting beside the diet.
Every food question below is support for it.

> **Live dashboard:** [c60.ch/rob/](https://c60.ch/rob/) — charts, timelines and a
> self-updating evidence feed.

## What part two establishes

| Finding | Where |
|---|---|
| **Coffee is the only food with strong hepatology evidence** — 38% lower rate of alcohol-related cirrhosis per extra 2 cups/day, and the effect survives in decaf | [`05`](docs/05-diet-and-antioxidants.md) |
| **Berries and antioxidants are null** on every liver marker ever measured (15 RCTs, n=1,028) | [`05`](docs/05-diet-and-antioxidants.md) |
| **The "sponge" idea is right about the destination and wrong about the object** — the gut toxin problem is real; oats bind bile acids, not poisons | [`06`](docs/06-gut-liver-axis.md) |
| **Survival curves do not separate until ~78 weeks of abstinence** — people quit just before it works | [`07`](docs/07-alcohol-the-root-cause.md) |
| **Chicken and fish are protective; saturated animal fat carries a 3.5× rate of liver-disease death** | [`08`](docs/08-protein-meat-and-fat.md) |
| **The same supplement built body protein at night and did nothing in the daytime** | [`08`](docs/08-protein-meat-and-fat.md) |
| **Treating gum disease halved blood endotoxin and improved MELD and cognition in 30 days** | [`09`](docs/09-oral-health.md) |
| **"Dark brown bread" is not automatically low-salt** — colour tells you nothing, read the pack | [`10`](docs/10-interactions-and-traps.md) |
| **Live kefir is a genuine hazard for an immunocompromised person** — and this is food, not just capsules | [`12`](docs/12-fermented-foods-and-blends.md) |

## Contents added

| Path | What's in it |
|------|--------------|
| [`docs/05-diet-and-antioxidants.md`](docs/05-diet-and-antioxidants.md) | Coffee, berries, greens, tea, and where the antioxidant story runs out |
| [`docs/06-gut-liver-axis.md`](docs/06-gut-liver-axis.md) | Endotoxaemia, ammonia, lactulose and rifaximin, and the "sponge" claim audited |
| [`docs/07-alcohol-the-root-cause.md`](docs/07-alcohol-the-root-cause.md) | Abstinence timeline, survival, relapse, and the drugs that are safe in cirrhosis |
| [`docs/08-protein-meat-and-fat.md`](docs/08-protein-meat-and-fat.md) | Before/after trial numbers, the meat and fat risk table, protein sources |
| [`docs/09-oral-health.md`](docs/09-oral-health.md) | Periodontal therapy in cirrhosis; the orange-juice-swirling claim audited |
| [`docs/10-interactions-and-traps.md`](docs/10-interactions-and-traps.md) | Sodium arithmetic, drug–food interactions, listeria, iron, aflatoxin |
| [`docs/11-evidence-watch.md`](docs/11-evidence-watch.md) | How the page keeps itself current, and what the automation deliberately cannot do |
| [`docs/12-fermented-foods-and-blends.md`](docs/12-fermented-foods-and-blends.md) | Kefir safety, greens, the breakfast blend, and the real rate limits |
| [`tools/watch.py`](tools/watch.py) | The scheduled PubMed watcher behind the live feed |

## A note on method

Two corrections were made to already-published material during this work, and both are
worth recording rather than hiding:

1. A survival statistic ("75% vs 21–27%") had been published to the live page from a
   **search-engine summary**. It could not be traced to a primary source and was
   replaced with a verified figure. A search summary is not a source.
2. The advice that the strict neutropenic diet had "fallen out of favour" was current
   when written and **stopped being settled in December 2025**, when a phase III trial
   was halted early for excess infections on the liberalised diet.

Both are the reason [`docs/11-evidence-watch.md`](docs/11-evidence-watch.md) keeps
interpretation out of the automation. The machine finds the papers; a person decides
what they mean.
