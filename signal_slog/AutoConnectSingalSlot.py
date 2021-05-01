from PyQt5.QtCore import *
from PyQt5 import QtCore
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

'''
自定义信号
pyqtSignal()
'''


class AutoSinglaSlot(QWidget):
    def __init__(self):
        super(AutoSinglaSlot, self).__init__()

        self.okButton = QPushButton('ok', self)
        # 这个名字要和槽函数的on_名字_信号 对应！
        self.okButton.setObjectName("okButton")
        self.cancelButton1 = QPushButton('cancel', self)
        self.cancelButton1.setObjectName("cancelButton")

        layout = QHBoxLayout()
        layout.addWidget(self.okButton)
        layout.addWidget(self.cancelButton1)
        self.setLayout(layout)

        QtCore.QMetaObject.connectSlotsByName(self)

    # 表明这是一个槽函数,
    # 命名一定要规范：on_发送者对象名称_发射信号名称(self, 参数)
    # 其中发送者对象名称是同归setObjectName('名称')确定的
    @QtCore.pyqtSlot()
    def on_okButton_clicked(self):
        print("点击了Ok按钮")

    @QtCore.pyqtSlot()
    def on_cancelButton_clicked(self):
        print("点击了cancelButton按钮")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = AutoSinglaSlot()
    main.show()
    sys.exit(app.exec_())
