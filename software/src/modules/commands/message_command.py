import struct
from dataclasses import dataclass
from typing import Self

from pyside_app_core.constants import DATA_STRUCT_ENDIAN
from pyside_app_core.services.serial_service.utils.conversion_utils import (
    int_from_bytes,
)

from modules.commands.enum.command_enums import CommandType
from modules.commands.enum.message_enums import MessageKind
from modules.commands.utils.abstract_command import AbstractCommand


@dataclass(frozen=True)
class MessageData:
    kind: MessageKind
    msg: str

    @classmethod
    def unpack(cls, raw_data: bytes) -> Self:
        kind_raw = raw_data[:1]
        msg_raw = raw_data[1:]

        msg_len_raw = msg_raw[:4]  # pack fmt `I` uses 4 bytes == unsigned long
        msg_encoded = msg_raw[4:]

        kind = int_from_bytes(kind_raw, signed=False)
        msg_len = int_from_bytes(msg_len_raw, signed=False)

        msg: bytes = struct.unpack(f"{DATA_STRUCT_ENDIAN}{msg_len}s", msg_encoded)[0]

        return cls(MessageKind(kind), msg.decode("utf-8"))

    def __eq__(self, other: "MessageData") -> bool:
        return all([self.kind == other.kind, self.msg == other.msg])


class MessageCommand(AbstractCommand[MessageData]):
    TYPE = CommandType.MSG

    @property
    def kind(self) -> MessageKind:
        return self.data.kind

    @property
    def body(self) -> str:
        return self.data.msg

    def encode(self) -> bytearray:
        raise NotImplementedError("sending messages to mcu is not supported")

    @classmethod
    def decode(cls, raw_data: bytes) -> Self:
        return cls(MessageData.unpack(raw_data))

    @classmethod
    def decode_error(cls, err: Exception) -> Self:
        return cls(MessageData(MessageKind.DECODE_ERROR, f"command decoding failed with {err}"))

    def __str__(self) -> str:
        return f"[{self.kind.name: <10}] {self.body}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__} <ID: {self.TYPE}> <Kind: {self.kind}> <Msg: {self.body}>"
