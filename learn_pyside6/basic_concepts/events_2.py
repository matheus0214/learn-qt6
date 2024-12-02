"""Module to handle with event."""

from PySide6 import QtGui
from PySide6.QtCore import Qt
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
        if event.button() == Qt.MouseButton.LeftButton:
            self.label.setText("mousePressEvent LEFT")
        elif event.button() == Qt.MouseButton.MiddleButton:
            self.label.setText("mousePressEvent MIDDLE")
        elif event.button() == Qt.MouseButton.RightButton:
            self.label.setText("mousePressEvent RIGHT")

    def mouseReleaseEvent(self, event: QtGui.QMouseEvent) -> None:
        """Overide event."""
        if event.button() == Qt.MouseButton.LeftButton:
            self.label.setText("mousePressEvent LEFT")
        elif event.button() == Qt.MouseButton.MiddleButton:
            self.label.setText("mousePressEvent MIDDLE")
        elif event.button() == Qt.MouseButton.RightButton:
            self.label.setText("mousePressEvent RIGHT")

    def mouseDoubleClickEvent(self, event: QtGui.QMouseEvent) -> None:
        """Overide event."""
        if event.button() == Qt.MouseButton.LeftButton:
            self.label.setText("mouseDoubleClickEvent LEFT")
        elif event.button() == Qt.MouseButton.MiddleButton:
            self.label.setText("mouseDoubleClickEvent MIDDLE")
        elif event.button() == Qt.MouseButton.RightButton:
            self.label.setText("mouseDoubleClickEvent RIGHT")


app = QApplication()

window = MainWindow()
window.show()

app.exec()
