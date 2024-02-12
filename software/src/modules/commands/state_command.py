import struct
from dataclasses import dataclass
from typing import Self

from pyside_app_core.constants import DATA_STRUCT_ENDIAN as Dse

from modules.commands.enum.command_enums import CommandType
from modules.commands.enum.state_enums import StateKind, StateResource
from modules.commands.utils.abstract_command import AbstractCommand


@dataclass(frozen=True)
class StateData:
    kind: StateKind
    resource: StateResource

    @staticmethod
    def packing_format() -> str:
        return f"{Dse}II"

    def pack(self) -> bytearray:
        packed = struct.pack(self.packing_format(), self.kind, self.resource)
        return bytearray(packed)

    @classmethod
    def unpack(cls, raw_data: bytes) -> Self:
        unpacked = struct.unpack(cls.packing_format(), raw_data)
        return cls(*unpacked)


class StateCommand(AbstractCommand[StateData]):
    TYPE = CommandType.STATE

    def encode(self) -> bytearray:
        return self.data.pack()

    @classmethod
    def decode(cls, raw_data: bytes) -> Self:
        return cls(StateData.unpack(raw_data))

    def __str__(self) -> str:
        return f"[{self.TYPE.name}] kind={self.data.kind.name}, resource={self.data.resource.name}"
