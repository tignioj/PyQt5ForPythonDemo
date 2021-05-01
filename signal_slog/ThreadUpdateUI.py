import time

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

'''
多线程更新UI数据
ThreadUpdateDataDemo
'''


class BackendThread(QThread):
    update_date_signal = pyqtSignal(str)

    def run(self):
        while True:
            data = QDateTime.currentDateTime()
            currentTime = data.toString('yyyy-MM-dd hh:mm:ss')
            self.update_date_signal.emit(str(currentTime))
            time.sleep(1)


class ThreadUpdateDataDemo(QDialog):
    def __init__(self):
        super(ThreadUpdateDataDemo, self).__init__()
        self.resize(500, 300)
        self.setWindowTitle('多线程更新UI数据')
        self.initUI()

    def initUI(self):
        self.input = QLineEdit(self)
        self.input.resize(400,100)
        self.backend = BackendThread()
        self.backend.update_date_signal.connect(self.handleDisplay)
        self.backend.start()

    def handleDisplay(self, data):
        self.input.setText(data)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = ThreadUpdateDataDemo()
    main.show()
    sys.exit(app.exec_())
