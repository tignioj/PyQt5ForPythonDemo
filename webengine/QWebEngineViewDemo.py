from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
import sys

'''
QWebEngineDemo
'''


class QWebEngineDemo(QMainWindow):
    def __init__(self):
        super(QWebEngineDemo, self).__init__()
        self.resize(500, 300)
        self.setWindowTitle('QWebEngineDemo')
        self.initUI()

    def initUI(self):
        self.browser = QWebEngineView()
        self.browser.load(QUrl('https://www.baidu.com'))
        self.setCentralWidget(self.browser)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QWebEngineDemo()
    main.show()
    sys.exit(app.exec_())
