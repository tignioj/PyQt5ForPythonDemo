import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class QColorDialogDemo(QWidget):
    def __init__(self):
        super(QColorDialogDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QColorDialogDemo")
        layout = QVBoxLayout()

        self.btn = QPushButton(self)
        self.btn.setText('选择颜色')
        self.btn.clicked.connect(self.getColor)
        layout.addWidget(self.btn)

        self.colorLabel = QLabel('Hello, 测试颜色')
        layout.addWidget(self.colorLabel)

        self.btn_bg = QPushButton(self)
        self.btn_bg.setText('设置背景颜色')
        self.btn_bg.clicked.connect(self.getBGColor)
        layout.addWidget(self.btn_bg)

        self.setLayout(layout)

    def getBGColor(self):
        color = QColorDialog.getColor()
        p = QPalette()
        p.setColor(QPalette.Window, color)
        self.colorLabel.setAutoFillBackground(True)
        self.colorLabel.setPalette(p)

    def getColor(self):
        color = QColorDialog.getColor()
        p = QPalette()
        p.setColor(QPalette.WindowText, color)
        self.colorLabel.setPalette(p)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QColorDialogDemo()
    main.show()
    sys.exit(app.exec_())
