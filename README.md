# lyrics-kb

Общая база знаний по лирике и сонграйтингу — двуязычная (RU + EN), с единым продакшен- и промптинг-слоем.

**Repo:** [AMEOBIUS-space/lyrics-kb](https://github.com/AMEOBIUS-space/lyrics-kb)  
**Источник RU:** [russian-lyrics-kb](https://github.com/AMEOBIUS-space/russian-lyrics-kb)

## Статус (2026-07-23)

| Этап | Статус |
|---|---|
| 1. Перенос RU-базы | ✅ |
| 2. EN-теория | ✅ prosody · rhyme · structure · hooks · meter |
| 3. EN-техники | ✅ object writing · boxes · tension · POV · figurative |
| 4. EN-детектор | ✅ patterns · whitelist · scoring · cliché rhymes |

## Структура

```
songwriting/
  ru/                 # энциклопедия (pointer→source), modern, lyrics, demo EP
  en/theory/          # prosody, rhyme, structure, hooks, meter
  en/techniques/      # object writing, boxes, tension, POV, figurative
  cross/
detector/
  ru/                 # entry → encyclopedia §§25–28
  en/                 # Detector EN 1.0
production/           # mix, master, coldwave, opendaw, post-master
suno/                 # prompts, v5.5, anchors, behavior tags, procedures
genres/               # folk-horror, darksynth, cloud-bedroom
vocals/
references/           # pantheon, scene, golden corpus, SiliconSense
index.json
journal.jsonl
validate.py
```

## Пайплайны

**RU lyric:** encyclopedia → detector RU → genre playbook → score → REPAIR  
**EN lyric:** theory → techniques → detector EN → score E1–E12 → REPAIR  
**Generate:** suno prompts + anchors + behavior tags → procedures → production

## Крупные pointer-файлы

- `songwriting/ru/encyclopedia.md` → full text in russian-lyrics-kb (SHA `31ed0fef…`)
- `references/siliconsense_catalog.json` (~1.6MB) → russian-lyrics-kb

## Валидация

```bash
python3 validate.py
```

## Лицензия

CC BY-NC 4.0
