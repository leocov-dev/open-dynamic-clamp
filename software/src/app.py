import argparse
import sys
from pathlib import Path

from PySide6.QtGui import QAction
from PySide6.QtWidgets import QMenu
from pyside_app_core.errors.excepthook import install_excepthook
from pyside_app_core.qt.widgets.base_app import BaseApp
from pyside_app_core.services import application_service
from pyside_app_core.services.serial_service.serial_service import SerialService

from modules.app.app_main_window import AppMainWindow
from modules.app.console_window import ConsoleWindow
from modules.app.debug_command_window import DebugCommandWindow
from modules.services.command_transcoder_service import CommandTranscoderService
from theme import ODC_THEME


class OpenDynamicClampWorkbench(BaseApp):
    def __init__(self, resources_path: Path, debug=False):
        super(OpenDynamicClampWorkbench, self).__init__(resources_rcc=resources_path)

        # ------------------------------------------------------------------------------

        self._serial_service = SerialService(transcoder=CommandTranscoderService(), parent=self)

        self._main_window = AppMainWindow(debug=debug)

        self._console_window = ConsoleWindow()
        self._debug_command_window = DebugCommandWindow()

        # ------------------------------------------------------------------------------

        self._dock_menu = QMenu()
        self._dock_menu.setAsDockMenu()
        self._dock_menu.addAction(QAction("test", parent=self._dock_menu))

        # ------------------------------------------------------------------------------

        self._serial_service.link(
            self._main_window,
            self._console_window,
            self._debug_command_window,
        )

        # ------------------------------------------------------------------------------
        self._main_window.show_console_window.connect(self._console_window.show)
        self._main_window.show_debug_command_widow.connect(self._debug_command_window.show)

        self.aboutToQuit.connect(self._on_close)

    def launch(self) -> int:
        self._main_window.show()
        return self.exec()

    def _on_close(self) -> None:
        self._console_window.close()
        self._console_window.deleteLater()
        self._main_window.deleteLater()
        self._serial_service.deleteLater()
        self._dock_menu.deleteLater()


if __name__ == "__main__":
    application_service.set_app_version("0.0.1")
    application_service.set_app_id("com.open-dynamic-clamp.workbench")
    application_service.set_app_name("open-dynamic-clamp-workbench")
    application_service.set_app_theme(ODC_THEME)

    resources_file = Path(__file__).parent / "theme" / "resources.rcc"

    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--debug", action="store_true")
    args = parser.parse_args()

    install_excepthook()

    sys.exit(
        OpenDynamicClampWorkbench(
            resources_path=resources_file,
            debug=args.debug,
        ).launch()
    )
