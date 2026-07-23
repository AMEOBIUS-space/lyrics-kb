# Sound corpus v0.1 — звуковые кейсы

Золотой корпус **звука** (не лирики). Каждый закрытый цикл gen→микс→мастер оставляет строку + lesson.

Источник: Notion Sound corpus v0.1 (2026-07-23 mirror).

---

## Кейсы

### CW-001 — ПОСЛЕДНЕЕ ОКНО ✅ CLOSED
- status: **closed**
- result: good
- fail_mode: thin_low
- LUFS: -12.5 | peak: -0.2 | crest: 14.4
- lesson: dark mix fixed via high shelf +2.5@3kHz + low shelf -2@100Hz
- pipeline: treblo → suno_cover_inspo
- git: `cases/CW-001-poslednee-okno.md`

### CW-011 — ТИШИНА 2.0 ✅ CLOSED
- status: **closed**
- result: good
- fail_mode: thin_low
- LUFS: -13.4 | peak: -0.1
- lesson: same dark mix pattern as CW-001. High shelf +2-3dB@3kHz fixed
- pipeline: treblo → suno_cover
- git: `cases/CW-011-tishina-2.md`

### CW-012 — ТРИ ЦИФРЫ (= CW-002 · ГИЛЬОТИНА) ✅ CLOSED
- status: **closed**
- result: good
- fail_mode: mud_2k
- LUFS: -12.5 | peak: -0.6
- lesson: bell cut -1.5@300Hz (муть) + high shelf +3@3kHz. 3 iterations
- pipeline: treblo → suno_cover
- git: `cases/CW-012-tri-cifry.md`
- note: desk-цикл CW-002 / ТРИСТА СОРОК СЕМЬ — mapping alias

### CW-013 — ЧУЖОЙ ЭТАЖ ✅ CLOSED
- status: **closed**
- fail_mode: thin_low
- lesson: 5 iterations; thin_low pattern holds

### CW-014 — СЧЁТЧИК ИДЁТ ✅ CLOSED
- status: **closed**
- lesson: benchmark presence 11%

---

## Агрегаты

| Метрика | Значение |
|---|---|
| closed cases | **6+** (canon freeze gate reached 2026-07-16) |
| top fail_mode | thin_low |
| package patches | **1** — EQ-стек coldwave default gen |

## Паттерн coldwave

Coldwave gens системно тёмные (thin_high/thin_low). Почти все кейсы потребовали high shelf +2–4 dB @ 3kHz.

**Рабочий EQ-стек на дефолтную Suno-генерацию (coldwave):**
- low shelf −2.5 @ 100 Q0.7
- high shelf +4 @ 3k Q0.7
- high shelf +4 @ 10k Q0.7
- limiter −0.5 dBTP

Вшит в Suno-пакет coldwave — первый package patch (2026-07-16).

---

## Слоты

- **CW-003..CW-010** — coldwave хребет
- **FH-001..FH-002** — folk satellite
- **CL-001..CL-002** — cloud satellite
- **IND-001..** — industrial/neurofunk (fail_modes prefix `IND-*`; coldwave EQ не авто-портить)

### IND-001 — THIRD PASS ⏳ PENDING_GENERATION
- lane: industrial / neurofunk · 140 BPM · F minor
- lyrics score: 8.4 EXCELLENT
- lyrics card: `cases/IND-001-third-pass.md`
- note: coldwave EQ-патч (+4@3k) не брать вслепую

### IND-002 — KILL THE CREST ⏳ PENDING_GENERATION
- lane: industrial / neurofunk · 134 BPM · C# minor
- lyrics score: 8.3 EXCELLENT
- lyrics card: `cases/IND-002-kill-the-crest.md`
- diptych after IND-001
