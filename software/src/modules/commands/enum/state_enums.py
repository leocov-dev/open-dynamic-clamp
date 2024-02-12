from enum import IntEnum


class StateKind(IntEnum):
    PING = 1
    PONG = 2


class StateResource(IntEnum):
    CONNECTION = 1
    CALIBRATION_DATA = 2
