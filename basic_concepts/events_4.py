"""Handle with events."""

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMenu, QWidget
from PySide6 import QtGui


class MainWindow(QWidget):
    """Class contains the main window app."""

    def __init__(self) -> None:
        """Initialize the main window."""
        super().__init__()
        self.show()

        self.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.customContextMenuRequested.connect(self.on_context_menu)

    def on_context_menu(self, pos) -> None:
        """Override."""
        context = QMenu(self)
        context.addAction(QtGui.QAction("test 1", self))
        context.addAction(QtGui.QAction("test 2", self))
        context.addAction(QtGui.QAction("test 3", self))
        context.exec(self.mapToGlobal(pos))


app = QApplication()

window = MainWindow()

app.exec()
