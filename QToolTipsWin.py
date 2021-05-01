import sys
from PyQt5.QtWidgets import QApplication, QToolTip, QWidget, QPushButton, QHBoxLayout
from PyQt5.QtGui import QIcon, QFont


class QToolTipsWin(QWidget):
    def __init__(self, parent=None):
        super(QToolTipsWin, self).__init__(parent)

        # 设置主窗口标题
        self.setWindowTitle('第一个主窗口应用')
        QToolTip.setFont(QFont('SansSerif', 12))
        self.setToolTip('今天是<b>星期五<b/>')
        self.setGeometry(300, 300, 200, 300)
        # 添加Button
        self.btn1 = QPushButton('按钮1')
        self.btn1.setToolTip('这是<b>按钮1</b>哦~')
        # 将信号与槽关联
        self.btn1.clicked.connect(self.onClick_Button1)

        layout = QHBoxLayout()
        layout.addWidget(self.btn1)

        self.setLayout(layout)

    # 按钮单击事件的方法 (自定义的槽)
    def onClick_Button1(self):
        sender = self.sender()
        print(sender.text() + '按钮被按下')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('./images/wsl.ico'))
    main = QToolTipsWin()
    main.show()

    sys.exit(app.exec_())
