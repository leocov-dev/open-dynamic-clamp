import logging

from PySide6.QtCore import QSize, Qt, Signal, Slot
from PySide6.QtGui import QIcon
from PySide6.QtSerialPort import QSerialPort, QSerialPortInfo
from PySide6.QtWidgets import QComboBox, QHBoxLayout, QPushButton, QSizePolicy, QWidget
from pyside_app_core import log
from pyside_app_core.qt.widgets.dynamic_stacked_widget import DynamicStackedWidget
from pyside_app_core.qt.widgets.object_name_mixin import ObjectNameMixin
from pyside_app_core.qt.widgets.settings_mixin import SettingsMixin

log.set_level(lvl=logging.DEBUG)


class ConnectionConfigWidget(ObjectNameMixin, SettingsMixin, QWidget):
    refresh_ports = Signal()
    request_connect = Signal(QSerialPortInfo)
    request_disconnect = Signal()

    def __init__(self, parent: QWidget):
        super(ConnectionConfigWidget, self).__init__(parent=parent)

        self.setStyleSheet(
            f"""       
        """
        )

        self.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        # ------------------------------------------------------------------------------
        self._layout = QHBoxLayout()
        self.setLayout(self._layout)

        self._refresh_btn = QPushButton(icon=QIcon(":/std/icons/reload"), parent=self)
        self._refresh_btn.setContentsMargins(0, 0, 0, 0)
        self._refresh_btn.setIconSize(QSize(18, 18))
        self._refresh_btn.setToolTip(self.tr("Refresh Device List"))
        self._layout.addWidget(self._refresh_btn)

        self._port_list = QComboBox(self)
        self._layout.addWidget(self._port_list, stretch=4)

        self._stack_layout = DynamicStackedWidget(parent=self)
        self._layout.addWidget(self._stack_layout, stretch=1)

        self._connect_btn = QPushButton(self.tr("Connect"), parent=self)
        self._connect_btn.setFixedWidth(125)
        self._connect_btn.setDisabled(True)
        self._stack_layout.addWidget(self._connect_btn)

        self._disconnect_btn = QPushButton(self.tr("Disconnect"), parent=self)
        self._disconnect_btn.setFixedWidth(125)
        self._stack_layout.addWidget(self._disconnect_btn)

        # ------------------------------------------------------------------------------\
        self._refresh_btn.clicked.connect(self._request_port_refresh)
        self._connect_btn.clicked.connect(self._on_connect_clicked)
        self._disconnect_btn.clicked.connect(self._on_disconnect_clicked)
        self._port_list.currentIndexChanged.connect(self._on_port_selected)

        self._initial_refresh = False

    def _restore_state(self) -> None:
        self._request_port_refresh()
        self._initial_refresh = True

    def _request_port_refresh(self):
        self.setDisabled(True)
        self.refresh_ports.emit()
        self._on_disconnect_clicked()

    def _reset_ui(self):
        self._port_list.setCurrentIndex(0)
        self._port_list.setEnabled(True)
        self._stack_layout.setCurrentIndex(0)

    @Slot(list)
    def handle_serial_ports(self, ports: list[QSerialPortInfo]) -> None:
        self.setEnabled(True)
        self._port_list.clear()
        self._port_list.setPlaceholderText(self.tr("Choose A Device"))

        for port in ports:
            name = port.portName()

            self._port_list.addItem(name, port)

    @Slot(Exception)
    def handle_serial_error(self, error: Exception) -> None:
        self.setDisabled(True)

        self._reset_ui()

    @Slot(QSerialPort)
    def handle_serial_connect(self, com: QSerialPort) -> None:
        self._port_list.setDisabled(True)
        self._stack_layout.setCurrentIndex(1)

    def _on_port_selected(self, index: int):
        port = self._port_list.itemData(index, Qt.ItemDataRole.UserRole)
        self._connect_btn.setEnabled(port is not None)

    def _on_connect_clicked(self) -> None:
        port = self._port_list.currentData(Qt.ItemDataRole.UserRole)
        if port:
            self.request_connect.emit(port)

    def _on_disconnect_clicked(self) -> None:
        self.request_disconnect.emit()
        self._port_list.setEnabled(True)
        self._stack_layout.setCurrentIndex(0)
