## 30. Машинно-читаемые блоки

Блоки в формате, удобном для парсинга и автоматизации. Можно вынести в отдельные JSON/YAML при необходимости.

### 30.1 JSON: пантеон с жанрами

```json
{
  "pantheon": [
    {"name": "Хаски", "genre": "рэп", "meter": "tonika", "key_traits": ["ugly_aesthetics", "register_contrast", "phonetics_percussive", "body_code", "myth_folk"]},
    {"name": "Pyrokinesis", "genre": "рэп-рок", "meter": "variable", "key_traits": ["rhizomatic_imagery", "intertext_high", "register_contrast"]},
    {"name": "Shortparis", "genre": "постпанк", "meter": "verlibr", "key_traits": ["refrain_anchor", "vocalisation", "trigger_imagery"]},
    {"name": "Скриптонит", "genre": "хип-хоп", "meter": "tonika", "key_traits": ["street_slang", "observational", "social_no_pafos"]},
    {"name": "ЛСП", "genre": "рэп/нуар", "meter": "tonika", "key_traits": ["noir_narrative", "hedonism_death_resurrection", "street_plus_literary"]},
    {"name": "Аффинаж", "genre": "постпанк/инди", "meter": "dolnik", "key_traits": ["melancholic_imagery", "style_and_rebellion_balance"]},
    {"name": "ploho", "genre": "постпанк/думер", "meter": "simple_sparse", "key_traits": ["cold_tone", "panelka", "apathy"]},
    {"name": "Буерак", "genre": "постпанк", "meter": "simple", "key_traits": ["absurd_irony", "memes", "social_podyeb"]},
    {"name": "Кровосток", "genre": "абстр. хип-хоп", "meter": "tonika_alliteration", "key_traits": ["black_humor", "cold_statement", "alliteration"]},
    {"name": "Saluki", "genre": "хип-хоп/эксп", "meter": "variable", "key_traits": ["melancholia", "collage", "intertext"]},
    {"name": "Пошлая Молли", "genre": "поппанк", "meter": "ровная_силлабо_тоника", "key_traits": ["AABB_banal_as_device", "viral_directness", "showbiz_irony"]},
    {"name": "25/17", "genre": "рэп/соц", "meter": "tonika_folk", "key_traits": ["confession", "we_not_I", "ritual"]},
    {"name": "Oxxxymiron", "genre": "рэп/лит", "meter": "variable", "key_traits": ["intertext_high", "complex_metaphor", "classic_dialogue"]}
  ],
  "poets": [
    {"name": "Бродский", "key_traits": ["rhythmic_inertia", "long_periods", "enjambment", "facture"]},
    {"name": "Елена Шварц", "key_traits": ["religious_no_pafos", "mystical_byt", "dry_holiness"]},
    {"name": "Полина Барскова", "key_traits": ["catastrophe_as_language", "detail_precision", "testimony_ethics"]},
    {"name": "Маяковский", "key_traits": ["tonika", "ladder", "urban_vocabulary"]},
    {"name": "Хлебников", "key_traits": ["zaum", "sound_painting", "word_as_object"]},
    {"name": "Шершеневич", "key_traits": ["image_chains", "futurist_byt"]}
  ]
}
```

### 30.2 JSON: детектор AI-маркеров

