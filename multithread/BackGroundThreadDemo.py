import cv2
import sys
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QApplication
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import QDir, pyqtSignal, QThread, QSize, QDateTime


# from GUIDesign import *
from camera.face_detect_face_recognition import faceDetect


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
            self.callBackFun = callbackFun
            self.invokeParam = invokeParam
            self.callBackParam = callbackParam
            self.invokeFun = invokeFun

        def run(self):
            """ 线程调用start()之后就会调用这个方法 """

            # 绑定槽函数，也就是回调函数
            self.signal.connect(self.callBackFun)
            try:
                # 调用需要大量计算的函数
                res = self.invokeFun(self.invokeParam)
                print(res)
                # 执行回调函数
                # self.signal.emit({'res': res, 'param': self.callBackParam})
                self.signal.emit({'res': res, 'param': self.callBackParam})
            except Exception as err:
                # 有可能出现异常
                # self.signal.emit({'res': err, 'param': self.callBackParam})
                self.signal.emit({'res': err, 'param': self.callBackParam})

    # 需要执行大量计算的函数
    @staticmethod
    def faceDetectInBackground(paramMap):
        color, gloss, image = faceDetect(paramMap['image'], paramMap['flag'])
        return {'color': color, 'gloss': gloss, 'image': image}

    # 生成报告，有IO操作
    @staticmethod
    def generateReport(paramMap):
        report = paramMap['reportUtils']
        report.wordCreate()
        report.word2pdf()
        return {'report', report}
