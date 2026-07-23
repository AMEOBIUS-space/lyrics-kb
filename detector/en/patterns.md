# EN Detector 1.0 — patterns and weights

Scan a lyric. Sum weights. Apply hard-fail caps. Then run `scoring.md`.

**Bands (pattern sum only):**
- 0–1.5 → clean enough to score freely
- 2–4 → suspect (must justify or repair)
- 4.5+ → slop-heavy

**Hard-fail:** any single pattern with weight **2.0** → cap overall alive-score at **6.9** until repaired (cannot rate GOOD/EXCELLENT).

---

## Pattern table

| ID | Pattern | Weight | What to flag | Fix direction |
|---|---|---|---|---|
| E01 | **tech_metaphor** | 2.0 HF | emotion wrapped in gadget/cloud/code (*tears in 4K*, *heart buffering*, *love offline*) | replace vehicle with physical scene |
| E02 | **organ_cliche** | 1.5 | *heart pounds/breaks/screams*, *soul on fire* without local detail | body detail or delete organ |
| E03 | **binary_light_dark** | 1.5 | song framed only as light vs dark / heaven vs hell | specific time/place contrast |
| E04 | **hypophora** | 1.5 | line asks, next line answers school-essay style | cut question or leave unanswered |
| E05 | **not_x_but_y** | 1.5 | *It's not goodbye — it's a new beginning* | one image, no slogan pivot |
| E06 | **chorus_checklist** | 2.0 HF | chorus = interchangeable virtue list (*I'll fight / I'll stay / I'll pray*) with no accumulating word | one claim + concrete cost |
| E07 | **position_apology** | 1.5 | *I'm not saying…*, *I don't mean to…*, *no judgment but…* | cut hedge; own the line |
| E08 | **cliche_rhyme_pair** | 1.0 | pairs from `cliche_rhymes.md` without twist | family rhyme or unexpected partner |
| E09 | **identity_rhyme** | 0.5 | *love/love*, *run/running* as end rhyme | change one end-word |
| E10 | **uniform_line_length** | 1.0 | 4+ lines same syllable/stress count with no mantra intent | break one line |
| E11 | **abstract_stack** | 1.0 | 3+ abstracts in a row (*pain, sorrow, endless night*) | one concrete noun |
| E12 | **adj_pile** | 0.5 | 3+ stacked adjectives | keep one killer adj |
| E13 | **filler_prosody** | 1.0 | strong beat on *the/and/to/just/really* | rewrite stress (see prosody.md) |
| E14 | **title_buried** | 1.0 | title only once mid-verse, never stable in chorus | place on chorus downbeat |
| E15 | **v2_paraphrase** | 1.5 | V2 restates V1 with synonyms | new fact/image only V2 can hold |
| E16 | **genre_autopilot_en** | 1.0 | stock genre stickers (*neon rain*, *whiskey tears*, *diesel and dust*) ×2+ un-twisted | local inventory from object writing |
| E17 | **sentiment_flatline** | 1.0 | single mood adjective repeated; no contradictory detail | add inconvenient emotion |
| E18 | **vague_deixis** | 0.5 | *something*, *everything*, *it all*, *this thing between us* with no trace | name a residue/object |
| E19 | **triple_rhetoric** | 0.5 | *blood, sweat, and tears* / tricolon of abstracts | cut to two or concretize one |
| E20 | **perfect_grammar_sterile** | 0.5 | no contraction, no fracture, speech-unlike polish throughout | allow cut syntax / enjambment |

HF = hard-fail eligible.

---

## Genre autopilot dictionaries (starters)

**Pop ballad:** endless night, broken pieces, shattered dreams, hold me close, forever and always  
**Country default:** truck, beer, small town (when all three with no specific name), dirt road sunset  
**EDM vocal:** tonight we rise, feel the love, into the light, higher higher  
**Indie sadboy:** cigarettes on the porch, empty bottle, 3am (alone as entire personality)  
**Trap flex:** generic flex list with no personal detail  

Flag when **≥2** stock items appear without a localizing twist.

---

## Scan protocol

1. Read full lyric cold once.
2. Mark E01–E20 hits with line numbers.
3. Sum weights; note any HF.
4. Run whitelist (`whitelist.md`).
5. Run `scoring.md`.
6. REPAIR highest-weight hits first.
