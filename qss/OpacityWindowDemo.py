from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

'''
OpacityWindowDemo
'''


class OpacityWindowDemo(QWidget):
    def __init__(self):
        super(OpacityWindowDemo, self).__init__()
        self.resize(500, 300)
        self.setWindowTitle('OpacityWindowDemo')
        self.initUI()

    def initUI(self):
        self.setWindowOpacity(0.8)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = OpacityWindowDemo()
    main.show()
    sys.exit(app.exec_())
