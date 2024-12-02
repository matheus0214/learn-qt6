from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget

from layout_colorwidget import Color


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        layout = QVBoxLayout()

        layout.addWidget(Color("red"))
        layout.addWidget(Color("blue"))
        layout.addWidget(Color("green"))

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)
        

app = QApplication()

window = MainWindow()
window.show()


app.exec()
