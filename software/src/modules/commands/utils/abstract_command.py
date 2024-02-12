from typing import Generic, Self, TypeVar

from pyside_app_core.services.serial_service.utils.abstract_decoder import CommandInterface

from modules.commands.enum.command_enums import CommandType

T = TypeVar("T")


class AbstractCommand(CommandInterface, Generic[T]):
    TYPE: CommandType

    _data: T

    @property
    def data(self) -> T:
        return self._data

    def __init__(self, data: T):
        self._data = data

    def encode(self) -> bytearray:
        if hasattr(self.data, "pack"):
            return self.data.pack()
        raise NotImplementedError

    @classmethod
    def decode(cls, raw_data: bytes) -> Self:
        raise NotImplementedError

    def __eq__(self, other: Self) -> bool:
        ids_equal = self.TYPE == other.TYPE
        vals_equal = self.data == other.data

        return all([ids_equal, vals_equal])

    def __str__(self) -> str:
        return f"[{self.TYPE.name: <10}] {self.data}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__} <data: {self.data}>"
