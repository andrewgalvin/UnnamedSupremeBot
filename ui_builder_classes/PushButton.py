from PyQt5.QtWidgets import QPushButton


class PushButton(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet(
            """
            QPushButton {
                background-color: #1C2541;
                color: #CAF0F8;
                border: 3px solid #0B132B;
                border-radius: 5px;
                font-weight: bold;
            }
            QPushButton::hover {
                background-color: #5BC0BE;
                border: 3px solid #5BC0BE;
            }
            QPushButton:pressed {
                background-color: #0B132B;
            }
            """
        )