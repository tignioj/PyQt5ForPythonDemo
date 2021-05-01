from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

'''
QDragWidthDemo
'''


class QDragWidthDemo(QWidget):
    def __init__(self):
        super(QDragWidthDemo, self).__init__()
        self.resize(500, 300)
        self.setWindowTitle('QDragWidthDemo')
        self.initUI()

    def initUI(self):
        hbox = QHBoxLayout(self)

        topLeft = QFrame()
        topLeft.setFrameShape(QFrame.StyledPanel)

        bottom = QFrame()
        bottom.setFrameShape(QFrame.StyledPanel)

        splitter1 = QSplitter(Qt.Horizontal)
        textEdit = QTextEdit()
        splitter1.addWidget(topLeft)
        splitter1.addWidget(textEdit)
        splitter1.setSizes([100, 200])

        splitter2 = QSplitter(Qt.Vertical)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottom)

        hbox.addWidget(splitter2)

        self.setLayout(hbox)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QDragWidthDemo()
    main.show()
    sys.exit(app.exec_())
