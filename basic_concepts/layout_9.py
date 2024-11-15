
from PySide6.QtWidgets import QApplication, QHBoxLayout, QMainWindow, QPushButton, QStackedLayout, QTabWidget, QVBoxLayout, QWidget

from layout_colorwidget import Color


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        tabs = QTabWidget()
        tabs.setTabPosition(QTabWidget.TabPosition.West)
        tabs.setMovable(True)
        tabs.setDocumentMode(True)

        for _, color in enumerate(["red", "green", "blue", "yellow"]):
            tabs.addTab(Color(color), color)

        self.setCentralWidget(tabs)

app = QApplication()

window = MainWindow()
window.show()

app.exec()

