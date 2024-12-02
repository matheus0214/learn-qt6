
from PySide6.QtWidgets import  QMainWindow, QApplication, QPushButton

from dialogs_2 import CustomDialog


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        button = QPushButton("Press me for a dialog!")
        button.clicked.connect(self.button_clicked)

        self.setCentralWidget(button)

    def button_clicked(self, s):
        print("click", s)

        dlg = CustomDialog()
        if dlg.exec():
            print("Success")
        else:
            print("Cancel")


app = QApplication()

window = MainWindow()
window.show()

app.exec()
