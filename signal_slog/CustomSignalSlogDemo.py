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

    def run(self):
        self.sendmsg.emit('Hello PyQt5')


class MySlot(QObject):
    def get(self, msg):
        print('信息:' + msg)

if __name__ == '__main__':
    send = MyTypeSignal()
    slot = MySlot()
    send.sendmsg.connect(slot.get)

    # 发送信号
    send.run()

    # 取消绑定，则不会再接收到信号
    send.sendmsg.disconnect(slot.get)
    send.run()
