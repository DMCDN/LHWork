# Form implementation generated from reading ui file 'c:\Users\HEXAOV\Desktop\l2_gui\GUI\Dialog_LaoZuo.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_LaoZuo(object):
    def setupUi(self, LaoZuo):
        LaoZuo.setObjectName("LaoZuo")
        LaoZuo.resize(401, 352)
        LaoZuo.setStyleSheet("background-color: rgb(255, 252, 235);")
        self.textBrowser = QtWidgets.QTextBrowser(parent=LaoZuo)
        self.textBrowser.setGeometry(QtCore.QRect(10, 50, 381, 281))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("font: 700 12pt \"微軟正黑體\";\n"
"background-color: rgb(231, 255, 241);")
        self.textBrowser.setObjectName("textBrowser")
        self.Label_Status = QtWidgets.QLabel(parent=LaoZuo)
        self.Label_Status.setGeometry(QtCore.QRect(-100, 10, 321, 31))
        self.Label_Status.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Label_Status.setObjectName("Label_Status")
        self.btnLaoZuoApply = QtWidgets.QPushButton(parent=LaoZuo)
        self.btnLaoZuoApply.setGeometry(QtCore.QRect(270, 10, 121, 31))
        self.btnLaoZuoApply.setObjectName("btnLaoZuoApply")
        self.btnThink = QtWidgets.QPushButton(parent=LaoZuo)
        self.btnThink.setGeometry(QtCore.QRect(150, 10, 111, 31))
        self.btnThink.setObjectName("btnThink")

        self.retranslateUi(LaoZuo)
        QtCore.QMetaObject.connectSlotsByName(LaoZuo)

    def retranslateUi(self, LaoZuo):
        _translate = QtCore.QCoreApplication.translate
        LaoZuo.setWindowTitle(_translate("LaoZuo", "勞作教育查詢"))
        self.textBrowser.setMarkdown(_translate("LaoZuo", "`查詢中...`\n"
"\n"
""))
        self.textBrowser.setHtml(_translate("LaoZuo", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微軟正黑體\'; font-size:12pt; font-weight:700; font-style:normal;\">\n"
"<p style=\" margin-top:8px; margin-bottom:8px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'標楷體\';\">查詢中...</span></p></body></html>"))
        self.Label_Status.setText(_translate("LaoZuo", "測試Status"))
        self.btnLaoZuoApply.setText(_translate("LaoZuo", "查詢目前可報名勞作"))
        self.btnThink.setText(_translate("LaoZuo", "[expect]btnThink"))
