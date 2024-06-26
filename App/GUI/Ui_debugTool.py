# Form implementation generated from reading ui file 'c:\Users\HEXAOV\Desktop\l2_gui\GUI\debugTool.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_debugTool(object):
    def setupUi(self, debugTool):
        debugTool.setObjectName("debugTool")
        debugTool.resize(210, 470)
        debugTool.setStyleSheet("\n"
"background-color: rgb(50, 50, 50);")
        debugTool.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(parent=debugTool)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 171, 411))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btnTracebackTest = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.btnTracebackTest.setMinimumSize(QtCore.QSize(0, 40))
        self.btnTracebackTest.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.btnTracebackTest.setStyleSheet("\n"
"background-color: rgb(221, 221, 221);")
        self.btnTracebackTest.setObjectName("btnTracebackTest")
        self.verticalLayout.addWidget(self.btnTracebackTest)
        self.btnOpenLogPath = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.btnOpenLogPath.setMinimumSize(QtCore.QSize(0, 40))
        self.btnOpenLogPath.setStyleSheet("\n"
"background-color: rgb(221, 221, 221);")
        self.btnOpenLogPath.setObjectName("btnOpenLogPath")
        self.verticalLayout.addWidget(self.btnOpenLogPath)
        self.btnLoggerDebugMode = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.btnLoggerDebugMode.setEnabled(True)
        self.btnLoggerDebugMode.setMinimumSize(QtCore.QSize(0, 40))
        self.btnLoggerDebugMode.setStyleSheet("\n"
"background-color: rgb(221, 221, 221);")
        self.btnLoggerDebugMode.setObjectName("btnLoggerDebugMode")
        self.verticalLayout.addWidget(self.btnLoggerDebugMode)
        self.btnOpenConsole = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.btnOpenConsole.setEnabled(False)
        self.btnOpenConsole.setMinimumSize(QtCore.QSize(0, 40))
        self.btnOpenConsole.setStyleSheet("\n"
"background-color: rgb(221, 221, 221);")
        self.btnOpenConsole.setObjectName("btnOpenConsole")
        self.verticalLayout.addWidget(self.btnOpenConsole)
        self.btnDumpAllPage = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.btnDumpAllPage.setMinimumSize(QtCore.QSize(0, 40))
        self.btnDumpAllPage.setStyleSheet("\n"
"background-color: rgb(221, 221, 221);")
        self.btnDumpAllPage.setObjectName("btnDumpAllPage")
        self.verticalLayout.addWidget(self.btnDumpAllPage)
        self.btnDumpScoreData = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.btnDumpScoreData.setMinimumSize(QtCore.QSize(0, 40))
        self.btnDumpScoreData.setStyleSheet("\n"
"background-color: rgb(221, 221, 221);")
        self.btnDumpScoreData.setObjectName("btnDumpScoreData")
        self.verticalLayout.addWidget(self.btnDumpScoreData)
        debugTool.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=debugTool)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 210, 22))
        self.menubar.setObjectName("menubar")
        debugTool.setMenuBar(self.menubar)

        self.retranslateUi(debugTool)
        QtCore.QMetaObject.connectSlotsByName(debugTool)

    def retranslateUi(self, debugTool):
        _translate = QtCore.QCoreApplication.translate
        debugTool.setWindowTitle(_translate("debugTool", "DebugTool"))
        self.btnTracebackTest.setText(_translate("debugTool", "報錯測試"))
        self.btnOpenLogPath.setText(_translate("debugTool", "開啟errorLog"))
        self.btnLoggerDebugMode.setText(_translate("debugTool", "切換Log層級(目前：Error)"))
        self.btnOpenConsole.setText(_translate("debugTool", "打開Console"))
        self.btnDumpAllPage.setText(_translate("debugTool", "dumpAllPage(31001)"))
        self.btnDumpScoreData.setText(_translate("debugTool", "dumpScoreData"))
