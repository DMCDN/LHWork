# Form implementation generated from reading ui file 'c:\Users\HEXAOV\Desktop\l2_gui\GUI\login.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.resize(377, 304)
        LoginWindow.setTabletTracking(True)
        LoginWindow.setStyleSheet("")
        LoginWindow.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonIconOnly)
        LoginWindow.setTabShape(QtWidgets.QTabWidget.TabShape.Rounded)
        self.centralwidget = QtWidgets.QWidget(parent=LoginWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnLogin = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnLogin.setGeometry(QtCore.QRect(150, 220, 71, 41))
        self.btnLogin.setStyleSheet("\n"
"    QPushButton{\n"
"        border:0;\n"
"        font: 700 12pt \"微軟正黑體\";\n"
"        border:1px solid #000;\n"
"        background:#fff;\n"
"        border-radius:10px;\n"
"    }\n"
"    QPushButton:hover{\n"
"        border:2px solid #000;\n"
"        background:rgb(255, 92, 92);\n"
"    }")
        self.btnLogin.setAutoDefault(True)
        self.btnLogin.setDefault(True)
        self.btnLogin.setObjectName("btnLogin")
        self.checkBox_bAutoLogin = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.checkBox_bAutoLogin.setEnabled(True)
        self.checkBox_bAutoLogin.setGeometry(QtCore.QRect(60, 170, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_bAutoLogin.setFont(font)
        self.checkBox_bAutoLogin.setTabletTracking(False)
        self.checkBox_bAutoLogin.setStyleSheet("")
        self.checkBox_bAutoLogin.setChecked(True)
        self.checkBox_bAutoLogin.setObjectName("checkBox_bAutoLogin")
        self.textEdit_Password = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.textEdit_Password.setGeometry(QtCore.QRect(60, 100, 261, 31))
        self.textEdit_Password.setTabletTracking(True)
        self.textEdit_Password.setStyleSheet("    QLineEdit{\n"
"        border:0;\n"
"        font: 700 11pt \"微軟正黑體\";\n"
"        border:1px solid #000;\n"
"        background:#fff;\n"
"        border-radius:10px;\n"
"        border-color: rgb(227, 227, 227);\n"
"    }\n"
"    QLineEdit:hover{\n"
"        border:1px solid #000;\n"
"\n"
"    }\n"
"")
        self.textEdit_Password.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.textEdit_Password.setObjectName("textEdit_Password")
        self.textEdit_Account = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.textEdit_Account.setGeometry(QtCore.QRect(60, 40, 261, 31))
        self.textEdit_Account.setTabletTracking(True)
        self.textEdit_Account.setStyleSheet("   \n"
" QLineEdit{\n"
"        border:0;\n"
"        font: 700 11pt \"微軟正黑體\";\n"
"        border:1px solid #000;\n"
"        background:#fff;\n"
"        border-radius:12px;\n"
"        \n"
"    border-color: rgb(227, 227, 227);\n"
"    }\n"
"    QLineEdit:hover{\n"
"        border:1px solid #000;\n"
"\n"
"    }\n"
"")
        self.textEdit_Account.setObjectName("textEdit_Account")
        self.btnGuest = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnGuest.setGeometry(QtCore.QRect(240, 170, 81, 21))
        self.btnGuest.setStyleSheet("\n"
"    QPushButton{\n"
"        border:0;\n"
"        font: 700 9pt \"微軟正黑體\";\n"
"        border:1px solid #000;\n"
"        background-color: rgb(220, 220, 220);\n"
"        border-radius:10px;\n"
"    }\n"
"    QPushButton:hover{\n"
"        border:2px solid #000;\n"
"    }")
        self.btnGuest.setAutoDefault(True)
        self.btnGuest.setDefault(True)
        self.btnGuest.setObjectName("btnGuest")
        self.hintText = QtWidgets.QLabel(parent=self.centralwidget)
        self.hintText.setGeometry(QtCore.QRect(140, 10, 101, 20))
        self.hintText.setStyleSheet("color: rgb(134, 134, 134);")
        self.hintText.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.hintText.setObjectName("hintText")
        LoginWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=LoginWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 377, 22))
        self.menubar.setObjectName("menubar")
        LoginWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=LoginWindow)
        self.statusbar.setObjectName("statusbar")
        LoginWindow.setStatusBar(self.statusbar)

        self.retranslateUi(LoginWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)
        LoginWindow.setTabOrder(self.textEdit_Account, self.textEdit_Password)
        LoginWindow.setTabOrder(self.textEdit_Password, self.btnLogin)
        LoginWindow.setTabOrder(self.btnLogin, self.checkBox_bAutoLogin)

    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "登入介面"))
        self.btnLogin.setText(_translate("LoginWindow", "登入"))
        self.checkBox_bAutoLogin.setText(_translate("LoginWindow", "自動登入"))
        self.textEdit_Password.setPlaceholderText(_translate("LoginWindow", "密碼"))
        self.textEdit_Account.setPlaceholderText(_translate("LoginWindow", "學號"))
        self.btnGuest.setText(_translate("LoginWindow", "遊客登入"))
        self.hintText.setText(_translate("LoginWindow", "[ex]"))
