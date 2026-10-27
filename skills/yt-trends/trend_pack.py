#!/usr/bin/env python3
"""trend_pack.py - build a hashtag and keyword pack from a seed topic.

    python3 trend_pack.py "beam backflip" --niche "AI gymnastics" --brand "Aria Fit"
    python3 trend_pack.py "beam backflip" --evidence evidence.json --json

Evidence file (JSON, all optional):
    {"trending_titles": ["..."], "tags_seen": ["#gymnastics", ...],
     "searches": ["beam backflip tutorial", ...],
     "date": "2026-10-20"}

Evidence is dated (v3.3.6): pass --evidence-date, or put "date" in
the evidence file. Evidence older than 30 days is flagged stale -
a tag pack built on it is a guess about last month, not this one.

Honest by design: this tool fetches nothing live. Tags marked "evidence"
come from words and hashtags the user pasted in; tags marked "heuristic"
come from the seed topic and the documented tiers below. A tag is a
suggestion to test, not a claim that it is trending right now.

Tiers:
  broad   - the big words anyone in the niche types
  niche   - the seed topic plus long-tail combinations
  branded - the channel and series name, so a series compounds
Search-intent clusters name the question behind the query, because a
title written for the wrong intent loses even when it ranks.
"""
import json, os, re, sys
from collections import Counter
from datetime import date

STOP = {"the", "a", "an", "and", "or", "of", "to", "in", "on", "for", "with",
        "is", "are", "it", "this", "that", "you", "your", "how", "what",
        "why", "vs", "best", "new", "top", "my", "i", "we", "be", "do",
        "does", "did", "can", "try", "tried", "get", "got", "make", "made"}

def words(text):
    return [w for w in re.findall(r"[a-z0-9']+", text.lower()) if w not in STOP]

def hashtags(text):
    return [h.lower() for h in re.findall(r"#([A-Za-z0-9_]+)", text)]

def clean_tag(tok):
    tok = re.sub(r"[^a-z0-9]", "", tok.lower())
    return tok

def title_case(words_):
    return " ".join(words_)

def _parse_date(raw):
    try:
        parts = [int(p) for p in str(raw).strip().split("-")]
        return date(*parts)
    except (ValueError, TypeError):
        return None


def build(seed, niche="", brand="", evidence=None, evidence_date=None):
    seed_w = words(seed)
    if not seed_w:
        return None
    ev = evidence or {}
    ev_titles = ev.get("trending_titles", []) or []
    ev_tags = ev.get("tags_seen", []) or []
    ev_searches = ev.get("searches", []) or []

    # --- evidence: repeated words and hashtags the user actually saw
    word_counts = Counter()
    for t in ev_titles + ev_searches:
        word_counts.update(words(t))
    ev_hash = Counter()
    for t in ev_titles + ev_tags + ev_searches:
        ev_hash.update(hashtags(t))
    # evidence-backed keywords: words that repeat across the evidence
    ev_keywords = [w for w, c in word_counts.most_common(12) if c >= 2]
    ev_tag_list = [f"#{h}" for h, _ in ev_hash.most_common(10)]

    seed_phrase = title_case(seed_w)
    seed_tag = "#" + "".join(seed_w)
    niche_w = words(niche)

    broad = []
    for w in niche_w:
        broad.append(f"#{w}")
    for w in ["shorts", "viral", "fyp"]:
        broad.append(f"#{w}")
    broad = list(dict.fromkeys(broad))

    niche_tags = [seed_tag]
    for extra in ["tutorial", "challenge", "fail", "tips", "training", "skills"]:
        niche_tags.append("#" + "".join(seed_w) + extra)
    for w in ev_keywords:
        if w not in seed_w:
            niche_tags.append("#" + w)
    niche_tags = list(dict.fromkeys(niche_tags))[:12]

    branded = []
    for name in (brand,):
        if name:
            branded.append("#" + re.sub(r"[^a-z0-9]", "", name.lower()))
            for w in words(name):
                branded.append("#" + w)
    branded = list(dict.fromkeys(branded))

    clusters = {
        "how-to": f"how to {seed_phrase}",
        "challenge": f"{seed_phrase} challenge",
        "fail-or-win": f"{seed_phrase} fail or win",
        "best-of": f"best {seed_phrase}",
        "comparison": f"{seed_phrase} vs beginner",
        "trend-jack": f"{seed_phrase} trend",
    }
    title_keywords = list(dict.fromkeys(
        seed_w + ev_keywords[:6] + ["challenge", "fail", "tutorial"]))

    ev_date = _parse_date(evidence_date or ev.get("date"))
    stale = bool(ev_date and (date.today() - ev_date).days > 30)
    return {
        "seed": seed,
        "niche": niche,
        "brand": brand,
        "evidence_date": ev_date.isoformat() if ev_date else None,
        "evidence_stale": stale,
        "evidence_used": bool(ev_titles or ev_tags or ev_searches),
        "hashtags": {
            "broad": broad,
            "niche": niche_tags,
            "branded": branded,
            "evidence_seen": ev_tag_list,
        },
        "title_keywords": title_keywords,
        "search_intent_clusters": clusters,
        "notes": [
            "Tags marked from evidence came from text you pasted in. "
            "Everything else is a heuristic from the seed topic.",
            "No live trend data was fetched. Re-check in YouTube search "
            "and your own Studio traffic sources before you trust a tag.",
            "Use at most 3-5 hashtags on a Short, 15 tags total on a "
            "long video. Relevance beats volume; an unrelated tag is "
            "against the terms and teaches the algorithm the wrong audience.",
        ],
    }

