from PySide6.QtGui import Qt
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QToolBar


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        label = QLabel("Hello!")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.setCentralWidget(label)

        toolbar = QToolBar("My main toolbar")
        self.addToolBar(toolbar)


app = QApplication()

window = MainWindow()
window.show()

app.exec()
