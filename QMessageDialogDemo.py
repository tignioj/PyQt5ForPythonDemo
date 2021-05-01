import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class QMessageDialogDemo(QWidget):
    def __init__(self):
        super(QMessageDialogDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QMessageDialogDemo")
        self.resize(300, 100)

        layout = QVBoxLayout()
        self.btn = QPushButton(self)
        self.btn.setText('显示关于对话框')
        self.btn.clicked.connect(self.showDialog)
        layout.addWidget(self.btn)

        self.btn_msg = QPushButton(self)
        self.btn_msg.setText('显示消息对话框')
        self.btn_msg.clicked.connect(self.showDialog)
        layout.addWidget(self.btn_msg)

        self.btn_warn = QPushButton(self)
        self.btn_warn.setText('显示警告对话框')
        self.btn_warn.clicked.connect(self.showDialog)
        layout.addWidget(self.btn_warn)

        self.btn_ask = QPushButton(self)
        self.btn_ask.setText('显示提问对话框')
        self.btn_ask.clicked.connect(self.showDialog)
        layout.addWidget(self.btn_ask)

        self.btn_err = QPushButton(self)
        self.btn_err.setText('显示错误对话框')
        self.btn_err.clicked.connect(self.showDialog)
        layout.addWidget(self.btn_err)

        self.setLayout(layout)

    def showDialog(self):
        text = self.sender().text()
        if text == '显示关于对话框':
            dialog = QMessageBox.about(self, '关于', '这是一个关于对话框')
            btn = QPushButton('确定', dialog)
        elif text == '显示消息对话框':
            reply = QMessageBox.information(self, '消息', '这是一个关于对话框',
                                            # 两个选择
                                            QMessageBox.Yes | QMessageBox.No,
                                            # 什么也不选，比如按下回车
                                            QMessageBox.Yes
                                            )
            print(reply == QMessageBox.Yes)
        elif text == '显示警告对话框':
            QMessageBox.warning(self, '警告', '这是一个警告对话框',
                                QMessageBox.Yes | QMessageBox.No,
                                QMessageBox.Yes)
        elif text == '显示提问对话框':
            QMessageBox.question(self, '提问', '这是一个提问对话框',
                                 QMessageBox.Yes | QMessageBox.No,
                                 QMessageBox.Yes)
        elif text == '显示错误对话框':
            QMessageBox.critical(self, '错误', '这是一个错误对话框',
                                 QMessageBox.Yes | QMessageBox.No,
                                 QMessageBox.Yes)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QMessageDialogDemo()
    main.show()
    sys.exit(app.exec_())
