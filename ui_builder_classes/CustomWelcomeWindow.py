from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QWidget


class CustomWelcomeWindow(QWidget):
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setWindowTitle('Welcome!')

        radius = 10.0
        path = QtGui.QPainterPath()

        self.resize(500, 300)
        self.setMinimumSize(QtCore.QSize(500, 300))
        self.setMaximumSize(QtCore.QSize(500, 300))
        self.setStyleSheet(
            "background-color: #0B132B; border-radius: 8px;")
        path.addRoundedRect(QtCore.QRectF(self.rect()), radius, radius)
        mask = QtGui.QRegion(path.toFillPolygon().toPolygon())
        self.setMask(mask)