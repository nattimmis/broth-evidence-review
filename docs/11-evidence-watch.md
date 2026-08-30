# 11 — The evidence watch: how this stays current

A scheduled job checks for new evidence every morning and publishes what it finds to
the live page at [c60.ch/rob/](https://c60.ch/rob/). This document explains what it
does, and — more importantly — what it deliberately does **not** do.

## The design rule

**Retrieval is deterministic. Interpretation is not automated.**

The single largest risk in automating a medical evidence page is a language model
inventing a citation, or quietly drifting the editorial line toward whatever sounds
hopeful. Both are well-documented failure modes, and during the research for this
repository a statistic that had already been published to the page had to be
retracted because it came from a search-engine summary rather than a primary source.

So the job is built the other way round from a typical "research agent":

- The search is a **PubMed E-utilities database query**, not a model being asked what
  it remembers. Every entry carries a PMID that resolves.
- **No model writes any part of a citation**, a title, a journal name or a date. Those
  fields come straight from the PubMed record.
- The job **cannot edit anything above the watch section**. It writes one JSON file.
  The page's hand-written content is untouchable by the automation.

## The quality gate

Filtering is done by PubMed itself, not by judgement. Every query is restricted to:

```
AND (randomizedcontrolledtrial[pt] OR "meta-analysis"[pt] OR systematicreview[pt]
     OR practiceguideline[pt] OR guideline[pt])
AND humans[mh] AND hasabstract
```

Randomised trials, meta-analyses, systematic reviews and practice guidelines in
humans, with abstracts. Nothing else is admitted — no preprints, no press releases,
no supplement-vendor content, no animal work.

## The eight standing queries

| Topic | Watching for |
|---|---|
| `fibrosis-regression` | cirrhosis regression, reversal, recompensation |
| `alcohol` | alcohol-related liver disease, abstinence, baclofen/naltrexone/acamprosate |
| `nutrition` | protein, sarcopenia, late-evening snack, malnutrition |
| `encephalopathy` | lactulose, rifaximin, probiotics, ammonia, endotoxaemia |
| `hcc` | hepatocellular carcinoma systemic therapy and survival |
| `diet` | coffee, Mediterranean diet, polyphenols, fibre, red meat, sodium |
| `oral` | periodontal disease and the liver |
| `safety` | supplement and herbal hepatotoxicity — turmeric, green tea, cinnamon |

## Operationally

- `systemd` timer `evidence-watch.timer`, daily at 06:17 UTC with up to 20 minutes of
  randomised delay, `Persistent=true` so a missed run catches up.
- Runs as an unprivileged user with `RuntimeMaxSec=600`.
- 10-day look-back window per run; daily runs plus PMID de-duplication catch anything
  indexed late.
- State in `/var/lib/evidence-watch/` (`seen.json`, `queue.json`, `watch.log`).
- Output is `evidence.json`, written atomically beside the page and fetched
  client-side. **If the job fails, the page loses the watch section and nothing else.**

## What still needs a human

Everything that matters. The feed is an intake queue, and the page says so in the
section banner. Deciding whether a new trial actually changes a conclusion — whether
the sample size is adequate, whether the endpoint is surrogate, whether it supersedes
something already plotted — is judgement, and judgement is not scheduled.

The honest division of labour is: **the machine finds the papers, a person decides
what they mean.**

Source: [`tools/watch.py`](../tools/watch.py)
