# Roadmap

This roadmap tracks planned research and engineering work for the Speech Deepfake Detection Toolkit.

## Phase 1 — Reproducible baselines

- [x] Repository structure and contribution guide
- [x] Minimal EER evaluation utility
- [x] Baseline experiment configuration
- [ ] Dataset protocol interface
- [ ] Score-file evaluation CLI
- [ ] Unit tests for core metrics

## Phase 2 — Acoustic and representation pipelines

- [ ] Utterance-level acoustic feature extraction
- [ ] Frame-level feature aggregation
- [ ] Self-supervised speech embedding interface
- [ ] Feature normalization and caching

## Phase 3 — Deepfake analysis tasks

- [ ] Bona fide vs. spoof detection baseline
- [ ] TTS vs. voice-conversion classification
- [ ] Attack / generator source attribution
- [ ] Seen vs. unseen attack evaluation
- [ ] Per-attack and per-speaker reporting

## Phase 4 — Speaker-aware forensics

- [ ] Speaker identification utilities
- [ ] Target/source-speaker protocol support
- [ ] Joint speaker and spoof analysis
- [ ] Error-analysis tools for attack/source confusion

## Phase 5 — Reproducible benchmark recipes

- [ ] Versioned benchmark configurations
- [ ] Confidence intervals and repeated-run reporting
- [ ] Model cards and experiment reports
- [ ] Community-contributed baselines

The roadmap may evolve as new speech synthesis and voice-conversion methods emerge.
