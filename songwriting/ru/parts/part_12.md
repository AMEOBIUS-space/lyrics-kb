## 25. Паттерны детекции

Regex-подобные правила для поиска AI-маркеров в тексте. Каждое правило = патрон. Сработало → маркер найден → текст в REPAIR.

### 25.1 Слова-маркеры

```
PATTERN: word_in_set([
  "вечность", "бесконечность", "симфония", "гармония", "мелодия души",
  "путешествие", "навсегда", "навечно", "бесконечный путь", "вечный",
  "непостижимый", "загадочный", "волшебный", "магический", "прекрасный"(filler),
  "чудесный", "дивный", "неземной", "космический"(love), "как никогда ранее",
  "ничто не могло подготовить", "глубокий"(filler)
])
ACTION: FLAG(marker_word)
FIX: replace_with_concrete_image (раздел 26.1)
```

### 25.2 Тех-метафоры эмоций

```
PATTERN: regex([
  "слёзы.*(формат|WAV|mp3|файл)",
  "сердце.*(архив|кэш|лог|облак|код)",
  "душа.*(облак|кэш|сервер|баз)",
  "любовь.*(кэш|перезагруз|файл)",
  "память.*(лог|индекс|баз)",
  "код души", "перезагрузка чувств", "файл одиночества"
])
EXCEPTION: IF контекст = технический_мир_героя (серверная, сисоп) AND лексика = грунт, NOT метафора_эмоции → PASS
ACTION: FLAG(tech_metaphor)
FIX: replace_with_bodily_or_sensory (раздел 26.2)
```

### 25.3 Сердце/душа штампы

```
PATTERN: regex([
  "сердце (бьётся|колотится|рвётся|кричит|плачет)",
  "душа (рвётся|кричит|плачет|горит|болит)"
])
ACTION: FLAG(organ_cliche)
FIX: replace_with_body_action (раздел 26.3)
```

### 25.4 Бинарная оппозиция свет/тьма

```
PATTERN: (
  text_contains("тьма") OR text_contains("во тьме") OR text_contains("мрак")
) AND (
  text_contains("свет") OR text_contains("свет внутри") OR text_contains("между светом и тьмой")
) AND (
  these_words_form_central_frame: true
)
ACTION: FLAG(binary_light_dark)
FIX: replace_with_concrete_contrast (раздел 26.4)
```

### 25.5 Гипофора (вопрос-ответ)

```
PATTERN: line_ends_with("?") AND next_line_answers_directly
EXAMPLE_BAD:
  "Что мне осталось?
   Только память."
ACTION: FLAG(hypophora)
FIX: remove_question_or_merge (раздел 26.5)
```

### 25.6 Формула «не X, а Y»

```
PATTERN: regex([
  "не просто .* — это был.*",
  "это не .* — это .*",
  "не .* а .*"(как центральная конструкция строки)
])
EXAMPLE_BAD:
  "Это было не просто любовь — это было проклятие"
ACTION: FLAG(not_x_but_y)
FIX: collapse_to_single_statement (раздел 26.6)
```

### 25.7 Стак существительных (3+)

```
PATTERN: count_consecutive_nouns(line) >= 3 AND no_verb_between
EXAMPLE_BAD:
  "одиночество пустота тишина ночи"
ACTION: FLAG(noun_stack)
FIX: break_with_verbs (раздел 26.7)
```

### 25.8 Нанизывание прилагательных (3+)

```
PATTERN: count_consecutive_adjectives_before_noun >= 3
EXAMPLE_BAD:
  "холодный пустой мёртвый серый дом"
ACTION: FLAG(adj_pile)
FIX: keep_max_two (раздел 26.8)
```

### 25.9 Глагольные рифмы

```
PATTERN: end_words_rhyme AND both_are_verbs AND rhyme_is_banal([
  "любить-забыть", "идти-найти", "летать-мечтать", "кричать-молчать",
  "гореть-тереть", "ждать-бежать", "плакать-вакать"
])
ACTION: FLAG(verb_rhyme)
FIX: replace_with_noun_or_loose_rhyme (раздел 26.9)
```

### 25.10 Банальные рифмопары

