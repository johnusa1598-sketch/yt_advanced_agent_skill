---
name: yt-originality
description: >-
  The pre-publish originality, AI-disclosure and safety gate for
  AI-generated videos: substance variation, the realistic-scene
  disclosure decision, health claims, dangerous moves, and a
  human sign-off. Use for "is this safe to publish", "do I need
  to disclose this", "is my channel at risk", or before
  `/yt-publish`.
---

# yt-originality

This is the highest-risk gate in the pack, because the three
rules behind it can each end a channel: reach cuts, demonetisation,
and removal. It is also the gate most AI channels skip, because
each rule is easy to trip over by accident. Run it before
`/yt-publish`, every time, and keep the human sign-off.

## Rule 1: Shorts originality prioritisation, 1 October 2026

YouTube updated Shorts recommendations to prioritise original
content and reduce the reach of content re-uploaded from other
creators without adding anything of your own. Channels primarily
aggregating or re-uploading without significant changes will
likely see less distribution. There is no Studio screen that tells
you your reach was cut; diagnosis is via Shorts-feed traffic
before and after 1 October.
**Three nuances (v3.3.6):** (a) this was a recommendation
change, not a new Community Guideline, YPP rule, or
monetisation rule — do not quote it as one; (b) the
judgement is channel-level ("primarily aggregating") and
reversible: a channel that starts adding its own substance
can recover distribution, it is not permanently flagged;
(c) Creator Insider's suggested alternative, second-hand:
share someone else's video via the Posts tab instead of
re-uploading it. That last point is reported, not verified
in Studio — flag it as such when you use it.

What does **not** count as original, per YouTube's own framing:

- A voiceover merely describing what is on screen.
- Small technical edits to someone else's clip.
- Applying the same template to many clips.

What does count: your own commentary, analysis, or storytelling
added to the material. For an AI channel, that means the video
must be yours in substance, not just in rendering.

## Rule 2: YPP "inauthentic content", 15 July 2025

This was a clarification, not a new ban on AI: mass-produced or
repetitive content is ineligible for monetisation regardless of
how it was made. The ineligible patterns YouTube names include
the same characters in the same situation repeatedly, image
slideshows with minimal narrative, and AI content made with
generic or unoriginal templates.

The test is substance, not surface. Varying the intro, the
outro, or the template while the video itself stays the same
does not pass. Each video must differ in what it teaches, shows,
or argues. `originality_scan.py` measures this mechanically: a
structure or phrase repeated across three or more recent uploads
is flagged for a human to look at.

One caution, stated plainly: a single third-party source reports
a July 2026 clarification naming repetitive AI video and synthetic
personas giving health, medicine, finance, or law advice as
ineligible. That list is **unverified against YouTube Help** and
is not quoted here as policy text. The advice it points to is
safe regardless: never let a synthetic persona give health
advice, and never build a channel on one repeated template.

## Rule 3: AI disclosure, and the gymnastics trap

Disclose, in Studio's AI-use attribute, realistic synthetic
content that a viewer could believe is real: a real person made
to appear to say or do something they did not, altered footage
of a real event or place, or a generated realistic scene that
did not occur.

**The gymnastics trap:** a photorealistic AI gymnast performing
a real-looking skill the viewer could believe is a real person
is exactly the realistic-scene case. Disclose it. A clearly
stylised or cartoon gymnast is not.

What does **not** require disclosure: AI-written scripts,
outlines, titles, thumbnails, and captions; your own voice
cloned for voiceover or dubs; minor edits. YouTube says
disclosure alone does not limit audience or monetisation
eligibility; consistent non-disclosure risks removal or YPP
suspension, and YouTube may apply a label itself, including
from C2PA metadata.

## May 2026 auto-labelling, reported (v3.2.0)

Reported by MediaNama and AIR Media-Tech from YouTube's
27 May 2026 announcement — treat this as reported policy,
not as text verified against YouTube Help in this pack:

- AI disclosure labels for photorealistic, meaningfully
  altered content are now shown more prominently and in one
  format: directly below the player on long-form, as an
  overlay on Shorts, and in the expanded description for
  animated, fictional, or lightly altered content.
- YouTube's systems now detect significant photorealistic
  AI use and apply the label themselves, even when the
  creator did not disclose it. Skipping disclosure therefore
  hides nothing; it only looks evasive.
- A mistaken auto-label can usually be corrected in Studio
  by answering "No" to the AI-use question — except for
  content made with YouTube's own tools (Veo, Dream Screen)
  or files carrying C2PA "fully generative" metadata, where
  the label is permanent.
- Practical rule, unchanged: disclose photorealistic AI
  yourself at upload, every time. Disclosure is free;
  non-disclosure is the risk.

## October 2026 additions (v3.3.6)

### AI-generated music labels

From 14 October 2026, YouTube Music rolls out player-page
labels for tracks "created primarily using generative AI",
identified through YouTube's own detection and music-partner
information; expansion to the main YouTube app is planned
with no date given. Sources: YouTube's announcement as
reported by Variety and ANI, 14–16 October 2026 — the
official blog URL was not verifiable at the time of writing,
so no blog link is cited here. Practical consequences for
this pack: (a) log whether a track is AI-generated in the
licence log (`/yt-sound`); (b) treat the label as a
transparency marker only — the announcement, as reported,
says nothing about recommendation or royalty effects, so do
not read the label as either; (c) partner declarations use
three categories — fully, partly, and no generative AI —
per trade coverage of YouTube's disclosure guidance, not
verified against the guidance itself, so check Studio before
relying on a category.

### Likeness detection: face live, voice announced

Correction to earlier pack wording: likeness detection is
face-only at the time of writing. Speaking-voice detection
was announced on 23 September 2026 for later in 2026, not
yet live. Enrolment opened to all creators aged 18 and over
in May 2026 and is not retroactive; since August 2026
disputes run in four categories with no revenue-sharing
option. The enrolment and dispute details are trade-press
reporting (see `/yt-algorithm`), not verified Help text.
For a channel built on a synthetic performer, the practical
rule is the same either way: the performer is disclosed,
and no real person's likeness is used without consent.

## Safety review, every video

- **Health claims:** no miracle claims, no guaranteed results,
  no synthetic persona giving health advice.
- **Dangerous moves:** a move that can injure needs warm-up,
  progression, and disclaimer language in the video itself, not
  just the description. Without them, cut the move.
- **Minors:** a minor-appearing subject means no idealised-body
  or weight framing, and the focus stays on the skill, not the
  body. YouTube limits repeated recommendations of
  idealised-body content to viewers aged 13-17.
- **Advertiser-friendly applies to the packaging too:**
  title, thumbnail, description, and tags are judged alongside
  the video, with three outcomes: full, limited, or no ads.

## How to run it

1. Run `skills/yt-originality/originality_scan.py` on a JSON
   list of your recent uploads (title, structure, repeated
   phrases, and the flags in the tool's help text).
2. Work the review items it returns, one by one. Each is a
   question for a human, not a verdict from a script.
3. Answer the disclosure question in Studio before upload,
   and record the answer in the publish checklist
   (`/yt-publish`).

## What this skill will never do

- No publishing or comment automation, no watermark removal,
  no re-upload guidance, and no template factory that varies
  only intro and outro. Those are the patterns the rules above
  punish, and this pack does not build them.
- No automated policy verdict. The tool flags; you decide.
  YouTube makes the call, and a script that pretends otherwise
  is worse than no script at all.

## The gate

Nothing here publishes. This skill hands back a review list and
a human sign-off line, ending with the question: **ship it, or
change it?**
