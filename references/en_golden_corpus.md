# EN Golden Corpus — detector regression battery

Parallel to RU `references/golden_corpus.md`. Synthetic fragments only.
Protocol: any change to `detector/en/patterns.md` or `scoring.md` runs this suite whole.

---

## Protocol

1. Run all cases through Detector EN 1.0 + whitelist.
2. Compare to expected column.
3. Regress = any verdict flip → roll back or refine rule.
4. New detection rule must ship with TP + FP-trap pair.
5. Targets: **FP = 0**, **FN ≤ 1** on full corpus.

---

## Group A — alive (expect 0 flags / GOOD+)

### EG-01 · confessional concrete
```
your mug still ghosts the sink ring
I leave the hallway light for nobody
the late shift of us keeps the meter spinning
```
- Expect: 0 hard-fail. High E1/E5/E9.

### EG-02 · spare post-punk lean
```
bus window fogs
I draw your name and wipe it
conductor says fares
that is the whole talk
```
- Expect: 0 flags. Short lines ≠ truncation.

### EG-03 · register contrast
```
mom prays — I count the coins
faith and a balance for two
God stays quiet like a collector before the call
knows me. has not dialed.
```
- Expect: 0 HF. One simile legal.

---

## Group B — slop (expect flags / SLOP or HF)

### EG-04 · organ + light/dark + checklist
```
my heart is breaking in the dark
I will love you forever
I will hold you together
I will fight for the light
```
- Expect: E02, E03, E06 HF, E08 risk → SLOP/HF.

### EG-05 · tech metaphor HF
```
my heart is a broken processor
rebooting feelings again and again
you are my forever update, my code without a password
```
- Expect: E01 hard-fail.

### EG-06 · therapy outro
```
in the end we are all healing
hold space for the inner child
I am still learning boundaries
```
- Expect: therapy bank + abstract stack → SUSPECT/SLOP.

### EG-07 · cliché rhyme chain
```
fire and desire through the night and light
heart torn apart from the start
love from above forever together
```
- Expect: E08 × multiple, E10.

### EG-08 · hypophora + not_x_but_y
```
What is left for me? Only memory.
It is not goodbye — it is a new beginning.
```
- Expect: E04, E05.

### EG-09 · industrial autopilot
```
neon veins and chrome heart
cyber tears in binary love
glitch in my soul, system override
```
- Expect: E16 genre_autopilot_en.

---

## Group C — border / whitelist

### EG-10 · mantra accumulation (W1)
```
water remembers
brick remembers
you will too
```
- Expect: E06 NOT flagged — slot accumulates.

### EG-11 · ironic cliché (W2)
```
love / above — yeah I know how that song goes
I file the rhyme under unpaid bills
```
- Expect: E08 suppressed by W2 if irony explicit.

### EG-12 · vague deixis without trace
```
something bigger waited for us
and all of this was not for nothing
```
- Expect: E18 vague_deixis.

### EG-13 · single stock door then local (W5)
```
neon rain on the lot
then the receipt sticks to my thumb
three bucks short for oil
```
- Expect: single stock OK under W5.

### EG-14 · filler prosody trap
```
and I just really want to be with you tonight
to the end of the beautiful light
```
- Expect: E13 and/or E08.

---

## Summary table

| Case | Expect |
|---|---|
| EG-01..03 | alive |
| EG-04 | SLOP / HF E06 |
| EG-05 | HF E01 |
| EG-06 | SUSPECT/SLOP |
| EG-07 | E08 heavy |
| EG-08 | E04+E05 |
| EG-09 | E16 |
| EG-10 | whitelist W1 |
| EG-11 | whitelist W2 |
| EG-12 | E18 |
| EG-13 | whitelist W5 |
| EG-14 | E13/E08 |

Status 2026-07-23: suite authored; run manually on rule changes.
