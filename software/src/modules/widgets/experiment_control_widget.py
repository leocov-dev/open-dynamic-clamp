from PySide6.QtCore import Qt, Signal, Slot
from PySide6.QtSerialPort import QSerialPort
from PySide6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QPushButton,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)

from pyside_app_core.qt.widgets.dynamic_stacked_widget import DynamicStackedWidget
from pyside_app_core.qt.widgets.object_name_mixin import ObjectNameMixin


class ExperimentControlWidget(ObjectNameMixin, QWidget):
    start = Signal()
    stop = Signal()

    def __init__(self, parent: QWidget):
        super(ExperimentControlWidget, self).__init__(parent=parent)

        self.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        self.setContentsMargins(0, 0, 0, 0)
        # ------------------------------------------------------------------------------

        _layout = QVBoxLayout()
        _layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(_layout)

        self._stack = DynamicStackedWidget(parent=self)
        self._stack.setFixedWidth(272)
        _layout.addWidget(self._stack)

        _please_connect = self._build_label()
        self._stack.addWidget(_please_connect)

        _buttons = self._build_buttons()
        self._stack.addWidget(_buttons)

    def _emit_start(self) -> None:
        self._start_btn.setDisabled(True)
        self._start_btn.setText("RUNNING")
        self._stop_btn.setEnabled(True)

        self.start.emit()

    def _emit_stop(self) -> None:
        self._start_btn.setEnabled(True)
        self._start_btn.setText("START")
        self._stop_btn.setDisabled(True)

        self.stop.emit()

    @Slot(QSerialPort)
    def handle_serial_connect(self, *args) -> None:
        self._stack.setCurrentIndex(1)

    @Slot()
    def handle_serial_disconnect(self, *args) -> None:
        self._stack.setCurrentIndex(0)

    def _build_buttons(self) -> QWidget:
        _container = QWidget(self)
        _layout = QHBoxLayout()
        _layout.setContentsMargins(0, 5, 10, 5)
        _container.setLayout(_layout)

        self._start_btn = QPushButton("START", parent=self)
        self._start_btn.setObjectName(f"{self.obj_name}_START")
        _layout.addWidget(self._start_btn)

        self._stop_btn = QPushButton("STOP", parent=self)
        self._stop_btn.setObjectName(f"{self.obj_name}_STOP")
        self._stop_btn.setDisabled(True)
        _layout.addWidget(self._stop_btn)

        # ------------------------------------------------------------------------------
        self._start_btn.clicked.connect(self._emit_start)
        self._stop_btn.clicked.connect(self._emit_stop)

        return _container

    def _build_label(self) -> QWidget:
        _container = QWidget(self)
        _layout = QHBoxLayout()
        _container.setLayout(_layout)

        _label = QLabel(self.tr("Connect to a Device"), parent=self)

        _layout.addWidget(_label, alignment=Qt.AlignmentFlag.AlignHCenter)

        return _container
