"""Handle with events."""

from PySide6.QtWidgets import QApplication, QMenu, QWidget
from PySide6 import QtGui


class MainWindow(QWidget):
    """Class contains the main window app."""

    def __init__(self) -> None:
        """Initialize the main window."""
        super().__init__()

    def contextMenuEvent(self, event: QtGui.QContextMenuEvent) -> None:
        """Override."""
        context = QMenu(self)
        context.addAction(QtGui.QAction("test 1", self))
        context.addAction(QtGui.QAction("test 2", self))
        context.addAction(QtGui.QAction("test 3", self))
        context.exec(event.globalPos())


app = QApplication()

window = MainWindow()
window.show()


app.exec()
