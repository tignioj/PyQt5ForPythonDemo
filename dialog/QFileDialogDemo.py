import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class QFileDialogDemo(QWidget):
    def __init__(self):
        super(QFileDialogDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QFileDialogDemo")
        layout = QVBoxLayout()

        self.btn = QPushButton(self)
        self.btn.setText('加载图片')
        self.btn.clicked.connect(self.loadImage)
        layout.addWidget(self.btn)

        # 显示图片
        self.imageLabel = QLabel()
        layout.addWidget(self.imageLabel)

        # 加载文本
        self.btn2 = QPushButton('加载文本文件')
        self.btn2.clicked.connect(self.loadText)
        layout.addWidget(self.btn2)

        # 显示文本
        self.contents = QTextEdit()
        layout.addWidget(self.contents)

        self.setLayout(layout)

    def loadImage(self):
        fname, _ = QFileDialog.getOpenFileName(self, '打开文件',
                                               '.',  # 默认路径
                                               '(*.jpg *.png)',  # 过滤哪些文件
                                               )
        self.imageLabel.setPixmap(QPixmap(fname))

    def loadText(self):
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.AnyFile)
        dialog.setFilter(QDir.Files)

        if dialog.exec():
            filenames = dialog.selectedFiles()
            f = open(filenames[0], encoding='utf-8', mode='r')
            with f:
                data = f.read()
                self.contents.setText(data)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QFileDialogDemo()
    main.show()
    sys.exit(app.exec_())
