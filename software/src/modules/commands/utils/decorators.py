import functools
from typing import Any, Callable, Type, TypeVar

from pyside_app_core import log

from modules.commands.utils.abstract_command import AbstractCommand
from modules.commands.utils.helpers import is_cmd_type
from modules.commands.utils.serialize import DecodedCommand

F = TypeVar("F", bound=AbstractCommand)

CommandHandlerFunc = Callable[[Any, AbstractCommand], None]


def cmd_filter(*types: Type[F]):
    def _inner(func: CommandHandlerFunc):
        @functools.wraps(func)
        def __wrapper(self, command: F):
            if is_cmd_type(command, *types):
                func(self, command)
            else:
                log.warning(f"skipping: {command.TYPE}")

        return __wrapper

    return _inner
