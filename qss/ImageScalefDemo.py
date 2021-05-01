from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

'''
ImageScaleDemo
'''


class ImageScaleDemo(QWidget):
    def __init__(self):
        super(ImageScaleDemo, self).__init__()
        # self.resize(500, 300)
        self.setWindowTitle('ImageScaleDemo')
        self.initUI()

    def initUI(self):
        # self.setFixedSize(800, 600)
        filename = "../images/bg.png"
        label1 = QLabel(self)
        label1.setFixedWidth(200)
        label1.setFixedHeight(200)
        img = QImage(filename)
        # result = img.scaled(label1.width(), label1.height())
        result = img.scaled(
            label1.width(), label1.height(),
            Qt.IgnoreAspectRatio,
            Qt.SmoothTransformation
                            )
        label1.setPixmap(QPixmap.fromImage(result))

        vBox = QVBoxLayout()
        vBox.addWidget(label1)

        self.setLayout(vBox)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = ImageScaleDemo()
    main.show()
    sys.exit(app.exec_())
