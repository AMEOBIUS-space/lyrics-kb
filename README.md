# lyrics-kb

Общая база знаний по лирике и сонграйтингу — двуязычная (RU + EN), с единым продакшен- и промптинг-слоем.

**Repo:** [AMEOBIUS-space/lyrics-kb](https://github.com/AMEOBIUS-space/lyrics-kb)  
**Источник RU:** [russian-lyrics-kb](https://github.com/AMEOBIUS-space/russian-lyrics-kb)  
**kb_version:** `3.4-lyrics-kb` · **entries:** 70

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
| 8. CW case cards | ✅ 003–009 full · 010 seed |
| 9. genre_bpm JSON | 🟡 stub; full → source `65b0b233…` |

## Структура

```
songwriting/ru|en|cross/
detector/ru|en/
production/  suno/  genres/  vocals/
references/  cases/   # CW-003…010 + series lessons
index.json   journal.jsonl   validate.py
```

## Пайплайны

**RU:** encyclopedia parts → detector RU → genre playbook → score → REPAIR  
**EN:** EN craft → theory/techniques → detector EN → E1–E12 → REPAIR  
**Sound:** cases + sound_corpus → EQ lessons → package patch

## Pointer / large files

- Encyclopedia multipart in-repo; monolith backup SHA `31ed0fef…`
- `siliconsense_catalog.json` (~1.6MB) → russian-lyrics-kb
- `siliconsense_genre_bpm.json` → stub here; full in source

## Валидация

```bash
python3 validate.py
```

## Лицензия

CC BY-NC 4.0
