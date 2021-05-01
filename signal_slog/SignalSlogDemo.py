from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

'''
SignalSlogDemo
'''


class SignalSlogDemo(QWidget):
    def __init__(self):
        super(SignalSlogDemo, self).__init__()
        self.resize(500, 300)
        self.setWindowTitle('SignalSlogDemo')
        self.initUI()

    def initUI(self):
        self.btn = QPushButton('我的按钮', self)
        self.btn.clicked.connect(self.onClick)

    def onClick(self):
        self.btn.setText('信号已经发出！')
        self.btn.setStyleSheet('QPushButton{max-width:200px;min-width:200px}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = SignalSlogDemo()
    main.show()
    sys.exit(app.exec_())
