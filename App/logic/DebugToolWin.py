
from PyQt6 import QtCore, QtGui, QtWidgets 
from PyQt6.QtCore import *
from PyQt6.QtWidgets import QFileDialog, QMessageBox, QDockWidget, QListWidget
from PyQt6.QtGui import *

from GUI.Ui_debugTool import Ui_debugTool
import os,sys

import logging
import json


logger = logging.getLogger()

class DebugTool(QtWidgets.QMainWindow, Ui_debugTool):
    def __init__(self, parent=None,lhuAuth=None):
        super(DebugTool, self).__init__(parent)
        self.setupUi(self)
        self.action()
        self.lhuAuth=lhuAuth
        self.LogLevel= 0 # 0 Error 1 Debug

        #
        self.loadingDialog = QMessageBox(self)
        self.loadingDialog.setStyleSheet("QLabel{ color: white}")
        

    def action(self):
        self.btnTracebackTest.clicked.connect(self.btnTracebackTest_OnClick)
        self.btnDumpAllPage.clicked.connect(self.btnDumpAllPage_OnClick)
        self.btnOpenLogPath.clicked.connect(self.btnOpenLogPath_OnClick)
        self.btnLoggerDebugMode.clicked.connect(self.btnLoggerDebugMode_OnClick)
        self.btnDumpScoreData.clicked.connect(self.btnDumpScoreData_OnClick)


    def btnTracebackTest_OnClick(self):
        print(os.path.basename(sys.argv[0]))
        0/0

    def btnDumpAllPage_OnClick(self):
        self.loadingDialog.setWindowTitle("devDumpAllPage")
        self.loadingDialog.setText("載入中.................")
        self.loadingDialog.show()
        self.lhuAuth.devDumpAllPage()
        self.loadingDialog.setText("完成!")
        #print(os.path.join(os.path.dirname(os.path.abspath(__name__)),"dump.bytes"))
        #os.system(f'start {os.path.join(os.path.dirname(os.path.abspath(__name__)),"dump.bytes")}')

    def btnOpenLogPath_OnClick(self):
        print(os.path.join(os.path.dirname(os.path.abspath(__name__)),"errorLog.log"))
        os.system(f'explorer.exe "{os.path.join(os.path.dirname(os.path.abspath(__name__)),"errorLog.log")}"')

    def btnLoggerDebugMode_OnClick(self):
        # 0 Error 1 Debug
        #Error->Debug
        if self.LogLevel == 0 :
            self.LogLevel = 1
            self.btnLoggerDebugMode.setText(f'切換Log層級(目前：Debug)')
            logger.setLevel(logging.DEBUG)
        elif self.LogLevel == 1 :
            self.LogLevel = 0
            self.btnLoggerDebugMode.setText(f'切換Log層級(目前：Error)')
            logger.setLevel(logging.ERROR)
        self.loadingDialog.setWindowTitle("DebugMode")
        self.loadingDialog.setText("切換完成")
        self.loadingDialog.show()
    
    def btnDumpScoreData_OnClick(self):

        with open('ScoreQuery_Global.json', 'w', encoding='utf-8') as json_file:
            json_file.write(json.dumps(self.lhuAuth.getGlobalScoreData(), ensure_ascii=False, indent=4))
        with open('ScoreQuery_User.json', 'w', encoding='utf-8') as json_file:
            json_file.write(json.dumps(self.lhuAuth.getScoreQueryDataV2(), ensure_ascii=False, indent=4))

        self.loadingDialog.setWindowTitle("DumpScoreData")
        self.loadingDialog.setText("DumpScoreData Done")
        self.loadingDialog.show()
    