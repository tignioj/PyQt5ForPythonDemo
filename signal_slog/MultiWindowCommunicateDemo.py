from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from DateDialog import DateDialog

import sys


class MultiWindowCommunicateDemo(QWidget):
    def __init__(self):
        super(MultiWindowCommunicateDemo, self).__init__()
        self.setWindowTitle("多窗口交互：不适用信号与槽")

        self.lineEdit = QLineEdit(self)

        self.btn1 = QPushButton("弹出对话框1")
        self.btn1.clicked.connect(self.onButton1Click)

        self.btn2 = QPushButton("弹出对话框2")
        self.btn2.clicked.connect(self.onButton2Click)


        gridLayout = QGridLayout()
        gridLayout.addWidget(self.lineEdit)
        gridLayout.addWidget(self.btn1)
        gridLayout.addWidget(self.btn2)

        self.setLayout(gridLayout)

    def onButton1Click(self):
        dialog = DateDialog(self)
        result = dialog.exec()
        date = dialog.dateTime()
        self.lineEdit.setText(date.date().toString())
        dialog.destroy()

    def onButton2Click(self):
        date, time, result = DateDialog.getDateTime()
        self.lineEdit.setText(date.toString())
        if result == QDialog.Accepted:
            print('点击了确定按钮')
        else:
            print('点击取消按钮')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MultiWindowCommunicateDemo()
    main.show()
    sys.exit(app.exec_())
