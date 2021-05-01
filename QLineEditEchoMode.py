from PyQt5.QtWidgets import *
import sys

'''
输出模式
'''


class QLineEditEchoMode(QWidget):
    def __init__(self):
        super(QLineEditEchoMode, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QLabel与伙伴控件')

        normalLineEdit = QLineEdit(self)
        normalLineEdit.setPlaceholderText("Normal")
        normalLineEdit.setEchoMode(QLineEdit.Normal)

        noEchoLineEdit = QLineEdit(self)
        noEchoLineEdit.setPlaceholderText("noEchoLine")
        noEchoLineEdit.setEchoMode(QLineEdit.NoEcho)

        passwordLineEdit = QLineEdit(self)
        passwordLineEdit.setPlaceholderText("PasswordLine")
        passwordLineEdit.setEchoMode(QLineEdit.Password)

        passwordEchoOnEditLineEdit = QLineEdit(self)
        passwordEchoOnEditLineEdit.setPlaceholderText("PasswordEchoOnEdit")
        passwordEchoOnEditLineEdit.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        mainLayout = QFormLayout(self)
        mainLayout.addRow("Normal", normalLineEdit)
        mainLayout.addRow("NoEchoLineEdit", noEchoLineEdit)
        mainLayout.addRow("PasswordLineEdit", passwordLineEdit)
        mainLayout.addRow("PasswordEchoOnEditLineEdit", passwordEchoOnEditLineEdit)
        
        

        self.setLayout(mainLayout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QLineEditEchoMode()
    mainWindow.show()
    sys.exit(app.exec_())
