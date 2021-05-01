import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class QPushButtonDemo1(QDialog):
    def __init__(self):
        super(QPushButtonDemo1, self).__init__()
        self.initUI()


    def initUI(self):
        self.setWindowTitle("QPushButton Demo")
        layout = QVBoxLayout()

        self.btn1 = QPushButton('第一个按钮')
        self.btn1.setText('FirstButton')
        self.btn1.setChecked(True)
        self.btn1.toggle()
        self.btn1.clicked.connect(self.whichButton)
        layout.addWidget(self.btn1)
        self.setLayout(layout)

    def whichButton(self, btn):
        sender = self.sender()
        print('被单机的按钮是<' + sender.text() + '>')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QPushButtonDemo1()
    main.show()
    sys.exit(app.exec_())
