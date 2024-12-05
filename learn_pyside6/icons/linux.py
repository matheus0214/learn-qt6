"""Handle with icons."""

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QPushButton

app = QApplication()

button = QPushButton("Hello")
icon = QIcon.fromTheme("document-new")
button.setIcon(icon)
button.show()

app.exec()
