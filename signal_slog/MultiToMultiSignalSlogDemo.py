from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

'''
自定义信号
pyqtSignal()
'''


class NNSignal(QObject):
    signal1 = pyqtSignal()
    signal2 = pyqtSignal(int)

    def __init__(self):
        super(NNSignal, self).__init__()
        self.signal1.connect(self.call1)
        self.signal1.connect(self.call11)
        self.signal1.emit()

        self.signal2.connect(self.signal1) # 绑定信号1
        self.signal2.emit(2)

        self.signal1.disconnect(self.call1)
        self.signal1.disconnect(self.call11)
        self.signal2.disconnect(self.signal1)

        self.signal2.connect(self.call1)
        self.signal2.connect(self.call2)

        self.signal1.emit()
        self.signal2.emit(2)


    def call1(self):
        print('call1 emit')

    def call11(self):
        print('call11 emit')

    def call2(self, val):
        print('call2 emit', val)


class MySlot(QObject):
    def get(self, msg):
        print('信息:' + msg)


if __name__ == '__main__':
    nnSignal = NNSignal()
