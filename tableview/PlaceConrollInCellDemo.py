from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

'''
QTableWidgetDemo
'''


class QTableWidgetDemo(QWidget):
    def __init__(self):
        super(QTableWidgetDemo, self).__init__()
        self.resize(500, 300)
        self.setWindowTitle('QTableWidgetDemo')
        self.initUI()

    def initUI(self):
        layout = QHBoxLayout()
        tableWidget = QTableWidget()
        tableWidget.setRowCount(4)
        tableWidget.setColumnCount(3)

        layout.addWidget(tableWidget)
        tableWidget.setHorizontalHeaderLabels(['姓名', '性别', '体重（kg）'])

        textItem = QTableWidgetItem('小明')
        tableWidget.setItem(0, 0, textItem)

        combox = QComboBox()
        combox.addItem('男')
        combox.addItem('女')
        # QSS
        combox.setStyleSheet('QComboBox{margin:3px}')
        tableWidget.setCellWidget(0, 1, combox)

        modifyButton = QPushButton("修改")
        modifyButton.setDown(True)
        modifyButton.setStyleSheet('QPushButton{margin:3px}')
        tableWidget.setCellWidget(0, 2, modifyButton)

        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QTableWidgetDemo()
    main.show()
    sys.exit(app.exec_())
