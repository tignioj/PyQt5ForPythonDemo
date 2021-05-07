import sys
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import *
import PyQt5.QtCore


class PopUpDLG(QDialog):
    def __init__(self):
        super(PopUpDLG, self).__init__()
        self.setObjectName("self")
        self.resize(200, 71)
        self.setMinimumSize(QtCore.QSize(200, 71))
        self.setMaximumSize(QtCore.QSize(200, 71))
        self.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icons/Plus-32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.gridLayout = QGridLayout(self)
        self.gridLayout.setObjectName("gridLayout")
        self.text_link = QLineEdit(self)
        self.text_link.setObjectName("text_link")
        self.gridLayout.addWidget(self.text_link, 0, 0, 1, 2)
        self.add_link = QPushButton(self)
        self.add_link.setObjectName("add_link")
        self.gridLayout.addWidget(self.add_link, 1, 0, 1, 1)
        self.cancel_link = QPushButton(self)
        self.cancel_link.setObjectName("cancel_link")
        self.gridLayout.addWidget(self.cancel_link, 1, 1, 1, 1)
        self.retranslateUi(self)
        self.cancel_link.clicked.connect(self.reject)
        self.add_link.clicked.connect(self.get_link)
        self.retrunVal = None

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Add link"))
        self.add_link.setText(_translate("Dialog", "Add"))
        self.cancel_link.setText(_translate("Dialog", "Cancel"))

    def get_link(self):
        self.retrunVal = self.text_link.text()
        self.accept()

    def exec_(self):
        super(PopUpDLG, self).exec_()
        return self.retrunVal


class MainDialog(QMainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        centralwidget = QWidget(self)
        self.layout = QHBoxLayout(centralwidget)
        self.button = QPushButton("Open")
        self.valText = QLabel("")
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.valText)
        self.setCentralWidget(centralwidget)
        self.button.clicked.connect(self.open_dialog)

    def open_dialog(self):
        dialog = PopUpDLG()
        value = dialog.exec_()
        if value:
            self.valText.setText(value)


def main():
    app = QApplication(sys.argv)
    form = MainDialog()
    form.show()
    app.exec_()


if __name__ == '__main__':
    main()
