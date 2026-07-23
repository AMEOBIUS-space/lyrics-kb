# EN Craft Layer — English lyrics ops

Operational layer for **English lyrics** on top of the RU craft hub. Not a second encyclopedia.

Mirror of Notion «EN Craft Layer» (2026-07-23). Complements `songwriting/en/theory/*`, `techniques/*`, `detector/en/*`.

---

## 0. When to open this

- Any **EN** GENERATE / AUDIT / REPAIR
- Before scoring EN text (Detector EN + this delta)
- When EN feels “fluent but dead” (AI-default)

**Do not open for:** full craft theory, RU coldwave desk, mix/master numbers.

---

## 1. Desk order (EN)

1. Voice + place + **one concrete object**
2. Cost-in-frame (what is lost and still visible)
3. Hook: 1–2 punch lines, say aloud at target BPM
4. Draft
5. Anti-slop bank pass
6. Detector EN (`detector/en/`) + delta below
7. Genre satellite if any (IND danger levers)
8. PACKAGE → gen

Naturalness test: *Would a person say this out loud — and can they sing it at tempo without chewing consonants?*

---

## 2. Anti-slop bank (EN)

Flag REPAIR if ≥2–3 hits across banks, or 1 chorus built on cliché pairs.

### 2.1 Therapy / consoling
`heal, healing, trauma, boundaries, valid, journey, self-care, inner child, hold space, still love, I'm sorry, please stay, almost, maybe` in **outro** especially — outro must not comfort.

### 2.2 Pop-AI glue
`in the end`, `nothing lasts`, `lost in the`, `screaming into`, `echoes of`, `broken pieces`, `drowning in`, `fade to black`, `demons in my`, `voice inside my head`

### 2.3 Cheap rhyme pairs (default ban unless ironic frame)
`night/light`, `heart/apart`, `fire/desire`, `pain/rain`, `eyes/lies`, `true/you`, `alone/home`, `scar/are`, `breath/death`

→ full list: `detector/en/cliche_rhymes.md`

### 2.4 Industrial / cyber stamps
`neon veins`, `chrome heart`, `digital god`, `glitch in my soul`, `cyber tears`, `binary love`, `system override` as emotion, `jacked into`

### 2.5 Syntax anti-patterns
- `It's not X, it's Y` / `I'm not X, I'm Y`
- Hypophora (ask → answer yourself)
- Uniform line length + parallel stacks with no turn
- Abstract pile with no object

### 2.6 Legal craft (do not false-flag)
- Production lexicon with dual-read (literal gear + human mask)
- Max **1** denial line per lyric — only when hero denies inner state; object/world properties → banned not_x_but_y
- One concrete remainder after a cut
- Second person that **acts** at least once (IND-002+)

---

## 3. Detector delta (RU → EN read)

| RU / detector | EN read |
|---|---|
| `tech_metaphor` | OK if literal object and/or hero mask. Fail if pure ornament. |
| `genre_autopilot` | Use EN banks §2.4 + genre satellite — not RU neon set alone. |
| `kantselyarit` | Map to corporate / HR / therapy register (§2.1). |
| Stress / ё | Replace with stress + schwa checks; Suno swallows unstressed syllables. |
| P3 rhyme | Prefer slant/internal over perfect cliché pairs. |
| P7 phonetics | Consonant clusters on downbeats = fail at 130–150 BPM. |
| P11 singability | Long notes want open vowels; avoid `/kst/`, `/pts/`, `/str/` on sustains. |
| P1 concrete | EN AI defaults abstract — demand object + verb + place every section. |

**Gate for industrial_en weights:** ≥2 closed IND sound cases, or ≥3 EN lyrics EXCELLENT + ≥1 closed IND sound. Desk-only scores never open the gate.

---

## 4. Prosody & hook (practical)

- Speak the line; primary stress on meaning words
- Multisyllable crush: `temperature`, `vulnerability` — usually bad in chorus
- Hook: one breath-group; 1–2 lines people can bark back
- Register lock per section; no therapy-climb in last four bars
- Title line carries weight — no filler around it

See also: `songwriting/en/theory/prosody.md`, `hooks_and_titles.md`

---

## 5. EN GENERATE micro-scaffold

```
VOICE: who speaks + how calm/cruel
PLACE: one room or street fact
OBJECT: touches or operates
COST: what warm thing is gone + visible remainder
YOU: does "you" act once? (required IND-002+)
HOOK: two lines max
OUTRO: fact or action — no comfort lexicon
ANTI-SLOP: scan §2
```

---

## 6. Lane discipline

- Primary new desk: **EN / IND** until industrial signature holds
- CW may still gen/finish; avoid parallel new RU concepts if focus is EN shift
- Card note: `Lang: EN`
- Sound corpus fail_modes: `IND-*` only for this lane
- Do not port coldwave EQ patch blind into IND gens

---

## Related in repo

- Theory: `songwriting/en/theory/`
- Techniques: `songwriting/en/techniques/`
- Detector: `detector/en/`
- Sound corpus: `references/sound_corpus.md`
- RU hub pointer: `songwriting/ru/encyclopedia.md`
