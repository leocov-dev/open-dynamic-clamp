import html
import logging
from typing import cast, Type

from PySide6.QtCore import QSize, Qt, Slot
from PySide6.QtGui import QFontDatabase
from PySide6.QtWidgets import (
    QHBoxLayout,
    QPlainTextEdit,
    QPushButton,
    QVBoxLayout,
    QWidget,
)
from pyside_app_core import log
from pyside_app_core.qt.widgets.frameless.main_window import FramelessMainWindow
from pyside_app_core.qt.widgets.multi_combo_box import MultiComboBox
from pyside_app_core.services.serial_service.serial_service import SerialService

from modules.commands import (
    AbstractCommand,
    DataPointCommand,
    EchoCommand,
    MessageCommand,
    ParamCommand,
    StateCommand,
)
from modules.commands.enum.command_enums import CommandType
from modules.commands.enum.message_enums import MessageKind
from modules.widgets.auto_scroll import AutoScrollIcon

log.set_level(lvl=logging.DEBUG)


class ConsoleWindow(FramelessMainWindow):
    def __init__(self):
        super(ConsoleWindow, self).__init__()

        # ------------------------------------------------------------------------------
        self._auto_scroll = True

        # ------------------------------------------------------------------------------

        self.setWindowTitle("Serial Console")
        self.setMinimumSize(QSize(600, 400))
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowType.WindowMaximizeButtonHint)
        self.statusBar().hide()

        _central = QWidget(parent=self)
        self.setCentralWidget(_central)

        layout = QVBoxLayout()
        layout.setContentsMargins(8, 8, 8, 8)
        _central.setLayout(layout)

        options = QHBoxLayout()
        layout.addLayout(options)

        self._filter_opts = MultiComboBox[Type[AbstractCommand]](parent=self)
        self._filter_opts.addItems(
            [
                "Message",
                "Echo",
                "DataPoint",
                "Handshake",
                "Parameters",
            ],
            [
                MessageCommand,
                EchoCommand,
                DataPointCommand,
                StateCommand,
                ParamCommand,
            ],
            True,
        )
        options.addWidget(self._filter_opts)

        self._auto_scroll_btn = QPushButton(parent=self)
        self._auto_scroll_btn.setCheckable(True)
        self._auto_scroll_btn.setIcon(AutoScrollIcon())
        self._auto_scroll_btn.setIconSize(QSize(24, 24))
        self._auto_scroll_btn.setToolTip("Auto Scroll")
        self._auto_scroll_btn.setFixedSize(32, 32)
        self._auto_scroll_btn.setChecked(self._auto_scroll)
        self._auto_scroll_btn.clicked.connect(self._set_auto_scroll)
        options.addWidget(self._auto_scroll_btn)

        self._text_box = QPlainTextEdit(parent=self)
        self._text_box.setReadOnly(True)
        self._text_box.setMaximumBlockCount(10000)
        layout.addWidget(self._text_box)

        _font = QFontDatabase.systemFont(QFontDatabase.SystemFont.FixedFont)
        self._text_box.setFont(_font)

    def bind_serial_service(self, serial_service: SerialService):
        serial_service.register_reader(self)

    @Slot(Exception)
    def handle_serial_error(self, error: Exception) -> None:
        self._text_box.appendHtml(self._colorize(f"[ERROR] {error}", "#E90C0C"))

    def _set_auto_scroll(self, val: bool) -> None:
        self._auto_scroll = val

    def _scroll_to_end(self) -> None:
        self._text_box.verticalScrollBar().setValue(self._text_box.verticalScrollBar().maximum())

    @Slot(object)
    def handle_serial_data(self, msg: AbstractCommand) -> None:
        if not self.isWindow():
            # not currently visible, skip data handling
            log.debug(f"skip: {msg}")
            return

        if type(msg) not in self._filter_opts.currentData():
            log.debug(f"filter: {msg}")
            return

        text = self._colorize(str(msg), "#6495ED")
        if msg.TYPE == CommandType.MSG:
            if cast(MessageCommand, msg).kind == MessageKind.DEBUG:
                text = self._colorize(str(msg), "lightgrey")
            elif cast(MessageCommand, msg).kind == MessageKind.INFO:
                text = self._colorize(str(msg), "white")
            elif cast(MessageCommand, msg).kind == MessageKind.WARN:
                text = self._colorize(str(msg), "yellow")
            elif cast(MessageCommand, msg).kind == MessageKind.ERROR:
                text = self._colorize(str(msg), "red")
        if msg.TYPE == CommandType.ECHO:
            text = self._colorize(str(msg), "#7FF03F")

        self._text_box.appendHtml(text)
        if self._auto_scroll:
            self._scroll_to_end()

    @staticmethod
    def _colorize(msg: str, color: str) -> str:
        return f'<span style="color: {color};">{html.escape(msg)}</span>'
