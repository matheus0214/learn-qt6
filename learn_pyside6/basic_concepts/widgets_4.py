
import sys

from PySide6.QtWidgets import QComboBox, QMainWindow, QApplication

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("My App")

        widget = QComboBox()
        widget.addItems(["One", "Two", "Three"])
        # widget.setEditable(True)
        # widget.setInsertPolicy(QComboBox.InsertPolicy.InsertAtTop)
        widget.setMaxCount(10)

        widget.currentIndexChanged.connect(self.index_changed)
        widget.currentTextChanged.connect(self.text_changed)

        self.setCentralWidget(widget)

    def index_changed(self, i):
        print(i)

    def text_changed(self, t):
        print(t)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
