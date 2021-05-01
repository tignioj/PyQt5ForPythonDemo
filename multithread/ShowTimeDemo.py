from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

'''
ShowTimeDemo
动态显示时间
QTime
QThread
'''


class ShowTimeDemo(QWidget):
    def __init__(self):
        super(ShowTimeDemo, self).__init__()
        self.setWindowTitle('动态显示当前时间')
        self.initUI()
        self.label = QLabel('显示当前时间')
        self.startBtn = QPushButton('开始')
        self.endBtn = QPushButton('结束')
        self.endBtn.setEnabled(False)
        layout = QGridLayout()

        self.timer = QTimer()
        self.timer.timeout.connect(self.showTime)

        layout.addWidget(self.label, 0, 0, 1, 2)
        layout.addWidget(self.startBtn, 1, 0)
        layout.addWidget(self.endBtn, 1, 1)

        self.startBtn.clicked.connect(self.startTimer)
        self.endBtn.clicked.connect(self.endTimer)

        self.setLayout(layout)

    def showTime(self):
        time = QDateTime.currentDateTime()
        timeDisplay = time.toString('yyyy-MM-dd hh:mm:ss dddd')
        self.label.setText(timeDisplay)

    def startTimer(self):
        self.timer.start(1000)
        self.startBtn.setEnabled(False)
        self.endBtn.setEnabled(True)

    def endTimer(self):
        self.timer.stop()
        self.startBtn.setEnabled(True)
        self.endBtn.setEnabled(False)

    def initUI(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = ShowTimeDemo()
    main.show()
    sys.exit(app.exec_())
