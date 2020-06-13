import json
import os
import re
import threading
import uuid
import requests
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *

# My custom ui_builder_classes below:
from MonitorV2 import Monitor
from ui_builder_classes.Label import Label
from ui_builder_classes.PushButton import PushButton
from ui_builder_classes.CustomMainWindow import CustomMainWindow
from ui_builder_classes.CustomHelpWindow import CustomHelpWindow
from ui_builder_classes.CustomWelcomeWindow import CustomWelcomeWindow
from ui_builder_classes.Ui_MainWindow import Ui_MainWindow
from ui_builder_classes.Ui_HelpWindow import Ui_HelpWindow
from ui_builder_classes.Ui_WelcomeWindow import Ui_WelcomeWindow


class WelcomeWindow(Ui_WelcomeWindow, CustomWelcomeWindow):
    def __init__(self):
        super().__init__()
        self.setupUi()
        self.pushButton.clicked.connect(self.open_window)
        self.pushCloseButton.clicked.connect(self.close_window)
        self.main = MainWindow()

    def close_window(self):
        self.close()

    def open_window(self):
        self.label.setText("Authenticating...")
        if self.lineEdit_2.text() == "test":
            self.main.show()
            self.close()
            pass
        # with requests.Session() as s:
        #     try:
        #         headers = {
        #             'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        #             'Accept-Encoding': 'gzip, deflate',
        #             'Accept-Language': 'en-US,en;q=0.9',
        #             'Connection': 'keep-alive',
        #             'Host': '5nifk90v489e82hhaswup20e4ew01xu7.us-east-2.elasticbeanstalk.com',
        #             'Upgrade-Insecure-Requests': '1',
        #             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'
        #         }
        #         url = "http://5nifk90v489e82hhaswup20e4ew01xu7.us-east-2.elasticbeanstalk.com/user_list"
        #         try:
        #             info = {
        #                 "license": self.lineEdit_2.text()
        #             }
        #             r = s.get(url=url, data=info, headers=headers)
        #             data = json.loads(r.text)
        #             if "license" in data:
        #                 if self.lineEdit_2.text() == data['license']:
        #                     msg = 'T'.join(re.findall('..', '%012x' % uuid.getnode()))[::-1]
        #                     msg = msg[0:int(int(len(msg) / 2 - 1) / 2 - 1)] + str(data['license'][::-1])[
        #                                                                       int(len(data['license'][::-1]) / 2):len(
        #                                                                           data['license'][::-1])] + str(
        #                         msg[int(len(msg) / 2):len(msg)]) + str(data['license'][::-1])[
        #                                                            0:int(len(data['license'][::-1]) / 2 - 1)]
        #                     msg = msg.encode()
        #                     ip_url = "http://5nifk90v489e82hhaswup20e4ew01xu7.us-east-2.elasticbeanstalk.com/user_list"
        #
        #                     if 'user' in data:
        #                         if data['user'] is None:
        #                             cont = {
        #                                 "auth": "vB3rsG3zhcEzHyf8gueXuYDTm7L0mIXE",
        #                                 "license": data['license'],
        #                                 "user": msg
        #                             }
        #                             s.post(url=ip_url, headers=headers, data=cont)
        #                             self.main.show()
        #                             self.close()
        #                         elif str.encode(data['user']) == msg:
        #                             self.main.show()
        #                             self.close()
        #                         else:
        #                             print(str.encode(data['user']))
        #                             self.label.setText("Do not share keys.")
        #             else:
        #                 self.label.setText("Invalid key.")
        #         except:
        #             self.label.setText("Server down.")
        #     except Exception as e:
        #         print(e)

    def mouseMoveEvent(self, event):
        # Enable mouse dragging
        if event.buttons() == QtCore.Qt.LeftButton:
            self.move(event.globalPos() - self.dragPosition)
            event.accept()

    def mousePressEvent(self, event):
        # Enable mouse dragging
        if event.button() == QtCore.Qt.LeftButton:
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()


