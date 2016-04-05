# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created: Tue Apr  5 18:30:58 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_SlotcarTimer(object):
    def setupUi(self, SlotcarTimer):
        SlotcarTimer.setObjectName(_fromUtf8("SlotcarTimer"))
        SlotcarTimer.resize(1283, 929)
        SlotcarTimer.setStyleSheet(_fromUtf8("background-color: rgb(65, 65, 65);"))
        self.pushButton = QtGui.QPushButton(SlotcarTimer)
        self.pushButton.setGeometry(QtCore.QRect(1100, 230, 85, 27))
        self.pushButton.setStyleSheet(_fromUtf8("background-color: rgb(255, 141, 1);"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.listWidget = QtGui.QListWidget(SlotcarTimer)
        self.listWidget.setGeometry(QtCore.QRect(120, 110, 411, 271))
        self.listWidget.setStyleSheet(_fromUtf8("background-color: rgb(44, 44, 44);\n"
"font: 75 28pt \"Sawasdee\";\n"
"color: rgb(255, 255, 255);"))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.label_2 = QtGui.QLabel(SlotcarTimer)
        self.label_2.setGeometry(QtCore.QRect(600, 60, 171, 41))
        self.label_2.setStyleSheet(_fromUtf8("font: 63 28pt \"URW Gothic L\";\n"
"color: rgb(255, 141, 1);"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(SlotcarTimer)
        self.label_3.setGeometry(QtCore.QRect(120, 60, 171, 41))
        self.label_3.setStyleSheet(_fromUtf8("font: 63 28pt \"URW Gothic L\";\n"
"color: rgb(255, 141, 1);"))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.graphicsView = PlotWidget(SlotcarTimer)
        self.graphicsView.setGeometry(QtCore.QRect(120, 400, 411, 291))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.lineEdit = QtGui.QLineEdit(SlotcarTimer)
        self.lineEdit.setGeometry(QtCore.QRect(1140, 190, 31, 27))
        self.lineEdit.setStyleSheet(_fromUtf8("background-color: rgb(66, 66, 66);\n"
"color: rgb(255, 255, 255);"))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label = QtGui.QLabel(SlotcarTimer)
        self.label.setGeometry(QtCore.QRect(1100, 200, 31, 17))
        self.label.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.label.setObjectName(_fromUtf8("label"))
        self.progressBar = QtGui.QProgressBar(SlotcarTimer)
        self.progressBar.setGeometry(QtCore.QRect(190, 710, 281, 23))
        self.progressBar.setStyleSheet(_fromUtf8("color: rgb(255, 141, 1);\n"
""))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.label_4 = QtGui.QLabel(SlotcarTimer)
        self.label_4.setGeometry(QtCore.QRect(190, 810, 91, 21))
        self.label_4.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"text-decoration: underline;\n"
"font: 14pt \"Noto Sans [unknown]\";"))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(SlotcarTimer)
        self.label_5.setGeometry(QtCore.QRect(320, 810, 56, 21))
        self.label_5.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"font: 12pt \"Noto Sans [unknown]\";"))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_7 = QtGui.QLabel(SlotcarTimer)
        self.label_7.setGeometry(QtCore.QRect(200, 770, 81, 21))
        self.label_7.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"text-decoration: underline;\n"
"font: 14pt \"Noto Sans [unknown]\";"))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_6 = QtGui.QLabel(SlotcarTimer)
        self.label_6.setGeometry(QtCore.QRect(320, 770, 56, 21))
        self.label_6.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"font: 12pt \"Noto Sans [unknown]\";"))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_8 = QtGui.QLabel(SlotcarTimer)
        self.label_8.setGeometry(QtCore.QRect(320, 850, 56, 21))
        self.label_8.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"font: 12pt \"Noto Sans [unknown]\";"))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(SlotcarTimer)
        self.label_9.setGeometry(QtCore.QRect(160, 850, 121, 21))
        self.label_9.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"text-decoration: underline;\n"
"font: 14pt \"Noto Sans [unknown]\";"))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_10 = QtGui.QLabel(SlotcarTimer)
        self.label_10.setGeometry(QtCore.QRect(120, 890, 171, 21))
        self.label_10.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"text-decoration: underline;\n"
