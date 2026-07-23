# Detector — EN

Anti-AI-slop patterns for English-language lyrics.

Parallel to RU Detector 2.0 (`songwriting/ru/encyclopedia.md` §§25–28), but **not a translation** — English has different cliché engines, stress habits, and pop defaults.

## Files

| File | Content |
|---|---|
| [`patterns.md`](./patterns.md) | 20 detection patterns + weights + hard-fail |
| [`whitelist.md`](./whitelist.md) | Legal exceptions (mantra, genre convention) |
| [`scoring.md`](./scoring.md) | EN score function E1–E12 + bands |
| [`cliche_rhymes.md`](./cliche_rhymes.md) | Hotlist of overused rhyme pairs |

## Quick pipeline

```
draft → patterns.md scan → apply weights → hard-fail check
     → whitelist pass → scoring.md → REPAIR if < 7.0
```

## Relation to RU detector

| Concept | RU | EN |
|---|---|---|
| Tech-metaphor wrap | слёзы в WAV | tears in 4K / heart in the cloud |
| Checklist chorus | чеклист припева | stacked "I'll always…" platitudes |
| Light/dark binary | свет/тьма frame | darkness/light soul clichés |
| Register contrast | high/low lexical clash | same — still gold |
| Body code | телесный код | same priority |
| Rhyme tells | verb rhymes, кровь-любовь | fire/desire, heart/apart |
