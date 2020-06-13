from PyQt5.QtCore import QObject, pyqtSignal


class Stream(QObject):
    newText = pyqtSignal(str)

    def write(self, text):
        self.newText.emit(str(text))