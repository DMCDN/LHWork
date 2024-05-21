
from PyQt6 import QtCore, QtGui, QtWidgets 
from PyQt6.QtCore import *
from PyQt6.QtWidgets import QFileDialog, QMessageBox, QDockWidget, QListWidget
from PyQt6.QtGui import *

from GUI.Ui_Dialog_Society import Ui_Society


class Society(QtWidgets.QMainWindow, Ui_Society):
    def __init__(self, parent=None,lhuAuth=None):
        super(Society, self).__init__(parent)
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

        RecordDict=self.lhuAuth.getPage_Society() 
        self.loadingDialog.close()


        if RecordDict == False:
            tmp="查無Society資料"
        else:
            tmp=f"[FBI Warning]發生未處理的錯誤({RecordDict})"
        
        self.textBrowser.setText(f"""
        {tmp}

        """)
