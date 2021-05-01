from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

'''

'''


class QTextEditDemo(QWidget):
    def __init__(self):
        super(QTextEditDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QTextEdit')

        self.textEdit = QTextEdit()

        self.btnText = QPushButton('显示文本')
        self.btnText.clicked.connect(self.onClick_ButtonText)

        self.btnHTML = QPushButton('显示HTML')
        self.btnHTML.clicked.connect(self.onClick_ButtonHTML)

        self.btnToText = QPushButton('获取文本')
        self.btnToText.clicked.connect(self.onClick_ButtonToText)

        self.btnToHTML = QPushButton('获取HTML')
        self.btnToHTML.clicked.connect(self.onClick_ButtonToHTML)

        layout = QVBoxLayout()
        layout.addWidget(self.textEdit)
        layout.addWidget(self.btnText)
        layout.addWidget(self.btnHTML)
        layout.addWidget(self.btnToText)
        layout.addWidget(self.btnToHTML)

        self.setLayout(layout)

    def onClick_ButtonText(self):
        self.textEdit.setPlainText('Hello World, 你好世界！')

    def onClick_ButtonToText(self):
        print(self.textEdit.toPlainText())

    def onClick_ButtonHTML(self):
        self.textEdit.setHtml("<font color='blue' size='5'>Hello World HTML!</font>")

    def onClick_ButtonToHTML(self):
        print(self.textEdit.toHtml())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QTextEditDemo()
    mainWindow.show()
    sys.exit(app.exec_())
