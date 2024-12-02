from PySide6.QtWidgets import QApplication, QHBoxLayout, QMainWindow, QPushButton, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Layout")

        layout_v = QVBoxLayout()
        layout_h = QHBoxLayout()

        btn_blue = QPushButton("Blue")
        btn_yellow = QPushButton("Yellow")
        btn_red = QPushButton("Red")

        layout_h.addWidget(btn_blue)
        layout_h.addWidget(btn_yellow)

        layout_v.addLayout(layout_h)
        layout_v.addWidget(btn_red)

        widget = QWidget()
        widget.setLayout(layout_v)

        self.setCentralWidget(widget)


app = QApplication()

window = MainWindow()
window.show()

app.exec()
