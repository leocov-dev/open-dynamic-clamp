from pyside_app_core.constants import LIST_DATA_LEN_MAX
from pyside_app_core.errors.basic_errors import CoreError


class CommandError(CoreError):
    """base error for commands"""


class CommandEncodingListError(CommandError):
    def __init__(self, actual_len: int):
        super(CommandEncodingListError, self).__init__(
            f"command data list was too long, max: {LIST_DATA_LEN_MAX}, actual: {actual_len}",
            internal=True,
        )
