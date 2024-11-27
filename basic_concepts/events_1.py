"""Module to handle with event."""

from PySide6 import QtGui
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow


class MainWindow(QMainWindow):
    """Class represent a main window."""

    def __init__(self) -> None:
        """Initialize a main window."""
        super().__init__()

        self.setMouseTracking(True)

        self.label = QLabel("Click in the window")
        self.setCentralWidget(self.label)

    def mouseMoveEvent(self, event: QtGui.QMouseEvent) -> None:
        """Overide event."""
        self.label.setText("mouse move event")

    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None:
        """Overide event."""
        self.label.setText("mouse press event")

    def mouseReleaseEvent(self, event: QtGui.QMouseEvent) -> None:
        """Overide event."""
        self.label.setText("mouse release event")

    def mouseDoubleClickEvent(self, event: QtGui.QMouseEvent) -> None:
        """Overide event."""
        self.label.setText("mouse double click event")


app = QApplication()

window = MainWindow()
window.show()

app.exec()