```
PATTERN: end_words_match([
  "любовь-кровь", "любовь-вновь", "кровь-вновь",
  "ночь-дочь", "ночь-прочь", "дочь-прочь",
  "пора-гора", "слёзы-грёзы", "беда-звезда",
  "туман-обман", "пожар-пожал"
])
ACTION: FLAG(banal_rhyme)
FIX: replace_with_loose_or_assonance (раздел 26.9)
```

### 25.11 Припев-чеклист

```
PATTERN: chorus_section AND count_listing_lines >= 4 AND each_line_is_status_check
EXAMPLE_BAD:
  "температура — норма
   влажность — допуск
   давление — в пределах
   сердце — работает"
ACTION: FLAG(chorus_checklist)
FIX: collapse_to_hook (раздел 26.10)
```

### 25.12 Объяснение позиции

```
PATTERN: text_contains_any([
  "я не сужу", "не мне судить", "я помню всё",
  "я не берусь объяснить", "не мне решать"
])
ACTION: FLAG(position_explanation)
FIX: remove_statement_show_through_action (раздел 26.11)
```

### 25.13 Усечение

```
PATTERN: text_contains([
  "[Продолжение следует", "Потом было",
  "…дальше — позже", "но это уже другая история"
])
ACTION: FLAG(truncation)
FIX: finish_to_end (раздел 26.12)
```

### 25.14 Одинаковая длина строк

```
PATTERN: count syllables_per_line across stanza AND variance < 1.5 AND genre != поппанк AND genre != mantra_refrain
# Нюанс: в поппанке (Пошлая Молли) и в мантре-рефрене (Shortparis) одинаковость — осознанный приём
ACTION: FLAG(uniform_line_length)
FIX: vary_one_line (раздел 26.13)
```

### 25.15 Параллелизм без сдвига

```
PATTERN: count_lines_starting_same_word >= 3 AND no_progression_or_shift
EXAMPLE_BAD:
  "я помню / я знаю / я вижу / я чувствую" (×4 без нарастания)
ACTION: FLAG(parallel_no_shift)
FIX: add_progression_or_break (раздел 26.14)
```

### 25.16 Сводный детектор

Прогон текста = прогон всех паттернов 25.1–25.15. Каждый сработавший паттерн → флаг с весом:

| Паттерн | Вес (вклад в AI-score) |
|---|---|
| tech_metaphor | 2.0 |
| organ_cliche | 1.5 |
| binary_light_dark | 1.5 |
| hypophora | 1.5 |
| not_x_but_y | 1.5 |
| marker_word | 1.0 |
| chorus_checklist | 2.0 |
| position_explanation | 1.5 |
| verb_rhyme | 1.0 |
| banal_rhyme | 1.0 |
| noun_stack | 0.5 |
| adj_pile | 0.5 |
| uniform_line_length | 1.0 |
| parallel_no_shift | 0.5 |
| truncation | 2.0 |

**AI-score = сумма весов сработавших паттернов.**
- 0–1.5 → вероятно живое
- 2–4 → подозрение, нужен REPAIR
- 4.5+ → слоуп, обязательный REPAIR

### 25.17 kantselyarit — канцелярит

```
PATTERN: word_in_set(["является", "данный", "осуществлять", "в рамках",
  "представляет собой", "имеет место", "стоит отметить", "важно понимать"])
ACTION: FLAG(kantselyarit)  # вес 1.5
FIX: 26.16 — разговорный регистр
WHY: русскоязычные LLM-тексты тяготеют к официально-деловому стилю;
     в лирике это мгновенный маркер
```

### 25.18 genitive_metaphor — родительный штамп

```
PATTERN: regex("(осколки|тени|эхо|пламя|нити|шёпот|бездна|океан)
  + род.п.(памяти|прошлого|души|сердца|судьбы|времени|чувств|боли)")
# конструкция «абстракция + родительный падеж абстракции»
ACTION: FLAG(genitive_metaphor)  # вес 1.5
FIX: 26.17 — конкретный объект + действие
EXAMPLES_BAD: "осколки памяти", "тени прошлого", "эхо души", "нити судьбы"
```

### 25.19 em_dash_cascade — тире-каскад

```
PATTERN: count_dash_insertions(line) >= 2 OR среднее тире > 1 на строку по строфе
ACTION: FLAG(em_dash_cascade)  # вес 0.5
FIX: 26.18 — максимум одна вставка, остальное — точки/парцелляция
NOTE: тире — легитимный приём (Цветаева!), флаг только при каскаде
```

