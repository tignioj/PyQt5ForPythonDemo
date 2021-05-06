import time

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

'''
QThreadCounterDemo
'''

sec = 0


class WorkThread(QThread):
    signal = pyqtSignal(dict)
    fun = None
    param = None

    def run(self):
        res = self.fun(self.param)
        time.sleep(5)
        self.signal.emit(res)

    @staticmethod
    def count(param):
        print("count", param)
        num = param['num']
        return {'res': num + 1}

    def invoke(self, fun, param):
        self.fun = fun
        self.param = param
        print("invoke", fun, param)
        self.start()


class QThreadCounterDemo(QWidget):
    def __init__(self):
        super(QThreadCounterDemo, self).__init__()
        self.setWindowTitle('多线程计时器')
        self.resize(300, 120)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        self.lcdNumber = QLCDNumber()
        layout.addWidget(self.lcdNumber)

        button = QPushButton('开始计数')
        layout.addWidget(button)

        self.workThread = WorkThread()
        self.workThread.signal.connect(self.handleRes)
        button.clicked.connect(self.work)

        self.setLayout(layout)

    def handleRes(self, res):
        print("handleRes", res)
        self.lcdNumber.display(res['res'])

    def countTime(self):
        global sec
        sec += 1
        self.lcdNumber.display(sec)

    def end(self):
        QMessageBox.information(self, '消息', '计数结束', QMessageBox.Ok)

    def work(self):
        self.workThread.invoke(WorkThread.count, {'num': self.lcdNumber.value()})


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QThreadCounterDemo()
    main.show()
    sys.exit(app.exec_())
