import math

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

'''
状态栏
'''


class StatusBarDemo(QMainWindow):
    def __init__(self):
        super(StatusBarDemo, self).__init__()
        self.setWindowTitle('状态栏')
        self.initUI()

    def initUI(self):
        bar = self.menuBar()
        file = bar.addMenu("File")
        file.addAction("show")
        file.triggered.connect(self.processTrigger)

        self.setCentralWidget(QTextEdit())
        # 新建状态栏
        self.statusBar = QStatusBar()
        # 设置状态栏
        self.setStatusBar(self.statusBar)


    def processTrigger(self, q):
        if q.text() == "show":
            self.statusBar.showMessage(q.text() + "菜单被点击了", 5000)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = StatusBarDemo()
    main.show()
    sys.exit(app.exec_())