```json
{
  "detector": {
    "marker_words": [
      "вечность", "бесконечность", "симфония", "гармония", "мелодия души",
      "путешествие", "навсегда", "навечно", "бесконечный путь", "вечный",
      "непостижимый", "загадочный", "волшебный", "магический", "прекрасный",
      "чудесный", "дивный", "неземной", "космический", "как никогда ранее",
      "ничто не могло подготовить", "глубокий"
    ],
    "tech_metaphors_regex": [
      "слёзы.*(формат|WAV|mp3|файл)",
      "сердце.*(архив|кэш|лог|облак|код)",
      "душа.*(облак|кэш|сервер|баз)",
      "любовь.*(кэш|перезагруз|файл)",
      "память.*(лог|индекс|баз)",
      "код души", "перезагрузка чувств", "файл одиночества"
    ],
    "organ_cliches_regex": [
      "сердце (бьётся|колотится|рвётся|кричит|плачет)",
      "душа (рвётся|кричит|плачет|горит|болит)"
    ],
    "banal_rhymes": [
      ["любовь", "кровь"], ["любовь", "вновь"], ["кровь", "вновь"],
      ["ночь", "дочь"], ["ночь", "прочь"], ["дочь", "прочь"],
      ["пора", "гора"], ["слёзы", "грёзы"], ["беда", "звезда"],
      ["туман", "обман"], ["пожар", "пожал"]
    ],
    "verb_rhymes": [
      ["любить", "забыть"], ["идти", "найти"], ["летать", "мечтать"],
      ["кричать", "молчать"], ["гореть", "тереть"], ["ждать", "бежать"]
    ],
    "constructions": {
      "binary_light_dark": {"requires": ["тьма|мрак|во тьме", "свет|свет внутри|между светом и тьмой"], "frame_check": true},
      "hypophora": {"pattern": "line_ends_with_? AND next_line_answers"},
      "not_x_but_y": {"regex": ["не просто .* — это был.*", "это не .* — это .*", "не .* а .*"]},
      "noun_stack": {"min_consecutive_nouns": 3, "no_verb_between": true},
      "adj_pile": {"min_consecutive_adjectives": 3},
      "position_explanation": ["я не сужу", "не мне судить", "я помню всё", "я не берусь объяснить", "не мне решать"],
      "truncation": ["[Продолжение следует", "Потом было", "…дальше — позже", "но это уже другая история"]
    },
    "weights": {
      "tech_metaphor": 2.0, "organ_cliche": 1.5, "binary_light_dark": 1.5,
      "hypophora": 1.5, "not_x_but_y": 1.5, "marker_word": 1.0,
      "chorus_checklist": 2.0, "position_explanation": 1.5,
      "verb_rhyme": 1.0, "banal_rhyme": 1.0, "noun_stack": 0.5,
      "adj_pile": 0.5, "uniform_line_length": 1.0, "parallel_no_shift": 0.5,
      "truncation": 2.0
    },
    "ai_score_bands": {"likely_human": "0-1.5", "suspect": "2-4", "slop": "4.5+"}
  }
}
```

### 30.3 YAML: векторы стиля (кратко)

```yaml
style_vectors:
  husky:
    meter: tonika
    beats_per_line: [2, 4]
    line_length: variable
    rhyme: internal_loose_assonance
    slang: heavy
    register_contrast: HIGH
    profanity: as_register
    ugly_aesthetics: HIGH
    body_code: HIGH
    phonetics: percussive
    myth: modernized_folk
    voice: marginal_at_bottom
    density: high
    hook_type: image_anchor
    form: verse-chorus

  shortparis:
    meter: verlibr
    beats_per_line: [1, 3]
    rhyme: optional_none
    slang: minimal
    register_contrast: LOW
    profanity: rare
    phonetics: vocalisation_heavy
    voice: intellectual_at_bottom
    density: low
    hook_type: refrain_anchor
    form: cyclic

  skryptonite:
    meter: tonika
    beats_per_line: [3, 5]
    rhyme: internal_end_smyslovaya
    slang: heavy_street
    register_contrast: MEDIUM
    profanity: point
    voice: witness_no_position
    density: high
    hook_type: phrase
    form: verse-chorus

  pyrokinesis:
    meter: variable
    beats_per_line: [2, 5]
    rhyme: loose_assonance
    register_contrast: HIGH
    intertext: HIGH
    imagery: rhizomatic
    voice: intellectual_at_bottom
    form: variable

  ploho:
    meter: simple_sparse
    beats_per_line: [2, 3]
    rhyme: simple_honest
    slang: бытовое
    register_contrast: LOW
    profanity: flat
    ugly_aesthetics: HIGH
    voice: cold_declaimer
    density: low
    hook_type: phrase_self_declaration
    form: verse-chorus_or_cyclic

  krovostok:
    meter: tonika_alliteration
    rhyme: free_internal_alliterative
    slang: philosophical_profane
    register_contrast: HIGH
    profanity: as_register
    phonetics: alliteration_HIGH
    voice: mask_of_absurd
    form: through-composed

  lsp:
    meter: tonika_narrative
    beats_per_line: [3, 5]
    line_length: long
    slang: street_plus_literary
    register_contrast: HIGH
    myth: noir
    voice: narrator_noir
    density: high
    form: verse-chorus_narrative_arc

  poshlaya_molli:
    meter: ровная_силлабо_тоника
    rhyme: AABB_exact_banal
    slang: meme_showbiz
    register_contrast: LOW
    profanity: playful
    voice: mask_of_absurd
    hook_type: phrase_viral
    form: verse-chorus

  affinazh:
    meter: dolnik
    beats_per_line: [2, 4]
    rhyme: loose_assonance
    register_contrast: LOW
    voice: melancholic
    density: medium
    hook_type: image
    form: verse-chorus

  25_17:
    meter: tonika_folk
    beats_per_line: [3, 5]
    line_length: long
    slang: street_folk
    register_contrast: MEDIUM
    myth: folk_ritual
    voice: confessor
    density: high
    hook_type: refrain_ritual
    form: verse-chorus_narrative
```

### 30.4 JSON: чек-лист «живое vs слоуп» (булев)

