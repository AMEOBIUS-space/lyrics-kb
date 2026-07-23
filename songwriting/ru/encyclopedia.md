# Энциклопедия русскоязычной лирики и сонграйтинга (v2.0)

Полный рабочий справочник (30 разделов, ~3000 строк).

> **Полный текст:** [`russian-lyrics-kb/songwriting/encyclopedia.md`](https://github.com/AMEOBIUS-space/russian-lyrics-kb/blob/main/songwriting/encyclopedia.md)  
> SHA blob: `31ed0fef97e424cf720cc5b6f4e8f6905e536cf8`  
> Причина pointer-файла: размер ~179KB — бинарный лифт через API в этом прогоне; содержимое идентично источнику.

## Оглавление

0. Принципы
1. Пантеон
2. Метрика и ритмика
3. Рифма
4. Структура песни
5. Образная система
6. Синтаксис лирики
7. Голос лирического героя
8. Регистровый контраст
9. Эстетика уродливого и телесный код
10. Звукопись и фонетика
11. Интертекстуальность и миф
12. Жанровые спецификации
13. Хук и припев
14. Тёмная и explicit-лирика
15. Сленг-словарь по жанрам
16. Анти-AI-словарь
17. Пайплайн написания
18. Калибровка по авторам
19. Разборы треков
20. Чек-листы
21. Упражнения
22. AI-операционная карта
23. Деревья решений
24. Векторы стиля
25. Паттерны детекции (Детектор 2.0 — 25 паттернов)
26. Правила трансформации
27. Шаблоны генерации
28. Функция оценки (P1–P12)
29. Промпт-скаффолды
30. Машинно-читаемые блоки (JSON/YAML)

## Ключевые блоки (quick ref)

**Детектор 2.0:** 25 паттернов AI-маркеров с весами, hard-fail (вес 2.0 → cap SUSPECT), white-list 25.27 (причитное усечение, припев-формула с накоплением).

**Scoring 2.0:** P1 concreteness · P2 rhythm_variance · P3 rhyme_quality · P4 register_contrast · P5 body_code · P6 ugly_aesthetics · P7 phonetics · P8 hook_strength · P9 voice_embodiment · P10 anti_ai_clean · P11 singability · P12 cohesion. Порог GOOD ≥ 7.0.

**Связанные файлы в lyrics-kb:**
- `detector/ru/README.md` — точка входа детектора
- `references/golden_corpus.md` — 14 регрессионных кейсов
- `references/pantheon_v2.md` — апдейт пантеона
- `songwriting/ru/modern_russian_lyrics.md` — голос и стиль
- `songwriting/ru/pipeline_demo_ep.md` — прогон EP
