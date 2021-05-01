from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
from functools import partial


class OverrideSlotDemo(QMainWindow):
    def __init__(self):
        super(OverrideSlotDemo, self).__init__()
        self.setWindowTitle("覆盖原有的槽函数")

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()
        elif e.key() == Qt.Key_Alt:
            self.setWindowTitle("按下Alt按键")
        else:
            self.setWindowTitle("按下" + str(e.key()) + "按键")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = OverrideSlotDemo()
    main.show()
    sys.exit(app.exec_())
