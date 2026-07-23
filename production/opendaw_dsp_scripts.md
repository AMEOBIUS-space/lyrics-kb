# openDAW MCP DSP Scripts — Complete Reference

**111 DSP scripts** (92 Werkstatt audio effects + 9 Apparat instruments + 10 Spielwerk MIDI effects)

All scripts run on the Werkstatt/Apparat/Spielwerk scriptable device platform in openDAW.
Load via `mcp_opendaw_set_script_device_code`, control params via `mcp_opendaw_set_script_param`.

## Werkstatt (Audio Effects) — 92 scripts

### Dynamics (12)
| Script | Function | Key params |
|--------|----------|------------|
| `werkstatt_compressor.js` | Peak compressor with soft knee | threshold, ratio, attack, release, makeup, mix, knee |
| `werkstatt_lookahead.js` | Lookahead compressor (transparent) | threshold, ratio, attack, release, knee, makeup, mix |
| `werkstatt_limiter.js` | Brickwall limiter | ceiling, release, lookahead, dither, mix |
| `werkstatt_maximizer.js` | Maximizer (loudness, stereo link) | ceiling, release, lookahead, dither, stereo_link, mix |
| `werkstatt_exciter.js` | Harmonic exciter (saturation + HPF) | freq, harmonics, drive, mix, output |
| `werkstatt_deesser.js` | De-esser (dynamic EQ) | freq, threshold, ratio, attack, release, mix, output |
| `werkstatt_transient.js` | Transient designer | attack, sustain, mix, output |
| `werkstatt_noisegate.js` | Noise gate | threshold, attack, hold, release, range |
| `werkstatt_multiband_comp.js` | 3-band multiband compressor (LR4) | crossover1/2, low/mid/high × thr/ratio/atk/rel/gain, mix |
| `werkstatt_expander.js` | Expander (downward) | threshold, ratio, attack, release, range, mix, knee, output |
| `werkstatt_glue_comp.js` | Glue compressor (bus, warmth) | threshold, ratio, attack, release, mix, warmth, output |
| `werkstatt_bass_enhancer.js` | Bass enhancer (sub + harmonics) | freq, sub_level, direct_level, harmonics, attack, release, mix, output |

### Saturation (8)
| Script | Function | Key params |
|--------|----------|------------|
| `werkstatt_darksat.js` | Tape saturation/drive | drive, bias, tone, mix, output |
| `werkstatt_overdrive.js` | Tube overdrive | drive, tone, level, bias, dry |
| `werkstatt_coldfold.js` | Wavefolding + bitcrush | drive, fold, crush, slew, mix |
| `werkstatt_bitcrusher.js` | Bitcrusher + sample-rate reduction | bits, rate, drive, offset, mix |
| `werkstatt_tube_saturator.js` | Tube saturation (harmonic) | drive, warmth, bias, tone, output, mix |
| `werkstatt_fuzz.js` | Fuzz distortion | sustain, tone, octave, gate, bias, level, dry, output |
| `werkstatt_waveshaper.js` | Waveshaper (custom curve) | drive, curve, bias, harmonics, tone, output, mix |
| `werkstatt_multiband_saturator.js` | 3-band multiband saturation | crossover1/2, low/mid/high_drive, low/mid/high_char, output, mix |

### Modulation (10)
| Script | Function | Key params |
|--------|----------|------------|
| `werkstatt_chorus.js` | Stereo chorus | rate, depth, center, feedback, mix |
| `werkstatt_dimension_chorus.js` | Dimension chorus (dual-rate) | rate_l, rate_r, depth, center, phase_offset, width, brightness, mix, output |
| `werkstatt_flanger.js` | Flanger (comb sweep) | rate, depth, center, feedback, mix |
| `werkstatt_phaser.js` | Phaser (allpass sweep) | rate, depth, stages, base_freq, feedback, mix, stereo |
| `werkstatt_tremolo.js` | Tremolo (amplitude LFO) | rate, depth, shape, phase |
| `werkstatt_harmonic_tremolo.js` | Harmonic tremolo (freq-split) | rate, depth, crossover, shape, phase_offset, mix, output |
| `werkstatt_vibrato.js` | Vibrato (pitch LFO) | rate, depth, shape, stereo |
| `werkstatt_rotary_speaker.js` | Rotary speaker (Leslie) | speed, depth, crossover, horn_level, rotor_level, acceleration, mix |
| `werkstatt_auto_pan.js` | Auto-pan (LFO-driven) | rate, depth, shape, phase, width, offset |
| `werkstatt_auto_wah.js` | Auto-wah (envelope follower) | attack, release, min_freq, max_freq, resonance, mix |

