# Form implementation generated from reading ui file 'c:\Users\HEXAOV\Desktop\l2_gui\GUI\main.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(459, 427)
        MainWindow.setMouseTracking(False)
        MainWindow.setStyleSheet("")
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setStyleSheet("QWidget#centralwidget{\n"
"background-color: rgb(255, 252, 235);}\n"
"\n"
"\n"
"    QPushButton{\n"
"        border:0;\n"
"        font: 700 12pt ;\n"
"        border:1px solid #000;\n"
"        background:#fff;\n"
"        border-radius:10px;\n"
"    }\n"
"    QPushButton:hover{\n"
"        border:4px solid #000;\n"
"    background-color: rgb(255, 195, 152);\n"
"    }")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(60, 110, 151, 241))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btnScoreQuery = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.btnScoreQuery.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        self.btnScoreQuery.setFont(font)
        self.btnScoreQuery.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.btnScoreQuery.setStyleSheet("")
        self.btnScoreQuery.setObjectName("btnScoreQuery")
        self.verticalLayout.addWidget(self.btnScoreQuery)
        self.line_4 = QtWidgets.QFrame(parent=self.verticalLayoutWidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout.addWidget(self.line_4)
        self.btnCert = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.btnCert.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        self.btnCert.setFont(font)
        self.btnCert.setStyleSheet("")
        self.btnCert.setObjectName("btnCert")
        self.verticalLayout.addWidget(self.btnCert)
        self.line_5 = QtWidgets.QFrame(parent=self.verticalLayoutWidget)
        self.line_5.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_5.setObjectName("line_5")
        self.verticalLayout.addWidget(self.line_5)
        self.btnLaoZuo = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.btnLaoZuo.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        self.btnLaoZuo.setFont(font)
        self.btnLaoZuo.setStyleSheet("")
        self.btnLaoZuo.setObjectName("btnLaoZuo")
        self.verticalLayout.addWidget(self.btnLaoZuo)
        self.line_6 = QtWidgets.QFrame(parent=self.verticalLayoutWidget)
        self.line_6.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_6.setObjectName("line_6")
        self.verticalLayout.addWidget(self.line_6)
        self.btnServiceQuery = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.btnServiceQuery.setEnabled(True)
        self.btnServiceQuery.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        self.btnServiceQuery.setFont(font)
        self.btnServiceQuery.setStyleSheet("")
        self.btnServiceQuery.setObjectName("btnServiceQuery")
        self.verticalLayout.addWidget(self.btnServiceQuery)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(250, 110, 151, 241))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.verticalLayoutWidget_2.setFont(font)
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.btnAbsendWarning = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_2)
        self.btnAbsendWarning.setEnabled(True)
        self.btnAbsendWarning.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        self.btnAbsendWarning.setFont(font)
        self.btnAbsendWarning.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.btnAbsendWarning.setStyleSheet("")
        self.btnAbsendWarning.setObjectName("btnAbsendWarning")
        self.verticalLayout_2.addWidget(self.btnAbsendWarning)
        self.line_3 = QtWidgets.QFrame(parent=self.verticalLayoutWidget_2)
        self.line_3.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_2.addWidget(self.line_3)
        self.btnSpeechEvent = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_2)
        self.btnSpeechEvent.setEnabled(True)
        self.btnSpeechEvent.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        self.btnSpeechEvent.setFont(font)
        self.btnSpeechEvent.setStyleSheet("")
        self.btnSpeechEvent.setObjectName("btnSpeechEvent")
        self.verticalLayout_2.addWidget(self.btnSpeechEvent)
        self.line_7 = QtWidgets.QFrame(parent=self.verticalLayoutWidget_2)
        self.line_7.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_7.setObjectName("line_7")
        self.verticalLayout_2.addWidget(self.line_7)
        self.btnTemp = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_2)
        self.btnTemp.setEnabled(False)
        self.btnTemp.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        self.btnTemp.setFont(font)
        self.btnTemp.setStyleSheet("")
        self.btnTemp.setObjectName("btnTemp")
        self.verticalLayout_2.addWidget(self.btnTemp)
        self.line_8 = QtWidgets.QFrame(parent=self.verticalLayoutWidget_2)
        self.line_8.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_8.setObjectName("line_8")
        self.verticalLayout_2.addWidget(self.line_8)
        self.btnGraduation = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_2)
        self.btnGraduation.setEnabled(True)
        self.btnGraduation.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        self.btnGraduation.setFont(font)
        self.btnGraduation.setStyleSheet("")
        self.btnGraduation.setObjectName("btnGraduation")
        self.verticalLayout_2.addWidget(self.btnGraduation)
        self.label_UserID = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_UserID.setGeometry(QtCore.QRect(60, 50, 341, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        self.label_UserID.setFont(font)
        self.label_UserID.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_UserID.setStyleSheet("color:black;\n"
"text-decoration: underline;\n"
"background-color: rgb(199, 255, 222);\n"
"        border:0;\n"
"\n"
"        border:1px solid #000;\n"
"\n"
"        border-radius:10px;\n"
"")
        self.label_UserID.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_UserID.setObjectName("label_UserID")
        self.btnUpdate = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnUpdate.setGeometry(QtCore.QRect(330, 370, 71, 24))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        self.btnUpdate.setFont(font)
        self.btnUpdate.setStyleSheet("    QPushButton{\n"
"        border:0;\n"
"        font: 700 10pt ;\n"
"        border:1px solid #000;\n"
"        background-color:#fff;\n"
"        border-radius:10px;\n"
"    }\n"
"    QPushButton:hover{\n"
"        border:2px solid #000;\n"
"    background-color: rgb(221, 221, 221);\n"
"    }")
        self.btnUpdate.setObjectName("btnUpdate")
        self.label_Ver = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_Ver.setGeometry(QtCore.QRect(360, 0, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.label_Ver.setFont(font)
        self.label_Ver.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_Ver.setStyleSheet("color: rgb(222, 222, 222);\n"
"color: rgb(167, 167, 167);")
        self.label_Ver.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_Ver.setObjectName("label_Ver")
        self.btnDebugTool = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnDebugTool.setEnabled(True)
        self.btnDebugTool.setGeometry(QtCore.QRect(10, 370, 31, 24))
        self.btnDebugTool.setStyleSheet("\n"
"background-color: rgb(221, 221, 221);")
        self.btnDebugTool.setObjectName("btnDebugTool")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 459, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "GUI"))
        self.btnScoreQuery.setText(_translate("MainWindow", "學分統計"))
        self.btnCert.setText(_translate("MainWindow", "證照查詢"))
        self.btnLaoZuo.setText(_translate("MainWindow", "勞作教育查詢"))
        self.btnServiceQuery.setText(_translate("MainWindow", "服務學習查詢"))
        self.btnAbsendWarning.setText(_translate("MainWindow", "課程預警"))
        self.btnSpeechEvent.setText(_translate("MainWindow", "非正式課程查詢"))
        self.btnTemp.setText(_translate("MainWindow", "[ex]btnTemp"))
        self.btnGraduation.setText(_translate("MainWindow", "畢業門檻狀態總覽"))
        self.label_UserID.setText(_translate("MainWindow", "UserID"))
        self.btnUpdate.setText(_translate("MainWindow", "檢查更新"))
        self.label_Ver.setText(_translate("MainWindow", "1.0.1|10"))
        self.btnDebugTool.setText(_translate("MainWindow", "0"))
