# lyrics-kb

Общая база знаний по лирике и сонграйтингу — двуязычная (RU + EN), с единым продакшен- и промптинг-слоем.

**Repo:** [AMEOBIUS-space/lyrics-kb](https://github.com/AMEOBIUS-space/lyrics-kb)  
**Источник RU:** [russian-lyrics-kb](https://github.com/AMEOBIUS-space/russian-lyrics-kb) (archived as source, not deleted)

## Статус (2026-07-23)

| Этап | Статус |
|---|---|
| 1. Перенос RU-базы | ✅ done (40 entries indexed) |
| 2. EN-теория | 🔜 next |
| 3. EN-техники | pending |
| 4. EN-детектор | pending |

## Структура

```
songwriting/
  ru/          # энциклопедия, modern lyrics, pipeline demo
  en/theory/   # prosody, rhyme, structure (next)
  en/techniques/
  cross/
detector/
  ru/  ·  en/
production/    # mixing, mastering, coldwave, opendaw, post-master
suno/          # prompts, v5.5, anchors, behavior tags, procedures
genres/        # folk-horror, darksynth, cloud-bedroom playbooks
vocals/
references/    # pantheon, scene, golden corpus, SiliconSense
index.json     # 40 entries, lang: ru|en|cross
journal.jsonl
validate.py
```

## Валидация

```bash
python3 validate.py
```

## Крупные файлы (pointer)

- `songwriting/ru/encyclopedia.md` → полный текст в russian-lyrics-kb (SHA `31ed0fef…`)
- `references/siliconsense_catalog.json` (~1.6MB) → остаётся в russian-lyrics-kb

## Лицензия

CC BY-NC 4.0
