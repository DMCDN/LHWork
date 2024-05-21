
from PyQt6 import QtCore, QtGui, QtWidgets 
from PyQt6.QtCore import *
from PyQt6.QtWidgets import QFileDialog, QMessageBox, QDockWidget, QListWidget
from PyQt6.QtGui import *
from GUI.Ui_Dialog_AbsendWarning import Ui_AbsendWarning

class AbsendWarning(QtWidgets.QMainWindow, Ui_AbsendWarning):
    def __init__(self, parent=None,lhuAuth=None):
        super(AbsendWarning, self).__init__(parent)
        self.setupUi(self)
        self.lhuAuth=lhuAuth
        self.startSearch()

    def startSearch(self):
        self.loadingDialog = QMessageBox(self)
        self.loadingDialog.setStyleSheet("QLabel{ color: white}")
        self.loadingDialog.setWindowTitle("查詢中......")
        self.loadingDialog.setText("查詢中.................")
        self.loadingDialog.show()

        self.AbsendWarningDict=self.lhuAuth.getPage_AbsendWarning() 
        self.loadingDialog.close()

        self.show()


        szTmpText=f'課程預警 |缺曠總節數|授課教師|科目名稱|\n'
        for key,val in self.AbsendWarningDict.items():
            if self.AbsendWarningDict[key]["szWarnText"] != "": #篩
                WarningText=self.AbsendWarningDict[key]["szWarnText"]
            else:
                WarningText= "None"
                szTmpText+=f'    {WarningText}   |          {self.AbsendWarningDict[key]["iAbsendNumTime"]}        |  {self.AbsendWarningDict[key]["szTeachName"]}   |{self.AbsendWarningDict[key]["szSubjectName"]}|\n'

        self.textBrowser.setText(szTmpText)

