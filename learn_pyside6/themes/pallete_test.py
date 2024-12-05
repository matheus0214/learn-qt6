"""Creating a custom pallet."""

from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QFont, QPalette
from PySide6.QtWidgets import QApplication, QLabel


app = QApplication() 

pallet = QPalette()
pallet.setColor(QPalette.ColorRole.Window, QColor(0, 128, 255))
pallet.setColor(QPalette.ColorRole.WindowText, Qt.GlobalColor.white)

app.setPalette(pallet)

w = QLabel("Pallet Test")
w.setStyleSheet("font-size: 30px")
w.show()

app.exec()
