import cobs.cobs
import pytest

from modules.commands import EchoCommand, MessageCommand, MessageData, MessageKind
from modules.commands import AbstractCommand


@pytest.mark.parametrize(
    "command, raw",
    [
        (EchoCommand(data=True), b"\x03\x01\x01"),
        (EchoCommand(data=False), b"\x02\x01\x01"),
        (
            MessageCommand(MessageData(MessageKind.DEBUG, "don't need to be seeing this!")),
            b"\x04\x02\x01\x1d\x01\x01\x1e\x64\x6f\x6e\x27\x74\x20\x6e\x65\x65\x64\x20\x74\x6f\x20\x62\x65\x20\x73\x65\x65\x69\x6e\x67\x20\x74\x68\x69\x73\x21",
        ),
    ],
)
def test_cobs_encode_decode(command, raw: bytes):
    decoded: AbstractCommand = cobs.cobs.decode(raw)

    # TODO - assert what?
