from PyQt5.QtWidgets import QLineEdit


class LineEdit(QLineEdit):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet(
            """
            QLineEdit {
                background-color: #3A506B;
                color: #CAF0F8;
                border: 3px solid #0B132B;
                border-radius: 5px;
                font-weight: bold;
            }
            QLineEdit::hover {
                background-color: #1C2541;
                border: 3px solid #5BC0BE;
            }
            QLineEdit:pressed {
                background-color: #0B132B;
            }
            """
        )