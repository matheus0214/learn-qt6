from PySide6.QtWidgets import QApplication, QPushButton

app = QApplication([])

button = QPushButton()
button.setText("Press me")
button.show()

app.exec()
