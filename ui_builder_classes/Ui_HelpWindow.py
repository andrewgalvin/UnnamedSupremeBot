from PyQt5 import QtWidgets, QtCore

from ui_builder_classes.PushButton import PushButton
from ui_builder_classes.TextEdit import TextEdit


class Ui_HelpWindow(object):
    def setup_help_ui(self):
        self.verticalLayoutWidget = QtWidgets.QWidget(self)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 300, 400))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.help_text = TextEdit(self.verticalLayoutWidget)
        self.help_text.setObjectName("help_text")
        self.help_text.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.help_text)
        self.close_help_button = PushButton(self.verticalLayoutWidget)
        self.close_help_button.setObjectName("pushButton")

        self.close_help_button.setFixedHeight(25)
        self.verticalLayout_2.addWidget(self.close_help_button)

        self.retranslateUi()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.help_text.setText(
            _translate("HelpWindow", "On release day:\n\n[Confirmed] Once items are loaded onto site, "
                                     "start your tasks.\n\n[NEWLY CONFIRMED] Start tasks 5-15 seconds "
                                     "before 11am.\n\nTo start a task input:\n\n-> a product name\n"
                                     "-> a color\n-> a size (if appliciable)\n\nThen click 'Add "
                                     "Task'.\n\nIf you want to get more than one item, start a task "
                                     "for each item."))
        self.close_help_button.setText(_translate("HelpWindow", "Close"))