from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

'''
MultiWindowsDemo
'''


class MultiWindowsDemo(QWidget):
    def __init__(self):
        super(MultiWindowsDemo, self).__init__()
        self.resize(500, 300)
        self.setWindowTitle('MultiWindowsDemo')
        self.initUI()

    def initUI(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MultiWindowsDemo()
    main.show()
    sys.exit(app.exec_())
