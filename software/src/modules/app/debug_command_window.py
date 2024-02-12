import logging

from PySide6.QtCore import QSize, Qt, Signal, Slot
from PySide6.QtSerialPort import QSerialPort
from PySide6.QtWidgets import (
    QComboBox,
    QHBoxLayout,
    QPushButton,
    QVBoxLayout,
    QWidget,
)
from pyside_app_core import log
from pyside_app_core.qt.widgets.frameless.main_window import FramelessMainWindow
from pyside_app_core.services.serial_service.serial_service import SerialService

from modules.commands import EchoCommand, ParamCommand, StateCommand, StateData
from modules.commands.enum.command_enums import CommandType
from modules.commands.enum.param_enums import CalParam, CndctParam
from modules.commands.enum.state_enums import StateKind, StateResource

log.set_level(lvl=logging.DEBUG)


class DebugCommandWindow(FramelessMainWindow):
    send_command = Signal(object)

    def __init__(self):
        super(DebugCommandWindow, self).__init__()

        self.setWindowTitle("Command Debugger")
        self.setFixedSize(QSize(600, 400))
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowType.WindowMaximizeButtonHint)
        self.statusBar().hide()

        _central = QWidget(parent=self)
        # _central.setEnabled(False)
        self.setCentralWidget(_central)

        _central.setLayout(QVBoxLayout())

        debug_widgets = [
            self._build_state_cmd_widget(),
            self._build_param_cmd_widget(),
            self._build_echo_cmd_widget(),
        ]

        for dw in debug_widgets:
            _central.layout().addWidget(dw)

        _central.layout().addStretch()

    @Slot(QSerialPort)
    def handle_serial_connect(self, *args):
        self.centralWidget().setEnabled(True)

    @Slot()
    def handle_serial_disconnect(self, *args):
        self.centralWidget().setEnabled(False)

    def bind_serial_service(self, serial_service: SerialService):
        serial_service.register_reader(self)
        self.send_command.connect(serial_service.send_command)

    def _build_state_cmd_widget(self) -> QWidget:
        container = QWidget(parent=self)
        container.setLayout(QHBoxLayout())

        send = QPushButton("StateCommand", parent=self)
        container.layout().addWidget(send)

        kind_sel = QComboBox(parent=self)
        container.layout().addWidget(kind_sel)
        for state in StateKind:
            kind_sel.addItem(state.name, state)

        resource_sel = QComboBox(parent=self)
        container.layout().addWidget(resource_sel)
        for resource in StateResource:
            resource_sel.addItem(resource.name, resource)

        def _on_send():
            cmd = StateCommand(StateData(kind_sel.currentData(), resource_sel.currentData()))
            self.send_command.emit(cmd)

        send.clicked.connect(_on_send)

        return container

    def _build_param_cmd_widget(self) -> QWidget:
        container = QWidget(parent=self)
        container.setLayout(QHBoxLayout())

        send = QPushButton("ParamCommand", parent=self)
        container.layout().addWidget(send)

        cmd_sel = QComboBox(parent=self)
        container.layout().addWidget(cmd_sel)
        variations = {
            "partial calibration a": ParamCommand(CommandType.CAL_PARAM, {CalParam.AMP_i: 50.0}),
            "partial conductance a": ParamCommand(CommandType.COND_PARAM, {CndctParam.G_Shunt: 2.0}),
        }

        for title, cmd in variations.items():
            cmd_sel.addItem(title, cmd)

        def _on_send():
            self.send_command.emit(cmd_sel.currentData())

        send.clicked.connect(_on_send)

        return container

    def _build_echo_cmd_widget(self) -> QWidget:
        container = QWidget(parent=self)
        container.setLayout(QHBoxLayout())

        send = QPushButton("EchoCommand", parent=self)
        container.layout().addWidget(send)

        val_sel = QComboBox(parent=self)
        container.layout().addWidget(val_sel)
        val_sel.addItem("OK", EchoCommand(True))
        val_sel.addItem("NOT-OK", EchoCommand(False))

        def _on_send():
            self.send_command.emit(val_sel.currentData())

        send.clicked.connect(_on_send)

        return container
