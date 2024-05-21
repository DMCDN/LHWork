
from PyQt6 import QtCore, QtGui, QtWidgets 
from PyQt6.QtCore import *
from PyQt6.QtWidgets import QFileDialog, QMessageBox, QDockWidget, QListWidget
from PyQt6.QtGui import *

from GUI.Ui_Dialog_SpeechEvent import Ui_SpeechEvent


class SpeechEvent(QtWidgets.QMainWindow, Ui_SpeechEvent):
    def __init__(self, parent=None,lhuAuth=None):
        super(SpeechEvent, self).__init__(parent)
        self.setupUi(self)
        #self.action()


        
        self.lhuAuth=lhuAuth
        self.startSearch()

    def action(self):
        pass


    def startSearch(self):
        self.loadingDialog = QMessageBox(self)
        self.loadingDialog.setStyleSheet("QLabel{ color: white}")
        self.loadingDialog.setWindowTitle("查詢中......")
        self.loadingDialog.setText("查詢中.................")
        self.loadingDialog.show()

        RecordDict=self.lhuAuth.getPage_SpeechEvent() 
        self.loadingDialog.close()

        tmp=""
        print(RecordDict)

        if RecordDict:
            for i in RecordDict:
                tmp+=f"{i['類別']}：{i['目前審過次數']}/{i['需求次數']}(需求/已完成次數)\n"
        else:
            tmp=f"發生錯誤({RecordDict})"
        
        self.textBrowser.setText(f"""
        {tmp}

        """)
 