"font: 14pt \"Noto Sans [unknown]\";"))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.label_11 = QtGui.QLabel(SlotcarTimer)
        self.label_11.setGeometry(QtCore.QRect(320, 890, 56, 21))
        self.label_11.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"font: 12pt \"Noto Sans [unknown]\";"))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.graphicsView_2 = PlotWidget(SlotcarTimer)
        self.graphicsView_2.setGeometry(QtCore.QRect(590, 400, 411, 291))
        self.graphicsView_2.setObjectName(_fromUtf8("graphicsView_2"))
        self.progressBar_2 = QtGui.QProgressBar(SlotcarTimer)
        self.progressBar_2.setGeometry(QtCore.QRect(660, 710, 281, 23))
        self.progressBar_2.setStyleSheet(_fromUtf8("color: rgb(255, 141, 1);"))
        self.progressBar_2.setProperty("value", 24)
        self.progressBar_2.setObjectName(_fromUtf8("progressBar_2"))
        self.label_12 = QtGui.QLabel(SlotcarTimer)
        self.label_12.setGeometry(QtCore.QRect(680, 770, 81, 21))
        self.label_12.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"text-decoration: underline;\n"
"font: 14pt \"Noto Sans [unknown]\";"))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.label_13 = QtGui.QLabel(SlotcarTimer)
        self.label_13.setGeometry(QtCore.QRect(800, 850, 56, 21))
        self.label_13.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"font: 12pt \"Noto Sans [unknown]\";"))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.label_14 = QtGui.QLabel(SlotcarTimer)
        self.label_14.setGeometry(QtCore.QRect(800, 810, 56, 21))
        self.label_14.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"font: 12pt \"Noto Sans [unknown]\";"))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.label_15 = QtGui.QLabel(SlotcarTimer)
        self.label_15.setGeometry(QtCore.QRect(640, 850, 121, 21))
        self.label_15.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"text-decoration: underline;\n"
"font: 14pt \"Noto Sans [unknown]\";"))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.label_16 = QtGui.QLabel(SlotcarTimer)
        self.label_16.setGeometry(QtCore.QRect(600, 890, 171, 21))
        self.label_16.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"text-decoration: underline;\n"
"font: 14pt \"Noto Sans [unknown]\";"))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.label_17 = QtGui.QLabel(SlotcarTimer)
        self.label_17.setGeometry(QtCore.QRect(670, 810, 91, 21))
        self.label_17.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"text-decoration: underline;\n"
"font: 14pt \"Noto Sans [unknown]\";"))
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.label_18 = QtGui.QLabel(SlotcarTimer)
        self.label_18.setGeometry(QtCore.QRect(800, 770, 56, 21))
        self.label_18.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"font: 12pt \"Noto Sans [unknown]\";"))
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.label_19 = QtGui.QLabel(SlotcarTimer)
        self.label_19.setGeometry(QtCore.QRect(800, 890, 56, 21))
        self.label_19.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"font: 12pt \"Noto Sans [unknown]\";"))
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.listWidget_2 = QtGui.QListWidget(SlotcarTimer)
        self.listWidget_2.setGeometry(QtCore.QRect(590, 110, 411, 271))
        self.listWidget_2.setStyleSheet(_fromUtf8("background-color: rgb(44, 44, 44);\n"
"font: 75 28pt \"Sawasdee\";\n"
"color: rgb(255, 255, 255);"))
        self.listWidget_2.setObjectName(_fromUtf8("listWidget_2"))
        self.label_20 = QtGui.QLabel(SlotcarTimer)
        self.label_20.setGeometry(QtCore.QRect(410, 780, 51, 21))
        self.label_20.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"text-decoration: underline;\n"
"font: 14pt \"Noto Sans [unknown]\";"))
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.label_21 = QtGui.QLabel(SlotcarTimer)
        self.label_21.setGeometry(QtCore.QRect(890, 790, 51, 21))
        self.label_21.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"text-decoration: underline;\n"
