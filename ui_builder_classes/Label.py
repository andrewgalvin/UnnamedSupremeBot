from PyQt5.QtWidgets import QLabel


class Label(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet(
            """
            QLabel {
                background-color: #3A506B;
                color: #CAF0F8;
                border: 3px solid #0B132B;
                border-radius: 5px;
                font-weight: bold;
            }
            QLabel::hover {
                background-color: #1C2541;
                border: 3px solid #5BC0BE;
            }
            QLabel:pressed {
                background-color: #0B132B;
            }
            """
        )

