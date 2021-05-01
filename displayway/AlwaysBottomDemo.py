from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

'''
AlwaysBottomDemo
'''


class AlwaysBottomDemo(QWidget):
    def __init__(self):
        super(AlwaysBottomDemo, self).__init__()
        self.resize(500, 300)
        self.setWindowTitle('AlwaysBottomDemo')
        self.initUI()

    def initUI(self):
        vlayout = QVBoxLayout()
        vlayout.addStretch(0)
        vlayout.addWidget(QPushButton('按钮1'))
        vlayout.addWidget(QPushButton('按钮2'))
        vlayout.addWidget(QPushButton('按钮3'))
        vlayout.addWidget(QPushButton('按钮4'))
        vlayout.addWidget(QPushButton('按钮5'))

        hlayout = QHBoxLayout()
        # 使得后面的按钮总在最右
        hlayout.addStretch(1)
        hlayout.addWidget(QPushButton('确定'))
        hlayout.addWidget(QPushButton('取消'))
        # 关键1:使得后面添加的组件/布局总在最后
        vlayout.addStretch(1)
        # 关键2:添加布局
        vlayout.addLayout(hlayout)
        self.setLayout(vlayout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = AlwaysBottomDemo()
    main.show()
    sys.exit(app.exec_())
