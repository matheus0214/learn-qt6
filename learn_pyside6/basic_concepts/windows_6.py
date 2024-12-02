"""External window."""

from random import randint
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QVBoxLayout, QWidget


class AnotherWindow(QWidget):
    """New window to appear."""

    def __init__(self) -> None:
        """Initialize a new window."""
        super().__init__()

        layout = QVBoxLayout()
        self.label = QLabel("Another window %d" % randint(0, 100))
        layout.addWidget(self.label)

        self.setLayout(layout)


class MainWindow(QMainWindow):
    """Main window class."""

    def __init__(self) -> None:
        """Initialize the main class."""
        super().__init__()

        self.w = AnotherWindow()
        self.button = QPushButton("Push the window")
        self.button.clicked.connect(self.toggle_window)
        self.setCentralWidget(self.button)


    def toggle_window(self, checked):
        """Show and hide window."""
        if self.w.isVisible():
            self.w.hide()
        else:
            self.w.show()


app = QApplication()

window = MainWindow()
window.show()

app.exec()
