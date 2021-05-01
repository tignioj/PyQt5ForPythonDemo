from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

'''
MyDemo
'''


class MyDemo(QWidget):
    def __init__(self):
        super(MyDemo, self).__init__()
        self.resize(500, 300)
        self.setWindowTitle('MyDemo')
        self.initUI()

    def initUI(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MyDemo()
    main.show()
    sys.exit(app.exec_())
