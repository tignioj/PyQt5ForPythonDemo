import math

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

'''
工具栏:默认只显示图标，文本将作为悬停提示
'''


class ToolBarDemo(QMainWindow):
    def __init__(self):
        super(ToolBarDemo, self).__init__()
        self.setWindowTitle('在窗口上不同的直线')
        self.initUI()

    def initUI(self):
        tb1 = self.addToolBar("File")

        newIcon = QIcon("../images/icons8_file_48px.png")
        newAction = QAction(newIcon, "new", self)

        openIcon = QIcon("../images/icons8_folder_48px.png")
        openAction = QAction(openIcon, "open", self)

        saveIcon = QIcon("../images/icons8_save_48px.png")
        saveAction = QAction(saveIcon, "save", self)

        tb1.addAction(newAction)
        tb1.addAction(openAction)
        tb1.addAction(saveAction)

        # 既显示文本又显示图标
        # tb1.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        # tb1.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        # tb1.setToolButtonStyle(Qt.ToolButtonFollowStyle)
        # tb1.setToolButtonStyle(Qt.ToolButtonTextOnly)
        tb1.setToolButtonStyle(Qt.ToolButtonIconOnly)

        tb2 = self.addToolBar("File1")

        newIcon1 = QIcon("../images/icons8_file_48px.png")
        newAction1 = QAction(newIcon1, "新建", self)
        tb2.addAction(newAction1)
        tb2.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        tb1.actionTriggered.connect(self.toolbtnpressed)

    def toolbtnpressed(self, a):
        print("按下的工具栏按钮是：", a.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = ToolBarDemo()
    main.show()
    sys.exit(app.exec_())
