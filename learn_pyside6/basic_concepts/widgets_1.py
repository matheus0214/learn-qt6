from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel, QMainWindow, QApplication

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My app")

        widget = QLabel("Hello")
        font = widget.font()
        font.setPointSize(30)

        widget.setFont(font)
        widget.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)

        self.setCentralWidget(widget)


app = QApplication()

window = MainWindow()
window.show()

app.exec()
