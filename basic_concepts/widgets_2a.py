import os

from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QLabel, QMainWindow, QApplication

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My app")

        widget = QLabel("Hello")
        widget.setPixmap(QPixmap(os.path.join(os.path.dirname(__file__), "cat.jpg")))
        widget.setScaledContents(True)

        self.setCentralWidget(widget)


app = QApplication()

window = MainWindow()
window.show()

app.exec()
