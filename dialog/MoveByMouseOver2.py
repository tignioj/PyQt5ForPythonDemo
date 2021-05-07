# importing libraries
# https://www.geeksforgeeks.org/pyqt5-move-the-label-position-within-the-window-using-arrow-keys/
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

from numpy.ma import angle


class Window(QMainWindow):

    def __init__(self):
        super().__init__()

        # setting title
        self.setWindowTitle("Python ")

        # width of window
        self.w_width = 1800

        # height of window
        self.w_height = 900

        # setting geometry
        self.setGeometry(100, 100, self.w_width, self.w_height)

        # calling method
        self.UiComponents()

        # showing all the widgets
        self.show()

        # speed variable
        self.speed = 45

    def wheelEvent(self, event):
        # if event.delta() > 0: # Roller up, PyQt4
        # This function has been deprecated, use pixelDelta() or angleDelta() instead.
        angle = event.angleDelta() / 8  # Returns the QPoint object, the value of the wheel, in 1/8 degrees
        angleX = angle.x()  # The distance rolled horizontally (not used here)
        angleY = angle.y()  # The distance that is rolled vertically

        self.label.setScaledContents(True)
        w = self.label.width()
        h = self.label.height()

        if angleY > 0:
            w += self.speed
            h += self.speed
            # self.label.setMinimumSize(self.w, self.h)

        else:  # roll down
            w -= self.speed
            h -= self.speed
            # self.label.setMaximumSize(self.w, self.h)

        self.label.setFixedWidth(w)
        self.label.setFixedHeight(h)
        self.label.setPixmap(self.srcPixMap)

    def mousePressEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:
            srcX = self.label.x()
            srcY = self.label.y()
            x = event.x()
            y = event.y()
            self.xd = srcX - x
            self.yd = srcY - y

    def mouseMoveEvent(self, event):
        x = event.x()
        y = event.y()
        print(x, y)
        # if x > 0 and y > 0:
        # x -= self.label.width() / 2
        # y -= self.label.height() / 2
        self.label.move(x + self.xd, y + self.yd)

    # method for components
    def UiComponents(self):
        self.xd = 0
        self.yd = 0

        # creating a label
        self.label = QLabel(self)

        qimg = QImage()
        qimg.load("../faces/7.jpeg")
        pixMap = QPixmap.fromImage(qimg.scaled(500, 500))
        self.label.setPixmap(pixMap)

        self.srcPixMap = self.label.pixmap()
        # label width
        self.l_width = 500

        # label height
        self.l_height = 500

        self.w = self.label.width()
        self.h = self.label.height()

        # setting geometry to the label
        self.label.setGeometry(200, 200, self.l_width, self.l_height)

        # setting stylesheet to the label
        # self.label.setStyleSheet("QLabel"
        #                          "{"
        #                          "border : 4px solid darkgreen;"
        #                          "background : lightgreen;"
        #                          "}")


# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
