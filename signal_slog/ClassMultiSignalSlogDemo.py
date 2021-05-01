from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

'''
自定义信号
pyqtSignal()
'''


class MultiSignalDemo(QObject):
    # 定义一个信号
    signal1 = pyqtSignal()
    signal2 = pyqtSignal(int)
    signal3 = pyqtSignal(int, str)
    signal4 = pyqtSignal(list)
    signal5 = pyqtSignal(dict)

    # 声明一个重载版本的信号：也就是槽函数的参数可以是int和str类型，也可以只有一个str类型的参数
    signal6 = pyqtSignal([int, str], [str])

    def __init__(self):
        super(MultiSignalDemo, self).__init__()
        self.signal1.connect(self.signalCall1)
        self.signal2.connect(self.signalCall2)
        self.signal3.connect(self.signalCall3)
        self.signal4.connect(self.signalCall4)
        self.signal5.connect(self.signalCall5)

        # 不指定则默认关联到第一个[str,int]
        self.signal6.connect(self.signalCall6)
        self.signal6.connect(self.signalCall6Overload)

        # 发送信号
        self.signal1.emit()
        self.signal2.emit(10)
        self.signal3.emit(1, 'hello world')
        self.signal4.emit([1, 2, 3, 4, 5, 6])
        self.signal5.emit({"name": "Bill", "age": 18})
        # 调用时候需要指定
        self.signal6[str].emit("test")
        self.signal6[int, str].emit(20, "test")

    def signalCall1(self):
        print('signal1 emit')

    def signalCall2(self, val):
        print('signal2 emit, value:', val)

    def signalCall3(self, val, text):
        print('signal3 emit, value:', val, ", text:", text)

    def signalCall4(self, list):
        print('signal3 emit, list:', list)

    def signalCall5(self, dict):
        print('signal3 emit, dict:', dict)

    def signalCall6(self, val, text):
        print('signal6 emit, value:', val, ", text:", text)

    def signalCall6Overload(self, text):
        print('signal6 overload emit, text:', text)


if __name__ == '__main__':
    send = MultiSignalDemo()
