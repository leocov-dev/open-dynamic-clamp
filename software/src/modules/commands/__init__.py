from typing import Dict, Type

from .data_point_command import DataPoint, DataPointCommand
from .echo_command import EchoCommand
from .enum.command_enums import CommandType
from .message_command import MessageCommand, MessageData, MessageKind
from .param_command import ParamCommand, ParamMapType
from .state_command import StateCommand, StateData
from .utils.abstract_command import AbstractCommand

CommandTypeMap: Dict[CommandType, Type[AbstractCommand]] = {
    CommandType.ECHO: EchoCommand,
    CommandType.MSG: MessageCommand,
    CommandType.CAL_PARAM: ParamCommand,
    CommandType.COND_PARAM: ParamCommand,
    CommandType.DATA_POINT: DataPointCommand,
    CommandType.STATE: StateCommand,
}
