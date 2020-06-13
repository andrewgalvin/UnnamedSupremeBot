from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QWidget


class CustomDiscordWindow(QWidget):
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setWindowTitle('Help')

        radius = 10.0
        path = QtGui.QPainterPath()

        self.resize(460, 460)
        self.setMinimumSize(QtCore.QSize(460, 460))
        self.setMaximumSize(QtCore.QSize(460, 460))
        self.setStyleSheet(
            "background-color: #0B132B; border-radius: 8px;")
        path.addRoundedRect(QtCore.QRectF(self.rect()), radius, radius)
        mask = QtGui.QRegion(path.toFillPolygon().toPolygon())
        self.setMask(mask)