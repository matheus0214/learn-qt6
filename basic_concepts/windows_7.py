"""Comunicate between window."""

from PySide6.QtWidgets import QApplication, QLabel, QLineEdit, QMainWindow, QPushButton, QVBoxLayout, QWidget


class AnotherWindow(QWidget):
    """Class to represent another window."""

    def __init__(self) -> None:
        """Initialize another window."""
        super().__init__()

        layout = QVBoxLayout()
        self.label = QLabel("Another window")
        layout.addWidget(self.label)

        self.setLayout(layout)



class MainWindow(QMainWindow):
    """Class to handle with the main window."""

    def __init__(self) -> None:
        """Initialize the main window."""
        super().__init__()

        self.w = AnotherWindow()
        self.button = QPushButton("Push the window")
        self.button.clicked.connect(self.toggle_window)

        self.input = QLineEdit()
        self.input.textChanged.connect(self.w.label.setText)

        layout = QVBoxLayout()
        layout.addWidget(self.button)
        layout.addWidget(self.input)
        
        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

    def toggle_window(self, c):
        """Activated when button is presed."""
        if self.w.isVisible():
            self.w.hide()
        else:
            self.w.show()



app = QApplication()

window = MainWindow()
window.show()

app.exec()
