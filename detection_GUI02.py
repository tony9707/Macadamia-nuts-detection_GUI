# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'detection_GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import os
import sys

import time
import cv2
import numpy as np

from PIL import Image
from yolo import YOLO
from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *



class Ui_QMainWindow(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(780, 598)

        self.pushButton_1 = QtWidgets.QPushButton(Form)
        self.pushButton_1.setGeometry(QtCore.QRect(30, 130, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_1.setFont(font)
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 280, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")

        # self.label_0 = QtWidgets.QLabel(Form)
        # self.label_0.setGeometry(QtCore.QRect(210, 90, 511, 421))
        # # self.label_0.setGeometry(QtCore.QRect(200, 200, 420, 420))
        # font = QtGui.QFont()
        # font.setPointSize(16)
        # self.label_0.setFont(font)
        # self.label_0.setIndent(100)
        # self.label_0.setObjectName("label_0")

        self.label_0 = QtWidgets.QLabel(Form)
        self.label_0.setGeometry(QtCore.QRect(210, 90, 511, 421))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_0.setFont(font)
        self.label_0.setStyleSheet('color: yellow')
        self.label_0.setToolTipDuration(-1)
        self.label_0.setLineWidth(1)
        self.label_0.setIndent(100)
        self.label_0.setObjectName("label_0")


        self.label_1 = QtWidgets.QLabel(Form)
        self.label_1.setGeometry(QtCore.QRect(0, 10, 381, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_1.setFont(font)
        self.label_1.setStyleSheet('color: yellow')
        self.label_1.setIndent(16)
        self.label_1.setObjectName("label_1")

        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(350, 520, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet('color: yellow')
        self.label_2.setObjectName("label_2")


        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(190, 510, 551, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setGeometry(QtCore.QRect(180, 80, 20, 441))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")

        self.line_3 = QtWidgets.QFrame(Form)
        self.line_3.setGeometry(QtCore.QRect(190, 70, 551, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")

        self.line_4 = QtWidgets.QFrame(Form)
        self.line_4.setGeometry(QtCore.QRect(730, 80, 20, 441))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")

        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 440, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")


        # window_pale = QtGui.QPalette()
        # window_pale.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap("./background.jpeg")))
        # self.setPalette(window_pale)




# ===============================================

        self.pushButton_1.clicked.connect(self.detec1)

        self.pushButton_2.clicked.connect(self.detec2)

        self.pushButton_3.clicked.connect(self.quxiao)

# ===============================================

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "???????????????????????????????????????GUI"))
        self.pushButton_1.setText(_translate("Form", "????????????"))
        self.pushButton_2.setText(_translate("Form", "????????????"))
        self.pushButton_3.setText(_translate("Form", "????????????"))
        self.label_2.setText(_translate("Form", "??????????????????"))
        self.label_1.setText(_translate("Form", "??????YOLOv3????????????????????????????????????"))
        self.label_0.setText(_translate("Form", "????????????????????????"))



# ===============================================


    # def openimage(self):
    #     the_image_url = QtWidgets.QFileDialog.getOpenFileName(None, 'select image', '', '')
    #
    #     # url = str(the_image_url).split("'")
    #     url = str(the_image_url)
    #
    #
    #     # self.label_0.setText(QtCore.QCoreApplication.translate("MainWindow", "?????????" + url[1]))
    #     # self.label_0.setScaledContents(True)  # ???????????????LABEL??????
    #
    #     img1 = QPixmap(url)
    #
    #     self.label_0.setPixmap(img1)
    #     self.label_0.setScaledContents(True)  # ???????????????LABEL??????


    def detec1(self):
        yolo = YOLO()

        img0, img1 = QtWidgets.QFileDialog.getOpenFileName(None, 'select image', '', '*.jpg')
        # img = str(img0)[:].split(',')

        img = Image.open(img0)

        r_image = yolo.detect_image(img)
        r_image.save('./768/' + str(img0.split('/')[-1])[:-4] + '_gai.jpg')

        # r_image.save('./768/' + str(img.split('/')[-1])[:-4] + '_gai.jpg')
        # r_image.show()

        img2 = QPixmap('./768/' + str(img0.split('/')[-1])[:-4] + '_gai.jpg')
        self.label_0.setPixmap(img2)
        self.label_0.setScaledContents(True)  # ???????????????LABEL??????

    # def detec2(self):
    #     yolo = YOLO()
    #
    #     video_path = 0
    #     capture = cv2.VideoCapture(video_path)
    #     fps = 0.0
    #
    #     while (True):
    #         t1 = time.time()
    #         # ???????????????
    #         ref, frame = capture.read()
    #         if not ref:
    #             break
    #
    #         # ???????????????BGRtoRGB
    #         frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    #         # ?????????Image
    #         frame = Image.fromarray(np.uint8(frame))
    #         # ????????????
    #         frame = np.array(yolo.detect_image(frame))
    #         # RGBtoBGR??????opencv????????????
    #         frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    #
    #         fps = (fps + (1. / (time.time() - t1))) / 2
    #         text0 = print("fps= %.2f" % (fps))
    #
    #         showImage = QtGui.QImage(frame.data, frame.shape[1], frame.shape[0], QtGui.QImage.Format_RGB888)
    #         self.label_0.setPixmap(QtGui.QPixmap.fromImage(showImage))
    #
    #         # self.label_1.setText(str(text0))


    # def detec1(self):
    #     yolo = YOLO()
    #
    #     img = input('Input image filename:')
    #     image = Image.open(img)
    #
    #     r_image = yolo.detect_image(image)
    #     r_image.save('./768/' + str(img.split('/')[-1])[:-4] + '_gai.jpg')
    #     # r_image.show()
    #
    #     img1 = QPixmap('./768/' + str(img.split('/')[-1])[:-4] + '_gai.jpg')
    #
    #     self.label_0.setPixmap(img1)
    #     self.label_0.setScaledContents(True)  # ???????????????LABEL??????

    def detec2(self):
        if __name__ == "__main__":
            yolo = YOLO()

# ----------------------------------------------------------------------------------------------------------#
            video_path = 0
            video_save_path = ""
            video_fps = 25.0

            capture = cv2.VideoCapture(video_path)
            if video_save_path != "":
                fourcc = cv2.VideoWriter_fourcc(*'XVID')
                size = (int(capture.get(cv2.CAP_PROP_FRAME_WIDTH)), int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
                out = cv2.VideoWriter(video_save_path, fourcc, video_fps, size)

            ref, frame = capture.read()
            if not ref:
                raise ValueError("?????????????????????????????????????????????????????????????????????????????????????????????????????????????????????")

            fps = 0.0
            while (True):
                t1 = time.time()
                # ???????????????
                ref, frame = capture.read()
                if not ref:
                    break
                # ???????????????BGRtoRGB
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                # ?????????Image
                frame = Image.fromarray(np.uint8(frame))
                # ????????????
                frame = np.array(yolo.detect_image(frame))
                # RGBtoBGR??????opencv????????????
                frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

                fps = (fps + (1. / (time.time() - t1))) / 2
                print("fps= %.2f" % (fps))

                frame1 = cv2.putText(frame, "fps= %.2f" % (fps), (0, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 256),
                                    2)

                cv2.imshow("video", frame1)

                showImage = QtGui.QImage(frame.data, frame.shape[1], frame.shape[0], QtGui.QImage.Format_BGR888)
                self.label_0.setPixmap(QtGui.QPixmap.fromImage(showImage))
                self.label_0.setScaledContents(True)                        # ???????????????LABEL??????


                c = cv2.waitKey(1) & 0xff
                if video_save_path != "":
                    out.write(frame)
                if c == 27:
                    capture.release()
                    break
                if c == ord('q'):
                    capture.release()
                    break

            print("Video Detection Done!")
            capture.release()
            if video_save_path != "":
                print("Save processed video to the path :" + video_save_path)
                out.release()
            cv2.destroyAllWindows()


    def quxiao(self):
        sys.exit()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)    # ?????????app
    MainWindow = QtWidgets.QMainWindow()      # ???????????????
    ui = Ui_QMainWindow()           # ??????UI??????
    ui.setupUi(MainWindow)          # ?????????UI???????????????????????????????????????ui?????????signal???slot

    MainWindow.setObjectName("MainWindow")
    MainWindow.setStyleSheet("#MainWindow{border-image:url(background.jpeg)}")

    MainWindow.show()               # ????????????
    sys.exit(app.exec_())           # ??????????????????????????????0???????????????sys.exit(0)????????????
