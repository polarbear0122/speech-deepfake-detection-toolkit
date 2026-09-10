# Speech Deepfake Detection Toolkit

An open-source research toolkit for **speech deepfake detection**, **attack source tracing**, and **speaker-aware analysis** of synthetic and converted speech.

This project is designed to make experiments in audio deepfake forensics easier to reproduce, extend, and compare. It focuses on modular pipelines for feature extraction, spoof detection, attack attribution, and speaker-related analysis.

## Goals

- Provide reusable building blocks for speech deepfake detection research.
- Support attack-source analysis across TTS and voice-conversion systems.
- Support speaker-aware experiments and source/target-speaker analysis.
- Make experiment configuration and evaluation reproducible.
- Offer simple baselines that can be extended to new datasets and models.

## Research Scope

- Bona fide vs. spoof speech detection
- TTS vs. VC recognition
- Attack / generator source attribution
- Seen vs. unseen attack evaluation
- Speaker identification and speaker-aware spoof analysis
- Acoustic feature baselines and deep representation pipelines

## Repository Structure

```text
speech-deepfake-detection-toolkit/
├── configs/        # Experiment configuration files
├── docs/           # Research notes and roadmap
├── examples/       # Minimal runnable examples
├── scripts/        # Training / evaluation entry points
├── src/            # Reusable Python modules
├── CONTRIBUTING.md
├── LICENSE
├── requirements.txt
└── README.md
```

## Quick Start

```bash
git clone https://github.com/polarbear0122/speech-deepfake-detection-toolkit.git
cd speech-deepfake-detection-toolkit
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
python examples/quickstart.py
```

## Design Principles

1. **Reproducibility** — experiment settings should be explicit and versioned.
2. **Modularity** — datasets, features, models, and metrics should be swappable.
3. **Interpretability** — attribution experiments should reflect meaningful properties of the speech-generation pipeline rather than only dataset IDs.
4. **Open research** — contributions, baselines, documentation, and reproducible experiments are welcome.

## Roadmap

Near-term targets include dataset protocol abstraction, acoustic feature extraction, SSL embeddings, binary spoof detection, TTS/VC classification, attack-source attribution, speaker-aware evaluation, and standard metrics such as EER, macro-F1, recall, and confusion matrices.

See [`docs/ROADMAP.md`](docs/ROADMAP.md) for details.

## Responsible Use

This project is intended for defensive security, academic research, benchmarking, and the development of methods that improve trust in synthetic-media ecosystems. Do not use it to impersonate individuals or facilitate deceptive audio generation.

## Contributing

Contributions are welcome. Please read [`CONTRIBUTING.md`](CONTRIBUTING.md) before opening an issue or pull request.

## Citation

A formal citation will be added when a corresponding public release or paper is available. Until then, please cite this repository URL when referring to the toolkit.

## License

Released under the [MIT License](LICENSE).