"font: 14pt \"Noto Sans [unknown]\";"))
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.label_22 = QtGui.QLabel(SlotcarTimer)
        self.label_22.setGeometry(QtCore.QRect(470, 820, 56, 21))
        self.label_22.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"font: 12pt \"Noto Sans [unknown]\";"))
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.label_23 = QtGui.QLabel(SlotcarTimer)
        self.label_23.setGeometry(QtCore.QRect(950, 820, 56, 21))
        self.label_23.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"font: 12pt \"Noto Sans [unknown]\";"))
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.pushButton_2 = QtGui.QPushButton(SlotcarTimer)
        self.pushButton_2.setGeometry(QtCore.QRect(1100, 350, 85, 27))
        self.pushButton_2.setStyleSheet(_fromUtf8("background-color: rgb(255, 141, 1);"))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.label_24 = QtGui.QLabel(SlotcarTimer)
        self.label_24.setGeometry(QtCore.QRect(950, 20, 301, 71))
        self.label_24.setStyleSheet(_fromUtf8("font: 48pt \"Imagination Station\";\n"
"color: rgb(255, 141, 1);"))
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.label_25 = QtGui.QLabel(SlotcarTimer)
        self.label_25.setGeometry(QtCore.QRect(1080, 100, 181, 21))
        self.label_25.setStyleSheet(_fromUtf8("font: 10pt \"Noto Sans [unknown]\";\n"
"color: rgb(255, 141, 1);"))
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.checkBox = QtGui.QCheckBox(SlotcarTimer)
        self.checkBox.setGeometry(QtCore.QRect(1100, 270, 151, 22))
        self.checkBox.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.label_26 = QtGui.QLabel(SlotcarTimer)
        self.label_26.setGeometry(QtCore.QRect(410, 820, 51, 21))
        self.label_26.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"text-decoration: underline;\n"
"font: 10pt \"Noto Sans [unknown]\";"))
        self.label_26.setObjectName(_fromUtf8("label_26"))
        self.label_27 = QtGui.QLabel(SlotcarTimer)
        self.label_27.setGeometry(QtCore.QRect(410, 850, 51, 21))
        self.label_27.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"text-decoration: underline;\n"
"font: 10pt \"Noto Sans [unknown]\";"))
        self.label_27.setObjectName(_fromUtf8("label_27"))
        self.label_28 = QtGui.QLabel(SlotcarTimer)
        self.label_28.setGeometry(QtCore.QRect(470, 850, 56, 21))
        self.label_28.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"font: 12pt \"Noto Sans [unknown]\";"))
        self.label_28.setObjectName(_fromUtf8("label_28"))
        self.label_29 = QtGui.QLabel(SlotcarTimer)
        self.label_29.setGeometry(QtCore.QRect(410, 880, 51, 21))
        self.label_29.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"text-decoration: underline;\n"
"font: 10pt \"Noto Sans [unknown]\";"))
        self.label_29.setObjectName(_fromUtf8("label_29"))
        self.label_30 = QtGui.QLabel(SlotcarTimer)
        self.label_30.setGeometry(QtCore.QRect(470, 880, 56, 21))
        self.label_30.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"font: 12pt \"Noto Sans [unknown]\";"))
        self.label_30.setObjectName(_fromUtf8("label_30"))
        self.label_31 = QtGui.QLabel(SlotcarTimer)
        self.label_31.setGeometry(QtCore.QRect(950, 880, 56, 21))
        self.label_31.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"font: 12pt \"Noto Sans [unknown]\";"))
        self.label_31.setObjectName(_fromUtf8("label_31"))
        self.label_32 = QtGui.QLabel(SlotcarTimer)
        self.label_32.setGeometry(QtCore.QRect(950, 850, 56, 21))
        self.label_32.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"font: 12pt \"Noto Sans [unknown]\";"))
        self.label_32.setObjectName(_fromUtf8("label_32"))
        self.label_33 = QtGui.QLabel(SlotcarTimer)
        self.label_33.setGeometry(QtCore.QRect(890, 850, 51, 21))
        self.label_33.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"text-decoration: underline;\n"
"font: 10pt \"Noto Sans [unknown]\";"))
        self.label_33.setObjectName(_fromUtf8("label_33"))
        self.label_34 = QtGui.QLabel(SlotcarTimer)
        self.label_34.setGeometry(QtCore.QRect(890, 880, 51, 21))
        self.label_34.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"text-decoration: underline;\n"
"font: 10pt \"Noto Sans [unknown]\";"))
        self.label_34.setObjectName(_fromUtf8("label_34"))
        self.label_35 = QtGui.QLabel(SlotcarTimer)
        self.label_35.setGeometry(QtCore.QRect(890, 820, 51, 21))
        self.label_35.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"text-decoration: underline;\n"
