from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

'''
AddButtonImage
'''


class AddButtonImage(QWidget):
    def __init__(self):
        super(AddButtonImage, self).__init__()
        # self.resize(500, 300)
        self.setWindowTitle('AddButtonImage')
        self.initUI()

    def initUI(self):
        label = QLabel(self)
        label.setToolTip('这是一个文本标签')
        label.setStyleSheet('QLabel{border-image:url(../images/bg.png)}')

        label.setFixedWidth(800)
        label.setFixedHeight(600)

        btn1 = QPushButton(self)
        btn1.setObjectName('btn1')

        btn1.setMaximumSize(48, 48)
        btn1.setMinimumSize(48, 48)

        style = '''
            #btn1{
                border-radius: 4px;
                background-image:url('../images/icons8_add_48px_1.png')
            }
            #btn1:Pressed{
                background-image:url('../images/add_hover.png');
            }
        '''
        btn1.setStyleSheet(style)
        vBox = QVBoxLayout()
        vBox.addWidget(label)
        vBox.addWidget(btn1)

        self.setLayout(vBox)
        self.setWindowTitle("使用QSS为标签添加按钮和背景图")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = AddButtonImage()
    main.show()
    sys.exit(app.exec_())
