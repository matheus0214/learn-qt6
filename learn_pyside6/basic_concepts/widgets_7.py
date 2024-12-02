
import sys

from PySide6.QtWidgets import QMainWindow, QApplication, QSpinBox

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("My App")

        widget = QSpinBox()

        widget.setMinimum(-10)
        widget.setMaximum(3)

        widget.setPrefix("$")
        widget.setSuffix("c")
        widget.setSingleStep(3)

        widget.valueChanged.connect(self.value_changed)
        widget.textChanged.connect(self.value_changed_str)

        self.setCentralWidget(widget)

    def value_changed(self, i):
        print(i)

    def value_changed_str(self, s):
        print(s)
       


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
