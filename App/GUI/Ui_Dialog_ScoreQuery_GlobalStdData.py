# Form implementation generated from reading ui file 'c:\Users\HEXAOV\Desktop\ProjectP\l2_gui\GUI\Dialog_ScoreQuery_GlobalStdData.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_ScoreQuery_GlobalStdData(object):
    def setupUi(self, ScoreQuery_GlobalStdData):
        ScoreQuery_GlobalStdData.setObjectName("ScoreQuery_GlobalStdData")
        ScoreQuery_GlobalStdData.resize(985, 652)
        ScoreQuery_GlobalStdData.setStyleSheet("QWidget#ScoreQuery{\n"
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
        self.tableWidget = QtWidgets.QTableWidget(parent=ScoreQuery_GlobalStdData)
        self.tableWidget.setGeometry(QtCore.QRect(20, 50, 951, 581))
        self.tableWidget.setAutoFillBackground(False)
        self.tableWidget.setStyleSheet("font: 700 12pt \"微軟正黑體\";\n"
"background-color: rgb(231, 255, 241);")
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tableWidget.verticalHeader().setVisible(False)
        self.filterText = QtWidgets.QTextEdit(parent=ScoreQuery_GlobalStdData)
        self.filterText.setGeometry(QtCore.QRect(750, 10, 181, 31))
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

        self.retranslateUi(ScoreQuery_GlobalStdData)
        QtCore.QMetaObject.connectSlotsByName(ScoreQuery_GlobalStdData)

    def retranslateUi(self, ScoreQuery_GlobalStdData):
        _translate = QtCore.QCoreApplication.translate
        ScoreQuery_GlobalStdData.setWindowTitle(_translate("ScoreQuery_GlobalStdData", "test40316"))
        self.tableWidget.setSortingEnabled(True)
        self.filterText.setWhatsThis(_translate("ScoreQuery_GlobalStdData", "篩選科目名稱"))
        self.filterText.setPlaceholderText(_translate("ScoreQuery_GlobalStdData", "篩選科目名稱"))
