#!/usr/bin/env python3
"""
Evidence watch for c60.ch/rob/

Design rule: RETRIEVAL IS DETERMINISTIC. Every entry this produces carries a real
PMID that resolves at pubmed.ncbi.nlm.nih.gov. No model writes any part of a
citation, so the classic failure mode -- a confidently fabricated reference --
cannot occur here.

Quality gating is done by PubMed itself, not by judgement: each query is
restricted to human studies with abstracts whose publication type is a
randomised trial, meta-analysis, systematic review or practice guideline.

Output is a JSON file the page fetches client-side. The page's HTML is never
machine-rewritten, so a failure here degrades to "watch section absent" rather
than a corrupted page.
"""

import json, os, re, sys, time, tempfile, urllib.parse, urllib.request
from datetime import datetime, timezone

EUTILS   = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"
TOOL     = "c60-rob-evidence-watch"
STATE    = "/var/lib/evidence-watch"
OUT      = "/var/www/c60.ch/rob/evidence.json"
LOG      = os.path.join(STATE, "watch.log")
SEEN     = os.path.join(STATE, "seen.json")
QUEUE    = os.path.join(STATE, "queue.json")

KEEP          = 60     # entries retained in the public feed
WINDOW_DAYS   = int(os.environ.get("WATCH_WINDOW_DAYS", "10"))  # look-back per run; daily runs + dedupe catch late indexing
MAX_PER_TOPIC = int(os.environ.get("WATCH_MAX_PER_TOPIC", "12"))

# Hard quality gate, applied by PubMed rather than by a model.
FILTER = ('AND (randomizedcontrolledtrial[pt] OR "meta-analysis"[pt] '
          'OR systematicreview[pt] OR practiceguideline[pt] OR guideline[pt]) '
          'AND humans[mh] AND hasabstract')

TOPICS = [
  ("fibrosis-regression", "Cirrhosis & fibrosis regression",
   '("liver cirrhosis"[MeSH] OR "liver fibrosis"[tiab]) AND (regression[tiab] OR reversal[tiab] OR recompensation[tiab])'),
  ("alcohol", "Alcohol-related liver disease & abstinence",
   '("liver diseases, alcoholic"[MeSH] OR "alcoholic cirrhosis"[tiab]) AND (abstinence[tiab] OR "alcohol use disorder"[tiab] OR baclofen[tiab] OR naltrexone[tiab] OR acamprosate[tiab])'),
  ("nutrition", "Nutrition, protein & sarcopenia in cirrhosis",
   '("liver cirrhosis"[MeSH]) AND (nutrition[tiab] OR protein[tiab] OR sarcopenia[tiab] OR "late evening snack"[tiab] OR malnutrition[tiab] OR "branched chain"[tiab])'),
  ("encephalopathy", "Hepatic encephalopathy & the gut-liver axis",
   '("hepatic encephalopathy"[MeSH] OR endotoxemia[tiab] OR "gut-liver axis"[tiab]) AND (lactulose[tiab] OR rifaximin[tiab] OR probiotic*[tiab] OR fiber[tiab] OR fibre[tiab] OR ammonia[tiab])'),
  ("hcc", "Hepatocellular carcinoma - systemic therapy & survival",
   '("carcinoma, hepatocellular"[MeSH]) AND (atezolizumab[tiab] OR durvalumab[tiab] OR tremelimumab[tiab] OR lenvatinib[tiab] OR "overall survival"[tiab] OR immunotherapy[tiab])'),
  ("diet", "Diet, coffee & food exposures in liver disease",
   '("liver cirrhosis"[MeSH] OR "carcinoma, hepatocellular"[MeSH] OR "fatty liver"[MeSH]) AND (coffee[tiab] OR diet[tiab] OR "mediterranean diet"[tiab] OR polyphenol*[tiab] OR anthocyanin*[tiab] OR fiber[tiab] OR "red meat"[tiab] OR sodium[tiab])'),
  ("oral", "Oral health & the liver",
   '(periodont*[tiab] OR "oral health"[tiab] OR "oral microbiome"[tiab]) AND (cirrhosis[tiab] OR "liver disease"[tiab] OR encephalopathy[tiab])'),
  ("safety", "Supplement & herbal hepatotoxicity",
   '("chemical and drug induced liver injury"[MeSH] OR hepatotoxicity[tiab]) AND (turmeric[tiab] OR curcumin[tiab] OR "green tea"[tiab] OR supplement*[tiab] OR herbal[tiab] OR cinnamon[tiab] OR coumarin[tiab])'),
]


