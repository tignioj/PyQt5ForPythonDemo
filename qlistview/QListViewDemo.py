from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

'''
QListViewDemo
'''


class QListViewDemo(QWidget):
    def __init__(self):
        super(QListViewDemo, self).__init__()
        self.resize(500, 300)
        self.setWindowTitle('QListViewDemo')
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        listView = QListView()
        listModel = QStringListModel()
        self.list = ["列表项1", "列表项2", "列表项3"]

        listModel.setStringList(self.list)
        listView.setModel(listModel)
        listView.clicked.connect(self.clicked)

        layout.addWidget(listView)
        self.setLayout(layout)

    def clicked(self, item):
        QMessageBox.information(self, "QListView", "您选择了：" + self.list[item.row()])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QListViewDemo()
    main.show()
    sys.exit(app.exec_())
