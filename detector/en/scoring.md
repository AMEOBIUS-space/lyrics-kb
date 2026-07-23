# EN Score function 1.0 (E1–E12)

After pattern scan + whitelist, score the lyric on twelve parameters **0.0–1.0**.  
**alive_score_en = sum(E1..E12)** → range 0–12, report normalized or raw consistently (we use **raw sum**, pass threshold **7.0** like RU).

---

## Parameters

| ID | Name | 1.0 means | 0.0 means |
|---|---|---|---|
| **E1** | concreteness | filmable nouns dominate | abstract fog |
| **E2** | rhythm_variance | stress-count & length breathe | machine-uniform |
| **E3** | rhyme_quality | family/assonance/internal on purpose | cliché perfect / verb-ish laziness |
| **E4** | prosody_fit | stresses match musical sense when spoken | filler on peaks |
| **E5** | body_presence | body costs something (breath, heat, injury, appetite) | floating consciousness |
| **E6** | image_engine | one metaphor family developed | sticker metaphors / mixed mess |
| **E7** | sonic_texture | alliteration/assonance working | flat phonetics |
| **E8** | hook_title | title/hook stable, singable, placed | buried or generic |
| **E9** | voice_embodiment | POV has place + want + tell | generic diarist |
| **E10** | anti_slop_clean | pattern sum ≤1.5 after whitelist | HF or sum ≥4.5 |
| **E11** | section_contrast | verse/chorus differ on ≥2 axes | same mush twice |
| **E12** | info_progress | V2/bridge add non-paraphrase info | loop of synonyms |

---

## Verdict bands

| Sum | Verdict |
|---|---|
| **9.0+** | EXCELLENT |
| **7.0–8.9** | GOOD |
| **5.0–6.9** | SUSPECT |
| **<5.0** | SLOP |

Hard-fail from patterns → cannot exceed **6.9** until cleared.

---

## Genre weight profiles (multipliers, renormalize mentally)

Apply as emphasis when judging borderline params (not strict math v1):

| Profile | Boost | Soften |
|---|---|---|
| **pop_radio** | E8, E11, E4 | E7 |
| **indie_confessional** | E1, E5, E9 | E3 |
| **rap_dense** | E3 internal, E7, E12 | E11 classic pop contrast |
| **folk_narrative** | E1, E12, E9 | E8 viral hook |
| **dance_vocal** | E8, E4 | E1 (still need one anchor) |

---

## REPAIR loop

```
while score < 7.0 and iteration ≤ 3:
  1. list top weight pattern hits
  2. fix highest HF or weight first
  3. re-score E10 and affected params
  4. stop if delta < 0.3 for 2 iterations
```

**Delta report format:**
```
E1 0.4→0.8 (+0.4) replaced "endless pain" with "bleach on the bathroom tile"
E8 0.5→0.9 (+0.4) title moved to chorus downbeat
SUM 6.2→7.4 GOOD
```

---

## Mini calibration (synthetic)

**GOOD sketch:**
```
// V
your mug still ghosts the sink ring
// CH
don't wait up — I'm on the late shift of us
```
High E1/E8/E9 potential; finish prosody and V2 progress before calling EXCELLENT.

**SLOP sketch:**
```
my heart is breaking in the dark
I'll love you forever / I'll hold you together / I'll fight for the light
```
E01/E02/E03/E06/E08 failure cluster.
