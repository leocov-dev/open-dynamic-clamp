from pyqtgraph import (
    ButtonItem,
    mkPen,
    PlotDataItem,
    PlotWidget,
    setConfigOptions,
    ViewBox,
)
from PySide6.QtCore import QSize
from PySide6.QtGui import QColor, QIcon
from PySide6.QtWidgets import QVBoxLayout, QWidget
from pyside_app_core.qt.widgets.object_name_mixin import ObjectNameMixin

from modules.widgets.dummy import times, values


class GraphView(ObjectNameMixin, QWidget):
    def __init__(self, parent: QWidget):
        super(GraphView, self).__init__(parent=parent)

        setConfigOptions(
            antialias=True,
            background=QColor(85, 85, 85),
            foreground=QColor(200, 200, 200),
        )

        _layout = QVBoxLayout()
        _layout.setContentsMargins(5, 5, 0, 5)

        self.setLayout(_layout)

        self._chart = PlotWidget(parent=self)

        self._chart.setMenuEnabled(False)
        self._chart.setMinimumSize(QSize(300, 300))

        _layout.addWidget(self._chart)

        self.membrane_plot: PlotDataItem = self._chart.plot(times, values, pen=mkPen(color=(120, 190, 255), width=1.5))
        btn: ButtonItem = self._chart.getPlotItem().autoBtn
        btn.setPixmap(QIcon(":/std/icons/reload").pixmap(QSize(50, 50)))
        view: ViewBox = self.membrane_plot.getViewBox()
        view.setMenuEnabled(False)
        view.setMouseEnabled(x=True, y=False)
