from PyQt5 import QtWidgets, QtCore

from ui_builder_classes.Label import Label
from ui_builder_classes.LineEdit import LineEdit
from ui_builder_classes.PushButton import PushButton


class Ui_WelcomeWindow(object):
    def setupUi(self):
        self.verticalLayoutWidget = QtWidgets.QWidget(self)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(50, 50, 400, 200))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = Label(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.label.setFixedSize(250, 50)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
        self.lineEdit_2 = LineEdit(self.verticalLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignVCenter)
        self.lineEdit_2.setFixedHeight(30)
        self.verticalLayout.addWidget(self.lineEdit_2)
        self.pushButton = PushButton(self.verticalLayoutWidget)
        self.pushButton.setFixedHeight(30)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushCloseButton = PushButton(self.verticalLayoutWidget)
        self.pushCloseButton.setFixedHeight(30)
        self.pushCloseButton.setObjectName("pushCloseButton")
        self.verticalLayout.addWidget(self.pushCloseButton)

        self.retranslateUi()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("MainWindow", "Welcome"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "license key"))
        self.pushButton.setText(_translate("MainWindow", "Enter"))
        self.pushCloseButton.setText(_translate("MainWindow", "Close"))