## 24. Векторы стиля

Стиль автора = набор параметров. Не абзац — **вектор**. Используй для калибровки и генерации.

Формат параметра: `ключ: значение` или `ключ: [значение1, значение2]`.

### 24.1 Хаски

```
meter:          tonika
beats_per_line: [2,4]
line_length:    variable
rhyme:          internal, loose, assonance
rhyme_position: internal+end
rhyme_scheme:   free
slang:          heavy (кент, мент, полтораха, подворотня)
register_low:   true
register_high:  true (сударыни, Монпарнас)
register_contrast: HIGH
profanity:      as_register
ugly_aesthetics: HIGH (панелька, подворотня, быт)
body_code:      HIGH (грязное, больное, пьющее)
phonetics:      percutssive (б/п=бочка, к/т=малый, р=очередь)
myth:           modernized_folk (Кощей, Яга в гротеске)
intertext:      christian+folk, desacralized
imagery:        rhizomatic_partial
voice:          margnal_at_bottom
density:        high (много слов/такт)
hook_type:      image_anchor
chorus:         refrain_anchor
form:           verse-chorus
```

### 24.2 Shortparis

```
meter:          verlibr
beats_per_line: [1,3]
line_length:    short, uniform_when_refrain
rhyme:          optional, mostly none
slang:          minimal, бытовое
register_low:   true
register_high:  false
register_contrast: LOW
profanity:      rare
ugly_aesthetics: MEDIUM (образы-триггеры, не пространство)
body_code:      LOW
phonetics:      vocalisation_heavy (la-la, tu-tu, ta-ta)
myth:           none
intertext:      none
imagery:        trigger-based
voice:          intellectual_at_bottom
density:        low (много воздуха)
hook_type:      refrain_anchor (одна фраза ×3)
chorus:         refrain_not_chorus
form:           cyclic
```

### 24.3 Скриптонит

```
meter:          tonika
beats_per_line: [3,5]
line_length:    variable
rhyme:          internal, end, смысловая
slang:          heavy (тащит, духом, семёра, район)
register_low:   true (уличный)
register_high:  false (социальный комментарий, не классика)
register_contrast: MEDIUM
profanity:      point
ugly_aesthetics: MEDIUM (быт, но наблюдается, не герой)
body_code:      MEDIUM
phonetics:      flow-based
myth:           none
intertext:      none
imagery:        observational
voice:          witness_no_position
density:        high
hook_type:      phrase
chorus:         refrain_with_variation
form:           verse-chorus
```

### 24.4 Pyrokinesis

```
meter:          variable (под музыку)
beats_per_line: [2,5]
line_length:    variable
rhyme:          loose, assonance
slang:          light
register_low:   true (бытовой)
register_high:  true (Бродский, классика)
register_contrast: HIGH
profanity:      rare
ugly_aesthetics: MEDIUM
body_code:      MEDIUM
phonetics:      medium
myth:           literary
intertext:      HIGH (цитата, аллюзия, реминисценция)
imagery:        rhizomatic
voice:          intellectual_at_bottom
density:        variable
hook_type:      image
chorus:         conceptual
form:           variable
```

### 24.5 ploho / моль / сруб

```
meter:          simple, sparse
beats_per_line: [2,3]
line_length:    short-medium
rhyme:          simple, honest (простая как честность)
slang:          бытовое (распиздяй, овца, подъёб)
register_low:   true
register_high:  false
register_contrast: LOW
profanity:      yes, flat
ugly_aesthetics: HIGH (панелька, холодный быт)
body_code:      MEDIUM
phonetics:      flat
myth:           none
intertext:      none
imagery:        sparse, бытовая
voice:          cold_declaimer (апатия)
density:        low
hook_type:      phrase (self-declaration)
chorus:         simple_refrain
form:           verse-chorus or cyclic
```

### 24.6 Кровосток

```
meter:          tonika, alliteration-driven
beats_per_line: [3,5]
line_length:    variable
rhyme:          free, internal, alliterative
slang:          philosophical+profane (бихевиоризм + мат)
register_low:   true (мат, быт)
register_high:  true (философский сленг)
register_contrast: HIGH
profanity:      as_register
ugly_aesthetics: HIGH (насилие как быт)
body_code:      MEDIUM
phonetics:      HIGH (п-п-п-б-б, аллитерация = структура)
myth:           none
intertext:      philosophical
imagery:        absurdist
voice:          mask_of_absurd (невозмутимый)
density:        medium
hook_type:      absurdist_image
chorus:         none (через строфу)
form:           through-composed
```

### 24.7 ЛСП

