from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

'''
SignalForWindowDemo
'''


class SignalForWindowDemo(QWidget):
    button_clicked_signal = pyqtSignal()

    def __init__(self):
        super(SignalForWindowDemo, self).__init__()
        self.resize(500, 300)
        self.setWindowTitle('SignalForWindowDemo')
        self.initUI()

    def initUI(self):
        btn = QPushButton('关闭窗口', self)
        btn.clicked.connect(self.btn_clicked)
        self.button_clicked_signal.connect(self.btn_close)

    def btn_clicked(self):
        self.button_clicked_signal.emit()

    def btn_close(self):
        self.close()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = SignalForWindowDemo()
    main.show()
    sys.exit(app.exec_())
