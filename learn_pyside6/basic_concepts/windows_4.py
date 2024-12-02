
"""Create a basic window."""

from random import randint
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class AnotherWindow(QWidget):
    """Create a 'window' is a QWidget. It it has no parent, it will appear as a free-floating window."""

    def __init__(self):
        """Initialize a new floating window."""
        super().__init__()

        layout = QVBoxLayout()
        self.label = QLabel("Another window %d" % randint(0, 100))
        layout.addWidget(self.label)

        self.setLayout(layout)


class MainWindow(QMainWindow):
    """Create a main window application."""

    def __init__(self):
        """Initialize a main window application."""
        super().__init__()

        self.w = None
        self.button = QPushButton("Push the window")
        self.button.clicked.connect(self.show_new_window)

        self.setCentralWidget(self.button)

    def show_new_window(self, checked):
        """Event when a button is clicked."""
        if self.w is None:
            self.w = AnotherWindow()
            self.w.show()
        else:
            self.w = None

app = QApplication()

main_window = MainWindow()
main_window.show()

app.exec()
