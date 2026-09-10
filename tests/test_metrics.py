from sdd_toolkit import compute_eer


def test_compute_eer_returns_probability():
    labels = [0, 0, 1, 1]
    scores = [0.1, 0.2, 0.8, 0.9]
    eer = compute_eer(labels, scores)
    assert 0.0 <= eer <= 1.0
