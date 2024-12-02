"""Designer."""

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

import learn_pyside6.designer.resources

class MainWindow(QMainWindow):
    """Main window class."""

    def __init__(self) -> None:
        """Initialize the main window."""
        super().__init__()
        print("here")
        self.setWindowTitle('Hello word!')
        b = QPushButton("My button")

        icon = QIcon(":/icons/penguin.png")
        b.setIcon(icon)

        self.setCentralWidget(b)

        self.show()


app = QApplication()

window = MainWindow()

app.exec()

