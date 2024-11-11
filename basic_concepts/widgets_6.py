import sys

from PySide6.QtWidgets import QLineEdit, QMainWindow, QApplication

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("My App")

        widget = QLineEdit()
        widget.setMaxLength(10)
        widget.setPlaceholderText("Enter you text")

        # widget.setReadOnly(True)
        # widget.setInputMask("000.000.000.000;_")

        widget.returnPressed.connect(self.return_pressed)
        widget.selectionChanged.connect(self.selection_changed)
        widget.textChanged.connect(self.text_changed)
        widget.selectionChanged.connect(self.text_edited)

        self.setCentralWidget(widget)

    def return_pressed(self):
        print("Return pressed!")
        print(type(self.centralWidget()))
        self.centralWidget().setText("Boom")

    def selection_changed(self):
        print("Selection changed")
        print(self.centralWidget().selectedText())
        
    def text_changed(self):
        print("Text changed...")

    def text_edited(self):
        print("Text edited...")



app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