"font: 10pt \"Noto Sans [unknown]\";"))
        self.label_35.setObjectName(_fromUtf8("label_35"))
        self.label_36 = QtGui.QLabel(SlotcarTimer)
        self.label_36.setGeometry(QtCore.QRect(1100, 300, 71, 17))
        self.label_36.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.label_36.setObjectName(_fromUtf8("label_36"))
        self.label_37 = QtGui.QLabel(SlotcarTimer)
        self.label_37.setGeometry(QtCore.QRect(1100, 320, 71, 17))
        self.label_37.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.label_37.setObjectName(_fromUtf8("label_37"))
        self.label_38 = QtGui.QLabel(SlotcarTimer)
        self.label_38.setGeometry(QtCore.QRect(60, 810, 111, 21))
        self.label_38.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"font: 12pt \"Noto Sans [unknown]\";"))
        self.label_38.setObjectName(_fromUtf8("label_38"))
        self.label_39 = QtGui.QLabel(SlotcarTimer)
        self.label_39.setGeometry(QtCore.QRect(560, 810, 91, 21))
        self.label_39.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"font: 12pt \"Noto Sans [unknown]\";"))
        self.label_39.setObjectName(_fromUtf8("label_39"))

        self.retranslateUi(SlotcarTimer)
        QtCore.QMetaObject.connectSlotsByName(SlotcarTimer)

    def retranslateUi(self, SlotcarTimer):
        SlotcarTimer.setWindowTitle(_translate("SlotcarTimer", "Dialog", None))
        self.pushButton.setText(_translate("SlotcarTimer", "Start!", None))
        self.label_2.setText(_translate("SlotcarTimer", "Player 2:", None))
        self.label_3.setText(_translate("SlotcarTimer", "Player 1:", None))
        self.lineEdit.setText(_translate("SlotcarTimer", "10", None))
        self.label.setText(_translate("SlotcarTimer", "Laps:", None))
        self.label_4.setText(_translate("SlotcarTimer", "Best Lap:", None))
        self.label_5.setText(_translate("SlotcarTimer", "X.XXX", None))
        self.label_7.setText(_translate("SlotcarTimer", "Average:", None))
        self.label_6.setText(_translate("SlotcarTimer", "X.XXX", None))
        self.label_8.setText(_translate("SlotcarTimer", "X.XXX", None))
        self.label_9.setText(_translate("SlotcarTimer", "Average of 5:", None))
        self.label_10.setText(_translate("SlotcarTimer", "Best Average of 5:", None))
        self.label_11.setText(_translate("SlotcarTimer", "X.XXX", None))
        self.label_12.setText(_translate("SlotcarTimer", "Average:", None))
        self.label_13.setText(_translate("SlotcarTimer", "X.XXX", None))
        self.label_14.setText(_translate("SlotcarTimer", "X.XXX", None))
        self.label_15.setText(_translate("SlotcarTimer", "Average of 5:", None))
        self.label_16.setText(_translate("SlotcarTimer", "Best Average of 5:", None))
        self.label_17.setText(_translate("SlotcarTimer", "Best Lap:", None))
        self.label_18.setText(_translate("SlotcarTimer", "X.XXX", None))
        self.label_19.setText(_translate("SlotcarTimer", "X.XXX", None))
        self.label_20.setText(_translate("SlotcarTimer", "Total:", None))
        self.label_21.setText(_translate("SlotcarTimer", "Total:", None))
        self.label_22.setText(_translate("SlotcarTimer", "X.XXX", None))
        self.label_23.setText(_translate("SlotcarTimer", "X.XXX", None))
        self.pushButton_2.setText(_translate("SlotcarTimer", "Continue", None))
        self.label_24.setText(_translate("SlotcarTimer", "SlotFighter", None))
        self.label_25.setText(_translate("SlotcarTimer", "recommended by IkerPaco", None))
        self.checkBox.setText(_translate("SlotcarTimer", "track swap race", None))
        self.label_26.setText(_translate("SlotcarTimer", "Track 1:", None))
        self.label_27.setText(_translate("SlotcarTimer", "Track 2:", None))
        self.label_28.setText(_translate("SlotcarTimer", "X.XXX", None))
        self.label_29.setText(_translate("SlotcarTimer", "Sum:", None))
        self.label_30.setText(_translate("SlotcarTimer", "X.XXX", None))
        self.label_31.setText(_translate("SlotcarTimer", "X.XXX", None))
        self.label_32.setText(_translate("SlotcarTimer", "X.XXX", None))
        self.label_33.setText(_translate("SlotcarTimer", "Track 2:", None))
        self.label_34.setText(_translate("SlotcarTimer", "Sum:", None))
        self.label_35.setText(_translate("SlotcarTimer", "Track 1:", None))
        self.label_36.setText(_translate("SlotcarTimer", "Track 1: P1", None))
        self.label_37.setText(_translate("SlotcarTimer", "Track 2: P2", None))
        self.label_38.setText(_translate("SlotcarTimer", "X.XXX", None))
        self.label_39.setText(_translate("SlotcarTimer", "X.XXX", None))

from pyqtgraph import PlotWidget
