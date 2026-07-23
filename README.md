# lyrics-kb

Общая база знаний по лирике и сонграйтингу — двуязычная (RU + EN), с единым продакшен- и промптинг-слоем.

**Repo:** [AMEOBIUS-space/lyrics-kb](https://github.com/AMEOBIUS-space/lyrics-kb)  
**Источник RU:** [russian-lyrics-kb](https://github.com/AMEOBIUS-space/russian-lyrics-kb) (archived — all content migrated)  
**kb_version:** `4.9-lyrics-kb` · **entries:** 84 · **self-contained** (0 external deps)

## Статус (2026-07-23)

| Этап | Статус |
|---|---|
| 1. Перенос RU-базы | ✅ |
| 2. EN-теория | ✅ |
| 3. EN-техники | ✅ |
| 4. EN-детектор | ✅ |
| 5. Sound corpus + EN craft | ✅ |
| 6. EN golden + cross | ✅ |
| 7. Encyclopedia multipart | ✅ `parts/part_01`…`part_17` |
| 8. CW case cards | ✅ 003–010 full desk |
| 9. genre_bpm JSON | ✅ full 420 genres in-repo |
| 10. EN desk cases | ✅ EN-001…010 (block closed) |
| 11. IND desk cases | ✅ IND-001 + IND-002 diptych |
| 12. Autonomy migration | ✅ all heavy files in-repo (`2cfdd48`) |

## Структура

```
songwriting/ru|en|cross/
detector/ru|en/
production/  suno/  genres/  vocals/
references/  cases/   # CW-003…010 · EN-001…010 · IND-001/002
index.json   journal.jsonl   validate.py
```

## Пайплайны

**RU:** encyclopedia parts → detector RU → genre playbook → score → REPAIR  
**EN:** EN craft → theory/techniques → detector EN → E1–E12 → REPAIR  
**Sound:** cases + sound_corpus → EQ lessons → package patch

## Large files (in-repo)

- `references/siliconsense_catalog.json` — 1.6MB, 865 artists
- `references/siliconsense_genre_bpm.json` — full 420 genres
- `references/siliconsense_moods.json` · `references/siliconsense_usecases.json` — full
- Encyclopedia multipart `parts/part_01…17` — fully in-repo, no external pointers

## Валидация

```bash
python3 validate.py
```

## Лицензия

CC BY-NC 4.0
