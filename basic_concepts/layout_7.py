from PySide6.QtWidgets import QApplication, QMainWindow, QStackedLayout, QWidget

from layout_colorwidget import Color


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        layout = QStackedLayout()

        layout.addWidget(Color("red"))
        layout.addWidget(Color("green"))
        layout.addWidget(Color("blue"))
        layout.addWidget(Color("yellow"))

        layout.setCurrentIndex(0)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)


app = QApplication()

window = MainWindow()
window.show()

app.exec()

