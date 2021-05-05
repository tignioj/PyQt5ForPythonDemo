import threading

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

'''
匿名内部类的QT多线程
QThreadCounterDemo
'''

class WorkThread:
    class InnerThread(QThread):
        signal = pyqtSignal(dict)

        def __init__(self, invokeFun, callbackFun, invokeParam={}, callbackParam={}):
            super(WorkThread.InnerThread, self).__init__()
            self.callBackFun = callbackFun
            self.invokeParam = invokeParam
            self.callBackParam = callbackParam
            self.invokeFun = invokeFun

        def run(self):
            self.signal.connect(self.callBackFun)
            res = self.invokeFun(self.invokeParam)
            self.signal.emit({'res': res, 'param': self.callBackParam})

    @staticmethod
    def fun1():
        print('fun1', threading.get_ident())

    @staticmethod
    def fun2():
        print('fun1', threading.get_ident())

    @staticmethod
    def calc(param):
        a = param['a']
        b = param['b']
        return ('calc=' + str(a + b))


class QThreadCounterDemo(QWidget):
    def __init__(self):
        super(QThreadCounterDemo, self).__init__()
        self.resize(300, 120)
        self.initUI()

    def initUI(self):
        WorkThread.InnerThread(WorkThread.calc, self.handleSignalClac, {'a': 1, 'b': 2}, {'c': 3, 'd': 4}).start()

    def handleSignalClac(self, params):
        print('handle signal param', params)

    def handleSignal1(self):
        print('handle signal1')

    def handleSignal2(self):
        print('handle signal1')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QThreadCounterDemo()
    # main.show()
    sys.exit(app.exec_())
