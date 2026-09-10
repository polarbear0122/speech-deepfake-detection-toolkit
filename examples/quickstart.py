"""Minimal example for the toolkit."""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from sdd_toolkit import compute_eer

labels = [0, 0, 1, 1, 1, 0]
scores = [0.10, 0.25, 0.80, 0.65, 0.90, 0.35]

print(f"Example EER: {compute_eer(labels, scores):.4f}")
