from enum import IntEnum, StrEnum
from typing import Dict, NamedTuple, TypedDict

from pyqtgraph import SpinBox
from PySide6.QtCore import Qt, Signal, Slot
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QHBoxLayout, QLabel, QSizePolicy, QVBoxLayout, QWidget
from pyside_app_core import log
from pyside_app_core.qt.widgets.object_name_mixin import ObjectNameMixin

from modules.commands.enum.command_enums import CommandType
from modules.commands.param_command import ParamCommand
from modules.commands.utils.helpers import is_cmd_type


class ParamData(NamedTuple):
    label: str
    init_val: int | float
    min_val: int | float
    max_val: int | float
    step: int | float
    unit: str | None


class ParamDefinition(TypedDict):
    type: CommandType
    icon: str
    data: Dict[int, ParamData]


ParamConfig = Dict[str, ParamDefinition]


class ParamListWidget(ObjectNameMixin, QWidget):
    param_changed = Signal()

    OBJECT_NAME = "ParamListWidget"
    TITLE: str

    def __init__(self, title: str, param_def: ParamDefinition, parent: QWidget):
        super(ParamListWidget, self).__init__(parent=parent)

        self._command_type = param_def["type"]
        self.icon = QIcon(param_def["icon"])
        _data = param_def["data"]

        self.TITLE = f"{title} Values"
        self._params: Dict[IntEnum, SpinBox] = {key: self._gen_widget(val) for key, val in _data.items()}

        _layout = QVBoxLayout()
        _layout.setContentsMargins(8, 5, 0, 0)
        _layout.setSpacing(15)
        self.setLayout(_layout)

        _title = QLabel(self.TITLE)
        _title.setObjectName(f"{self.obj_name}_TITLE")
        _layout.addWidget(_title)

        self._form_layout = QVBoxLayout()
        self._form_layout.setContentsMargins(0, 0, 0, 10)
        self._form_layout.setSpacing(5)
        _layout.addLayout(self._form_layout)

        for k, w in self._params.items():
            w.valueChanged.connect(lambda _, x=k: self._on_value_changed(x))
            _row = QHBoxLayout()
            _row.setContentsMargins(0, 0, 0, 0)
            _row.setSpacing(0)
            self._form_layout.addLayout(_row)

            _label = QLabel(_data[k].label)
            _label.setObjectName(f"{self.obj_name}_HEADING")
            _label.setMinimumHeight(30)
            _label.setSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)

            _row.addWidget(_label, alignment=Qt.AlignmentFlag.AlignVCenter)
            _row.addWidget(w, alignment=Qt.AlignmentFlag.AlignVCenter)

    def _on_value_changed(self, kind: StrEnum | IntEnum):
        log.debug(kind.name, self._params[kind].value())

    def _gen_widget(self, config: ParamData) -> SpinBox:
        sb = SpinBox(parent=self)
        sb.setMinimumHeight(30)
        sb.setSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)

        sb.setMinimum(config.min_val)
        sb.setMaximum(config.max_val)
        sb.setValue(config.init_val)
        sb.setSingleStep(config.step)

        if config.unit:
            sb.setOpts(suffix=config.unit, siPrefix=True)

        return sb

    @property
    def current_values(self) -> Dict[StrEnum | IntEnum, int | float]:
        return {k: v.value() for k, v in self._params.items()}

    @Slot(object)
    def handle_serial_data(self, cmd: ParamCommand):
        if is_cmd_type(cmd, self._command_type):
            for kind, value in cmd.values.items():
                self._params[kind].setValue(value)
