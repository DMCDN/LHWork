# Form implementation generated from reading ui file 'c:\Users\HEXAOV\Desktop\l2_gui\GUI\Dialog_LaoZuo_ApplyReserve.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_LaoZuo_ApplyReserve(object):
    def setupUi(self, LaoZuo_ApplyReserve):
        LaoZuo_ApplyReserve.setObjectName("LaoZuo_ApplyReserve")
        LaoZuo_ApplyReserve.resize(966, 639)
        LaoZuo_ApplyReserve.setStyleSheet("background-color: rgb(255, 252, 235);")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=LaoZuo_ApplyReserve)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 30, 901, 471))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.ReserveTable = QtWidgets.QTableWidget(parent=self.verticalLayoutWidget)
        self.ReserveTable.setStyleSheet("font: 700 10pt \"微軟正黑體\";\n"
"background-color: rgb(231, 255, 241);")
        self.ReserveTable.setObjectName("ReserveTable")
        self.ReserveTable.setColumnCount(0)
        self.ReserveTable.setRowCount(0)
        self.ReserveTable.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.ReserveTable)
        self.label_2 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.SuccessTable = QtWidgets.QTableWidget(parent=self.verticalLayoutWidget)
        self.SuccessTable.setStyleSheet("font: 700 10pt \"微軟正黑體\";\n"
"background-color: rgb(231, 255, 241);")
        self.SuccessTable.setObjectName("SuccessTable")
        self.SuccessTable.setColumnCount(0)
        self.SuccessTable.setRowCount(0)
        self.SuccessTable.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.SuccessTable)
        self.btnClearSuccess = QtWidgets.QPushButton(parent=LaoZuo_ApplyReserve)
        self.btnClearSuccess.setGeometry(QtCore.QRect(30, 510, 111, 31))
        self.btnClearSuccess.setObjectName("btnClearSuccess")
        self.progressBar_RemainTime = QtWidgets.QProgressBar(parent=LaoZuo_ApplyReserve)
        self.progressBar_RemainTime.setGeometry(QtCore.QRect(20, 590, 151, 23))
        self.progressBar_RemainTime.setProperty("value", 1)
        self.progressBar_RemainTime.setTextVisible(False)
        self.progressBar_RemainTime.setObjectName("progressBar_RemainTime")
        self.RemainTimeText = QtWidgets.QLabel(parent=LaoZuo_ApplyReserve)
        self.RemainTimeText.setGeometry(QtCore.QRect(20, 570, 201, 16))
        self.RemainTimeText.setObjectName("RemainTimeText")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(parent=LaoZuo_ApplyReserve)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(220, 520, 711, 111))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.RemainTimeText_2 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_2)
        self.RemainTimeText_2.setObjectName("RemainTimeText_2")
        self.verticalLayout_2.addWidget(self.RemainTimeText_2)
        self.textbox_Logger = QtWidgets.QTextBrowser(parent=self.verticalLayoutWidget_2)
        self.textbox_Logger.setObjectName("textbox_Logger")
        self.verticalLayout_2.addWidget(self.textbox_Logger)

        self.retranslateUi(LaoZuo_ApplyReserve)
        QtCore.QMetaObject.connectSlotsByName(LaoZuo_ApplyReserve)

    def retranslateUi(self, LaoZuo_ApplyReserve):
        _translate = QtCore.QCoreApplication.translate
        LaoZuo_ApplyReserve.setWindowTitle(_translate("LaoZuo_ApplyReserve", "[test]LaborMiner"))
        self.label.setText(_translate("LaoZuo_ApplyReserve", "預定列表"))
        self.label_2.setText(_translate("LaoZuo_ApplyReserve", "成功列表"))
        self.btnClearSuccess.setText(_translate("LaoZuo_ApplyReserve", "清除成功列表"))
        self.RemainTimeText.setText(_translate("LaoZuo_ApplyReserve", "下一次嘗試剩餘時間：{time}"))
        self.RemainTimeText_2.setText(_translate("LaoZuo_ApplyReserve", "紀錄"))
