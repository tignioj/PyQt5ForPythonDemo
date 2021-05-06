import time

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

from utils.LogUtils import LogUtils

'''
QThreadCounterDemo
'''

sec = 0


class WorkThread(QThread):
    # signal = pyqtSignal(dict)

    # def __init__(self):
    #     super(WorkThread, self).__init__()
    #     self._mutex = QMutex()
    #     LogUtils.log("Worker", "init")

    def setParam(self, invokeFun, param):
        LogUtils.log("Worker", "setParam", (invokeFun, param))
        self.invokeFun = invokeFun
        self.param = param

    def run(self):
        LogUtils.log("Worker", "run")
        # self._mutex.lock()
        # res = self.invokeFun(self.param)
        # self.signal.emit(res)
        # self._mutex.unlock()

    @staticmethod
    def count(param):
        LogUtils.log("Worker", "counting")
        print("count", param)
        num = param['num']
        return {'res': num + 1}


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

        button.clicked.connect(self.work)

        self.setLayout(layout)

    def handleRes(self, res):
        LogUtils.log("Worker", "handle")
        print("handleRes", res)
        self.lcdNumber.display(int(res['res']))

    def countTime(self):
        global sec
        sec += 1
        self.lcdNumber.display(sec)

    def end(self):
        QMessageBox.information(self, '消息', '计数结束', QMessageBox.Ok)

    def work(self):
        w = WorkThread()
        w.setParam(WorkThread.count, {'num': self.lcdNumber.value()})
        w.signal.connect(self.handleRes)
        w.start()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QThreadCounterDemo()
    main.show()
    sys.exit(app.exec_())
