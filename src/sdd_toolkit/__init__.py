"""Core utilities for the Speech Deepfake Detection Toolkit."""

from .metrics import compute_eer
from .protocol import ProtocolEntry, labels, load_protocol, parse_protocol_line

__all__ = [
    "compute_eer",
    "ProtocolEntry",
    "labels",
    "load_protocol",
    "parse_protocol_line",
]
