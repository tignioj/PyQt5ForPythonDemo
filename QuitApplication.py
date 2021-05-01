import sys
from PyQt5.QtWidgets import QHBoxLayout, QDesktopWidget, QPushButton, QMainWindow, QApplication, QWidget
from PyQt5.QtGui import QIcon


class QuitApplication(QMainWindow):
    def __init__(self, parent=None):
        super(QuitApplication, self).__init__(parent)

        # 设置主窗口标题
        self.setWindowTitle('推出应用程序')
        self.resize(400, 300)

        # 添加Button
        self.btn1 = QPushButton('退出应用程序')
        # 将信号与槽关联
        self.btn1.clicked.connect(self.onClick_Button1)

        layout = QHBoxLayout()
        layout.addWidget(self.btn1)

        mainFrame = QWidget()
        mainFrame.setLayout(layout)
        self.setCentralWidget(mainFrame)


    # 按钮单击事件的方法 (自定义的槽)
    def onClick_Button1(self):
        sender = self.sender()
        print(sender.text() + '按钮被按下')
        app = QApplication.instance()
        app.quit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('./images/wsl.ico'))
    main = QuitApplication()
    main.show()

    sys.exit(app.exec_())
