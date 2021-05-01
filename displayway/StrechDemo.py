from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

'''
StrechDemo
'''


class StrechDemo(QWidget):
    def __init__(self):
        super(StrechDemo, self).__init__()
        self.resize(500, 300)
        self.setWindowTitle('StrechDemo')
        self.initUI()

    def initUI(self):
        hlayout = QHBoxLayout()
        hlayout.addWidget(QPushButton('按钮1'))
        hlayout.addWidget(QPushButton('按钮2'))
        hlayout.addWidget(QPushButton('按钮3'))
        hlayout.addWidget(QPushButton('按钮4'))
        hlayout.addWidget(QPushButton('按钮5'))

        hlayout.addStretch(1)
        hlayout.addWidget(QPushButton('确定'))
        hlayout.addWidget(QPushButton('取消'))
        hlayout.setSpacing(40)
        self.setLayout(hlayout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = StrechDemo()
    main.show()
    sys.exit(app.exec_())
