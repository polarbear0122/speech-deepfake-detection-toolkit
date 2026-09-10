"""Dataset protocol helpers for speech deepfake experiments."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, List


@dataclass(frozen=True)
class ProtocolEntry:
    """One utterance entry in a dataset protocol.

    Fields are intentionally generic so the same format can represent
    bona fide, TTS, VC, and speaker-aware experiments.
    """

    utterance_id: str
    audio_path: str
    label: str
    attack_id: str = "-"
    speaker_id: str = "-"
    split: str = "-"


def parse_protocol_line(line: str) -> ProtocolEntry:
    """Parse a whitespace-separated protocol line.

    Expected columns:
    utterance_id audio_path label [attack_id] [speaker_id] [split]
    """
    parts = line.strip().split()
    if len(parts) < 3:
        raise ValueError("Protocol line must contain at least 3 columns")

    padded = parts + ["-"] * (6 - len(parts))
    return ProtocolEntry(*padded[:6])


def load_protocol(path: str | Path) -> List[ProtocolEntry]:
    """Load protocol entries, ignoring blank lines and comments."""
    entries: List[ProtocolEntry] = []
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        entries.append(parse_protocol_line(stripped))
    return entries


def labels(entries: Iterable[ProtocolEntry]) -> List[str]:
    """Return labels in input order."""
    return [entry.label for entry in entries]