class MainWindow(Ui_MainWindow, CustomMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()
        self.setMouseTracking(True)
        self.start_button.clicked.connect(self.create_task)
        self.stop_button.clicked.connect(self.stop)
        self.mini_button.clicked.connect(self.mini)
        # sys.stdout = Stream(newText=self.on_update_text)
        timer = QTimer(self)
        timer.timeout.connect(self.display_time)
        timer.start(1)
        self.help_button.clicked.connect(self.help_menu)
        self.help = HelpWindow()
        self.clear_button.clicked.connect(self.clear)

    def create_task(self):
        if self.name_input.text() == "" or self.color_input == "" or self.size_input.currentText() == "Select a Size":
            if self.name_input.text() == "":
                self.name_input.setStyleSheet(
                    """
                    QLineEdit {
                        background-color: #3A506B;
                        color: #CAF0F8;
                        border: 3px solid red;
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
            else:
                self.name_input.setStyleSheet(
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
            if self.color_input.text() == "":
                self.color_input.setStyleSheet(
                    """
                    QLineEdit {
                        background-color: #3A506B;
                        color: #CAF0F8;
                        border: 3px solid red;
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
            else:
                self.color_input.setStyleSheet(
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
            if self.size_input.currentText() == "Select a Size":
                self.size_input.setStyleSheet(
                    """
                    QComboBox {
                        background-color: #3A506B;
                        color: #CAF0F8;
                        border: 3px solid red;
                        border-radius: 5px;
                        font-weight: bold;
                    }
                    QComboBox::hover {
                        background-color: #1C2541;
                        border: 3px solid #5BC0BE;
                    }
                    QComboBox:pressed {
                        background-color: #0B132B;
                    }
                    """
                )
            else:
                self.size_input.setStyleSheet(
                    """
                    QComboBox {
                        background-color: #3A506B;
                        color: #CAF0F8;
                        border: 3px solid #0B132B;
                        border-radius: 5px;
                        font-weight: bold;
                    }
                    QComboBox::hover {
                        background-color: #1C2541;
                        border: 3px solid #5BC0BE;
                    }
                    QComboBox:pressed {
                        background-color: #0B132B;
                    }
                    QListView{
                    color: #CAF0F8;
                    }
                    """
                )
        else:
            self.name_input.setStyleSheet(
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
            self.color_input.setStyleSheet(
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
            self.size_input.setStyleSheet(
                """
                QComboBox {
                    background-color: #3A506B;
                    color: #CAF0F8;
                    border: 3px solid #0B132B;
                    border-radius: 5px;
                    font-weight: bold;
                }
                QComboBox::hover {
                    background-color: #1C2541;
                    border: 3px solid #5BC0BE;
                }
                QComboBox:pressed {
                    background-color: #0B132B;
                }
                QListView{
                color: #CAF0F8;
                }
                """
            )
            tasks = QtWidgets.QHBoxLayout()
            tasks.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
            tasks.setSpacing(1)

            task_name = Label(self.name_input.text())
            task_name.setFixedSize(175, 30)
            task_name.setAlignment(Qt.AlignCenter)

            task_color = Label(self.color_input.text())
            task_color.setFixedSize(80, 30)
            task_color.setAlignment(Qt.AlignCenter)

            task_size = Label(self.size_input.currentText())
            task_size.setFixedSize(80, 30)
            task_size.setAlignment(Qt.AlignCenter)

            task_status = Label("Click ► to start")
            task_status.setFixedSize(125, 30)
            task_status.setAlignment(Qt.AlignCenter)

            task_start = PushButton("►")
            task_start.setFixedSize(50, 30)

            task_options = QtWidgets.QHBoxLayout()
            task_options.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
            task_options.setSpacing(0)

            task_stop = PushButton("X")
            task_stop.setFixedSize(50, 30)

            task_options.addWidget(task_start)

            task_options.addWidget(task_stop)

            name = task_name.text()
            color = task_color.text()
            size = task_size.text()

            tasks.addWidget(task_name)
            tasks.addWidget(task_color)
            tasks.addWidget(task_size)
            tasks.addWidget(task_status)
            tasks.addLayout(task_options)

            task_stop.clicked.connect(lambda: self.delete_items_of_layout(tasks))
            task_start.clicked.connect(lambda: self.start_task(name, color, size, task_status))

            self.leftVertical2.addLayout(tasks)

    def delete_items_of_layout(self, layout):
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.setParent(None)
                else:
                    self.delete_items_of_layout(item.layout())

    def start_task(self, product, color, size, label):

        if size == 'Select a Size':
            size = ""
        else:
            size = self.size_input.currentText()

        try:
            item_list = []
            task = Monitor()
            t = threading.Thread(target=task.start_search2, args=(
                product, size, color, item_list, label))
            t.start()
        except Exception as e:
            print("\n[ERROR] {0}".format(e))

    def clear(self):
        self.name_input.clear()
        self.size_input.setCurrentIndex(self.size_input.findText("Select a Size"))
        self.color_input.clear()

    def help_menu(self):
        self.help.show()

    def display_time(self):
        current_time = QTime.currentTime()
        display_text = current_time.toString('h:mm:ss ap')
        self.clock_label.setText(display_text)

    def mini(self):
        self.showMinimized()

    def stop(self):
        os._exit(1)

    def mouseMoveEvent(self, event):
        # Enable mouse dragging
        if event.buttons() == QtCore.Qt.LeftButton and not self.size_input.hasFocus():
            self.move(event.globalPos() - self.dragPosition)
            event.accept()

    def mousePressEvent(self, event):
        # Enable mouse dragging
        if event.button() == QtCore.Qt.LeftButton and not self.size_input.hasFocus():
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            os._exit(1)

    # def on_update_text(self, text):
    #     if text.__contains__("RESTOCK") or text.__contains__("SOLD OUT"):
    #         cursor = self.restock_text.textCursor()
    #         cursor.movePosition(QtGui.QTextCursor.End)
    #         cursor.insertText(text)
    #         self.restock_text.setTextCursor(cursor)
    #         self.restock_text.ensureCursorVisible()
    #     else:
    #         cursor = self.task_text.textCursor()
    #         cursor.movePosition(QtGui.QTextCursor.End)
    #         cursor.insertText(text)
    #         self.task_text.setTextCursor(cursor)
    #         self.task_text.ensureCursorVisible()

    # def run_task(self):
    #
    #     if self.size_input.currentText() == 'Select a Size':
    #         size = ""
    #     else:
    #         size = self.size_input.currentText()
    #     name = self.name_input.text()
    #
    #     try:
    #         item_list = []
    #         task = Monitor()
    #         t = threading.Thread(target=task.start_search, args=(
    #             name, size, self.color_input.text(), item_list))
    #         t.start()
    #     except Exception as e:
    #         print("\n[ERROR] {0}".format(e))

    # def start_monitor(self):
    #     if len(self.restock_input.text()) != 0:
    #         list_item = []
    #         monitor = Monitor()
    #         t = threading.Thread(target=monitor.start_specific_monitor,
    #                              args=(self.restock_input.text(), list_item)).start()
    #     else:
    #         try:
    #             monitor = Monitor()
    #             t = threading.Thread(target=monitor.start_monitor).start()
    #         except Exception as e:
    #             print("\n[ERROR] {0}".format(e))


class HelpWindow(Ui_HelpWindow, CustomHelpWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_help_ui()
        self.close_help_button.clicked.connect(self.close_window)

    def close_window(self):
        self.close()

    def mouseMoveEvent(self, event):
        # Enable mouse dragging
        if event.buttons() == QtCore.Qt.LeftButton:
            self.move(event.globalPos() - self.dragPosition)
            event.accept()

    def mousePressEvent(self, event):
        # Enable mouse dragging
        if event.button() == QtCore.Qt.LeftButton:
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()
