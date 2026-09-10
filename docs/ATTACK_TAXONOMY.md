# Attack Taxonomy for Speech Deepfake Research

Speech deepfake datasets often assign one label per attack system. That is useful for bookkeeping, but it can hide the physical or algorithmic structure shared by different systems. This project therefore encourages describing attacks by generation components in addition to dataset IDs.

## Recommended levels of description

### 1. Generation paradigm

At the highest level, identify whether the sample is:

- Bona fide speech
- Text-to-speech (TTS)
- Voice conversion (VC)
- Hybrid or otherwise unspecified synthetic speech

### 2. Linguistic or content source

Record how linguistic content enters the generation pipeline when known:

- Text input
- Source speech
- Content encoder / unit representation
- Automatic speech recognition or discrete speech units

### 3. Acoustic / representation model

When available, record the model family that predicts or transforms an acoustic representation, for example:

- Autoregressive acoustic model
- Transformer-based acoustic model
- Diffusion / flow-based acoustic model
- Encoder-decoder conversion model
- Retrieval- or nearest-neighbor-based conversion model
- Self-supervised representation conversion pipeline

The goal is not to force every system into a single taxonomy, but to capture meaningful common structure between attacks.

### 4. Waveform generator / vocoder

The waveform-generation stage can leave artifacts that are shared across otherwise different attacks. When known, record the vocoder or waveform synthesis family separately from the acoustic model.

### 5. Speaker conditioning

Speaker information should be described independently when possible:

- Single-speaker model
- Multi-speaker model
- Speaker embedding conditioned
- Reference-audio conditioned
- Zero-shot / few-shot speaker conditioning
- Source-to-target conversion

### 6. Seen / unseen status

Seen and unseen should be defined at the level being tested. A dataset attack ID may be unseen while some of its components are not.

Useful distinctions include:

- Unseen attack ID
- Unseen acoustic model family
- Unseen vocoder
- Unseen conversion model
- Unseen target speaker
- Unseen source speaker
- Unseen combination of otherwise seen components

## Why component-level labels matter

A classifier trained directly on attack IDs may learn dataset-specific shortcuts rather than properties of the underlying generation process. Component-level analysis can reveal whether errors occur because two attacks share an acoustic model, vocoder, speaker-conditioning mechanism, or another generation component.

This also makes confusion matrices easier to interpret: a "wrong" attack-ID prediction may still be physically meaningful if the predicted and true attacks share substantial parts of the synthesis pipeline.

## Suggested metadata fields

Where licensing and dataset documentation permit, attack metadata may include:

```text
attack_id
generation_paradigm
content_representation
acoustic_model_family
conversion_model_family
vocoder_family
speaker_conditioning
source_speaker_status
target_speaker_status
seen_status
notes
```

Unknown fields should remain explicitly unknown rather than being guessed from model outputs or filenames.
