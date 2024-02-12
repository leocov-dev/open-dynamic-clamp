from PySide6.QtCore import QSize, Qt, Signal
from PySide6.QtGui import QAction, QCloseEvent, QIcon
from PySide6.QtWidgets import (
    QApplication,
    QDialog,
    QHBoxLayout,
    QProgressBar,
    QVBoxLayout,
    QWidget,
)
from pyside_app_core.qt.widgets.frameless.main_window import FramelessMainWindow
from pyside_app_core.qt.widgets.tool_stack import ToolStack
from pyside_app_core.services.serial_service.serial_service import SerialService

from modules.widgets.connection_config_widget import ConnectionConfigWidget
from modules.widgets.experiment_control_widget import ExperimentControlWidget
from modules.widgets.graph_view import GraphView
from modules.widgets.param_list_widget import ParamListWidget
from parameters import PARAMETERS


class AppMainWindow(FramelessMainWindow):
    close_window = Signal()
    show_console_window = Signal()
    show_debug_command_widow = Signal()
    toggle_debug = Signal(bool)

    def __init__(self, debug=False):
        super(AppMainWindow, self).__init__()

        self._debug = debug

        # ------------------------------------------------------------------------------
        # self.setWindowTitle(self.tr("Open Dynamic Clamp Workbench"))
        self.setMinimumSize(QSize(800, 480))

        # ------------------------------------------------------------------------------
        self._setup_main_menu()
        self._setup_main_toolbar()
        self._setup_status_bar()

        # ------------------------------------------------------------------------------
        _central = QWidget(parent=self)
        self.setCentralWidget(_central)

        _central_layout = QVBoxLayout()
        _central_layout.setContentsMargins(0, 0, 0, 0)
        _central_layout.setSpacing(0)
        self.centralWidget().setLayout(_central_layout)

        _top_layout = QHBoxLayout()
        _top_layout.setSpacing(5)
        _central_layout.addLayout(_top_layout, stretch=4)

        _graph = GraphView(parent=self)
        _top_layout.addWidget(_graph)

        _tool_stack = ToolStack(
            "right",
            parent=self,
            theme=self._theme,
            menu=self._tool_menu,
        )
        _top_layout.addWidget(_tool_stack)

        for name, param_def in PARAMETERS.items():
            _param_widget = ParamListWidget(name, param_def, parent=self)
            _tool_stack.add_widget(_param_widget.icon, _param_widget, self.tr(_param_widget.TITLE))

        _bottom_layout = QHBoxLayout()
        _bottom_layout.setSpacing(0)
        _central_layout.addLayout(_bottom_layout)

        self._connection_config = ConnectionConfigWidget(parent=self)
        _bottom_layout.addWidget(self._connection_config)

        self._experiment_ctl = ExperimentControlWidget(parent=self)
        _bottom_layout.addWidget(self._experiment_ctl)

    def bind_serial_service(self, serial_service: SerialService):
        self._connection_config.request_disconnect.connect(serial_service.close_connection)
        self._connection_config.request_connect.connect(serial_service.open_connection)
        self._connection_config.refresh_ports.connect(serial_service.scan_for_ports)
        serial_service.register_reader(self._connection_config)

        serial_service.register_reader(self._experiment_ctl)

    def _setup_main_menu(self) -> None:
        _menu_bar = self.menu_bar

        with _menu_bar.add_menu(self.tr("File")) as file_menu:
            with file_menu.add_action(self.tr("Quit")) as exit_action:
                exit_action.setMenuRole(QAction.MenuRole.QuitRole)
                exit_action.triggered.connect(self.close)

        with _menu_bar.add_menu(self.tr("View")) as view_menu:
            with view_menu.add_menu(self.tr("Tool Windows")) as tool_window_menu:
                self._tool_menu = tool_window_menu

            with view_menu.add_action(self.tr("Debug Console")) as console_action:
                console_action.triggered.connect(self.show_console_window.emit)
                console_action.setVisible(self._debug)
                self.toggle_debug.connect(console_action.setVisible)
            with view_menu.add_action(self.tr("Debug Commands")) as debug_cmd_action:
                debug_cmd_action.triggered.connect(self.show_debug_command_widow.emit)
                debug_cmd_action.setVisible(self._debug)
                self.toggle_debug.connect(debug_cmd_action.setVisible)

        with _menu_bar.add_menu(self.tr("Help")) as help_menu:
            with help_menu.add_action(self.tr("About")) as about_action:
                about_action.setMenuRole(QAction.MenuRole.AboutRole)
                dialog = QDialog(self)
                dialog.setWindowTitle(about_action.text())
                about_action.triggered.connect(dialog.show)
            with help_menu.add_action(self.tr("Show Debug Utilities")) as debug_util_action:
                debug_util_action.setCheckable(True)
                debug_util_action.setChecked(self._debug)

                def _switch_debug():
                    self._debug = not self._debug
                    self.toggle_debug.emit(self._debug)

                debug_util_action.triggered.connect(_switch_debug)

    def _setup_main_toolbar(self) -> None:
        self.tool_bar.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonIconOnly)

        with self.tool_bar.add_action(self.tr("Save"), QIcon(":/std/icons/save")) as bar_save_action:
            pass

        # with tool_bar.add_action(self.tr('Load')) as bar_load_action:
        #     bar_load_action.setIcon(STD_LOAD(self))

        # with tool_bar.add_action(self.tr('Export')) as bar_export_action:
        #     bar_export_action.setIcon(STD_FILE(self))

        with self.tool_bar.add_action(self.tr("Console"), QIcon(":/app/icons/console")) as bar_console_action:
            bar_console_action.triggered.connect(self.show_console_window.emit)
            bar_console_action.setVisible(self._debug)
            self.toggle_debug.connect(bar_console_action.setVisible)
        with self.tool_bar.add_action(
            self.tr("Debug Commands"), QIcon(":/app/icons/debug-cmds")
        ) as bar_debug_cmd_action:
            bar_debug_cmd_action.triggered.connect(self.show_debug_command_widow.emit)
            bar_debug_cmd_action.setVisible(self._debug)
            self.toggle_debug.connect(bar_debug_cmd_action.setVisible)

    def _setup_status_bar(self) -> None:
        self.statusBar().show()
        self._progress = QProgressBar(parent=self)
        self._progress.setMaximumWidth(200)
        self._progress.setMinimum(0)
        self._progress.setMaximum(100)
        self._progress.setVisible(False)

        self.statusBar().addPermanentWidget(self._progress)

        self.statusBar().showMessage("Connect A Device...")

    def closeEvent(self, event: QCloseEvent) -> None:
        QApplication.exit(0)
        super().closeEvent(event)
