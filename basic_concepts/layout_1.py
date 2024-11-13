from PySide6.QtWidgets import QMainWindow, QApplication

from layout_colorwidget import Color


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        widget = Color("red")

        self.setCentralWidget(widget)


app = QApplication()

window = MainWindow()
window.show()

app.exec()
