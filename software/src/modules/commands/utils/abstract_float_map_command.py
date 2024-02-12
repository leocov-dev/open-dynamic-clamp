from abc import abstractmethod
from typing import Iterator, Mapping, Self, TypeVar

import pytest
from pyside_app_core.services.serial_service.utils.float_map import FloatMap

from modules.commands.utils.abstract_command import AbstractCommand

K = TypeVar("K", bound=int)
D = TypeVar("D", bound=FloatMap)


class AbstractFloatMapCommand(Mapping[K, float], AbstractCommand[D]):
    def __init__(self, data: Mapping[K, float]):
        super(AbstractFloatMapCommand, self).__init__(data)
        self._data = FloatMap[K](data)

    def __str__(self) -> str:
        format_list = "\n".join([f"  <{k.name}> {v}" for k, v in self.items()])

        return f"[{self.TYPE.name}]\n{format_list}"

    def __eq__(self, other: Self) -> bool:
        return all(
            [
                self.TYPE == other.TYPE,
                self.data == other.data,
            ]
        )

    def __getitem__(self, k: K) -> float:
        return self.data[k]

    def __len__(self) -> int:
        return len(self.data)

    def __iter__(self) -> Iterator[K]:
        return iter(self.data)
