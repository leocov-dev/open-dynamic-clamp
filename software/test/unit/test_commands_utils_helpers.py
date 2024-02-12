from typing import List

import pytest

from modules.commands import AbstractCommand, DataPointCommand, EchoCommand, MessageCommand
from modules.commands.enum.command_enums import CommandType
from modules.commands.utils.helpers import CommandFilters, is_cmd_type


@pytest.mark.parametrize(
    "cmd, filters, expected",
    [
        (EchoCommand(True), [EchoCommand], True),
        (EchoCommand(True), [MessageCommand, EchoCommand], True),
        (
            EchoCommand(True),
            [CommandType.ECHO, MessageCommand],
            True,
        ),
        (EchoCommand(True), [DataPointCommand, MessageCommand], False),
        (EchoCommand(True), [CommandType.DATA_POINT, DataPointCommand], False),
    ],
)
def test_is_cmd_type(cmd: AbstractCommand, filters: List[CommandFilters], expected: bool):
    result = is_cmd_type(cmd, *filters)

    assert result == expected
