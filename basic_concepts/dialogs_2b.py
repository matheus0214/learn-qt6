
from PySide6.QtWidgets import QDialog, QDialogButtonBox, QLabel, QVBoxLayout


class CustomDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Hello !")

        buttons = (
            QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
        )

        self.buttonBox = QDialogButtonBox(buttons)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.rejected)

        layout = QVBoxLayout()
        message = QLabel("Somthing happend, is that OK?")

        layout.addWidget(message)
        layout.addWidget(self.buttonBox)

        self.setLayout(layout)
