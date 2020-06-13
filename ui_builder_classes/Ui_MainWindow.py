from PyQt5 import QtWidgets, QtCore

from ui_builder_classes.ComboBox import ComboBox
from ui_builder_classes.Label import Label
from ui_builder_classes.LineEdit import LineEdit
from ui_builder_classes.PushButton import PushButton


class Ui_MainWindow(object):

    def setup_ui(self):
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(5, 5, 590, 490))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.splitLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.splitLayout.setContentsMargins(0, 0, 0, 0)
        self.splitLayout.setObjectName("splitLayout")

        self.leftVertical = QtWidgets.QVBoxLayout()
        self.leftVertical.setObjectName("leftVertical")
        self.leftVerticalName = QtWidgets.QHBoxLayout()
        self.leftVerticalName.setObjectName("leftVerticalName")

        self.rightVertical = QtWidgets.QVBoxLayout()
        self.rightVertical.setObjectName("rightVertical")

        self.rightMenu = QtWidgets.QHBoxLayout()
        self.rightMenu.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.rightMenu.setSpacing(0)
        self.rightMenu.setObjectName("rightMenu")

        self.help_button = PushButton(self.horizontalLayoutWidget_2)
        self.help_button.setObjectName("help_button")
        self.help_button.setFixedHeight(30)
        self.rightMenu.addWidget(self.help_button)

        self.mini_button = PushButton(self.horizontalLayoutWidget_2)
        self.mini_button.setObjectName("mini_button")
        self.mini_button.setObjectName("mini_button")
        self.mini_button.setFixedHeight(30)
        self.rightMenu.addWidget(self.mini_button)

        self.stop_button = PushButton(self.horizontalLayoutWidget_2)
        self.stop_button.setObjectName("stop_button")
        self.stop_button.setFixedHeight(30)
        self.rightMenu.addWidget(self.stop_button)

        self.leftVertical.addLayout(self.rightMenu)

        self.clock_label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.clock_label.setObjectName("clock_label")
        self.clock_label.setStyleSheet("color: #CAF0F8; font: bold; font-size: 12pt;")
        self.clock_label.setAlignment(QtCore.Qt.AlignCenter)
        self.leftVertical.addWidget(self.clock_label)

        spacerItemTop = QtWidgets.QSpacerItem(40, 10, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.leftVertical.addItem(spacerItemTop)

        self.name_input = LineEdit(self.horizontalLayoutWidget_2)
        self.name_input.setObjectName("name_input")
        self.name_input.setFixedHeight(25)
        self.leftVerticalName.addWidget(self.name_input)
        self.leftVertical.addLayout(self.leftVerticalName)

        self.leftVerticalColor = QtWidgets.QHBoxLayout()
        self.leftVerticalColor.setObjectName("leftVerticalColor")

        self.color_input = LineEdit(self.horizontalLayoutWidget_2)
        self.color_input.setObjectName("color_input")
        self.color_input.setFixedHeight(25)
        self.leftVerticalColor.addWidget(self.color_input)
        self.leftVertical.addLayout(self.leftVerticalColor)

        self.leftVerticalSize = QtWidgets.QHBoxLayout()
        self.leftVerticalSize.setObjectName("leftVerticalSize")

        self.size_input = ComboBox(self.horizontalLayoutWidget_2)
        self.size_input.setObjectName("size_input")
        self.size_input.setFixedHeight(25)
        sizes = ['Select a Size', '', 'Small', 'Medium', 'Large', 'XLarge', '6.0', '6.5', '7.0', '7.5', '8.0', '8.5',
                 '9.0',
                 '9.5', '10.0', '10.5', '11.0',
                 '11.5', '12.0',
                 '12.5', '13.0']
        self.size_input.addItems(sizes)
        self.size_input.view().setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.leftVerticalSize.addWidget(self.size_input)
        self.leftVertical.addLayout(self.leftVerticalSize)

        self.leftVerticalStart = QtWidgets.QVBoxLayout()
        self.leftVerticalStart.setObjectName("leftVerticalStart")

        spacerItemBottom = QtWidgets.QSpacerItem(40, 10, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.leftVertical.addItem(spacerItemBottom)

        self.startMenu = QtWidgets.QHBoxLayout()

        self.startMenu.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.startMenu.setSpacing(0)
        self.startMenu.setObjectName("rightMenu")

        self.start_button = PushButton(self.horizontalLayoutWidget_2)
        self.start_button.setObjectName("start_button")

        self.start_button.setFixedHeight(30)
        self.startMenu.addWidget(self.start_button)

        self.clear_button = PushButton(self.horizontalLayoutWidget_2)
        self.clear_button.setObjectName("clear_button")
        self.clear_button.setFixedHeight(30)
        self.startMenu.addWidget(self.clear_button)

        self.leftVerticalStart.addLayout(self.startMenu)
        self.leftVertical.addLayout(self.leftVerticalStart)

        self.tasks = Label("Tasks")
        self.tasks.setFixedHeight(30)
        self.tasks.setStyleSheet(
            """
            QLabel {
                color: #CAF0F8;
                font-weight: bold;
                font-size: 12pt;
            }

            """
        )
        self.tasks.setAlignment(QtCore.Qt.AlignCenter)

        self.leftVertical.addWidget(self.tasks)

        self.task_layout = QtWidgets.QHBoxLayout()
        self.task_label = Label("             Name                                Color                   Size"
                                "                         Status                        Options")
        self.task_label.setFixedHeight(30)
        self.task_label.setStyleSheet(
            """
            QLabel {
                background-color: #1C2541;
                color: #CAF0F8;
                border: 3px solid #0B132B;
                border-radius: 5px;
                font-weight: bold;
            }
            """
        )
        self.task_label.setAlignment(QtCore.Qt.AlignCenter)
        self.task_layout.addWidget(self.task_label)
        self.task_layout.setSpacing(1)
        self.leftVertical.addLayout(self.task_layout)

        self.task_area = QtWidgets.QScrollArea()
        self.task_area.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.task_area.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.task_area.setWidgetResizable(True)
        self.task_area.setObjectName("task_area")

        self.task_area_contents = QtWidgets.QWidget()
        self.task_area_contents.setGeometry(QtCore.QRect(0, 0, 100, 450))
        self.task_area_contents.setObjectName("scrollAreaWidgetContents")
        self.task_area.setWidget(self.task_area_contents)

        self.leftVertical2 = QtWidgets.QVBoxLayout(self.task_area_contents)
        self.leftVertical2.setObjectName("leftVertical2")
        self.leftVerticalName2 = QtWidgets.QHBoxLayout()
        self.leftVerticalName2.setObjectName("leftVerticalName2")

        self.leftVertical.addWidget(self.task_area)

        self.splitLayout.addLayout(self.leftVertical)

        self.retranslateUi()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.start_button.setText(_translate("MainWindow", "+   Add Task"))
        self.clock_label.setText(_translate("MainWindow", "TIME"))
        self.help_button.setText(_translate("MainWindow", u"\U00002048"))
        self.mini_button.setText(_translate("MainWindow", u"\U0001f5d5"))
        self.stop_button.setText(_translate("MainWindow", u"\U0001F5D9"))
        # self.task_text.setText(_translate("MainWindow", "Tasks:\n"))
        self.name_input.setPlaceholderText(_translate("MainWindow", "Name"))
        self.color_input.setPlaceholderText(_translate("MainWindow", "Color"))
        # self.size_input.setPlaceholderText(_translate("MainWindow","Size"))
        self.clear_button.setText(_translate("MainWindow", "⯀  Clear"))