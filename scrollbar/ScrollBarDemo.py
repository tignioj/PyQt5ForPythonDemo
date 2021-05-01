from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

'''
ScrollBarDemo
'''


class ScrollBarDemo(QWidget):
    def __init__(self):
        super(ScrollBarDemo, self).__init__()
        self.resize(500, 300)
        self.setWindowTitle('ScrollBarDemo')
        self.initUI()

    def initUI(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = ScrollBarDemo()
    main.show()
    sys.exit(app.exec_())
