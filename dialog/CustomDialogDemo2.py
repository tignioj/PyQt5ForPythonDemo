import sys
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import *
import PyQt5.QtCore

# https://www.programmersought.com/article/36971069089/
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 20:49:32 2019
@author: Tiny
"""
# =============================================================================
from numpy.ma import angle

''' Mouse event, each action response event can be customized '''

''' Reference: 1. https://blog.csdn.net/richenyunqi/article/details/80554257
                          Pyqt determines the mouse click event - left button press, middle button press, right button press, left and right button press, etc.;
         2. https://fennbk.com/8065
                          Pyqt5 mouse (introduction to events and methods)
         3. https://blog.csdn.net/leemboy/article/details/80462632
                          PyQt5 Programming - Mouse Events
         4. https://doc.qt.io/qtforpython/PySide2/QtGui/QWheelEvent.html#PySide2.QtGui.PySide2.QtGui.QWheelEvent.delta
            QWheelEvent'''
# =============================================================================
# =============================================================================
''' PyQt4 and PyQt5 difference: '''
#   PySide2.QtGui.QWheelEvent.delta()
#   Return type:	int
#   This function has been deprecated, use pixelDelta() or angleDelta() instead.
# =============================================================================
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

'''Custom QLabel class'''


class MyQImgLabel(QtWidgets.QLabel):
    def __init__(self, parent=None):
        super(MyQImgLabel, self).__init__(parent)
        f = QFont("ZYSong18030", 10)  # Set the font, font size

        self.setFont(f)  # After the event is not defined, the two sentences are deleted or commented out.

    '''Reload the mouse click event (click) '''

    def mousePressEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:  # left button pressed
            self.pixmap()


class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.imgLabel = MyQImgLabel()  # declare imgLabel
        self.image = QImage()  # declare new img
        if self.image.load("../faces/7.jpeg"):  # if the image is loaded, then
            self.imgLabel.setPixmap(QPixmap.fromImage(self.image.scaled(500, 500)))  # Display image

        self.gridLayout = QtWidgets.QGridLayout(self)  # Layout settings
        self.gridLayout.addWidget(self.imgLabel, 0, 0, 1,
                                  1)  # comment out these two sentences, no image will be displayed


# '''Main function'''
# if __name__ == "__main__":
#     app = QtWidgets.QApplication(sys.argv)
#     myshow = MyWindow()
#     myshow.show()
#     sys.exit(app.exec_())


class PopUpDLG(QDialog):
    def __init__(self, pixMap):
        super(PopUpDLG, self).__init__()
        self.setObjectName("self")
        # self.resize()
        # self.setMinimumSize(QtCore.QSize(400, 400))
        # self.setMaximumSize(QtCore.QSize(1920, 1080))
        self.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.gridLayout = QGridLayout(self)
        self.gridLayout.setObjectName("gridLayout")
        self.labelImg = QLabel("你好")
        self.labelImg.setPixmap(pixMap)
        self.gridLayout.addWidget(self.labelImg, 1, 1, 1, 1)
        self.retranslateUi(self)
        self.retrunVal = None

    def mouseMoveEvent(self, event):
        # srcX = self.label.x()
        # srcY = self.label.y()
        x = event.x()
        y = event.y()
        print(x, y)
        # self.move(x, y)

        # override the key press event

    def keyPressEvent(self, event):

        # get the current co-ordinates of the label
        # X Co-ordinate
        x = self.labelImg.x()

        # Y Co-ordinate
        y = self.labelImg.y()

        # if up arrow key is pressed
        if event.key() == Qt.Key_Up:

            # if top position is attained
            if y > 0:
                self.labelImg.move(x, y - self.speed)

        # if down arrow key is pressed
        elif event.key() == Qt.Key_Down:

            # if bottom position is attained
            # for bottom point, bottom co-ordinate will be
            # height of window - height of label
            if y < self.w_height - self.l_height:
                self.labelImg.move(x, y + self.speed)

        # if left arrow key is pressed
        elif event.key() == Qt.Key_Left:

            # if left end position is attained
            if x > 0:
                self.labelImg.move(x - self.speed, y)

        # if down arrow key is pressed
        elif event.key() == Qt.Key_Right:

            # if right end position is attained
            # for right end point, right co-ordinate will be
            # width of window - width of label
            if x < self.w_width - self.l_width:
                self.labelImg.move(x + self.speed, y)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate

    def setPixMap(self, pixMap):
        self.labelImg.setPixmap(pixMap)

    def exec_(self):
        super(PopUpDLG, self).exec_()
        return self.retrunVal


class MainDialog(QMainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        centralwidget = QWidget(self)
        self.layout = QHBoxLayout(centralwidget)
        self.button = QPushButton("Open")
        self.valText = QLabel("")
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.valText)
        self.setCentralWidget(centralwidget)
        self.button.clicked.connect(self.open_dialog)

    def open_dialog(self):
        qimg = QImage()
        qimg.load("../faces/7.jpeg")
        pixMap = QPixmap.fromImage(qimg.scaled(500, 500))
        dialog = PopUpDLG(pixMap)
        # dialog.setPixMap(pixMap)
        value = dialog.exec_()
        if value:
            self.valText.setText(value)


def main():
    app = QApplication(sys.argv)
    form = MainDialog()
    form.show()
    app.exec_()


if __name__ == '__main__':
    main()
