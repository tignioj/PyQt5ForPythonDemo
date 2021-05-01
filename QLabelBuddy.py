from PyQt5.QtWidgets import *
import sys

'''
QLabel与伙伴控件
'''


class QLabelBuddy(QDialog):
    def __init__(self):
        super(QLabelBuddy, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QLabel与伙伴控件')

        nameLabel = QLabel('&Name', self)
        nameLineEdit = QLineEdit(self)
        # 设置伙伴控件
        nameLabel.setBuddy(nameLineEdit)

        pwdLabel = QLabel('&Edit', self)
        pwdLineEdit = QLineEdit(self)
        # 设置伙伴控件
        pwdLabel.setBuddy(pwdLineEdit)

        btnOk = QPushButton('&Ok')
        btnCancel = QPushButton('&Cancel')
        mainLayout = QGridLayout(self)
        # 第一行
        mainLayout.addWidget(nameLabel, 0, 0)
        mainLayout.addWidget(nameLineEdit, 0, 1, 1, 2)

        # 第二行
        mainLayout.addWidget(pwdLabel, 1, 0)
        mainLayout.addWidget(pwdLineEdit, 1, 1, 1, 2)

        # d第三行
        mainLayout.addWidget(btnOk, 2, 1)
        mainLayout.addWidget(btnCancel, 2, 2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QLabelBuddy()
    mainWindow.show()
    sys.exit(app.exec_())