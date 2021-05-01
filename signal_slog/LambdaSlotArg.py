# 无参数
# fun = lambda: print("hello world")
# fun()
#
# # 带参数
# fun1 = lambda x, y: print(x, y)
# fun1("a,", "b")
#
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys


class LambdaSlotArg(QMainWindow):
    def __init__(self):
        super(LambdaSlotArg, self).__init__()
        self.setWindowTitle("使用Lambda表达式为槽函数传递参数")
        btn1 = QPushButton("按钮1")
        btn2 = QPushButton("按钮2")
        btn1.clicked.connect(lambda: self.onButtonClick(10, 20))
        btn2.clicked.connect(lambda: self.onButtonClick(40, 20))

        layout = QHBoxLayout()
        layout.addWidget(btn1)
        layout.addWidget(btn2)

        mainFrame = QWidget()
        mainFrame.setLayout(layout)

        self.setCentralWidget(mainFrame)

    def onButtonClick(self, m, n):
        print("m+n=" + str(m + n))
        QMessageBox.information(self, "结果", str(m) +
                                "+" + str(n)
                                + "的结果:" + str(m + n))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = LambdaSlotArg()
    main.show()
    sys.exit(app.exec_())
