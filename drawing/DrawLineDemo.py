from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys


class DrawTextDemo(QWidget):
    def __init__(self):
        super(DrawTextDemo, self).__init__()
        self.setWindowTitle('在窗口上绘制文本')
        self.text = ' Python 从菜鸟到高手 '
        self.resize(300, 200)
        self.i = 0

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.begin(self)
        self.i += 1
        print('绘图次数:' + str(self.i))

        painter.setPen(QColor(150, 43, 5))
        painter.setFont(QFont('SimSun', 25))

        painter.drawText(event.rect(),
                         Qt.AlignCenter,
                         self.text
                         )

        painter.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = DrawTextDemo()
    main.show()
    sys.exit(app.exec_())
