import sys

from PySide6.QtWidgets import QListWidget, QMainWindow, QApplication

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("My App")

        widget = QListWidget()
        widget.addItems(["One", "Two", "Three"])

        widget.currentItemChanged.connect(self.item_changed)
        widget.currentTextChanged.connect(self.text_changed)

        self.setCentralWidget(widget)

    def item_changed(self, i):
        print(i.text())

    def text_changed(self, t):
        print(t)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