```json
{
  "alive_check": {
    "red_flags": {
      "tech_metaphor_wrapping_emotion": false,
      "chorus_is_checklist_not_hook": false,
      "explains_position": false,
      "uniform_line_length_except_intentional": false,
      "verb_rhymes": false,
      "binary_light_dark_frame": false,
      "hypophora": false,
      "not_x_but_y_formula": false,
      "noun_stack_3plus": false,
      "adj_pile_3plus": false,
      "truncation": false,
      "parallel_no_shift": false,
      "banal_rhyme_pairs": false,
      "marker_words_present": false,
      "organ_cliches": false
    },
    "green_flags": {
      "physical_anchor_smell_touch_sound": true,
      "register_contrast_high_low": true,
      "refrain_anchor_not_checklist": true,
      "concrete_specific_noun": true,
      "body_code_unromantic": true,
      "ugly_as_character": true,
      "internal_rhyme_present": true,
      "enjambment_present": true,
      "rhythm_variance": true,
      "voice_embodied": true
    },
    "pass_condition": "all red_flags == false AND at_least_5 green_flags == true"
  }
}
```

### 30.5 JSON: дерево выбора голоса (исполняемое)

```json
{
  "voice_decision_tree": {
    "branches": {
      "rap": {
        "быт_подворотня_панелька": "marginal_at_bottom",
        "социальное_наблюдение": "witness_no_position",
        "литература_философия": "intellectual_at_bottom",
        "нуар_город_история": "narrator_noir",
        "поколение_исповедь": "confessor",
        "абсурд_насилие": "mask_of_absurd"
      },
      "post_punk": {
        "апатия_быт": "cold_declaimer",
        "тревога_страх": "intellectual_at_bottom",
        "абсурд_ирония": "mask_of_absurd"
      },
      "pop_punk": "mask_of_absurd",
      "indie_neofolk": "melancholic",
      "spoken_word": "cold_declaimer"
    },
    "fallback": "witness_no_position"
  }
}
```

### 30.6 JSON: сводная функция оценки

```json
{
  "score_function": {
    "name": "alive_score",
    "range": "0.0-10.0",
    "pass_threshold": 7.0,
    "parameters": {
      "P1_concreteness": {"range": "0.0-1.0", "1.0": "all concrete", "0.0": "all abstract"},
      "P2_rhythm_variance": {"range": "0.0-1.0", "1.0": "varied length+enjambment", "0.0": "uniform"},
      "P3_rhyme_quality": {"range": "0.0-1.0", "1.0": "loose/assonance/internal", "0.0": "verb/banal"},
      "P4_register_contrast": {"range": "0.0-1.0", "1.0": "explicit high/low clash", "0.0": "one register"},
      "P5_body_code": {"range": "0.0-1.0", "1.0": "dirty/sick/tired body", "0.0": "absent/idealized"},
      "P6_ugly_aesthetics": {"range": "0.0-1.0", "1.0": "ugly as character", "0.0": "absent/abstract"},
      "P7_phonetics": {"range": "0.0-1.0", "1.0": "alliteration/vocalisation structural", "0.0": "none"},
      "P8_hook_strength": {"range": "0.0-1.0", "1.0": "catchy 1-2 lines", "0.0": "checklist/none"},
      "P9_voice_embodiment": {"range": "0.0-1.0", "1.0": "body+place+action", "0.0": "abstract I"},
      "P10_anti_ai_clean": {"range": "0.0-1.0", "1.0": "zero markers", "0.0": "3+ or high-weight"}
    },
    "formula": "score = sum(P1..P10)",
    "verdicts": {
      "8.0+": "EXCELLENT",
      "7.0-7.9": "GOOD",
      "5.0-6.9": "SUSPECT",
      "<5.0": "SLOP"
    },
    "repair_loop": {
      "while": "score < 7.0",
      "max_iterations": 3,
      "steps": ["detect (sec 25)", "transform (sec 26)", "re-score (sec 28)"],
      "stop_if": "score doesn't improve for 2 iterations"
    }
  }
}
```

### 30.7 Использование машинно-читаемых блоков

Эти блоки можно:
- **Парсить** в скрипт/агента для автоматической детекции и оценки
- **Подставлять** в системные промпты (векторы, деревья)
- **Расширять** — добавлять авторов, патроны, параметры
- **Экспортировать** в отдельные файлы (JSON/YAML) при росте

При добавлении нового автора: добавить строку в `pantheon` (30.1), вектор в `style_vectors` (30.3), при необходимости — ветку в `voice_decision_tree` (30.5).

При добавлении нового AI-маркера: добавить в `detector` (30.2), назначить вес в `weights`, добавить правило трансформации в раздел 26.

---
