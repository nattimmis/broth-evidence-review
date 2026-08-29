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
