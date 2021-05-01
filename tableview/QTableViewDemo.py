from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

'''
QTableViewDemo
'''


class QTableViewDemo(QWidget):
    def __init__(self):
        super(QTableViewDemo, self).__init__()
        self.setWindowTitle('QTableViewDemo')
        self.resize(500, 300)
        self.initUI()

    def initUI(self):
        self.model = QStandardItemModel(4, 3)
        self.model.setHorizontalHeaderLabels(['id', '姓名', '年龄'])
        self.tableView = QTableView()
        # 关联QTableView控件和Model
        self.tableView.setModel(self.model)

        # 添加数据
        item11 = QStandardItem("10")
        item12 = QStandardItem("雷神")
        item13 = QStandardItem("2000")
        self.model.setItem(0, 0, item11)
        self.model.setItem(0, 1, item12)
        self.model.setItem(0, 2, item13)

        item21 = QStandardItem("20")
        item22 = QStandardItem("张三")
        item23 = QStandardItem("3000")
        self.model.setItem(1, 0, item21)
        self.model.setItem(1, 1, item22)
        self.model.setItem(1, 2, item23)

        item31 = QStandardItem("30")
        item32 = QStandardItem("李四")
        item33 = QStandardItem("4000")
        self.model.setItem(2, 0, item31)
        self.model.setItem(2, 1, item32)
        self.model.setItem(2, 2, item33)

        layout = QVBoxLayout()
        layout.addWidget(self.tableView)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QTableViewDemo()
    main.show()
    sys.exit(app.exec_())