def show(pack):
    print(f"\n  Hashtag pack: {pack['seed']}")
    if pack.get("evidence_date"):
        stale = " - STALE (over 30 days old), re-check before trusting it" \
            if pack.get("evidence_stale") else ""
        print(f"  evidence dated: {pack['evidence_date']}{stale}")
    if pack["evidence_used"]:
        print("  (built from your evidence + heuristics; nothing fetched live)")
    else:
        print("  (no evidence supplied - all heuristic. Paste trending titles "
              "for an evidence-backed pack.)")
    for tier, tags in pack["hashtags"].items():
        if tags:
            print(f"\n  {tier.upper()}")
            print("   " + " ".join(tags))
    print("\n  TITLE KEYWORDS")
    print("   " + ", ".join(pack["title_keywords"]))
    print("\n  SEARCH-INTENT CLUSTERS")
    for k, v in pack["search_intent_clusters"].items():
        print(f"    {k:<14} {v}")
    print()
    for n in pack["notes"]:
        print(f"  note: {n}")
    print()

def main():
    a = sys.argv[1:]
    as_json = "--json" in a
    niche, brand, ev_path, ev_date, seed_parts = "", "", None, None, []
    i = 0
    while i < len(a):
        arg = a[i]
        if arg == "--json":
            pass
        elif arg == "--niche" and i + 1 < len(a):
            niche = a[i + 1]; i += 1
        elif arg == "--brand" and i + 1 < len(a):
            brand = a[i + 1]; i += 1
        elif arg == "--evidence" and i + 1 < len(a):
            ev_path = a[i + 1]; i += 1
        elif arg == "--evidence-date" and i + 1 < len(a):
            ev_date = a[i + 1]; i += 1
        elif not arg.startswith("--"):
            seed_parts.append(arg)
        i += 1
    ev = None
    if ev_path and os.path.exists(ev_path):
        ev = json.load(open(ev_path, encoding="utf-8"))
    seed = " ".join(seed_parts)
    if not seed:
        print(__doc__); sys.exit(1)
    pack = build(seed, niche, brand, ev, ev_date)
    if pack is None:
        print(__doc__); sys.exit(1)
    if as_json:
        print(json.dumps(pack, indent=1)); return
    show(pack)

if __name__ == "__main__":
    main()
