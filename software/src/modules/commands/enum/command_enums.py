import enum
from typing import List


class CommandType(enum.IntEnum):
    ECHO = 1
    MSG = 2
    CAL_PARAM = 3
    COND_PARAM = 4
    DATA_POINT = 5
    STATE = 6


ParamCommandTypes: List[CommandType] = [c for c in CommandType if c.name.endswith("PARAM")]
