from pathlib import Path

from pyside_app_core.generator_utils.style_types import QtResourceFile, QtResourceGroup
from pyside_app_core.qt.style import QssTheme
from pyside_app_core.qt.util.s_color import SColor

__theme_dir = Path(__file__).parent


class _OdcCustomQssTheme(QssTheme):
    experiment_start = SColor(98, 197, 84)
    experiment_stop = SColor(245, 191, 79)


ODC_THEME = _OdcCustomQssTheme()

ODC_RESOURCES = QtResourceGroup(
    prefix="/app",
    files=[
        QtResourceFile(
            str(__theme_dir / "icons" / "auto-scroll-off.svg"),
            alias="icons/auto-scroll-off",
        ),
        QtResourceFile(
            str(__theme_dir / "icons" / "auto-scroll-on.svg"),
            alias="icons/auto-scroll-on",
        ),
        QtResourceFile(
            str(__theme_dir / "icons" / "calibration.svg"),
            alias="icons/calibration",
        ),
        QtResourceFile(
            str(__theme_dir / "icons" / "conductance.svg"),
            alias="icons/conductance",
        ),
        QtResourceFile(
            str(__theme_dir / "icons" / "console.svg"),
            alias="icons/console",
        ),
        QtResourceFile(
            str(__theme_dir / "icons" / "debug-cmds.svg"),
            alias="icons/debug-cmds",
        ),
    ],
)
