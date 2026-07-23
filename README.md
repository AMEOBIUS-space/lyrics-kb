# lyrics-kb

Общая база знаний по лирике и сонграйтингу — двуязычная (RU + EN), с единым продакшен- и промптинг-слоем.

**Repo:** [AMEOBIUS-space/lyrics-kb](https://github.com/AMEOBIUS-space/lyrics-kb)  
**Источник RU:** [russian-lyrics-kb](https://github.com/AMEOBIUS-space/russian-lyrics-kb)  
**kb_version:** `3.2-lyrics-kb` · **entries:** 61

## Статус (2026-07-23)

| Этап | Статус |
|---|---|
| 1. Перенос RU-базы | ✅ |
| 2. EN-теория | ✅ prosody · rhyme · structure · hooks · meter |
| 3. EN-техники | ✅ object writing · boxes · tension · POV · figurative |
| 4. EN-детектор | ✅ patterns · whitelist · scoring · cliché rhymes |
| 5. Sound corpus + EN craft | ✅ `references/sound_corpus.md` · `songwriting/en/EN_CRAFT_LAYER.md` |
| 6. EN golden + cross | ✅ EG-01..14 · `songwriting/cross/*` |
| 7. Encyclopedia multipart | 🟡 hub + part_01/02/17; остальные части + genre_bpm JSON — in progress |

## Структура

```
songwriting/
  ru/                 # encyclopedia hub + parts/, modern, lyrics, demo EP
  en/theory/          # prosody, rhyme, structure, hooks, meter
  en/techniques/      # object writing, boxes, tension, POV, figurative
  en/EN_CRAFT_LAYER.md
  cross/              # narrative arc, topline phrasing
detector/
  ru/                 # entry → encyclopedia §§25–28
  en/                 # Detector EN 1.0
production/           # mix, master, coldwave, opendaw, post-master
suno/                 # prompts, v5.5, anchors, behavior tags, procedures
genres/               # folk-horror, darksynth, cloud-bedroom
vocals/
references/           # pantheon, scene, golden + EN golden, sound corpus, SiliconSense
index.json
journal.jsonl
validate.py
```

## Пайплайны

**RU lyric:** encyclopedia → detector RU → genre playbook → score → REPAIR  
**EN lyric:** EN craft layer → theory/techniques → detector EN → score E1–E12 → REPAIR  
**Generate:** suno prompts + anchors + behavior tags → procedures → production  
**Sound:** sound corpus fail_modes → EQ/mix lessons → package patch

## Крупные / pointer-файлы

- `songwriting/ru/encyclopedia.md` → multipart `parts/` + monolith в russian-lyrics-kb (SHA `31ed0fef…`)
- `references/siliconsense_catalog.json` (~1.6MB) → russian-lyrics-kb
- `references/siliconsense_genre_bpm.json` → push in progress (source SHA `65b0b233…`)

## Валидация

```bash
python3 validate.py
```

## Лицензия

CC BY-NC 4.0
