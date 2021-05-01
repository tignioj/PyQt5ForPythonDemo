from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

'''
LoadGifDemo
'''


class LoadGifDemo(QWidget):
    def __init__(self):
        super(LoadGifDemo, self).__init__()
        # self.resize(500, 300)
        self.setWindowTitle('LoadGifDemo')
        self.initUI()

    def initUI(self):
        self.label = QLabel("", self)
        self.setFixedSize(800, 600)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        # self.movie = QMovie("../images/loading.gif")
        self.movie = QMovie("../images/face_scanning.gif")
        self.movie.setScaledSize(QSize(800, 600))
        self.label.setMovie(self.movie)
        self.movie.start()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = LoadGifDemo()
    main.show()
    sys.exit(app.exec_())
