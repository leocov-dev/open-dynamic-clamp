from typing import Type

from cobs import cobs
from pyside_app_core.constants import DATA_ENCODING_ENDIAN
from pyside_app_core.services.serial_service.utils.conversion_utils import int_to_bytes

from modules.commands import AbstractCommand, CommandType, CommandTypeMap


def cobs_encode(command: AbstractCommand) -> bytes:
    byte_data = bytearray(int_to_bytes(command.TYPE, 1, False))
    byte_data.extend(command.encode())

    return cobs.encode(bytes(byte_data))


def cobs_decode(raw_command: bytes) -> AbstractCommand:
    cobs_decoded = cobs.decode(raw_command)
    command_id = CommandType.from_bytes(cobs_decoded[:1], DATA_ENCODING_ENDIAN)
    raw_data = cobs_decoded[1:]

    cmd_klass: Type[AbstractCommand] = CommandTypeMap.get(command_id)
    if not cmd_klass:
        raise NotImplementedError(f"CommandId not implemented: {command_id}")

    return cmd_klass.decode(raw_data)
