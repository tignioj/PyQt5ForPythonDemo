from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
# from designer.ReportWidget import  Ui_Form as ReportWidget
from designer.ReportPage import Ui_MainWindow as ReportPage

'''
MultiWindowsDemo2Interaction
'''

class ReportPageDemo(QMainWindow, ReportPage):
    def __init__(self):
        super(ReportPageDemo, self).__init__()
        self.setupUi(self)


class Controller:
    def __init__(self):
        self.reportPage = None
        self.mainWindow = MultiWindowsDemo2Interaction()
        self.mainWindow.go_to_window.connect(self.show_report_page)

    def show_main(self):
        self.mainWindow.show()

    def show_report_page(self, context):
        if self.reportPage is None:
            self.reportPage = ReportPageDemo()

            self.reportPage.pushButton_back_home.clicked.connect(self.go_main)
            self.reportPage.show()

        else:
            self.reportPage.show()

    def go_main(self):
        self.reportPage.close()
        self.mainWindow.show()


class MultiWindowsDemo2Interaction(QMainWindow):
    go_to_window = pyqtSignal(object)

    def __init__(self):
        super(MultiWindowsDemo2Interaction, self).__init__()
        self.resize(500, 300)
        self.setWindowTitle('MultiWindowsDemo2Interaction')
        self.mainFrame = QWidget()
        self.initUI()

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
        self.go_to_window.emit(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    c = Controller()
    c.show_main()
    sys.exit(app.exec_())
