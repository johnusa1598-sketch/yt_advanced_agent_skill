#!/usr/bin/env python3
"""package_builder.py - assemble one publish-ready package from a video brief.

    python3 package_builder.py brief.json
    python3 package_builder.py brief.json --json
    python3 package_builder.py brief.json --trends trends.json

Brief JSON fields (all plain text, nothing fetched):
    title_idea  - the working title or subject, e.g. "beam backflip"
    hook        - the spoken or on-screen hook line
    format      - "short" or "long" (default: short)
    duration_s  - length in seconds (default: 30)
    beats       - [{"time": "0-3s", "text": "what happens"}] (for text layers)
    cta         - the one call to action, e.g. "follow for part 2"
    series      - series name, e.g. "Skill Challenge"
    channel     - channel name, e.g. "Aria Fit"
    audience    - who it is for, e.g. "gymnastics fans, 13-25"
    keywords    - extra keywords, optional list

Optional --trends file: the JSON output of trend_pack.py, used for the
hashtag line and the tag list. Without it, hashtags come from the brief.

The package is a draft to copy, check and change. Title variants are
built from templates with the brief's own subject and numbers - no
invented statistics, no copied lines from other creators. The title
and thumbnail must carry different words (see title.py), so every
variant is checked against the thumbnail text.
"""
import json, os, re, sys

def words(t):
    return re.findall(r"[a-z0-9']+", (t or "").lower())

def first_subject(title_idea):
    w = [x for x in words(title_idea) if x not in
         {"the", "a", "an", "how", "to", "my", "i"}]
    return " ".join(w[:3]) if w else title_idea

def title_variants(brief):
    subject = first_subject(brief.get("title_idea", ""))
    hook = (brief.get("hook") or "").strip()
    series = brief.get("series", "")
    n = re.search(r"\d+", brief.get("title_idea", "") or "")
    num = n.group(0) if n else ""
    cands = [
        (f"I tried the {subject} - only 1 landing stuck",
         "contrast + specificity: a named skill, one outcome, no vague adjective"),
        (f"Can she land the {subject}?",
         "open question up front: the viewer clicks to resolve it"),
        (f"{subject} in one take - no cuts",
         "front-loaded subject plus a concrete production claim"),
        (f"She fell {num + ' times' if num else 'twice'} before this {subject}",
         "failure first: the hook is the cost, the landing is the payoff"),
        (f"Watch the landing, not the flip - {subject}",
         "curiosity gap: redirects attention to the part people rewatch"),
    ]
    if series:
        cands.append((f"{series}: the {subject} that took all week",
                     "series frame: returning viewers recognise the arc"))
    out = []
    for t, why in cands:
        issues = []
        if len(t) > 100:
            issues.append("over YouTube's 100-character hard limit")
        elif len(t) > 60:
            issues.append("truncates in desktop search near 60 characters")
        if len(words(t)) > 12:
            issues.append("long for a feed - the subject may not survive")
        out.append({"title": t, "chars": len(t), "ctr_reasoning": why,
                    "issues": issues})
    return out

def text_layers(brief):
    layers = []
    for b in brief.get("beats", []) or []:
        txt = (b.get("text") or "").strip()
        if not txt:
            continue
        onscreen = txt
        w = onscreen.split()
        if len(w) > 5:
            onscreen = " ".join(w[:5])
        layers.append({
            "time": b.get("time", ""),
            "on_screen": onscreen,
            "full_beat": txt,
            "style": "bold sans, high contrast, centre or lower third, "
                     "max 5 words on screen at once",
        })
    if not layers and brief.get("hook"):
        layers.append({"time": "0-3s", "on_screen": brief["hook"][:40],
                       "full_beat": brief["hook"],
                       "style": "bold sans, high contrast, centre"})
    return layers

