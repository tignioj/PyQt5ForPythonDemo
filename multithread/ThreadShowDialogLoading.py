from PyQt5.QtCore import *
import time
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys


class BackendThread(QThread):
    update_report_signal = pyqtSignal()

    def __init__(self):
        super(BackendThread, self).__init__()

    def run(self):
        # faceColor, faceGloss, image = faceDetect(self.inputImage, self.videoFlag)
        time.sleep(5)
        # self.color, self.gloss, self.image = faceDetect(self.inputImage, self.videoFlag)
        self.update_report_signal.emit()


class ThreadShowDialogLoading(QWidget):
    def __init__(self):
        super(ThreadShowDialogLoading, self).__init__()
        self.btn = QPushButton("显示Dialog")
        self.btn.clicked.connect(self.showDialog)
        self.label = QLabel()
        self.label.setText('显示Dialog')

        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.btn)
        self.b = BackendThread()
        self.b.update_report_signal.connect(self.handleUpdate)

        self.setLayout(self.vbox)

    def showDialog(self):
        self.label.setText("loading...")

        self.showloadingGIF(True)
        self.b.start()

    def handleUpdate(self):
        self.label.setText("finished!")
        self.showloadingGIF(False)

    def showloadingGIF(self, isShow=True):
        if isShow:
            self.label1 = QLabel("Hello World")
            self.setFixedSize(800, 600)
            self.movie = QMovie("../images/face_scanning.gif")
            self.movie.setScaledSize(QSize(800, 600))
            self.label1.setMovie(self.movie)
            self.movie.start()
            vBox = QVBoxLayout()
            vBox.addWidget(self.label1)

            self.vbox.addLayout(vBox)
            self.setLayout(vBox)
        else:
            if isShow is not None:
                self.movie.stop()
                pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = ThreadShowDialogLoading()
    main.show()
    sys.exit(app.exec_())
