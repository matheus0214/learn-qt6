import os

from PySide6.QtCore import QSize
from PySide6.QtGui import QAction, QIcon, Qt
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QStatusBar, QToolBar


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        label = QLabel("Hello!")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.setCentralWidget(label)

        toolbar = QToolBar("My main toolbar")
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)

        button_action = QAction(
            QIcon(os.path.join(os.path.dirname(__file__), "bug.png")),
            "Your button",
            self,
        )
        button_action.setStatusTip("This is yout button")
        button_action.setCheckable(True)
        button_action.triggered.connect(self.onMyToolBarButtonClick)

        toolbar.addAction(button_action)

        self.setStatusBar(QStatusBar(self))

    def onMyToolBarButtonClick(self, s):
        print("click", s)


app = QApplication()

window = MainWindow()
window.show()

app.exec()
