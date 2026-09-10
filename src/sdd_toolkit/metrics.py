import numpy as np
from sklearn.metrics import roc_curve


def compute_eer(labels, scores):
    """Return equal error rate for binary labels and detection scores."""
    labels = np.asarray(labels)
    scores = np.asarray(scores, dtype=float)
    if labels.shape != scores.shape:
        raise ValueError("labels and scores must have matching shapes")
    fpr, tpr, _ = roc_curve(labels, scores)
    fnr = 1.0 - tpr
    index = np.argmin(np.abs(fnr - fpr))
    return float((fpr[index] + fnr[index]) / 2.0)
