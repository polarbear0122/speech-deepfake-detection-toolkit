"""Evaluate a CSV score file containing label and score columns."""

import argparse
import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from sdd_toolkit import compute_eer


def load_scores(path):
    labels, scores = [], []
    with open(path, newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            labels.append(int(row["label"]))
            scores.append(float(row["score"]))
    return labels, scores


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("score_file", help="CSV with label and score columns")
    args = parser.parse_args()

    labels, scores = load_scores(args.score_file)
    print(f"EER: {compute_eer(labels, scores):.6f}")


if __name__ == "__main__":
    main()
