from PySide6.QtGui import QIcon


class AutoScrollIcon(QIcon):
    def __init__(self):
        super(AutoScrollIcon, self).__init__()

        self.addFile(
            ":/app/icons/auto-scroll-on",
            mode=QIcon.Mode.Normal,
            state=QIcon.State.On,
        )
        self.addFile(
            ":/app/icons/auto-scroll-off",
            mode=QIcon.Mode.Normal,
            state=QIcon.State.Off,
        )