def build(brief, trends=None):
    fmt = (brief.get("format") or "short").lower()
    dur = int(brief.get("duration_s") or (30 if fmt == "short" else 600))
    titles = title_variants(brief)
    thumb = {
        "text": "LAND IT?" if fmt == "short" else titles[0]["title"][:24],
        "elements": ["the hardest moment, frozen mid-action",
                     "one face, one reaction, no clutter",
                     "high contrast; text is 3 words at most"],
        "rule": "thumbnail words must differ from the title words - "
                "the pairing carries twice the information",
    }
    hashtags = []
    if trends:
        h = trends.get("hashtags", {})
        hashtags = (h.get("branded", []) + h.get("niche", [])[:5])[:8]
    else:
        base = first_subject(brief.get("title_idea", ""))
        hashtags = ["#" + re.sub(r"[^a-z0-9]", "", w)
                    for w in base.split() if w][:3] + ["#shorts"]
        hashtags = list(dict.fromkeys(hashtags))
    desc_lines = [
        f"{titles[0]['title']}. {brief.get('hook', '')}".strip(),
        "",
        f"{brief.get('channel', '')} - {brief.get('series', '')}".strip(" -"),
        f"For {brief.get('audience', 'anyone learning this skill')}.",
        "",
        " ".join(hashtags),
    ]
    tags = list(dict.fromkeys(
        words(brief.get("title_idea", "")) + words(brief.get("series", "")) +
        words(brief.get("niche", "")) + (brief.get("keywords") or [])))[:15]
    timing = {
        "guidance": "Post when YOUR audience is on, not when a blog says so: "
                    "check Studio -> Analytics -> Audience -> 'when your "
                    "viewers are on YouTube' and pick the first evening "
                    "peak of your own week.",
        "default_if_no_data": "late afternoon to early evening in the "
                              "audience's timezone, on the series' usual day",
        "cadence_note": "A series compounds only on a rhythm. Same day, "
                        "same slot, every week beats random uploads.",
    }
    ab = {
        "test": "title A vs title B, thumbnail held constant",
        "variant_a": titles[0]["title"],
        "variant_b": titles[1]["title"] if len(titles) > 1 else titles[0]["title"],
        "metric": "click-through rate in the first 48 hours, judged "
                  "against the channel's own median, not a global benchmark",
        "decision_rule": "Keep the winner only if it also holds average view "
                         "duration. A click that leaves is a worse video, "
                         "not a better title.",
        "duration": "48 hours, or 1,000 impressions, whichever comes first",
    }
    return {
        "format": fmt,
        "duration_s": dur,
        "titles": titles,
        "thumbnail_brief": thumb,
        "description": "\n".join(desc_lines),
        "tags": tags,
        "hashtags": hashtags,
        "text_layers": text_layers(brief),
        "end_screen_cta": brief.get("cta", "follow for part 2"),
        "pinned_comment": f"Which part was hardest - the flip or the landing? "
                          f"Tell me and I will film {brief.get('series', 'part 2')} "
                          f"around your answer.",
        "upload_timing": timing,
        "ab_test": ab,
        "checklist": ["AI disclosure added if any visual or sound is AI generated",
                      "title and thumbnail words do not repeat",
                      "first two description lines carry the search words",
                      "end screen and pinned comment set before publish"],
    }

def show(pkg):
    print(f"\n  PACKAGE - {pkg['format']} {pkg['duration_s']}s")
    print("\n  TITLES (with CTR reasoning)")
    for i, t in enumerate(pkg["titles"], 1):
        print(f"    {i}. \"{t['title']}\" ({t['chars']} chars)")
        print(f"       why: {t['ctr_reasoning']}")
        for iss in t["issues"]:
            print(f"       x {iss}")
    print("\n  THUMBNAIL BRIEF")
    print(f"    text: {pkg['thumbnail_brief']['text']}")
    for e in pkg["thumbnail_brief"]["elements"]:
        print(f"    - {e}")
    print(f"    rule: {pkg['thumbnail_brief']['rule']}")
    print("\n  DESCRIPTION")
    print("   " + pkg["description"].replace("\n", "\n   "))
    print("\n  TAGS: " + ", ".join(pkg["tags"]))
    print("  HASHTAGS: " + " ".join(pkg["hashtags"]))
    print("\n  TEXT LAYERS / CAPTIONS")
    for l in pkg["text_layers"]:
        print(f"    [{l['time']}] {l['on_screen']}")
    print(f"\n  END SCREEN CTA: {pkg['end_screen_cta']}")
    print(f"  PINNED COMMENT: {pkg['pinned_comment']}")
    print("\n  UPLOAD TIMING")
    print(f"    {pkg['upload_timing']['guidance']}")
    print(f"    default: {pkg['upload_timing']['default_if_no_data']}")
    print("\n  A/B TEST")
    print(f"    A: {pkg['ab_test']['variant_a']}")
    print(f"    B: {pkg['ab_test']['variant_b']}")
    print(f"    metric: {pkg['ab_test']['metric']}")
    print(f"    rule: {pkg['ab_test']['decision_rule']}")
    print()

def main():
    a = sys.argv[1:]
    as_json = "--json" in a
    trends, files = None, []
    i = 0
    while i < len(a):
        arg = a[i]
        if arg == "--json":
            pass
        elif arg == "--trends" and i + 1 < len(a):
            if os.path.exists(a[i + 1]):
                trends = json.load(open(a[i + 1], encoding="utf-8"))
            i += 1
        elif not arg.startswith("--"):
            files.append(arg)
        i += 1
    if not files or not os.path.exists(files[0]):
        print(__doc__); sys.exit(1)
    brief = json.load(open(files[0], encoding="utf-8"))
    pkg = build(brief, trends)
    if as_json:
        print(json.dumps(pkg, indent=1)); return
    show(pkg)

if __name__ == "__main__":
    main()
