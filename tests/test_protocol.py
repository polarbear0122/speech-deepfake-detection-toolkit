from sdd_toolkit.protocol import ProtocolEntry, parse_protocol_line


def test_parse_minimal_protocol_line():
    entry = parse_protocol_line("utt001 audio/utt001.wav bonafide")
    assert entry == ProtocolEntry("utt001", "audio/utt001.wav", "bonafide")


def test_parse_extended_protocol_line():
    entry = parse_protocol_line("utt002 audio/utt002.wav spoof A07 spk01 eval")
    assert entry.attack_id == "A07"
    assert entry.speaker_id == "spk01"
    assert entry.split == "eval"