### Reverb (6)
| Script | Function | Key params |
|--------|----------|------------|
| `werkstatt_reverb.js` | Plate reverb | decay, predelay, damping, width, mix |
| `werkstatt_shimmer.js` | Shimmer reverb (pitch-shifted tail) | time, feedback, pitch, shimmer, damping, mix |
| `werkstatt_spring_reverb.js` | Spring reverb (physical model) | decay, damp, tension, boing, mix |
| `werkstatt_convolution_reverb.js` | Convolution reverb (generated IR) | room_size, decay, damping, predelay, early_late, width, mix, output |
| `werkstatt_gated_reverb.js` | Gated reverb (80s drum) | decay, predelay, damping, width, threshold, hold, release, mix, output |
| `werkstatt_dereverb.js` | De-reverb (reverb reduction) | reduction, decay_est, sensitivity, bands, preserve, mix, output |

### Delay (5)
| Script | Function | Key params |
|--------|----------|------------|
| `werkstatt_stereo_delay.js` | Stereo delay with ping-pong | time_l, time_r, feedback, tone, mix, pingpong |
| `werkstatt_tape_delay.js` | Tape delay (wow/flutter/saturation) | time, feedback, wow, flutter, saturation, mix |
| `werkstatt_multitap_delay.js` | 4-tap delay with per-tap control | tap1-4 × time/level/pan/fb, spread, damping, mix, output |
| `werkstatt_reverse_delay.js` | Reverse delay (reverse buffer) | time, feedback, levels, pan, fade, damping, mix, output |
| `werkstatt_grain_delay.js` | Granular delay (pitch-shift grains) | delay, grain_size, grain_rate, pitch, scatter, pan, reverse, feedback, mix, output |

### EQ (5)
| Script | Function | Key params |
|--------|----------|------------|
| `werkstatt_paraeq.js` | Parametric EQ (3-band + HP/LP) | band1-3 × freq/gain/q, hp_freq, lp_freq, mix |
| `werkstatt_graphic_eq.js` | 10-band graphic EQ (ISO) | band_32/64/125/250/500/1k/2k/4k/8k/16k, master |
| `werkstatt_dynamic_eq.js` | Dynamic EQ (3-band, threshold-driven) | band1-3 × freq/gain/q/threshold/range, attack, release, mix, output |
| `werkstatt_tilt_eq.js` | Tilt EQ (spectral balance) | tilt, pivot, steepness, mix, output |
| `werkstatt_matching_eq.js` | Matching EQ (auto-match target) | target, match_amt, smooth, adapt_rate, tilt, mix, output |

### Filter / Pitch / Time / Stereo / Spectral / Restoration / Physical / Creative
См. полный перечень в исходнике `russian-lyrics-kb` — 12 filter + 9 pitch + 4 time + 5 stereo + 6 spectral + 6 restoration + 2 physical + 6 creative FX.

## Apparat (Instruments) — 9 scripts
| Script | Function |
|--------|----------|
| `apparat_darkbass.js` | Subtractive bass synth |
| `apparat_coldlead.js` | FM lead synth |
| `apparat_subcrusher.js` | Sub bass + distortion |
| `apparat_pluck.js` | Karplus-Strong plucked string |
| `apparat_wavetable.js` | Wavetable synth |
| `apparat_fm.js` | FM synth |
| `apparat_ringmod.js` | Ring modulation synth |
| `apparat_supersaw.js` | Supersaw synth |
| `apparat_bowed_string.js` | Bowed string physical model |

## Spielwerk (MIDI Effects) — 10 scripts
| Script | Function |
|--------|----------|
| `spielwerk_arpeggiator.js` | Arpeggiator |
| `spielwerk_powerchord.js` | Power chord generator |
| `spielwerk_chorder.js` | Chord generator |
| `spielwerk_chordmemory.js` | Chord memory |
| `spielwerk_scale_quantizer.js` | Scale quantizer |
| `spielwerk_strum.js` | Strum pattern |
| `spielwerk_harmonizer.js` | MIDI harmonizer |
| `spielwerk_mididelay.js` | MIDI delay |
| `spielwerk_prob_gate.js` | Probabilistic gate |
| `spielwerk_velocity.js` | Velocity scaler |

## DSP Chains (presets)

### Mastering chain
EQ (parametric) → Compressor → Exciter → Stereo width → Limiter

### Vocal chain
EQ (parametric) → Compressor → De-esser → Exciter → Limiter

### Lo-fi chain
Bitcrusher → Tape saturation → Tape delay (wow/flutter) → Spring reverb

### Vinyl character chain
Scratch → Reverse (triggered) → Tube saturator → Graphic EQ

### Vocoder chain
Formant filter → Vocoder (carrier: saw) → Graphic EQ → Exciter

### Drum bus chain
Transient designer → Glue compressor → Multiband saturator → Maximizer

## Categories Summary

| Category | Count |
|----------|-------|
| Dynamics | 12 |
| Saturation | 8 |
| Modulation | 10 |
| Reverb | 6 |
| Delay | 5 |
| EQ | 5 |
| Filter | 12 |
| Pitch | 9 |
| Time | 4 |
| Stereo | 5 |
| Spectral/FX | 6 |
| Restoration | 6 |
| Physical Modeling | 2 |
| Creative FX | 6 |
| Apparat | 9 |
| Spielwerk | 10 |
| **Total** | **111** |

*Updated: 2026-07-06, opendaw-mcp v1.247.0. Full param tables preserved in source russian-lyrics-kb.*
