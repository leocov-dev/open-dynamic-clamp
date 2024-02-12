from abc import abstractmethod
from enum import IntEnum
from typing import Dict, Generic, TypeVar

from modules.commands import AbstractCommand

DT = TypeVar("DT")
PE = TypeVar("PE", bound=IntEnum)


class AbstractParamCommand(AbstractCommand[DT], Generic[DT, PE]):
    @property
    @abstractmethod
    def values(self) -> Dict[PE, float]:
        raise NotImplementedError
