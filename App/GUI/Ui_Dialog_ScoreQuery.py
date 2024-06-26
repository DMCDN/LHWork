# Form implementation generated from reading ui file 'c:\Users\HEXAOV\Desktop\l2_gui\GUI\Dialog_ScoreQuery.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_ScoreQuery(object):
    def setupUi(self, ScoreQuery):
        ScoreQuery.setObjectName("ScoreQuery")
        ScoreQuery.resize(765, 652)
        ScoreQuery.setStyleSheet("QWidget#ScoreQuery{\n"
"background-color: rgb(255, 252, 235);\n"
"}\n"
"\n"
"    QPushButton{\n"
"        border:0;\n"
"        font: 700 11pt ;\n"
"        border:1px solid #000;\n"
"        background:#fff;\n"
"        border-radius:10px;\n"
"    }\n"
"    QPushButton:hover{\n"
"        border:2px solid #000;\n"
"    \n"
"    background-color: rgb(255, 253, 188);\n"
"    }")
        self.textBrowser = QtWidgets.QTextBrowser(parent=ScoreQuery)
        self.textBrowser.setGeometry(QtCore.QRect(20, 40, 721, 201))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("font: 700 10pt \"微軟正黑體\";\n"
"background-color: rgb(231, 255, 241);")
        self.textBrowser.setObjectName("textBrowser")
        self.tableWidget = QtWidgets.QTableWidget(parent=ScoreQuery)
        self.tableWidget.setGeometry(QtCore.QRect(20, 290, 721, 341))
        self.tableWidget.setAutoFillBackground(False)
        self.tableWidget.setStyleSheet("font: 700 12pt \"微軟正黑體\";\n"
"background-color: rgb(231, 255, 241);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tableWidget.verticalHeader().setVisible(False)
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=ScoreQuery)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 230, 721, 73))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.sz = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.sz.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.sz.setContentsMargins(0, 0, 0, 0)
        self.sz.setObjectName("sz")
        self.btnPointAll = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.btnPointAll.setObjectName("btnPointAll")
        self.sz.addWidget(self.btnPointAll)
        self.btnPoint1 = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.btnPoint1.setObjectName("btnPoint1")
        self.sz.addWidget(self.btnPoint1)
        self.btnPoint2 = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.btnPoint2.setObjectName("btnPoint2")
        self.sz.addWidget(self.btnPoint2)
        self.btnPoint3 = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.btnPoint3.setObjectName("btnPoint3")
        self.sz.addWidget(self.btnPoint3)
        self.btnUnPass = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.btnUnPass.setObjectName("btnUnPass")
        self.sz.addWidget(self.btnUnPass)
        self.filterText = QtWidgets.QTextEdit(parent=ScoreQuery)
        self.filterText.setGeometry(QtCore.QRect(570, 10, 171, 21))
        self.filterText.setStyleSheet("\n"
"        border:0;\n"
"        font: 700 11pt ;\n"
"        border:1px solid #000;\n"
"        background-color: rgb(221, 221, 221);\n"
"        border-radius:10px;\n"
"        td align=\"center\" valign=\"center\";\n"
"        font: 8pt \"微軟正黑體\";")
        self.filterText.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.filterText.setObjectName("filterText")
        self.btnGlobalPassRate = QtWidgets.QPushButton(parent=ScoreQuery)
        self.btnGlobalPassRate.setEnabled(False)
        self.btnGlobalPassRate.setGeometry(QtCore.QRect(420, 10, 131, 24))
        self.btnGlobalPassRate.setObjectName("btnGlobalPassRate")

        self.retranslateUi(ScoreQuery)
        QtCore.QMetaObject.connectSlotsByName(ScoreQuery)

    def retranslateUi(self, ScoreQuery):
        _translate = QtCore.QCoreApplication.translate
        ScoreQuery.setWindowTitle(_translate("ScoreQuery", "應修學分統計"))
        self.textBrowser.setMarkdown(_translate("ScoreQuery", "**應修學分:{Score}/128 學分 **\n"
"\n"
"**校(選擇性)必修、院訂必修:{point1}/36 學分 **\n"
"\n"
"**院、系專業必修:{point2}/68 學分 **\n"
"\n"
"**系專業選修:{point3}/24 學分 **\n"
"\n"
"**通職:{pointS1}/4 通過項目 (已過:{pointS1BlackList})**\n"
"\n"
""))
        self.textBrowser.setHtml(_translate("ScoreQuery", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微軟正黑體\'; font-size:10pt; font-weight:700; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft JhengHei UI\'; font-size:12pt;\">應修學分:{Score}/128 學分 </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Microsoft JhengHei UI\'; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft JhengHei UI\'; font-size:12pt;\">校(選擇性)必修、院訂必修:{point1}/36 學分 </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Microsoft JhengHei UI\'; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft JhengHei UI\'; font-size:12pt;\">院、系專業必修:{point2}/68 學分 </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Microsoft JhengHei UI\'; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft JhengHei UI\'; font-size:12pt;\">系專業選修:{point3}/24 學分 </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Microsoft JhengHei UI\'; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Microsoft JhengHei UI\'; font-size:12pt;\">通職:{pointS1}/4 通過項目 (已過:{pointS1BlackList})</span></p></body></html>"))
        self.btnPointAll.setText(_translate("ScoreQuery", "所有分數"))
        self.btnPoint1.setText(_translate("ScoreQuery", "校(選擇性)必修、院訂必修"))
        self.btnPoint2.setText(_translate("ScoreQuery", "院、系專業必修"))
        self.btnPoint3.setText(_translate("ScoreQuery", "系專業選修"))
        self.btnUnPass.setText(_translate("ScoreQuery", "未通過"))
        self.filterText.setWhatsThis(_translate("ScoreQuery", "篩選科目名稱"))
        self.filterText.setPlaceholderText(_translate("ScoreQuery", "篩選科目名稱"))
        self.btnGlobalPassRate.setText(_translate("ScoreQuery", "正在連結..."))
