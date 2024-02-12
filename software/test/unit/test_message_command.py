import pytest
from cobs.cobs import decode

from modules.commands import MessageData, MessageKind


@pytest.mark.parametrize(
    "cobs_raw, expected_kind, expected_message",
    [
        (
            b"\x04\x02\x01\x1d\x01\x01\x1e\x64\x6f\x6e\x27\x74\x20\x6e\x65\x65\x64\x20\x74\x6f\x20\x62\x65\x20\x73\x65\x65\x69\x6e\x67\x20\x74\x68\x69\x73\x21",
            MessageKind.DEBUG,
            "don't need to be seeing this!",
        ),
    ],
)
def test_message_decode(cobs_raw: bytes, expected_kind, expected_message):
    raw = decode(cobs_raw)
    data = MessageData.unpack(raw[1:])

    assert data.kind == expected_kind
    assert data.msg == expected_message


@pytest.mark.parametrize(
    "raw, expected",
    [
        (
            b"\x02\x0f\x00\x00\x00\x41\x20\x74\x65\x73\x74\x20\x6d\x65\x73\x73\x61\x67\x65\x21",
            MessageData(MessageKind.INFO, "A test message!"),
        )
    ],
)
def test_message_data_unpack(raw: bytes, expected: MessageData):
    data = MessageData.unpack(raw)

    assert data.kind == expected.kind
    assert data.msg == expected.msg
