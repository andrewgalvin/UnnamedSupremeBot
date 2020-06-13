from PyQt5.QtWidgets import QComboBox

#test
class ComboBox(QComboBox):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet(
            """
            QComboBox {
                background-color: #3A506B;
                color: #CAF0F8;
                border: 3px solid #0B132B;
                border-radius: 5px;
                font-weight: bold;
                padding: 1px 0px 1px 3px;
            }
            QComboBox::hover {
                background-color: #1C2541;
                border: 3px solid #5BC0BE;
            }
            QComboBox:pressed {
                background-color: #3A506B;
            }
            QListView{
                color: #CAF0F8;
            }
            """
        )