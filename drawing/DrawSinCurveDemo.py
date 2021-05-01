import math

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

'''
用像素点绘制正弦曲线
-2PI 2PI
'''


class DrawSinCurveDemo(QWidget):
    def __init__(self):
        super(DrawSinCurveDemo, self).__init__()
        self.setWindowTitle('在窗口上绘制正弦曲线')
        self.resize(300, 200)
        self.i = 0

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.begin(self)
        self.i += 1
        print('绘图次数:' + str(self.i))

        painter.setPen(Qt.blue)

        size = self.size()
        for i in range(1000):
            x = 100 * (-1 + 2.0 * i / 1000) + size.width() / 2.0
            y = -50 * math.sin((x - size.width() / 2.0) * math.pi / 50) + size.height() / 2.0
            painter.drawPoint(x, y)
        painter.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = DrawSinCurveDemo()
    main.show()
    sys.exit(app.exec_())
