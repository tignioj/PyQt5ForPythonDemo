from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from CommonHelper import CommonHelper
import sys

'''
LoadQssDynamicDemo
'''


class LoadQssDynamicDemo(QMainWindow):
    def __init__(self):
        super(LoadQssDynamicDemo, self).__init__()
        self.resize(500, 300)
        self.setWindowTitle('LoadQssDynamicDemo')
        self.initUI()

    def initUI(self):
        btn = QPushButton()
        btn.setText('加载QSS文件')
        btn.setToolTip('提示文本')
        vBox = QVBoxLayout()
        vBox.addWidget(btn)
        btn.clicked.connect(self.onClick)

        widget = QWidget(self)
        widget.setLayout(vBox)
        self.setCentralWidget(widget)

    def onClick(self):
        styleFile = 'style.qss'
        qssStyle = CommonHelper.readQSS(styleFile)
        self.setStyleSheet(qssStyle)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = LoadQssDynamicDemo()
    win.show()
    sys.exit(app.exec_())
