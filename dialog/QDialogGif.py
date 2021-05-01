import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class QDialogDemo(QMainWindow):
    def __init__(self):
        super(QDialogDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QDialog Demo")
        self.resize(300, 100)
        layout = QVBoxLayout()

        self.btn = QPushButton(self)
        self.btn.setText('弹出对话框')
        self.btn.clicked.connect(self.showDialog)

        layout.addWidget(self.btn)

        self.setLayout(layout)

    def showDialog(self):
        dialog = QDialog()

        label1 = QLabel("Hello World", dialog)
        # self.setFixedSize(800, 600)
        movie = QMovie("../images/face_scanning.gif")
        movie.setScaledSize(QSize(800, 600))
        label1.setMovie(self.movie)
        movie.start()
        # btn = QPushButton('确定', dialog)
        # btn.clicked.connect(dialog.close)
        # btn.move(50, 50)
        dialog.setWindowTitle("对话框")
        # 设置背景不可点击直到对话框关闭
        dialog.setWindowModality(Qt.ApplicationModal)
        dialog.exec()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QDialogDemo()
    main.show()
    sys.exit(app.exec_())
