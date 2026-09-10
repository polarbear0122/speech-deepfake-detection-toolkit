# Reproducibility Guide

Reproducibility is a core goal of this project. Experiments should make it possible for another researcher to understand exactly what data protocol, features, model configuration, and evaluation procedure were used.

## Minimum experiment record

For each experiment, record:

- Dataset and protocol version
- Train/dev/eval split definition
- Bona fide / spoof label mapping
- Attack IDs and whether they are seen or unseen during training
- Speaker IDs or speaker protocol when relevant
- Feature representation and preprocessing
- Model configuration and random seed
- Optimization settings
- Checkpoint selection criterion
- Evaluation metrics and score direction

## Protocol format

The default text protocol format is:

```text
utterance_id audio_path label attack_id speaker_id split
```

Only the first three columns are required. Missing optional fields may be represented by `-`.

Example:

```text
utt0001 data/utt0001.wav bonafide - spk01 train
utt0002 data/utt0002.wav spoof A07 spk01 train
```

## Seen / unseen attacks

When evaluating generalization, document the exact attack IDs excluded from training. Avoid calling a condition "unseen" unless the generator or attack family is genuinely absent from the training protocol.

## Reporting

At minimum, report the evaluation split and the metric implementation. For attack attribution, prefer both aggregate metrics and per-attack results. For speaker-aware experiments, report performance separately when target/source speaker conditions differ.

## Data handling

Do not commit restricted datasets, private audio, model checkpoints, or personally identifying recordings to this repository. Store only code, protocols that are legally redistributable, metadata templates, and reproducible instructions.
