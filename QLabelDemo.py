import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QPalette
from PyQt5.QtCore import Qt

'''
QLabel与伙伴控件
'''


class QLabelDemo(QWidget):
    def __init__(self):
        super(QLabelDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QLabel测试')

        label1 = QLabel(self)
        label2 = QLabel(self)
        label3 = QLabel(self)
        label4 = QLabel(self)

        label1.setText("<font style='font-size: 100px;font-weight:bold' color='yellow'>Yellow</font>")
        label1.setAutoFillBackground(True)
        patette = QPalette()
        # 设置背景颜色
        patette.setColor(QPalette.Window, Qt.blue)
        label1.setPalette(patette)
        # 设置对其方式
        label1.setAlignment(Qt.AlignCenter)

        label2.setText("<a href='#'>欢迎使用Python GUI程序</font>")
        # 绑定hover事件
        label2.linkHovered.connect(self.linkHovered)

        label3.setToolTip('这是一个图片标签')
        label3.setPixmap(QPixmap('./images/wsl.ico'))

        label4.setText("<a href='https://localhost:8090/'>本地8090</a>")
        label4.setOpenExternalLinks(True)
        label4.setAlignment(Qt.AlignRight)
        label4.setToolTip('这是一个超链接')
        label4.linkActivated.connect(self.linkClicked)

        vBox = QVBoxLayout()
        vBox.addWidget(label1)
        vBox.addWidget(label2)
        vBox.addWidget(label3)
        vBox.addWidget(label4)

        self.setLayout(vBox)


    def linkHovered(self):
        print('当鼠标划过label2标签时，触发事件')


    def linkClicked(self):
        print('当鼠标单机label4标签时，触发事件')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QLabelDemo()
    mainWindow.show()
    sys.exit(app.exec_())


