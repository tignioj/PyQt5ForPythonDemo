from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
# from designer.ReportWidget import  Ui_Form as ReportWidget
from designer.ReportPage import Ui_MainWindow as ReportPage

'''
MultiWindowsDemo3Interaction
'''

class ReportPageDemo(QMainWindow, ReportPage):
    def __init__(self):
        super(ReportPageDemo, self).__init__()
        self.setupUi(self)


class MultiWindowsDemo3Interaction(QMainWindow):
    def __init__(self):
        super(MultiWindowsDemo3Interaction, self).__init__()
        self.resize(500, 300)
        self.setWindowTitle('MultiWindowsDemo3Interaction')
        self.mainFrame = QWidget()
        self.initUI()
        self.reportPage = None

    def initUI(self):
        self.btn = QPushButton(self)
        self.btn.setText("打开窗口")
        self.btn.clicked.connect(self.clicked)

        # 添加Button
        self.btn1 = QPushButton('退出应用程序')
        # 将信号与槽关联
        self.btn1.clicked.connect(self.onClick_Button1)

        layout = QHBoxLayout()
        layout.addWidget(self.btn)
        layout.addWidget(self.btn1)

        self.mainFrame.setLayout(layout)
        self.setCentralWidget(self.mainFrame)

    def onClick_Button1(self):
        self.close()

    def clicked(self):
        if self.reportPage is None:
            self.reportPage = ReportPageDemo()
            self.reportPage.pushButton_back_home.clicked.connect(self.back_home)

        self.reportPage.show()

    def back_home(self):
        self.reportPage.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    m = MultiWindowsDemo3Interaction()
    m.show()
    sys.exit(app.exec_())
