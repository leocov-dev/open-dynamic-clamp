import enum


class MessageKind(enum.IntEnum):
    DECODE_ERROR = 0
    DEBUG = 1
    INFO = 2
    WARN = 3
    ERROR = 4
