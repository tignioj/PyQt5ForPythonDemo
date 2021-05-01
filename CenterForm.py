import sys
from PyQt5.QtWidgets import QDesktopWidget,QMainWindow, QApplication
from PyQt5.QtGui import QIcon


class CenterWin(QMainWindow):
    def __init__(self, parent=None):
        super(CenterWin, self).__init__(parent)

        # 设置主窗口标题
        self.setWindowTitle('第一个主窗口应用')
        self.resize(400, 300)
        self.center()

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        newLeft = (screen.width() - size.width())/2
        newTop = (screen.height() - size.height())/2
        self.move(newLeft, newTop)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('./images/wsl.ico'))
    main = CenterWin()
    main.show()

    sys.exit(app.exec_())

