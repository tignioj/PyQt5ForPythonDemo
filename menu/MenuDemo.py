import math

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

'''
用像素点绘制正弦曲线
-2PI 2PI
'''


class MenuDemo(QMainWindow):
    def __init__(self):
        super(MenuDemo, self).__init__()
        self.setWindowTitle('在窗口上不同的直线')
        self.initUI()

    def initUI(self):
        bar = self.menuBar()
        file = bar.addMenu("文件")
        file.addAction('新建')

        save = QAction('保存', self)
        save.setShortcut("Ctrl + S")
        save.triggered.connect(self.process)
        file.addAction(save)


        edit = bar.addMenu("Edit")
        edit.addAction("copy")
        edit.addAction("paste")
        quit = QAction("退出", self)
        file.addAction(quit)


    def process(self, a):
        print(self.sender().text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MenuDemo()
    main.show()
    sys.exit(app.exec_())
