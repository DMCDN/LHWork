# Form implementation generated from reading ui file 'c:\Users\HEXAOV\Desktop\l2_gui\GUI\Graduation.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Graduation(object):
    def setupUi(self, Graduation):
        Graduation.setObjectName("Graduation")
        Graduation.resize(410, 407)
        Graduation.setStyleSheet("QWidget#centralwidget{\n"
"background-color: rgb(255, 252, 235);}\n"
"")
        Graduation.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(parent=Graduation)
        self.centralwidget.setStyleSheet("QWidget#centralwidget{\n"
"background-color: rgb(255, 252, 235);}\n"
"\n"
"\n"
"    QPushButton{\n"
"    background-color: #fff;\n"
"    border: 1px solid  rgb(180, 180, 180);\n"
"font: 14pt \"微軟正黑體\";\n"
"    padding: 2px;\n"
"    }\n"
"    QPushButton:hover{\n"
"        border:4px solid #000;\n"
"    background-color: rgb(255, 195, 152);\n"
"    }\n"
" QToolTip {\n"
"                font-size: 16px;\n"
"                color: black;\n"
"            }")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(50, 30, 311, 331))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.ScoreQueryText = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(225)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ScoreQueryText.sizePolicy().hasHeightForWidth())
        self.ScoreQueryText.setSizePolicy(sizePolicy)
        self.ScoreQueryText.setMinimumSize(QtCore.QSize(0, 0))
        self.ScoreQueryText.setMaximumSize(QtCore.QSize(225, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setKerning(False)
        self.ScoreQueryText.setFont(font)
        self.ScoreQueryText.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.ScoreQueryText.setAutoFillBackground(False)
        self.ScoreQueryText.setStyleSheet("   \n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid  rgb(180, 180, 180); /* 边框样式 */\n"
"font: 14pt \"微軟正黑體\";\n"
"")
        self.ScoreQueryText.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.ScoreQueryText.setObjectName("ScoreQueryText")
        self.horizontalLayout_2.addWidget(self.ScoreQueryText)
        self.btnScoreQuery = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.btnScoreQuery.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnScoreQuery.sizePolicy().hasHeightForWidth())
        self.btnScoreQuery.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setKerning(False)
        self.btnScoreQuery.setFont(font)
        self.btnScoreQuery.setStyleSheet("")
        self.btnScoreQuery.setObjectName("btnScoreQuery")
        self.horizontalLayout_2.addWidget(self.btnScoreQuery)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.LaoZuoText = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(225)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LaoZuoText.sizePolicy().hasHeightForWidth())
        self.LaoZuoText.setSizePolicy(sizePolicy)
        self.LaoZuoText.setMinimumSize(QtCore.QSize(0, 0))
        self.LaoZuoText.setMaximumSize(QtCore.QSize(225, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setKerning(False)
        self.LaoZuoText.setFont(font)
        self.LaoZuoText.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.LaoZuoText.setAutoFillBackground(False)
        self.LaoZuoText.setStyleSheet("   \n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid  rgb(180, 180, 180); /* 边框样式 */\n"
"font: 14pt \"微軟正黑體\";\n"
"")
        self.LaoZuoText.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.LaoZuoText.setObjectName("LaoZuoText")
        self.horizontalLayout_3.addWidget(self.LaoZuoText)
        self.btnLaoZuo = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.btnLaoZuo.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnLaoZuo.sizePolicy().hasHeightForWidth())
        self.btnLaoZuo.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setKerning(False)
        self.btnLaoZuo.setFont(font)
        self.btnLaoZuo.setStyleSheet("")
        self.btnLaoZuo.setObjectName("btnLaoZuo")
        self.horizontalLayout_3.addWidget(self.btnLaoZuo)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_6 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(225)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMinimumSize(QtCore.QSize(100, 0))
        self.label_6.setMaximumSize(QtCore.QSize(225, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setKerning(False)
        self.label_6.setFont(font)
        self.label_6.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_6.setAutoFillBackground(False)
        self.label_6.setStyleSheet("   \n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid  rgb(180, 180, 180); /* 边框样式 */\n"
"font: 14pt \"微軟正黑體\";\n"
"")
        self.label_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        self.btnFuWu = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.btnFuWu.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnFuWu.sizePolicy().hasHeightForWidth())
        self.btnFuWu.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setKerning(False)
        self.btnFuWu.setFont(font)
        self.btnFuWu.setStyleSheet("")
        self.btnFuWu.setObjectName("btnFuWu")
        self.horizontalLayout_6.addWidget(self.btnFuWu)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_7 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(225)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setMinimumSize(QtCore.QSize(100, 0))
        self.label_7.setMaximumSize(QtCore.QSize(225, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setKerning(False)
        self.label_7.setFont(font)
        self.label_7.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_7.setAutoFillBackground(False)
        self.label_7.setStyleSheet("   \n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid  rgb(180, 180, 180); /* 边框样式 */\n"
"font: 14pt \"微軟正黑體\";\n"
"")
        self.label_7.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_7.addWidget(self.label_7)
        self.btnCertMain = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.btnCertMain.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnCertMain.sizePolicy().hasHeightForWidth())
        self.btnCertMain.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.NoAntialias)
        self.btnCertMain.setFont(font)
        self.btnCertMain.setStyleSheet("    background-color: #fff;\n"
"    border: 1px solid  rgb(180, 180, 180);\n"
"font: 14pt \"微軟正黑體\";\n"
"    padding: 2px;")
        self.btnCertMain.setObjectName("btnCertMain")
        self.horizontalLayout_7.addWidget(self.btnCertMain)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_10 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(225)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setMinimumSize(QtCore.QSize(100, 0))
        self.label_10.setMaximumSize(QtCore.QSize(225, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setKerning(False)
        self.label_10.setFont(font)
        self.label_10.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_10.setAutoFillBackground(False)
        self.label_10.setStyleSheet("   \n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid  rgb(180, 180, 180); /* 边框样式 */\n"
"font: 14pt \"微軟正黑體\";\n"
"")
        self.label_10.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_10.addWidget(self.label_10)
        self.btnCertForeign = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.btnCertForeign.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnCertForeign.sizePolicy().hasHeightForWidth())
        self.btnCertForeign.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.NoAntialias)
        self.btnCertForeign.setFont(font)
        self.btnCertForeign.setStyleSheet("    background-color: #fff;\n"
"    border: 1px solid  rgb(180, 180, 180);\n"
"font: 14pt \"微軟正黑體\";\n"
"    padding: 2px;")
        self.btnCertForeign.setObjectName("btnCertForeign")
        self.horizontalLayout_10.addWidget(self.btnCertForeign)
        self.verticalLayout.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_11 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(225)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setMinimumSize(QtCore.QSize(100, 0))
        self.label_11.setMaximumSize(QtCore.QSize(225, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setKerning(False)
        self.label_11.setFont(font)
        self.label_11.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_11.setAutoFillBackground(False)
        self.label_11.setStyleSheet("   \n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid  rgb(180, 180, 180); /* 边框样式 */\n"
"font: 14pt \"微軟正黑體\";\n"
"")
        self.label_11.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_11.addWidget(self.label_11)
        self.btnSpeechEvent = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.btnSpeechEvent.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnSpeechEvent.sizePolicy().hasHeightForWidth())
        self.btnSpeechEvent.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.NoAntialias)
        self.btnSpeechEvent.setFont(font)
        self.btnSpeechEvent.setStyleSheet("")
        self.btnSpeechEvent.setObjectName("btnSpeechEvent")
        self.horizontalLayout_11.addWidget(self.btnSpeechEvent)
        self.verticalLayout.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_12 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(225)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setMinimumSize(QtCore.QSize(100, 0))
        self.label_12.setMaximumSize(QtCore.QSize(225, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setKerning(False)
        self.label_12.setFont(font)
        self.label_12.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_12.setAutoFillBackground(False)
        self.label_12.setStyleSheet("   \n"
"background-color: rgb(234, 234, 234);\n"
"border: 1px solid  rgb(180, 180, 180); /* 边框样式 */\n"
"font: 14pt \"微軟正黑體\";\n"
"")
        self.label_12.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_12.addWidget(self.label_12)
        self.pushButton_15 = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.pushButton_15.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_15.sizePolicy().hasHeightForWidth())
        self.pushButton_15.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.NoAntialias)
        self.pushButton_15.setFont(font)
        self.pushButton_15.setStyleSheet("")
        self.pushButton_15.setObjectName("pushButton_15")
        self.horizontalLayout_12.addWidget(self.pushButton_15)
        self.verticalLayout.addLayout(self.horizontalLayout_12)
        Graduation.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=Graduation)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 410, 22))
        self.menubar.setObjectName("menubar")
        Graduation.setMenuBar(self.menubar)

        self.retranslateUi(Graduation)
        QtCore.QMetaObject.connectSlotsByName(Graduation)

    def retranslateUi(self, Graduation):
        _translate = QtCore.QCoreApplication.translate
        Graduation.setWindowTitle(_translate("Graduation", "GUI"))
        self.ScoreQueryText.setText(_translate("Graduation", "學分"))
        self.btnScoreQuery.setText(_translate("Graduation", "佇列"))
        self.LaoZuoText.setText(_translate("Graduation", "勞作"))
        self.btnLaoZuo.setText(_translate("Graduation", "佇列"))
        self.label_6.setText(_translate("Graduation", "服務學習"))
        self.btnFuWu.setText(_translate("Graduation", "佇列"))
        self.label_7.setText(_translate("Graduation", "專業證照"))
        self.btnCertMain.setText(_translate("Graduation", "佇列"))
        self.label_10.setText(_translate("Graduation", "外語證照"))
        self.btnCertForeign.setText(_translate("Graduation", "佇列"))
        self.label_11.setText(_translate("Graduation", "非正式課程(演講)"))
        self.btnSpeechEvent.setText(_translate("Graduation", "佇列"))
        self.label_12.setText(_translate("Graduation", "[ex]"))
        self.pushButton_15.setText(_translate("Graduation", "0"))