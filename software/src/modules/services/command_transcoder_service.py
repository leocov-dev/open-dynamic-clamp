from pyside_app_core.services.serial_service.utils.abstract_decoder import CommandInterface, TranscoderInterface

from modules.commands import AbstractCommand, MessageCommand
from modules.commands.utils.serialize import cobs_decode, cobs_encode


class CommandTranscoderService(TranscoderInterface):
    @classmethod
    def encode_data(cls, command: AbstractCommand) -> bytearray:
        return bytearray(cobs_encode(command))

    @classmethod
    def decode_data(cls, data: bytearray) -> AbstractCommand:
        return cobs_decode(data)

    @classmethod
    def format_error(cls, error: Exception) -> MessageCommand:
        return MessageCommand.decode_error(error)
