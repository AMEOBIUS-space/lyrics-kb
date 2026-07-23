# Энциклопедия русскоязычной лирики и сонграйтинга (v2.0)

Полный рабочий справочник (30 разделов). Разбит на части из‑за размера API-push.

| Часть | Файл | Содержание |
|---|---|---|
| 1 | [parts/encyclopedia_p1.md](./parts/encyclopedia_p1.md) | Принципы → синтаксис (§0–6) |
| 2 | [parts/encyclopedia_p2.md](./parts/encyclopedia_p2.md) | Голос → explicit (§7–14) |
| 3 | [parts/encyclopedia_p3.md](./parts/encyclopedia_p3.md) | Сленг → AI-карта (§15–22) |
| 4 | [parts/encyclopedia_p4.md](./parts/encyclopedia_p4.md) | Деревья → JSON/scoring (§23–30) |

> Полный monolithic blob (идентичный): [`russian-lyrics-kb` …/encyclopedia.md](https://github.com/AMEOBIUS-space/russian-lyrics-kb/blob/main/songwriting/encyclopedia.md) · SHA `31ed0fef97e424cf720cc5b6f4e8f6905e536cf8`

## Ключевые блоки (quick ref)

**Детектор 2.0:** 25 паттернов, hard-fail, white-list 25.27 → см. p4 + `detector/ru/`

**Scoring 2.0:** P1–P12, порог GOOD ≥ 7.0 → p4 §28

**Связанные:**
- `references/golden_corpus.md` — 14 lyric regression cases
- `references/sound_corpus.md` — sound cases (CW/IND)
- `references/pantheon_v2.md`
- `songwriting/ru/modern_russian_lyrics.md`
