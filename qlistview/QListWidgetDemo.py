from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

'''
QListWidgetDemo
'''


class QListWidgetDemo(QMainWindow):
    def __init__(self):
        super(QListWidgetDemo, self).__init__()
        self.resize(500, 300)
        self.setWindowTitle('QListWidgetDemo')
        self.initUI()

    def initUI(self):
        self.listWidget = QListWidget()
        self.listWidget.resize(300, 120)
        self.listWidget.addItem("item1")
        self.listWidget.addItem("item2")
        self.listWidget.addItem("item3")
        self.listWidget.addItem("item4")
        self.listWidget.addItem("item5")

        self.listWidget.setWindowTitle("demo")

        self.setCentralWidget(self.listWidget)

        self.listWidget.itemClicked.connect(self.clicked)

    def clicked(self, Index):
        QMessageBox.information(
            self,
            "QListWidget",
            "您选择了:" +
            self.listWidget.item(
                self.listWidget.row(Index)
            ).text()
        )


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QListWidgetDemo()
    main.show()
    sys.exit(app.exec_())
