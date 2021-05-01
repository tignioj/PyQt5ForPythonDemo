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
        tableWidget.setHorizontalHeaderLabels(['姓名', '年龄', '籍贯'])

        nameItem = QTableWidgetItem('小明')
        tableWidget.setItem(0, 0, nameItem)

        ageItem = QTableWidgetItem('24')
        tableWidget.setItem(0, 1, ageItem)

        bornItem = QTableWidgetItem('北京')
        tableWidget.setItem(0, 2, bornItem)

        # 禁止编辑
        tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # 整行选择
        tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)

        # 调整列和调整行
        tableWidget.resizeColumnsToContents()
        tableWidget.resizeRowsToContents()

        tableWidget.horizontalHeader().setVisible(False)
        # tableWidget.verticalHeader().setVisible(False)

        # 设置纵向表头
        tableWidget.setVerticalHeaderLabels(["a", "b"])

        # 隐藏表格线
        tableWidget.setShowGrid(False)

        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QTableWidgetDemo()
    main.show()
    sys.exit(app.exec_())
