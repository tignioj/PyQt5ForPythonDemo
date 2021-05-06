import threading

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

from utils.LogUtils import LogUtils

'''
QThreadCounterDemo
'''

sec = 0

from PyQt5.QtCore import QThread, pyqtSignal


class BackendThread:
    class InnerThread(QThread):
        """
        匿名内部类线程
        """
        """定义一个信号"""
        signal = pyqtSignal(dict)

        def __init__(self,
                     invokeFun,  # 让线程执行的函数，通常是大量计算的函数
                     callbackFun,  # 回调函数
                     invokeParam={},  # 线程执行函数需要传的参数，需要传入字典
                     callbackParam={}  # 回调函数的参数，需要传入字典
                     ):
            # 一定要调用父类，不然这个线程可能执行不了
            super(BackendThread.InnerThread, self).__init__()
            LogUtils.log("BackendThread", "正在生成UI线程...", self.signal)
            self.callBackFun = callbackFun
            self.invokeParam = invokeParam
            self.callBackParam = callbackParam
            self.invokeFun = invokeFun
            LogUtils.log("BackendThread", "后台线程初始化完毕！", (invokeFun, callbackFun, invokeParam, callbackParam,))

        def run(self):
            """ 线程调用start()之后就会调用这个方法 """
            # 绑定槽函数，也就是回调函数
            LogUtils.log("BackendThread-run", "正在执行run", self.signal)
            self.signal.connect(self.callBackFun)
            try:
                # 调用需要大量计算的函数
                res = self.invokeFun(self.invokeParam)
                # 执行回调函数
                # self.signal.emit({'res': res, 'param': self.callBackParam})
                self.signal.emit({'res': res, 'param': self.callBackParam})
            except Exception as err:
                # 有可能出现异常
                # self.signal.emit({'res': err, 'param': self.callBackParam})
                LogUtils.error("BackendThread-run", "出现异常！", err)
                self.signal.emit({'res': err, 'param': self.callBackParam})

    # 需要执行大量计算的函数
    @staticmethod
    def faceDetectInBackground(paramMap):
        LogUtils.log("BackendThread", "正在进行人脸检测...")
        # detectedFaces = faceDetect(paramMap['image'], 1, paramMap['name'], paramMap['gender'])
        # LogUtils.log("BackendThread", "检测到..." + str(len(detectedFaces)) + "张人脸, 准备生成报告...")
        # reports = ReportService.generateReports(detectedFaces)
        # LogUtils.log("BackendThread", '共生成' + str(len(reports)) + "份报告")
        # return {'reports': reports}

    # 生成报告，有IO操作
    @staticmethod
    def generateReport(paramMap):
        LogUtils.log("BK", "123")
        # report = paramMap['reports']
        # faces = report.faces
        # for face in faces:
        # ReportService.wordCreate(face)
        # report.wordCreate()
        # return {'report', report}

    @staticmethod
    def fakeFunctionForUpdateUI(paramMap):
        pass


class QThreadCounterDemo(QWidget):
    def __init__(self):
        super(QThreadCounterDemo, self).__init__()
        self.setWindowTitle('多线程计时器')
        self.resize(300, 120)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        self.lcdNumber = QLCDNumber()
        layout.addWidget(self.lcdNumber)

        button = QPushButton('开始计数')
        layout.addWidget(button)
        self.sec = 0


        # self.workThread.timer.connect(self.countTime)
        # self.workThread.end.connect(self.end)
        button.clicked.connect(self.work)
        self.setLayout(layout)

    def countTime(self):
        LogUtils.log("BackendThread", "执行了countTime", threading.Thread.name)
        self.sec += 1
        self.lcdNumber.display(self.sec)

    def end(self):
        QMessageBox.information(self, '消息', '计数结束', QMessageBox.Ok)

    def work(self):
        BackendThread.InnerThread(BackendThread.fakeFunctionForUpdateUI, self.countTime).start()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QThreadCounterDemo()
    main.show()
    sys.exit(app.exec_())
