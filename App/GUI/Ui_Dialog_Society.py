# Form implementation generated from reading ui file 'c:\Users\HEXAOV\Desktop\l2_gui\GUI\Dialog_Society.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Society(object):
    def setupUi(self, Society):
        Society.setObjectName("Society")
        Society.resize(316, 235)
        Society.setStyleSheet("background-color: rgb(255, 252, 235);")
        self.textBrowser = QtWidgets.QTextBrowser(parent=Society)
        self.textBrowser.setGeometry(QtCore.QRect(5, 41, 301, 181))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("font: 700 12pt \"微軟正黑體\";\n"
"background-color: rgb(231, 255, 241);")
        self.textBrowser.setObjectName("textBrowser")

        self.retranslateUi(Society)
        QtCore.QMetaObject.connectSlotsByName(Society)

    def retranslateUi(self, Society):
        _translate = QtCore.QCoreApplication.translate
        Society.setWindowTitle(_translate("Society", "社團紀錄查詢"))
        self.textBrowser.setMarkdown(_translate("Society", "`查詢中...`\n"
"\n"
""))
        self.textBrowser.setHtml(_translate("Society", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'微軟正黑體\'; font-size:12pt; font-weight:700; font-style:normal;\">\n"
"<p style=\" margin-top:8px; margin-bottom:8px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'標楷體\';\">查詢中...</span></p></body></html>"))