def log(msg):
    line = "%s  %s" % (datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%SZ"), msg)
    print(line, flush=True)
    try:
        os.makedirs(STATE, exist_ok=True)
        with open(LOG, "a") as f:
            f.write(line + "\n")
    except Exception:
        pass


def get(url, tries=3):
    last = None
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": TOOL})
            with urllib.request.urlopen(req, timeout=45) as r:
                return r.read().decode("utf-8", "replace")
        except Exception as e:
            last = e
            time.sleep(2 + 3 * i)
    raise last


def load(path, default):
    try:
        with open(path) as f:
            return json.load(f)
    except Exception:
        return default


def save_atomic(path, obj):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    d = os.path.dirname(path)
    fd, tmp = tempfile.mkstemp(dir=d, suffix=".tmp")
    try:
        with os.fdopen(fd, "w") as f:
            json.dump(obj, f, ensure_ascii=False, indent=1)
        os.chmod(tmp, 0o644)
        os.replace(tmp, path)
    except Exception:
        try:
            os.unlink(tmp)
        except Exception:
            pass
        raise


def esearch(query):
    q = "%s %s" % (query, FILTER)
    url = "%s/esearch.fcgi?%s" % (EUTILS, urllib.parse.urlencode({
        "db": "pubmed", "term": q, "retmode": "json", "retmax": MAX_PER_TOPIC,
        "datetype": "edat", "reldate": WINDOW_DAYS, "sort": "date", "tool": TOOL}))
    data = json.loads(get(url))
    return data.get("esearchresult", {}).get("idlist", []) or []


PT_RANK = [("Practice Guideline", "guideline"), ("Guideline", "guideline"),
           ("Meta-Analysis", "meta-analysis"), ("Systematic Review", "systematic review"),
           ("Randomized Controlled Trial", "randomised trial")]


def esummary(pmids):
    if not pmids:
        return {}
    url = "%s/esummary.fcgi?%s" % (EUTILS, urllib.parse.urlencode({
        "db": "pubmed", "id": ",".join(pmids), "retmode": "json", "tool": TOOL}))
    return json.loads(get(url)).get("result", {})


def classify(pubtypes):
    for needle, label in PT_RANK:
        if any(needle.lower() == p.lower() for p in pubtypes):
            return label
    return "study"


def clean(s):
    s = re.sub(r"<[^>]+>", "", s or "")
    return re.sub(r"\s+", " ", s).strip()


def main():
    seen = set(load(SEEN, {}).get("pmids", []))
    queue = load(QUEUE, {}).get("items", [])
    added = 0

    for key, label, query in TOPICS:
        try:
            ids = esearch(query)
            time.sleep(0.4)
            fresh = [i for i in ids if i not in seen]
            if not fresh:
                log("%-22s %2d hits, 0 new" % (key, len(ids)))
                continue
            res = esummary(fresh)
            time.sleep(0.4)
            n = 0
            for pmid in fresh:
                rec = res.get(pmid)
                if not isinstance(rec, dict) or not rec.get("title"):
                    continue
                queue.append({
                    "pmid": pmid,
                    "topic": key,
                    "topicLabel": label,
                    "title": clean(rec.get("title")),
                    "journal": clean(rec.get("fulljournalname") or rec.get("source")),
                    "date": clean(rec.get("pubdate")),
                    "kind": classify(rec.get("pubtype") or []),
                    "url": "https://pubmed.ncbi.nlm.nih.gov/%s/" % pmid,
                    "found": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
                })
                seen.add(pmid)
                n += 1
            added += n
            log("%-22s %2d hits, %d new" % (key, len(ids), n))
        except Exception as e:
            log("%-22s FAILED: %s" % (key, e))

    # newest first, capped
    order = {"guideline": 0, "meta-analysis": 1, "systematic review": 2,
             "randomised trial": 3, "study": 4}
    queue.sort(key=lambda x: (x.get("found", ""), -order.get(x.get("kind"), 9)), reverse=True)
    queue = queue[:KEEP]

    save_atomic(QUEUE, {"items": queue})
    save_atomic(SEEN, {"pmids": sorted(seen)[-4000:]})
    save_atomic(OUT, {
        "generated": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "added": added,
        "tracked": len(seen),
        "windowDays": WINDOW_DAYS,
        "filter": "human studies with abstracts; RCTs, meta-analyses, systematic reviews and guidelines only",
        "items": queue,
    })
    log("run complete: %d new, %d in feed, %d PMIDs tracked" % (added, len(queue), len(seen)))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as e:
        log("FATAL: %s" % e)
        sys.exit(1)