```
meter:          tonika, narrative
beats_per_line: [3,5]
line_length:    long
rhyme:          end, loose
slang:          street+literary
register_low:   true (уличный)
register_high:  true (нуар, лит)
register_contrast: HIGH
profanity:      yes
ugly_aesthetics: HIGH (нуарный город)
body_code:      MEDIUM
phonetics:      medium
myth:           noir (гедонизм→смерть→воскресение)
intertext:      literary
imagery:        narrative
voice:          narrator_noir
density:        high
hook_type:      phrase
chorus:         refrain
form:           verse-chorus, narrative_arc
```

### 24.8 Пошлая Молли

```
meter:          ровная силлабо-тоника
beats_per_line: [3,4] (равномерно)
line_length:    uniform (осознанно)
rhyme:          AABB, exact, banal (как приём)
slang:          meme, showbiz
register_low:   true
register_high:  false
register_contrast: LOW
profanity:      yes, playful
ugly_aesthetics: LOW
body_code:      LOW
phonetics:      simple
myth:           none
intertext:      pop_culture
imagery:        direct, viral
voice:          mask_of_absurd (подъёб)
density:        medium
hook_type:      phrase (viral)
chorus:         simple, viral
form:           verse-chorus
```

### 24.9 Аффинаж / almgamba (неофолк)

```
meter:          dolnik
beats_per_line: [2,4]
line_length:    medium
rhyme:          loose, assonance
slang:          conversational (не сленг, разговорный)
register_low:   true
register_high:  false (поэтический, но не высокий)
register_contrast: LOW
profanity:      rare
ugly_aesthetics: LOW (меланхолия, не уродство)
body_code:      MEDIUM
phonetics:      smooth
myth:           none
intertext:      light
imagery:        melancholic, poetic
voice:          melancholic
density:        medium
hook_type:      image
chorus:         refrain
form:           verse-chorus
```

### 24.10 25/17

```
meter:          tonika, folk-rap
beats_per_line: [3,5]
line_length:    long
rhyme:          loose, assonance
slang:          street+folk
register_low:   true
register_high:  true (фолк-патетика)
register_contrast: MEDIUM
profanity:      point
ugly_aesthetics: MEDIUM
body_code:      MEDIUM
phonetics:      declamatory
myth:           folk (ритуал)
intertext:      folk
imagery:        generational
voice:          confessor (мы, не я)
density:        high
hook_type:      refrain (ритуальный)
chorus:         refrain_ritual
form:           verse-chorus, narrative
```

### 24.11 Как использовать векторы

**GENERATE:** выбери автора → возьми его вектор → подставь параметры в шаблон (раздел 27) → генерируй по параметрам.

**CALIBRATE:** возьми вектор целевого автора → сравни параметры текста с вектором → каждая несовпавшая пара = delta → трансформируй по разделу 26.

**BLEND (смесь):** возьми 2 вектора → выбери параметры от каждого → например: meter от Shortparis + register_contrast от Хаски + voice от ploho. Проверь на конфликты (постпанк-верлибр + плотность рэпа = конфликт).

### 24.12 Таблица совместимости (blend-карта)

| Параметр | Хаски | Shortparis | Скриптонит | Pyrokinesis | ploho | Кровосток | ЛСП | Пошлая Молли | Аффинаж | 25/17 |
|---|---|---|---|---|---|---| ЛСП | ПМ | Аф | 25 |
| meter | тоника | верлибр | тоника | variable | simple | тоника | тоника | ровная | дольник | тоника |
| density | high | low | high | variable | low | med | high | med | med | high |
| register_contrast | HIGH | LOW | MED | HIGH | LOW | HIGH | HIGH | LOW | LOW | MED |
| rhyme | internal | none | internal | loose | simple | allit | end | AABB | loose | loose |
| profanity | as_reg | rare | point | rare | flat | as_reg | yes | playful | rare | point |
| phonetics | percuss | vocal | flow | med | flat | allit | med | simple | smooth | declam |
| myth | folk | none | none | lit | none | none | noir | none | none | folk |

**Зелёные blend-ы** (параметры совместимы):
- Хаски + Кровосток (тоника, HIGH contrast, as_reg profanity, phonetics-driven)
- Shortparis + ploho (low density, low contrast, постпанк-поле)
- Скриптонит + 25/17 (тоника, high density, наблюдение/исповедь)

**Красные blend-ы** (конфликт):
- Shortparis + Хаски (low density vs high density — выбрать один)
- Пошлая Молли + Pyrokinesis (ровная AABB vs loose, LOW vs HIGH contrast)
- ploho + ЛСП (apathy vs narrative arc — конфликт голоса)

---
