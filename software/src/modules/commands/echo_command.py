from typing import Self

from pyside_app_core.services.serial_service.utils.conversion_utils import (
    int_from_bytes,
    int_to_bytes,
)

from modules.commands.enum.command_enums import CommandType
from modules.commands.utils.abstract_command import AbstractCommand


class EchoCommand(AbstractCommand[bool]):
    TYPE = CommandType.ECHO

    def encode(self) -> bytearray:
        return bytearray(int_to_bytes(1 if self.data else 0, 1, False))

    @classmethod
    def decode(cls, raw_data: bytes) -> Self:
        val = int_from_bytes(raw_data, False)
        return cls(True if val == 1 else False)

    def __str__(self) -> str:
        return f"[ECHO ] {'<OK>' if self.data else '>NOT-OK<'}"