### 25.20 simile_chain — цепочка сравнений

```
PATTERN: count("словно|будто|как будто|точно(=как)") >= 2 в строфе
ACTION: FLAG(simile_chain)  # вес 1.0
FIX: 26.19 — оставить одно сравнение или свернуть в метафору-действие
```

### 25.21 sentiment_flatline — эмоциональная стерильность

```
PATTERN: нет ни одного резкого/грязного/негативного слова
  AND тон ровно-возвышенный по всему тексту
ACTION: FLAG(sentiment_flatline)  # вес 1.0
FIX: 26.20 — тело, грязь, резкость (§9, §14 энциклопедии)
WHY: LLM по умолчанию избегают негатива и резкости —
     человеческая лирика заметно «грязнее»
```

### 25.22 perfect_grammar — слишком правильно

```
PATTERN: все предложения полные (подлежащее+сказуемое+дополнение)
  AND нет эллипсиса/парцелляции/разговорных сломов
ACTION: FLAG(perfect_grammar)  # вес 0.5
FIX: 26.21 — эллипсис, парцелляция, слом
```

### 25.23 school_arc — школьная арка

```
PATTERN: куплет 1 = вступление-экспозиция AND финал = вывод-мораль ("и тогда я понял")
ACTION: FLAG(school_arc)  # вес 1.0
FIX: 26.22 — начать с середины сцены (in medias res), финал действием
NOTE: дополняет «закрытый финал с моралью» из §16.5 — теперь ловим и экспозицию
```

### 25.24 triple_rhetoric — риторическая триада

```
PATTERN: перечисление ровно из трёх однородных абстракций: "боль, страх и пустота"
ACTION: FLAG(triple_rhetoric)  # вес 0.5
FIX: 26.23 — оставить одно, самое конкретное
```

### 25.25 genre_autopilot — жанровый автопилот

```
PATTERN: word_in_genre_cliche_set(genre)
# darksynth/синтвейв: "неон", "в свете фар", "город спит", "по венам ток", "вечная ночь"
# рэп: "весь этот мир", "против системы", "с самых низов"
# постпанк: "серые дома"(без конкретики), "пустота внутри"
ACTION: FLAG(genre_autopilot)  # вес 1.0
FIX: 26.24 — переосмыслить или заземлить конкретикой (см. жанровый плейбук)
NOTE: словарь пополняется в каждом жанровом плейбуке
```

### 25.26 vague_deixis — размытый указатель

```
PATTERN: "всё это", "это всё", "что-то большее", "нечто"
  без конкретного референта в соседних строках
ACTION: FLAG(vague_deixis)  # вес 0.5
FIX: 26.25 — конкретный референт или вырезать
```

### 25.27 Добавка к таблице весов (v2.0)

> Источник: Notion-апдейт §25–28 v2.0. При конфликте — новее.

| Паттерн | Вес |
|---|---|
| kantselyarit | 1.5 |
| genitive_metaphor | 1.5 |
| simile_chain | 1.0 |
| sentiment_flatline | 1.0 |
| school_arc | 1.0 |
| genre_autopilot | 1.0 |
| em_dash_cascade | 0.5 |
| perfect_grammar | 0.5 |
| triple_rhetoric | 0.5 |
| vague_deixis | 0.5 |

### 25.28 Hard-fail правило (v2.0)

- Любой флаг веса **2.0** (tech_metaphor, chorus_checklist, truncation) → текст не может получить вердикт выше SUSPECT: обязательный REPAIR, даже если суммарный AI-score низкий.
- Полосы AI-score без изменений (0–1.5 живое · 2–4 подозрение · 4.5+ слоуп), hard-fail работает поверх полос.

### 25.29 Почему не перплексия/burstiness

- Статистические детекторы ловят «предсказуемость» текста, но дают ложные срабатывания на канонических текстах и не работают на коротких формах вроде лирики. Наш детектор — **паттерновый**: ловим конкретные привычки моделей, а не статистику. Из статистики берём одно — вариативность длины и синтаксиса строк (уже покрыто uniform_line_length и parallel_no_shift).

---
