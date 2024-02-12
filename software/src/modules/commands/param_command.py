from enum import IntEnum
from typing import Dict, Mapping, Self

from pyside_app_core.services.serial_service.utils.float_map import FloatMap

from modules.commands.enum.command_enums import CommandType
from modules.commands.utils.abstract_float_map_command import AbstractFloatMapCommand

ParamMapType = Dict[IntEnum, float]


class ParamCommand(AbstractFloatMapCommand[IntEnum, ParamMapType]):
    def __init__(self, cmd_type: CommandType, data: Mapping[IntEnum, float]):
        super(ParamCommand, self).__init__(data)

        self.TYPE = cmd_type

    @classmethod
    def decode(cls, raw_data: bytes) -> Self:
        return cls(FloatMap.unpack(raw_data))

    @property
    def values(self) -> ParamMapType:
        return self.data
