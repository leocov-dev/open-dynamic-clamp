from enum import IntEnum
from typing import Type

from modules.commands import AbstractCommand
from modules.commands.enum.command_enums import CommandType

CommandFilters = Type[AbstractCommand] | CommandType


def is_cmd_type(cmd: AbstractCommand, *types_filter: CommandFilters) -> bool:
    for f in types_filter:
        if isinstance(f, IntEnum) or isinstance(f, CommandType):
            if cmd.TYPE == f:
                return True

        elif issubclass(cmd.__class__, f):
            return True

    return False
