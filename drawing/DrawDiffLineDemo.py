import math

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

'''
用像素点绘制正弦曲线
-2PI 2PI
'''


class DrawDiffLineDemo(QWidget):
    def __init__(self):
        super(DrawDiffLineDemo, self).__init__()
        self.setWindowTitle('在窗口上不同的直线')
        self.resize(300, 300)
        self.i = 0

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.begin(self)
        self.i += 1
        print('绘图次数:' + str(self.i))

        pen = QPen(Qt.red, 3, Qt.SolidLine)
        painter.setPen(pen)
        painter.drawLine(20, 20, 250, 20)

        pen.setStyle(Qt.DashLine)
        painter.setPen(pen)
        painter.drawLine(20, 40, 250, 40)

        pen.setStyle(Qt.DashDotLine)
        painter.setPen(pen)
        painter.drawLine(20, 60, 250, 60)

        pen.setStyle(Qt.DotLine)
        painter.setPen(pen)
        painter.drawLine(20, 80, 250, 80)

        pen.setStyle(Qt.CustomDashLine)
        pen.setDashPattern([1, 3, 5, 7])
        painter.setPen(pen)
        painter.drawLine(20, 100, 250, 100)

        painter.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = DrawDiffLineDemo()
    main.show()
    sys.exit(app.exec_())
