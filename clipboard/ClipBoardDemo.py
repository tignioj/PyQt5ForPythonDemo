from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys


class ClipBoardDemo(QWidget):
    def __init__(self, parent=None):
        super(ClipBoardDemo, self).__init__(parent)

        # 设置主窗口标题
        self.setWindowTitle('剪贴版演示')
        self.initUI()

    def initUI(self):
        textCopyBtn = QPushButton('复制文本')
        textPasteButton = QPushButton('粘贴文本')

        htmlCopyButton = QPushButton('复制HTML')
        htmlPasteButton = QPushButton('粘贴HTML')

        imageCopyButton = QPushButton('复制图像')
        imagePasteButton = QPushButton('粘贴图像')

        self.textLabel = QLabel('默认文本')
        self.imageLabel = QLabel()
        self.imageLabel.setPixmap(QPixmap('../images/lufei.png'))

        layout = QGridLayout()
        layout.addWidget(textCopyBtn, 0, 0)
        layout.addWidget(imageCopyButton, 0, 1)
        layout.addWidget(htmlCopyButton, 0, 2)

        layout.addWidget(textPasteButton, 1, 0)
        layout.addWidget(imagePasteButton, 1, 1)
        layout.addWidget(htmlPasteButton, 1, 2)

        layout.addWidget(self.textLabel, 2, 0, 1, 2)
        layout.addWidget(self.imageLabel, 2, 2)

        self.setLayout(layout)

        textCopyBtn.clicked.connect(self.copyText)
        textPasteButton.clicked.connect(self.pasteText)

        htmlCopyButton.clicked.connect(self.copyHtml)
        htmlPasteButton.clicked.connect(self.pasteHtml)

        imageCopyButton.clicked.connect(self.copyImage)
        imagePasteButton.clicked.connect(self.pasteImage)

    def copyText(self):
        clipboard = QApplication.clipboard()
        clipboard.setText('Hello world')

    def pasteText(self):
        clipboard = QApplication.clipboard()
        self.textLabel.setText(clipboard.text())

    def copyHtml(self):
        clipboard = QApplication.clipboard()
        mimeData = QMimeData()
        mimeData.setHtml('<b>Bold and <font color=red>Red</font></b>')
        clipboard.setMimeData(mimeData)

    def pasteHtml(self):
        clipboard = QApplication.clipboard()
        mimeData = clipboard.mimeData()
        if mimeData.hasHtml():
            self.textLabel.setText(mimeData.html())

    def copyImage(self):
        clipboard = QApplication.clipboard()
        clipboard.setPixmap(QPixmap('./images/lufei.png'))

    def pasteImage(self):
        clipboard = QApplication.clipboard()
        self.imageLabel.setPixmap(clipboard.pixmap())
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = ClipBoardDemo()
    main.show()

    sys.exit(app.exec_())
