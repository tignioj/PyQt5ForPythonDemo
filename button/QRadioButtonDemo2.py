import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


# https://pythonbasics.org/pyqt-radiobutton/
class QRadioButtonDemo1(QDialog):
    def __init__(self):
        super(QRadioButtonDemo1, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QRadioButton Demo")
        layout = QHBoxLayout()
        self.btn1 = QRadioButton('单选按钮1')
        self.btn1.country = 'China'
        self.btn1.toggled.connect(self.buttonState)
        self.btn1.setChecked(True)

        self.btn2 = QRadioButton('单选按钮2')
        self.btn2.toggled.connect(self.buttonState)
        self.btn2.country = 'USA'

        layout.addWidget(self.btn1)
        layout.addWidget(self.btn2)
        self.setLayout(layout)

    def buttonState(self):
        radioButton = self.sender()
        if radioButton.isChecked():
            print("Country is %s" % (radioButton.country))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QRadioButtonDemo1()
    main.show()
    sys.exit(app.exec_())
