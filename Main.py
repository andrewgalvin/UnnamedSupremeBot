import sys
from PyQt5 import QtWidgets
from Gui import MainWindow, WelcomeWindow, HelpWindow

app = QtWidgets.QApplication(sys.argv)
win = WelcomeWindow()
win.show()
sys.exit(app.exec_())

































