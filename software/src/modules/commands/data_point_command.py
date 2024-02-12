import struct
from dataclasses import dataclass
from typing import Final, Self

from pyside_app_core.constants import DATA_STRUCT_ENDIAN as Dse, STRUCT_FLOAT_FMT as Sff

from modules.commands.enum.command_enums import CommandType
from modules.commands.utils.abstract_command import AbstractCommand


@dataclass(frozen=True)
class DataPoint:
    timestamp: int
    membrane: float
    inject: float
    cycle: float

    @classmethod
    def unpack(cls, raw_data: bytes) -> Self:
        unpacked = struct.unpack(f"{Dse}Q{Sff}{Sff}{Sff}", raw_data)
        return cls(*unpacked)


class DataPointCommand(AbstractCommand[DataPoint]):
    TYPE: Final[CommandType] = CommandType.DATA_POINT

    @property
    def timestamp(self):
        return self.data.timestamp

    @property
    def membrane(self):
        return self.data.membrane

    @property
    def inject(self):
        return self.data.inject

    @property
    def cycle(self):
        return self.data.cycle

    def encode(self) -> bytearray:
        raise NotImplementedError("sending data-point to mcu is not supported")

    @classmethod
    def decode(cls, raw_data: bytes) -> Self:
        return cls(DataPoint.unpack(raw_data))
