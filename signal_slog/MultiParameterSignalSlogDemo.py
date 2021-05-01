from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

'''
自定义信号
pyqtSignal()
'''


class MyTypeSignal(QObject):
    # 定义一个信号
    sendmsg = pyqtSignal(object)

    # 发送三个参数的信号
    sendmsg_multiparam = pyqtSignal(str, int, int)

    def run(self):
        self.sendmsg.emit('Hello PyQt5')

    def sendMulti(self):
        self.sendmsg_multiparam.emit("hello", 3, 4)


class MySlot(QObject):
    def get(self, msg):
        print('信息:' + msg)

    def getMulti(self, msg, a, b):
        print(msg, a + b)


if __name__ == '__main__':
    send = MyTypeSignal()
    slot = MySlot()
    send.sendmsg.connect(slot.get)
    send.sendmsg_multiparam.connect(slot.getMulti)

    # 发送信号
    send.run()
    send.sendMulti()

