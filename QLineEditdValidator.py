from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

'''
校验器
'''


class QLineEditValidatorDemo(QWidget):
    def __init__(self):
        super(QLineEditValidatorDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QLabel与伙伴控件')

        numberLineEdit = QLineEdit(self)
        numberLineEdit.setPlaceholderText("Number only, range: 1-99")
        numberValidator = QIntValidator(self)
        numberValidator.setRange(1, 99)
        numberLineEdit.setValidator(numberValidator)

        doubleLineEdit = QLineEdit(self)
        doubleLineEdit.setPlaceholderText("double number only")
        doubleValidator = QDoubleValidator(self)
        # 设置范围
        doubleValidator.setRange(-360, 360)
        # 标准显示小数点
        doubleValidator.setNotation(QDoubleValidator.StandardNotation)
        # 设置精度:保留小数点后两位
        doubleValidator.setDecimals(2)
        doubleLineEdit.setValidator(doubleValidator)

        regexLineEdit = QLineEdit(self)
        regexLineEdit.setPlaceholderText("regex: Number And Alphabet only")
        regexValidator = QRegExpValidator(self)
        reg = QRegExp('[a-zA-Z0-9]+$')
        regexValidator.setRegExp(reg)
        regexLineEdit.setValidator(regexValidator)

        mainLayout = QFormLayout(self)
        mainLayout.addRow("Int", numberLineEdit)
        mainLayout.addRow("Double", doubleLineEdit)
        mainLayout.addRow("Regex:Number And Alphabet", regexLineEdit)

        self.setLayout(mainLayout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QLineEditValidatorDemo()
    mainWindow.show()
    sys.exit(app.exec_())
