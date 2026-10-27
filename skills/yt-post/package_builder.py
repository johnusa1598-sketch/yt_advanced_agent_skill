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
and thumbnail must carry different words (see title.py), so the
thumbnail text is derived from the brief's hook minus the words of
title variant 1, never hardcoded (v3.3.6). Re-check the pairing
against the title you actually publish.

Brief fields added in v3.3.6:
    comparison_sides - ["side A", "side B"] in video order, for a
        challenge/comparison Short. The pinned comment becomes the
        vote naming both sides (yt-post vote rule). A comparison
        brief without sides produces a warning, not a vote.
    beats entries may carry "end" (seconds or "8s"): the text
        layer's end. A layer ending past its beat's end is flagged
        (text-end rule, yt-post / yt-qa).
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

THUMB_STOP = {"the", "a", "an", "how", "to", "my", "i", "it", "is",
              "was", "this", "that", "can", "you", "do", "we", "they",
              "he", "her", "his", "its", "in", "on", "of", "for",
              "with", "and", "or", "but", "so", "if", "then", "than",
              "from", "one"}


def thumbnail_text(brief, titles):
    """Derive thumbnail text from the hook, minus title variant 1's
    words, so the pairing carries twice the information. Falls back
    to the subject, then to the hook's first words. Never hardcoded."""
    title_words = set(words(titles[0]["title"]))
    hook_words = [w for w in words(brief.get("hook", ""))
                  if w not in THUMB_STOP and w not in title_words]
    if hook_words:
        return " ".join(hook_words[:3]).upper()
    subject_words = [w for w in words(brief.get("title_idea", ""))
                     if w not in THUMB_STOP and w not in title_words]
    if subject_words:
        return " ".join(subject_words[:3]).upper()
    return " ".join(words(brief.get("hook", ""))[:3]).upper()


def _secs(value):
    """Parse '8s', '8', or 8 into seconds; None when unparseable."""
    if value is None:
        return None
    if isinstance(value, (int, float)):
        return float(value)
    m = re.match(r"^\s*(\d+(?:\.\d+)?)\s*s?\s*$", str(value))
    return float(m.group(1)) if m else None


def _range_end(time_range):
    m = re.match(r"^\s*(\d+(?:\.\d+)?)\s*-\s*(\d+(?:\.\d+)?)\s*s?\s*$",
                 str(time_range or ""))
    return float(m.group(2)) if m else None


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
        beat_end = _range_end(b.get("time", ""))
        end = _secs(b.get("end")) if b.get("end") is not None else beat_end
        layers.append({
            "time": b.get("time", ""),
            "on_screen": onscreen,
            "full_beat": txt,
            "end_s": end,
            "beat_end_s": beat_end,
            "ends_past_beat": bool(end is not None and beat_end is not None
                                   and end > beat_end),
            "style": "bold sans, high contrast, centre or lower third, "
                     "max 5 words on screen at once",
        })
    if not layers and brief.get("hook"):
        layers.append({"time": "0-3s", "on_screen": brief["hook"][:40],
                       "full_beat": brief["hook"],
                       "end_s": 3.0, "beat_end_s": 3.0,
                       "ends_past_beat": False,
                       "style": "bold sans, high contrast, centre"})
    return layers


def pinned_comment(brief):
    """Vote rule (v3.3.2, yt-post): on a comparison/challenge Short
    the pinned comment names both sides in video order. Returns
    (comment, warning); warning is set when the brief claims a
    comparison but supplies no sides."""
    sides = brief.get("comparison_sides") or brief.get("sides") or []
    if len(sides) >= 2:
        return (f"Team {sides[0]} or Team {sides[1]} - which wins? "
                f"Vote in the comments.", None)
    if brief.get("comparison"):
        return (f"Which part was hardest - the flip or the landing? "
                f"Tell me and I will film {brief.get('series', 'part 2')} "
                f"around your answer.",
                "comparison Short without sides: the pinned comment must "
                "be the vote naming both sides in video order (yt-post). "
                "Add comparison_sides to the brief.")
    return (f"Which part was hardest - the flip or the landing? "
            f"Tell me and I will film {brief.get('series', 'part 2')} "
            f"around your answer.", None)

def build(brief, trends=None):
    fmt = (brief.get("format") or "short").lower()
    dur = int(brief.get("duration_s") or (30 if fmt == "short" else 600))
    titles = title_variants(brief)
    thumb = {
        "text": thumbnail_text(brief, titles),
        "elements": ["the hardest moment, frozen mid-action",
                     "one face, one reaction, no clutter",
                     "high contrast; text is 3 words at most"],
        "rule": "thumbnail words must differ from the title words - "
                "the pairing carries twice the information",
        "check": "derived from the hook minus title variant 1's words; "
                 "re-check against the title you actually publish "
                 "(title.py)",
    }
    pin, pin_warning = pinned_comment(brief)
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
        # v3.3.6: no generic default. FINAL §20.6 trusts only the
        # channel's own heatmap; without one, keep the series day
        # and record the heatmap as the first post-publish task.
        "default_if_no_data": "No generic best-time default. Publish on "
                              "the series' usual day and record the "
                              "Audience heatmap as the first post-publish "
                              "task; the heatmap becomes the timing source.",
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
        "pinned_comment": pin,
        "pinned_comment_warning": pin_warning,
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
        flag = " x ends past its beat" if l.get("ends_past_beat") else ""
        print(f"    [{l['time']}] {l['on_screen']}{flag}")
    print(f"\n  END SCREEN CTA: {pkg['end_screen_cta']}")
    print(f"  PINNED COMMENT: {pkg['pinned_comment']}")
    if pkg.get("pinned_comment_warning"):
        print(f"  PINNED COMMENT WARNING: {pkg['pinned_comment_warning']}")
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
