import os

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
import sys

'''
QWebEngineNativeWebDemo
'''


class QWebEngineNativeWebDemo(QMainWindow):
    def __init__(self):
        super(QWebEngineNativeWebDemo, self).__init__()
        self.resize(500, 300)
        self.setWindowTitle('QWebEngineNativeWebDemo')
        self.initUI()

    def initUI(self):
        self.browser = QWebEngineView()
        url = os.getcwd() + '/web/index.html'
        print(url)
        self.browser.load(QUrl.fromLocalFile(url))
        self.setCentralWidget(self.browser)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QWebEngineNativeWebDemo()
    main.show()
    sys.exit(app.exec_())
