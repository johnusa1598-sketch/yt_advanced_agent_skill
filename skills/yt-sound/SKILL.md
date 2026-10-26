---
name: yt-sound
description: >-
  Background music and sound design for a video: mood and tempo
  mapped to the video's energy, licence-safe sources, meme sound
  effects, ducking, and loop points for Shorts. Use for "what music",
  "background music", "sound design", "what song for this Short",
  "audio feels flat".
---

# yt-sound

Sound is half the retention curve and almost none of the planning.
A viewer who cannot hear the video still watches it if the captions
work; a viewer who hears music fighting the voice leaves. This skill
plans the sound before the edit, not after it.

## Mood and tempo, mapped to energy

Pick the video's energy first, then the music. The ranges below
are production practice, not platform rules - a slow track under a
fast cut feels wrong at any tempo, and that feeling is the test.

| Video energy | What is happening | Tempo guide | Music job |
| --- | --- | --- | --- |
| Calm / tutorial | One skill, taught slowly | 70-95 BPM, sparse | Stay out of the way; the voice teaches |
| Building | Attempts, fails, retries | 95-120 BPM, rising | Raise the stakes toward the payoff |
| Peak / payoff | The landing, the reveal, the win | 120-140 BPM, full | Make the moment feel bigger than it is |
| Comedy / meme | The joke, the reaction | Any tempo, sharp cuts | The sound effect IS the punchline |

For a Short, the track must earn its place in the first two
seconds. If the first beat of the music does not match the first
frame, cut the intro of the track, not the hook of the video.

## Licence-safe sources

Use music you are allowed to use, and keep the proof. In order of
least friction:

1. **YouTube Audio Library** - free, inside Studio, with its
   licence terms shown per track. Attribution where it asks for it.
2. **Creator music libraries with a creator licence** - the big
   names are Epidemic Sound, Artlist, and Pixabay Music. Read the
   licence for your channel size and for Shorts specifically; a
   licence that covers long-form does not always cover Shorts.
3. **Original or commissioned loops** - the only option that can
   never be claimed. For a series, one signature loop that returns
   every episode is worth more than ten licensed tracks, because
   the audience learns it.

Never use a commercial chart song you do not have rights to, and
never trust "no copyright sounds" in a reupload's title. If you
cannot find the licence, you do not have it. A claim on a video
that was doing well is worse than a quieter track.

## Meme sound effects

A sound effect is a punchline with no words. The rules are the
same as for a visual meme (`/yt-meme`):

- One effect per joke. Two effects in two seconds is noise.
- The effect lands **on** the cut or the reaction, not a beat
  after it. Half a second late is a different joke, and a worse
  one.
- Keep a small personal library of effects you reuse: a fail
  sting, a win sting, a record scratch, a crowd gasp. Reuse is
  what makes a sound yours; novelty every time is forgettable.
- Ducking: when the voice or the key sound speaks, the music
  drops under it. As a starting point, music sits well below the
  voice and rises only in gaps - then adjust by ear, because no
  number survives a bad mix.

## Loop points for Shorts

A Short that loops cleanly gets watched twice, and a second watch
is the cheapest retention there is. Plan the loop in the sound,
not just the picture:

- The last beat of the track must land on the last frame, and the
  first beat must pick up without a gap or a click. If the track
  does not loop, cut it to a section that does.
- The loop point is also a narrative point: the last line sets up
  the first line (`/yt-viral-loop`), and the music should rise
  into it, not fade out under it.
- Test the loop by watching the Short twice back to back with
  sound on. If the join is audible, it is not a loop yet.

## AI sound, disclosed

When music, a voice, or an effect is AI generated, mark it in the
publish checklist (`/yt-publish`). Do not claim a performance that
did not happen, and do not hide the generation. Disclosure is a
habit, not a confession.

## Captions: SRT QA before upload

Sound-off is the default scroll state, and on-screen captions
plus keyword highlights in the first two seconds hold sound-off
viewers. For a visual niche, captions carry the coaching cue and
the safety note, so a dropped caption is a dropped safety note.

Run `skills/yt-sound/srt_qa.py` on the caption file before
upload. It checks timing overlaps and out-of-order cues (errors),
reading speed, line length and count, cue length, and missing
sentence punctuation (warnings), and, with `--safety-words`, which
listed safety terms survived into the file. The speed, line, and
duration numbers are readability guidelines, not YouTube rules:
YouTube publishes no SRT speed limit, and the check exists so a
human looks at the cue.

Caption style, in brief: one to two lines max, keyword highlights
on screen in the first two seconds, hook words visible before
anyone unmutes, and text kept inside the safe zone - which now
includes TV, where Shorts Series playback puts small captions
under real strain.

## The licence log: the mistake this prevents

Shorts sound-library tracks are licensed **for Shorts only** -
not reusable in long-form or live. A song downloaded elsewhere
and edited in is not the same as picking it in-app, and can
trigger Content ID. Most library songs cover 90 seconds or less
(some 60 or 30). TikTok or Instagram trending sounds are not
licensed for YouTube. No seconds-length is safe by default:
Content ID matches the recording.

One more disagreement to check per upload, not to assume: older
guidance said a Short over one minute with any active copyright
claim is blocked worldwide; a September 2026 guide says such
Shorts are no longer automatically blocked in every case. Check
the claim status in Studio for each upload.

Keep the proof in `templates/audio-licence-log.csv`: track,
source, allowed surfaces, duration cap, and claim status. The
log is what stops a Shorts-only track leaking into a long video
months later, when nobody remembers where it came from.

## Auto-dubbing: review it, do not trust it

Auto-dubbing expanded to all creators in February 2026, now
covers 27 languages, and preserves tone, pacing, and energy
(Expressive Speech) in 8 of them: English, French, German,
Hindi, Indonesian, Italian, Portuguese, and Spanish. Viewers
get a Preferred Language setting, and creators monitor dubs by
the audio-track filter in Studio. YouTube says auto-dubbing does
not hurt discovery.

Review every dub before it matters: safety cues, numbers, and
body-part terms in each language, and thumbnail text per
language. A mistranslated safety cue is worse than no dub, and
for a coaching channel the safety cue is the part that cannot
be wrong.

## Loudness and beat gate (v3.3.2)

A Short with only native room noise is not a finished
Short. This gate is a publishing check, not a ranking
claim: it stops a quiet, music-less video from shipping
unnoticed, as happened with the October 2026 front-split
video, which measured about −29 LUFS with gym noise only.

- **Beat track required.** Every Short carries a music or
  beat track from a licence-safe source (see above), starting
  in the first 2 seconds. Native gym, room, or camera noise
  alone FAILS this gate, however clean the video looks.
- **Loudness check before upload.** Measure the finished
  audio's integrated loudness and normalise to a −14 LUFS
  target, with true peak no higher than −1 dBTP. −14 LUFS
  is the level YouTube normalises to, used here as the
  publishing target; it is not a claim about ranking.
  A measurement far below target (for example −29 LUFS)
  must be normalised before upload, not shipped quiet.
- **Licence still applies.** The track that passes this
  gate must still be logged in the licence log below.
  Loudness never excuses an unlicensed track.

## The gate

Nothing here publishes. This skill writes and you publish. Every
sound brief ends with the track, the licence, the loop point, and
the question: **ship it, or change it?**
